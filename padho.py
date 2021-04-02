#Idea By @ProgrammingError
#Made By @ProgrammingError
#Thanks To Google😂😂😂

import requests, random, os
from decouple import config
from telethon import Button, custom, events, functions, TelegramClient
import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)

tgbot = TelegramClient('NoobiezBots', APP_ID, API_HASH).start(bot_token=BOT_TOKEN)


dc=(random.randrange(1,3))
if dc==1:
    API_KEY = "AIzaSyAyDBsY3WRtB5YPC6aB_w8JAy6ZdXNc6FU"
if dc==2: 
    API_KEY = "AIzaSyBF0zxLlYlPMp9xwMQqVKCQRq8DgdrLXsg"
if dc==3:
    API_KEY = "AIzaSyDdOKnwnPwVIQ_lbH5sYE4FoXjAKIQV0DQ"
if dc==4:
    API_KEY = "AIzaSyC2BAHB0MVs9q_vxTAIzbUB4VKug3cptT4"
SEARCH_ENGINE_ID = "d99e58572df67b77a"

@tgbot.on(events.InlineQuery(pattern=r"(.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    query = event.pattern_match.group(1)
    if event.query.user_id:
        
        piggi = 1
        padhai = []
        start = (piggi - 1) * 3 + 1
        
        programmingerror = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
        shivambro = requests.get(programmingerror).json()
        search_items = shivambro.get("items")
        
        for i, search_item in enumerate(search_items, start=1):
            title = search_item.get("title")
            #Idea By @ProgrammingError
    #Made By @ProgrammingError
    #Thanks To Google😂😂😂# https://www.googleapis.com/customsearch/v1?key=AIzaSyAyDBsY3WRtB5YPC6aB_w8JAy6ZdXNc6FU&cx=d99e58572df67b77a&q=vector
            danish_00 = search_item.get("link")
            atul_xd = search_item.get("snippet")
            #Idea By @ProgrammingError
    #Made By @ProgrammingError
    #Thanks To Google😂😂😂
            toppers = f"{title}\n\nAnswer in Short:\n   {atul_xd}"
            padho = f"{title}"
            padhai.append(
                await event.builder.article(
                    title=padho,
                    description=f"{atul_xd}",#Idea By @ProgrammingError
    #Made By @ProgrammingError
    #Thanks To Google😂😂😂
                    text=toppers,
                    buttons=[[Button.url('Answer', f"{danish_00}")],[Button.switch_inline(
                        "Search Again", query="ques ", same_peer=True)
                    ],],
                )
            )
        await event.answer(padhai)

tgbot.run_until_disconnected()
