# Source: https://docs.vllm.ai/en/stable/design/lora_resolver_plugins/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/design/lora_resolver_plugins.md "Edit this page")

# LoRA Resolver Plugins[¶](#lora-resolver-plugins "Permanent link")

This directory contains vLLM\'s LoRA resolver plugins built on the `LoRAResolver` framework. They automatically discover and load LoRA adapters from a specified local storage path, eliminating the need for manual configuration or server restarts.

## Overview[¶](#overview "Permanent link")

LoRA Resolver Plugins provide a flexible way to dynamically load LoRA adapters at runtime. When vLLM receives a request for a LoRA adapter that hasn\'t been loaded yet, the resolver plugins will attempt to locate and load the adapter from their configured storage locations. This enables:

-   **Dynamic LoRA Loading**: Load adapters on-demand without server restarts
-   **Multiple Storage Backends**: Support for filesystem, S3, and custom backends. The built-in `lora_filesystem_resolver` requires a local storage path, but custom resolvers can be implemented to fetch from any source.
-   **Automatic Discovery**: Seamless integration with existing LoRA workflows
-   **Scalable Deployment**: Centralized adapter management across multiple vLLM instances

## Prerequisites[¶](#prerequisites "Permanent link")

Before using LoRA Resolver Plugins, ensure the following environment variables are configured:

### Required Environment Variables[¶](#required-environment-variables "Permanent link")

1.  **`VLLM_ALLOW_RUNTIME_LORA_UPDATING`**: Must be set to `true` or `1` to enable dynamic LoRA loading

    ::: 
        export VLLM_ALLOW_RUNTIME_LORA_UPDATING=true
    :::

2.  **`VLLM_PLUGINS`**: Must include the desired resolver plugins (comma-separated list)

    ::: 
        export VLLM_PLUGINS=lora_filesystem_resolver
    :::

3.  **`VLLM_LORA_RESOLVER_CACHE_DIR`**: Must be set to a valid directory path for filesystem resolver

    ::: 
        export VLLM_LORA_RESOLVER_CACHE_DIR=/path/to/lora/adapters
    :::

### Optional Environment Variables[¶](#optional-environment-variables "Permanent link")

-   **`VLLM_PLUGINS`**: If not set, all available plugins will be loaded. If set to empty string, no plugins will be loaded.

## Available Resolvers[¶](#available-resolvers "Permanent link")

### lora_filesystem_resolver[¶](#lora_filesystem_resolver "Permanent link")

The filesystem resolver is installed with vLLM by default and enables loading LoRA adapters from a local directory structure.

#### Setup Steps[¶](#setup-steps "Permanent link")

1.  **Create the LoRA adapter storage directory**:

    ::: 
        mkdir -p /path/to/lora/adapters
    :::

2.  **Set environment variables**:

    ::: 
        export VLLM_ALLOW_RUNTIME_LORA_UPDATING=true
        export VLLM_PLUGINS=lora_filesystem_resolver
        export VLLM_LORA_RESOLVER_CACHE_DIR=/path/to/lora/adapters
    :::

3.  **Start vLLM server**: Your base model can be `meta-llama/Llama-2-7b-hf`. Please make sure you set up the Hugging Face token in your env var `export HF_TOKEN=xxx235`.

    ::: 
        python -m vllm.entrypoints.openai.api_server \
            --model your-base-model \
            --enable-lora
    :::

#### Directory Structure Requirements[¶](#directory-structure-requirements "Permanent link")

The filesystem resolver expects LoRA adapters to be organized in the following structure:

    /path/to/lora/adapters/
    ├── adapter1/
    │   ├── adapter_config.json
    │   ├── adapter_model.bin
    │   └── tokenizer files (if applicable)
    ├── adapter2/
    │   ├── adapter_config.json
    │   ├── adapter_model.bin
    │   └── tokenizer files (if applicable)
    └── ...

Each adapter directory must contain:

-   **`adapter_config.json`**: Required configuration file with the following structure:

    ::: 
        
    :::

