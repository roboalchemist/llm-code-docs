# Source: https://samuraisam.github.io/django-json-rpc/

Title: samuraisam/django-json-rpc @ GitHub

URL Source: https://samuraisam.github.io/django-json-rpc/

Markdown Content:
[![Image 1](http://github.com/images/modules/download/zip.png)](http://github.com/samuraisam/django-json-rpc/zipball/master)[![Image 2](http://github.com/images/modules/download/tar.png)](http://github.com/samuraisam/django-json-rpc/tarball/master)

A basic JSON-RPC Implementation for your Django-powered sites.

Features:

*   Simple, pythonic API
*   Support for Django authentication
*   Mostly supports JSON-RPC 1.1 and 2.0 Spec
*   Proxy to test your JSON Service

Dependencies
------------

django

Install
-------

python setup.py install

License
-------

MIT

Authors
-------

Samuel Sutch (samuraiblog@gmail.com)

Contact
-------

(samuraiblog@gmail.com)

Download
--------

You can download this project in either [zip](http://github.com/samuraisam/django-json-rpc/zipball/master) or [tar](http://github.com/samuraisam/django-json-rpc/tarball/master) formats.

You can also clone the project with [Git](http://git-scm.com/) by running:

$ git clone git://github.com/samuraisam/django-json-rpc
Usage
-----

The basic API:

**myproj/myapp/views.py**

```
from jsonrpc import jsonrpc_method
     
    @jsonrpc_method('myapp.sayHello')
    def whats_the_time(request, name='Lester'):
      return "Hello %s" % name
     
    @jsonrpc_method('myapp.gimmeThat', authenticated=True)
    def something_special(request, secret_data):
      return {'sauce': ['authenticated', 'sauce']}
```

**myproj/urls.py**

```
from jsonrpc import jsonrpc_site
    import myproj.myapp.views # you must import the views that need connected
     
    urls += patterns('', (r'^json/', jsonrpc_site.dispatch))
```

**To test your service:**

```
>>> from jsonrpc.proxy import ServiceProxy
     
    >>> s = ServiceProxy('http://localhost:8080/json/')
     
    >>> s.myapp.sayHello('Sam')
    {u'error': None, u'id': u'jsonrpc', u'result': u'Hello Sam'}
     
    >>> s.myapp.gimmeThat('username', 'password', 'test data')
    {u'error': None, u'id': u'jsonrpc', u'result': {u'sauce': [u'authenticated', u'sauce']}}
```

We add the `jsonrpc_version` variable to the request object. It be either '1.0' or '2.0'. Arg.
