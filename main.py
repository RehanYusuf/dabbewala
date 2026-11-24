from contextlib import asynccontextmanager
from fastapi import FastAPI , Depends , HTTPException , Query , Path
from database import get_session , create_tables

from routes.orders import router as orders_router
from routes.stats import router as stats_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    print("Database tables created")
    yield
    print("Database tables dropped")



app = FastAPI(
    title = "Dabbewala",
    description = "A simple API for managing orders",
    version = "0.1.0",
    lifespan = lifespan
)



app.include_router(orders_router)
app.include_router(stats_router)



@app.get("/")
def home_page():
    return{
        "status": "This is the Home page that you have arrived of Dabbewala"
    }


@app.get("/health" , tags = ["health"])
def health_check():
    return {"status": "ok"}
