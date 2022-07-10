import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "12479561")
    API_HASH = getenv("API_HASH", "3fdb18b5d47c107279014b5e6b120dda")
    TOKEN = getenv("TOKEN", "5416154782:AAFEIUmrqpfa-QAhXbozcHA1MW_gj757-lw")
    OWNER_ID = getenv("OWNER_ID", "12479561")
    STRING_SESSION = getenv("STRING_SESSION", "1BVtsOGgBu2wESU4f7_aFcA6iVBXv3AWaX1O0w3EmzpTTuGZS62ybmE_v6nMfO4bEpSJQ_7s0exMkN_hpHJtdaoQ3kYsWJIm6_gUDMD_8xAOQkqM1w7QVcXPCVeBImNOt-WjmWXh7LwXWjzppAVDN-R81yVJTsKDrRbC-WZsudDLbm_EACyNG9F2T-mko-D0iCRQRX0x2CBX27du4WqZYEg3I1MtLjyY5vKuf3E0BlUN_3T2m4tJXnIYBDoIemLmjLWJNjuAlHsZLJYJhbWO--aSlTqy4VoGVklr_GgsTju28752Mh_wG17qjlhjTaQa_cOskhjZyYbiMhhE7q7LLiu2hrQbnMzI=")
    OWNER_USERNAME = getenv("OWNER_USERNAME", "baytoddd")
    DB_URI = getenv("DATABASE_URL", "postgresql://sqfasbbh:gZB4IVNwh3tKHMQjLkEbaCjHXcXDJ24l@abul.db.elephantsql.com/sqfasbbh")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1001763422160")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1001763422160")
    SYS_ADMIN = getenv("SYS_ADMIN", "12479561")
    DEV_USERS = getenv("DEV_USERS", "12479561")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CASH_API_KEY = getenv("CASH_API_KEY", "https://www.alphavantage.co/support/#api-key")
    TIME_API_KEY = getenv("TIME_API_KEY", "https://timezonedb.com/api")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "https://t.me/SpamWatchBot")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "1669178360").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
