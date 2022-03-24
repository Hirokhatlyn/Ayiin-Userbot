# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


from datetime import datetime as dt

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import ayiin_cmd, edit_or_reply


@ayiin_cmd(pattern="btpm(?: |$)(.*)")
async def listbtpm(list):
    ayiin = await edit_or_reply(list, "`Processing...`")
    if list.pattern_match.group(1):
        text, link = list.pattern_match.group(1).split()
    else:
        await list.edit("**Yang Benerlah Kentod, Biar Bisa Buat List!!!**")
        return

    n_ch = text.replace(".", " ")
    d_form = "%d - %B - %Y"
    user = await list.client.get_me()
    await ayiin.edit(f"**𝙱𝚃𝙿𝙼 𝙲𝙷:** {n_ch}\n"
                     f"**𝚃𝙰𝙽𝙶𝙶𝙰𝙻 : {dt.now().strftime(d_form)}**\n\n"
                     f"**𝙰𝙳𝙼𝙸𝙽 : @{user.username}**\n"
                     f"**𝙲𝙷: {link}**\n"
                     f"**----------------------------------**\n"
                     f"**• 𝟶𝟶.𝟶𝟶 - 𝟶𝟸.𝟶𝟶 : **\n"
                     f"**-𝙰𝙳𝙼𝙸𝙽 : **\n"
                     f"**• 𝟶𝟸.𝟶𝟶 - 𝟶𝟺.𝟶𝟶 : **\n"
                     f"**-𝙰𝙳𝙼𝙸𝙽 : **\n"
                     f"**• 𝟶𝟺.𝟶𝟶 - 𝟶𝟼.𝟶𝟶 : **\n"
                     f"**-𝙰𝙳𝙼𝙸𝙽 : **\n"
                     f"**• 𝟶𝟼.𝟶𝟶 - 𝟶𝟾.𝟶𝟶 : **\n"
                     f"**-𝙰𝙳𝙼𝙸𝙽 : **\n"
                     f"**• 𝟶𝟾.𝟶𝟶 - 𝟷𝟶.𝟶𝟶 : **\n"
                     f"**-𝙰𝙳𝙼𝙸𝙽 : **\n"
                     f"**• 𝟷𝟶.𝟶𝟶 - 𝟷𝟸.𝟶𝟶 : **\n"
                     f"**-𝙰𝙳𝙼𝙸𝙽 : **\n"
                     f"**----------------------------------------------**\n"
                     f"**• 𝟷𝟸.𝟶𝟶 - 𝟷𝟺.𝟶𝟶 : **\n"
                     f"**-𝙰𝙳𝙼𝙸𝙽 : **\n"
                     f"**• 𝟷𝟺.𝟶𝟶 - 𝟷𝟼.𝟶𝟶 : **\n"
                     f"**-𝙰𝙳𝙼𝙸𝙽 : **\n"
                     f"**• 𝟷𝟼.𝟶𝟶 - 𝟷𝟾.𝟶𝟶 : **\n"
                     f"**-𝙰𝙳𝙼𝙸𝙽 : **\n"
                     f"**• 𝟷𝟾.𝟶𝟶 - 𝟸𝟶.𝟶𝟶 : **\n"
                     f"**-𝙰𝙳𝙼𝙸𝙽 : **\n"
                     f"**• 𝟸𝟶.𝟶𝟶 - 𝟸𝟸.𝟶𝟶 : **\n"
                     f"**-𝙰𝙳𝙼𝙸𝙽 : **\n"
                     f"**• 𝟸𝟸.𝟶𝟶 - 𝟶𝟶.𝟶𝟶 : **\n"
                     f"**-𝙰𝙳𝙼𝙸𝙽 : **\n"
                     f"**-----------------------------------------------**\n"
                     f"**❗𝙼𝚊𝚞 𝟸 𝚓𝚊𝚖 𝚕𝚎𝚋𝚒𝚑 𝚋𝚒𝚜𝚊 𝚕𝚊𝚗𝚐𝚜𝚞𝚗𝚐 𝚕𝚒𝚜𝚝**\n"
                     f"**❗𝙺𝚘𝚗𝚝𝚎𝚗 𝚔𝚎𝚎𝚙 𝟷 𝚇 𝟸𝟺 𝚓𝚊𝚖**\n"
                     f"**❗️𝙽𝙾 𝚂𝙷𝙾𝚁𝚃𝙻𝙸𝙽𝙺**")


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "btpmayiin": f"**Plugin:** `btpmayiin`\
        \n\n  • **Perintah :** `{cmd}btpm` <nama_ch (TanpaSpasi)> <username ch>\
        \n  •  **Kegunaan :** __Untuk Mendapatkan List Btpm Kosong.__\
    "
    }
)
