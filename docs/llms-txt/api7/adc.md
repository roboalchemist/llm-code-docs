# Source: https://docs.api7.ai/enterprise/3.2.16.7/reference/adc.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/reference/adc.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/reference/adc.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/reference/adc.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/reference/adc.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/reference/adc.md

# Source: https://docs.api7.ai/enterprise/reference/adc.md

# Source: https://docs.api7.ai/enterprise/3.8.x/reference/adc.md

# Source: https://docs.api7.ai/enterprise/3.7.x/reference/adc.md

# Source: https://docs.api7.ai/enterprise/3.6.x/reference/adc.md

# Source: https://docs.api7.ai/enterprise/3.5.x/reference/adc.md

# Source: https://docs.api7.ai/enterprise/3.4.x/reference/adc.md

# Source: https://docs.api7.ai/enterprise/3.3.x/reference/adc.md

# Source: https://docs.api7.ai/apisix/reference/adc.md

# Source: https://docs.api7.ai/enterprise/3.3.x/reference/adc.md

# Source: https://docs.api7.ai/apisix/reference/adc.md

# API Declarative CLI (ADC)

API Declarative CLI (ADC) is a command-line tool for managing both APISIX and API7 Enterprise declaratively. It offers simplicity and clarity in defining the desired state of the gateway, allowing developers and administrators to focus on the result rather than the steps.

The declarative configurations serve as the single source of truth that developers can manage through their existing version control systems.

ADC has the following general syntax:

```
adc [command] [options]
```

with global options:

* `-v, --version` to check the version
* `-h, --help` to print the help menu of the command

## Install ADC[â](#install-adc "Direct link to Install ADC")

Install ADC with a quickstart script:

```
curl -sL "https://run.api7.ai/adc/install" | bash
```

To verify the installation, run:

```
adc help
```

You should see the following response:

```
Usage: adc [options] [command]

Options:
  -v, --version      output the version number
  -h, --help         display help for command

Commands:
  ping [options]     Verify connectivity with backend
  dump [options]     Dump configurations from the backend
  diff [options]     Show the difference between local and backend configurations
  sync [options]     Sync local configurations to backend
  convert [options]  Convert other API spec to ADC configurations
  lint [options]     Check provided configuration files, local execution only, ensuring inputs meet ADC requirements
  help [command]     display help for command
```

By default, the backend is set to `apisix` and the server is set to `http://localhost:9180`. To verify connectivity with APISIX, run:

```
adc ping
```

You should see the following response:

```
Connected to the "apisix" backend successfully!
```

## Configure ADC[â](#configure-adc "Direct link to Configure ADC")

ADC needs to be configured before it can be used to manage the gateway. You can configure ADC using environment variables or command-line flags.

### Using Environment Variables[â](#using-environment-variables "Direct link to Using Environment Variables")

ADC exposes all configuration options as environment variables. For example, you can configure the backend type and address using the `ADC_BACKEND` and `ADC_SERVER` environment variables, respectively.

```
export ADC_BACKEND=apisix
export ADC_SERVER=http://localhost:9180
```

A better way is to configure these options in a `.env` file:

.env

```
ADC_BACKEND=apisix
ADC_SERVER=http://localhost:9180
```

### Using Command-Line Flags[â](#using-command-line-flags "Direct link to Using Command-Line Flags")

You can also configure ADC or overwrite the configuration in the environment variables using the command-line flags. For example, to configure/overwrite the backend type and address for the `ping` command:

```
adc ping --backend apisix --server "http://localhost:9180"
```

Run `adc help [command]` to see the available configuration options for a command.

## Commands[â](#commands "Direct link to Commands")

### `adc ping`[â](#adc-ping "Direct link to adc-ping")

Ping the configured backend to verify connectivity.

| Option                             | Default Value           | Description                                                                                                       | Valid Values              | Env Variable               |
| ---------------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------- | -------------------------- |
| `--verbose <integer>`              | `1`                     | Overrides verbose logging levels.`0` represents no log, `1` represents basic logs, and `2` represents debug logs. | `0`, `1` or `2`           |                            |
| `--backend <backend>`              | `apisix`                | Backend type to connect.                                                                                          | `apisix` or `api7ee`      | `ADC_BACKEND`              |
| `--server <string>`                | `http://localhost:9180` | Backend server address.                                                                                           |                           | `ADC_SERVER`               |
| `--token <string>`                 |                         | API token to access the backend.                                                                                  |                           | `ADC_TOKEN`                |
| `--gateway-group <string>`         | `default`               | Gateway group to operate on.                                                                                      |                           | `ADC_GATEWAY_GROUP`        |
| `--label-selector <selectors>`     |                         | Resource labels to filter for.                                                                                    |                           |                            |
| `--include-resource-type <string>` |                         | Filter for resource types, such that the resource search results should only contain the specified type.          |                           |                            |
| `--exclude-resource-type <string>` |                         | Filter for resource types, such that the resource search results should exclude the specified type.               |                           |                            |
| `--timeout <duration>`             | `10s`                   | Request timeout for the client to connect with the backend Admin API in duration, such as 30s, 10m, and 1h10m.    |                           |                            |
| `--ca-cert-file <string>`          |                         | Path to CA certificate for verifying the backend Admin API.                                                       |                           | `ADC_CA_CERT_FILE`         |
| `--tls-client-cert-file <string>`  |                         | Path to mutual TLS client certificate for verifying the backend Admin API.                                        |                           | `ADC_TLS_CLIENT_CERT_FILE` |
| `--tls-client-key-file <string>`   |                         | Path to mutual TLS client key for verifying the backend Admin API.                                                | `ADC_TLS_CLIENT_KEY_FILE` |                            |
| `--tls-skip-verify`                | `false`                 | Whether to verify the TLS certificate when connecting to the backend Admin API.                                   | `ADC_TLS_SKIP_VERIFY`     |                            |
| `--request-concurrent`             | `10`                    | Number of concurrent requests to the backend                                                                      |                           |                            |

