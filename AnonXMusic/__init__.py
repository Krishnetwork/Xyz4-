from KRISH.core.bot import LORD 
from KRISH.core.dir import dirr
from KRISH.core.git import git
from KRISH.core.userbot import Userbot
from KRISH.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = LORD ()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
