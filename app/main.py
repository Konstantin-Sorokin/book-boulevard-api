import uvicorn
from fastapi import FastAPI

from config import settings
from api import router

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        app=settings.run.app,
        reload=True,
        host=settings.run.host,
        port=settings.run.port,
    )
