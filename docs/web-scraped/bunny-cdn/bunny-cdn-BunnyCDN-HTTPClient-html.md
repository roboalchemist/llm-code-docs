# Source: https://hexdocs.pm/bunny_cdn/BunnyCDN.HTTPClient.html

Title: BunnyCDN.HTTPClient — bunny_cdn v0.1.0

URL Source: https://hexdocs.pm/bunny_cdn/BunnyCDN.HTTPClient.html

Published Time: Fri, 10 Jan 2025 19:07:00 GMT

Markdown Content:
BunnyCDN.HTTPClient — bunny_cdn v0.1.0
===============

Search

 

[bunny_cdn](https://hexdocs.pm/bunny_cdn/readme.html)

*   [Pages](https://hexdocs.pm/bunny_cdn/BunnyCDN.HTTPClient.html#full-list)
*   [Modules](https://hexdocs.pm/bunny_cdn/BunnyCDN.HTTPClient.html#full-list)

*   [BunnyCDN](https://hexdocs.pm/bunny_cdn/BunnyCDN.html)
    *   [Summary](https://hexdocs.pm/bunny_cdn/BunnyCDN.html#summary)
    *   [Functions](https://hexdocs.pm/bunny_cdn/BunnyCDN.html#functions)
        *   [delete/2](https://hexdocs.pm/bunny_cdn/BunnyCDN.html#delete/2 "delete(client, uri)")
        *   [get/2](https://hexdocs.pm/bunny_cdn/BunnyCDN.html#get/2 "get(client, uri)")
        *   [put/3](https://hexdocs.pm/bunny_cdn/BunnyCDN.html#put/3 "put(client, file, uri)")
        *   [put/4](https://hexdocs.pm/bunny_cdn/BunnyCDN.html#put/4 "put(client, file, path, name)")

*   [BunnyCDN.Client](https://hexdocs.pm/bunny_cdn/BunnyCDN.Client.html)
    *   [Summary](https://hexdocs.pm/bunny_cdn/BunnyCDN.Client.html#summary)
    *   [Types](https://hexdocs.pm/bunny_cdn/BunnyCDN.Client.html#types)
        *   [t/0](https://hexdocs.pm/bunny_cdn/BunnyCDN.Client.html#t:t/0 "t()")

    *   [Functions](https://hexdocs.pm/bunny_cdn/BunnyCDN.Client.html#functions)
        *   [new/3](https://hexdocs.pm/bunny_cdn/BunnyCDN.Client.html#new/3 "new(storage_endpoint, storage_zone, storage_api_key)")
        *   [new!/0](https://hexdocs.pm/bunny_cdn/BunnyCDN.Client.html#new!/0 "new!()")
        *   [new!/1](https://hexdocs.pm/bunny_cdn/BunnyCDN.Client.html#new!/1 "new!(storage_endpoint)")
        *   [put_http_client/2](https://hexdocs.pm/bunny_cdn/BunnyCDN.Client.html#put_http_client/2 "put_http_client(client, http_client)")
        *   [request/6](https://hexdocs.pm/bunny_cdn/BunnyCDN.Client.html#request/6 "request(client, method, url, body, headers, opts \\ [])")

*   [BunnyCDN.HTTPClient](https://hexdocs.pm/bunny_cdn/BunnyCDN.HTTPClient.html#content)
    *   [Summary](https://hexdocs.pm/bunny_cdn/BunnyCDN.HTTPClient.html#summary)
    *   [Callbacks](https://hexdocs.pm/bunny_cdn/BunnyCDN.HTTPClient.html#callbacks)
        *   [request/5](https://hexdocs.pm/bunny_cdn/BunnyCDN.HTTPClient.html#c:request/5 "request(method, url, body, headers, options)")

*   [BunnyCDN.HTTPClient.Req](https://hexdocs.pm/bunny_cdn/BunnyCDN.HTTPClient.Req.html)
*   [BunnyCDN.Request](https://hexdocs.pm/bunny_cdn/BunnyCDN.Request.html)
    *   [Summary](https://hexdocs.pm/bunny_cdn/BunnyCDN.Request.html#summary)
    *   [Functions](https://hexdocs.pm/bunny_cdn/BunnyCDN.Request.html#functions)
        *   [request/6](https://hexdocs.pm/bunny_cdn/BunnyCDN.Request.html#request/6 "request(client, method, uri, body \\ nil, headers \\ [], options \\ [])")

Settings[View Source](https://github.com/quarterpi/bunny_cdn/blob/v0.1.0//Users/admin/Documents/Elixir/Packages/bunny_cli/bunny_cdn/lib/http_client.ex#L1 "View Source")BunnyCDN.HTTPClient behaviour(bunny_cdn v0.1.0)
=======================================================================================================================================================================================================================

Http Client Behaviour specification.

The default http client uses Req underneath the hood. You can implement your own http client if your prefer a different http client. You'll need to set the `:http_client` configuration in [`BunnyCDN.Client`](https://hexdocs.pm/bunny_cdn/BunnyCDN.Client.html):

```
client = %BunnyCDN.Client{http_client: {MyHTTPClient, []}}
BunnyCDN.get(client, "some/file.txt")
```

[Link to this section](https://hexdocs.pm/bunny_cdn/BunnyCDN.HTTPClient.html#summary) Summary
=============================================================================================

[Callbacks](https://hexdocs.pm/bunny_cdn/BunnyCDN.HTTPClient.html#callbacks)
----------------------------------------------------------------------------

[request(method, url, body, headers, options)](https://hexdocs.pm/bunny_cdn/BunnyCDN.HTTPClient.html#c:request/5)

Executes an HTTP request. Must return either {:ok, map} or {:error, reason}.

[Link to this section](https://hexdocs.pm/bunny_cdn/BunnyCDN.HTTPClient.html#callbacks) Callbacks
=================================================================================================

[Link to this callback](https://hexdocs.pm/bunny_cdn/BunnyCDN.HTTPClient.html#c:request/5 "Link to this callback")
request(method, url, body, headers, options)
============================================

[View Source](https://github.com/quarterpi/bunny_cdn/blob/v0.1.0//Users/admin/Documents/Elixir/Packages/bunny_cli/bunny_cdn/lib/http_client.ex#L24 "View Source")

@callback request(
  method ::
    :get | :post | :head | :patch | :delete | :options | :put | [String.t](https://hexdocs.pm/elixir/String.html#t:t/0)(),
  url :: [String.t](https://hexdocs.pm/elixir/String.html#t:t/0)() | [URI.t](https://hexdocs.pm/elixir/URI.html#t:t/0)(),
  body :: [iodata](https://hexdocs.pm/elixir/typespecs.html#built-in-types)() | nil,
  headers ::
    [{header_name :: [String.t](https://hexdocs.pm/elixir/String.html#t:t/0)(), header_value :: [String.t](https://hexdocs.pm/elixir/String.html#t:t/0)()}] | [] | nil,
  options :: [keyword](https://hexdocs.pm/elixir/typespecs.html#built-in-types)()
) :: {:ok, [binary](https://hexdocs.pm/elixir/typespecs.html#built-in-types)(), [term](https://hexdocs.pm/elixir/typespecs.html#built-in-types)()} | {:error, [term](https://hexdocs.pm/elixir/typespecs.html#built-in-types)()}

Executes an HTTP request. Must return either {:ok, map} or {:error, reason}.

*   `body` must be raw file data without any encoding. See [BunnyCDN API reference][https://docs.bunny.net/reference/put_-storagezonename-path-filename](https://docs.bunny.net/reference/put_-storagezonename-path-filename)
*   `headers` already contains required headers such as the Authorization headers.

[Hex Package](https://hex.pm/packages/bunny_cdn/0.1.0)[Hex Preview](https://preview.hex.pm/preview/bunny_cdn/0.1.0) ([current file](https://preview.hex.pm/preview/bunny_cdn/0.1.0/show//Users/admin/Documents/Elixir/Packages/bunny_cli/bunny_cdn/lib/http_client.ex))  Search HexDocs [Download ePub version](https://hexdocs.pm/bunny_cdn/bunny_cdn.epub "ePub version")

Built using [ExDoc](https://github.com/elixir-lang/ex_doc "ExDoc") (v0.29.4) for the [Elixir programming language](https://elixir-lang.org/ "Elixir")

×
