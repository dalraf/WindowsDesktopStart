from pathlib import Path
from vars import (
    choco_install_list,
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
)
from functions import (
    download_install_google,
    download_install_google_zip,
    install_chocolatey,
    install_chocolatey_list,
)


# Install chocolatey
install_chocolatey(ps_script_url, ps_script_name)

# Install programas padrão
install_chocolatey_list(choco_install_list)

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
citrix_path_execution = path_local / "Citrix10" / "Versao 10.1" / "PN_10_1.msi"
download_install_google_zip(
    "Citrix",
    citrix_google_id,
    citrix_file_name,
    f"msiexec /i {citrix_path_execution}",
)

input("Instalação finalizada, pressione qualquer tecla para fechar...")
