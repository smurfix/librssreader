# -*- coding: utf-8 -*-

# librssreader
# Copyright (C) 2014  Zigler Zhang <zigler.zhang@gmail.com>
# Python library for the Google Reader Like API

__author__ = "Zigler Zhang <zigler.zhang@gmail.com>"
__version__ = "0.0.8"
__copyright__ = "MIT License"

try:
    import requests
except ImportError:
    # Will occur during setup.py install
    pass
else:
    import imp
    from .rssreader import RssReader
    from .auth import AuthenticationMethod, ClientAuthMethod, OAuthMethod, OAuth2Method
    from .items import *
