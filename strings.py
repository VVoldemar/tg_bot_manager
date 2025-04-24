GREETING = '''
VPN
'''   # TODO

def PROFILE(name, subscription, expiration_date):
    return f'''
👤 {name}
📜 {subscription}
🕒 {expiration_date}
'''


APP = '''
'''  # TODO

HELP = '''
❓Какие у вас возникли проблемы?
'''

def REFERRAL(id):  # TODO
    return f'''
https://t.me/your_bot_name?start={id}
'''

class APP:
    MESSAGE = '''
None
''' # TODO

    class BUTTONS:
        ANDROID = "🤖 Android"
        IOS = "📱 IOS"
        WINDOWS = "🖥️ Windows"
        MACOS = "💻 MacOS"
        OTHER = "⚙️ Other"

        
    class CALLBACK:
        ANDROID = "android"
        IOS = "ios"
        WINDOWS = "windows"
        MACOS = "macos"
        OTHER = "other"

    class ANSWER:
        ANDROID = ("1) Запустите приложение WireGuard.\n"
                   "2) Нажмите кнопку \"+\" внизу экрана.\n"
                   "3) Выберите \"Импортировать из файла\" и найдите полученный конфигурационный файл.\n"
                   "4) Либо выберите \"Создать из QR-кода\", если ваш провайдер предоставил QR-код с конфигурацией.\n"
                   )
        IOS = ("Запустите приложение WireGuard.\n"
               "Нажмите кнопку \"+\" вверху экрана.\n"
               "Выберите \"Импортировать из файла или архива\" и найдите полученный конфигурационный файл.\n"
               "Либо выберите \"Создать из QR-кода\".\n"
               )
        WINDOWS = ("Запустите приложение WireGuard.\n"
                   "Нажмите кнопку \"Импортировать туннель из файла...\" или значок \"+\" внизу окна.\n"
                   "Выберите полученный конфигурационный файл (.conf)\n"
                   )
        MACOS = ("Запустите приложение WireGuard.\n"
                 "Нажмите кнопку \"Импортировать туннель...\" или значок \"+\" в левом нижнем углу окна.\n"
                 "Выберите полученный конфигурационный файл (.conf)\n"
                 )
        OTHER = ("**Ubuntu**\n"
                 "`sudo apt install wireguard`\n"
                 "\n"
                 "**Debian** \n"
                 "`apt install wireguard`\n"
                 "\n"
                 "**Fedora**\n"
                 "`sudo dnf install wireguard-tools`\n"
                 "\n"
                 "**Arch**\n"
                 "`sudo pacman -S wireguard-tools`\n")

    class LINKS:
        ANDROID = "https://play.google.com/store/apps/details?id=com.wireguard.android"
        IOS = "https://itunes.apple.com/us/app/wireguard/id1441195209?ls=1&mt=8"
        WINDOWS = "https://download.wireguard.com/windows-client/wireguard-installer.exe"
        MACOS = "https://itunes.apple.com/us/app/wireguard/id1451685025?ls=1&mt=12"
        OTHER = "https://www.wireguard.com/install/"

    OPEN = "🔗 Скачать"


class KEYBOARD:
    PROFILE = "👤 Профиль"
    BUY = "🎟️ Получить"
    APP = "🧰 Программа"
    CONFIG = "📜 Конфиг"
    HELP = "🆘 Поддержка"
    REFERRAL = "🔗 Привести друга"