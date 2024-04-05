from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data for books
books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951}
]

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    query = request.args.get('query', '')
    results = [book for book in books if query.lower() in book['title'].lower() or query.lower() in book['author'].lower()]
    return jsonify(results)

@app.route('/book/<int:index>')
def book(index):
    if 0 <= index < len(books):
        book = books[index]
        return render_template('book.html', book=book)
    else:
        return "Book not found"

if __name__ == '__main__':
    app.run(debug=True)
