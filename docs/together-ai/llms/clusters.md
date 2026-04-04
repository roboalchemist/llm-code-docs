# Source: https://docs.together.ai/reference/cli/clusters.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Clusters

## Setup

See our [Getting Started](/reference/cli/getting-started) guide for initial setup.

## `clusters create`

```sh Usage theme={null}
together beta clusters create [OPTIONS]
```

**Options**

| Name               | Type                      | Description                                                                                                         |
| ------------------ | ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `--name`           | string                    | Name of the cluster                                                                                                 |
| \`--num-gpus       | number                    | Number of GPUs to allocate in the cluster                                                                           |
| `--region`         | enum                      | Region to create the cluster in. Valid regions can be found with `clusters list-regions`                            |
| `--billing-type`   | `ON_DEMAND` or `RESERVED` | Billing type to use for the cluster                                                                                 |
| `--driver-version` | enum                      | Driver version to use for the cluster. Valid driver versions can be found with `clusters list-regions`              |
| `--duration-days`  | number                    | Only used with `RESERVED` billing                                                                                   |
| `--gpu-type`       | enum                      | GPU type to use for the cluster. Find available gpu types for each region with the `clusters list-regions` command. |
| \`--cluster-type   | `KUBERNETES` or `SLURM`   | Cluster type                                                                                                        |
| `--volume`         | ID                        | Storage volume ID to use for the cluster                                                                            |
| `--json`           |                           | Output in JSON format                                                                                               |

## `clusters update`

```sh Usage theme={null}
together beta clusters update CLUSTER_ID [OPTIONS]
```

**Options**

| Name             | Type                    | Description                               |
| ---------------- | ----------------------- | ----------------------------------------- |
| `--num-gpus`     | number                  | Number of GPUs to allocate in the cluster |
| \`--cluster-type | `KUBERNETES` or `SLURM` | Cluster type                              |
| `--json`         |                         | Output in JSON format                     |

## `clusters retrieve`

```sh Usage theme={null}
together beta clusters retrieve CLUSTER_ID
```

## `clusters delete`

```sh Usage theme={null}
together beta clusters delete CLUSTER_ID
```

## `clusters list`

```sh Usage theme={null}
together beta clusters list CLUSTER_ID
```

## `clusters list-regions`

Get configuration information per region to use in creating your cluster.

```sh Usage theme={null}
together beta clusters list-regions
```

**Example Output**

```json  theme={null}
{
    "regions": [
        {
            "driver_versions": [
                "CUDA_12_6_565",
                "CUDA_12_5_555",
                "CUDA_12_8_570",
                "CUDA_12_9_575",
                "CUDA_12_6_560",
                "CUDA_12_4_550"
            ],
            "name": "us-central-8",
            "supported_instance_types": [
                "H100_SXM",
                "H200_SXM"
            ]
        },
    ]
}
```

## `clusters get-credentials`

```sh Usage theme={null}
together beta clusters get-credentials CLUSTER_ID [OPTIONS]
```

**Options**

| Name                    | Type        | Description                                                                                                                                    |
| ----------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `--file`                | path or `-` | Path to write the kubeconfig to. If you pass `-` it will print the config to stdout instead of writing to a file.  \[default: \~/.kube/config] |
| `--context-name`        | string      | Name of the context to add to the kubeconfig. By default it will be the cluster name.                                                          |
| `--overwrite-existing`  |             | If there is a conflict with the existing kubeconfig, overwrite the existing kubeconfig instead of raising an error.                            |
| `--set-default-context` |             | Change the current context for kubectl to the new context.                                                                                     |

## `clusters storage create`

```sh Usage theme={null}
together beta clusters storage create [OPTIONS]
```

**Options**

| Name            | Type                  | Description                                         |
| --------------- | --------------------- | --------------------------------------------------- |
| `--region`      | string                | Region to create the storage volume in. \[required] |
| `--size-tib`    | number                | Size of the storage volume in TiB  \[required]      |
| `--volume-name` | string                | Name of the storage volume  \[required]             |
| `--json`        | Output in JSON format |                                                     |

## `clusters storage retrieve`

```sh Usage theme={null}
together beta clusters storage retrieve VOLUME_ID 
```

## `clusters storage list`

```sh Usage theme={null}
together beta clusters storage list 
```

## `clusters storage delete`

```sh Usage theme={null}
together beta clusters storage delete VOLUME_ID
```


Built with [Mintlify](https://mintlify.com).