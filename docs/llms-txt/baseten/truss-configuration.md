# Source: https://docs.baseten.co/reference/truss-configuration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Truss configuration

> Set your model resources, dependencies, and more

The `config.yaml` file defines how your model runs on Baseten: its dependencies,
compute resources, secrets, and runtime behavior. You specify what your model
needs; Baseten handles the infrastructure.

Every Truss includes a `config.yaml` in its root directory. Configuration is
optional, every value has a sensible default.

Common configuration tasks include:

* [Allocate GPU and memory](#resources): compute resources for your instance.
* [Declare environment variables](#environment-variables): environment variables for your model.
* [Configure concurrency](#runtime): parallel request handling.
* [Use a custom Docker image](#base-image): deploy pre-built inference servers.

<Accordion title="YAML syntax">
  If you're new to YAML, here's a quick primer.
  The default config uses `[]` for empty lists and `{}` for empty dictionaries.
  When adding values, the syntax changes to indented lines:

  ```yaml  theme={"system"}
  # Empty
  requirements: []
  secrets: {}

  # With values
  requirements:
    - torch
    - transformers
  secrets:
    hf_access_token: null
  ```
</Accordion>

## Example

The following example shows a config file for a GPU-accelerated text generation model:

```yaml config.yaml theme={"system"}
model_name: my-llm
description: A text generation model.
requirements:
  - torch
  - transformers
  - accelerate
resources:
  cpu: "4"
  memory: 16Gi
  accelerator: L4
secrets:
  hf_access_token: null
```

For more examples, see the
[truss-examples](https://github.com/basetenlabs/truss-examples) repository.

## Reference

<Snippet file="config-params.mdx" />
