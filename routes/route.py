from flask import Flask, request, jsonify
from app import app
from models.book import Book
from controllers.controllers import save_book, read_book
books = []
book_id_control = 1

# ADD A BOOK
@app.route("/books", methods = ["POST"])
def add_book():
    global book_id_control
    data = request.get_json() 
    new_book = Book(id = book_id_control, title = data["title"], author = data["author"], isbn = data["isbn"], publication_year = data["publication_year"], genre = data["genre"], available = ["available"])
    book_id_control += 1
    books.append(new_book)
    print(books)
    
    # --- ADD BOOK IN JSON ---
    books_to_save = [book.to_dict() for book in books]
    save_book(books_to_save)
    
    return jsonify({
        "message" : "BOOK SUCESSFULLY ADDED", "id" : new_book.id}), 201
    
# READ THE JSON DATABASE
@app.route("/books", methods = ["GET"])
def get_books():
    book_list = [book.to_dict() for book in books]
    print([])
    output = {
        "book" : book_list,
        "books_total" : len(book_list)
    }
    print([])
    return jsonify(output), 201

# GET A SPECIFIC BOOK
@app.route("/books/<int:id>", methods = ["GET"])
def get_book(id):
    for book in books:
        if book.id == id:
            return jsonify(book.to_dict())
    
    return jsonify(
        {"message" : "BOOK NOT FOUND"}
        ) , 404


# UPDATE A BOOK
@app.route("/books/<int:id>", methods = ["PUT"])
def update_book(id):
    book = None
    for book in books:
        if book.id == id:
            book = book
            break
    print(book)        
    if book == None:
        return jsonify({"message" : "BOOK NOT FOUND"}), 404
        
    data = request.get_json()
    book.title = data["title"]
    book.author = data["author"]
    book.isbn = data["isbn"]
    book.publication_year = data["publication_year"]
    book.genre = data["genre"]
    book.available = data["available"]
    save_book([book.to_dict() for book in books])
    print(book)
    return jsonify({"message" : "BOOK UPDATED SUCESSFULLY😁👌"})

@app.route("/books/<int:id>", methods = ["DELETE"])
def delete_book(id):
    book = None
    
    for book in books:
        if book.id == id:
            book = book
            break
    if book == None:
        return jsonify({"message" : "BOOK NOT FOUND"}), 404
    
    deleted_book = books.remove(book)
    print(f"DELETED BOOK: {deleted_book}")
    for index, book in enumerate(books):
        book.id = index + 1
    
    save_book([book.to_dict() for book in books])
    return jsonify({
        "message" : "BOOK SUCESSFULLY REMOVED",
        "book" : [book.to_dict() for book in books]})