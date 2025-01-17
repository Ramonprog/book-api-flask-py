from flask import Flask
from flask_migrate import Migrate
from db import db
from models.book import Book

app = Flask(__name__)

@app.route('/')
def hello():
  return 'Api is live'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/books'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')


"""
comandos para iniciar o banco de dados
flask db init
flask db migrate -m 'nome da migração'

depois do migration ele entende que tem um modelo e tem que fazer o upgrade
para fazer a transação
flask db upgrade
"""
