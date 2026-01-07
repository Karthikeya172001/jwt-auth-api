import os
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from app.database import users_collection

router = APIRouter()

# Password hashing
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# JWT config
SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"
security = HTTPBearer()


# ---------- Password helpers ----------

def hash_password(password: str) -> str:
    return pwd_context.hash(password[:72])


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain[:72], hashed)


# ---------- JWT helpers ----------

def create_token(email: str) -> str:
    payload = {
        "sub": email,
        "exp": datetime.utcnow() + timedelta(hours=2)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")

        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        user = users_collection.find_one({"email": email})
        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        return email

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")


# ---------- Routes ----------

@router.post("/signup")
def signup(email: str, password: str):
    if users_collection.find_one({"email": email}):
        raise HTTPException(status_code=400, detail="User already exists")

    users_collection.insert_one({
        "email": email,
        "password": hash_password(password)
    })

    return {"message": "Signup successful"}


@router.post("/login")
def login(email: str, password: str):
    user = users_collection.find_one({"email": email})
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(email)
    return {"token": token}


@router.get("/me")
def read_me(current_user: str = Depends(get_current_user)):
    return {
        "email": current_user,
        "status": "authenticated"
    }
