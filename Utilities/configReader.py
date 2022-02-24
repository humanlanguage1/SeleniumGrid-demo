from configparser import ConfigParser


def readConfig(section, key):
    config = ConfigParser()
    config.read("conf.ini")
    return config.get(section, key)

