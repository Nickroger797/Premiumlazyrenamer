"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**ðª Silver Tier ðª** 
	Daily  Upload  limit 10GB
	Price ð°Rs80ð°  ind /ð 0.9$  per Month
	
	**ð« Gold Tier ð«**
	Daily Upload limit 50GB
	Price ð°Rs150ð°  ind /ð 1.8$  per Month
	
	**ð Diamond ð**
	Daily Upload limit 100GB
	Price ð°Rs250ð°  ind /ð 3.2$  per Month
	
	
	Pay Using Upi I'd ```7070477289@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin @mdiskbot200"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN ð",url = "https://t.me/mdiskbot200")], 
        			[InlineKeyboardButton("Silver Plan ð°Rs80ð°",url = "https://paytm.me/AmdC-gs"),
        			InlineKeyboardButton("Gold Plan ð°Rs150ð°",url = "https://paytm.me/LEVS-BX")],
                                [InlineKeyboardButton("Diamond Plan ð°Rs250ð°",url = "https://paytm.me/t6jc-6v"),
                                InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**ðª Silver Tier ðª** 
	Daily  Upload  limit 10GB
	Price ð°Rs80ð°  ind /ð 0.9$  per Month
	
	**ð« Gold Tier ð«**
	Daily Upload limit 50GB
	Price ð°Rs150ð°  ind /ð 1.8$  per Month
	
	**ð Diamond ð**
	Daily Upload limit 100GB
	Price ð°Rs250ð°  ind /ð 3.2$  per Month
	
	
	Pay Using Upi I'd ```7070477289@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin @mdiskbot200"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN ð",url = "https://t.me/mdiskbot200")], 
        			[InlineKeyboardButton("Silver Plan ð°Rs80ð°",url = "https://paytm.me/AmdC-gs"),
        			InlineKeyboardButton("Gold Plan ð°Rs150ð°",url = "https://paytm.me/LEVS-BX")],
                                [InlineKeyboardButton("Diamond Plan ð°Rs250ð°",url = "https://paytm.me/t6jc-6v"),
                                InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
