import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

pr0fess0r_99=Client(
    "𝔹𝕆𝕋 𝕊𝕋𝔸ℝ𝕋𝔼𝔻 ℙ𝕃𝔼𝔸𝕊𝔼 𝕊𝕌𝔹𝕊ℂℝ𝕀𝔹𝔼ℝ 𝕊𝔽ℙ 𝔽𝕀𝕃𝕄𝕊",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

CHAT_ID=int(os.environ.get("CHAT_ID", None))
TEXT=os.environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYour Auto Approved")
APPROVED = os.environ.get("APPROVED_WELCOME", "on").lower()

@pr0fess0r_99.on_message(filters.private & filters.command(["start"]))
async def start(client: pr0fess0r_99, message: Message):
    approvedbot = await client.get_me() 
    button=[[
      InlineKeyboardButton("𝚄𝙿𝙳𝙰𝚃𝙴𝚉", url="https://t.me/sinhalaflims"),
      InlineKeyboardButton("𝚂𝚄𝙿𝙿𝙾𝚁𝚃", url="https://t.me/sinhalaflims")
      ],[
      InlineKeyboardButton("AD BOOSTER 🚀", url=f"https://t.me/Adboosterlk")
      ]]
    await message.reply_text(text="**𝙷𝙴𝙻𝙻𝙾...⚡\n\n𝙸𝙰𝙼 𝙰 𝚂𝙸𝙼𝙿𝙻𝙴 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙰𝚄𝚃𝙾 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙰𝙲𝙲𝙴𝙿𝚃 𝙱𝙾𝚃.\n𝙵𝙾𝚁 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝚃𝚂 𝙲𝚁𝙴𝙰𝚃𝙴 𝙾𝙽𝙴 𝙱𝙾𝚃...**", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@pr0fess0r_99.on_chat_join_request(filters.chat(CHAT_ID))
async def autoapprove(client: pr0fess0r_99, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} 𝙹𝙾𝙸𝙽𝙴𝙳 ⚡") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))       

print("𝔹𝕆𝕋 𝕊𝕋𝔸ℝ𝕋𝔼𝔻 ℙ𝕃𝔼𝔸𝕊𝔼 𝕊𝕌𝔹𝕊ℂℝ𝕀𝔹𝔼ℝ 𝕊𝔽ℙ 𝔽𝕀𝕃𝕄𝕊")
pr0fess0r_99.run()
