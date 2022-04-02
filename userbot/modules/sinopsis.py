"""
Sinopsis scraper.
t.me/erruuu
"""

import requests
from bs4 import BeautifulSoup as bs
import re
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.sinop ?(.*)")
async def _(event):
    xurl = "https://neonime.watch/episode/"
    url = event.pattern_match.group(1)
    url = url.replace(" ", "-")
    if not url:
        await event.edit("Enter anime title, see .help sinopsis")
    else:
        await event.edit("`please wait..`")
        neourl = requests.get(xurl + url)
        neopage = bs(neourl.content, 'html.parser')
        altimg = neopage.find(itemprop="image")
        if not altimg:
            await event.edit("Not found...")
        else:
            ttl = altimg["alt"]
            msg = f"<b>➲ Sinopsis <a href='{xurl}{url}'>{ttl}</a></b>\n"
            bts = 7*"═"
            msg += f"{bts}\n"
            neos = neopage.find("div", class_="contenidotv")
            neop = neos.find(itemprop="description")
            for sino in neop.find_all('p'):
                msg += f"<b>{sino}</b>\n"

        await event.edit(msg, link_preview=False, parse_mode="html")


CMD_HELP.update(
    {
        "sinopsis": "**Sinopsis**"
        "\n ➲`.sinop` title"
        "\n ➣ ex: `.sinop aharen`"
    }
)
