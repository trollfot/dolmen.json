# -*- coding: utf-8 -*-

from cromlech.io.interfaces import IResponse
from cromlech.browser.interfaces import IView


def simple_jsonification(result):
    # We need more error handling here
    try:
        import cjson
        return cjson.encode(result)
    except ImportError:
        import json
        return json.dumps(result)
    else:
        raise NotImplementedError


class json(object):

    def __init__(self, func):
        self.func = func

    def transform(self, result):
        return simple_jsonification(result)

    def __get__(self, obj, type=None):
        return self.__class__(self.func.__get__(obj, type))
 
    def __call__(self, *args, **kw):
        result = self.transform(self.func(*args, **kw))
        view = getattr(self.func, 'im_self', None)
        if view is not None and IView.providedBy(view):
            # this is a method of an IRenderer
            if view.response is not None:
                resp = IResponse(view.response)
                resp.headers['Content-Type'] = 'application/json'
        return result
