# Source: https://hexdocs.pm/req/Req.Steps.html

Title: Req.Steps — req v0.5.17

URL Source: https://hexdocs.pm/req/Req.Steps.html

Markdown Content:
The collection of built-in steps.

Req is composed of:

*   [`Req`](https://hexdocs.pm/req/Req.html) - the high-level API

*   [`Req.Request`](https://hexdocs.pm/req/Req.Request.html) - the low-level API and the request struct

*   [`Req.Steps`](https://hexdocs.pm/req/Req.Steps.html) - the collection of built-in steps (you're here!)

*   [`Req.Test`](https://hexdocs.pm/req/Req.Test.html) - the testing conveniences

[](https://hexdocs.pm/req/Req.Steps.html#summary)Summary
--------------------------------------------------------

[Request Steps](https://hexdocs.pm/req/Req.Steps.html#request-steps)
--------------------------------------------------------------------

Sets request authentication.

Performs HTTP caching using `if-modified-since` header.

Sets expected response body checksum.

Compresses the request body.

Asks the server to return compressed response.

Encodes the request body.

Signs request with AWS Signature Version 4.

Sets base URL for all requests.

Adds params to request query string.

Uses a templated request path.

Sets the "Range" request header.

Sets the user-agent header.

Runs the request using [`Finch`](https://hexdocs.pm/req/Req.Steps.html).

Runs the request against a plug instead of over the network.

[Response Steps](https://hexdocs.pm/req/Req.Steps.html#response-steps)
----------------------------------------------------------------------

Decodes response body based on the detected format.

Decompresses the response body based on the `content-encoding` header.

Handles HTTP Digest authentication.

Handles HTTP 4xx/5xx error responses.

Follows redirects.

Verifies the response body checksum.

[Error Steps](https://hexdocs.pm/req/Req.Steps.html#error-steps)
----------------------------------------------------------------

Retries a request in face of errors.

[](https://hexdocs.pm/req/Req.Steps.html#request-steps)Request Steps
--------------------------------------------------------------------

Sets request authentication.

[](https://hexdocs.pm/req/Req.Steps.html#auth/1-request-options)Request Options
-------------------------------------------------------------------------------

*   `:auth` - sets the `authorization` header:

    *   `string` - sets to this value;

    *   `{:basic, userinfo}` - uses Basic HTTP authentication;

    *   `{:digest, userinfo}` - uses Digest HTTP authentication;

    *   `{:bearer, token}` - uses Bearer HTTP authentication;

    *   `:netrc` - load credentials from `.netrc` at path specified in `NETRC` environment variable. If `NETRC` is not set, load `.netrc` in user's home directory;

    *   `{:netrc, path}` - load credentials from `path`

    *   `fn -> {:bearer, "eyJ0eXAi..." } end` - a 0-arity function that returns one of the aforementioned types.

    *   `{mod, fun, args}` - an MFArgs tuple that returns one of the aforementioned types.

[](https://hexdocs.pm/req/Req.Steps.html#auth/1-examples)Examples
-----------------------------------------------------------------

```
iex> Req.get!("https://httpbin.org/basic-auth/foo/bar", auth: {:basic, "foo:foo"}).status
401
iex> Req.get!("https://httpbin.org/basic-auth/foo/bar", auth: {:basic, "foo:bar"}).status
200
iex> Req.get!("https://httpbin.org/basic-auth/foo/bar", auth: fn -> {:basic, "foo:bar"} end).status
200
iex> Req.get!("https://httpbin.org/basic-auth/foo/bar", auth: {Authentication, :fetch_token, []}).status
200

iex> Req.get!("https://httpbin.org/digest-auth/auth/user/pass", auth: {:digest, "user:pass"}).status
200

iex> Req.get!("https://httpbin.org/bearer", auth: {:bearer, ""}).status
401
iex> Req.get!("https://httpbin.org/bearer", auth: {:bearer, "foo"}).status
200
iex> Req.get!("https://httpbin.org/bearer", auth: fn -> {:bearer, "foo"} end).status
200

iex> System.put_env("NETRC", "./test/my_netrc")
iex> Req.get!("https://httpbin.org/basic-auth/foo/bar", auth: :netrc).status
200

iex> Req.get!("https://httpbin.org/basic-auth/foo/bar", auth: {:netrc, "./test/my_netrc"}).status
200
iex> Req.get!("https://httpbin.org/basic-auth/foo/bar", auth: fn -> {:netrc, "./test/my_netrc"} end).status
200
```

Performs HTTP caching using `if-modified-since` header.

Only successful (200 OK) responses are cached.

This step also _prepends_ a response step that loads and writes the cache. Be careful when _prepending_ other response steps, make sure the cache is loaded/written as soon as possible.

[](https://hexdocs.pm/req/Req.Steps.html#cache/1-options)Options
----------------------------------------------------------------

*   `:cache` - if `true`, performs simple caching using `if-modified-since` header. Defaults to `false`.

*   `:cache_dir` - the directory to store the cache, defaults to `<user_cache_dir>/req` (see: [`:filename.basedir/3`](https://www.erlang.org/doc/apps/stdlib/filename.html#basedir/3))

[](https://hexdocs.pm/req/Req.Steps.html#cache/1-examples)Examples
------------------------------------------------------------------

```
iex> url = "https://elixir-lang.org"
iex> response1 = Req.get!(url, cache: true)
iex> response2 = Req.get!(url, cache: true)
iex> response1 == response2
true
```

Sets expected response body checksum.

[](https://hexdocs.pm/req/Req.Steps.html#checksum/1-request-options)Request Options
-----------------------------------------------------------------------------------

*   `:checksum` - if set, this is the expected response body checksum.

Can be one of:

    *   `"md5:(...)"`
    *   `"sha1:(...)"`
    *   `"sha256:(...)"`

[](https://hexdocs.pm/req/Req.Steps.html#checksum/1-examples)Examples
---------------------------------------------------------------------

```
iex> resp = Req.get!("https://httpbin.org/json", checksum: "sha1:9274ffd9cf273d4a008750f44540c4c5d4c8227c")
iex> resp.status
200

iex> Req.get!("https://httpbin.org/json", checksum: "sha1:bad")
** (Req.ChecksumMismatchError) checksum mismatch
expected: sha1:bad
actual:   sha1:9274ffd9cf273d4a008750f44540c4c5d4c8227c
```

Compresses the request body.

[](https://hexdocs.pm/req/Req.Steps.html#compress_body/1-request-options)Request Options
----------------------------------------------------------------------------------------

*   `:compress_body` - if set to `true`, compresses the request body using gzip. Defaults to `false`.

Asks the server to return compressed response.

Supported formats:

*   `gzip`

*   `br` (if [brotli](https://hex.pm/packages/brotli) is installed)

*   `zstd` (if [ezstd](https://hex.pm/packages/ezstd) is installed)

[](https://hexdocs.pm/req/Req.Steps.html#compressed/1-request-options)Request Options
-------------------------------------------------------------------------------------

*   `:compressed` - if set to `true`, sets the `accept-encoding` header with compression algorithms that Req supports. Defaults to `true`.

When streaming response body (`into: fun | collectable`), `compressed` defaults to `false`.

[](https://hexdocs.pm/req/Req.Steps.html#compressed/1-examples)Examples
-----------------------------------------------------------------------

Req automatically decompresses response body ([`decompress_body/1`](https://hexdocs.pm/req/Req.Steps.html#decompress_body/1) step) so let's disable that by passing `raw: true`.

By default, we ask the server to send compressed response. Let's look at the headers and the raw body. Notice the body starts with `<<31, 139>>` (`<<0x1F, 0x8B>>`), the "magic bytes" for gzip:

```
iex> response = Req.get!("https://elixir-lang.org", raw: true)
iex> Req.Response.get_header(response, "content-encoding")
["gzip"]
iex> response.body |> binary_part(0, 2)
<<31, 139>>
```

Now, let's pass `compressed: false` and notice the raw body was not compressed:

```
iex> response = Req.get!("https://elixir-lang.org", raw: true, compressed: false)
iex> response.body |> binary_part(0, 15)
"<!DOCTYPE html>"
```

The Brotli and Zstandard compression algorithms are also supported if the optional packages are installed:

```
Mix.install([
  :req,
  {:brotli, "~> 0.3.0"},
  {:ezstd, "~> 1.0"}
])

response = Req.get!("https://httpbin.org/anything")
response.body["headers"]["Accept-Encoding"]
#=> "zstd, br, gzip"
```

Encodes the request body.

[](https://hexdocs.pm/req/Req.Steps.html#encode_body/1-request-options)Request Options
--------------------------------------------------------------------------------------

*   `:form` - if set, encodes the request body as `application/x-www-form-urlencoded` (using [`URI.encode_query/1`](https://hexdocs.pm/elixir/URI.html#encode_query/1)).

*   `:form_multipart` - if set, encodes the request body as `multipart/form-data`.

It accepts `name` / `value` pairs. `value` can be one of:

    *   integer (automatically encoded as string)

    *   iodata

    *   [`File.Stream`](https://hexdocs.pm/elixir/File.Stream.html)

    *   [`Enumerable`](https://hexdocs.pm/elixir/Enumerable.html)

    *   `{value, options}` tuple.

`value` can be any of the values mentioned above.

Supported options are: `:filename`, `:content_type`, and `:size`.

When `value` is an [`Enumerable`](https://hexdocs.pm/elixir/Enumerable.html), option `:size` can be set with the binary size of the `value`. The size will be used to calculate and send the `content-length` header which might be required for some servers. There is no need to pass `:size` for `integer`, `iodata`, and [`File.Stream`](https://hexdocs.pm/elixir/File.Stream.html) values as it's automatically calculated.

*   `:json` - if set, encodes the request body as JSON (using [`Jason.encode_to_iodata!/1`](https://hexdocs.pm/jason/1.4.4/Jason.html#encode_to_iodata!/1)), sets the `accept` header to `application/json`, and the `content-type` header to `application/json`.

[](https://hexdocs.pm/req/Req.Steps.html#encode_body/1-examples)Examples
------------------------------------------------------------------------

Encoding form (`application/x-www-form-urlencoded`):

```
iex> Req.post!("https://httpbin.org/anything", form: [a: 1]).body["form"]
%{"a" => "1"}
```

Encoding form (`multipart/form-data`):

```
iex> fields = [a: 1, b: {"2", filename: "b.txt"}]
iex> resp = Req.post!("https://httpbin.org/anything", form_multipart: fields)
iex> resp.body["form"]
%{"a" => "1"}
iex> resp.body["files"]
%{"b" => "2"}
```

Encoding streaming form (`multipart/form-data`):

```
iex> stream = Stream.cycle(["abc"]) |> Stream.take(3)
iex> fields = [file: {stream, filename: "b.txt"}]
iex> resp = Req.post!("https://httpbin.org/anything", form_multipart: fields)
iex> resp.body["files"]
%{"file" => "abcabcabc"}

# with explicit :size
iex> stream = Stream.cycle(["abc"]) |> Stream.take(3)
iex> fields = [file: {stream, filename: "b.txt", size: 9}]
iex> resp = Req.post!("https://httpbin.org/anything", form_multipart: fields)
iex> resp.body["files"]
%{"file" => "abcabcabc"}
```

Encoding JSON:

```
iex> Req.post!("https://httpbin.org/post", json: %{a: 2}).body["json"]
%{"a" => 2}
```

Signs request with AWS Signature Version 4.

[](https://hexdocs.pm/req/Req.Steps.html#put_aws_sigv4/1-request-options)Request Options
----------------------------------------------------------------------------------------

*   `:aws_sigv4` - if set, the AWS options to sign request:

    *   `:access_key_id` - the AWS access key id.

    *   `:secret_access_key` - the AWS secret access key.

    *   `:token` - if set, the AWS security token, for example returned from AWS STS.

    *   `:service` - the AWS service. We try to automatically detect the service (e.g. `s3.amazonaws.com` host sets service to `:s3`)

    *   `:region` - the AWS region. Defaults to `"us-east-1"`.

    *   `:datetime` - the request datetime, defaults to `DateTime.utc_now(:second)`.

Additionally, it can be an `{mod, fun, args}` tuple that returns the above options.

[](https://hexdocs.pm/req/Req.Steps.html#put_aws_sigv4/1-examples)Examples
--------------------------------------------------------------------------

```
iex> req =
...>   Req.new(
...>     base_url: "https://s3.amazonaws.com",
...>     aws_sigv4: [
...>       access_key_id: System.get_env("AWS_ACCESS_KEY_ID"),
...>       secret_access_key: System.get_env("AWS_SECRET_ACCESS_KEY")
...>     ]
...>   )
iex>
iex> %{status: 200} = Req.put!(req, url: "/bucket1/key1", body: "Hello, World!")
iex> resp = Req.get!(req, url: "/bucket1/key1").body
"Hello, World!"
```

Request body streaming also works though `content-length` header must be explicitly set:

```
iex> path = "a.txt"
iex> File.write!(path, String.duplicate("a", 100_000))
iex> size = File.stat!(path).size
iex> chunk_size = 10 * 1024
iex> stream = File.stream!(path, chunk_size)
iex> %{status: 200} = Req.put!(req, url: "/key1", headers: [content_length: size], body: stream)
iex> byte_size(Req.get!(req, "/bucket1/key1").body)
100_000
```

Sets base URL for all requests.

[](https://hexdocs.pm/req/Req.Steps.html#put_base_url/1-request-options)Request Options
---------------------------------------------------------------------------------------

*   `:base_url` - if set, the request URL is merged with this base URL.

The base url can be a string, a `%URI{}` struct, a 0-arity function, or a `{mod, fun, args}` tuple describing a function to call.

[](https://hexdocs.pm/req/Req.Steps.html#put_base_url/1-examples)Examples
-------------------------------------------------------------------------

```
iex> req = Req.new(base_url: "https://httpbin.org")
iex> Req.get!(req, url: "/status/200").status
200
iex> Req.get!(req, url: "/status/201").status
201
```

Adds params to request query string.

[](https://hexdocs.pm/req/Req.Steps.html#put_params/1-request-options)Request Options
-------------------------------------------------------------------------------------

*   `:params` - params to add to the request query string. Defaults to `[]`.

[](https://hexdocs.pm/req/Req.Steps.html#put_params/1-examples)Examples
-----------------------------------------------------------------------

```
iex> Req.get!("https://httpbin.org/anything/query", params: [x: 1, y: 2]).body["args"]
%{"x" => "1", "y" => "2"}
```

Uses a templated request path.

By default, params in the URL path are expressed as strings prefixed with `:`. For example, `:code` in `https://httpbin.org/status/:code`. If you want to use the `{code}` syntax, set `path_params_style: :curly`. Param names must start with a letter and can contain letters, digits, and underscores; this is true both for `:colon_params` as well as `{curly_params}`.

Path params are replaced in the request URL path. The path params are specified as a keyword list of parameter names and values, as in the examples below. The values of the parameters are converted to strings using the [`String.Chars`](https://hexdocs.pm/elixir/String.Chars.html) protocol ([`to_string/1`](https://hexdocs.pm/elixir/Kernel.html#to_string/1)).

[](https://hexdocs.pm/req/Req.Steps.html#put_path_params/1-request-options)Request Options
------------------------------------------------------------------------------------------

*   `:path_params` - if set, params to add to the templated path. Defaults to `nil`.

*   `:path_params_style` (_available since v0.5.1_) - how path params are expressed. Can be one of:

    *   `:colon` - (default) for Plug-style parameters, such as `:code` in `https://httpbin.org/status/:code`.

    *   `:curly` - for [OpenAPI](https://swagger.io/specification/)-style parameters, such as `{code}` in `https://httpbin.org/status/{code}`.

[](https://hexdocs.pm/req/Req.Steps.html#put_path_params/1-examples)Examples
----------------------------------------------------------------------------

```
iex> Req.get!("https://httpbin.org/status/:code", path_params: [code: 201]).status
201

iex> Req.get!("https://httpbin.org/status/{code}", path_params: [code: 201], path_params_style: :curly).status
201
```

Sets adapter to [`run_plug/1`](https://hexdocs.pm/req/Req.Steps.html#run_plug/1).

See [`run_plug/1`](https://hexdocs.pm/req/Req.Steps.html#run_plug/1) for more information.

[](https://hexdocs.pm/req/Req.Steps.html#put_plug/1-request-options)Request Options
-----------------------------------------------------------------------------------

*   `:plug` - if set, the plug to run the request through.

Sets the "Range" request header.

[](https://hexdocs.pm/req/Req.Steps.html#put_range/1-request-options)Request Options
------------------------------------------------------------------------------------

*   `:range` - can be one of the following:

    *   a string - returned as is

    *   a `first..last` range - converted to `"bytes=<first>-<last>"`

[](https://hexdocs.pm/req/Req.Steps.html#put_range/1-examples)Examples
----------------------------------------------------------------------

```
iex> response = Req.get!("https://httpbin.org/range/100", range: 0..3)
iex> response.status
206
iex> response.body
"abcd"
iex> Req.Response.get_header(response, "content-range")
["bytes 0-3/100"]
```

Sets the user-agent header.

[](https://hexdocs.pm/req/Req.Steps.html#put_user_agent/1-request-options)Request Options
-----------------------------------------------------------------------------------------

*   `:user_agent` - sets the `user-agent` header. Defaults to `"req/0.5.17"`.

[](https://hexdocs.pm/req/Req.Steps.html#put_user_agent/1-examples)Examples
---------------------------------------------------------------------------

```
iex> Req.get!("https://httpbin.org/user-agent").body
%{"user-agent" => "req/0.5.17"}

iex> Req.get!("https://httpbin.org/user-agent", user_agent: "foo").body
%{"user-agent" => "foo"}
```

Runs the request using [`Finch`](https://hexdocs.pm/finch/0.19.0/Finch.html).

This is the default Req _adapter_. See ["Adapter" section in the `Req.Request`](https://hexdocs.pm/req/Req.Request.html#module-adapter) module documentation for more information on adapters.

Finch returns [`Mint.TransportError`](https://hexdocs.pm/mint/1.6.2/Mint.TransportError.html) exceptions on HTTP connection problems. These are automatically converted to [`Req.TransportError`](https://hexdocs.pm/req/Req.TransportError.html) exceptions. Similarly, HTTP-protocol-related errors, [`Mint.HTTPError`](https://hexdocs.pm/mint/1.6.2/Mint.HTTPError.html) and [`Finch.Error`](https://hexdocs.pm/finch/0.19.0/Finch.Error.html), and converted to [`Req.HTTPError`](https://hexdocs.pm/req/Req.HTTPError.html).

[](https://hexdocs.pm/req/Req.Steps.html#run_finch/1-http-1-pools)HTTP/1 Pools
------------------------------------------------------------------------------

On HTTP/1 connections, Finch creates a pool per `{scheme, host, port}` tuple. These pools are kept around to re-use connections as much as possible, however they are **not automatically terminated**. To do so, you can configure custom Finch pool:

```
{:ok, _} =
  Finch.start_link(
    name: MyFinch,
    pools: %{
      default: [
        # terminate idle {scheme, host, port} pool after 60s
        pool_max_idle_time: 60_000
      ]
    }
  )

Req.get!("https://httpbin.org/json", finch: MyFinch)
```

More commonly you'd add the the custom Finch pool as part of your supervision tree in your `application.ex`:

```
children = [
  {Finch,
   name: MyFinch,
   pools: %{
     default: [size: 70]
   }}
]
```

That way you can also configure a bigger pool size for the HTTP pool. You just mustn't forget to pass along `finch: MyFinch` as discussed above. You could use [`Req.default_options/1`](https://hexdocs.pm/req/Req.html#default_options/1) to make it a global default but it's generally discouraged.

For documentation about the possible pool options and their meaning, please check out the [Finch docs on pool configuration options](https://hexdocs.pm/finch/Finch.html#start_link/1-pool-configuration-options).

[](https://hexdocs.pm/req/Req.Steps.html#run_finch/1-request-options)Request Options
------------------------------------------------------------------------------------

*   `:finch` - the name of the Finch pool. Defaults to a pool automatically started by Req.

*   `:connect_options` - dynamically starts (or re-uses already started) Finch pool with the given connection options:

    *   `:timeout` - socket connect timeout in milliseconds, defaults to `30_000`.

    *   `:protocols` - the HTTP protocols to use, defaults to `[:http1]`.

    *   `:hostname` - Mint explicit hostname, see [`Mint.HTTP.connect/4`](https://hexdocs.pm/mint/1.6.2/Mint.HTTP.html#connect/4) for more information.

    *   `:transport_opts` - Mint transport options, see [`Mint.HTTP.connect/4`](https://hexdocs.pm/mint/1.6.2/Mint.HTTP.html#connect/4) for more information.

    *   `:proxy_headers` - Mint proxy headers, see [`Mint.HTTP.connect/4`](https://hexdocs.pm/mint/1.6.2/Mint.HTTP.html#connect/4) for more information.

    *   `:proxy` - Mint HTTP/1 proxy settings, a `{scheme, address, port, options}` tuple. See [`Mint.HTTP.connect/4`](https://hexdocs.pm/mint/1.6.2/Mint.HTTP.html#connect/4) for more information.

    *   `:client_settings` - Mint HTTP/2 client settings, see [`Mint.HTTP.connect/4`](https://hexdocs.pm/mint/1.6.2/Mint.HTTP.html#connect/4) for more information.

*   `:inet6` - if set to true, uses IPv6.

If the request URL looks like IPv6 address, i.e., say, `[::1]`, it defaults to `true` and otherwise defaults to `false`. This is a shortcut for setting `connect_options: [transport_opts: [inet6: true]]`.

*   `:pool_timeout` - pool checkout timeout in milliseconds, defaults to `5000`.

*   `:receive_timeout` - socket receive timeout in milliseconds, defaults to `15_000`.

*   `:unix_socket` - if set, connect through the given UNIX domain socket.

*   `:pool_max_idle_time` - the maximum number of milliseconds that a pool can be idle before being terminated, used only by HTTP1 pools. Default to `:infinity`.

*   `:finch_private` - a map or keyword list of private metadata to add to the Finch request. May be useful for adding custom data when handling telemetry with [`Finch.Telemetry`](https://hexdocs.pm/finch/0.19.0/Finch.Telemetry.html).

*   `:finch_request` - a function that executes the Finch request, defaults to using [`Finch.request/3`](https://hexdocs.pm/finch/0.19.0/Finch.html#request/3).

The function should accept 4 arguments:

    *   `request` - the `%Req.Request{}` struct

    *   `finch_request` - the Finch request

    *   `finch_name` - the Finch name

    *   `finch_options` - the Finch options

And it should return either `{request, response}` or `{request, exception}`.

[](https://hexdocs.pm/req/Req.Steps.html#run_finch/1-examples)Examples
----------------------------------------------------------------------

Custom `:receive_timeout`:

`iex> Req.get!(url, receive_timeout: 1000)`
Connecting through UNIX socket:

```
iex> Req.get!("http:///v1.41/_ping", unix_socket: "/var/run/docker.sock").body
"OK"
```

Custom connection options:

```
iex> Req.get!(url, connect_options: [timeout: 5000])

iex> Req.get!(url, connect_options: [protocols: [:http2]])
```

Connecting without certificate check (useful in development, not recommended in production):

`iex> Req.get!(url, connect_options: [transport_opts: [verify: :verify_none]])`
Connecting with custom certificates:

`iex> Req.get!(url, connect_options: [transport_opts: [cacertfile: "certs.pem"]])`
Connecting through a proxy with basic authentication:

```
iex> Req.new(
...>  url: "https://elixir-lang.org",
...>  connect_options: [
...>    proxy: {:http, "your.proxy.com", 8888, []},
...>    proxy_headers: [{"proxy-authorization", "Basic " <> Base.encode64("user:pass")}]
...>  ]
...> )
iex> |> Req.get!()
```

Transport errors are represented as [`Req.TransportError`](https://hexdocs.pm/req/Req.TransportError.html) exceptions:

```
iex> Req.get("https://httpbin.org/delay/1", receive_timeout: 0, retry: false)
{:error, %Req.TransportError{reason: :timeout}}
```

Runs the request against a plug instead of over the network.

This step is a Req _adapter_. It is set as the adapter by the [`put_plug/1`](https://hexdocs.pm/req/Req.Steps.html#put_plug/1) step if the `:plug` option is set.

It requires [`:plug`](https://hexdocs.pm/plug) dependency:

`{:plug, "~> 1.0"}`
[](https://hexdocs.pm/req/Req.Steps.html#run_plug/1-request-options)Request Options
-----------------------------------------------------------------------------------

*   `:plug` - the plug to run the request through. It can be one of:

    *   A _function_ plug: a `fun(conn)` or `fun(conn, options)` function that takes a [`Plug.Conn`](https://hexdocs.pm/plug/1.16.1/Plug.Conn.html) and returns a [`Plug.Conn`](https://hexdocs.pm/plug/1.16.1/Plug.Conn.html).

    *   A _module_ plug: a `module` name or a `{module, options}` tuple.

Req automatically calls [`Plug.Conn.fetch_query_params/2`](https://hexdocs.pm/plug/1.16.1/Plug.Conn.html#fetch_query_params/2) before your plug, so you can get query params using `conn.query_params`.

Req also automatically parses request body using [`Plug.Parsers`](https://hexdocs.pm/plug/1.16.1/Plug.Parsers.html) for JSON, urlencoded and multipart requests and you can access it with `conn.body_params`. The raw request body of the request is available by calling [`Req.Test.raw_body/1`](https://hexdocs.pm/req/Req.Test.html#raw_body/1) with the `conn` in your tests.

[](https://hexdocs.pm/req/Req.Steps.html#run_plug/1-examples)Examples
---------------------------------------------------------------------

This step is particularly useful to test plugs:

```
defmodule Echo do
  def call(conn, _) do
    "/" <> path = conn.request_path
    Plug.Conn.send_resp(conn, 200, path)
  end
end

test "echo" do
  assert Req.get!("http:///hello", plug: Echo).body == "hello"
end
```

You can define plugs as functions too:

```
test "echo" do
  echo = fn conn ->
    "/" <> path = conn.request_path
    Plug.Conn.send_resp(conn, 200, path)
  end

  assert Req.get!("http:///hello", plug: echo).body == "hello"
end
```

which is particularly useful to create HTTP service stubs, similar to tools like [Bypass](https://github.com/PSPDFKit-labs/bypass).

Response streaming is also supported however at the moment the entire response body is emitted as one chunk:

```
test "echo" do
  plug = fn conn ->
    conn = Plug.Conn.send_chunked(conn, 200)
    {:ok, conn} = Plug.Conn.chunk(conn, "echo")
    {:ok, conn} = Plug.Conn.chunk(conn, "echo")
    conn
  end

  assert Req.get!(plug: plug, into: []).body == ["echoecho"]
end
```

When testing JSON APIs, it's common to use the [`Req.Test.json/2`](https://hexdocs.pm/req/Req.Test.html#json/2) helper:

```
test "JSON" do
  plug = fn conn ->
    Req.Test.json(conn, %{message: "Hello, World!"})
  end

  resp = Req.get!(plug: plug)
  assert resp.status == 200
  assert resp.headers["content-type"] == ["application/json; charset=utf-8"]
  assert resp.body == %{"message" => "Hello, World!"}
end
```

You can simulate network errors by calling [`Req.Test.transport_error/2`](https://hexdocs.pm/req/Req.Test.html#transport_error/2) in your plugs:

```
test "network issues" do
  plug = fn conn ->
    Req.Test.transport_error(conn, :timeout)
  end

  assert Req.get(plug: plug, retry: false) ==
           {:error, %Req.TransportError{reason: :timeout}}
end
```

[](https://hexdocs.pm/req/Req.Steps.html#response-steps)Response Steps
----------------------------------------------------------------------

Decodes response body based on the detected format.

Supported formats:

| Format | Decoder |
| --- | --- |
| `json` | [`Jason.decode/2`](https://hexdocs.pm/jason/1.4.4/Jason.html#decode/2) |
| `tar`, `tgz` | [`:erl_tar.extract/2`](https://www.erlang.org/doc/apps/stdlib/erl_tar.html#extract/2) |
| `zip` | [`:zip.unzip/2`](https://www.erlang.org/doc/apps/stdlib/zip.html#unzip/2) |
| `gzip` | [`:zlib.gunzip/1`](https://www.erlang.org/doc/apps/erts/zlib.html#gunzip/1) |
| `zst` | [`:ezstd.decompress/1`](https://hexdocs.pm/ezstd/1.1.0/ezstd.html#decompress/1) (if [ezstd](https://hex.pm/packages/ezstd) is installed) |
| `csv` | [`NimbleCSV.RFC4180.parse_string/2`](https://hexdocs.pm/nimble_csv/1.2.0/NimbleCSV.RFC4180.html#parse_string/2) (if [nimble_csv](https://hex.pm/packages/nimble_csv) is installed) |

The format is determined based on the `content-type` header of the response. For example, if the `content-type` is `application/json`, the response body is decoded as JSON. The built-in decoders also understand format extensions, such as decoding as JSON for a content-type of `application/vnd.api+json`. To do this, Req falls back to [`MIME.extensions/1`](https://hexdocs.pm/mime/2.0.6/MIME.html#extensions/1); check the documentation for that function for more information.

This step is disabled on response body streaming. If response body is not a binary, in other words it has been transformed by another step, it is left as is.

[](https://hexdocs.pm/req/Req.Steps.html#decode_body/1-request-options)Request Options
--------------------------------------------------------------------------------------

*   `:decode_body` - if set to `false`, disables automatic response body decoding. Defaults to `true`.

*   `:decode_json` - options to pass to [`Jason.decode/2`](https://hexdocs.pm/jason/1.4.4/Jason.html#decode/2), defaults to `[]`.

*   `:raw` - if set to `true`, disables response body decoding. Defaults to `false`.

Note: setting `raw: true` also disables response body decompression in the [`decompress_body/1`](https://hexdocs.pm/req/Req.Steps.html#decompress_body/1) step.

[](https://hexdocs.pm/req/Req.Steps.html#decode_body/1-examples)Examples
------------------------------------------------------------------------

Decode JSON:

```
iex> response = Req.get!("https://httpbin.org/json")
...> response.body["slideshow"]["title"]
"Sample Slide Show"
```

Decode gzip:

```
iex> response = Req.get!("https://httpbin.org/gzip")
...> response.body["gzipped"]
true
```

Decompresses the response body based on the `content-encoding` header.

This step is disabled on response body streaming. If response body is not a binary, in other words it has been transformed by another step, it is left as is.

Supported formats:

| Format | Decoder |
| --- | --- |
| gzip, x-gzip | [`:zlib.gunzip/1`](https://www.erlang.org/doc/apps/erts/zlib.html#gunzip/1) |
| br | [`:brotli.decode/1`](https://hexdocs.pm/brotli/0.3.2/brotli.html#decode/1) (if [brotli](http://hex.pm/packages/brotli) is installed) |
| zstd | [`:ezstd.decompress/1`](https://hexdocs.pm/ezstd/1.1.0/ezstd.html#decompress/1) (if [ezstd](https://hex.pm/packages/ezstd) is installed) |
| _other_ | Returns data as is |

This step updates the following headers to reflect the changes:

*   `content-encoding` is removed
*   `content-length` is removed

[](https://hexdocs.pm/req/Req.Steps.html#decompress_body/1-options)Options
--------------------------------------------------------------------------

*   `:raw` - if set to `true`, disables response body decompression. Defaults to `false`.

Note: setting `raw: true` also disables response body decoding in the [`decode_body/1`](https://hexdocs.pm/req/Req.Steps.html#decode_body/1) step.

[](https://hexdocs.pm/req/Req.Steps.html#decompress_body/1-examples)Examples
----------------------------------------------------------------------------

```
iex> response = Req.get!("https://httpbin.org/gzip")
iex> response.body["gzipped"]
true
```

If the [brotli](http://hex.pm/packages/brotli) package is installed, Brotli is also supported:

```
Mix.install([
  :req,
  {:brotli, "~> 0.3.0"}
])

response = Req.get!("https://httpbin.org/brotli")
Req.Response.get_header(response, "content-encoding")
#=> ["br"]
response.body["brotli"]
#=> true
```

Handles HTTP Digest authentication.

This step is invoked when setting `:auth` option with `{:digest, ...}`. When response is HTTP 401 with `www-authenticate` header, this step will calculate `authorization: Digest ...` header and make another request.

See [`auth/1`](https://hexdocs.pm/req/Req.Steps.html#auth/1).

[](https://hexdocs.pm/req/Req.Steps.html#handle_http_digest/1-examples)Examples
-------------------------------------------------------------------------------

```
iex> resp = Req.get!("https://httpbin.org/digest-auth/auth/user/pass", auth: {:digest, "user:pass"})
iex> resp.status
200
```

Handles HTTP 4xx/5xx error responses.

[](https://hexdocs.pm/req/Req.Steps.html#handle_http_errors/1-request-options)Request Options
---------------------------------------------------------------------------------------------

*   `:http_errors` - how to handle HTTP 4xx/5xx error responses. Can be one of the following:

    *   `:return` (default) - return the response

    *   `:raise` - raise an error

[](https://hexdocs.pm/req/Req.Steps.html#handle_http_errors/1-examples)Examples
-------------------------------------------------------------------------------

```
iex> Req.get!("https://httpbin.org/status/404").status
404

iex> Req.get!("https://httpbin.org/status/404", http_errors: :raise)
** (RuntimeError) The requested URL returned error: 404
Response body: ""
```

Follows redirects.

The original request method may be changed to GET depending on the status code:

| Code | Method handling |
| --- | --- |
| 301, 302, 303 | Changed to GET |
| 307, 308 | Method not changed |

[](https://hexdocs.pm/req/Req.Steps.html#redirect/1-request-options)Request Options
-----------------------------------------------------------------------------------

*   `:redirect` - if set to `false`, disables automatic response redirects. Defaults to `true`.

*   `:redirect_trusted` - by default, authorization credentials are only sent on redirects with the same host, scheme and port. If `:redirect_trusted` is set to `true`, credentials will be sent to any host.

*   `:redirect_log_level` - the log level to emit redirect logs at. Can also be set to `false` to disable logging these messages. Defaults to `:debug`.

*   `:max_redirects` - the maximum number of redirects, defaults to `10`. If the limit is reached, the pipeline is halted and a [`Req.TooManyRedirectsError`](https://hexdocs.pm/req/Req.TooManyRedirectsError.html) exception is returned.

[](https://hexdocs.pm/req/Req.Steps.html#redirect/1-examples)Examples
---------------------------------------------------------------------

```
iex> Req.get!("http://api.github.com").status
# 23:24:11.670 [debug] redirecting to https://api.github.com/
200

iex> Req.get!("https://httpbin.org/redirect/4", max_redirects: 3)
# 23:07:59.570 [debug] redirecting to /relative-redirect/3
# 23:08:00.068 [debug] redirecting to /relative-redirect/2
# 23:08:00.206 [debug] redirecting to /relative-redirect/1
** (RuntimeError) too many redirects (3)

iex> Req.get!("http://api.github.com", redirect_log_level: false)
200

iex> Req.get!("http://api.github.com", redirect_log_level: :error)
# 23:24:11.670 [error]  redirecting to https://api.github.com/
200
```

Verifies the response body checksum.

See [`checksum/1`](https://hexdocs.pm/req/Req.Steps.html#checksum/1) for more information.

[](https://hexdocs.pm/req/Req.Steps.html#error-steps)Error Steps
----------------------------------------------------------------

Retries a request in face of errors.

This function can be used as either or both response and error step.

[](https://hexdocs.pm/req/Req.Steps.html#retry/1-request-options)Request Options
--------------------------------------------------------------------------------

*   `:retry` - can be one of the following:

    *   `:safe_transient` (default) - retry safe (GET/HEAD) requests on one of:

        *   HTTP 408/429/500/502/503/504 responses

        *   [`Req.TransportError`](https://hexdocs.pm/req/Req.TransportError.html) with `reason: :timeout | :econnrefused | :closed`

        *   [`Req.HTTPError`](https://hexdocs.pm/req/Req.HTTPError.html) with `protocol: :http2, reason: :unprocessed`

    *   `:transient` - same as `:safe_transient` except retries all HTTP methods (POST, DELETE, etc.)

    *   `fun` - a 2-arity function that accepts a [`Req.Request`](https://hexdocs.pm/req/Req.Request.html) and either a [`Req.Response`](https://hexdocs.pm/req/Req.Response.html) or an exception struct and returns one of the following:

        *   `true` - retry with the default delay controller by default delay option described below.

        *   `{:delay, milliseconds}` - retry with the given delay.

        *   `false/nil` - don't retry.

    *   `false` - don't retry.

*   `:retry_delay` - if not set, which is the default, the retry delay is determined by the value of the `Retry-After` header on HTTP 429/503 responses. If the header is not set, or the header value is negative, the default delay follows a simple exponential backoff: 1s, 2s, 4s, 8s, ...

`:retry_delay` can be set to a function that receives the retry count (starting at 0) and returns the delay, the number of milliseconds to sleep before making another attempt.

*   `:retry_log_level` - the log level to emit retry logs at. Can also be set to `false` to disable logging these messages. Defaults to `:warning`.

*   `:max_retries` - maximum number of retry attempts, defaults to `3` (for a total of `4` requests to the server, including the initial one.)

[](https://hexdocs.pm/req/Req.Steps.html#retry/1-examples)Examples
------------------------------------------------------------------

With default options:

```
iex> Req.get!("https://httpbin.org/status/500,200").status
# 19:02:08.463 [warning] retry: got response with status 500, will retry in 2000ms, 2 attempts left
# 19:02:10.710 [warning] retry: got response with status 500, will retry in 4000ms, 1 attempt left
200
```

Delay with jitter:

```
iex> delay = fn n -> trunc(Integer.pow(2, n) * 1000 * (1 - 0.1 * :rand.uniform())) end
iex> Req.get!("https://httpbin.org/status/500,200", retry_delay: delay).status
# 08:43:19.101 [warning] retry: got response with status 500, will retry in 941ms, 2 attempts left
# 08:43:22.958 [warning] retry: got response with status 500, will retry in 1877ms, 1 attempt left
200
```
