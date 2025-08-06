from flask import Flask, request, jsonify

app = Flask(_name_)

# In-memory user store
users = {}

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify({user_id: user}), 200
    return jsonify({"error": "User not found"}), 404

# POST - create a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = data.get("id")
    name = data.get("name")

    if not user_id or not name:
        return jsonify({"error": "ID and Name required"}), 400

    if user_id in users:
        return jsonify({"error": "User already exists"}), 409

    users[user_id] = name
    return jsonify({"message": "User added"}), 201

# PUT - update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data.get("name")

    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    users[user_id] = name
    return jsonify({"message": "User updated"}), 200

# DELETE - remove a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    del users[user_id]
    return jsonify({"message": "User deleted"}), 200

if _name_ == '_main_':
    app.run(debug=True)
