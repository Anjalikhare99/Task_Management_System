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
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    pagination = User.query.paginate(page=page, per_page=per_page, error_out=False)
    users = pagination.items

    return jsonify({
        "users": [{"id": u.id, "name": u.name, "email": u.email} for u in users],
        "total": pagination.total,
        "page": pagination.page,
        "pages": pagination.pages
    })

@bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({"id": user.id, "name": user.name, "email": user.email})
