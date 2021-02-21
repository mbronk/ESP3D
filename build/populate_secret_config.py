Import("env")
import os
import shutil

def populate_secret_config():
    if not os.path.isfile('esp3d/secret_config.h'):
        print("")
        print("Creating 'secret_config.h' file from default")
        shutil.copy('esp3d/secret_config.example', 'esp3d/secret_config.h')

populate_secret_config()
