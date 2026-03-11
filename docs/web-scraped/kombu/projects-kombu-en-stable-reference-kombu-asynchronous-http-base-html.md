# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html

Title: Async HTTP Client Interface - kombu.asynchronous.http.base — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.asynchronous.http.base.html).

Base async HTTP client implementation.

Represents a mapping of HTTP headers.

Set when all of the headers have been read.

_class_ kombu.asynchronous.http.base.Request(_url_, _method='GET'_, _on\_ready=None_, _on\_timeout=None_, _on\_stream=None_, _on\_prepare=None_, _on\_header=None_, _headers=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/http/base.html#Request)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request "Link to this definition")
A HTTP Request.

Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#arguments "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

> url (str): The URL to request. method (str): The HTTP method to use (defaults to `GET`).

Keyword Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#keyword-arguments "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

> headers (Dict, ~kombu.asynchronous.http.Headers): Optional headers for
> this request
> 
> 
> body (str): Optional body for this request. connect_timeout (float): Connection timeout in float seconds
> 
> 
> > Default is 30.0.
> 
> timeout (float): Time in float seconds before the request times out
> Default is 30.0.
> 
> follow_redirects (bool): Specify if the client should follow redirects
> Enabled by default.
> 
> 
> max_redirects (int): Maximum number of redirects (default 6). use_gzip (bool): Allow the server to use gzip compression.
> 
> 
> > Enabled by default.
> 
> validate_cert (bool): Set to true if the server certificate should be
> verified when performing `https://` requests. Enabled by default.
> 
> 
> auth_username (str): Username for HTTP authentication. auth_password (str): Password for HTTP authentication. auth_mode (str): Type of HTTP authentication (`basic` or `digest`). user_agent (str): Custom user agent for this request. network_interface (str): Network interface to use for this request. on_ready (Callable): Callback to be called when the response has been
> 
> 
> > received. Must accept single `response` argument.
> 
> on_stream (Callable): Optional callback to be called every time body
> content has been read from the socket. If specified then the response body and buffer attributes will not be available.
> 
> on_timeout (callable): Optional callback to be called if the request
> times out.
> 
> on_header (Callable): Optional callback to be called for every header
> line received from the server. The signature is `(headers, line)` and note that if you want `response.headers` to be populated then your callback needs to also call `client.on_header(headers, line)`.
> 
> on_prepare (Callable): Optional callback that is implementation
> specific (e.g. curl client will pass the `curl` instance to this callback).
> 
> proxy_host (str): Optional proxy host. Note that a `proxy_port` must
> also be provided or a [`ValueError`](https://docs.python.org/dev/library/exceptions.html#ValueError "(in Python v3.15)") will be raised.
> 
> proxy_username (str): Optional username to use when logging in
> to the proxy.
> 
> proxy_password (str): Optional password to use when authenticating
> with the proxy server.
> 
> 
> ca_certs (str): Custom CA certificates file to use. client_key (str): Optional filename for client SSL key. client_cert (str): Optional filename for client SSL certificate.

auth_mode _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.auth_mode "Link to this definition")auth_password _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.auth_password "Link to this definition")auth_username _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.auth_username "Link to this definition")body _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.body "Link to this definition")ca_certs _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.ca_certs "Link to this definition")client_cert _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.client_cert "Link to this definition")client_key _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.client_key "Link to this definition")connect_timeout _=30.0_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.connect_timeout "Link to this definition")follow_redirects _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.follow_redirects "Link to this definition")max_redirects _=6_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.max_redirects "Link to this definition")method[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.method "Link to this definition")network_interface _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.network_interface "Link to this definition")on_prepare[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.on_prepare "Link to this definition")on_ready[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.on_ready "Link to this definition")on_stream[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.on_stream "Link to this definition")on_timeout[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.on_timeout "Link to this definition")proxy_host _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.proxy_host "Link to this definition")proxy_password _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.proxy_password "Link to this definition")proxy_port _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.proxy_port "Link to this definition")proxy_username _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.proxy_username "Link to this definition")request_timeout _=30.0_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.request_timeout "Link to this definition")then(_callback_, _errback=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/http/base.html#Request.then)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.then "Link to this definition")url[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.url "Link to this definition")use_gzip _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.use_gzip "Link to this definition")user_agent _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.user_agent "Link to this definition")validate_cert _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Request.validate_cert "Link to this definition")_class_ kombu.asynchronous.http.base.Response(_request_, _code_, _headers=None_, _buffer=None_, _effective\_url=None_, _error=None_, _status=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/http/base.html#Response)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Response "Link to this definition")
HTTP Response.

Parameters:
*   **(****~kombu.asynchronous.http.Request****)** (_request_)

*   **(****int****)** (_code_)

*   **(****~kombu.asynchronous.http.Headers****)** (_headers_)

*   **(****bytes****)** (_buffer_)

*   **(****str****)** (_status_)

*   **(****str****)**

request(_~kombu.asynchronous.http.Request_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Response.request "Link to this definition")
get this response.

Type:
object used to

code(_int_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Response.code "Link to this definition")Type:
HTTP response code (e.g. 200, 404, or 500).

for this response.

Type:
HTTP headers

buffer(_bytes_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Response.buffer "Link to this definition")Type:
Socket read buffer.

effective_url(_str_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Response.effective_url "Link to this definition")
following redirects.

Type:
The destination url for this request after

error(_Exception_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Response.error "Link to this definition")
a HTTP error code.

Type:
Error instance if the request resulted in

status(_str_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Response.status "Link to this definition")
e.g. `OK`, Not found, or ‘Internal Server Error’.

Type:
Human equivalent of [`code`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#id1 "kombu.asynchronous.http.base.Response.code"),

_property_ body[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Response.body "Link to this definition")
The full contents of the response body.

Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#note "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------

> Accessing this property will evaluate the buffer and subsequent accesses will be cached.

buffer[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#id0 "Link to this definition")code[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#id1 "Link to this definition")_property_ content[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Response.content "Link to this definition")effective_url[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#id2 "Link to this definition")error[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#id3 "Link to this definition")headers[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#id4 "Link to this definition")raise_for_error()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/http/base.html#Response.raise_for_error)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Response.raise_for_error "Link to this definition")
Raise if the request resulted in an HTTP error code.

Raises:
**HttpError** –

request[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#id5 "Link to this definition")status[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#id6 "Link to this definition")_property_ status_code[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.http.base.html#kombu.asynchronous.http.base.Response.status_code "Link to this definition")
