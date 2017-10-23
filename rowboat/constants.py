import re
import yaml
from disco.types.user import GameType, Status

# Emojis
GREEN_TICK_EMOJI_ID = 351769190190809091
RED_TICK_EMOJI_ID = 351769542415876096
GREEN_TICK_EMOJI = 'green_tick:{}'.format(GREEN_TICK_EMOJI_ID)
RED_TICK_EMOJI = 'red_tick:{}'.format(RED_TICK_EMOJI_ID)
STAR_EMOJI = u'\U00002B50'
STATUS_EMOJI = {
    Status.ONLINE: ':status_online:352580726413066241',
    Status.IDLE: ':status_away:352580726845079553',
    Status.DND: ':status_dnd:352580726736289802',
    Status.OFFLINE: ':status_offline:352580726664724501',
    GameType.STREAMING: ':status_streaming:352581805070614531',
}
SNOOZE_EMOJI = u'\U0001f4a4'


# Regexes
INVITE_LINK_RE = re.compile(r'(discordapp.com/invite|discord.me|discord.gg)(?:/#)?(?:/invite)?/([a-z0-9\-]+)', re.I)
URL_RE = re.compile(r'(https?://[^\s]+)')
EMOJI_RE = re.compile(r'<:(.+):([0-9]+)>')
USER_MENTION_RE = re.compile('<@!?([0-9]+)>')

# IDs and such
ROWBOAT_GUILD_ID = 330967164939010048
ROWBOAT_USER_ROLE_ID = 346507606841491456
ROWBOAT_CONTROL_CHANNEL = 346508082815434754

# Discord Error codes
ERR_UNKNOWN_MESSAGE = 10008

# Etc
YEAR_IN_SEC = 60 * 60 * 24 * 365
CDN_URL = 'https://twemoji.maxcdn.com/2/72x72/{}.png'

# Loaded from files
with open('data/badwords.txt', 'r') as f:
    BAD_WORDS = f.readlines()

# Merge in any overrides in the config
with open('config.yaml', 'r') as f:
    loaded = yaml.load(f.read())
    locals().update(loaded.get('constants', {}))
