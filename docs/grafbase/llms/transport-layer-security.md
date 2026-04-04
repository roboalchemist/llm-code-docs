# Source: https://grafbase.com/docs/gateway/configuration/transport-layer-security.md

# Transport Layer Security

You can configure the gateway to serve HTTPS traffic without a reverse proxy. When you don't define a `tls` section, the server uses plain HTTP mode.

```toml
[tls]
certificate = "/path/to/cert.pem"
key = "/path/to/key.pem"
```

- `certificate`: Specifies the path to your PEM format certificate file.
- `key`: Specifies the path to your PEM format private key file.