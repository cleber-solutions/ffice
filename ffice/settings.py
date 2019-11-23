from os import getenv
from pathlib import PosixPath
from prettyconf import config


HOME = getenv('HOME')


CONFIG_DIR = PosixPath(
    config(
        'FFICE_CONFIG_DIR',
        default=f'{HOME}/.ffice'
    )
)
