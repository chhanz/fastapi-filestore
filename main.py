import os
import secrets
from typing import List

from fastapi import FastAPI, Depends, HTTPException, status, File, UploadFile
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import FileResponse

security = HTTPBasic()
UPLOAD_DIRECTORY = "./upload"

def auth(credentials: HTTPBasicCredentials = Depends(security)):
    is_user_ok = secrets.compare_digest(credentials.username, os.getenv('FILESTORE_ID'))
    is_pass_ok = secrets.compare_digest(credentials.password, os.getenv('FILESTORE_PASS'))

    if not (is_user_ok and is_pass_ok):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect id or password.',
            headers={'WWW-Authenticate': 'Basic'},
        )

app = FastAPI(openapi_url="/api/access/openapi.json", docs_url="/api/access/docs")
app.router.redirect_slashes = False

@app.post("/uploadfiles/", dependencies=[Depends(auth)])
async def upload_files(files: List[UploadFile] = File(...)):
    for file in files:
        contents = await file.read()
        with open(os.path.join(UPLOAD_DIRECTORY, file.filename), "wb") as fp:
            fp.write(contents)
    return {"filenames": [file.filename for file in files]}

@app.get("/files/", dependencies=[Depends(auth)]) 
async def list_files():
    files = os.listdir(UPLOAD_DIRECTORY)
    return {"list_files": files}

@app.get("/download/", dependencies=[Depends(auth)]) 
async def download_file(filename):
    file_path = UPLOAD_DIRECTORY + "/" + filename
    if os.path.isfile(file_path):
        return FileResponse(file_path)
    return None

@app.get("/", dependencies=[Depends(auth)])
async def main():
    return FileResponse('index.html')
