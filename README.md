# Django ToDo App

A simple **Django-based ToDo application** that allows users to manage their daily tasks. This project demonstrates CRUD operations, task completion tracking, and a clean UI layout using **Bootstrap**.

> Built as a hands-on project to practice Django fundamentals, task management, and UI integration.

---

## Features

- Add, update, and delete tasks
- Mark tasks as completed
- View tasks in two sections: **ToDo** (left) and **Completed** (right)
- Responsive UI using **Bootstrap**
- Displays the current date
- Single-page UI with a separate page for updating tasks

---

## Tech Stack

- Python 3.x
- Django 4.x
- SQLite (default Django database)
- Bootstrap 5

---

## Installation

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd ToDo
```

2. **Create and activate a virtual environment (recommended)**
   python -m venv venv

# Linux/Mac

source venv/bin/activate

# Windows

venv\Scripts\activate

3. **Install Django**

```bash
pip install django
```

3. **Apply database migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

## Running the Project

Start the Django development server:

```bash
python manage.py runserver
```

Open your browser and go to:

```bash
http://127.0.0.1:8000/
```

## Project Structure

```bash
ToDo/
│── manage.py
│── db.sqlite3
│── todo_main/          # Main Django app
│── todo/               # Secondary app (if used)
│── templates/          # HTML templates
│── venv/               # Virtual environment
│── README.md
│── LICENSE
```

How It Works

1. Add a Task: Use the input field and click Add.
2. Mark as Completed: Click the check button on a task.
3. Update a Task: Click the pencil icon, edit on the new page, then click Update.
4. Delete a Task: Click the trash icon.
   Tasks automatically appear in the correct section based on their completion status.

## Future Improvements

- Add user authentication (login/register)
- Allow due dates and reminders
- Add task prioritization
- Implement drag-and-drop UI for better task management
