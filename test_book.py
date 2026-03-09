import pytest, requests as req

# CRUD
BASE_URL = 'http://127.0.0.1:5000'
books = []
# CREATE

def test_add_book():
    book = {
        "title" : "ARE YOU OKAY I",
        "author" : "Pandoro Gama",
        "isbn" : "1234756867",
        "publication_year" : "2026-11-9",
        "genre" : "Action",
        "available" : False
    }
    
    #URL/endpoint, json = book
    response = req.post(f"{BASE_URL}/books", json = book)
    assert response.status_code == 201
    
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    books.append(response.json()['id'])
    
# READ

def test_get_books():
    response = req.get(f"{BASE_URL}/books")
    assert response.status_code == 201
    response_json = response.json()
    
    assert "book" in response_json
    assert "books_total" in response_json
    
    
# SPECIFIC BOOK

def test_get_book():
    if books:
        book_id = books[0]
        response = req.get(f"{BASE_URL}/books/{book_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert book_id == response_json['id']
        
        
# UPDATE

def test_update_boook():
    if books:
        book_id = books[0]
        payload = {
        "title" : "ARE YOU OKAY II",
        "author" : "Pandoro Fortes",
        "isbn" : "123456789",
        "publication_year" : "2026-12-30",
        "genre" : "Action",
        "available" : True
        }
        response = req.put(f"{BASE_URL}/books/{book_id}", json = payload)
        response.status_code == 200
        response_json = response.json()
        assert "message" in response_json
        
        # NEW REQUEST TO A SPECIFIC BOOK
        response = req.get(f"{BASE_URL}/books/{book_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json['title'] == payload['title']
        assert response_json['author'] == payload['author']
        assert response_json['isbn'] == payload['isbn']
        assert response_json['publication_year'] == payload['publication_year']
        assert response_json['genre'] == payload['genre']
        assert response_json['available'] == payload['available']
# def test_delete_book():
#     if  books:
#         book_id = books[0]
#         response = req.delete(f"{BASE_URL}/books/{book_id}")
#         response.status_code == 200
        
#         response = req.get(f"{BASE_URL}/books/{book_id}")
#         assert response.status_code == 404