dolmen.json
***********

  >>> import dolmen.json
  >>> from zope.interface import implements
  >>> from cromlech.io.tests import TestResponse
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
  '{"something": "somevalue", "value": 1}'

  >>> view.response is not None
  True

  >>> print view.response.body
  '{"something": "somevalue", "value": 1}'

  >>> print view.response.headers
  {'Content-Type': 'application/json'}
