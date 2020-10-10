import os
import configparser

ENV = os.environ.get('ENV', 'development')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG = configparser.ConfigParser()
CONFIG.read(os.path.join(BASE_DIR, 'resources', f'{ENV}.ini'))

HOST = CONFIG.get('DEFAULT', 'HOST')
PORT = CONFIG.getint('DEFAULT', 'PORT')
DEBUG = CONFIG.getboolean('DEFAULT', 'DEBUG')
RELOAD = CONFIG.getboolean('DEFAULT', 'RELOAD')
