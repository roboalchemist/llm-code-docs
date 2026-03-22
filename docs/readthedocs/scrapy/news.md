# Release notes

## Scrapy 2.14.2 (2026-03-12)

### Security bug fixes

- 

Values from the `Referrer-Policy` header of HTTP responses are no longer
executed as Python callables. See the cwxj-rr6w-m6w7 [https://github.com/scrapy/scrapy/security/advisories/GHSA-cwxj-rr6w-m6w7] security advisory
for details.

- 

In line with the standard [https://fetch.spec.whatwg.org/#http-redirect-fetch], 301 redirects of
`POST` requests are converted into `GET` requests.

Converting to a `GET` request implies not only a method change, but also
omitting the body and `Content-*` headers in the redirect request. On
cross-origin redirects (for example, cross-domain redirects), this is
effectively a security bug fix for scenarios where the body contains
secrets.

### Deprecations

- 

Passing a response URL string as the first positional argument to
`scrapy.spidermiddlewares.referer.RefererMiddleware.policy()` is
deprecated. Pass a `Response` instead.

The parameter has also been renamed to `response` to reflect this change.
The old parameter name (`resp_or_url`) is deprecated.

### New features

- 

Added a new setting, `REFERER_POLICIES`, to allow customizing
supported referrer policies.

### Bug fixes

- 

Made additional redirect scenarios convert to `GET` in line with the
standard [https://fetch.spec.whatwg.org/#http-redirect-fetch]:

  - 

Only `POST` 302 redirects are converted into `GET` requests; other
methods are preserved.

  - 

`HEAD` 303 redirects are not converted into `GET` requests.

  - 

`GET` 303 redirects do not have their body or standard `Content-*`
headers removed.

- 

Redirects where the original request body is dropped now also have their
`Content-Encoding`, `Content-Language` and `Content-Location` headers
removed, in addition to the `Content-Type` and `Content-Length` headers
that were already being removed.

- 

Redirects now preserve the source URL fragment if the redirect URL does not
include one. This is useful when using browser-based download handlers,
such as scrapy-playwright [https://github.com/scrapy-plugins/scrapy-playwright] or scrapy-zyte-api [https://scrapy-zyte-api.readthedocs.io/en/latest/], while letting Scrapy
handle redirects.

- 

The `Referer` header is now removed on redirect if
`RefererMiddleware` is disabled.

- 

The handling of the `Referer` header on redirects now takes into account
the `Referer-Policy` header of the response that triggers the redirect.

## Scrapy 2.14.1 (2026-01-12)

### Deprecations

- 

`scrapy.utils.defer.maybeDeferred_coro()` is deprecated. (issue 7212 [https://github.com/scrapy/scrapy/issues/7212])

### Bug fixes

- 

Fixed custom stats collectors that require a `spider` argument in their
`open_spider()` and `close_spider()` methods not receiving the
argument when called by the engine.

Note, however, that the `spider` argument is now deprecated and will stop
being passed in a future version of Scrapy.

(issue 7213 [https://github.com/scrapy/scrapy/issues/7213])

### Quality assurance

- 

Replaced deprecated `codecov/test-results-action@v1` GitHub Action with
`codecov/codecov-action@v5`.
(issue 7180 [https://github.com/scrapy/scrapy/issues/7180], issue 7215 [https://github.com/scrapy/scrapy/issues/7215])

## Scrapy 2.14.0 (2026-01-05)

Highlights:

- 

More coroutine-based replacements for Deferred-based APIs

- 

The default priority queue is now `DownloaderAwarePriorityQueue`

- 

Dropped support for Python 3.9 and PyPy 3.10

- 

Improved and documented the API for custom download handlers

### Modified requirements

- 

Dropped support for Python 3.9.
(issue 7121 [https://github.com/scrapy/scrapy/issues/7121])

- 

Dropped support for PyPy 3.10.
(issue 7050 [https://github.com/scrapy/scrapy/issues/7050])

- 

Increased the minimum versions of the following dependencies:

  - 

lxml [https://lxml.de/]: 4.6.0 → 4.6.4

  - 

Pillow [https://github.com/python-pillow/Pillow] (optional dependency): 8.0.0 → 8.3.2

  - 

botocore [https://github.com/boto/botocore] (optional dependency): 1.4.87 → 1.13.45

- 

Restored support for `brotlicffi` dropped in Scrapy 2.13.4. Its minimum
supported version is now `1.2.0.0`.
(issue 7160 [https://github.com/scrapy/scrapy/issues/7160])

### Backward-incompatible changes

- 

If you set the `TWISTED_REACTOR` setting to a non-asyncio
value at the spider level, you
may now need to set the `FORCE_CRAWLER_PROCESS` setting to
`True` when running Scrapy via its command-line tool to avoid a reactor mismatch exception.
(issue 6845 [https://github.com/scrapy/scrapy/issues/6845])

- 

The `log_count/*` stats no longer count some of the early messages that
they counted before. While the earliest log messages, emitted before the
counter is initialized, were never counted, the counter initialization now
happens later than in previous Scrapy versions. You may need to adjust
expected values if you retrieve and compare values of these stats in your
code.
(issue 7046 [https://github.com/scrapy/scrapy/issues/7046])

- 

The classes listed below are now abstract base classes [https://docs.python.org/3/glossary.html#term-abstract-base-class]. They cannot be instantiated directly and their subclasses
need to override the abstract methods listed below to be able to be
instantiated. If you previously instantiated these classes directly, you
will now need to subclass them and provide trivial (e.g. empty)
implementations for the abstract methods.

  - 

`scrapy.commands.ScrapyCommand`

    - 

`run()`

    - 

`short_desc()`