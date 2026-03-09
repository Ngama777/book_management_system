import json
import os

JSON_PATH = os.path.join('data', 'book.json')

def read_book():
    if not os.path.exists(JSON_PATH):
        return []
    with open(JSON_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_book(dados):
    os.makedirs('data', exist_ok=True) # Cria a pasta data se não existir
    with open(JSON_PATH, 'w', encoding='utf-8') as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)

# def reed_book():
#     return read_book()

def add_book(data):
    books = read_book()
    # GENERATE AUTOMATIC ID
    new_id = books[-1]["id"] + 1 if books else 1
    data["id"] = new_id
    books.append(data)
    save_book[books]
    return data

def delete_book(id):
    books = read_book()
    orginial_len = len(books)
    books = [book for book in books if books["id"] != id]
    if len(books) < orginial_len:
        save_book(books)
        return True
    return False