from flask import Blueprint, request, jsonify
from app.models import db, Task, Project, User

bp = Blueprint("tasks", __name__, url_prefix="/tasks")

@bp.route("/", methods=["POST"])
def create_task():
    data = request.get_json()
    title = data.get("title")
    description = data.get("description")
    status = data.get("status", "pending")
    project_id = data.get("project_id")
    user_id = data.get("user_id")

    if not title or not project_id:
        return jsonify({"error": "Title and project_id are required"}), 400

    project = Project.query.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    if user_id:
        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "Assigned user not found"}), 404

    task = Task(
        title=title,
        description=description,
        status=status,
        project_id=project_id,
        user_id=user_id
    )
    db.session.add(task)
    db.session.commit()

    return jsonify({
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "status": task.status,
        "project_id": task.project_id,
        "user_id": task.user_id
    }), 201

@bp.route("/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return jsonify({
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "status": task.status,
        "project_id": task.project_id,
        "user_id": task.user_id
    })


@bp.route("/<int:task_id>/status", methods=["PATCH"])
def update_task_status(task_id):
    data = request.get_json()
    new_status = data.get("status")
    if not new_status:
        return jsonify({"error": "Status is required"}), 400

    task = Task.query.get_or_404(task_id)

    for dep in task.dependencies:
        if dep.status != "completed":
            return jsonify({"error": f"Cannot update status. Dependency task {dep.id} is not completed."}), 400

    task.status = new_status
    db.session.commit()

    return jsonify({
        "id": task.id,
        "status": task.status
    })

@bp.route("/user/<int:user_id>", methods=["GET"])
def list_tasks_by_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    pagination = Task.query.filter_by(user_id=user.id).paginate(page=page, per_page=per_page, error_out=False)
    tasks = pagination.items

    result = []
    for t in tasks:
        result.append({
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "status": t.status,
            "project_id": t.project_id,
            "dependencies": [d.id for d in t.dependencies]
        })

    return jsonify({
        "tasks": result,
        "total": pagination.total,
        "page": pagination.page,
        "pages": pagination.pages
    })

@bp.route("/status/<string:status>", methods=["GET"])
def list_tasks_by_status(status):
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    pagination = Task.query.filter_by(status=status).paginate(page=page, per_page=per_page, error_out=False)
    tasks = pagination.items

    result = []
    for t in tasks:
        result.append({
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "user_id": t.user_id,
            "project_id": t.project_id,
            "dependencies": [d.id for d in t.dependencies]
        })

    return jsonify({
        "tasks": result,
        "total": pagination.total,
        "page": pagination.page,
        "pages": pagination.pages
    })