from pyrogram import Client, filters
import re

API_ID = 20473364
API_HASH = "bdff11a8638e06334438c3033ea9d155"
BOT_TOKEN = "7725440049:AAHyouGmJpvMH9l7Pw0DvpDJhKwLX_2AbBI"

app = Client(
    "autodelete-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# URL ডিটেক্টর Regex
url_pattern = r"https?://\S+|www\.\S+"

@app.on_message(filters.group)
async def delete_forward_or_link(client, message):
    # Forwarded message
    if message.forward_from or message.forward_sender_name:
        await message.delete()
        return

    # URL check
    if message.text and re.search(url_pattern, message.text):
        await message.delete()

app.run()