# E-commerce Manager Dashboard

A backend API using FastAPI for managing e-commerce operations.

## Setup

1. Build the Docker image:
```bash
docker-compose build


2. Run the Migeration:
```bash
alembic revision --autogenerate -m "Create user table"

3. Apply Tables:
```bash
alembic upgrade head


ecommerce_manager/
│
├── app/                         
│   ├── api/                     
│   │   ├── v1/                   
│   │   │   ├── endpoints/        
│   │   │   │   ├── user.py
│   │   │   │   ├── sales.py
│   │   │   │   ├── inventory.py
│   │   │   │   └── product.py
│   │   │   ├── __init__.py
│   │   │   └── main.py           
│   │   └── deps.py               
│   │
│   ├── core/                     
│   │   ├── config.py             # Configuration including logging config
│   │   ├── security.py           
│   │   └── database.py           
│   │
│   ├── middlewares/              # Middleware components
│   │   ├── __init__.py
│   │   ├── auth.py               # Authentication middleware
│   │   └── logging.py            # Logging middleware
│   │
│   ├── models/                   
│   │   ├── user.py
│   │   ├── product.py
│   │   ├── sales.py
│   │   └── inventory.py
│   │
│   ├── schemas/                 
│   │   ├── user.py
│   │   ├── product.py
│   │   ├── sales.py
│   │   └── inventory.py
│   │
│   ├── services/                
│   │   ├── user_service.py
│   │   ├── product_service.py
│   │   ├── sales_service.py
│   │   └── inventory_service.py
│   │
│   ├── utils/                   
│   │   └── timezone.py          
│   │
│   ├── main.py                  
│   └── __init__.py
│
├── tests/                       
│   ├── api/
│   │   ├── v1/
│   │   ├── user/
│   │   ├── product/
│   │   ├── sales/
│   │   └── inventory/
│   │
│   ├── services/
│   ├── conftest.py
│   └── __init__.py
│
├── alembic/                     
│   ├── versions/
│   └── alembic.ini
│
├── logs/                        
│   ├── access.log               # Log for access details
│   └── error.log                # Log for errors and exceptions
│                 
├── docker-compose.yml           
├── .env                         
├── .gitignore
├── README.md
└── requirements.txt


# fastapi-ecommerce-api
DATABASE_URL=postgresql://admin:12345678@localhost:5432/localdb
SECRET_KEY=YourSuperSecretKeyHere
ACCESS_TOKEN_EXPIRE_MINUTES=30

FastApi123@
admin@Acb1232

DATABASE_URL=postgresql://postgres:admin%40Acb1232@db.jarmhqwuxrimwwriaycr.supabase.co:5432/postgres
SECRET_KEY=YourSuperSecretKeyHere
ACCESS_TOKEN_EXPIRE_MINUTES=30

