# E-commerce Manager Dashboard

A backend API using FastAPI for managing e-commerce operations.

## Setup

1. Build the Docker image:
```bash
docker-compose build
# fastapi-ecommerce-api
DATABASE_URL=postgresql://admin:12345678@localhost:5432/localdb
SECRET_KEY=YourSuperSecretKeyHere
ACCESS_TOKEN_EXPIRE_MINUTES=30
