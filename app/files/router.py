from fastapi import APIRouter, UploadFile, File, Header, HTTPException
from pypdf import PdfMerger
import uuid
from pydantic import BaseModel
import aiohttp
import json

router = APIRouter()

authentication_url = '0.0.0.0'

files = {}


class FileModel(BaseModel):
    filename: str
    path: str
    author: str

@router.post("/merge")
async def merge_files() -> dict[str, str]:
    file1 = "files/act01.pdf"
    file2 = "files/act02.pdf"
    merged = "files/act01act02.pdf"
    pdfs = [file1, file2]
    merger = PdfMerger()

    for pdf in pdfs:
        merger.append(pdf)

    name = merged
    merger.write(name)
    merger.close()

    return {"status": "ok"}


@router.get("/")
async def get_files(auth: str = Header()) -> list[dict[str, FileModel]]:
    user = await auth_check(auth)

    result = []
    username = user['username']

    for key, value in files.items():
        if value.author == username:
            result.append({key: value})

    return result


@router.post("/")
async def post_file(
    auth: str = Header(),
    input_file: UploadFile = File()
) -> dict[str, FileModel]:
    user = await auth_check(auth)

    prefix = 'files/'
    file_id = str(uuid.uuid4())
    while file_id in files:
        file_id = str(uuid.uuid4())
    path = prefix + file_id + '.pdf'

    with open(path, "wb") as buffer:
        while chunk := await input_file.read(8192):
            buffer.write(chunk)

    new_file = FileModel(
        filename=input_file.filename,
        path=path,
        author=user['username'],
    )
    files[file_id] = new_file

    return {file_id: new_file}


@router.get("/{id}")
async def get_file_by_id() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/{id}")
async def post_file_by_id() -> dict[str, str]:
    return {"status": "ok"}


@router.delete("/{id}")
async def delete_file_by_id() -> dict[str, str]:
    return {"status": "ok"}


async def introspect(auth: str):
    headers = {
        "accept": "application/json",
        "auth": auth
    }
    url = "http://" + authentication_url + ":80/auth/introspect"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, ssl=False) as response:
            status_code = response.status
            if status_code != 200:
                return None
            body = await response.text()
            return body


async def auth_check(auth):
    auth_response = await introspect(auth=auth)
    if auth_response is None:
        raise HTTPException(status_code=403, detail='Forbidden')

    return json.loads(auth_response)
