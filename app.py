from flask import Flask, render_template
from config import Config
from modelos import db
from rotas_inscr import inscricao_bp
from rotas_menu import menu_bp
from flask_mail import Mail

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)

    app.register_blueprint(inscricao_bp)
    app.register_blueprint(menu_bp)

    # Rota principal adicionada corretamente para carregar o index.html e o CSS
    @app.route('/')
    def index():
        return render_template('index.html')

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)