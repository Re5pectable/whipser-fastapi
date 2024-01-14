from fastapi import UploadFile

from ..config import app_settings


async def save_file(file: UploadFile) -> str:
    contents = await file.read()
    
    to_save_path = (
        app_settings.audio_path + '/'
        if not str(app_settings.audio_path).endswith('/')
        else app_settings.audio_path
    ) + file.filename
    with open(to_save_path, "wb") as f:
        f.write(contents)
        
    return to_save_path