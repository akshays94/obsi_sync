import os
import logging
from datetime import datetime

LOG_LEVEL = logging.DEBUG

FORMAT = '[%(levelname)s:%(name)s:%(asctime)s] %(message)s'
formatter = logging.Formatter(FORMAT)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler('obsi_sync.log')
file_handler.setFormatter(formatter)

log = logging.getLogger('osynclogger')
log.setLevel(LOG_LEVEL)

log.addHandler(console_handler)
log.addHandler(file_handler)


def main():

    log.debug('STARTED')

    log.debug('BUILDING COMMAND')

    cmd = f"{get_repo()} \
        git add -A; \
        git commit -am '{get_commit_msg()}'; \
        git pull origin master; \
        git push -u origin master;"

    log.debug(f'RUNNING -> {cmd}')

    os.system(cmd)

    log.debug('COMPLETED')


def get_repo():
    return "cd ~/projects/akies-obsidian;"


def get_commit_msg():
    return f'OBS: {datetime.strftime(datetime.now(), "%d-%m-%Y %H:%M")}'


if __name__ == '__main__':
    main()
