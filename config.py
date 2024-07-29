from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
STRING = getenv("STRING_SESSION", "BAF4bRkAELt0ciL_mMqReLlWSZkG9WvIRWRT9YELVLaDRMZ3a61ksx6Vo7rSmpxWp5qFAwVBay_N4LXxxPxFQtSbDDPHFJvT_aSbusYJoQtWGnxck7P1WY7Fk-cOsiAfIAOaXYzDb5WUmZ-64-ImnOdJXJBYgHFn934OEx3-QjX3V46zUH8cEkQgrbjTB9aC1nj5jvCbThKJc8wEnTNQVuxdltnCk3_1az3iiA2qWjmWXHHk1M6X3rkWkDLey1wEnDkNJ9Olr2id0sVf_R1RcgS-94anpdfU4yTpzT_YVFzbMYVVN7LlU600OjHAufCKx6DYeMrknqWlOfOlRi2TLy8QQvvkuwAAAAG3GP96AA")
BOT_TOKEN = getenv("BOT_TOKEN" ,"7252009826:AAHuBH6GOMLuf291IWaSY-_SGkmpTewxlSI")
API_ID = int(getenv("API_ID", "24669465"))
API_HASH = getenv("API_HASH","ef15199702ea76ebb2ebe4eca477ab60")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "999999"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://denemehesabb0:<izmirin664>@izmirin664.yhknsgf.mongodb.net/?retryWrites=true&w=majority&appName=izmirin664")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6623140842").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "6623140842").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-4256062628"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME","Logi")
if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))
