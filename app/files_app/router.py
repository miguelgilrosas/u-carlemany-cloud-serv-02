from fastapi import APIRouter

router = APIRouter()


@router.get("/files")
async def healthcheck1() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/files")
async def healthcheck2() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/files/{id}")
async def healthcheck3() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/files/{id}")
async def healthcheck4() -> dict[str, str]:
    return {"status": "ok"}


@router.delete("/files/{id}")
async def healthcheck5() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/files/merge")
async def healthcheck6() -> dict[str, str]:
    return {"status": "ok"}
