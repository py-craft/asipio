# flake8: noqa: F401,F403
from importlib.metadata import version, PackageNotFoundError

__author__ = 'Vardan Aloyan'
__email__ = 'valoyan2@gmail.com'
try:
    __version__ = version("aiovoip")
except PackageNotFoundError:
    __version__ = "0.0.0-dev"
    
from .dialog import *
from .message import *
from .uri import *
from .protocol import *
from .application import *
from .exceptions import *
from .dialplan import *
