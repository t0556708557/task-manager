# Task Manager REST API

Professional task management system built with Flask, MongoDB, and modern web technologies.

## 📁 Project Structure

```
task-manager/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── config.py            # Configuration
│   ├── models.py            # Database models
│   ├── routes.py            # API endpoints
│   └── static/
│       └── index.html       # Frontend UI
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Test configuration
│   └── test_api.py          # API tests
├── docker-compose.yml       # Docker compose config
├── Dockerfile               # Docker image config
├── requirements.txt         # Python dependencies
└── run.py                   # Application entry point
```

## 🚀 Features

- ✅ Create, read, update, delete tasks
- 🔍 Search tasks by title/description
- ✏️ Edit task details
- ☑️ Mark tasks as completed
- 🗑️ Delete individual or all completed tasks
- 🎨 Beautiful, responsive UI
- 🐳 Fully dockerized
- 🧪 Comprehensive unit tests

## 📋 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/tasks | Get all tasks |
| GET | /api/tasks/{id} | Get task by ID |
| POST | /api/tasks | Create new task |
| PUT | /api/tasks/{id} | Update task |
| DELETE | /api/tasks/{id} | Delete task |
| DELETE | /api/tasks/completed | Delete all completed |
| GET | /api/tasks/search?q={query} | Search tasks |

## 🐳 Quick Start

**Start with Docker:**
```bash
docker-compose up --build
```

**Access:**
- Frontend: http://localhost:5000
- API: http://localhost:5000/api/tasks

**Run tests:**
```bash
docker-compose run web pytest tests/ -v
```

## 💻 Local Development

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start MongoDB:
```bash
mongod --dbpath /path/to/data
```

4. Run application:
```bash
python run.py
```

## 📝 API Examples

**Create task:**
```bash
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Buy groceries","description":"Milk, eggs","completed":false}'
```

**Get all tasks:**
```bash
curl http://localhost:5000/api/tasks
```

**Search tasks:**
```bash
curl http://localhost:5000/api/tasks/search?q=groceries
```

## 🧪 Testing

Run all tests with coverage:
```bash
pytest tests/ --cov=app --cov-report=html -v
```

## 📦 Tech Stack

- Flask 3.0 (Python web framework)
- MongoDB 7.0 (Database)
- Pytest (Testing framework)
- Docker & Docker Compose
- Vanilla JavaScript (Frontend)

## 📄 License

MIT License - Free to use for learning and development.