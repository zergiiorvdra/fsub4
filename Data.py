# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Perintah untuk Pengguna BOT
 ├ /start - Mulai Bot
 ├ /about - Tentang Bot ini
 ├ /help - Bantuan Perintah Bot ini
 └ /ping - Untuk mengecek bot hidup 

👨‍💻 Develoved by @ZERGIIORVDRA</b>
"""

    close = [
        [InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ", callback_data="about"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    ABOUT = """
<b>Tentang Bot ini:

@{} adalah Bot Telegram untuk menyimpan Postingan atau File yang dapat Diakses melalui Link Khusus.

 • Creator: @{}
 • Source Code: <a href='https://github.com/zergiiorvdra/fsub4'>Zer-FileSharing 4</a>
 • Owner Repo: @ZERGIIORVDRA

👨‍💻 Develoved by @ZERGIIORVDRA</b>
"""
