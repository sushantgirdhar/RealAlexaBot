import subprocess
import html
import json
import random
from random import randrange
import time
from telethon.tl.types import ChannelParticipantsAdmins
import re
import html
import wikipedia
import html
from typing import Optional, List
from telethon import events
import datetime
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from datetime import timedelta
from telethon.tl.types import UserStatusEmpty, UserStatusLastMonth, UserStatusLastWeek, UserStatusOffline, UserStatusOnline, UserStatusRecently, ChannelParticipantsKicked, ChatBannedRights
from telethon.tl import functions, types
from time import sleep
import asyncio
from telegram import Message, Chat, Update, Bot, User, ParseMode
from telegram.error import BadRequest
from telegram.ext import run_async, Filters
from telegram.utils.helpers import mention_html
from haruka import dispatcher, LOGGER, CHROME_DRIVER, GOOGLE_CHROME_BIN
from haruka.modules.disable import DisableAbleCommandHandler
from haruka.modules.helper_funcs.chat_status import bot_admin, user_admin, is_user_ban_protected, can_restrict, \
    is_user_admin, is_user_in_chat
from haruka.modules.helper_funcs.extraction import extract_user_and_text
from haruka.modules.helper_funcs.string_handling import extract_time
from haruka.modules.log_channel import loggable
from haruka.modules.translations.strings import tld
import re
from pyDownload import Downloader
import datetime
import time
import os
from haruka.modules.helper_funcs.telethon.chat_status import user_is_ban_protectedd, user_is_adminn, is_user_adminn, haruka_is_adminn, is_user_in_chatt, can_delete_messagess, can_change_infoo, can_ban_userss, can_invite_userss, can_add_adminss, can_pin_messagess
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
import pytz
from io import BytesIO 
from time import sleep
from typing import Optional, List
from telegram import TelegramError, Chat, Message
from telegram import Update, Bot, User
from telegram import ParseMode
from telegram.error import BadRequest
from telegram.ext import MessageHandler, Filters, CommandHandler
from telegram.ext.dispatcher import run_async
from telegram.utils.helpers import escape_markdown
from haruka.modules.helper_funcs.chat_status import is_user_ban_protected, user_admin
import random
import telegram
import haruka.modules.sql.users_sql as sql
from haruka import dispatcher, OWNER_ID, SUDO_USERS, SUPPORT_USERS, LOGGER, OCR_SPACE_API_KEY, IBM_WATSON_CRED_URL, IBM_WATSON_CRED_PASSWORD
from haruka.modules.helper_funcs.filters import CustomFilters
from haruka.modules.disable import DisableAbleCommandHandler
USERS_GROUP = 4
import os
import re
import requests
from haruka.modules.helper_funcs.chat_status import bot_admin, can_promote, user_admin, can_pin
import urllib
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
from typing import List
from telegram import ParseMode, InputMediaPhoto, Update, Bot, TelegramError
from telegram.ext import run_async
from haruka import dispatcher
from haruka.modules.disable import DisableAbleCommandHandler
from googleapiclient.discovery import build
import requests 
import urllib.request
from haruka.modules.helper_funcs.chat_status import user_admin, is_user_admin

from telethon.errors import (BadRequestError, ChatAdminRequiredError,
                             ImageProcessFailedError, PhotoCropSizeSmallError,
                             UserAdminInvalidError)
from telethon.errors.rpcerrorlist import (UserIdInvalidError,
                                          MessageTooLongError)
from telethon.tl.functions.channels import (EditAdminRequest,
                                            EditBannedRequest,
                                            EditPhotoRequest)
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (PeerChat, PeerChannel,
                               ChannelParticipantsAdmins, ChatAdminRights,
                               ChatBannedRights, MessageEntityMentionName,
                               MessageMediaPhoto, ChannelParticipantsBots)
from telethon import events
from telethon.errors import YouBlockedUserError
import asyncio
import datetime
import time
from telethon import events
import pytz
import pyfiglet
from urllib.parse import quote_plus
from urllib.error import HTTPError
from telethon import events, functions
import sys
import datetime
import asyncio
import os
import subprocess
import datetime
import os
import time
from bs4 import BeautifulSoup as bs 
import requests
from telethon import events
import asyncio
from telegraph import Telegraph
from googleapiclient.errors import HttpError
import asyncio
import shutil
from bs4 import BeautifulSoup
import re
from time import sleep
from html import unescape
from re import findall
from urllib.parse import quote_plus
from urllib.error import HTTPError
from gtts import gTTS
from wikipedia import summary
from wikipedia.exceptions import DisambiguationError, PageError
import os
import time
import math
import asyncio
import shutil
from youtube_dl import YoutubeDL
from youtube_dl.utils import (DownloadError, ContentTooShortError,
                              ExtractorError, GeoRestrictedError,
                              MaxDownloadsReached, PostProcessingError,
                              UnavailableVideoError, XAttrMetadataError)
from html import unescape
from typing import Optional, List
import os
from gtts import gTTS, gTTSError
import requests
from requests import get
from telegram import Message, Chat, Update, Bot
from telegram.ext import run_async
from haruka import dispatcher, updater
from haruka.modules.disable import DisableAbleCommandHandler
from telegram import ChatAction
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import Message, Update, Bot, User, Chat
from telegram import ParseMode, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, run_async, Filters
from telegram.utils.helpers import escape_markdown, mention_html
from telegram.error import BadRequest

from haruka import dispatcher, OWNER_ID, SUDO_USERS, SUPPORT_USERS, WHITELIST_USERS, tbot, OPENWEATHERMAP_ID, YOUTUBE_API_KEY, TEMP_DOWNLOAD_DIRECTORY
from haruka.__main__ import GDPR
from haruka.__main__ import STATS, USER_INFO
from haruka.modules.disable import DisableAbleCommandHandler
from haruka.modules.helper_funcs.extraction import extract_user
from haruka.modules.translations.strings import tld
from haruka.events import register
from requests import get
from telethon import events
from telethon.errors import YouBlockedUserError
import asyncio
from re import findall
from shutil import rmtree
from urllib.error import HTTPError
from wikipedia import summary
import asyncio
from telethon.errors import FloodWaitError
from haruka import tbot
from haruka.events import register
from wikipedia.exceptions import DisambiguationError, PageError
import os
import time
import math
import asyncio
import shutil
import requests
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, run_async, Filters
from telegram.utils.helpers import escape_markdown, mention_html
from telegram.error import BadRequest
from haruka import dispatcher, OWNER_ID, SUDO_USERS, SUPPORT_USERS, WHITELIST_USERS
from haruka.__main__ import GDPR
from haruka.__main__ import STATS, USER_INFO
from haruka.modules.disable import DisableAbleCommandHandler
from haruka.modules.helper_funcs.extraction import extract_user
from haruka.modules.translations.strings import tld
from requests import get
from youtube_dl import YoutubeDL
from youtube_dl.utils import (DownloadError, ContentTooShortError,
                              ExtractorError, GeoRestrictedError,
                              MaxDownloadsReached, PostProcessingError,
                              UnavailableVideoError, XAttrMetadataError)
from asyncio import sleep
from telethon.tl.types import DocumentAttributeAudio
from collections import deque
from googleapiclient.discovery import build
from html import unescape
import requests

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)

UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)
# ==================================#
from random import randint
from datetime import datetime
from typing import Optional, List
from typing import Optional, List
from hurry.filesize import size
import requests
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode, ReplyKeyboardRemove, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, run_async, Filters
from telegram.utils.helpers import escape_markdown, mention_html
from haruka import dispatcher, OWNER_ID, SUDO_USERS, SUPPORT_USERS, WHITELIST_USERS, BAN_STICKER
from haruka.__main__ import GDPR
from haruka.__main__ import STATS, USER_INFO
from haruka.modules.disable import DisableAbleCommandHandler
from haruka.modules.helper_funcs.extraction import extract_user
from haruka.modules.helper_funcs.filters import CustomFilters
from haruka.modules.rextester.api import Rextester, CompilerError
from haruka.modules.rextester.langs import languages
from haruka.modules.sql.translation import prev_locale
from haruka.modules.translations.strings import tld
from requests import get



async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):

        return isinstance(
            (await tbot(functions.channels.GetParticipantRequest(chat, user))).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator)
        )
    elif isinstance(chat, types.InputPeerChat):

        ui = await tbot.get_peer_id(user)
        ps = (await tbot(functions.messages.GetFullChatRequest(chat.chat_id))) \
            .full_chat.participants.participants
        return isinstance(
            next((p for p in ps if p.user_id == ui), None),
            (types.ChatParticipantAdmin, types.ChatParticipantCreator)
        )
    else:
        return None

@user_admin
@run_async
def runs(bot: Bot, update: Update):
    chat = update.effective_chat  # type: Optional[Chat]
    update.effective_message.reply_text(random.choice(tld(chat.id, "RUNS-K")))

