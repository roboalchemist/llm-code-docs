# Source: https://docs.together.ai/reference/cli/endpoints.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Endpoints

> Create, update and delete endpoints via the CLI

## Setup

See our [Getting Started](/reference/cli/getting-started) guide for initial setup.

## Endpoint ID

Many commands require an `ENDPOINT_ID` to identify which endpoint to operate on. The endpoint ID is a unique identifier assigned when an endpoint is created, in the format:

```
endpoint-<uuid>
```

For example: `endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462`

<Note>
  The endpoint ID is different from the model name (e.g., `mistralai/Mixtral-8x7B-Instruct-v0.1`) or the display name you set with `--display-name`.
</Note>

### How to find your endpoint ID

You can find your endpoint ID in the following ways:

1. **From the create command output**: The endpoint ID is returned when you create an endpoint.

2. **Using the list command**: Run `together endpoints list --mine` to see all your endpoints with their IDs.

3. **From the web interface**: The endpoint ID is shown in the endpoint details page on the [Together AI console](https://api.together.ai/endpoints).

## Create

Create a new dedicated inference endpoint.

### Usage

```sh Shell theme={null}
together endpoints create \
  --model mistralai/Mixtral-8x7B-Instruct-v0.1 \
  --hardware 4x_nvidia_h100_80gb_sxm \
  --display-name "My Endpoint" \
  --wait
```

### Options

| Options                     | Argument                                | Description                                                      |
| --------------------------- | --------------------------------------- | ---------------------------------------------------------------- |
| `--model`                   | string                                  | (**required**) The model to deploy                               |
| `--hardware`                | string                                  | (**required**) GPU type to use for inference                     |
| `--min-replicas`            | number                                  | Minimum number of replicas to deploy                             |
| `--max-replicas`            | number                                  | Maximum number of replicas to deploy                             |
| `--display-name`            | string                                  | A human-readable name for the endpoint                           |
| `--no-auto-start`           |                                         | Create the endpoint in STOPPED state instead of auto-starting it |
| `--no-speculative-decoding` |                                         | Disable speculative decoding for this endpoint                   |
| `--availability-zone`       | `together endpoints availability-zones` | Start endpoint in specified availability zone                    |
| `--wait`                    |                                         | Wait for the endpoint to be ready after creation                 |
| `--json`                    |                                         | Outputs in JSON                                                  |

## Hardware

List all the hardware options, optionally filtered by model.

### Usage

<CodeGroup>
  ```sh Usage theme={null}
  together endpoints hardware [OPTIONS]
  ```

  ```sh Filter by Model theme={null}
  # Only returns hardware for this model
  together endpoints hardware \
    --model mistralai/Mixtral-8x7B-Instruct-v0.1
  ```

  ```sh Available theme={null}
  # Only returns hardware for this model that is currently available
  together endpoints hardware \
    --model mistralai/Mixtral-8x7B-Instruct-v0.1 \
    --available
  ```

  ```sh JSON theme={null}
  # Get the id of the first usable option for a given model
  # You could pass this directly to an endpoint create call.
  HARDWARE_ID = together endpoints hardware \
    --model mistralai/Mixtral-8x7B-Instruct-v0.1 \
    --available \
    --json | jq '.[0].id' 

  # HARDWARE_ID == "2x_nvidia_h100_80gb_sxm"
  ```
</CodeGroup>

### Options

| Options       | Argument | Description                                                                    |
| ------------- | -------- | ------------------------------------------------------------------------------ |
| `--model`     | TEXT     | Filter hardware options by model                                               |
| `--json`      |          | Print output in JSON format                                                    |
| `--available` |          | Print only available hardware options (can only be used if model is passed in) |

## Retrieve

Print details for a specific endpoint.

### Usage

```sh Shell theme={null}
together endpoints retrieve endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462
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
together endpoints stop endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462
```

### Options

| Options  | Description                   |
| -------- | ----------------------------- |
| `--wait` | Wait for the endpoint to stop |

## Delete

Delete a dedicated inference endpoint.

### Usage

```sh Shell theme={null}
together endpoints delete endpoint-c2a48674-9ec7-45b3-ac30-0f25f2ad9462
```

## List

### Usage

```sh Shell theme={null}
together endpoints list --type dedicated
```

### Options

| Options                           | Description                 |
| --------------------------------- | --------------------------- |
| `--json`                          | Print output in JSON format |
| `type` \[dedicated \| serverless] | Filter by endpoint type     |


Built with [Mintlify](https://mintlify.com).