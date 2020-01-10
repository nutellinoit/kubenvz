import os

DOWNLOAD_PATH = os.environ.get('TERRA_PATH', os.environ.get('HOME') + "/.kubenvz") + "/"
VERSION_FILE = ".kubenvz"