# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.url.html

Title: kombu.utils.url — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.url.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.utils.url.html).

URL Utilities - `kombu.utils.url`[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.url.html#url-utilities-kombu-utils-url "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

URL Utilities.

kombu.utils.url.as_url(_scheme:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_, _host:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")=None_, _port:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")=None_, _user:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")=None_, _password:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")=None_, _path:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")=None_, _query:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")|[None](https://docs.python.org/dev/library/constants.html#None "(in Python v3.15)")=None_, _sanitize:[bool](https://docs.python.org/dev/library/functions.html#bool "(in Python v3.15)")=False_, _mask:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")='**'_)→[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/url.html#as_url)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.url.html#kombu.utils.url.as_url "Link to this definition")
Generate URL from component parts.

kombu.utils.url.maybe_sanitize_url(_url:Any_, _mask:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")='**'_)→Any[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/url.html#maybe_sanitize_url)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.url.html#kombu.utils.url.maybe_sanitize_url "Link to this definition")
Sanitize url, or do nothing if url undefined.

kombu.utils.url.parse_ssl_cert_reqs(_query\_value:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_)→Any[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/url.html#parse_ssl_cert_reqs)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.url.html#kombu.utils.url.parse_ssl_cert_reqs "Link to this definition")
Given the query parameter for ssl_cert_reqs, return the SSL constant or None.

kombu.utils.url.parse_url(_url:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_)→Dict[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/url.html#parse_url)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.url.html#kombu.utils.url.parse_url "Link to this definition")
Parse URL into mapping of components.

kombu.utils.url.sanitize_url(_url:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_, _mask:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")='**'_)→[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/url.html#sanitize_url)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.url.html#kombu.utils.url.sanitize_url "Link to this definition")
Return copy of URL with password removed.

kombu.utils.url.url_to_parts(_url:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_)→[urlparts](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.url.html#kombu.utils.url.urlparts "kombu.utils.url.urlparts")[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/url.html#url_to_parts)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.url.html#kombu.utils.url.url_to_parts "Link to this definition")
Parse URL into [`urlparts`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.url.html#kombu.utils.url.urlparts "kombu.utils.url.urlparts") tuple of components.

_class_ kombu.utils.url.urlparts(_scheme:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_, _hostname:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_, _port:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_, _username:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_, _password:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_, _path:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_, _query:Mapping_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/url.html#urlparts)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.url.html#kombu.utils.url.urlparts "Link to this definition")
Named tuple representing parts of the URL.

hostname _:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.url.html#kombu.utils.url.urlparts.hostname "Link to this definition")
Alias for field number 1

password _:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.url.html#kombu.utils.url.urlparts.password "Link to this definition")
Alias for field number 4

path _:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.url.html#kombu.utils.url.urlparts.path "Link to this definition")
Alias for field number 5

port _:[int](https://docs.python.org/dev/library/functions.html#int "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.url.html#kombu.utils.url.urlparts.port "Link to this definition")
Alias for field number 2

query _:[Mapping](https://docs.python.org/dev/library/collections.abc.html#collections.abc.Mapping "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.url.html#kombu.utils.url.urlparts.query "Link to this definition")
Alias for field number 6

scheme _:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.url.html#kombu.utils.url.urlparts.scheme "Link to this definition")
Alias for field number 0

username _:[str](https://docs.python.org/dev/library/stdtypes.html#str "(in Python v3.15)")_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.url.html#kombu.utils.url.urlparts.username "Link to this definition")
Alias for field number 3
