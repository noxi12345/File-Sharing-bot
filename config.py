# (©)Codexbotz
# Recife By Zaen @Mafia_Tobatz
# Kalo clone Gak usah hapus 
# gue tandain akun tele nya ngentod


import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6352551921:AAGXHeg3O2U4x754OSsFfcO2xCyiddK02oA")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "26120934"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "d947cc0927226f527f33b65d63250973")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001595024077"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "-1001862948992"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "@Mafia_Tobatz")

# Database
DB_URI = os.environ.get("DATABASE_URL", "")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "Lunatic0de")
GROUP = os.environ.get("GROUP", "SharingUserbot")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001844137833"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "0"))

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1001918274790"))
FORCE_SUB_GROUP1 = int(os.environ.get("FORCE_SUB_GROUP1", "0"))

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "@goblokyatim").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nAnda harus bergabung di Channel/Grup saya Terlebih dahulu untuk Melihat File yang saya Bagikan\n\nSilakan Join Ke Channel & Group Terlebih Dahulu</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", jangan lupa share tod)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "True" ) == "True"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)
ADMINS.append(844432220)
ADMINS.append(1750080384)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
