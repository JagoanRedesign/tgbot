from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 5166575484  # my telegram ID
    OWNER_USERNAME = "SonOfLars"  # my telegram username
    API_KEY = "5937294943:AAF__32hQvheNIGI8D3MiTr30HNhXm56oF8y"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database'  # sample db credentials
    MESSAGE_DUMP = '-1234567890' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [5166575484, 83489514]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
