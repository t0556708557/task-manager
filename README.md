# Task Manager REST API

A RESTful API for managing tasks built with Flask and MongoDB. This application provides a complete task management system with CRUD operations, search functionality, and Docker containerization.

## 📋 Table of Contents

1. [Overview](#Overview)
2. [Prerequisites](#prerequisites)
3. [Installation & Setup](#installation--setup)
4. [Project Structure](#project-structure)
5. [API Endpoints](#api-endpoints)
6. [Testing](#testing)
7. [CI/CD Pipeline](#cicd-pipeline)
8. [Tech Stack](#tech-stack)
9. [Related Links](#related-links)

---

## 🎯 Overview

### Key Features

- ✅ Create, read, update, delete tasks (CRUD)
- 🔍 Search tasks by title/description
- ✏️ Edit task details
- ☑️ Mark tasks as completed
- 🗑️ Delete individual or all completed tasks
- 🎨 Beautiful, responsive UI
- 🐳 Fully dockerized
- 🧪 Comprehensive unit tests

---

## 🔧 Prerequisites

### For Docker Setup
- Docker and Docker Compose

### For Local Development
- Python 3.11+
- MongoDB 7.0
- Docker (optional, for database)

---

## 🚀 Installation & Setup

### Option 1: Docker Setup

#### Step 1: Clone the Repository
```bash
git clone https://github.com/t0556708557/task-manager.git
cd task-manager
```

#### Step 2: Build and Run
```bash
docker-compose up --build
```

#### Step 3: Access the Application
- Frontend: http://localhost:5000
- API: http://localhost:5000/api/tasks

#### Run Tests
```bash
docker compose --profile test run --rm test
```

---

### Option 2: Local Development

#### Step 1: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

#### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 3: Start MongoDB
```bash
# Using Docker (recommended)
docker run -d -p 27017:27017 --name mongodb mongo:7.0

# Or using local MongoDB
mongod --dbpath /path/to/data
```

#### Step 4: Set Environment Variables (Optional)
```bash
echo "MONGO_URI=mongodb://localhost:27017/taskdb" > .env
echo "FLASK_ENV=development" >> .env
```

#### Step 5: Run the Application
```bash
python run.py
```

---

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
├── Dockerfile.test          # Test container
├── requirements.txt         # Python dependencies
├── requirements-test.txt    # Test dependencies
├── run.py                   # Application entry point
└── README.md               # This file
```

---

## 📋 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/tasks | Get all tasks |
| GET | /api/tasks/{id} | Get task by ID |
| POST | /api/tasks | Create new task |
| PUT | /api/tasks/{id} | Update task |
| DELETE | /api/tasks/{id} | Delete task |
| DELETE | /api/tasks/completed | Delete all completed tasks |
| GET | /api/tasks/search?q={query} | Search tasks |

---

## 🧪 Testing

### Running Unit Tests

```bash
# Basic tests
docker compose --profile test run --rm test

# Tests with coverage
docker compose --profile test run --rm test pytest tests/ -v --cov=app
```

---

## 🚢 CI/CD Pipeline

### Overview

The project includes an automated pipeline that performs:

1. **Build & Unit Test**: Build Docker images and run unit tests
2. **Package & Integration Tests**: Create production image and run E2E tests
3. **Publish**: Push verified image to Amazon ECR
4. **Deploy**: Deploy to Amazon EKS

### Pipeline Stages

- **Unit Tests**: Isolated tests with mocked database
- **E2E Tests**: Full application testing with real database
- **Security**: OIDC authentication for AWS access
- **Deployment**: Rolling updates to Kubernetes

### Required Secrets (GitHub Repository)

```
AWS_ROLE: ARN of IAM role for AWS access
AWS_REGION: AWS region (e.g., us-east-1)
ECR_REPOSITORY: ECR repository URL
DB_USER: MongoDB username
DB_PASSWORD: MongoDB password
```

---

## 📦 Tech Stack

### Backend
- Flask 3.0.0 - Python web framework
- PyMongo 4.6.1 - MongoDB driver
- Python 3.11 - Runtime

### Database
- MongoDB 7.0

### Testing
- Pytest - Testing framework

### DevOps
- Docker & Docker Compose
- GitHub Actions (CI/CD)
- Amazon ECR (Container Registry)
- Amazon EKS (Kubernetes)

---

## 🔗 Related Links

- [Infrastructure Repository](https://github.com/t0556708557/terraform-eks) - Terraform infrastructure code
- [Helm Charts Repository](https://github.com/t0556708557/task-manager-helm-charts) - Kubernetes deployment charts

---
---