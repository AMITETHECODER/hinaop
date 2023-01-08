class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "11450167"
    API_HASH = "d0d147646f5c54e7d2324ddc873bc90c"

    CASH_API_KEY = "1T4JPU6WMF1DG7EI"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://bvniqxvs:dmsixK9EmuQXESa7i79XGPdpN8rBd7XC@dumbo.db.elephantsql.com/bvniqxvs"  # A sql database url from elephantsql.com

    EVENT_LOGS = "-1001762139427"  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://lunaop:lunaopop@cluster0.6iqsuld.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/538c2560d0dfb51e8bfe8.jpg"

    SUPPORT_CHAT = "timepassxdman"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5624877035:AAG01fApnckLJoSCV-V1XwasIRQRLD9dndw"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "B85ZUBOAF86M"  # Get this value from https://timezonedb.com/api

    OWNER_ID = "5222353449"  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [5222353449]  # User id of sudo users
    DEV_USERS = [5222353449]  # User id of dev users
    DEMONS = [5021231683]  # User id of support users
    TIGERS = [5021231683]  # User id of tiger users
    WOLVES = [5733263480]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
