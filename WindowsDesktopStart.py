import subprocess
import urllib.request
from pathlib import Path
from google_drive import download_install_google, download_install_google_zip


# Parametros Chocolatey
ps_script_url = "https://community.chocolatey.org/install.ps1"
ps_script_name = "install_chocolatey.ps1"

# Parametros Caixa
caixa_google_id = "1u0JnYuLxxcOgMTU5iYwMR20SOwBq3vaB"
caixa_file_name = "Setup.jar"

# Parametros Adobe Air
adobeair_google_id = "13fUuPTnwpzIoydnefw9bcdX2h5KbJb0N"
adobeair_file_name = "AdobeAir.exe"

# Parametros Sisbr2.0
sisbr20_google_id = "13E-X5fZZrj2FMZDIcLWJ94c9DgTqUA3f"
sisbr20_file_name = "Sisbr2.0.exe"

# Parametros Citrix10
citrix_google_id = "19o1eGqGL6xR1B9b3VYunea4zzYe3Heb9"
citrix_file_name = "Citrix10.zip"

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
        "teamviewer",
        "anydesk.install",
        "adobereader",
    ]
    for programa in choco_install_list:
        subprocess.call("choco install -y " + programa)
except Exception as e:
    print(e.args[0])

# Instalacao do Caixa
caixa_file_path = path_local / caixa_file_name
download_install_google(
    "Caixa",
    caixa_google_id,
    caixa_file_name,
    f"java -jar  {caixa_file_path}",
)

# Instalacao do Adobe Air
adobeair_file_path = path_local / adobeair_file_name
download_install_google(
    "Adobe Air",
    adobeair_google_id,
    adobeair_file_name,
    f"{adobeair_file_path}",
)

# Instalacao do Sisbr2.0
sisbr20_file_path = path_local / sisbr20_file_name
download_install_google(
    "Sisbr 2.0",
    sisbr20_google_id,
    sisbr20_file_name,
    f"{sisbr20_file_path}",
)

# Instalacao Citrix10
citrix_file_path = path_local / citrix_file_name
citrix_path_execution = path_local / 'Citrix10' / 'Versao 10.1' / 'PN_10_1.msi'
download_install_google_zip(
    "Citrix",
    citrix_google_id,
    citrix_file_path,
    f'msiexec /i {citrix_path_execution}',
)


input("Instalação finalizada, pressione qualquer tecla para fechar...")
