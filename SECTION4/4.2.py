from flask import Flask, jsonify, request

app = Flask(__name__)


users = []
next_id = 1


def make_response(status=True, data=None, message=""):
    return jsonify({"status": status, "data": data, "message": message})


@app.route("/users", methods=["GET"])
def get_users():
    return make_response(data=users, message="Список користувачів")


@app.route("/users", methods=["POST"])
def create_user():
    global next_id
    data = request.json
    if not data or "name" not in data or "email" not in data:
        return make_response(status=False, message="Введіть name і email"), 400
    user = {"id": next_id, "name": data["name"], "email": data["email"]}
    users.append(user)
    next_id += 1
    return make_response(data=user, message="Користувач створений"), 201


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return make_response(status=False, message="Користувача не знайдено"), 404
    return make_response(data=user)


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return make_response(status=False, message="Користувача не знайдено"), 404
    data = request.json
    user["name"] = data.get("name", user["name"])
    user["email"] = data.get("email", user["email"])
    return make_response(data=user, message="Користувач оновлений")


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return make_response(status=False, message="Користувача не знайдено"), 404
    users = [u for u in users if u["id"] != user_id]
    return make_response(message="Користувач видалений")

if __name__ == "__main__":
    app.run(debug=True)
