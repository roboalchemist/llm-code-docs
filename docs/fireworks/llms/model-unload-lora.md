# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/model-unload-lora.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# firectl model unload-lora

> Unloads a LoRA model.

### Usage

Unloads a LoRA model from a dedicated deployment.

```
firectl model unload-lora [flags]
```

### Examples

```
firectl model unload-lora my-lora --deployment abcd1234
```

### Flags

```
      --deployment string       The resource name of the deployment where the model is to be undeployed.
  -h, --help                    help for unload-lora
      --wait                    Wait until the model is deployed.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 30m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
