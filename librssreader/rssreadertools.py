# -*- coding: utf-8 -*-


def getBasicConfig():
    import inspect
    ReaderBasicConfig = None
    cur_f = inspect.currentframe()
    while cur_f is not None and ReaderBasicConfig is None:
        try:
            ReaderBasicConfig = \
                cur_f.f_globals['ReaderBasicConfig']
        except KeyError:
            pass
        finally:
            cur_f = cur_f.f_back
    if ReaderBasicConfig is None:
        from inoreaderconfig import ReaderBasicConfig
    return ReaderBasicConfig
