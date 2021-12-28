# Overview
Project for todo app

## Structure

```bash
.
├── README.md
├── backend
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── todo.db
├── docker-compose.yml
└── frontend
    ├── Dockerfile
    ├── __pycache__
    │   └── app.cpython-39.pyc
    ├── app.py
    ├── requirements.txt
    └── templates
        ├── create.html
        ├── detail.html
        ├── index.html
        └── update.html

4 directories, 14 files
```

# Features
This app is able to use below function.

## User Story
- Add a task.
- Check detail of tasks.
- See the list of tasks.
- Delete tasks.
- Change status of task.
- Edit tasks.

# Using of language, framework, technology
- Python
- HTML/CSS
- Flask
- Docker compose
- SQLite3
- SQLAlchemy
  
# Requirement
- Python==3.9
- Flask==2.0.2
- flask-marshmallow==0.14.0
- Flask-SQLAlchemy==2.5.1
- requests==2.26.0
- WTForms==3.0.0
 
# Installation
 
```bash
$ git clone https://github.com/hinatha/Flask-SQLite.git
```
 
# Usage
 
```bash
$ docker-compose up
```
 
# Future plans
- Convert DB to MySQL
