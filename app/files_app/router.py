from fastapi import APIRouter

router = APIRouter()


@router.get("/files")
async def get_files() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/files")
async def post_files() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/files/{id}")
async def get_file_by_id() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/files/{id}")
async def post_file_by_id() -> dict[str, str]:
    return {"status": "ok"}


@router.delete("/files/{id}")
async def delete_file_by_id() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/files/merge")
async def merge_files() -> dict[str, str]:
    return {"status": "ok"}
