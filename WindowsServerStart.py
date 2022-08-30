import subprocess
import urllib.request
from pathlib import Path


#Parametros Openssh
openssh_download_url = 'https://github.com/PowerShell/Win32-OpenSSH/releases/download/v8.9.1.0p1-Beta/OpenSSH-Win32-v8.9.1.0.msi'
openssh_msi_name = 'OpenSSH-Win32-v8.9.1.0.msi'

#Parametros Chocolatey
ps_script_url = 'https://community.chocolatey.org/install.ps1'
ps_script_name = 'install_chocolatey.ps1'


path_local = Path('.')

#Install chocolatey
print('Instalando Chocolatey...')
try:
    ps_script_path = path_local / ps_script_name
    urllib.request.urlretrieve(ps_script_url, ps_script_path)
    command = 'powershell.exe -noprofile -executionpolicy bypass -file ' + str(ps_script_path)
    subprocess.call(command, shell=True)
except Exception as e:
    print(e.args[0])

#Install programas padrão
print('Instalando programas padrão...')
try:
    choco_install_list = ['googlechrome', 'firefox', 'rsync']
    for programa in choco_install_list:
        subprocess.call('choco install -y ' + programa)
except Exception as e:
    print(e.args[0])

#Install openssh
print('Instalando openssh...')
try:
    openssh_msi_path = path_local / openssh_msi_name
    urllib.request.urlretrieve(openssh_download_url, openssh_msi_path)
    command = ' msiexec /i' + str(openssh_msi_path)
    subprocess.call(command, shell=True)
except Exception as e:
    print(e.args[0])

input('Instalação finalizada, pressione qualquer tecla para fechar...')