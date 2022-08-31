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
)

menu = [
    ["1", "- Instalar Chocolatey", install_chocolatey],
    ["2", "- Instalar Google Chrome", install_google_chrome],
    ["3", "- Instalar Firefox", install_firefox],
    ["4", "- Instalar Java", install_java],
    ["5", "- Instalar Spark", install_spark],
    ["6", "- Instalar Anydesk", install_anydesk],
    ["7", "- Instalar Teamviewer", install_teamviewer],
    ["8", "- Instalar Adobe Air", install_adobeair],
    ["9", "- Instalar Sisbr2.0", install_sisbr20],
    ["10", "- Instalar Citrix 10", install_citrix10],
    ["11", "- Instalar Caixa", install_caixa],
]

for i in menu:
    print(i[0], i[1])
print('12 - Instalar tudo')

status = input("Digite a opção desejada:")

if status == '12':
    for i in menu:
        i[2]()
else:
    for i in menu:
        if status == i[0]:
            i[2]()

input("Instalação finalizada, pressione qualquer tecla para fechar...")
