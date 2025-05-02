import os
import logging
from datetime import datetime

LOG_LEVEL = logging.DEBUG

FORMAT = "[%(levelname)s:%(name)s:%(asctime)s] %(message)s"
formatter = logging.Formatter(FORMAT)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler("obsi_sync.log")
file_handler.setFormatter(formatter)

log = logging.getLogger("osynclogger")
log.setLevel(LOG_LEVEL)

log.addHandler(console_handler)
log.addHandler(file_handler)


def main():
    log.debug("STARTED FOR WINDOWS")

    log.debug("BUILDING COMMAND")

    cmd = f'{get_repo()} && git add -A && git commit -am "{get_commit_msg()}"'
    log.debug(f"RUNNING -> {cmd}")
    os.system(cmd)

    cmd = f"{get_repo()} && git pull origin master"
    log.debug(f"RUNNING -> {cmd}")
    os.system(cmd)

    cmd = f"{get_repo()} && git push -u origin master"
    log.debug(f"RUNNING -> {cmd}")
    os.system(cmd)

    log.debug("COMPLETED FOR WINDOWS")


def get_repo():
    # /d allows changing drives (important if you’re not on D:)
    return r"cd /d D:\akie_projects\akies-obsidian"


def get_commit_msg():
    return f'OBS: WINDOWS {datetime.strftime(datetime.now(), "%d-%m-%Y %H:%M")}'


if __name__ == "__main__":
    main()
