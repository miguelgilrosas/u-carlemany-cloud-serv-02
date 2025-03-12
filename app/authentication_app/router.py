from hashlib import sha256
from fastapi import APIRouter, Body, HTTPException
from pydantic import BaseModel

router = APIRouter()

users = {}
tokens = {}


class User(BaseModel):
    username: str
    password: bytes
    mail: str
    age_of_birth: int


class RegisterInput(BaseModel):
    username: str
    password: str
    mail: str
    age_of_birth: int


class RegisterOutput(BaseModel):
    username: str
    mail: str
    age_of_birth: int


@router.post("/register")
async def auth_register(input: RegisterInput = Body()) -> dict[str, RegisterOutput]:
    if input.username in users:
        raise HTTPException(status_code=409, detail="This username is already taken")

    to_hash = input.username + input.password
    hashed_password = sha256(to_hash.encode()).digest()

    new_user = User(
        username=input.username,
        password=hashed_password,
        mail=input.mail,
        age_of_birth=input.age_of_birth,
    )
    # print('HASH: ' + str(hashed_password.hex()))

    users[input.username] = new_user

    output = RegisterOutput(
        username=input.username,
        mail=input.mail,
        age_of_birth=input.age_of_birth,
    )

    return {"new_user": output}


@router.post("/login")
async def auth_login() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/logout")
async def auth_logout() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/introspect")
async def auth_introspect() -> dict[str, str]:
    return {"status": "ok"}
