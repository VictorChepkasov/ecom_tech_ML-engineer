from fastapi import FastAPI

from app.routes.grades import router

app = FastAPI(
    title="Students Grades API"
)

app.include_router(router)