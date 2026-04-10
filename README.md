# Week 3 - Task Management System

## Overview

This project is a Task Management System built using Flask. It includes user authentication, task management features, frontend integration, and database support using SQLite.


## Features

* User Registration and Login
* Create, Read, Update, Delete (CRUD) Tasks
* Frontend UI using HTML and JavaScript
* Backend APIs using Flask
* Data storage using SQLite database
* API testing using Postman


## Technology Used

* Python
* Flask
* SQLite
* HTML
* JavaScript
* Postman
* GitHub


## Project Structure

week3-task-management/
app.py
models/
 db.py
 user.py
 task.py
routes/
 auth_routes.py
 task_routes.py
templates/
 index.html
requirements.txt
README.md


## How to Run

1. Install Flask
   pip install flask

2. Run the application
   python app.py

3. Open browser
   http://127.0.0.1:5000


## API Endpoints

### Authentication

POST /register
POST /login

### Task Management

POST /tasks
GET /tasks
PUT /tasks/<id>
DELETE /tasks/<id>


## Concepts Covered

* REST API development
* CRUD operations
* Authentication
* Frontend and backend integration
* Database integration using SQLite
* Error handling


## Outcome

This project demonstrates building a full-stack application with backend, frontend, and database integration. It improves practical development skills and real-world problem solving.
