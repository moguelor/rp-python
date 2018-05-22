#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import subprocess
import os
import sys
from config import (name_server_test, name_server_prod)
from config_local import (base_path_local_source)

# Mensaje para confirmar.
def confirmMessage(message):
    reply = str(input(message + ' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return print("Uhhhh... please enter ")

# Devuelve el texto con color.
def printWithColor(text):
    color_header = '\033[95m'
    color_end = '\033[0m'
    print (color_header + text + color_end)

# Obtener el nombre del servidor.
def getNameServer(env = 'test'):
    if(env == 'test' or env == 'demo'):
        return name_server_test
    elif(env == 'prod'):
        return name_server_prod
    else:
        return ''

# Obtener la base principal de las fuentes.
def getBasePathSource(env = 'dev'):
    if(env == 'dev'):
        return base_path_local_source
    elif (env == 'test' or env == 'demo' or env == 'prod'):
        return './'