import asyncio
import os
from pathlib import Path

from ..utils import load_module, remove_plugin
from . import ALIVE_NAME, CMD_LIST, SUDO_LIST

DELETE_TIMEOUT = 5
thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"


@bot.on(admin_cmd(pattern="install$"))
@bot.on(sudo_cmd(pattern="install$", allow_sudo=True))
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = await event.client.download_media(
                await event.get_reply_message(),
                "userbot/plugins/",
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await edit_or_reply(
                    event,
                    f"Installed Plugin `{os.path.basename(downloaded_file_name)}`",
                )
            else:
                os.remove(downloaded_file_name)
                await edit_or_reply(
                    event, "Errors! This plugin is already installed/pre-installed."
                )
        except Exception as e:
            await edit_or_reply(event, str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()


@bot.on(admin_cmd(pattern=r"load (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"load (.*)", allow_sudo=True))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match.group(1)
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        await edit_or_reply(event, f"Successfully loaded {shortname}")
    except Exception as e:
        await edit_or_reply(
            event,
            f"Could not load {shortname} because of the following error.\n{str(e)}",
        )


@bot.on(admin_cmd(pattern=r"unload (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"unload (.*)", allow_sudo=True))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match.group(1)
    try:
        remove_plugin(shortname)
        await edit_or_reply(event, f"Unloaded {shortname} successfully")
    except Exception as e:
        await edit_or_reply(event, f"Successfully unload {shortname}\n{str(e)}")


@bot.on(admin_cmd(pattern=r"uninstall (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"uninstall (.*)", allow_sudo=True))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match.group(1)
    path = Path(f"userbot/plugins/{shortname}.py")
    if not os.path.exists(path):
        return await edit_delete(
            event, f"There is no plugin with path {path} to uninstall it"
        )
    os.remove(path)
    if shortname in CMD_LIST:
        CMD_LIST.pop(shortname)
    if shortname in SUDO_LIST:
        SUDO_LIST.pop(shortname)
    if shortname in CMD_HELP:
        CMD_HELP.pop(shortname)
    try:
        remove_plugin(shortname)
        await edit_or_reply(event, f"{shortname} is Uninstalled successfully")
    except Exception as e:
        await edit_or_reply(event, f"Successfully uninstalled {shortname}\n{str(e)}")


CMD_HELP.update(
    {
        "corecmds": """**Plugin : **`corecmds`
  •  **Syntax : **`.install`
  •  **Function : **__Reply to any external plugin to install in bot__ 
  
  •  **Syntax : **`.load <plugin name>`
  •  **Function : **__To load that plugin again__
  
  •  **Syntax : **`.unload <plugin name>`
  •  **Function : **__To stop functioning of that plugin__ 
  
  •  **Syntax : **`.uninstall <plugin name>`
  •  **Function : **__To stop functioning of that plugin and remove that plugin from bot__ 
  
**Note : **__To unload a plugin permenantly from bot set __`NO_LOAD`__ var in heroku with that plugin name with space between plugin names__"""
    }
)
