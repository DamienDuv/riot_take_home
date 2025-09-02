from fastapi import APIRouter

router = APIRouter(tags=["signing"])

@router.post("/sign")
async def sign_route():
   print("sign")
    
@router.post("/verify")
async def verify_route():
   print("verify")