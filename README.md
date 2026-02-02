# Task Manager REST API

A RESTful API for managing tasks built with Flask and MongoDB. This application provides a complete task management system with CRUD operations, search functionality, and Docker containerization.

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

### Unit Tests
```bash
# Run unit tests
docker compose --profile test run --rm test

# Run with coverage
docker compose --profile test run --rm test pytest tests/ -v --cov=app
```

### Manual Testing
```bash
# Test API endpoints
curl http://localhost:5000/api/tasks

# Create a task
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Test Task", "description": "Test description"}'
```

## 🚢 CI/CD Pipeline

The project includes a comprehensive CI/CD pipeline that:

1. **Build & Unit Test**: Builds Docker images and runs unit tests
2. **Package & Integration Tests**: Creates production image and runs E2E tests
3. **Publish**: Pushes verified image to Amazon ECR
4. **Deploy**: Deploys to Amazon EKS

### Pipeline Stages

- **Unit Tests**: Mocked database tests for isolated testing
- **E2E Tests**: Full application testing with real database
- **Security**: OIDC authentication for AWS access
- **Deployment**: Rolling updates to Kubernetes

### Required Secrets (GitHub Repository)

```
AWS_ROLE: ARN of IAM role for AWS access
AWS_REGION: AWS region (e.g., us-east-1)
ECR_REPOSITORY: ECR repository URL
DB_USER: MongoDB username (optional)
DB_PASSWORD: MongoDB password (optional)
```

## 🔗 Related Repositories

- [Infrastructure](https://github.com/t0556708557/terraform-eks) - Terraform infrastructure code
- [Helm Charts](https://github.com/t0556708557/task-manager-k8s-helm) - Kubernetes deployment charts

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

**Happy task managing! 🎯**

## 📦 Tech Stack

- Flask 3.0 (Python web framework)
- MongoDB 7.0 (Database)
- Pytest (Testing framework)
- Docker & Docker Compose
