import json

import whisper

from ..config import app_settings

__model = whisper.load_model(
    app_settings.whisper_model_type,
    download_root=app_settings.whisper_models_dir
)


def get_filename(filepath: str):
    no_dirs = filepath.split('/')[-1] if filepath.count('/') else filepath
    no_ext = "".join(no_dirs.split('.')[:-1]) if no_dirs.count('.') > 1 else no_dirs
    return no_ext + '.json'


def get_path_to_save(filename: str):
    return (
        app_settings.transcription_path + '/'
        if not str(app_settings.transcription_path).endswith('/')
        else app_settings.transcription_path
    ) + get_filename(filename)


def get_transcription(orig_filename: str):
    return json.load(open(get_path_to_save(orig_filename), 'r'))


async def transcribe_by_filepath(filepath: str) -> dict:
    result = __model.transcribe(filepath, fp16=False)
    path_to_save = get_path_to_save(filepath)
    json.dump(result, open(path_to_save, 'w'), ensure_ascii=False)
    return result
