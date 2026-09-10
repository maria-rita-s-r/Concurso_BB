from flask import Blueprint, request, jsonify
from modelos import db, Inscrito
from flask_mail import Message
import re

inscricao_bp = Blueprint('inscricao', __name__)

@inscricao_bp.route('/api/inscricoes', methods=['POST'])
def realizar_inscricao():
    dados = request.get_json()

    if not dados:
        return jsonify({"success": False, "message": "Dados inválidos ou ausentes."}), 400

    nome = dados.get('nome')
    telefone = dados.get('telefone')  # Processado em memória, mas não persistido
    email = dados.get('email')

    if not nome or not email:
        return jsonify({"success": False, "message": "Os campos nome e e-mail são obrigatórios."}), 400

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({"success": False, "message": "Endereço de e-mail inválido."}), 400

    if Inscrito.query.filter_by(email=email).first():
        return jsonify({"success": False, "message": "Este e-mail já realizou inscrição."}), 400

    try:
        novo_inscrito = Inscrito(nome=nome, email=email)
        db.session.add(novo_inscrito)
        db.session.commit()

        from app import mail
        msg = Message(
            subject="Confirmação de inscrição",
            recipients=[email]
        )
        msg.body = f"""Olá, {nome},
            Agradecemos por realizar sua inscrição.
            Para que sua inscrição seja efetivamente confirmada, será necessário realizar a validação dos dados informados por meio do link disponibilizado abaixo.

            Link para confirmação:
            https://www.siteoficial.com/video-confirmacao

            Solicitamos que a confirmação seja realizada seguindo as orientações apresentadas no conteúdo disponibilizado.
            Em caso de dúvidas ou dificuldades durante o processo de confirmação, entre em contato com nossa equipe responsável.

            Atenciosamente,
            Equipe responsável pela inscrição"""

        mail.send(msg)

        return jsonify({
            "success": True,
            "message": "Inscrição realizada com sucesso."
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "message": "Falha ao processar a inscrição ou enviar o e-mail."}), 500