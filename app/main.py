from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from functools import lru_cache
from app.src.routers import webfinger
from app.src.routers import actor

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(webfinger.router)
app.include_router(actor.router)
