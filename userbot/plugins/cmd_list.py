import asyncio

from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="cmds", outgoing=True))
async def install(event):
    if event.fwd_from:
        return
    cmd = "ls userbot/plugins"
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = f"**List of Plugins in HellBot:**\n`{o}`\n\n**TIP:** __If you want to know the commands for a plugin, do:-__ \n `.help <plugin name>` **without the < > brackets.**\n__Some plugins might not work directly.\n Go to @HellBot_Official Chat group for assistance..."
    await event.edit(OUTPUT)