@user_admin
@run_async
def slap(bot: Bot, update: Update, args: List[str]):
    chat = update.effective_chat  # type: Optional[Chat]
    msg = update.effective_message  # type: Optional[Message]

    # reply to correct message
    reply_text = msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text

    # get user who sent message
    if msg.from_user.username:
        curr_user = "@" + escape_markdown(msg.from_user.username)
    else:
        curr_user = "[{}](tg://user?id={})".format(msg.from_user.first_name, msg.from_user.id)

    user_id = extract_user(update.effective_message, args)
    if user_id:
        slapped_user = bot.get_chat(user_id)
        user1 = curr_user
        if slapped_user.username:
            user2 = "@" + escape_markdown(slapped_user.username)
        else:
            user2 = "[{}](tg://user?id={})".format(slapped_user.first_name,
                                                   slapped_user.id)

    # if no target found, bot targets the sender
    else:
        user1 = "[{}](tg://user?id={})".format(bot.first_name, bot.id)
        user2 = curr_user

    temp = random.choice(tld(chat.id, "SLAP_TEMPLATES-K"))
    item = random.choice(tld(chat.id, "ITEMS-K"))
    hit = random.choice(tld(chat.id, "HIT-K"))
    throw = random.choice(tld(chat.id, "THROW-K"))
    itemp = random.choice(tld(chat.id, "ITEMP-K"))
    itemr = random.choice(tld(chat.id, "ITEMR-K"))

    repl = temp.format(user1=user1, user2=user2, item=item, hits=hit, throws=throw, itemp=itemp, itemr=itemr)
    #user1=user1, user2=user2, item=item_ru, hits=hit_ru, throws=throw_ru, itemp=itemp_ru, itemr=itemr_ru

    reply_text(repl, parse_mode=ParseMode.MARKDOWN)
    
@user_admin
@run_async
def get_id(bot: Bot, update: Update, args: List[str]):
    user_id = extract_user(update.effective_message, args)
    chat = update.effective_chat  # type: Optional[Chat]
    if user_id:
        if update.effective_message.reply_to_message and update.effective_message.reply_to_message.forward_from:
            user1 = update.effective_message.reply_to_message.from_user
            user2 = update.effective_message.reply_to_message.forward_from
            update.effective_message.reply_text(tld(chat.id,
                "The original sender, {}, has an ID of `{}`.\nThe forwarder, {}, has an ID of `{}`.").format(
                    escape_markdown(user2.first_name),
                    user2.id,
                    escape_markdown(user1.first_name),
                    user1.id),
                parse_mode=ParseMode.MARKDOWN)
        else:
            user = bot.get_chat(user_id)
            update.effective_message.reply_text(tld(chat.id, "{}'s id is `{}`.").format(escape_markdown(user.first_name), user.id),
                                                parse_mode=ParseMode.MARKDOWN)
    else:
        chat = update.effective_chat  # type: Optional[Chat]
        if chat.type == "private":
            update.effective_message.reply_text(tld(chat.id, "Your id is `{}`.").format(chat.id),
                                                parse_mode=ParseMode.MARKDOWN)

        else:
            update.effective_message.reply_text(tld(chat.id, "This group's id is `{}`.").format(chat.id),
                                                parse_mode=ParseMode.MARKDOWN)
@run_async
def stats(bot: Bot, update: Update):
    update.effective_message.reply_text("Current stats:\n" + "\n".join([mod.__stats__() for mod in STATS]))

@user_admin
@run_async
def info(bot: Bot, update: Update, args: List[str]):
    msg = update.effective_message  # type: Optional[Message]
    user_id = extract_user(update.effective_message, args)
    chat = update.effective_chat  # type: Optional[Chat]

    if user_id:
        user = bot.get_chat(user_id)

    elif not msg.reply_to_message and not args:
        user = msg.from_user

    elif not msg.reply_to_message and (not args or (
            len(args) >= 1 and not args[0].startswith("@") and not args[0].isdigit() and not msg.parse_entities(
        [MessageEntity.TEXT_MENTION]))):
        msg.reply_text(tld(chat.id, "I can't extract a user from this."))
        return

    else:
        return

    text =  tld(chat.id, "<b>User info</b>:")
    text += "\nID: <code>{}</code>".format(user.id)
    text += tld(chat.id, "\nFirst Name: {}").format(html.escape(user.first_name))

    if user.last_name:
        text += tld(chat.id, "\nLast Name: {}").format(html.escape(user.last_name))

    if user.username:
        text += tld(chat.id, "\nUsername: @{}").format(html.escape(user.username))

    text += tld(chat.id, "\nUser link: {}\n").format(mention_html(user.id, "link"))

    if user.id == OWNER_ID:
        text += tld(chat.id, "\n\nAy, This guy is my owner. I would never do anything against him!")
    else:
        if user.id in SUDO_USERS:
            text += tld(chat.id, "\nThis person is one of my sudo users! " \
            "Nearly as powerful as my owner - so watch it.")
        else:
            if user.id in SUPPORT_USERS:
                text += tld(chat.id, "\nThis person is one of my support users! " \
                        "Not quite a sudo user, but can still gban you off the map.")

            if user.id in WHITELIST_USERS:
                text += tld(chat.id, "\nThis person has been whitelisted! " \
                        "That means I'm not allowed to ban/kick them.")

    for mod in USER_INFO:
        mod_info = mod.__user_info__(user.id, chat.id).strip()
        if mod_info:
            text += "\n\n" + mod_info

    update.effective_message.reply_text(text, parse_mode=ParseMode.HTML)

@user_admin
@run_async
def echo(bot: Bot, update: Update):
    args = update.effective_message.text.split(None, 1)
    message = update.effective_message
    if message.reply_to_message:
        message.reply_to_message.reply_text(args[1])
    else:
        message.reply_text(args[1], quote=False)
    message.delete()

@user_admin
@run_async
def reply_keyboard_remove(bot: Bot, update: Update):
    reply_keyboard = []
    reply_keyboard.append([
        ReplyKeyboardRemove(
            remove_keyboard=True
        )
    ])
    reply_markup = ReplyKeyboardRemove(
        remove_keyboard=True
    )
    old_message = bot.send_message(
        chat_id=update.message.chat_id,
        text='Bot Keyboard removed successfully !',
        reply_markup=reply_markup,
        reply_to_message_id=update.message.message_id
    )
    bot.delete_message(
        chat_id=update.message.chat_id,
        message_id=old_message.message_id
    )

@user_admin
@run_async
def gdpr(bot: Bot, update: Update):
    update.effective_message.reply_text(tld(update.effective_chat.id, "Deleting identifiable data..."))
    for mod in GDPR:
        mod.__gdpr__(update.effective_user.id)

    update.effective_message.reply_text(tld(update.effective_chat.id, "send_gdpr"), parse_mode=ParseMode.MARKDOWN)

@user_admin
@run_async
def markdown_help(bot: Bot, update: Update):
    chat = update.effective_chat  # type: Optional[Chat]
    update.effective_message.reply_text(tld(chat.id, "MARKDOWN_HELP-K"), parse_mode=ParseMode.HTML)
    update.effective_message.reply_text(tld(chat.id, "Try forwarding the following message to me, and you'll see!"))
    update.effective_message.reply_text(tld(chat.id, "/save test This is a markdown test. _italics_, *bold*, `code`, "
                                        "[URL](example.com) [button](buttonurl:github.com) "
                                        "[button2](buttonurl://google.com:same)"))

@run_async
@user_admin
def github(bot: Bot, update: Update):
    message = update.effective_message
    text = message.text[len('/git '):]
    usr = get(f'https://api.github.com/users/{text}').json()
    if usr.get('login'):
        reply_text = f"""*Name:* `{usr['name']}`
*Username:* `{usr['login']}`
*Account ID:* `{usr['id']}`
*Account type:* `{usr['type']}`
*Location:* `{usr['location']}`
*Bio:* `{usr['bio']}`
*Followers:* `{usr['followers']}`
*Following:* `{usr['following']}`
*Hireable:* `{usr['hireable']}`
*Public Repos:* `{usr['public_repos']}`
*Public Gists:* `{usr['public_gists']}`
*Email:* `{usr['email']}`
*Company:* `{usr['company']}`
*Website:* `{usr['blog']}`
*Last updated:* `{usr['updated_at']}`
*Account created at:* `{usr['created_at']}`
"""
    else:
        reply_text = "User not found. Make sure you entered valid username!"
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)


