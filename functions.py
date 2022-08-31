import requests
from pathlib import Path
import subprocess
import zipfile
import urllib.request
from vars import path_local
import platform

def execute(cmd):
    if platform.system() == 'Linux':
        print(cmd)
    else:
        subprocess.call(cmd, shell=True)


def install_chocolatey(ps_script_url, ps_script_name):
    print("Instalando Chocolatey...")
    try:
        ps_script_path = path_local / ps_script_name
        urllib.request.urlretrieve(ps_script_url, ps_script_path)
        command = "powershell.exe -noprofile -executionpolicy bypass -file " + str(
            ps_script_path
        )
        execute(command)
    except Exception as e:
        print(e.args[0])


def install_chocolatey_list(choco_install_list):
    print("Instalando programas padrão...")
    try:
        for programa in choco_install_list:
            execute("choco install -y " + programa)
    except Exception as e:
        print(e.args[0])


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
    try:
        download_file_from_google_drive(id, file_path)
        execute(cmd)
    except Exception as e:
        print(e.args[0])


def download_install_google_zip(nome, id, file_name, cmd):
    print(f"Instalando {nome}...")
    file_path = path_local / file_name
    try:
        download_file_from_google_drive(id, file_path)
        with zipfile.ZipFile(file_path, "r") as citrixzip:
            citrixzip.extractall(path_local)
        execute(cmd)
    except Exception as e:
        print(e.args[0])
