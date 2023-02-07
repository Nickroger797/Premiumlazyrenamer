"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price 💰Rs80💰  ind /🌎 0.9$  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price 💰Rs150💰  ind /🌎 1.8$  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price 💰Rs250💰  ind /🌎 3.2$  per Month
	
	
	Pay Using Upi I'd ```7070477289@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin @mdiskbot200"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/mdiskbot200")], 
        			[InlineKeyboardButton("Silver Plan 💰Rs80💰",url = "https://p.paytm.me/xCTH/vo37hii9"),
        			[InlineKeyboardButton("Gold Plan 💰Rs150💰",url = "https://p.paytm.me/xCTH/vo37hii9"),
                                InlineKeyboardButton("Diamond Plan 💰Rs250💰",url = "https://p.paytm.me/xCTH/vo37hii9")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price 💰Rs80💰  ind /🌎 0.9$  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price 💰Rs150💰  ind /🌎 1.8$  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price 💰Rs250💰  ind /🌎 3.2$  per Month
	
	
	Pay Using Upi I'd ```7070477289@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin @mdiskbot200"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/mdiskbot200")], 
        			[InlineKeyboardButton("Silver Plan 💰Rs80💰",url = "https://p.paytm.me/xCTH/vo37hii9"),
        			[InlineKeyboardButton("Gold Plan 💰Rs150💰",url = "https://p.paytm.me/xCTH/vo37hii9"),
                                InlineKeyboardButton("Diamond Plan 💰Rs250💰",url = "https://p.paytm.me/xCTH/vo37hii9")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
