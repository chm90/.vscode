from glob import iglob
import os
from os import path


THIS_DIR = path.dirname(path.realpath(__file__))
JSON_FILES_PATTERN = path.join(THIS_DIR,'*.json')
VSCODE_CONFIG_DIR = path.expanduser('~/Library/Application Support/Code/User/')


def main():
    for config_path in iglob(JSON_FILES_PATTERN):
        config_fn = path.basename(config_path)
        config_link = path.join(VSCODE_CONFIG_DIR,config_fn)
        if path.isfile(config_link):
            os.remove(config_link)
        os.link(config_path,config_link)
if __name__ == '__main__':
    main()
