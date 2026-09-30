# FastAPI To-Do API

A RESTful To-Do API built with **FastAPI, SQLAlchemy, and PostgreSQL**. This project was created to practice backend development and CRUD operations.

## Features

- Create, read, update, and delete todos
- PostgreSQL database
- Pydantic data validation
- SQLAlchemy ORM
- Automatic API documentation

## Technologies

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Uvicorn

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/todos` | Get all todos |
| GET | `/todo/{id}` | Get a todo |
| POST | `/todo` | Create a todo |
| PUT | `/todo/{id}` | Update a todo |
| DELETE | `/todo/{id}` | Delete a todo |

## Setup

```bash
git clone https://github.com/CesarSoto20/fastAPI-To-Do.git
cd fastAPI-To-Do

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
