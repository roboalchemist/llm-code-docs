# Source: https://boltons.readthedocs.io/en/latest/urlutils.html

Title: Structured URL — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/urlutils.html

Markdown Content:
`urlutils` - Structured URL[](https://boltons.readthedocs.io/en/latest/urlutils.html#module-boltons.urlutils "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

`urlutils` is a module dedicated to one of software’s most versatile, well-aged, and beloved data structures: the URL, also known as the [Uniform Resource Locator](https://en.wikipedia.org/wiki/Uniform_Resource_Locator).

Among other things, this module is a full reimplementation of URLs, without any reliance on the `urlparse` or [`urllib`](https://docs.python.org/3/library/urllib.html#module-urllib "(in Python v3.14)") standard library modules. The centerpiece and top-level interface of urlutils is the [`URL`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL "boltons.urlutils.URL") type. Also featured is the [`find_all_links()`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.find_all_links "boltons.urlutils.find_all_links") convenience function. Some low-level functions and constants are also below.

The implementations in this module are based heavily on [RFC 3986](https://tools.ietf.org/html/rfc3986) and [RFC 3987](https://tools.ietf.org/html/rfc3987), and incorporates details from several other RFCs and [W3C documents](https://www.w3.org/TR/uri-clarification/).

Added in version 17.2.

The URL type[](https://boltons.readthedocs.io/en/latest/urlutils.html#the-url-type "Link to this heading")
-----------------------------------------------------------------------------------------------------------

_class_ boltons.urlutils.URL(_url=''_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/urlutils.html#URL)[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL "Link to this definition")
The URL is one of the most ubiquitous data structures in the virtual and physical landscape. From blogs to billboards, URLs are so common, that it’s easy to overlook their complexity and power.

There are 8 parts of a URL, each with its own semantics and special characters:

> *   [`scheme`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.scheme "boltons.urlutils.URL.scheme")
> 
> *   [`username`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.username "boltons.urlutils.URL.username")
> 
> *   [`password`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.password "boltons.urlutils.URL.password")
> 
> *   [`host`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.host "boltons.urlutils.URL.host")
> 
> *   [`port`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.port "boltons.urlutils.URL.port")
> 
> *   [`path`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.path "boltons.urlutils.URL.path")
> 
> *   [`query_params`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.query_params "boltons.urlutils.URL.query_params") (query string parameters)
> 
> *   [`fragment`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.fragment "boltons.urlutils.URL.fragment")

Each is exposed as an attribute on the URL object. RFC 3986 offers this brief structural summary of the main URL components:

 foo://user:pass@example.com:8042/over/there?name=ferret#nose
 \_/   \_______/ \_________/ \__/\_________/ \_________/ \__/
  |        |          |        |      |           |        |
scheme  userinfo     host     port   path       query   fragment

And here’s how that example can be manipulated with the URL type:

>>> url = URL('foo://example.com:8042/over/there?name=ferret#nose')
>>> print(url.host)
example.com
>>> print(url.get_authority())
example.com:8042
>>> print(url.qp['name'])  # qp is a synonym for query_params
ferret

URL’s approach to encoding is that inputs are decoded as much as possible, and data remains in this decoded state until re-encoded using the [`to_text()`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.to_text "boltons.urlutils.URL.to_text") method. In this way, it’s similar to Python’s current approach of encouraging immediate decoding of bytes to text.

Note that URL instances are mutable objects. If an immutable representation of the URL is desired, the string from [`to_text()`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.to_text "boltons.urlutils.URL.to_text") may be used. For an immutable, but almost-as-featureful, URL object, check out the [hyperlink package](https://github.com/mahmoud/hyperlink).

scheme[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.scheme "Link to this definition")
The scheme is an ASCII string, normally lowercase, which specifies the semantics for the rest of the URL, as well as network protocol in many cases. For example, “http” in “[http://hatnote.com](http://hatnote.com/)”.

username[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.username "Link to this definition")
The username is a string used by some schemes for authentication. For example, “public” in “[ftp://public@example.com](ftp://public@example.com/)”.

password[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.password "Link to this definition")
The password is a string also used for authentication. Technically deprecated by [RFC 3986 Section 7.5](https://tools.ietf.org/html/rfc3986#section-7.5), they’re still used in cases when the URL is private or the password is public. For example “password” in “db://private:password@127.0.0.1”.

host[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.host "Link to this definition")
The host is a string used to resolve the network location of the resource, either empty, a domain, or IP address (v4 or v6). “example.com”, “127.0.0.1”, and “::1” are all good examples of host strings.

Per spec, fully-encoded output from [`to_text()`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.to_text "boltons.urlutils.URL.to_text") is [IDNA encoded](https://en.wikipedia.org/wiki/Internationalized_domain_name#Example_of_IDNA_encoding) for compatibility with DNS.

port[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.port "Link to this definition")
The port is an integer used, along with [`host`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.host "boltons.urlutils.URL.host"), in connecting to network locations. `8080` is the port in “[http://localhost:8080/index.html](http://localhost:8080/index.html)”.

Note

As is the case for 80 for HTTP and 22 for SSH, many schemes have default ports, and [Section 3.2.3 of RFC 3986](https://tools.ietf.org/html/rfc3986#section-3.2.3) states that when a URL’s port is the same as its scheme’s default port, the port should not be emitted:

>>> URL(u'https://github.com:443/mahmoud/boltons').to_text()
u'https://github.com/mahmoud/boltons'

Custom schemes can register their port with [`register_scheme()`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.register_scheme "boltons.urlutils.register_scheme"). See [`URL.default_port`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.default_port "boltons.urlutils.URL.default_port") for more info.

path[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.path "Link to this definition")
The string starting with the first leading slash after the authority part of the URL, ending with the first question mark. Often percent-quoted for network use. “/a/b/c” is the path of “[http://example.com/a/b/c?d=e](http://example.com/a/b/c?d=e)”.

path_parts[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.path_parts "Link to this definition")
The [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)") form of [`path`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.path "boltons.urlutils.URL.path"), split on slashes. Empty slash segments are preserved, including that of the leading slash:

>>> url = URL(u'http://example.com/a/b/c')
>>> url.path_parts
(u'', u'a', u'b', u'c')

query_params[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/urlutils.html#URL.query_params)[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.query_params "Link to this definition")
An instance of [`QueryParamDict`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.QueryParamDict "boltons.urlutils.QueryParamDict"), an [`OrderedMultiDict`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict "boltons.dictutils.OrderedMultiDict") subtype, mapping textual keys and values which follow the first question mark after the [`path`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.path "boltons.urlutils.URL.path"). Also available as the handy alias `qp`:

>>> url = URL('http://boltons.readthedocs.io/en/latest/?utm_source=docs&sphinx=ok')
>>> url.qp.keys()
[u'utm_source', u'sphinx']

Also percent-encoded for network use cases.

fragment[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.fragment "Link to this definition")
The string following the first ‘#’ after the [`query_params`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.query_params "boltons.urlutils.URL.query_params") until the end of the URL. It has no inherent internal structure, and is percent-quoted.

_classmethod_ from_parts(_scheme=None_, _host=None_, _path\_parts=()_, _query\_params=()_, _fragment=''_, _port=None_, _username=None_, _password=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/urlutils.html#URL.from_parts)[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.from_parts "Link to this definition")
Build a new URL from parts. Note that the respective arguments are not in the order they would appear in a URL:

Parameters:
*   **scheme** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The scheme of a URL, e.g., ‘http’

*   **host** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The host string, e.g., ‘hatnote.com’

*   **path_parts** ([_tuple_](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")) – The individual text segments of the path, e.g., (‘post’, ‘123’)

*   **query_params** ([_dict_](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – An OMD, dict, or list of (key, value) pairs representing the keys and values of the URL’s query parameters.

*   **fragment** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The fragment of the URL, e.g., ‘anchor1’

*   **port** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The integer port of URL, automatic defaults are available for registered schemes.

*   **username** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The username for the userinfo part of the URL.

*   **password** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The password for the userinfo part of the URL.

Note that this method does relatively little validation. [`URL.to_text()`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.to_text "boltons.urlutils.URL.to_text") should be used to check if any errors are produced while composing the final textual URL.

to_text(_full\_quote=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/urlutils.html#URL.to_text)[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.to_text "Link to this definition")
Render a string representing the current state of the URL object.

>>> url = URL('http://listen.hatnote.com')
>>> url.fragment = 'en'
>>> print(url.to_text())
http://listen.hatnote.com#en

By setting the _full\_quote_ flag, the URL can either be fully quoted or minimally quoted. The most common characteristic of an encoded-URL is the presence of percent-encoded text (e.g., %60). Unquoted URLs are more readable and suitable for display, whereas fully-quoted URLs are more conservative and generally necessary for sending over the network.

default_port[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.default_port "Link to this definition")
Return the default port for the currently-set scheme. Returns `None` if the scheme is unrecognized. See [`register_scheme()`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.register_scheme "boltons.urlutils.register_scheme") above. If [`port`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.port "boltons.urlutils.URL.port") matches this value, no port is emitted in the output of [`to_text()`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.to_text "boltons.urlutils.URL.to_text").

Applies the same ‘+’ heuristic detailed in [`URL.uses_netloc()`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.uses_netloc "boltons.urlutils.URL.uses_netloc").

uses_netloc[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.uses_netloc "Link to this definition")
Whether or not a URL uses `:` or `://` to separate the scheme from the rest of the URL depends on the scheme’s own standard definition. There is no way to infer this behavior from other parts of the URL. A scheme either supports network locations or it does not.

The URL type’s approach to this is to check for explicitly registered schemes, with common schemes like HTTP preregistered. This is the same approach taken by `urlparse`.

URL adds two additional heuristics if the scheme as a whole is not registered. First, it attempts to check the subpart of the scheme after the last `+` character. This adds intuitive behavior for schemes like `git+ssh`. Second, if a URL with an unrecognized scheme is loaded, it will maintain the separator it sees.

>>> print(URL('fakescheme://test.com').to_text())
fakescheme://test.com
>>> print(URL('mockscheme:hello:world').to_text())
mockscheme:hello:world

Used by URL schemes that have a network location, [`get_authority()`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.get_authority "boltons.urlutils.URL.get_authority") combines [`username`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.username "boltons.urlutils.URL.username"), [`password`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.password "boltons.urlutils.URL.password"), [`host`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.host "boltons.urlutils.URL.host"), and [`port`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.port "boltons.urlutils.URL.port") into one string, the _authority_, that is used for connecting to a network-accessible resource.

Used internally by [`to_text()`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.to_text "boltons.urlutils.URL.to_text") and can be useful for labeling connections.

>>> url = URL('ftp://user@ftp.debian.org:2121/debian/README')
>>> print(url.get_authority())
ftp.debian.org:2121
>>> print(url.get_authority(with_userinfo=True))
user@ftp.debian.org:2121

Parameters:
*   **full_quote** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Whether or not to apply IDNA encoding. Defaults to `False`.

*   **with_userinfo** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Whether or not to include username and password, technically part of the authority. Defaults to `False`.

normalize(_with\_case=True_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/urlutils.html#URL.normalize)[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.normalize "Link to this definition")
Resolve any “.” and “..” references in the path, as well as normalize scheme and host casing. To turn off case normalization, pass `with_case=False`.

More information can be found in [Section 6.2.2 of RFC 3986](https://tools.ietf.org/html/rfc3986#section-6.2.2).

navigate(_dest_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/urlutils.html#URL.navigate)[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.navigate "Link to this definition")
Factory method that returns a _new_ [`URL`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL "boltons.urlutils.URL") based on a given destination, _dest_. Useful for navigating those relative links with ease.

The newly created [`URL`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL "boltons.urlutils.URL") is normalized before being returned.

>>> url = URL('http://boltons.readthedocs.io')
>>> url.navigate('en/latest/')
URL(u'http://boltons.readthedocs.io/en/latest/')

Parameters:
**dest** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – A string or URL object representing the destination

More information can be found in [Section 5 of RFC 3986](https://tools.ietf.org/html/rfc3986#section-5).

Low-level functions[](https://boltons.readthedocs.io/en/latest/urlutils.html#low-level-functions "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------

A slew of functions used internally by [`URL`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL "boltons.urlutils.URL").

boltons.urlutils.parse_url(_url\_text_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/urlutils.html#parse_url)[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.parse_url "Link to this definition")
Used to parse the text for a single URL into a dictionary, used internally by the [`URL`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL "boltons.urlutils.URL") type.

Note that “URL” has a very narrow, standards-based definition. While [`parse_url()`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.parse_url "boltons.urlutils.parse_url") may raise `URLParseError` under a very limited number of conditions, such as non-integer port, a surprising number of strings are technically valid URLs. For instance, the text `"url"` is a valid URL, because it is a relative path.

In short, do not expect this function to validate form inputs or other more colloquial usages of URLs.

>>> res = parse_url('http://127.0.0.1:3000/?a=1')
>>> sorted(res.keys())  # res is a basic dictionary
['_netloc_sep', 'authority', 'family', 'fragment', 'host', 'password', 'path', 'port', 'query', 'scheme', 'username']

boltons.urlutils.parse_host(_host_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/urlutils.html#parse_host)[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.parse_host "Link to this definition")
Low-level function used to parse the host portion of a URL.

Returns a tuple of (family, host) where _family_ is a [`socket`](https://docs.python.org/3/library/socket.html#module-socket "(in Python v3.14)") module constant or `None`, and host is a string.

>>> parse_host('googlewebsite.com') == (None, 'googlewebsite.com')
True
>>> parse_host('[::1]') == (socket.AF_INET6, '::1')
True
>>> parse_host('192.168.1.1') == (socket.AF_INET, '192.168.1.1')
True

Odd doctest formatting above due to py3’s switch from int to enums for [`socket`](https://docs.python.org/3/library/socket.html#module-socket "(in Python v3.14)") constants.

boltons.urlutils.parse_qsl(_qs_, _keep\_blank\_values=True_, _encoding='utf8'_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/urlutils.html#parse_qsl)[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.parse_qsl "Link to this definition")
Converts a query string into a list of (key, value) pairs.

boltons.urlutils.resolve_path_parts(_path\_parts_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/urlutils.html#resolve_path_parts)[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.resolve_path_parts "Link to this definition")
Normalize the URL path by resolving segments of ‘.’ and ‘..’, resulting in a dot-free path. See RFC 3986 section 5.2.4, Remove Dot Segments.

_class_ boltons.urlutils.QueryParamDict(_*a_, _**kw_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/urlutils.html#QueryParamDict)[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.QueryParamDict "Link to this definition")
A subclass of `OrderedMultiDict` specialized for representing query string values. Everything is fully unquoted on load and all parsed keys and values are strings by default.

As the name suggests, multiple values are supported and insertion order is preserved.

>>> qp = QueryParamDict.from_text(u'key=val1&key=val2&utm_source=rtd')
>>> qp.getlist('key')
[u'val1', u'val2']
>>> qp['key']
u'val2'
>>> qp.add('key', 'val3')
>>> qp.to_text()
'key=val1&key=val2&utm_source=rtd&key=val3'

See `OrderedMultiDict` for more API features.

_classmethod_ from_text(_query\_string_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/urlutils.html#QueryParamDict.from_text)[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.QueryParamDict.from_text "Link to this definition")
Parse _query\_string_ and return a new [`QueryParamDict`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.QueryParamDict "boltons.urlutils.QueryParamDict").

to_text(_full\_quote=False_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/urlutils.html#QueryParamDict.to_text)[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.QueryParamDict.to_text "Link to this definition")
Render and return a query string.

Parameters:
**full_quote** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Whether or not to percent-quote special characters or leave them decoded for readability.

### Quoting[](https://boltons.readthedocs.io/en/latest/urlutils.html#quoting "Link to this heading")

URLs have many parts, and almost as many individual “quoting” (encoding) strategies.

boltons.urlutils.quote_userinfo_part(_text_, _full\_quote=True_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/urlutils.html#quote_userinfo_part)[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.quote_userinfo_part "Link to this definition")
Quote special characters in either the username or password section of the URL. Note that userinfo in URLs is considered deprecated in many circles (especially browsers), and support for percent-encoded userinfo can be spotty.

boltons.urlutils.quote_path_part(_text_, _full\_quote=True_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/urlutils.html#quote_path_part)[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.quote_path_part "Link to this definition")
Percent-encode a single segment of a URL path.

boltons.urlutils.quote_query_part(_text_, _full\_quote=True_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/urlutils.html#quote_query_part)[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.quote_query_part "Link to this definition")
Percent-encode a single query string key or value.

boltons.urlutils.quote_fragment_part(_text_, _full\_quote=True_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/urlutils.html#quote_fragment_part)[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.quote_fragment_part "Link to this definition")
Quote the fragment part of the URL. Fragments don’t have subdelimiters, so the whole URL fragment can be passed.

There is however, only one unquoting strategy:

boltons.urlutils.unquote(_string_, _encoding='utf-8'_, _errors='replace'_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/urlutils.html#unquote)[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.unquote "Link to this definition")
Percent-decode a string, by replacing %xx escapes with their single-character equivalent. The optional _encoding_ and _errors_ parameters specify how to decode percent-encoded sequences into Unicode characters, as accepted by the [`bytes.decode()`](https://docs.python.org/3/library/stdtypes.html#bytes.decode "(in Python v3.14)") method. By default, percent-encoded sequences are decoded with UTF-8, and invalid sequences are replaced by a placeholder character.

>>> unquote(u'abc%20def')
u'abc def'

Useful constants[](https://boltons.readthedocs.io/en/latest/urlutils.html#useful-constants "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

boltons.urlutils.SCHEME_PORT_MAP[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.boltons.urlutils.SCHEME_PORT_MAP "Link to this definition")
A mapping of URL schemes to their protocols’ default ports. Painstakingly assembled from the [IANA scheme registry](https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml), [port registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml), and independent research.

Keys are lowercase strings, values are integers or None, with None indicating that the scheme does not have a default port (or may not support ports at all):

>>> boltons.urlutils.SCHEME_PORT_MAP['http']
80
>>> boltons.urlutils.SCHEME_PORT_MAP['file']
None

See [`URL.port`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.URL.port "boltons.urlutils.URL.port") for more info on how it is used. See [`NO_NETLOC_SCHEMES`](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.boltons.urlutils.NO_NETLOC_SCHEMES "boltons.urlutils.boltons.urlutils.NO_NETLOC_SCHEMES") for more scheme info.

Also [available in JSON](https://gist.github.com/mahmoud/2fe281a8daaff26cfe9c15d2c5bf5c8b).

boltons.urlutils.NO_NETLOC_SCHEMES[](https://boltons.readthedocs.io/en/latest/urlutils.html#boltons.urlutils.boltons.urlutils.NO_NETLOC_SCHEMES "Link to this definition")
This is a [`set`](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.14)") of schemes explicitly do not support network resolution, such as “mailto” and “urn”.
