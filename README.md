# Task Manager REST API

A RESTful API for managing tasks built with Flask and MongoDB. This application provides a complete task management system with CRUD operations, search functionality, and Docker containerization.

## 🚀 Features

- ✅ Create, read, update, delete tasks
- 🔍 Search tasks by title/description
- ✏️ Edit task details
- ☑️ Mark tasks as completed
- 🗑️ Delete individual or all completed tasks
- 🎨 Beautiful, responsive UI
- 🐳 Fully dockerized
- 🧪 Comprehensive unit tests

## 🐳 Start with Docker (Recommended)

**Prerequisites:**
- Docker and Docker Compose
- Python 3.11+ (for local development)
- MongoDB (for local development)

```bash
# Clone the repository
git clone https://github.com/t0556708557/task-manager.git
cd task-manager

# Build and run all services
docker-compose up --build
```

**Access:**
- Frontend: http://localhost:5000
- API: http://localhost:5000/api/tasks

**Run tests:**
```bash
docker compose --profile test run --rm test
```

## 📋 Local Development Setup

1. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Start MongoDB:**
```bash
# Using Docker (recommended)
docker run -d -p 27017:27017 --name mongodb mongo:7.0

# Or using local MongoDB
mongod --dbpath /path/to/data
```

4. **Set environment variables (optional):**
```bash
echo "MONGO_URI=mongodb://localhost:27017/taskdb" > .env
echo "FLASK_ENV=development" >> .env
```

5. **Run the application:**
```bash
python run.py
```

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


## 🧪 Unit Tests
```bash
# Run unit tests
docker compose --profile test run --rm test

# Run with coverage
docker compose --profile test run --rm test pytest tests/ -v --cov=app
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
- [Helm Charts](https://github.com/t0556708557/task-manager-helm-charts) - Kubernetes deployment charts

## 📦 Tech Stack

- Flask 3.0.0 (Python web framework)
- MongoDB 7.0 (Database)
- PyMongo 4.6.1 (MongoDB driver)
- Pytest (Testing framework)
- Docker & Docker Compose
- Python 3.11 (Runtime)

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
├── .env                     # Environment variables (optional)
├── docker-compose.yml       # Docker compose config
├── Dockerfile               # Docker image config
├── Dockerfile.test          # Test container
├── requirements.txt         # Python dependencies
├── requirements-test.txt    # Test dependencies
├── run.py                   # Application entry point
├── ci-cd.yaml              # CI/CD pipeline
├── task-manager-full-architecture.png  # Architecture diagram
└── README.md               # This file
```

**Happy task managing! 🎯**
