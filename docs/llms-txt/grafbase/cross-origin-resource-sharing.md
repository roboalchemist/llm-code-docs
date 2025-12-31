# Source: https://grafbase.com/docs/gateway/configuration/cross-origin-resource-sharing.md

# Cross-Origin Resource Sharing

Configure CORS to prevent unauthorized browser requests.

```toml
[cors]
allow_credentials = false
allow_origins = "https://app.grafbase.com"
max_age = "60s"
allow_methods = ["GET", "POST"]
allow_headers = "Content-Type"
expose_headers = ["Access-Control-Allow-Origin"]
allow_private_network = false
```

- `allow_credentials`: Enables or disables credential sending. Defaults to `false`.
- `allow_origins`: Allowed domains, one or multiple domains in a list. A Glob pattern can also be used. To accept any domain, use `"*"`. Defaults to no domains if CORS is enabled.
- `max_age` ([duration](https://grafbase.com/docs/gateway/configuration/durations.md)): Duration for caching preflight `OPTIONS` request results. Default: none.
- `allow_methods`: One or multiple allowed HTTP methods. To accept any method, use `"*"`. Defaults to none if CORS is enabled.
- `allow_headers`: One or multiple allowed headers. To accept any header, use `"*"`. Defaults to no headers if CORS is enabled.
- `expose_headers`: Headers a preflight request can return to the client. Default: no headers if CORS is enabled.
- `allow_private_network`: Allows private network requests. Defaults to `false`.

The supported glob patterns for `allow_origins` are:

- `*` matches zero or more characters.
- `?` matches any single character.
- `[ab]` matches one of the characters contained in the brackets. Use `[!ab]` to match any character except `a` and `b`.
- `{p1,p2}` matches either pattern `p1` or `p2`.

For example `*.example.com` will match all sub-domains of `example.com`.