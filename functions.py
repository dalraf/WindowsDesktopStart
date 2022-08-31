import requests
from pathlib import Path
import subprocess
import zipfile
from vars import path_local, ps_script_url, ps_script_name, choco_install_list
import platform

def execute(cmd):
    if platform.system() == 'Linux':
        print(cmd)
    else:
        subprocess.call(cmd, cwd=path_local, shell=True)


def download_file_from_google_drive(id, destination):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith("download_warning"):
                return value
        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)

    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params={"id": id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {"id": id, "confirm": token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)


def download_install_google(nome, id, file_name, cmd):
    print(f"Instalando {nome}...")
    file_path = path_local / file_name
    if file_path.exists():
        print('Arquivo existente não executando download')
    else:
        download_file_from_google_drive(id, file_path)
    try:
        execute(cmd)
    except Exception as e:
        print(e)


def download_install_google_zip(nome, id, file_name, cmd):
    print(f"Instalando {nome}...")
    file_path = path_local / file_name
    if file_path.exists():
        print('Arquivo existente não executando download')
    else:
        download_file_from_google_drive(id, file_path)
    try:
        with zipfile.ZipFile(file_path, "r") as citrixzip:
            citrixzip.extractall(path_local)
        execute(cmd)
    except Exception as e:
        print(e)