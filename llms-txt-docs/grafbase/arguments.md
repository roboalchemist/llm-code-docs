# Source: https://grafbase.com/docs/gateway/arguments.md

# Gateway Command Line Arguments

The Grafbase Gateway accepts command line arguments to configure its operations. Specify the gateway's behavior using these arguments. Run `grafbase-gateway --help` to see all available options.

## Listen Address

**Argument**: `-l, --listen-address <LISTEN_ADDRESS>`

The IPv4 or IPv6 address and port to listen on. Default is `127.0.0.1:5000`.

## Graph Ref

**Argument**: `-g, --graph-ref <GRAPH_REF>`

The graph reference to fetch from the Grafbase API, following the format `graph@branch`. Branch can be omitted to use the production branch. The gateway checks for graph changes every ten seconds. Cannot be used with the `--schema` option.

## Schema

**Argument**: `-s, --schema <SCHEMA_FILE>`

The path to the federated schema file. Use this option to run the gateway in air-gapped mode. Cannot be used with the `--graph-ref` option.

The gateway checks for schema changes every five seconds. If the file changes, it reloads the file, creates a new engine; and if configured, warms the operation cache.

## Config

**Argument**: `-c, --config <CONFIG_FILE>`

The path to the TOML configuration file.

## Log Level

**Argument**: `--log <LOG_LEVEL>`

Sets the logging level and controls the detail for all spans, logs and trace events.

In production, use only `off`, `error`, `warn`, and `info` levels. More verbose levels like `debug` include sensitive information such as request variables and responses.

Setting the level to `off` or `error` prevents the gateway from sending traces to the OpenTelemetry collector.

You can use these values: `off`, `error`, `warn`, `info`, `debug`, `trace`, or a custom string. Custom strings pass directly to [`tracing_subscriber::EnvFilter`] for debugging only. Grafbase makes no guarantees about the format stability.

The default level is `info`.

## Log Style

**Argument**: `--log-style <LOG_STYLE>`

Select a log style format for the gateway. Choose `pretty` for human-readable logs, `json` for machine-readable logs, or `text` for black and white logs when you pipe standard output to a file. Grafbase uses `pretty` as the default style.

## Hot Reload

**Argument**: `--hot-reload`

Enables hot reloading of the gateway configuration. This option applies to configuration sections that can change without a gateway restart.

## Help

**Argument**: `-h, --help`

## Version

**Argument**: `-V, --version`