# Source: https://grafbase.com/docs/gateway/configuration/network.md

# Network

```toml
[network]
listen_address = "127.0.0.1:5000"
```

- `listen_address`: Specify the address that the server binds to. The server defaults to `127.0.0.1:5000`. Configure this setting in the configuration file or specify it through the command line interface with the `--listen-address` argument.