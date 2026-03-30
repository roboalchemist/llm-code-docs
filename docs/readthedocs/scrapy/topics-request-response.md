# Requests and Responses

Scrapy uses `Request` and `Response` objects for crawling web
sites.

Typically, `Request` objects are generated in the spiders and pass
across the system until they reach the Downloader, which executes the request
and returns a `Response` object which travels back to the spider that
issued the request.

Both `Request` and `Response` classes have subclasses which add
functionality not required in the base classes. These are described
below in Request subclasses and
Response subclasses.

## Request objects

*class *scrapy.Request(**args: Any*, ***kwargs: Any*)

Represents an HTTP request, which is usually generated in a Spider and
executed by the Downloader, thus generating a `Response`.

Parameters:

- 

**url** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – 

the URL of this request

If the URL is invalid, a `ValueError` [https://docs.python.org/3/library/exceptions.html#ValueError] exception is raised.

- 

**callback** (*Callable**[**Concatenate**[**Response**, **...**]**, **Any**] **| **None*) – sets `callback`, defaults to `None`.

- 

**method** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – the HTTP method of this request. Defaults to `'GET'`.

- 

**meta** (*dict* [https://docs.python.org/3/library/stdtypes.html#dict]) – the initial values for the `Request.meta` attribute. If
given, the dict passed in this parameter will be shallow copied.

- 

**body** (*bytes* [https://docs.python.org/3/library/stdtypes.html#bytes]* or **str* [https://docs.python.org/3/library/stdtypes.html#str]) – the request body. If a string is passed, then it’s encoded as
bytes using the `encoding` passed (which defaults to `utf-8`). If
`body` is not given, an empty bytes object is stored. Regardless of the
type of this argument, the final value stored will be a bytes object
(never a string or `None`).

- 

**headers** (*dict* [https://docs.python.org/3/library/stdtypes.html#dict]) – 

the headers of this request. The dict values can be strings
(for single valued headers) or lists (for multi-valued headers). If
`None` is passed as value, the HTTP header will not be sent at all.

Caution

Cookies set via the `Cookie` header are not considered by the
CookiesMiddleware. If you need to set cookies for a request, use the
`cookies` argument. This is a known current limitation that is being
worked on.