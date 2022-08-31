import urllib.request
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
    execute,
)


def install_chocolatey():
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


def install_chocolatey_list():
    print("Instalando programas padrão...")
    try:
        for programa in choco_install_list:
            execute("choco install -y " + programa)
    except Exception as e:
        print(e.args[0])


# Instalacao do Caixa
def install_caixa():
    caixa_file_path = path_local / caixa_file_name
    download_install_google(
        "Caixa",
        caixa_google_id,
        caixa_file_name,
        f"java -jar  {caixa_file_path}",
    )


# Instalacao do Adobe Air
def install_adobeair():
    adobeair_file_path = path_local / adobeair_file_name
    download_install_google(
        "Adobe Air",
        adobeair_google_id,
        adobeair_file_name,
        f"{adobeair_file_path}",
    )


# Instalacao do Sisbr2.0
def install_sisbr20():
    sisbr20_file_path = path_local / sisbr20_file_name
    download_install_google(
        "Sisbr 2.0",
        sisbr20_google_id,
        sisbr20_file_name,
        f"{sisbr20_file_path}",
    )


# Instalacao Citrix10
def install_citrix10():
    citrix_path_execution = path_local / "Citrix10" / "Versao 10.1" / "PN_10_1.msi"
    download_install_google_zip(
        "Citrix10",
        citrix_google_id,
        citrix_file_name,
        f"msiexec /i {citrix_path_execution}",
    )
