# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.curl.html

Title: Async pyCurl HTTP Client - kombu.asynchronous.http.curl — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.curl.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.asynchronous.http.curl.html).

HTTP Client using pyCurl.

_class_ kombu.asynchronous.http.curl.CurlClient(_hub:[Hub](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.html#kombu.asynchronous.Hub "kombu.asynchronous.Hub")|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")=None_, _max\_clients:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")=10_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/http/curl.html#CurlClient)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.curl.html#kombu.asynchronous.http.curl.CurlClient "Link to this definition")
Curl HTTP Client.

Curl _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.curl.html#kombu.asynchronous.http.curl.CurlClient.Curl "Link to this definition")add_request(_request_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/http/curl.html#CurlClient.add_request)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.curl.html#kombu.asynchronous.http.curl.CurlClient.add_request "Link to this definition")close()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/http/curl.html#CurlClient.close)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.curl.html#kombu.asynchronous.http.curl.CurlClient.close "Link to this definition")on_readable(_fd_, _\_pycurl=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/http/curl.html#CurlClient.on_readable)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.curl.html#kombu.asynchronous.http.curl.CurlClient.on_readable "Link to this definition")on_writable(_fd_, _\_pycurl=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/http/curl.html#CurlClient.on_writable)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.curl.html#kombu.asynchronous.http.curl.CurlClient.on_writable "Link to this definition")
