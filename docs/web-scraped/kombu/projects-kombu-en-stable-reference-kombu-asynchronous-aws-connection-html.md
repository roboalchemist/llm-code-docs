# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html

Title: Amazon AWS Connection - kombu.asynchronous.aws.connection — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.asynchronous.aws.connection.html).

Amazon AWS Connection.

_class_ kombu.asynchronous.aws.connection.AsyncConnection(_sqs\_connection_, _http\_client=None_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/aws/connection.html#AsyncConnection)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncConnection "Link to this definition")
Async AWS Connection.

get_http_connection()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/aws/connection.html#AsyncConnection.get_http_connection)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncConnection.get_http_connection "Link to this definition")_class_ kombu.asynchronous.aws.connection.AsyncHTTPSConnection(_strict=None_, _timeout=20.0_, _http\_client=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/aws/connection.html#AsyncHTTPSConnection)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection "Link to this definition")
Async HTTP Connection.

_class_ Request(_url_, _method='GET'_, _on\_ready=None_, _on\_timeout=None_, _on\_stream=None_, _on\_prepare=None_, _on\_header=None_, _headers=None_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request "Link to this definition")
A HTTP Request.

Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#arguments "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

> url (str): The URL to request. method (str): The HTTP method to use (defaults to `GET`).

Keyword Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#keyword-arguments "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

auth_mode _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.auth_mode "Link to this definition")auth_password _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.auth_password "Link to this definition")auth_username _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.auth_username "Link to this definition")body _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.body "Link to this definition")ca_certs _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.ca_certs "Link to this definition")client_cert _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.client_cert "Link to this definition")client_key _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.client_key "Link to this definition")connect_timeout _=30.0_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.connect_timeout "Link to this definition")follow_redirects _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.follow_redirects "Link to this definition")max_redirects _=6_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.max_redirects "Link to this definition")method[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.method "Link to this definition")network_interface _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.network_interface "Link to this definition")on_prepare[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.on_prepare "Link to this definition")on_ready[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.on_ready "Link to this definition")on_stream[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.on_stream "Link to this definition")on_timeout[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.on_timeout "Link to this definition")proxy_host _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.proxy_host "Link to this definition")proxy_password _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.proxy_password "Link to this definition")proxy_port _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.proxy_port "Link to this definition")proxy_username _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.proxy_username "Link to this definition")request_timeout _=30.0_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.request_timeout "Link to this definition")then(_callback_, _errback=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.then "Link to this definition")url[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.url "Link to this definition")use_gzip _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.use_gzip "Link to this definition")user_agent _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.user_agent "Link to this definition")validate_cert _=True_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Request.validate_cert "Link to this definition")Response[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.Response "Link to this definition")
alias of `AsyncHTTPResponse`

body _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.body "Link to this definition")close()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/aws/connection.html#AsyncHTTPSConnection.close)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.close "Link to this definition")connect()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/aws/connection.html#AsyncHTTPSConnection.connect)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.connect "Link to this definition")default_ports _={'http':80,'https':443}_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.default_ports "Link to this definition")getrequest()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/aws/connection.html#AsyncHTTPSConnection.getrequest)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.getrequest "Link to this definition")getresponse(_callback=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/aws/connection.html#AsyncHTTPSConnection.getresponse)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.getresponse "Link to this definition")method _='GET'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.method "Link to this definition")path _='/'_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.path "Link to this definition")putrequest(_method_, _path_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/aws/connection.html#AsyncHTTPSConnection.putrequest)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.putrequest "Link to this definition")request(_method_, _path_, _body=None_, _headers=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/aws/connection.html#AsyncHTTPSConnection.request)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.request "Link to this definition")send(_data_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/aws/connection.html#AsyncHTTPSConnection.send)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.send "Link to this definition")set_debuglevel(_level_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/aws/connection.html#AsyncHTTPSConnection.set_debuglevel)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.aws.connection.html#kombu.asynchronous.aws.connection.AsyncHTTPSConnection.set_debuglevel "Link to this definition")
