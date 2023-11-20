# app/main.py
import logging
from fastapi import FastAPI,Depends
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from app.middlewares.auth import auth_middleware
from fastapi.middleware.cors import CORSMiddleware
from app.api.main import router as api_v1_router  # Adjust this import if necessary
from app.core.config import settings  # Adjust the import path as necessary for your config settings
  # Adjust the import path as necessary for your security functions
# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the SQLAlchemy engine using your settings
engine = create_engine(settings.database_url)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


app.middleware("http")(auth_middleware)
@app.on_event("startup")
async def startup_db_test():
    # Try to connect to the database to ensure it's up
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        logger.info("Database--@@@@@@@@@@--connection test successful")
    except OperationalError as e:
        logger.critical(f"Database connection test failed: {e}")
        # Depending on your requirements, you might want to stop app launch if the DB can't connect.
        # raise e

# Include the API v1 router
app.include_router(api_v1_router, prefix="/api" )

@app.get("/")
async def read_root():
    return {"message": "Hello World"}


