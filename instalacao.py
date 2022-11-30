import urllib.request
import shutil
from vars import (
    ps_script_name,
    ps_script_url,
    caixa_google_id,
    caixa_file_name,
    adobeair_google_id,
    adobeair_file_name,
    sisbr20_google_id,
    sisbr20_file_name,
    citrix_google_id,
    citrix_file_name,
    path_local,
    choco_path,
)
from functions import (
    download_install_google,
    download_install_google_zip,
    execute,
    execute_powershell,
)


def install_chocolatey():
    print("Instalando Chocolatey...")
    try:
        command = "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"
        execute_powershell(command)
    except Exception as e:
        print(e.args[0])


def install_chocolatey_program(programa, cmd):
    try:
        execute(f"{choco_path} install -y " + cmd)
    except Exception as e:
        print(e.args[0])


def install_google_chrome():
    install_chocolatey_program("Chrome", "googlechrome")


def install_firefox():
    install_chocolatey_program("Firefox", "firefox")


def install_spark():
    install_chocolatey_program("Spark", "spark")


def install_java():
    install_chocolatey_program(
        "Java 8 32bits", 'jre8 -PackageParameters "/exclude:64" -y'
    )


def install_teamviewer():
    install_chocolatey_program("Teamviewer", "teamviewer")


def install_anydesk():
    install_chocolatey_program("Anydesk", "anydesk.install")


def install_anydesk():
    install_chocolatey_program("AdobeReader", "adobereader")


def install_7zip():
    install_chocolatey_program("7Zip", "7zip.install")


def install_notepadplusplus():
    install_chocolatey_program("Notepad++", "notepadplusplus")


# Instalacao do Caixa
def install_caixa():
    caixa_file_path = (path_local / caixa_file_name).absolute()
    download_install_google(
        "Caixa",
        caixa_google_id,
        caixa_file_name,
        f'java -jar  "{caixa_file_path}"',
    )


# Instalacao do Adobe Air
def install_adobeair():
    adobeair_file_path = (path_local / adobeair_file_name).absolute()
    download_install_google(
        "Adobe Air",
        adobeair_google_id,
        adobeair_file_name,
        f"{adobeair_file_path}",
    )


# Instalacao do Sisbr2.0
def install_sisbr20():
    sisbr20_file_path = (path_local / sisbr20_file_name).absolute()
    download_install_google(
        "Sisbr 2.0",
        sisbr20_google_id,
        sisbr20_file_name,
        f"{sisbr20_file_path}",
    )


# Instalacao Citrix10
def install_citrix10():
    citrix_path_execution = (
        path_local / "Citrix10" / "Versao 10.1" / "PN_10_1.msi"
    ).absolute()
    download_install_google_zip(
        "Citrix10",
        citrix_google_id,
        citrix_file_name,
        f'msiexec /i "{citrix_path_execution}"',
    )
