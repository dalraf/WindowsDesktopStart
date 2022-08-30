import subprocess
import urllib.request
from pathlib import Path


# Parametros Chocolatey
ps_script_url = "https://community.chocolatey.org/install.ps1"
ps_script_name = "install_chocolatey.ps1"


path_local = Path(".")

# Install chocolatey
print("Instalando Chocolatey...")
try:
    ps_script_path = path_local / ps_script_name
    urllib.request.urlretrieve(ps_script_url, ps_script_path)
    command = "powershell.exe -noprofile -executionpolicy bypass -file " + str(
        ps_script_path
    )
    subprocess.call(command, shell=True)
except Exception as e:
    print(e.args[0])

# Install programas padrão
print("Instalando programas padrão...")
try:
    choco_install_list = [
        "googlechrome",
        "firefox",
        "spark",
        'jre8 -PackageParameters "/exclude:64" -y',
        'teamviewer',
        'anydesk.install',
        'adobereader',
    ]
    for programa in choco_install_list:
        subprocess.call("choco install -y " + programa)
except Exception as e:
    print(e.args[0])

input("Instalação finalizada, pressione qualquer tecla para fechar...")