-   **`adapter_model.bin`**: The LoRA adapter weights file

#### Usage Example[¶](#usage-example "Permanent link")

1.  **Prepare your LoRA adapter**:

    ::: 
        # Assuming you have a LoRA adapter in /tmp/my_lora_adapter
        cp -r /tmp/my_lora_adapter /path/to/lora/adapters/my_sql_adapter
    :::

2.  **Verify the directory structure**:

    ::: 
        ls -la /path/to/lora/adapters/my_sql_adapter/
        # Should show: adapter_config.json, adapter_model.bin, etc.
    :::

3.  **Make a request using the adapter**:

    ::: 
        curl http://localhost:8000/v1/completions \
            -H "Content-Type: application/json" \
            -d ''
    :::

#### How It Works[¶](#how-it-works "Permanent link")

1.  When vLLM receives a request for a LoRA adapter named `my_sql_adapter`
2.  The filesystem resolver checks if `/path/to/lora/adapters/my_sql_adapter/` exists
3.  If found, it validates the `adapter_config.json` file
4.  If the configuration matches the base model and is valid, the adapter is loaded
5.  The request is processed normally with the newly loaded adapter
6.  The adapter remains available for future requests

## Advanced Configuration[¶](#advanced-configuration "Permanent link")

### Multiple Resolvers[¶](#multiple-resolvers "Permanent link")

You can configure multiple resolver plugins to load adapters from different sources:

\'lora_s3_resolver\' is an example of a custom resolver you would need to implement

    export VLLM_PLUGINS=lora_filesystem_resolver,lora_s3_resolver

All listed resolvers are enabled; at request time, vLLM tries them in order until one succeeds.

### Custom Resolver Implementation[¶](#custom-resolver-implementation "Permanent link")

To implement your own resolver plugin:

1.  **Create a new resolver class**:

    ::: 
        from vllm.lora.resolver import LoRAResolver, LoRAResolverRegistry
        from vllm.lora.request import LoRARequest

        class CustomResolver(LoRAResolver):
            async def resolve_lora(self, base_model_name: str, lora_name: str) -> Optional[LoRARequest]:
                # Your custom resolution logic here
                pass
    :::

2.  **Register the resolver**:

    ::: 
        def register_custom_resolver():
            resolver = CustomResolver()
            LoRAResolverRegistry.register_resolver("Custom Resolver", resolver)
    :::

## Troubleshooting[¶](#troubleshooting "Permanent link")

### Common Issues[¶](#common-issues "Permanent link")

1.  **\"VLLM_LORA_RESOLVER_CACHE_DIR must be set to a valid directory\"**

2.  Ensure the directory exists and is accessible

3.  Check file permissions on the directory

4.  **\"LoRA adapter not found\"**

5.  Verify the adapter directory name matches the requested model name

6.  Check that `adapter_config.json` exists and is valid JSON

7.  Ensure `adapter_model.bin` exists in the directory

8.  **\"Invalid adapter configuration\"**

9.  Verify `peft_type` is set to \"LORA\"

10. Check that `base_model_name_or_path` matches your base model

11. Ensure `target_modules` is properly configured

12. **\"LoRA rank exceeds maximum\"**

13. Check that `r` value in `adapter_config.json` doesn\'t exceed `max_lora_rank` setting

### Debugging Tips[¶](#debugging-tips "Permanent link")

1.  **Enable debug logging**:

    ::: 
        export VLLM_LOGGING_LEVEL=DEBUG
    :::

2.  **Verify environment variables**:

    ::: 
        echo $VLLM_ALLOW_RUNTIME_LORA_UPDATING
        echo $VLLM_PLUGINS
        echo $VLLM_LORA_RESOLVER_CACHE_DIR
    :::

3.  **Test adapter configuration**:

    ::: 
        python -c "
        import json
        with open('/path/to/lora/adapters/my_adapter/adapter_config.json') as f:
            config = json.load(f)
        print('Config valid:', config)
        "
    :::

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [November 14, 2025] ]