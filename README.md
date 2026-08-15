# 🚀 Smart TaskFlow API

A clean, production-oriented REST API for personal task management. Smart TaskFlow provides secure user authentication, task CRUD operations, categories, filtering, pagination, automatic OpenAPI documentation, and a simple SQLite default setup.

> Built with FastAPI, SQLAlchemy, Pydantic, JWT, and SQLite/PostgreSQL compatibility.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Overview

Smart TaskFlow API is the backend foundation for a task management application. It handles user accounts, authentication, tasks, priorities, statuses, categories, pagination, filtering, and data validation through a documented REST API.

The default setup uses SQLite so the project can run locally without installing a database server. The database URL can be changed to PostgreSQL through environment variables when the application is deployed.

## What the API does

- Registers new users with validated email and password data.
- Authenticates users and returns a JWT access token.
- Protects private endpoints with token-based authentication.
- Creates, lists, reads, updates, and deletes tasks.
- Filters tasks by status and priority.
- Paginates task results for efficient client requests.
- Creates and manages task categories.
- Generates interactive Swagger and ReDoc documentation automatically.

## Technology stack

| Layer | Technology |
|---|---|
| API framework | FastAPI |
| Language | Python |
| Database access | SQLAlchemy ORM |
| Validation | Pydantic |
| Authentication | JWT |
| Password hashing | bcrypt through Passlib |
| Default database | SQLite |
| Production database option | PostgreSQL |
| API documentation | OpenAPI, Swagger UI, ReDoc |

## API workflow

```text
Register user
     ↓
Login and receive JWT token
     ↓
Authorize protected requests
     ↓
Create and manage tasks
     ↓
Filter, update, or complete tasks
```

## Project structure

```text
smart-taskflow-api/
├── main.py                 # Creates the FastAPI application
├── config.py               # Loads application settings from environment variables
├── database.py             # Creates the SQLAlchemy engine and database sessions
├── models/                 # Defines User, Task, and Category database models
│   ├── __init__.py
│   ├── user.py
│   └── task.py
├── schemas/                # Defines validated API request and response models
│   ├── __init__.py
│   ├── user.py
│   └── task.py
├── routers/                # Groups the API endpoints by feature
│   ├── __init__.py
│   ├── auth.py             # Registration, login, and current user
│   ├── tasks.py            # Task CRUD, filters, and pagination
│   └── categories.py       # Category endpoints
├── utils/                  # Shared security and dependency functions
│   ├── __init__.py
│   ├── security.py
│   └── dependencies.py
├── assets/                 # Screenshots and documentation assets
├── requirements.txt        # Python dependencies
├── .env.example            # Safe environment variable template
├── .gitignore              # Files excluded from Git
├── CONTRIBUTING.md         # Contribution guidelines
├── LICENSE                 # MIT license
└── README.md               # Project documentation
```

## Quick start

### Windows PowerShell

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
python -m uvicorn main:app --reload
```

### macOS or Linux

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
python -m uvicorn main:app --reload
```

## Local URLs

After starting the server:

| Resource | URL |
|---|---|
| API root | [127.0.0.1:8000](http://127.0.0.1:8000) |
| Health check | [127.0.0.1:8000/health](http://127.0.0.1:8000/health) |
| Swagger UI | [127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) |
| ReDoc | [127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) |

## Authentication

The protected task and category endpoints require a JWT token.

1. Call `POST /api/auth/register` to create an account.
2. Call `POST /api/auth/login` with the same credentials.
3. Copy the `access_token` from the response.
4. Click **Authorize** in Swagger UI.
5. Enter the token and call the protected endpoints.

## Main endpoints

| Area | Method | Endpoint | Description |
|---|---:|---|---|
| Authentication | POST | `/api/auth/register` | Create a user account |
| Authentication | POST | `/api/auth/login` | Authenticate and receive a JWT token |
| Authentication | GET | `/api/auth/me` | Return the authenticated user |
| Tasks | GET | `/api/tasks/` | List tasks with filters and pagination |
| Tasks | POST | `/api/tasks/` | Create a task |
| Tasks | GET | `/api/tasks/{task_id}` | Return one task |
| Tasks | PUT | `/api/tasks/{task_id}` | Update a task |
| Tasks | DELETE | `/api/tasks/{task_id}` | Delete a task |
| Categories | GET | `/api/categories/` | List categories |
| Categories | POST | `/api/categories/` | Create a category |
| Categories | DELETE | `/api/categories/{category_id}` | Delete a category |

## Example payloads

### Register a user

```json
{
  "username": "demo_user",
  "email": "demo@example.com",
  "password": "secure-password-123"
}
```

### Create a task

```json
{
  "title": "Review API documentation",
  "description": "Check the README and endpoint examples",
  "status": "pending",
  "priority": "high"
}
```

## Configuration

Copy `.env.example` to `.env` and set a long random secret:

```env
DATABASE_URL=sqlite:///./tasks.db
SECRET_KEY=replace-with-a-long-random-secret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DEBUG=True
```

Never commit `.env`, passwords, tokens, virtual environments, or local database files.

## Testing and verification

Compile the main Python modules before committing:

```powershell
python -m py_compile config.py database.py main.py
```

Verify that the health endpoint returns a healthy response:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

## Security notes

- Passwords are stored as bcrypt hashes, never as plain text.
- JWT tokens protect authenticated endpoints.
- Pydantic validates incoming request data.
- SQLAlchemy provides parameterized ORM queries.
- Secrets and local databases are excluded through `.gitignore`.

## Roadmap

- Add a complete pytest test suite.
- Add Alembic migrations.
- Add role-based authorization.
- Add Docker and Docker Compose deployment.
- Add a responsive frontend dashboard.
- Add task search and sorting.
- Add due-date reminders and activity history.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

Distributed under the [MIT License](LICENSE).


Author
Built by El-Sombra-Dev.

- GitHub: [El-Sombra-Dev](https://github.com/El-Sombra-Dev)
  
---

## API Documentation Preview

The API includes interactive OpenAPI documentation powered by Swagger UI.

Run the application locally and open:

```text
http://127.0.0.1:8000/docs
```

![Smart TaskFlow API Swagger Documentation](assets/swagger-docs.png)

<div align="center">

**Made with ❤️ using Python & FastAPI By DevZed El-Sombra**

⭐ Star this repo if you find it helpful!

</div>

