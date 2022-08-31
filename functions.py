import requests
import subprocess
import zipfile
from vars import path_local
import platform
import gdown

def execute(cmd):
    if platform.system() == 'Linux':
        print(cmd)
    else:
        print(cmd)
        subprocess.call(cmd, cwd=path_local, shell=True)


def download_file_from_google_drive(id, destination):
    gdown.download(id=id, output=str(destination), quiet=False)


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
