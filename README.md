ask Management REST API

Project Overview
----------------
Ye ek simple REST API hai jo task management ke liye banaya gaya hai.
Isme Users, Projects, aur Tasks manage kar sakte ho with support for task dependencies.

Technologies Used
-----------------
- Python 3.x
- Flask
- Flask-SQLAlchemy
- PostgreSQL
- psycopg2-binary

Setup Instructions
------------------

1. Clone the Repository
   --------------------
   git clone https://github.com/Anjalikhare99/Task_Management_System.git
   cd Task_Management_System

2. Install Dependencies
   --------------------
   pip install -r requirements.txt

   Agar requirements.txt nahi hai toh:
   pip install Flask Flask-SQLAlchemy psycopg2-binary

3. Configure Database
   -------------------
   - Make sure PostgreSQL installed and running.
   - Create database named 'task_db':
     createdb task_db

   - Update config.py with your PostgreSQL credentials:
     SQLALCHEMY_DATABASE_URI = "postgresql://<username>:<password>@localhost/task_db"

4. Initialize Database Tables
   --------------------------
   Run custom Flask CLI command to create tables:
   flask create-db

5. (Optional) Seed Sample Data
   ----------------------------
   python seed.py

6. Run the Flask Application
   --------------------------
   flask run

   Ya agar run.py se start karte ho:
   python run.py

7. Access Base URL
   ----------------
   http://127.0.0.1:5000/

API Endpoints
-------------

Users
-----
Method   Endpoint        Description
POST     /users/         Create a new user
GET      /users/         List all users
GET      /users/<id>     Get user by ID

Projects
--------
Method   Endpoint              Description
POST     /projects/            Create a new project
GET      /projects/            List all projects
GET      /projects/<id>        Get project by ID
GET      /projects/<id>/tasks  List tasks under a project

Tasks
-----
Method   Endpoint                   Description
POST     /tasks/                   Create a new task
GET      /tasks/<id>               Get task details by ID
PATCH    /tasks/<id>/status        Update task status (checks dependencies)
GET      /tasks/user/<user_id>     List tasks assigned to a user
GET      /tasks/status/<status>    List tasks filtered by status (e.g. pending)

Notes
-----
- Task status can only be updated if all dependencies are completed.
- Proper HTTP status codes and error messages are returned.
- Relationships:
  * Users have multiple tasks.
  * Projects have multiple tasks.
  * Tasks can depend on multiple other tasks.

Troubleshooting
---------------
- Ensure PostgreSQL server is running.
- Double-check config.py for correct DB URI.
- Use Postman or curl to test endpoints.
- For 404 errors, confirm the URL and blueprint prefixes.

Contact
-------
Agar koi issue aaye toh mujhe bata dena ya code me comments check kar lena.

Happy coding! 🚀