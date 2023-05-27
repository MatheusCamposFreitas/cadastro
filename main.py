from flask import Flask

from controllers.user_controller import user_blueprint

app = Flask(__name__)

# Registrar os blueprints das rotas
app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run(debug=True)