#### Sample Usage[â](#sample-usage "Direct link to Sample Usage")

```
adc ping --backend apisix --server http://localhost:9180
```

### `adc lint`[â](#adc-lint "Direct link to adc-lint")

Validate the provided configuration files locally.

| Option                   | Default Value | Description    | Valid Values | Env Variable |
| ------------------------ | ------------- | -------------- | ------------ | ------------ |
| `-f, --file <file-path>` |               | Files to lint. |              |              |

#### Sample Usage[â](#sample-usage-1 "Direct link to Sample Usage")

```
adc lint -f service-a.yaml -f service-b.yaml
```

### `adc sync`[â](#adc-sync "Direct link to adc-sync")

Synchronize the local configuration to the connected backend.

| Option                             | Default Value           | Description                                                                                                       | Valid Values              | Env Variable               |
| ---------------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------- | -------------------------- |
| `--verbose <integer>`              | `1`                     | Overrides verbose logging levels.`0` represents no log, `1` represents basic logs, and `2` represents debug logs. | `0`, `1` or `2`           |                            |
| `--backend <backend>`              | `apisix`                | Backend type to connect.                                                                                          | `apisix` or `api7ee`      | `ADC_BACKEND`              |
| `--server <string>`                | `http://localhost:9180` | Backend server address.                                                                                           |                           | `ADC_SERVER`               |
| `--token <string>`                 |                         | API token to access the backend.                                                                                  |                           | `ADC_TOKEN`                |
| `--gateway-group <string>`         | `default`               | Gateway group to operate on.                                                                                      |                           | `ADC_GATEWAY_GROUP`        |
| `--label-selector <selectors>`     |                         | Resource labels to filter for.                                                                                    |                           |                            |
| `-f, --file <file-path>`           |                         | Configuration files to synchronize.                                                                               |                           |                            |
| `--include-resource-type <string>` |                         | Filter for resource types, such that the resource search results should only contain the specified type.          |                           |                            |
| `--exclude-resource-type <string>` |                         | Filter for resource types, such that the resource search results should exclude the specified type.               |                           |                            |
| `--timeout <duration>`             | `10s`                   | Request timeout for the client to connect with the backend Admin API in duration, such as 30s, 10m, and 1h10m.    |                           |                            |
| `--ca-cert-file <string>`          |                         | Path to CA certificate for verifying the backend Admin API.                                                       |                           | `ADC_CA_CERT_FILE`         |
| `--tls-client-cert-file <string>`  |                         | Path to mutual TLS client certificate for verifying the backend Admin API.                                        |                           | `ADC_TLS_CLIENT_CERT_FILE` |
| `--tls-client-key-file <string>`   |                         | Path to mutual TLS client key for verifying the backend Admin API.                                                | `ADC_TLS_CLIENT_KEY_FILE` |                            |
| `--tls-skip-verify`                | `false`                 | Whether to verify the TLS certificate when connecting to the backend Admin API.                                   | `ADC_TLS_SKIP_VERIFY`     |                            |

#### Sample Usage[â](#sample-usage-2 "Direct link to Sample Usage")

```
adc sync -f service-a.yaml -f service-b.yaml --backend apisix --server http://localhost:9180
```

### `adc dump`[â](#adc-dump "Direct link to adc-dump")

Save backend configuration to a local file.

