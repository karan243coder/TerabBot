from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import logging
import asyncio
from datetime import datetime
from pyrogram.enums import ChatMemberStatus
from dotenv import load_dotenv
import os
from status import format_progress_bar
from video import download_video, upload_video
from web import keep_alive

# Load environment variables
load_dotenv('config.env', override=True)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Get environment variables
api_id = os.environ.get('TELEGRAM_API', '')
if not api_id:
    logging.error("TELEGRAM_API variable is missing! Exiting now")
    exit(1)

api_hash = os.environ.get('TELEGRAM_HASH', '')
if not api_hash:
    logging.error("TELEGRAM_HASH variable is missing! Exiting now")
    exit(1)

bot_token = os.environ.get('BOT_TOKEN', '')
if not bot_token:
    logging.error("BOT_TOKEN variable is missing! Exiting now")
    exit(1)

dump_id = os.environ.get('DUMP_CHAT_ID', '')
if not dump_id:
    logging.error("DUMP_CHAT_ID variable is missing! Exiting now")
    exit(1)
else:
    dump_id = int(dump_id)

fsub_id = os.environ.get('FSUB_ID', '')
if not fsub_id:
    logging.error("FSUB_ID variable is missing! Exiting now")
    exit(1)
else:
    fsub_id = int(fsub_id)

# Initialize the bot client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    sticker_message = await message.reply_sticker("CAACAgIAAxkBAAEYonplzwrczhVu3I6HqPBzro3L2JU6YAACvAUAAj-VzAoTSKpoG9FPRjQE")
    await asyncio.sleep(2)
    await sticker_message.delete()
    user_mention = message.from_user.mention
    reply_message = f"ᴡᴇʟᴄᴏᴍᴇ, {user_mention}.\n\n🌟 ɪ ᴀᴍ ᴀ ᴛᴇʀᴀʙᴏx ᴅᴏᴡɴʟᴏᴀᴅᴇʀ ʙᴏᴛ. sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴛᴇʀᴀʙᴏx ʟɪɴᴋ ɪ ᴡɪʟʟ ᴅᴏᴡɴʟᴏᴀᴅ ᴡɪᴛʜɪɴ ғᴇᴡ sᴇᴄᴏɴᴅs ᴀɴᴅ sᴇɴᴅ ɪᴛ ᴛᴏ ʏᴏᴜ ✨."
    join_button = InlineKeyboardButton("ᴊᴏɪɴ ❤️🚀", url="https://t.me/jetmirror")
    developer_button = InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ ⚡️", url="https://t.me/hrishikesh2861")
    reply_markup = InlineKeyboardMarkup([[join_button, developer_button]])
    video_file_id = "/app/Jet-Mirror.mp4"
    
    if os.path.exists(video_file_id):
        await client.send_video(
            chat_id=message.chat.id,
            video=video_file_id,
            caption=reply_message,
            reply_markup=reply_markup
        )
    else:
        await message.reply_text(reply_message, reply_markup=reply_markup)

async def is_user_member(client, user_id):
    try:
        member = await client.get_chat_member(fsub_id, user_id)
        logging.info(f"User  {user_id} membership status: {member.status}")
        return member.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]
    except Exception as e:
        logging.error(f"Error checking membership status for user {user_id}: {e}")
        return False

@app.on_message(filters.text)
async def handle_message(client, message: Message):
    if message.from_user is None:
        logging.error("Message does not contain user information.")
        return

    user_id = message.from_user.id
    user_mention = message.from_user.mention
    is_member = await is_user_member(client, user_id)

    if not is_member:
        join_button = InlineKeyboardButton("ᴊᴏɪɴ ❤️🚀", url="https://t.me/jetmirror")
        reply_markup = InlineKeyboardMarkup([[join_button]])
        await message.reply_text("ʏᴏᴜ ᴍᴜsᴛ ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ.", reply_markup=reply_markup)
        return

    valid_domains = [
        'terabox.com', 'nephobox.com', '4funbox.com', 'mirrobox.com', 
        'momerybox.com', 'teraboxapp.com', '1024tera.com', 
        'terabox.app', 'gibibox.com', 'goaibox.com', 'terasharelink.com', 'teraboxlink.com', 'terafileshare.com'
    ]

    terabox_link = message.text.strip()

    if not any(domain in terabox_link for domain in valid_domains):
        await message.reply_text("ᴘʟᴇᴀsᴇ sᴇɴᴅ ᴀ ᴠᴀʟɪᴅ ᴛᴇʀᴀʙᴏx ʟɪɴᴋ.")
        return

    reply_msg = await message.reply_text("

    

if __name__ == "__main__":
    keep_alive()
    app.run()