@user_admin
@run_async
def repo(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    text = message.text[len('/repo '):]
    usr = get(f'https://api.github.com/users/{text}/repos?per_page=300').json()
    reply_text = "*Repo*\n"
    for i in range(len(usr)):
        reply_text += f"[{usr[i]['name']}]({usr[i]['html_url']})\n"
    message.reply_text(reply_text,
                       parse_mode=ParseMode.MARKDOWN,
                       disable_web_page_preview=True)


BASE_URL = 'https://del.dog'

@user_admin
@run_async
def paste(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message

    if message.reply_to_message:
        data = message.reply_to_message.text
    elif len(args) >= 1:
        data = message.text.split(None, 1)[1]
    else:
        message.reply_text("What am I supposed to do with this?!")
        return

    r = requests.post(f'{BASE_URL}/documents', data=data.encode('utf-8'))

    if r.status_code == 404:
        update.effective_message.reply_text('Failed to reach dogbin')
        r.raise_for_status()

    res = r.json()

    if r.status_code != 200:
        update.effective_message.reply_text(res['message'])
        r.raise_for_status()

    key = res['key']
    if res['isUrl']:
        reply = f'Shortened URL: {BASE_URL}/{key}\nYou can view stats, etc. [here]({BASE_URL}/v/{key})'
    else:
        reply = f'{BASE_URL}/{key}'
    update.effective_message.reply_text(reply, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

@user_admin
@run_async
def get_paste_content(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message

    if len(args) >= 1:
        key = args[0]
    else:
        message.reply_text("Please supply a paste key!")
        return

    format_normal = f'{BASE_URL}/'
    format_view = f'{BASE_URL}/v/'

    if key.startswith(format_view):
        key = key[len(format_view):]
    elif key.startswith(format_normal):
        key = key[len(format_normal):]

    r = requests.get(f'{BASE_URL}/raw/{key}')

    if r.status_code != 200:
        try:
            res = r.json()
            update.effective_message.reply_text(res['message'])
        except Exception:
            if r.status_code == 404:
                update.effective_message.reply_text('Failed to reach dogbin')
            else:
                update.effective_message.reply_text('Unknown error occured')
        r.raise_for_status()

    update.effective_message.reply_text('```' + escape_markdown(r.text) + '```', parse_mode=ParseMode.MARKDOWN)

@user_admin
@run_async
def get_paste_stats(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message

    if len(args) >= 1:
        key = args[0]
    else:
        message.reply_text("Please supply a paste key!")
        return

    format_normal = f'{BASE_URL}/'
    format_view = f'{BASE_URL}/v/'

    if key.startswith(format_view):
        key = key[len(format_view):]
    elif key.startswith(format_normal):
        key = key[len(format_normal):]

    r = requests.get(f'{BASE_URL}/documents/{key}')

    if r.status_code != 200:
        try:
            res = r.json()
            update.effective_message.reply_text(res['message'])
        except Exception:
            if r.status_code == 404:
                update.effective_message.reply_text('Failed to reach dogbin')
            else:
                update.effective_message.reply_text('Unknown error occured')
        r.raise_for_status()

    document = r.json()['document']
    key = document['_id']
    views = document['viewCount']
    reply = f'Stats for **[/{key}]({BASE_URL}/{key})**:\nViews: `{views}`'
    update.effective_message.reply_text(reply, parse_mode=ParseMode.MARKDOWN)


@register(pattern="^/tts (.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
       await event.reply("")
       return
    input_str = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await event.reply("Invalid Syntax\nFormat `/tts lang | text`\nFor eg: `/tts en | hello`")
        return
    text = text.strip()
    lan = lan.strip()
    try:
        tts = gTTS(text, tld='com', lang=lan)
        tts.save("k.mp3")
    except AssertionError:
        await event.reply('The text is empty.\n'
                         'Nothing left to speak after pre-precessing, '
                         'tokenizing and cleaning.')
        return
    except ValueError:
        await event.reply('Language is not supported.')
        return
    except RuntimeError:
        await event.reply('Error loading the languages dictionary.')
        return
    except gTTSError:
        await event.reply('Error in Google Text-to-Speech API request !')
        return
    with open("k.mp3", "r"):
        await event.client.send_file(event.chat_id, "k.mp3", voice_note=True, reply_to=reply_to_id)
        os.remove("k.mp3")

@register(pattern=r"^/wiki (.*)")
async def wiki(wiki_q):
    """ For .google command, fetch content from Wikipedia. """
    if wiki_q.is_group:
     if not (await is_register_admin(wiki_q.input_chat, wiki_q.message.sender_id)):
       await wiki_q.reply("")
       return
    match = wiki_q.pattern_match.group(1)
    try:
        summary(match)
    except DisambiguationError as error:
        await wiki_q.reply(f"Disambiguated page found.\n\n{error}")
        return
    except PageError as pageerror:
        await wiki_q.reply(f"Page not found.\n\n{pageerror}")
        return
    result = summary(match)
    if len(result) >= 4096:
        file = open("output.txt", "w+")
        file.write(result)
        file.close()
        await wiki_q.client.send_file(
            wiki_q.chat_id,
            "output.txt",
            reply_to=wiki_q.id,
            caption="`Output too large, sending as file`",
        )
        if os.path.exists("output.txt"):
            os.remove("output.txt")
        return
    await wiki_q.reply("**Search:**\n`" + match + "`\n\n**Result:**\n" + result)

import asyncio
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
#from google_images_download import google_images_download
import sys
import shutil
from re import findall
import html2text

@register(pattern="^/google (.*)") # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
       await event.reply("")
       return
    # SHOW_DESCRIPTION = False
    input_str = event.pattern_match.group(1) # + " -inurl:(htm|html|php|pls|txt) intitle:index.of \"last modified\" (mkv|mp4|avi|epub|pdf|mp3)"
    input_url = "https://bots.shrimadhavuk.me/search/?q={}".format(input_str)
    headers = {"USER-AGENT": "UniBorg"}
    response = requests.get(input_url, headers=headers).json()
    output_str = " "
    for result in response["results"]:
        text = result.get("title")
        url = result.get("url")
        description = result.get("description")
        last = html2text.html2text(description)
        output_str += "[{}]({})\n{}\n".format(text, url, last)       
    await event.reply("{}".format(output_str), link_preview=False, parse_mode='Markdown')

import aiohttp
import io
import time
from datetime import tzinfo, datetime


@register(pattern="^/weather (.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
       await event.reply("")
       return
    sample_url = "https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric"
    input_str = event.pattern_match.group(1)
    async with aiohttp.ClientSession() as session:
        response_api_zero = await session.get(sample_url.format(input_str, OPENWEATHERMAP_ID))
    response_api = await response_api_zero.json()
    if response_api["cod"] == 200:
        country_code = response_api["sys"]["country"]
        country_time_zone = int(response_api["timezone"])
        sun_rise_time = int(response_api["sys"]["sunrise"]) + country_time_zone
        sun_set_time = int(response_api["sys"]["sunset"]) + country_time_zone
        await event.reply(
            """**Location**: {}
**Temperature**: {}°С
    __minimium__: {}°С
    __maximum__ : {}°С
**Humidity**: {}%
**Wind**: {}m/s
**Clouds**: {}hpa
**Sunrise**: {} {}
**Sunset**: {} {}""".format(
                input_str,
                response_api["main"]["temp"],
                response_api["main"]["temp_min"],
                response_api["main"]["temp_max"],
                response_api["main"]["humidity"],
                response_api["wind"]["speed"],
                response_api["clouds"]["all"],
                # response_api["main"]["pressure"],
                time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(sun_rise_time)),
                country_code,
                time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(sun_set_time)),
                country_code
            )
        )
    else:
        await event.reply(response_api["message"])


@register(pattern="^/wttr (.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
       await event.reply("")
       return
    sample_url = "https://wttr.in/{}.png"
    # logger.info(sample_url)
    input_str = event.pattern_match.group(1)
    async with aiohttp.ClientSession() as session:
        response_api_zero = await session.get(sample_url.format(input_str))
        # logger.info(response_api_zero)
        response_api = await response_api_zero.read()
        with io.BytesIO(response_api) as out_file:
            await event.reply(
                file=out_file)
            

 
@register(pattern="^/figlet (.*)")
async def figlet(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
       await event.reply("")
       return
    input_str = event.pattern_match.group(1)
    result = pyfiglet.figlet_format(input_str)
    await event.respond("`{}`".format(result))

"""Download & Upload Images on Telegram\n
Syntax: `.img <Name>` or `.img (replied message)`
\n Upgraded and Google Image Error Fixed
"""

from haruka.google_imgs import googleimagesdownload
import os
import shutil
from re import findall

@register(pattern="^/img ?(.*)")
async def img_sampler(event):
    if event.fwd_from:
        return
    if event.is_group:
       if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply:
        query = reply.message
    else:
    	return
        
    lim = findall(r"lim=\d+", query)
    # lim = event.pattern_match.group(1)
    try:
        lim = lim[0]
        lim = lim.replace("lim=", "")
        query = query.replace("lim=" + lim[0], "")
    except IndexError:
        lim = 5
    response = googleimagesdownload()

    # creating list of arguments
    arguments = {
        "keywords": query,
        "limit": lim,
        "format": "jpg",
        "no_directory": "no_directory"
    }

    # passing the arguments to the function
    paths = response.download(arguments)
    lst = paths[0][query]
    await event.client.send_file(await event.client.get_input_entity(event.chat_id), lst)
    shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))

@run_async
@user_admin
def shrug(bot: Bot, update: Update):
    default_msg = "¯\_(ツ)_/¯"
    message = update.effective_message
    if message.reply_to_message:
        message.reply_to_message.reply_text(default_msg)
    else:
        message.reply_text(default_msg)
        
from PyDictionary import PyDictionary
dictionary=PyDictionary()

@run_async
@user_admin
def define(bot: Bot, update: Update):
  message = update.effective_message
  text = message.text[len('/define '):]
  word = f'"{text}"'
  let = dictionary.meaning(word)
  set = str(let)
  jet = set.replace("{","")
  net = jet.replace("}","")
  got = net.replace("'", "")
  message.reply_text(got)


@register(pattern="^/yt (.*)")
async def yts_search(video_q):
    # For .yts command, do a YouTube search from Telegram.
    if video_q.is_group:
     if not (await is_register_admin(video_q.input_chat, video_q.message.sender_id)):
       await video_q.reply("")
       return
    query = video_q.pattern_match.group(1)
    result = ''

    if not YOUTUBE_API_KEY:
        await video_q.reply(
            "`Error: YouTube API key missing! Add it to environment vars or config.env.`"
        )
        return

   
    full_response = await youtube_search(query)
    videos_json = full_response[1]

    for video in videos_json:
        title = f"{unescape(video['snippet']['title'])}"
        link = f"https://youtu.be/{video['id']['videoId']}"
        result += f"{title}\n{link}\n\n"

    reply_text = f"**Search Query:**\n`{query}`\n\n**Results:**\n\n{result}"

    await video_q.reply(reply_text, link_preview=False)


async def youtube_search(query,
                         order="relevance",
                         token=None,
                         location=None,
                         location_radius=None):
    """ Do a YouTube search. """
    youtube = build('youtube',
                    'v3',
                    developerKey=YOUTUBE_API_KEY,
                    cache_discovery=False)
    search_response = youtube.search().list(
        q=query,
        type="video",
        pageToken=token,
        order=order,
        part="id,snippet",
        maxResults=10,
        location=location,
        locationRadius=location_radius).execute()

    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append(search_result)
    try:
        nexttok = search_response["nextPageToken"]
        return (nexttok, videos)
    except HttpError:
        nexttok = "last_page"
        return (nexttok, videos)
    except KeyError:
        nexttok = "KeyError, try again."
        return (nexttok, videos)

"""Get Administrators of any Chat*
Syntax: .userlist"""
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
from telethon.errors.rpcerrorlist import (UserIdInvalidError, MessageTooLongError, ChatAdminRequiredError)
                                                                                    
@register(pattern="^/users$")
async def get_users(show):
        if not show.is_group:
            await show.reply("Are you sure this is a group?")
            return
        if show.is_group:
         if not (await is_register_admin(show.input_chat, show.message.sender_id)):
          await show.reply("")
          return
        info = await show.client.get_entity(show.chat_id)
        title = info.title if info.title else "this chat"
        mentions = "Users in {}: \n".format(title)
        async for user in show.client.iter_participants(show.chat_id):
                  if not user.deleted:
                     mentions += f"\n[{user.first_name}](tg://user?id={user.id}) {user.id}"
                  else:
                      mentions += f"\nDeleted Account {user.id}"
        file = open("userslist.txt", "w+")
        file.write(mentions)
        file.close()
        await show.client.send_file(
                show.chat_id,
                "userslist.txt",
                caption='Users in {}'.format(title),
                reply_to=show.id,
                )
        os.remove("userslist.txt")


import requests
import bs4 
import re
from telethon import *

@register(pattern="^/app (.*)")
async def apk(e):
    if e.is_group:
     if not (await is_register_admin(e.input_chat, e.message.sender_id)):
          await e.reply("")
          return
    try:
        app_name = e.pattern_match.group(1)
        remove_space = app_name.split(' ')
        final_name = '+'.join(remove_space)
        page = requests.get("https://play.google.com/store/search?q="+final_name+"&c=apps")
        lnk = str(page.status_code)
        soup = bs4.BeautifulSoup(page.content,'lxml', from_encoding='utf-8')
        results = soup.findAll("div","ZmHEEd")
        app_name = results[0].findNext('div', 'Vpfmgd').findNext('div', 'WsMG1c nnK0zc').text
        app_dev = results[0].findNext('div', 'Vpfmgd').findNext('div', 'KoLSrc').text
        app_dev_link = "https://play.google.com"+results[0].findNext('div', 'Vpfmgd').findNext('a', 'mnKHRc')['href']
        app_rating = results[0].findNext('div', 'Vpfmgd').findNext('div', 'pf5lIe').find('div')['aria-label']
        app_link = "https://play.google.com"+results[0].findNext('div', 'Vpfmgd').findNext('div', 'vU6FJ p63iDd').a['href']
        app_icon = results[0].findNext('div', 'Vpfmgd').findNext('div', 'uzcko').img['data-src']
        app_details = "<a href='"+app_icon+"'>📲&#8203;</a>"
        app_details += " <b>"+app_name+"</b>"
        app_details += "\n\n<code>Developer :</code> <a href='"+app_dev_link+"'>"+app_dev+"</a>"
        app_details += "\n<code>Rating :</code> "+app_rating.replace("Rated ", "⭐ ").replace(" out of ", "/").replace(" stars", "", 1).replace(" stars", "⭐ ").replace("five", "5")
        app_details += "\n<code>Features :</code> <a href='"+app_link+"'>View in Play Store</a>"
        app_details += "\n\n===> @AlexaFamilyBot <==="
        await e.reply(app_details, link_preview = True, parse_mode = 'HTML')
    except IndexError:
        await e.reply("No result found in search. Please enter **Valid app name**")
    except Exception as err:
        await e.reply("Exception Occured:- "+str(err))

import asyncio
from telethon import events
from cowpy import cow

@register(pattern=r"^/(\w+)say (.*)")
async def univsaye(cowmsg):
    if cowmsg.is_group:
     if not (await is_register_admin(cowmsg.input_chat, cowmsg.message.sender_id)):
          await cowmsg.reply("")
          return
    """ For .cowsay module, uniborg wrapper for cow which says things. """
    if not cowmsg.text[0].isalpha() and cowmsg.text[0] not in ("#", "@"):
        arg = cowmsg.pattern_match.group(1).lower()
        text = cowmsg.pattern_match.group(2)

        if arg == "cow":
            arg = "default"
        if arg not in cow.COWACTERS:
            return
        cheese = cow.get_cow(arg)
        cheese = cheese()

        await cowmsg.reply(f"`{cheese.milk(text).replace('`', '´')}`")
 

@register(pattern="^/zombies(?: |$)(.*)")
async def rm_deletedacc(show):
    """ For .delusers command, list all the ghost/deleted accounts in a chat. """
    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = "`No deleted accounts found, Group is cleaned as Hell`"
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    
    if show.is_private:
        await show.reply("You can use this command in groups but not in PM's")
        return

    if show.is_group:
     if not (await is_register_admin(show.input_chat, show.message.sender_id)):
          await show.reply("")
          return

    if con != "clean":
        await show.reply("`Searching for zombie accounts...`")
        async for user in show.client.iter_participants(show.chat_id):
            if user.deleted:
                del_u += 1
         
        if del_u > 0:
            del_status = f"Found **{del_u}** deleted account(s) in this group,\
            \nclean them by using `/zombies clean`"

        await show.reply(del_status)
        return

    # Here laying the sanity check

    # Well
    if not admin and not creator:
        await show.reply("`I am not an admin here!`")
        return

    await show.reply("`Deleting deleted accounts...`")
    del_u = 0
    del_a = 0

    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client(
                    EditBannedRequest(show.chat_id, user.id, BANNED_RIGHTS))
            except ChatAdminRequiredError:
                await show.reply("`I don't have ban rights in this group`")
                return
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await show.client(
                EditBannedRequest(show.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1

    if del_u > 0:
        del_status = f"Cleaned **{del_u}** deleted account(s)"

    if del_a > 0:
        del_status = f"Cleaned **{del_u}** deleted account(s) \
        \n**{del_a}** deleted admin accounts are not removed"

    await show.reply(del_status)


import json
import os
from PIL import Image
import requests


def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_API_KEY, language='eng'):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.json()


def ocr_space_url(url, overlay=False, api_key=OCR_SPACE_API_KEY, language='eng'):
    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.json()


def progress(current, total):
    logger.info("Downloaded {} of {}\nCompleted {}".format(
        current, total, (current / total) * 100))


@register(pattern="^/img2textlang")
async def get_ocr_languages(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
    languages = {}
    languages["English"] = "eng"
    languages["Arabic"] = "ara"
    languages["Bulgarian"] = "bul"
    languages["Chinese (Simplified)"] = "chs"
    languages["Chinese (Traditional)"] = "cht"
    languages["Croatian"] = "hrv"
    languages["Czech"] = "cze"
    languages["Danish"] = "dan"
    languages["Dutch"] = "dut"
    languages["Finnish"] = "fin"
    languages["French"] = "fre"
    languages["German"] = "ger"
    languages["Greek"] = "gre"
    languages["Hungarian"] = "hun"
    languages["Korean"] = "kor"
    languages["Italian"] = "ita"
    languages["Japanese"] = "jpn"
    languages["Polish"] = "pol"
    languages["Portuguese"] = "por"
    languages["Russian"] = "rus"
    languages["Slovenian"] = "slv"
    languages["Spanish"] = "spa"
    languages["Swedish"] = "swe"
    languages["Turkish"] = "tur"
    a = json.dumps(languages, sort_keys=True, indent=4)
    await event.reply(str(a))


@register(pattern="^/img2text (.*)")
async def parse_ocr_space_api(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
    await event.reply("Processing ...")
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    lang_code = event.pattern_match.group(1)
    downloaded_file_name = await event.client.download_media(
        await event.get_reply_message(),
        TEMP_DOWNLOAD_DIRECTORY)
    if downloaded_file_name.endswith((".webp")):
        downloaded_file_name = conv_image(downloaded_file_name)
    test_file = ocr_space_file(filename=downloaded_file_name, language=lang_code)
    ParsedText = "hmm"
    try:
        ParsedText = test_file["ParsedResults"][0]["ParsedText"]
        ProcessingTimeInMilliseconds = str(int(test_file["ProcessingTimeInMilliseconds"]) // 1000)
    except Exception as e:
        await event.reply("Error :\n `{}`\nReport This to @AlexaSupport\n\n`{}`".format(str(e), json.dumps(test_file, sort_keys=True, indent=4)))
    else:
        await event.reply("Read Document in {} seconds. \n{}".format(ProcessingTimeInMilliseconds, ParsedText))
    os.remove(downloaded_file_name)
   



def conv_image(image):
    im = Image.open(image)
    im.save(image, "PNG")
    new_file_name = image + ".png"
    os.rename(image, new_file_name)
    return new_file_name



import asyncio
from getpass import getuser
from os import remove
from sys import executable
from haruka.events import register


"""Speech to Text
Syntax: .stt <Language Code> as reply to a speech message"""
from telethon import events
import requests
import os
import datetime

@register(pattern="^/stt")
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
    start = datetime.datetime.now()
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    await event.reply("Downloading to Alexa's server for Analysis ...")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        required_file_name = await event.client.download_media(previous_message, TEMP_DOWNLOAD_DIRECTORY)
        if IBM_WATSON_CRED_URL is None or IBM_WATSON_CRED_PASSWORD is None:
            await event.reply("You need to set the required ENV variables for this module. \nModule stopping")
        else:
            await event.reply("Starting analysis")
            headers = {
                "Content-Type": previous_message.media.document.mime_type,
            }
            data = open(required_file_name, "rb").read()
            response = requests.post(
                IBM_WATSON_CRED_URL + "/v1/recognize",
                headers=headers,
                data=data,
                auth=("apikey", IBM_WATSON_CRED_PASSWORD)
            )
            r = response.json()
            if "results" in r:
                # process the json to appropriate string format
                results = r["results"]
                transcript_response = ""
                transcript_confidence = ""
                for alternative in results:
                    alternatives = alternative["alternatives"][0]
                    transcript_response += " " + str(alternatives["transcript"]) 
                    transcript_confidence += " " + str(alternatives["confidence"]) + " + "
                end = datetime.datetime.now()
                ms = (end - start).seconds
                if transcript_response != "":
                    string_to_show = "Language: `English`\nTRANSCRIPT: `{}`\nTime Taken: {} seconds\nConfidence: `{}`".format(transcript_response, ms, transcript_confidence)
                else:
                    string_to_show = "Language: `English`\nTime Taken: {} seconds\n**No Results Found**".format(ms)
                await event.reply(string_to_show)
            else:
                await event.reply(r["error"])
            # now, remove the temporary file
            os.remove(required_file_name)
    else:
        await event.reply("Reply to a voice message, to get the text out of it.")

from telethon import events
import os
import requests
import json
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


@register(pattern="^/news")
async def _(event):
  if event.is_group:
     return
  if event.fwd_from:
     return
 
  news_url="https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
  Client=urlopen(news_url)
  xml_page=Client.read()
  Client.close()
  soup_page=soup(xml_page,"xml")
  news_list=soup_page.findAll("item")
  for news in news_list:
       title = news.title.text
       text = news.link.text
       date = news.pubDate.text
       seperator = "-"*50
       l = "\n"
       lastisthis = title+l+text+l+date+l+seperator
       await event.reply(lastisthis)


from telethon.tl.types import InputMediaDice

@register(pattern="^/dice")
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
    input_str = print(randrange(7))
    r = await event.reply(file=InputMediaDice(''))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice(''))
        except:
            pass

@register(pattern="^/basketball")
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
    input_str = print(randrange(6))
    r = await event.reply(file=InputMediaDice('🏀'))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice('🏀'))
        except:
            pass


@register(pattern="^/dart")
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
    input_str = print(randrange(7))
    r = await event.reply(file=InputMediaDice('🎯'))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice('🎯'))
        except:
            pass

import datetime
from typing import List

import requests
from telegram import Bot, Update, ParseMode
from telegram.ext import run_async

from haruka import dispatcher, TIME_API_KEY
from haruka.modules.disable import DisableAbleCommandHandler

def generate_time(to_find: str, findtype: List[str]) -> str:
    data = requests.get(f"http://api.timezonedb.com/v2.1/list-time-zone"
                        f"?key={TIME_API_KEY}"
                        f"&format=json"
                        f"&fields=countryCode,countryName,zoneName,gmtOffset,timestamp,dst").json()

    for zone in data["zones"]:
        for eachtype in findtype:
            if to_find in zone[eachtype].lower():
                country_name = zone['countryName']
                country_zone = zone['zoneName']
                country_code = zone['countryCode']

                if zone['dst'] == 1:
                    daylight_saving = "Yes"
                else:
                    daylight_saving = "No"

                date_fmt = r"%d-%m-%Y"
                time_fmt = r"%H:%M:%S"
                day_fmt = r"%A"
                gmt_offset = zone['gmtOffset']
                timestamp = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=gmt_offset)
                current_date = timestamp.strftime(date_fmt)
                current_time = timestamp.strftime(time_fmt)
                current_day = timestamp.strftime(day_fmt)

                break

    try:
        result = (f"<b>🌍Country :</b> <code>{country_name}</code>\n"
                  f"<b>⏳Zone Name :</b> <code>{country_zone}</code>\n"
                  f"<b>🗺Country Code :</b> <code>{country_code}</code>\n"
                  f"<b>🌞Daylight saving :</b> <code>{daylight_saving}</code>\n"
                  f"<b>🌅Day :</b> <code>{current_day}</code>\n"
                  f"<b>⌚Current Time :</b> <code>{current_time}</code>\n"
                  f"<b>📆Current Date :</b> <code>{current_date}</code>")
    except:
        result = None

    return result


@run_async
@user_admin
def gettime(bot: Bot, update: Update):
    message = update.effective_message

    try:
        query = message.text.strip().split(" ", 1)[1]
    except:
        message.reply_text("Provide a country name/abbreviation/timezone to find.")
        return
    send_message = message.reply_text(f"Finding timezone info for <b>{query}</b>", parse_mode=ParseMode.HTML)

    query_timezone = query.lower()
    if len(query_timezone) == 2:
        result = generate_time(query_timezone, ["countryCode"])
    else:
        result = generate_time(query_timezone, ["zoneName", "countryName"])

    if not result:
        send_message.edit_text(f"Timezone info not available for <b>{query}</b>", parse_mode=ParseMode.HTML)
        return

    send_message.edit_text(result, parse_mode=ParseMode.HTML)



# Simple lyrics module using tswift by @TheRealPhoenix

from tswift import Song
from telegram import Bot, Update, Message, Chat
from telegram.ext import run_async
from haruka import dispatcher
from haruka.modules.disable import DisableAbleCommandHandler


@run_async
@user_admin
def lyrics(bot: Bot, update: Update, args):
    msg = update.effective_message
    query = " ".join(args)
    song = ""
    if not query:
        msg.reply_text("You haven't specified which song to look for!")
        return
    else:
        song = Song.find_song(query)
        if song:
            if song.lyrics:
                reply = song.format()
            else:
                reply = "Couldn't find any lyrics for that song!"
        else:
            reply = "Song not found!"
        if len(reply) > 4090:
            with open("lyrics.txt", 'w') as f:
                f.write(f"{reply}\n\n\nOwO UwU OwO")
            with open("lyrics.txt", 'rb') as f:
                msg.reply_document(document=f,
                caption="Message length exceeded max limit! Sending as a text file.")
        else:
            msg.reply_text(reply)

# Made by @Ayushchatterjee

import wolframalpha 
from haruka import WOLFRAM_ID

@register(pattern=r"^/alexa(?: |$)([\s\S]*)")
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
    if not event.reply_to_msg_id:
       app_id =  WOLFRAM_ID
       client = wolframalpha.Client(app_id) 
       question = event.pattern_match.group(1)
       res = client.query(question) 
       answer = next(res.results).text 
       await event.reply(f'**{question}**\n\n' + answer, parse_mode='Markdown')
        
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        required_file_name = await event.client.download_media(previous_message, TEMP_DOWNLOAD_DIRECTORY)
        if IBM_WATSON_CRED_URL is None or IBM_WATSON_CRED_PASSWORD is None:
            await event.reply("You need to set the required ENV variables for this module. \nModule stopping")
        else:
            headers = {
                "Content-Type": previous_message.media.document.mime_type,
            }
            data = open(required_file_name, "rb").read()
            response = requests.post(
                IBM_WATSON_CRED_URL + "/v1/recognize",
                headers=headers,
                data=data,
                auth=("apikey", IBM_WATSON_CRED_PASSWORD)
            )
            r = response.json()
            if "results" in r:
                # process the json to appropriate string format
                results = r["results"]
                transcript_response = ""
                transcript_confidence = ""
                for alternative in results:
                    alternatives = alternative["alternatives"][0]
                    transcript_response += " " + str(alternatives["transcript"]) 
                if transcript_response != "":
                    string_to_show = "{}".format(transcript_response)           
                    app_id =  WOLFRAM_ID
                    client = wolframalpha.Client(app_id)
                    res = client.query(string_to_show)
                    answer = next(res.results).text
                    try:
                       tts = gTTS(answer, tld='com', lang='en')
                       tts.save("results.mp3")
                    except AssertionError: 
                      return
                    except ValueError:    
                      return
                    except RuntimeError:        
                      return
                    except gTTSError:
                      return
                    with open("results.mp3", "r"):
                        await event.client.send_file(event.chat_id, "results.mp3", voice_note=True, reply_to=event.id)
                    os.remove("results.mp3")
                else:                   
                    try:
                       answer = "Sorry I can't recognise your query"
                       tts = gTTS(answer, tld='com', lang='en')
                       tts.save("results.mp3")
                    except AssertionError: 
                      return
                    except ValueError:    
                      return
                    except RuntimeError:        
                      return
                    except gTTSError:
                      return
                    with open("results.mp3", "r"):
                        await event.client.send_file(event.chat_id, "results.mp3", voice_note=True, reply_to=event.id)
                    os.remove("results.mp3")
            else:
                await event.reply("API Failure !")
                os.remove(required_file_name)


from bs4 import BeautifulSoup as bs 
import requests
from telethon import events
from haruka.events import register
import asyncio
import subprocess
import telegraph
telegraph = Telegraph()
telegraph.create_account(short_name='Alexa')

@register(pattern="^/torrent (.*)")
async def tor_search(event):
   if event.fwd_from:
      return 
   if event.is_group:
    if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
   str = event.pattern_match.group(1)
   let = f'"{str}"'
   jit = subprocess.check_output(["we-get", "-s", let, "-J"])   
   proc = jit.decode()
   sit = proc.replace("{", "")
   pit = sit.replace("}", "")
   op = pit.replace(",", "")
   seta = f"Magnets for {str} are below:"
   response = telegraph.create_page(seta, html_content=op)
   await event.reply('Magnet Links for {}:\n\nhttps://telegra.ph/{}'.format(str,response['path']), link_preview=False) 

@register(pattern="^/fortune")
async def fortune(event):
   if event.fwd_from:
      return 
   if event.is_group:
    if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
   jit = subprocess.check_output("fortune")
   await event.reply(jit)


from haruka import *

@register(pattern="^/helptorrent")
async def helptorrent(event):
 if event.fwd_from or event.is_group:
    return 
 else:
   topa = "./haruka/Tutorial_For_Torrent.mp4"
   file = await event.client.upload_file(topa) 
   await event.client.send_file(event.chat_id, file, caption="Tutorial For Torrent Module", reply_to=event.id)
   
@register(pattern="^/helpcamscanner")
async def helpcam(event):
 if event.fwd_from or event.is_group:
    return 
 else:
   topa = "./haruka/Tutorial for Camscanner.mp4"
   file = await event.client.upload_file(topa) 
   await event.client.send_file(event.chat_id, file, caption="Tutorial For Camscanner Module", reply_to=event.id)
   


import sys
import requests
import json
import time
import urllib
import os

@register(pattern=r'^/phone (.*)')
async def phone(event): 
    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
    information = event.pattern_match.group(1)
    number = information
    key = "fe65b94e78fc2e3234c1c6ed1b771abd" 
    api = "http://apilayer.net/api/validate?access_key=" + key + "&number=" + number + "&country_code=&format=1"
    output = requests.get(api)
    content = output.text
    obj = json.loads(content)
    country_code = obj['country_code']
    country_name = obj['country_name']
    location = obj['location']
    carrier = obj['carrier']
    line_type = obj['line_type']	
    validornot = obj['valid']	
    aa = "Valid: "+str(validornot)
    a = "Phone number: "+str(number)
    b = "Country: " +str(country_code)
    c = "Country Name: " +str(country_name)
    d = "Location: " +str(location)
    e = "Carrier: " +str(carrier)
    f = "Device: " +str(line_type)
    g = f"{aa}\n{a}\n{b}\n{c}\n{d}\n{e}\n{f}"
    await event.reply(g)


@register(pattern="^/ping")
async def pingme(pong):
    if pong.is_group:
     if not (await is_register_admin(pong.input_chat, pong.message.sender_id)):
          await pong.reply("")
          return
    """ FOr .pingme command, ping the userbot from any chat.  """
    start = datetime.datetime.now()
    up = await pong.reply("`Pong!`")
    end = datetime.datetime.now()
    duration = (end - start).microseconds / 1000
    await up.edit("`Pong!\n%sms`" % (duration))


from telethon import events
from telethon.tl.types import UserStatusEmpty, UserStatusLastMonth, UserStatusLastWeek, UserStatusOffline, UserStatusOnline, UserStatusRecently, ChannelParticipantsKicked, ChatBannedRights
from telethon.tl import functions, types
from time import sleep
import asyncio
from telethon import *
from telethon.tl.functions.channels import (EditAdminRequest,
                                            EditBannedRequest,
                                            EditPhotoRequest)
                                           
@register(pattern="^/kickthefools")
async def _(event):
    if event.fwd_from:
        return
    
    if event.is_private:
        await event.reply("You can use this command in groups but not in PM's")
        return

    chat = await event.get_chat()
    admin = chat.admin_rights
    sender = await event.get_sender()
    
    if not event.chat.admin_rights.ban_users:
       await event.reply("I don't have sufficient permissions")
       return

    if event.is_group:
     if not (await is_register_admin(event.input_chat, event.message.sender_id)):
       return

    c = 0
    KICK_RIGHTS = ChatBannedRights(until_date=None, view_messages=True)
    await event.reply("Searching Participant Lists...")
    async for i in event.client.iter_participants(event.chat_id):
        print(i) #optional
        if isinstance(i.status, UserStatusLastMonth):
            status = await event.client(EditBannedRequest(event.chat_id, i, KICK_RIGHTS))
            if not status:
               return
            else:
               c = c + 1
                    
        if isinstance(i.status, UserStatusLastWeek):
            status = await event.client(EditBannedRequest(event.chat_id, i, KICK_RIGHTS))
            if not status:
               return
            else:
               c = c + 1                 

    required_string = "Successfully Kicked **{}** users"
    await event.reply(required_string.format(c))


from coffeehouse.lydia import LydiaAI
from coffeehouse.api import API
import asyncio
from telethon import events
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

import coffeehouse as cf

import asyncio
import io
import coffeehouse
from haruka import LYDIA_API_KEY
from telethon import events
from coffeehouse.lydia import LydiaAI
from coffeehouse.api import API


# Non-SQL Mode
ACC_LYDIA = {}

if LYDIA_API_KEY:
    api_key = LYDIA_API_KEY
    api_client = API(api_key)
    lydia = LydiaAI(api_client)


@register(pattern="^/autochat")
async def addcf(event):
    if event.fwd_from:
        return
    if event.is_group:
       if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
    reply_msg = await event.get_reply_message()
    sender = event.sender_id
    if reply_msg:
        session = lydia.create_session()
        session_id = session.id
        if reply_msg.from_id is None:
            return 
        if not reply_msg.from_id == sender:
            return 
        ACC_LYDIA.update({(event.chat_id & reply_msg.from_id): session})
        await event.reply("Coffeehouse AI successfully enabled for user: {} in chat: {}".format(str(reply_msg.from_id), str(event.chat_id)))
    else:
        return

@register(pattern="^/stopchat")
async def remcf(event):
    if event.fwd_from:
        return
    if event.is_group:
       if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
    reply_msg = await event.get_reply_message()
    try:
        del ACC_LYDIA[event.chat_id & reply_msg.from_id]
        await event.reply("Coffeehouse AI successfully disabled for user: {} in chat: {}".format(str(reply_msg.from_id), str(event.chat_id)))
    except Exception:
        return

@register(pattern="")
async def user(event):
    user_text = event.text
    try:
        session = ACC_LYDIA[event.chat_id & event.from_id]
        msg = event.text
        text_rep = session.think_thought(msg)
        await event.reply(text_rep)
    except (KeyError, TypeError):
        return
      
import os
import sys

@register(pattern="^/camscanner")
async def asciiart(event):
  if event.fwd_from:
     return  
  if not event.from_id:
     await event.reply("Reply To A Image Plox..")
     return
  if event.is_group:
   if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
  directory = "./"
  test = os.listdir(directory)
  for item in test:
    if item.endswith(".jpg"):
        os.remove(os.path.join(directory, item))
    elif item.endswith(".png"):
        os.remove(os.path.join(directory, item))
    elif item.endswith(".jpeg"):
        os.remove(os.path.join(directory, item))
  reply_msg = await event.get_reply_message()
  downloaded_file_name = await event.client.download_media(reply_msg, './')
  let = f"{downloaded_file_name}"
  subprocess.run(["python", "scan", "--image", let])
  fuck = await event.client.upload_file("./scanned.jpg")
  await event.client.send_file(event.chat_id, fuck)
  directory = "./"
  test = os.listdir(directory)
  for item in test:
    if item.endswith(".jpg"):
        os.remove(os.path.join(directory, item))
    elif item.endswith(".png"):
        os.remove(os.path.join(directory, item))
    elif item.endswith(".jpeg"):
        os.remove(os.path.join(directory, item))
    

import asyncio
import barcode
import os
import time
from barcode.writer import ImageWriter
import datetime
from haruka.events import register
from telethon import events


@register(pattern="^/barcode ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
       if not (await is_register_admin(event.input_chat, event.message.sender_id)):
          await event.reply("")
          return
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    message = "SYNTAX: `.barcode <long text to include>`"
    reply_msg_id = event.message.id
    if input_str:
        message = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        reply_msg_id = previous_message.id
        if previous_message.media:
            downloaded_file_name = await event.client.download_media(
                previous_message,
                Config.TEMP_DOWNLOAD_DIRECTORY,
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                message += m.decode("UTF-8") + "\r\n"
            os.remove(downloaded_file_name)
        else:
            message = previous_message.message
    else:
        message = "SYNTAX: `.barcode <long text to include>`"
    bar_code_type = "code128"
    try:
        bar_code_mode_f = barcode.get(bar_code_type, message, writer=ImageWriter())
        filename = bar_code_mode_f.save(bar_code_type)
        await event.client.send_file(
            event.chat_id,
            filename,
            caption=message,
            reply_to=reply_msg_id,
        )
        os.remove(filename)
    except Exception as e:
        await event.reply(str(e))
        return
    end = datetime.now()
    ms = (end - start).seconds
    await event.reply("Created BarCode in {} seconds".format(ms))


import logging
import requests
import base64
import json
import os 
import telethon

from PIL import Image
from io import BytesIO

logger = logging.getLogger(__name__)


if 1 == 1:
    strings = {
        "name": "Quotes",
        "api_token_cfg_doc": "API Key/Token for Quotes.",
        "api_url_cfg_doc": "API URL for Quotes.",
        "colors_cfg_doc": "Username colors",
        "default_username_color_cfg_doc": "Default color for the username.",
        "no_reply": "<b>You didn't reply to a message.</b>",
        "no_template": "<b>You didn't specify the template.</b>",
        "delimiter": "</code>, <code>",
        "server_error": "<b>Server error. Please report to developer.</b>",
        "invalid_token": "<b>You've set an invalid token.</b>",
        "unauthorized": "<b>You're unauthorized to do this.</b>",
        "not_enough_permissions": "<b>Wrong template. You can use only the default one.</b>",
        "templates": "<b>Available Templates:</b> <code>{}</code>",
        "cannot_send_stickers": "<b>You cannot send stickers in this chat.</b>",
        "admin": "admin",
        "creator": "creator",
        "hidden": "hidden",
        "channel": "Channel"
    }

    config = dict({"api_token": os.environ.get("API_TOKEN"), 
                                          "api_url": "http://api.antiddos.systems",
                                          "username_colors": ["#fb6169", "#faa357", "#b48bf2", "#85de85",
                                                              "#62d4e3", "#65bdf3", "#ff5694"],
                                          "default_username_color": "#b48bf2"})

    @register(pattern="^/quotly(.*)")
    async def quotecmd(message):  # noqa: C901
        """Quote a message.
        Usage: .quote [template]
        If template is missing, possible templates are fetched."""
        if message.is_group:
         if not (await is_register_admin(message.input_chat, message.message.sender_id)):
          return
        args = message.raw_text.split(" ")[1:]
        if args == []:
            args = ["default"]
        reply = await message.get_reply_message()

        if not reply:
            return await message.respond(strings["no_reply"])

        if not args:
            return await message.respond(strings["no_template"])

        username_color = username = admintitle = user_id = None
        profile_photo_url = reply.from_id

        admintitle = ""
        if isinstance(message.to_id, telethon.tl.types.PeerChannel):
            try:
                user = await event.client(telethon.tl.functions.channels.GetParticipantRequest(message.chat_id,
                                                                                              reply.from_id))
                if isinstance(user.participant, telethon.tl.types.ChannelParticipantCreator):
                    admintitle = user.participant.rank or strings["creator"]
                elif isinstance(user.participant, telethon.tl.types.ChannelParticipantAdmin):
                    admintitle = user.participant.rank or strings["admin"]
                user = user.users[0]
            except telethon.errors.rpcerrorlist.UserNotParticipantError:
                user = await reply.get_sender()
        elif isinstance(message.to_id, telethon.tl.types.PeerChat):
            chat = await event.client(telethon.tl.functions.messages.GetFullChatRequest(reply.to_id))
            participants = chat.full_chat.participants.participants
            participant = next(filter(lambda x: x.user_id == reply.from_id, participants), None)
            if isinstance(participant, telethon.tl.types.ChatParticipantCreator):
                admintitle = strings["creator"]
            elif isinstance(participant, telethon.tl.types.ChatParticipantAdmin):
                admintitle = strings["admin"]
            user = await reply.get_sender()
        else:
            user = await reply.get_sender()

        username = telethon.utils.get_display_name(user)
        user_id = reply.from_id

        if reply.fwd_from:
            if reply.fwd_from.saved_from_peer:
                username = telethon.utils.get_display_name(reply.forward.chat)
                profile_photo_url = reply.forward.chat
                admintitle = strings["channel"]
            elif reply.fwd_from.from_name:
                username = reply.fwd_from.from_name
            elif reply.forward.sender:
                username = telethon.utils.get_display_name(reply.forward.sender)
            elif reply.forward.chat:
                username = telethon.utils.get_display_name(reply.forward.chat)

        pfp = await event.client.download_profile_photo(profile_photo_url, bytes)
        if pfp is not None:
            profile_photo_url = "data:image/png;base64, " + base64.b64encode(pfp).decode()

        if user_id is not None:
            username_color = config["username_colors"][user_id % 7]
        else:
            username_color = config["default_username_color"]

        request = json.dumps({
            "ProfilePhotoURL": profile_photo_url,
            "usernameColor": username_color,
            "username": username,
            "adminTitle": admintitle,
            "Text": reply.message,
            "Markdown": get_markdown(reply),
            "Template": args[0],
            "APIKey": config["api_token"]
        })

        resp = requests.post(config["api_url"] + "/api/v2/quote", data=request)
        resp.raise_for_status()
        resp = resp.json()

        if resp["status"] == 500:
            return await message.respond(strings["server_error"])
        elif resp["status"] == 401:
            if resp["message"] == "ERROR_TOKEN_INVALID":
                return await message.respond(strings["invalid_token"])
            else:
                raise ValueError("Invalid response from server", resp)
        elif resp["status"] == 403:
            if resp["message"] == "ERROR_UNAUTHORIZED":
                return await message.respond(strings["unauthorized"])
            else:
                raise ValueError("Invalid response from server", resp)
        elif resp["status"] == 404:
            if resp["message"] == "ERROR_TEMPLATE_NOT_FOUND":
                newreq = requests.post(config["api_url"] + "/api/v1/getalltemplates", data={
                    "token": config["api_token"]
                })
                newreq = newreq.json()

                if newreq["status"] == "NOT_ENOUGH_PERMISSIONS":
                    return await message.respond(strings["not_enough_permissions"])
                elif newreq["status"] == "SUCCESS":
                    templates = strings["delimiter"].join(newreq["message"])
                    return await message.respond(strings["templates"].format(templates))
                elif newreq["status"] == "INVALID_TOKEN":
                    return await message.respond(strings["invalid_token"])
                else:
                    raise ValueError("Invalid response from server", newreq)
            else:
                raise ValueError("Invalid response from server", resp)
        elif resp["status"] != 200:
            raise ValueError("Invalid response from server", resp)

        req = requests.get(config["api_url"] + "/cdn/" + resp["message"])
        req.raise_for_status()
        file = BytesIO(req.content)
        file.seek(0)

        img = Image.open(file)
        with BytesIO() as sticker:
            img.save(sticker, "webp")
            sticker.name = "sticker.webp"
            sticker.seek(0)
            try:
                await reply.reply(file=sticker)
            except telethon.errors.rpcerrorlist.ChatSendStickersForbiddenError:
                await message.respond(strings["cannot_send_stickers"])
            file.close()


def get_markdown(reply):
    if not reply.entities:
        return []

    markdown = []
    for entity in reply.entities:
        md_item = {
            "Type": None,
            "Start": entity.offset,
            "End": entity.offset + entity.length - 1
        }
        if isinstance(entity, telethon.tl.types.MessageEntityBold):
            md_item["Type"] = "bold"
        elif isinstance(entity, telethon.tl.types.MessageEntityItalic):
            md_item["Type"] = "italic"
        elif isinstance(entity, (telethon.tl.types.MessageEntityMention, telethon.tl.types.MessageEntityTextUrl,
                                 telethon.tl.types.MessageEntityMentionName, telethon.tl.types.MessageEntityHashtag,
                                 telethon.tl.types.MessageEntityCashtag, telethon.tl.types.MessageEntityBotCommand,
                                 telethon.tl.types.MessageEntityUrl)):
            md_item["Type"] = "link"
        elif isinstance(entity, telethon.tl.types.MessageEntityCode):
            md_item["Type"] = "code"
        elif isinstance(entity, telethon.tl.types.MessageEntityStrike):
            md_item["Type"] = "stroke"
        elif isinstance(entity, telethon.tl.types.MessageEntityUnderline):
            md_item["Type"] = "underline"
        else:
            logger.warning("Unknown entity: " + str(entity))

        markdown.append(md_item)
    return markdown



__help__ = """
 - /id: get the current group id. If used by replying to a message, gets that user's id.
 - /runs: reply a random string from an array of replies.
 - /slap: slap a user, or get slapped if not a reply.
 - /info: get information about a user.
 - /gdpr: deletes your information from the bot's database. Private chats only.
 - /paste: Create a paste or a shortened url using del.dog
 - /getpaste: Get the content of a paste or shortened url from del.dog
 - /pastestats: Get stats of a paste or shortened url from del.dog
 - /removebotkeyboard: Got a nasty bot keyboard stuck in your group?
 - /shrug: try and check it out yourself.
 - /datetime <city>: Get the present date and time information
 - /camscanner: Reply to a image to scan and improve it's clarity.
*Instructions*
▪️The image should be a page with some written text on it (screenshots aren't permitted)
▪️The image should contain the page with four corners clearly visible
▪️The background should be somewhat darker than the page
▪️The image should contain only the page with no other objects like pencil, eraser etc. beside it(within the image)
*PRO TIP*
You can simply draw a border(a black square) around the portion you want to scan for better efficiency and edge detection
If you are still messed up send `/helpcamscanner` in pm for the tutorial !
 - /google <text>: perform a google search
 - /gps: <location> Get gps location.
 - /imdb - Get full info about a movie with imdb.com
 - /img <text>: Search Google for images and returns them\nFor greater no. of results specify lim, For eg: `/img hello lim=10`
 - /img2text <lang>: Type in reply to a image to extract the text from it 	
 - /img2textlang: List all the available languages	
 - /phone <number in international format>: Check if the number really exists and returns information about it.If the number is fake then it will return null-type response 
Example: `/phone +9162XX93X805`, `/phone +1916X978XX1`
 - /news: Returns today's Indian Headlines (ONLY WORKS IN PM)
 - /getqr: Get the QR Code content from the replied QR Code
 - /makeqr <content>: Make a QR Code from the given message (text, link, etc...)
 - /reverse: Does a reverse image search of the media which it was replied to.
 - /rmbg: Type in reply to a media to remove it's background 
 - /stt: Type in reply to a voice message(english only) to extract text from it.
 - /tts <lang | text>: Returns a speech note of the text provided
 - /torrent <text>: Search for torrent links
If you are still messed up send `/helptorrent` in pm for the tutorial !
 - /wall <topic>: Searches best wallpaper on the given topic and returns them 
 - /weather <city>: Get weather info in a particular place
 - /wttr <city>: Advanced weather module, usage same as /weather
 - /wttr moon: Get the current status of moon 
 - /wiki <text>: Returns search from wikipedia for the input text
 - /yt <text>: perform a youtube search
 - /ytaudio <link> or /ytvideo <link>: Downlods a video or audio from a youtube video to the bots local server
 - /zip: reply to a telegram file to compressing in .zip format
 - /unzip: reply to a telegram file to decompress it from the .zip format
 - /git <username>: Returns info about a GitHub user or organization.
 - /repo <username>: Return the GitHub user or organization repository list 
 - /magisk: Get latest magisk updates 
 - /app <appname>: Search for an app in playstore 
 - /magisk: Get the latest Magisk releases
 - /device <codename>: Get info about an Android device
 - /codename <brand> <device>: Search for Android device codename
 - /specs <brand> <device>: Get device specifications info
 - /twrp <codename>: Get the latest TWRP download for an Android device
 - /song <songname artist(optional)>: uploads the song in it's best quality available
 - /barcode <text>: makes a barcode out of the text, crop the barcode if you don't want to reveal the text
 - /quotly <text> / reply to a message: an alternative to @QuotLyBot
"""

__mod_name__ = "Utilities ⚡"


ID_HANDLER = DisableAbleCommandHandler("id", get_id, pass_args=True, admin_ok=True)
RUNS_HANDLER = DisableAbleCommandHandler("runs", runs, admin_ok=True)
SHRUG_HANDLER = DisableAbleCommandHandler("shrug", shrug, admin_ok=True)
SLAP_HANDLER = DisableAbleCommandHandler("slap", slap, pass_args=True, admin_ok=True)
INFO_HANDLER = DisableAbleCommandHandler("info", info, pass_args=True, admin_ok=True)
GITHUB_HANDLER = DisableAbleCommandHandler("git", github)
REPO_HANDLER = DisableAbleCommandHandler("repo", repo, pass_args=True, admin_ok=True)
ECHO_HANDLER = CommandHandler("echo", echo)
MD_HELP_HANDLER = CommandHandler("markdownhelp", markdown_help, filters=Filters.private)
GDPR_HANDLER = CommandHandler("gdpr", gdpr, filters=Filters.private)
PASTE_HANDLER = DisableAbleCommandHandler("paste", paste, pass_args=True)
GET_PASTE_HANDLER = DisableAbleCommandHandler("getpaste", get_paste_content, pass_args=True)
PASTE_STATS_HANDLER = DisableAbleCommandHandler("pastestats", get_paste_stats, pass_args=True)
LYRICS_HANDLER = CommandHandler("lyrics", lyrics, pass_args=True)
TIME_HANDLER = CommandHandler("datetime", gettime)
STATS_HANDLER = CommandHandler("stats", stats, filters=Filters.user(OWNER_ID))
UD_HANDLER = CommandHandler("define", define)


dispatcher.add_handler(STATS_HANDLER)
dispatcher.add_handler(TIME_HANDLER)
dispatcher.add_handler(PASTE_HANDLER)
dispatcher.add_handler(GET_PASTE_HANDLER)
dispatcher.add_handler(PASTE_STATS_HANDLER)
dispatcher.add_handler(ID_HANDLER)
dispatcher.add_handler(RUNS_HANDLER)
dispatcher.add_handler(SLAP_HANDLER)
dispatcher.add_handler(LYRICS_HANDLER)
dispatcher.add_handler(INFO_HANDLER)
dispatcher.add_handler(ECHO_HANDLER)
dispatcher.add_handler(SHRUG_HANDLER)
dispatcher.add_handler(UD_HANDLER)
dispatcher.add_handler(MD_HELP_HANDLER)
dispatcher.add_handler(GDPR_HANDLER)
dispatcher.add_handler(GITHUB_HANDLER)
dispatcher.add_handler(REPO_HANDLER)
dispatcher.add_handler(DisableAbleCommandHandler("removebotkeyboard", reply_keyboard_remove))
