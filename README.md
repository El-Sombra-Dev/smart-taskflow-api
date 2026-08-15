# 🚀 Smart TaskFlow API

A clean, production-oriented REST API for personal task management. Smart TaskFlow provides secure user authentication, task CRUD operations, categories, filtering, pagination, automatic OpenAPI documentation, and a simple SQLite default setup.

> Built with FastAPI, SQLAlchemy, Pydantic, JWT, and SQLite/PostgreSQL compatibility.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 🔐 **JWT Authentication** - Secure user authentication and authorization
- 📝 **CRUD Operations** - Full Create, Read, Update, Delete functionality
- 🗄️ **Database Integration** - PostgreSQL/SQLite support with SQLAlchemy ORM
- 🧪 **Automated Testing** - Comprehensive test suite with pytest
- 📦 **Docker Ready** - Containerized deployment with Docker Compose
- 📚 **Auto Documentation** - Interactive API docs with Swagger UI
- 🎯 **Production Ready** - Logging, error handling, and validation
- ⚡ **High Performance** - Async/await support for optimal speed

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL / SQLite
- **ORM**: SQLAlchemy
- **Authentication**: JWT (PyJWT)
- **Validation**: Pydantic
- **Testing**: pytest
- **Containerization**: Docker & Docker Compose

## 📋 Prerequisites

- Python 3.9 or higher
- PostgreSQL (optional, SQLite works by default)
- Docker & Docker Compose (optional)

## 🚀 Quick Start

### 1. Clone the Repository

@@@bash
git clone https://github.com/El-Sombra-Dev/smart-taskflow-api.git
cd smart-taskflow-api
@@@

### 2. Create Virtual Environment

@@@bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
@@@

### 3. Install Dependencies

@@@bash
pip install -r requirements.txt
@@@

### 4. Configure Environment Variables

@@@bash
cp .env.example .env
@@@

Edit .env file with your configuration:

@@@env
DATABASE_URL=sqlite:///./tasks.db
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
@@@

### 5. Run the Application

@@@bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
@@@

### 6. Access the API

- **API Base URL**: http://localhost:8000
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📚 API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/auth/register | Register new user |
| POST | /api/auth/login | Login and get JWT token |
| GET | /api/auth/me | Get current user info |

### Tasks

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/tasks | Get all tasks |
| GET | /api/tasks/{task_id} | Get specific task |
| POST | /api/tasks | Create new task |
| PUT | /api/tasks/{task_id} | Update task |
| DELETE | /api/tasks/{task_id} | Delete task |

### Categories

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/categories | Get all categories |
| POST | /api/categories | Create new category |
| DELETE | /api/categories/{category_id} | Delete category |

## 🧪 Running Tests

@@@bash
# Run all tests
pytest

# Run with coverage
pytest --cov=.

# Run specific test file
pytest tests/test_auth.py
@@@

## 🐳 Docker Deployment

### Build and Run with Docker Compose

@@@bash
docker-compose up --build
@@@

### Access the API

- **API**: http://localhost:8000
- **Docs**: http://localhost:8000/docs

## 📁 Project Structure

@@@
smart-taskflow-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models/
│   ├── schemas/
│   ├── routers/
│   └── utils/
├── requirements.txt
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
└── README.md
@@@

## 🔒 Security

- Password hashing with bcrypt
- JWT token-based authentication
- CORS configuration
- Input validation with Pydantic
- SQL injection protection via SQLAlchemy ORM

## 📝 Example Usage

### Register a User

@@@bash
curl -X POST "http://localhost:8000/api/auth/register" @@
  -H "Content-Type: application/json" @@
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepassword123"
  }'
@@@

### Login

@@@bash
curl -X POST "http://localhost:8000/api/auth/login" @@
  -H "Content-Type: application/json" @@
  -d '{
    "username": "johndoe",
    "password": "securepassword123"
  }'
@@@

### Create a Task (with JWT token)

@@@bash
curl -X POST "http://localhost:8000/api/tasks" @@
  -H "Content-Type: application/json" @@
  -H "Authorization: Bearer YOUR_JWT_TOKEN" @@
  -d '{
    "title": "Complete project documentation",
    "description": "Write comprehensive API documentation",
    "status": "pending",
    "priority": "high"
  }'
@@@

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (@@@git checkout -b feature/AmazingFeature@@)
3. Commit your changes (@@@git commit -m 'Add some AmazingFeature'@@)
4. Push to the branch (@@@git push origin feature/AmazingFeature@@)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**DevZed El-Sombra**

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

