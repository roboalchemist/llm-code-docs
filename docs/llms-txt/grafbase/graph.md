# Source: https://grafbase.com/docs/gateway/configuration/graph.md

# Graph

```toml
[graph]
path = "/graphql"
websocket_path = "/ws"
introspection = false
```

- `path` (optional): Specifies the URL path that hosts the GraphQL API. Defaults to `/graphql`.
- `websocket_path` (optional): Specifies the URL path of the Websocket endpoint, for subscriptions. Defaults to `/ws`.
- `introspection`: Enable or disable GraphQL introspection. The default value is `false`.

## Contracts

```toml
[graph.contracts]
# default_key = ""
cache.max_size = 100
```

Schema contract configuration to be used in conjunction with a contracts extension. The default key is used if the `on_request`
hook does not exist or doesn't return a contract key. The cache max size defines how many schema contracts at most the gateway keeps in cache.

See the [tag](/extensions/tag) extension for a contract extension.