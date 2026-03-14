# Source: https://docs.nats.io/running-a-nats-service/configuration/clustering/jetstream_clustering/troubleshooting.md

# Troubleshooting

Diagnosing problems in NATS JetStream clusters requires:

* knowledge of [JetStream concepts](https://docs.nats.io/nats-concepts/jetstream)
* knowledge of the [NATS Command Line Interface (CLI)](https://github.com/nats-io/natscli#the-nats-command-line-interface)

The following tips and commands (while not an exhaustive list) can be useful when diagnosing problems in NATS JetStream clusters:

## Troubleshooting tips

1. Look at [nats-server](https://github.com/nats-io/nats-server) logs. By default, only warning and error logs are produced, but debug and trace logs can be turned on from the command line using `-D` and `-DV`, respectively. Alternatively, enabling `debug` or `trace` in the [server config](https://docs.nats.io/running-a-nats-service/configuration#monitoring-and-tracing).
2. Make sure that in the [NATS JetStream configuration](https://docs.nats.io/running-a-nats-service/configuration/clustering/jetstream_clustering/..#configuration), at least one system user is configured in this section: `{ $SYS { users } }`.

### `nats account` commands

| Command                                                                                               | Description                                 |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| [`nats account info`](https://docs.nats.io/running-a-nats-service/nats_admin/jetstream_admin/account) | Verify that JetStream is enabled on account |

### Basic `nats server` commands

| Command                                                                | Description                            |
| ---------------------------------------------------------------------- | -------------------------------------- |
| `nats server ls`                                                       | List known servers                     |
| `nats server ping`                                                     | Ping all servers                       |
| `nats server info`                                                     | Show information about a single server |
| [`nats server check`](https://docs.nats.io/clients#testing-your-setup) | Health check for NATS servers          |

### `nats server report` commands

| Command                                                                                                                                         | Description                  |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| `nats server report connections`                                                                                                                | Report on connections        |
| `nats server report accounts`                                                                                                                   | Report on account activity   |
| [`nats server report jetstream`](https://docs.nats.io/running-a-nats-service/configuration/clustering/administration#viewing-the-cluster-state) | Report on JetStream activity |

### `nats server request` commands

| Command                                                                                                                                          | Description                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- |
| [`nats server request jetstream`](https://docs.nats.io/running-a-nats-service/configuration/clustering/administration#viewing-the-cluster-state) | Show JetStream details        |
| `nats server request subscriptions`                                                                                                              | Show subscription information |
| `nats server request variables`                                                                                                                  | Show runtime variables        |
| `nats server request connections`                                                                                                                | Show connection details       |
| `nats server request routes`                                                                                                                     | Show route details            |
| `nats server request gateways`                                                                                                                   | Show gateway details          |
| `nats server request leafnodes`                                                                                                                  | Show leafnode details         |
| `nats server request accounts`                                                                                                                   | Show account details          |

### `nats server cluster` commands

| Command                                                                                                                                                            | Description                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------- |
| [`nats server cluster step-down`](https://docs.nats.io/running-a-nats-service/configuration/clustering/administration#forcing-stream-and-consumer-leader-election) | Force a new leader election by standing down the current meta leader |
| [`nats server cluster peer-remove`](https://docs.nats.io/running-a-nats-service/configuration/clustering/administration#evicting-a-peer)                           | Removes a server from a JetStream cluster                            |

### Experimental commands

| Command                                                                               | Description                                      |
| ------------------------------------------------------------------------------------- | ------------------------------------------------ |
| [`nats traffic`](https://github.com/nats-io/natscli/blob/main/cli/traffic_command.go) | Monitor NATS traffic. (**Experimental command**) |

## Further troubleshooting references

* [Testing your setup](https://docs.nats.io/clients#testing-your-setup)
