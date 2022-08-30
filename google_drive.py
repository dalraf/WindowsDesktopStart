import requests
from pathlib import Path
import subprocess
import zipfile

def download_file_from_google_drive(self, id, destination):
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
    path_local = Path(".")
    print(f'Instalando {nome}...')
    file_path = path_local / file_name
    try:
        download_file_from_google_drive(id, file_path)
        subprocess.call(cmd, shell=True)
    except Exception as e:
        print(e.args[0])

def download_install_google_zip(nome, id, file_name, cmd):
    path_local = Path(".")
    print(f'Instalando {nome}...')
    file_path = path_local / file_name
    try:
        download_file_from_google_drive(id, file_path)
        with zipfile.ZipFile(file_path, "r") as citrixzip:
            citrixzip.extractall(path_local)
        subprocess.call(cmd, shell=True)
    except Exception as e:
        print(e.args[0])