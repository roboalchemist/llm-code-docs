# Source: https://grafbase.com/docs/gateway/configuration/headers.md

# Headers

Header go through many different components during the lifecycle of a request:

1. [on_request](https://docs.rs/grafbase-sdk/latest/grafbase_sdk/trait.HooksExtension.html#method.on_request) hook has mutable access to the incoming gateway headers before anything else.
2. [authenticate](https://docs.rs/grafbase-sdk/latest/grafbase_sdk/trait.AuthenticationExtension.html#tymethod.authenticate) has read-only access to the gateway headers
3. global header rules are applied. From now on we're talking about "subgraph headers" rather than the "gateway headers"
4. [authorize_query](https://docs.rs/grafbase-sdk/latest/grafbase_sdk/trait.AuthorizationExtension.html#tymethod.authorize_query) has mutable access to the subgraph headers.
5. subgraph header rules are applied.
6. [on_subgraph_request](https://docs.rs/grafbase-sdk/latest/grafbase_sdk/trait.HooksExtension.html#method.on_subgraph_request) is the final component with mutable access to the subgraph headers just before sending the request.

## Header rules

### Global header rules

Define header rules and execute them in order. The gateway uses `forward`, `insert`, `rename_duplicate` or `remove` rules to manage headers for subgraphs:

```toml
[[headers]]
rule = "forward"
name = "authorization"

[[headers]]
rule = "forward"
name = "x-custom-header"
rename = "y-custom-header"

[[headers]]
rule = "forward"
name = "x-possible-empty"
default = "default-value"
```

Header rules also support pattern expressed as [regular expression](https://docs.rs/regex/latest/regex/#syntax) that apply on the header names. They're case insensitive.

```toml
[[headers]]
rule = "forward"
pattern = "^x-custom*"
```

Use the `insert` rule to add header values:

```toml
[[headers]]
rule = "insert"
name = "authorization"
value = "Bearer secret-token"
```

Insert header values from environment variables:

```toml
[[headers]]
rule = "insert"
name = "authorization"
value = "Bearer {{ env.AUTHORIZATION_TOKEN }}"
```

Use the `remove` rule to block header forwarding for headers that match patterns:

```toml
[[headers]]
rule = "remove"
name = "x-custom-secret"
```

The `rename_duplicate` rule forwards the defined header value and copies the value with the specified rename to the subgraphs.

```toml
[[headers]]
rule = "rename_duplicate"
name = "x-custom-value"
default = "the value was missing"
rename = "y-custom-value"
```

The gateway forwards two headers to the subgraph with the same value - one named `x-custom-value` and one named `y-custom-value`. When a request is missing the `x-custom-value` header, and you define a `default` value, the gateway creates both headers using that default value. If you omit the default, the gateway doesn't forward the header or create a duplicate.

<CardWidget>

These headers don't use header rules:

- `Accept`
- `Accept-Charset`
- `Accept-Encoding`
- `Accept-Ranges`
- `Connection`
- `Content-Length`
- `Content-Type`
- `Keep-Alive`
- `Proxy-Authenticate`
- `Proxy-Authorization`
- `TE`
- `Trailer`
- `Transfer-Encoding`
- `Upgrade`

</CardWidget>

### Subgraph header rules

It is also possible to use dedicated subgraph header rules. For example to apply header rules only for the `prodcuts` subgraph you may use the following:

```toml
[[subgraph.products.headers]]
rule = "forward"
name = "x-custom-header"
rename = "y-custom-header"
```