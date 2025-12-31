# Source: https://grafbase.com/docs/gateway/configuration/cross-site-request-forgery-prevention.md

# Cross-Site Request Forgery Prevention

Enable CSRF protection if the graph is accessible over the internet with a browser.

If enabled, you must provide a special header `x-grafbase-csrf-protection: 1` in every request not `OPTIONS`. The server returns `403 Forbidden` if the header is not found.

```toml
[csrf]
enabled = true
```

- `enabled`: Enables CSRF protection. Defaults to `false`.