from app import create_app, db
from app.models import User, Project, Task

app = create_app()

with app.app_context():
    # Drop all tables and recreate (optional, if you want fresh start)
    db.drop_all()
    db.create_all()

    # Create sample users
    user1 = User(name="Alice", email="alice@example.com")
    user2 = User(name="Bob", email="bob@example.com")

    # Create sample projects
    project1 = Project(name="Project Alpha", description="First project")
    project2 = Project(name="Project Beta", description="Second project")

    # Add users and projects to session
    db.session.add_all([user1, user2, project1, project2])
    db.session.commit()

    # Create sample tasks
    task1 = Task(
        title="Task One",
        description="Complete the first task",
        status="pending",
        user_id=user1.id,
        project_id=project1.id
    )

    task2 = Task(
        title="Task Two",
        description="Complete the second task",
        status="pending",
        user_id=user2.id,
        project_id=project2.id
    )

    db.session.add_all([task1, task2])
    db.session.commit()

    print("Seed data inserted successfully.")
