from flask import Blueprint, request, jsonify
from app.models import db, Project, Task

bp = Blueprint("projects", __name__, url_prefix="/projects")

@bp.route("/", methods=["POST"])
def create_project():
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")

    if not name:
        return jsonify({"error": "Project name is required"}), 400

    project = Project(name=name, description=description)
    db.session.add(project)
    db.session.commit()

    return jsonify({"id": project.id, "name": project.name, "description": project.description}), 201

@bp.route("/", methods=["GET"])
def list_projects():
    projects = Project.query.all()
    result = []
    for p in projects:
        result.append({
            "id": p.id,
            "name": p.name,
            "description": p.description
        })
    return jsonify(result)

@bp.route("/<int:project_id>/tasks", methods=["GET"])
def list_tasks_under_project(project_id):
    project = Project.query.get_or_404(project_id)
    tasks = Task.query.filter_by(project_id=project.id).all()

    task_list = []
    for t in tasks:
        task_list.append({
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "status": t.status,
            "user_id": t.user_id
        })
    return jsonify(task_list)

@bp.route("/<int:project_id>", methods=["GET"])
def get_project(project_id):
    project = Project.query.get_or_404(project_id)
    return jsonify({
        "id": project.id,
        "name": project.name,
        "description": project.description
    })