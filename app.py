from flask import Flask, request, jsonify
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

@app.route('/books', methods=['POST'])
def add_book():
   data = request.get_json()
   newBook = Book(title=data['title'], author=data['author'], description=data['description'])
   db.session.add(newBook)
   db.session.commit()
   return jsonify({'message': 'Book added successfully'}), 201

@app.route('/books', methods=['GET'])
def get_all_books():
   books = Book.query.all()
   return jsonify([books.to_dict() for books in books]), 200

@app.route('/books/<book_id>', methods=['GET'])
def get_one_book(book_id):
   book = Book.query.get_or_404(book_id)
   return jsonify(book.to_dict())

@app.route('/books/<book_id>', methods=['PATCH'])
def update_book(book_id):
  book = Book.query.get_or_404(book_id)
  data = request.get_json()
  for key, value in data.items():
      setattr(book, key, value)

  db.session.commit()
    
  return jsonify({'message': 'Livro atualizado com sucesso'})

@app.route('/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
  book = Book.query.get_or_404(book_id)
  db.session.delete(book)
  db.session.commit()
  return jsonify({'message': 'livro removido com sucesso'})
   

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
