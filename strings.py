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
'''  # TODO

def REFERRAL(id):  # TODO
    return f'''
https://t.me/your_bot_name?start={id}
'''

class APP:
    MESSAGE = '''
None
''' # TODO
    class CALLBACK:
        ANDROID = "android"
        IOS = "ios"
        WINDOWS = "windows"
        MACOS = "macos"
        OTHER = "other"

    class ANSWER: # TODO
        ANDROID = "android"
        IOS = "ios"
        WINDOWS = "windows"
        MACOS = "macos"
        OTHER = "other"

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