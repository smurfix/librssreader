# -*- coding: utf-8 -*-


def getBasicConfig():
    import inspect
    ReaderBasicConfig = None
    try:
        ReaderBasicConfig = \
            inspect.currentframe().f_back.f_back.f_globals['ReaderBasicConfig']
    except KeyError:
        from inoreaderconfig import ReaderBasicConfig
    return ReaderBasicConfig
