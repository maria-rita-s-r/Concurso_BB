import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///inscricoes.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configurações do Servidor de E-mail (Substitua pelas credenciais reais do seu SMTP)
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.example.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'seu_usuario@example.com')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'sua_senha')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'noreply@example.com')
    