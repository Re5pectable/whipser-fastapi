import json
import os

import whisper

from ..config import app_settings

__model = whisper.load_model(
    app_settings.whisper_model_type,
    download_root=app_settings.whisper_models_dir
)


def get_path_to_save(filename: str):
    return app_settings.transcription_path + os.path.basename(filename) + '.json'


def get_transcription(orig_filename: str):
    return json.load(open(get_path_to_save(orig_filename), 'r'))


def transcribe_by_filepath(language: str, filepath: str, path_to_save: str) -> dict:
    result = __model.transcribe(filepath, language=language, fp16=False)
    json.dump(result, open(path_to_save, 'w'), ensure_ascii=False)
    return result
