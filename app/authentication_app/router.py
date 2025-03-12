from fastapi import APIRouter

router = APIRouter()


@router.post("/register")
async def auth_register() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/login")
async def auth_login() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/logout")
async def auth_logout() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/introspect")
async def auth_introspect() -> dict[str, str]:
    return {"status": "ok"}