| Option                             | Default Value           | Description                                                                                                       | Valid Values              | Env Variable               |
| ---------------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------- | -------------------------- |
| `--verbose <integer>`              | `1`                     | Overrides verbose logging levels.`0` represents no log, `1` represents basic logs, and `2` represents debug logs. | `0`, `1` or `2`           |                            |
| `--backend <backend>`              | `apisix`                | Backend type to connect.                                                                                          | `apisix` or `api7ee`      | `ADC_BACKEND`              |
| `--server <string>`                | `http://localhost:9180` | Backend server address.                                                                                           |                           | `ADC_SERVER`               |
| `--token <string>`                 |                         | API token to access the backend.                                                                                  |                           | `ADC_TOKEN`                |
| `--gateway-group <string>`         | `default`               | Gateway group to operate on.                                                                                      |                           | `ADC_GATEWAY_GROUP`        |
| `--label-selector <selectors>`     |                         | Resource labels to filter for.                                                                                    |                           |                            |
| `-o, --output <file-path>`         |                         | Specify the file path where the backend data should be dumped.                                                    |                           |                            |
| `--include-resource-type <string>` |                         | Filter for resource types, such that the resource search results should only contain the specified type.          |                           |                            |
| `--exclude-resource-type <string>` |                         | Filter for resource types, such that the resource search results should exclude the specified type.               |                           |                            |
| `--timeout <duration>`             | `10s`                   | Request timeout for the client to connect with the backend Admin API in duration, such as 30s, 10m, and 1h10m.    |                           |                            |
| `--ca-cert-file <string>`          |                         | Path to CA certificate for verifying the backend Admin API.                                                       |                           | `ADC_CA_CERT_FILE`         |
| `--tls-client-cert-file <string>`  |                         | Path to mutual TLS client certificate for verifying the backend Admin API.                                        |                           | `ADC_TLS_CLIENT_CERT_FILE` |
| `--tls-client-key-file <string>`   |                         | Path to mutual TLS client key for verifying the backend Admin API.                                                | `ADC_TLS_CLIENT_KEY_FILE` |                            |
| `--tls-skip-verify`                | `false`                 | Whether to verify the TLS certificate when connecting to the backend Admin API.                                   | `ADC_TLS_SKIP_VERIFY`     |                            |

#### Sample Usage[â](#sample-usage-3 "Direct link to Sample Usage")

```
adc dump -o apisix-dump.yaml --backend apisix --server http://localhost:9180
```

### `adc diff`[â](#adc-diff "Direct link to adc-diff")

Show differences in the configuration between the local file and the backend.

| Option                             | Default Value           | Description                                                                                                       | Valid Values              | Env Variable               |
| ---------------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------- | -------------------------- |
| `--verbose <integer>`              | `1`                     | Overrides verbose logging levels.`0` represents no log, `1` represents basic logs, and `2` represents debug logs. | `0`, `1` or `2`           |                            |
| `--backend <backend>`              | `apisix`                | Backend type to connect.                                                                                          | `apisix` or `api7ee`      | `ADC_BACKEND`              |
| `--server <string>`                | `http://localhost:9180` | Backend server address.                                                                                           |                           | `ADC_SERVER`               |
| `--token <string>`                 |                         | API token to access the backend.                                                                                  |                           | `ADC_TOKEN`                |
| `--gateway-group <string>`         | `default`               | Gateway group to operate on.                                                                                      |                           | `ADC_GATEWAY_GROUP`        |
| `--label-selector <selectors>`     |                         | Resource labels to filter for.                                                                                    |                           |                            |
| `-f, --file <file-path>`           |                         | Configuration files to compare.                                                                                   |                           |                            |
| `--include-resource-type <string>` |                         | Filter for resource types, such that the resource search results should only contain the specified type.          |                           |                            |
| `--exclude-resource-type <string>` |                         | Filter for resource types, such that the resource search results should exclude the specified type.               |                           |                            |
| `--timeout <duration>`             | `10s`                   | Request timeout for the client to connect with the backend Admin API in duration, such as 30s, 10m, and 1h10m.    |                           |                            |
| `--ca-cert-file <string>`          |                         | Path to CA certificate for verifying the backend Admin API.                                                       |                           | `ADC_CA_CERT_FILE`         |
| `--tls-client-cert-file <string>`  |                         | Path to mutual TLS client certificate for verifying the backend Admin API.                                        |                           | `ADC_TLS_CLIENT_CERT_FILE` |
| `--tls-client-key-file <string>`   |                         | Path to mutual TLS client key for verifying the backend Admin API.                                                | `ADC_TLS_CLIENT_KEY_FILE` |                            |
| `--tls-skip-verify`                | `false`                 | Whether to verify the TLS certificate when connecting to the backend Admin API.                                   | `ADC_TLS_SKIP_VERIFY`     |                            |

#### Sample Usage[â](#sample-usage-4 "Direct link to Sample Usage")

```
adc diff -f service-a.yaml -f service-b.yaml --backend apisix --server http://localhost:9180
```

### `adc convert`[â](#adc-convert "Direct link to adc-convert")

Convert API specification to ADC configuration.

| Option    | Default Value | Description                                            | Valid Values | Env Variable |
| --------- | ------------- | ------------------------------------------------------ | ------------ | ------------ |
| `openapi` |               | Convert an OpenAPI specification to ADC configuration. |              |              |

#### Sample Usage[â](#sample-usage-5 "Direct link to Sample Usage")

```
adc convert openapi -f open-api-spec.yaml -o adc.yaml
```

### `adc help`[â](#adc-help "Direct link to adc-help")

Print the general help menu or the help menu for the specified command.

#### Sample Usage[â](#sample-usage-6 "Direct link to Sample Usage")

```
adc help [command]
```
