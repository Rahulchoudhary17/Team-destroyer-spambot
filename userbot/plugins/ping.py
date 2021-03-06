import asyncio
from datetime import datetime

from . import mention


@bot.on(admin_cmd(pattern="ping$"))
@bot.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    event = await edit_or_reply(event, "Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f"š š£š¼š»š“!\n`{ms} šŗš`\nMere_aaka: {mention}")


@bot.on(admin_cmd(pattern=f"fping$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"fping$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    animation_interval = 0.2
    animation_ttl = range(26)
    event = await edit_or_reply(event, "ping....")
    animation_chars = [
 "My šµ š® š³ š¬  Is : Calculating...",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 26])
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        "āāāāāāāāāā¬ā¬ā¬ā¬ā¬ā¬ā¬ā¬ā¬\nā¬š¶š¶š¶š¶š¶š¶š¶ā¬\nā¬ā¬ā¬ā¬š¶ā¬ā¬š¶ā¬\nā¬ā¬ā¬ā¬š¶ā¬ā¬š¶ā¬\nā¬ā¬ā¬ā¬š¶ā¬ā¬š¶ā¬\nā¬ā¬ā¬ā¬ā¬š¶š¶ā¬ā¬\nā¬ā¬ā¬ā¬ā¬ā¬ā¬ā¬ā¬\nā¬ā¬š¶š¶š¶š¶š¶ā¬ā¬\nā¬š¶ā¬ā¬ā¬ā¬ā¬š¶ā¬\nā¬š¶ā¬ā¬ā¬ā¬ā¬š¶ā¬\nā¬š¶ā¬ā¬ā¬ā¬ā¬š¶ā¬\nā¬ā¬š¶š¶š¶š¶š¶ā¬ā¬\nā¬ā¬ā¬ā¬ā¬ā¬ā¬ā¬ā¬\nā¬š¶š¶š¶š¶š¶š¶š¶ā¬\nā¬ā¬ā¬ā¬ā¬ā¬š¶ā¬ā¬\nā¬ā¬ā¬ā¬ā¬š¶ā¬ā¬ā¬\nā¬ā¬ā¬ā¬š¶ā¬ā¬ā¬ā¬\nā¬š¶š¶š¶š¶š¶š¶š¶ā¬\nā¬ā¬ā¬ā¬ā¬ā¬ā¬ā¬ā¬\nā¬ā¬š¶š¶š¶š¶š¶ā¬ā¬\nā¬š¶ā¬ā¬ā¬ā¬ā¬š¶ā¬\nā¬š¶ā¬ā¬ā¬ā¬ā¬š¶ā¬\nā¬š¶ā¬š¶ā¬ā¬ā¬š¶ā¬\nā¬ā¬š¶š¶ā¬ā¬š¶ā¬ā¬\nā¬ā¬ā¬ā¬ā¬ā¬ā¬ā¬ā¬\nā¬š¶ā¬š¶š¶š¶š¶š¶ā¬\nā¬ā¬ā¬ā¬ā¬ā¬ā¬ā¬ā¬ \nāāāāāāāāā \n \n My šµ š® š³ š¬  Is : {} ms".format(
            ms
        )
    )


CMD_HELP.update(
    {
        "ping": "**Plugin :** `ping`\
    \n\nā¢  **Syntax :** `.ping`\
    \nā¢  **Function : **__Shows you the ping speed of server__\
    \n\nā¢  **Syntax : **`.fping`\
    \nā¢  **Function : **__Shows the server ping with extra animation__\
    "
    }
)
