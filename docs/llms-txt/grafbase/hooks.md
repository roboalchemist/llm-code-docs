# Source: https://grafbase.com/docs/gateway/configuration/hooks.md

# Hooks

Deploy the Grafbase Gateway together with the hooks extension, as per the [Gateway hooks guide](/guides/implementing-gateway-hooks).

```toml
[extensions.my-hooks] # my-hooks is the name of your hooks project
path = "path/to/build"
networking = false
stdout = false
stderr = false
environment_variables = false
max_pool_size = 1000
config = {}
```

- `location` specifies the path to the WASM file that contains custom hooks. You must provide a valid path and have read access to the file.
- `networking` enables network access with TCP and UDP sockets, name resolution and WASI HTTP bindings to the guest. TCP and UDP sockets work only if the guest language supports WASI preview 2 standard. Default value is false.
- `stdout` enables the guest to write to the standard output stream. Default value is `false`.
- `stderr` enables the guest to write to the standard error stream. Default value is `false`.
- `environment_variables` copies host environment variables to the guest. Default value is `false`.
- `max_pool_size` specifies the number of hook instances that can run concurrently. Default value is four times the number of CPU cores.
- `config` allows custom configuration for the extension. You must handle parsing and validation of the configuration in the extension initialization.