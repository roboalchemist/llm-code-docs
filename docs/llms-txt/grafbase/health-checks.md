# Source: https://grafbase.com/docs/gateway/configuration/health-checks.md

# Health Checks

Configure a health check endpoint in the gateway:

```toml
[health]
enabled = true
listen = "0.0.0.0:9668"
path = "/health"
```

- `enabled`: Enables or disables the health check endpoint. Default value is `true`.
- `path`: Sets the request path for the endpoint. Default value is `"/health"`.
- `listen`: Sets the address and port for health requests. Uses the main GraphQL endpoint's socket and port if not specified.

The health check endpoint sends a status code 200 with a body of `{"status": "healthy"}` when the gateway runs in a healthy state. The service returns a 503 status code when it detects an unhealthy gateway state.

The `tls` configuration settings in your configuration apply to the health check endpoint.