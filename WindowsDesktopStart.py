from instalacao import (
    install_chocolatey,
    install_google_chrome,
    install_firefox,
    install_java,
    install_spark,
    install_anydesk,
    install_teamviewer,
    install_adobeair,
    install_sisbr20,
    install_citrix10,
    install_caixa,
    install_7zip,
    install_notepadplusplus
)

menu = [
    ["Chocolatey", install_chocolatey],
    ["Google Chrome", install_google_chrome],
    ["Firefox", install_firefox],
    ["Java", install_java],
    ["Spark", install_spark],
    ["Anydesk", install_anydesk],
    ["Teamviewer", install_teamviewer],
    ["Adobe Air", install_adobeair],
    ["7zip", install_7zip],
    ["Notepad++", install_notepadplusplus],
    ["Sisbr2.0", install_sisbr20],
    ["Citrix 10", install_citrix10],
    ["Caixa", install_caixa],
]

while(True):
    for indice, value in enumerate(menu):
        print(indice, '- Instalar ', value[0],)
    print('99 - Instalar tudo')

    status = input("Digite a opção desejada:")

    if status == '99':
        for i in menu:
            i[1]()
    else:
        menu[int(status)][1]()

