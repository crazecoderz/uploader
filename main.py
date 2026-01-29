import os
from pyrogram import Client, filters
from pyrogram.types import Message

# ========== ENV VARIABLES ==========
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

# ========== BASIC CHECK ==========
if not BOT_TOKEN or not API_ID or not API_HASH:
    raise RuntimeError("BOT_TOKEN / API_ID / API_HASH missing in Environment Variables")

# ========== BOT INIT ==========
app = Client(
    "UGUploaderBot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

# ========== MEMORY STORAGE (NO DB) ==========
USERS = set()

# ========== COMMANDS ==========

@app.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message: Message):
    USERS.add(message.from_user.id)
    await message.reply_text(
        "👋 Hello!\n\n"
        "✅ Bot is running without MongoDB\n"
        "📤 Send me a file to upload\n\n"
        "⚠️ Data is temporary (memory only)"
    )

@app.on_message(filters.private & filters.document)
async def file_handler(client, message: Message):
    await message.reply_text("📥 File received!\n(Upload logic yahan add kar sakte ho)")

# ========== RUN ==========
print("🤖 Bot Started (No MongoDB)")
app.run()
