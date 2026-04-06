# Working with API's in Flask

# import libraries
from flask import Flask, jsonify, request 


app = Flask(__name__)


# Initial data in to do list

items = [
    {'id': 1, 'name': 'item1', 'description': 'This is item 1'},
    {'id': 2, 'name': 'item2', 'description': 'This is item 2'},
    {'id': 3, 'name': 'item3', 'description': 'This is item 3'}
]

@app.route('/')
def home():
    return "Welcome to To Do List App"

# GET: Retrieve all items in the to do list
@app.route('/items', methods = ['GET'])
def get_items():
    return jsonify(items)

# Get : Retrieve a specific item by id
@app.route('/items/<int:id>', methods = ['GET'])
def get_item(id):
    item = next((item for item in items if item['id'] == id), None)
    if item is None:
        return jsonify({'message': 'Item not found'})
    return jsonify(item)

# POST: Create a new item in the to do list - Working with API's in Flask (Postman)
@app.route('/items', methods = ['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        return jsonify({'message': 'Name is required'})
    new_item = {
        'id': items[-1]['id'] + 1 if items else 1,
        'name': request.json['name'],
        'description': request.json('description')
    }
    items.append(new_item)
    return jsonify(new_item)

# PUT: Update an existing item in the to do list
@app.route('/items/<int:id>',methods = ['PUT'])
def update_item(id):
    item = next((item for item in items if item['id'] == id), None)
    if item is None:
        return jsonify({'message': 'Item not found'})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)


 # DELETE: Delete an item from the to do list
@app.route('/items/<int:id>', methods = ['DELETE'])
def delete_item(id):
    global items
    items = [item for item in items if item['id'] != id]
    return jsonify({'message': 'Item deleted'})

if __name__ == '__main__':
    app.run(debug=True)