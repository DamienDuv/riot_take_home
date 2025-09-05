import logging
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

# Simple error handler to catch unexpected errors and log them
# we discard classic errors like request validation, 404...
@app.exception_handler(Exception)
async def log_unhandled_exception(request: Request, exc: Exception):

    if isinstance(exc, (RequestValidationError, StarletteHTTPException)):
        raise exc
    
    logger.exception("Unhandled exception on %s %s", request.method, request.url.path)
    return JSONResponse({"detail": "Internal Server Error"}, status_code=500)

app.include_router(router)