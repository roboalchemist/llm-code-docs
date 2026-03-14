# Source: https://docs.mystic.ai/docs/gpus-and-accelerators.md

# GPUs and accelerators

When it comes time to deploy your Pipeline, there are a few extra infrastructure considerations. The `pipeline.yaml` file provides a way to specify what type of hardware your Pipeline will need to run on (this is usually something like an NVIDIA graphics card).

# Concepts

* Accelerator - The piece of hardware to run with your Pipeline

Specify your hardware requirements in your YAML file like so:

```yaml
accelerators: ["nvidia_a100", "nvidia_a100"]
```

Notice how you can specify multiple GPUs, just make sure your specification is one of the available configurations listed below!

If accelerators is an empty list, it will default to a `"cpu"` configuration.

# Accelerator list

The accelerators that we currently offer are:

| Name                       | Max VRAM |
| :------------------------- | :------- |
| `nvidia_t4`                | 16GB     |
| `nvidia_a100`              | 40GB     |
| `nvidia_a100_5gb`\*        | 5GB      |
| `nvidia_a100_10gb`\*       | 10GB     |
| `nvidia_a100_20gb`\*       | 20GB     |
| `nvidia_a100_80gb`         | 80GB     |
| `nvidia_a100_80gb_40gb` \* | 40GB     |
| `nvidia_a100_80gb_20gb` \* | 20GB     |
| `nvidia_a100_80gb_10gb` \* | 10GB     |
| `nvidia_h100`              | 80GB     |
| `nvidia_l4`                | 24GB     |
| `nvidia_a10` \*\*          | 24GB     |
| `nvidia_a10_12gb` \*\*     | 12GB     |
| `nvidia_a10_8gb` \*\*      | 8GB      |
| `nvidia_a10_4gb` \*\*      | 4GB      |
| `cpu`                      | -        |

*\*Fractional GPU*\
*\*\*BYOC Only*

# Fractional GPUs and GPU sharing

Mystic does offer fractional GPUs! At the moment they're limited to the A100 GPUs but will be supported with H100s in an upcoming release.

Supported fractions:

| Name               | VRAM |
| :----------------- | :--- |
| `nvidia_a100_5gb`  | 5GB  |
| `nvidia_a100_10gb` | 10GB |
| `nvidia_a100_20gb` | 20GB |

You define these as normal in the accelerator field in the `pipeline.yaml` with your project:

```yaml
runtime:
  container_commands:
    ...
  python:
    ...
accelerators: ["nvidia_a100_5gb"]
pipeline_graph: new_pipeline:my_new_pipeline
pipeline_name: paulh/a-cool-model
readme: README.md
...
```

### Fractional pricing

> 👍 No low volume premium for fractional GPUs
>
> There is a completely flat pricing for fractional GPUs, there is not a premium for the first 10 hours!

| Name               | Per second cost | Per hour cost |
| :----------------- | :-------------- | :------------ |
| `nvidia_a100_5gb`  | $0.000119       | $0.429        |
| `nvidia_a100_10gb` | $0.000278       | $1            |
| `nvidia_a100_20gb` | $0.0004165      | $1.5          |

# Catalyst Accelerator configurations

You can configure the above accelerators in any of the configurations below:

| Accelerators          | Per second cost | Per hour cost |
| :-------------------- | :-------------- | :------------ |
| 1x Nvidia T4          | $0.000111       | $0.4          |
| 1x Nvidia A100 (40GB) | $0.000833       | $3            |
| 1x Nvidia A100 (80GB) | $0.001111       | $4            |
| 1x Nvidia L4          | $0.000208       | $0.75         |
| CPU                   | $0.0000278      | $0.10         |