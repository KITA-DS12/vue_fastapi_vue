from fastapi import FastAPI
import uvicorn

from db.database import engine
from db import models
from db import routers

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(routers.router)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        reload=True,
        port=8888,
        log_level="debug",
    )
