import platform
from configparser import ConfigParser

def readConfig(section, key):
    config = ConfigParser()
    if platform.system() == 'Windows':
        config.read("conf.ini")
    else:
        config.read("conf.ini")
    return config.get(section, key)
