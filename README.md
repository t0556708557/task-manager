# Task Manager API

A RESTful API for managing tasks built with Flask and MongoDB. This application provides a complete task management system with CRUD operations, search functionality, and Docker containerization.

## 🚀 Features

- ✅ Create, read, update, and delete tasks
- 🔍 Search tasks by title or description
- 📊 Track task completion status
- 🐳 Docker containerization
- 🧪 Unit and integration testing
- 🚢 CI/CD pipeline with AWS ECR and EKS deployment
- 📝 RESTful API with JSON responses

## 📋 Prerequisites

- Python 3.11+
- Docker and Docker Compose
- MongoDB (for local development)
- Git

## 🛠️ Installation

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/t0556708557/task-manager
   cd task-manager
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   # Create .env file
   MONGO_URI=mongodb://localhost:27017/taskdb
   FLASK_ENV=development
   ```

5. **Start MongoDB:**
   ```bash
   # Using Docker
   docker run -d -p 27017:27017 --name mongodb mongo:7.0
   ```

6. **Run the application:**
   ```bash
   python run.py
   ```

The API will be available at `http://localhost:5000`

## 🐳 Docker Setup

### Build and Run with Docker Compose

1. **Build and start all services:**
   ```bash
   docker compose up --build
   ```

2. **Run in background:**
   ```bash
   docker compose up -d --build
   ```

3. **View logs:**
   ```bash
   docker compose logs -f web
   ```

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `MONGO_URI` | `mongodb://mongodb:27017/taskdb` | MongoDB connection string |
| `FLASK_ENV` | `production` | Flask environment (development/production) |
| `DB_USER` | - | MongoDB username (optional) |
| `DB_PASSWORD` | - | MongoDB password (optional) |

### Docker Commands

```bash
# Build specific service
docker compose build web

# Run tests
docker compose --profile test up --build

# Stop all services
docker compose down

# Remove volumes
docker compose down -v
```

## 📚 API Documentation

### Base URL
```
http://localhost:5000/api
```

### Response Format
All responses follow this structure:
```json
{
  "success": boolean,
  "data": object|array,
  "message": string,
  "error": string,
  "count": number
}
```

### Endpoints

#### 1. Get All Tasks
**GET** `/api/tasks`

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "id": "507f1f77bcf86cd799439011",
      "title": "Sample Task",
      "description": "Task description",
      "completed": false,
      "created_at": "2023-01-01T00:00:00Z",
      "updated_at": "2023-01-01T00:00:00Z"
    }
  ],
  "count": 1
}
```

#### 2. Get Task by ID
**GET** `/api/tasks/{task_id}`

**Response (Success):**
```json
{
  "success": true,
  "data": {
    "id": "507f1f77bcf86cd799439011",
    "title": "Sample Task",
    "description": "Task description",
    "completed": false,
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z"
  }
}
```

**Response (Not Found):**
```json
{
  "success": false,
  "error": "Task not found"
}
```

#### 3. Create Task
**POST** `/api/tasks`

**Request Body:**
```json
{
  "title": "New Task",
  "description": "Task description",
  "completed": false
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "id": "507f1f77bcf86cd799439011",
    "title": "New Task",
    "description": "Task description",
    "completed": false,
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z"
  },
  "message": "Task created"
}
```

#### 4. Update Task
**PUT** `/api/tasks/{task_id}`

**Request Body:**
```json
{
  "title": "Updated Task",
  "completed": true
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "id": "507f1f77bcf86cd799439011",
    "title": "Updated Task",
    "description": "Task description",
    "completed": true,
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z"
  },
  "message": "Task updated"
}
```

#### 5. Delete Task
**DELETE** `/api/tasks/{task_id}`

**Response:**
```json
{
  "success": true,
  "message": "Task deleted"
}
```

#### 6. Delete Completed Tasks
**DELETE** `/api/tasks/completed`

**Response:**
```json
{
  "success": true,
  "message": "Deleted 3 tasks",
  "count": 3
}
```

#### 7. Search Tasks
**GET** `/api/tasks/search?q={query}`

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "id": "507f1f77bcf86cd799439011",
      "title": "Sample Task",
      "description": "Task description",
      "completed": false,
      "created_at": "2023-01-01T00:00:00Z",
      "updated_at": "2023-01-01T00:00:00Z"
    }
  ],
  "count": 1,
  "query": "Sample"
}
```

### Error Responses

**400 Bad Request:**
```json
{
  "success": false,
  "error": "Title required"
}
```

**404 Not Found:**
```json
{
  "success": false,
  "error": "Task not found"
}
```

**500 Internal Server Error:**
```json
{
  "success": false,
  "error": "Failed to retrieve tasks"
}
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

## 📁 Project Structure

```
task-manager/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── config.py            # Configuration classes
│   ├── models.py            # Database models
│   └── routes.py            # API endpoints
├── tests/
│   ├── conftest.py          # Test configuration
│   └── test_api.py          # API tests
├── static/
│   └── index.html           # Frontend (optional)
├── Dockerfile               # Production container
├── Dockerfile.test          # Test container
├── docker-compose.yml       # Local development
├── requirements.txt         # Python dependencies
├── requirements-test.txt    # Test dependencies
├── run.py                   # Application entry point
├── ci-cd.yaml              # GitHub Actions pipeline
└── README.md               # This file
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
