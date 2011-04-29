dolmen.json
***********

  >>> import dolmen.json

Simple function decoration
==========================

  >>> @dolmen.json.json
  ... def print_me():
  ...     return [{"grok": "mammoth"}]

  >>> print_me()
  '[{"grok": "mammoth"}]'


Simple method decoration
========================

  >>> class SomeRenderer(object):
  ...
  ...    @dolmen.json.json
  ...    def ints(self):
  ...        return (1, 2, 3, 4)
  ...
  ...    @dolmen.json.json
  ...    def floats(self):
  ...        return (.1, .2, .3, .4)

  >>> renderer = SomeRenderer()

  >>> renderer.ints()
  '[1, 2, 3, 4]'

  >>> renderer.floats()
  '[0.1, 0.2, 0.3, 0.4]'


Decoration of an IView method
=============================

  >>> from zope.interface import implements
  >>> from cromlech.io.testing import TestResponse
  >>> from cromlech.browser.interfaces import IView

  >>> class View(object):
  ...     implements(IView)
  ...
  ...     response = None
  ...
  ...     def __init__(self, context, request):
  ...         self.context = context
  ...         self.request = request
  ...
  ...     def namespace(self):
  ...         return {}
  ...
  ...     def update(self, *args, **kwargs):
  ...         self.response = TestResponse()
  ...
  ...     @dolmen.json.json
  ...     def render(self):
  ...         return {'value': 1, 'something': u"somevalue"}
  ...
  ...     def __call__(self, *args, **kwargs):	
  ...         self.update()
  ... 	      self.response.write(self.render())
  ...         return self.response

  >>> mammoth = object()
  >>> request = object()

  >>> from zope.interface.verify import verifyObject
  >>> view = View(mammoth, request)
  >>> verifyObject(IView, view)
  True

  >>> view.render()
  '{"something": "somevalue", "value": 1}'

  >>> print view.response
  None

  >>> view()
  <cromlech.io.testing.TestResponse object at ...>

  >>> view.response is not None
  True

  >>> view.response.body
  '{"something": "somevalue", "value": 1}'

  >>> view.response.headers
  {'Content-Type': 'application/json'}
