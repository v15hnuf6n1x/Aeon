from bot import LOGGER
from pyshorteners import Shortener

def tinyfy(long_url):
    s = Shortener()
    try:
        short_url = long_url
        LOGGER.info(f'tinyfied {long_url} to {short_url}')
        return long_url
    except Exception:
        LOGGER.error(f'Failed to shorten URL: {long_url}')
        return long_url
