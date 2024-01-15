import os
import subprocess

from fastapi import UploadFile

from ..config import app_settings


async def save_file(file: UploadFile) -> str:
    contents = await file.read()

    to_save_path = app_settings.audio_path + file.filename
    with open(to_save_path, "wb") as f:
        f.write(contents)

    return to_save_path


def convert_to_mp3(input_path, output_path):
    subprocess.run(["ffmpeg", "-i", input_path, output_path])
    print('mp3 version saved in ', output_path)
    return output_path
