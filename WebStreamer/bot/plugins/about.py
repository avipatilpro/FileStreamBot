from pyrogram import Client, Filters


@Client.on_message(Filters.command(["about"]))
async def start(client, message):
    helptxt = f"Created for 😘😘 you only 😍"
    await message.reply_text(helptxt)
