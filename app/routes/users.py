from flask import Blueprint, request, jsonify
from app.models import db, User

bp = Blueprint("users", __name__, url_prefix="/users")

@bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data.get("email") or not data.get("name"):
        return jsonify({"error": "Missing required fields"}), 400
    user = User(name=data["name"], email=data["email"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"id": user.id, "name": user.name}), 201

@bp.route("/", methods=["GET"])
def list_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])

@bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({"id": user.id, "name": user.name, "email": user.email})
