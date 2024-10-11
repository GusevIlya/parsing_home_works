from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
db = client['books']
book_info = db.book_info

with open('books.json', 'r') as f:
    data = json.load(f)

for book in data:
    book_info.insert_one(book)

for book in book_info.find({'price': {'$lt': 11}}):
    print(book)
