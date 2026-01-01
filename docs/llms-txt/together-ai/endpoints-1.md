# Source: https://docs.together.ai/reference/endpoints-1.md

# Endpoints

> Create, update and delete endpoints via the CLI

## Create

Create a new dedicated inference endpoint.

### Usage

```sh Shell theme={null}
together endpoints create [MODEL] [GPU] [OPTIONS]
```

### Example

```sh Shell theme={null}
together endpoints create \
--model mistralai/Mixtral-8x7B-Instruct-v0.1 \
--gpu h100 \
--gpu-count 2 \
--display-name "My Endpoint" \
--wait
```

### Options

| Options                                             | Description                                                      |
| --------------------------------------------------- | ---------------------------------------------------------------- |
| `--model`- TEXT                                     | (required) The model to deploy                                   |
| `--gpu` \[ h100 \| a100 \| l40 \| l40s \| rtx-6000] | (required) GPU type to use for inference                         |
| `--min-replicas`- INTEGER                           | Minimum number of replicas to deploy                             |
| `--max-replicas`- INTEGER                           | Maximum number of replicas to deploy                             |
| `--gpu-count` - INTEGER                             | Number of GPUs to use per replica                                |
| `--display-name`- TEXT                              | A human-readable name for the endpoint                           |
| `--no-prompt-cache`                                 | Disable the prompt cache for this endpoint                       |
| `--no-speculative-decoding`                         | Disable speculative decoding for this endpoint                   |
| `--no-auto-start`                                   | Create the endpoint in STOPPED state instead of auto-starting it |
| `--wait`                                            | Wait for the endpoint to be ready after creation                 |

## Hardware

List all the hardware options, optionally filtered by model.

### Usage

```sh Shell theme={null}
together endpoints hardware [OPTIONS]
```

### Example

```sh Shell theme={null}
together endpoints hardware --model mistralai/Mixtral-8x7B-Instruct-v0.1
```

### Options

| Options         | Description                                                                    |
| --------------- | ------------------------------------------------------------------------------ |
| `--model`- TEXT | Filter hardware options by model                                               |
| `--json`        | Print output in JSON format                                                    |
| `--available`   | Print only available hardware options (can only be used if model is passed in) |

## Get

Print details for a specific endpoint.

### Usage

```sh Shell theme={null}
together endpoints get [OPTIONS]
```

### Example

```sh Shell theme={null}
together endpoints get endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462
```

### Options

| Options  | Description                 |
| -------- | --------------------------- |
| `--json` | Print output in JSON format |

## Update

Update an existing endpoint by listing the changes followed by the endpoint ID.

You can find the endpoint ID by listing your dedicated endpoints.

### Usage

```sh Shell theme={null}
together endpoints update [OPTIONS] ENDPOINT_ID
```

### Example

```sh Shell theme={null}
together endpoints update --min-replicas 2 --max-replicas 4 endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462
```

### Options

Note: Both `--min-replicas` and `--max-replicas` must be specified together

| Options                    | Description                                   |
| -------------------------- | --------------------------------------------- |
| `--display-name` - TEXT    | A new human-readable name for the endpoint    |
| `--min-replicas` - INTEGER | New minimum number of replicas to maintain    |
| `--max-replicas` - INTEGER | New maximum number of replicas to scale up to |

## Start

Start a dedicated inference endpoint.

### Usage

```sh Shell theme={null}
together endpoints start [OPTIONS] ENDPOINT_ID
```

### Example

```sh Shell theme={null}
together endpoints start endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462
```

### Options

| Options  | Description                    |
| -------- | ------------------------------ |
| `--wait` | Wait for the endpoint to start |

## Stop

Stop a dedicated inference endpoint.

### Usage

```sh Shell theme={null}
together endpoints stop [OPTIONS] ENDPOINT_ID
```

### Example

```sh Shell theme={null}
together endpoints stop endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462
```

### Options

| Options  | Description                   |
| -------- | ----------------------------- |
| `--wait` | Wait for the endpoint to stop |

## Update

### Usage

Update an existing endpoint by listing the changes followed by the endpoint ID.

You can find the endpoint ID by listing your dedicated endpoints

```sh Shell theme={null}
together endpoints update [OPTIONS] ENDPOINT_ID
```

### Example

```sh Shell theme={null}
together endpoints update --min-replicas 2 --max-replicas 4 endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462
```

### Options

Note: Both `--min-replicas` and `--max-replicas` must be specified together

| Options                    | Description                                   |
| -------------------------- | --------------------------------------------- |
| `--display-name` - TEXT    | A new human-readable name for the endpoint    |
| `--min-replicas` - INTEGER | New minimum number of replicas to maintain    |
| `--max-replicas` - INTEGER | New maximum number of replicas to scale up to |

## Delete

Delete a dedicated inference endpoint.

### Usage

```sh Shell theme={null}
together endpoints delete [OPTIONS] ENDPOINT_ID
```

### Example

```sh Shell theme={null}
together endpoints delete endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462
```

## List

### Usage

```sh Shell theme={null}
together endpoints list [FLAGS]
```

### Example

```sh Shell theme={null}
together endpoints list --type dedicated
```

### Options

| Options                           | Description                 |
| --------------------------------- | --------------------------- |
| `--json`                          | Print output in JSON format |
| `type` \[dedicated \| serverless] | Filter by endpoint type     |

## Help

See all commands with

```sh Shell theme={null}
together endpoints --help
```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt