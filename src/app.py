from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api import router

app = FastAPI()

# Not allowing specific origins in the context of this exercise
# as it would mostly make sense with a known calling domain
app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],
    allow_credentials=True,
    allow_methods=["POST"], 
    allow_headers=["*"], 
)

app.include_router(router)