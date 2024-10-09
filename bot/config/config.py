from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file="config.env", env_ignore_empty=True)

    API_ID: int = 123
    API_HASH: str = 'qwerty'

    USE_REF: bool = True
    REF_ID: str = 'f7505768028'

    USE_RANDOM_DELAY_IN_RUN: bool = True
    RANDOM_DELAY_IN_RUN: list[int] = [5, 60]

    SLEEP_TIME_IN_MINUTES: list[int] = [15, 30]

    ENABLE_AUTO_TASKS: bool = True
    ENABLE_AUTO_DRAW: bool = True
    ENABLE_JOIN_TG_CHANNELS: bool = True
    ENABLE_CLAIM_REWARD: bool = True
    ENABLE_AUTO_UPGRADE: bool = True

    ENABLE_SSL: bool = False

    PAINT_REWARD_MAX: int = 7
    ENERGY_LIMIT_MAX: int = 6
    RE_CHARGE_SPEED_MAX: int = 11

    BOOSTS_BLACK_LIST: list[str] = ['invite3frens', 'INVITE_FRIENDS', 'TON_TRANSACTION', 'BOOST_CHANNEL', 'ACTIVITY_CHALLENGE', 'CONNECT_WALLET']
    TASKS_TODO_LIST: list[str] = ["x:notcoin", "x:notpixel", "paint20pixels", "leagueBonusSilver", "leagueBonusGold", "leagueBonusPlatinum", "channel:notpixel_channel", "channel:notcoin", "premium"]

    USE_PROXY_FROM_FILE: bool = True

settings = Settings()
