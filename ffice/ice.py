import os
import re
from shutil import rmtree
import sys

import click

from .user_chrome import generate_user_chrome
from .user_js import generate_user_js
from . import settings


@click.command()
@click.argument('url')
@click.option('--profile', default=None)
@click.option('--show-command', default=False)
def run(url, profile=None, show_command=False):
    profileid = profile or re.sub(r'^https?://', '', url)
    profileid = re.sub(r'[^a-zA-Z0-9-:.]+', '_', profileid)

    profilepath = settings.CONFIG_DIR / 'firefox' / profileid
    chromepath = profilepath / 'chrome'
    chromepath.mkdir(
        parents=True,
        exist_ok=True
    )

    generate_user_chrome(chromepath)
    generate_user_js(profilepath)

    cmd = f'firefox -profile {profilepath} -no-remote -new-instance "{url}"'

    if show_command:
        print(cmd)
        sys.exit(0)

    os.system(cmd)

    cache2 = profilepath / 'cache2'
    rmtree(cache2)
