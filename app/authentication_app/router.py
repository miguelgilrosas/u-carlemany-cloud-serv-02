from fastapi import APIRouter

router = APIRouter()


@router.post("/register")
async def healthcheck1() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/login")
async def healthcheck2() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/logout")
async def healthcheck3() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/introspect")
async def healthcheck4() -> dict[str, str]:
    return {"status": "ok"}
