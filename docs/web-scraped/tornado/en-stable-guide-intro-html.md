# Source: https://www.tornadoweb.org/en/stable/guide/intro.html

Title: Introduction — Tornado 6.5.5 documentation

URL Source: https://www.tornadoweb.org/en/stable/guide/intro.html

Markdown Content:
[Tornado](http://www.tornadoweb.org/) is a Python web framework and asynchronous networking library, originally developed at [FriendFeed](https://en.wikipedia.org/wiki/FriendFeed). By using non-blocking network I/O, Tornado can scale to tens of thousands of open connections, making it ideal for [long polling](http://en.wikipedia.org/wiki/Push_technology#Long_polling), [WebSockets](http://en.wikipedia.org/wiki/WebSocket), and other applications that require a long-lived connection to each user.

Tornado can be roughly divided into three major components:

*   A web framework (including [`RequestHandler`](https://www.tornadoweb.org/en/stable/web.html#tornado.web.RequestHandler "tornado.web.RequestHandler") which is subclassed to create web applications, and various supporting classes).

*   Client- and server-side implementions of HTTP ([`HTTPServer`](https://www.tornadoweb.org/en/stable/httpserver.html#tornado.httpserver.HTTPServer "tornado.httpserver.HTTPServer") and [`AsyncHTTPClient`](https://www.tornadoweb.org/en/stable/httpclient.html#tornado.httpclient.AsyncHTTPClient "tornado.httpclient.AsyncHTTPClient")).

*   An asynchronous networking library including the classes [`IOLoop`](https://www.tornadoweb.org/en/stable/ioloop.html#tornado.ioloop.IOLoop "tornado.ioloop.IOLoop") and [`IOStream`](https://www.tornadoweb.org/en/stable/iostream.html#tornado.iostream.IOStream "tornado.iostream.IOStream"), which serve as the building blocks for the HTTP components and can also be used to implement other protocols.

The Tornado web framework and HTTP server together offer a full-stack alternative to [WSGI](http://www.python.org/dev/peps/pep-3333/). While it is possible to use the Tornado HTTP server as a container for other WSGI frameworks ([`WSGIContainer`](https://www.tornadoweb.org/en/stable/wsgi.html#tornado.wsgi.WSGIContainer "tornado.wsgi.WSGIContainer")), this combination has limitations and to take full advantage of Tornado you will need to use Tornado’s web framework and HTTP server together.
