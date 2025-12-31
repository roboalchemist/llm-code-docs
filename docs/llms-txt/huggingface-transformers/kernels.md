# Source: https://huggingface.co/docs/transformers/v5.0.0rc1/main_classes/kernels.md

## Kernels

This page documents the kernels configuration utilities.

### KernelConfig[[transformers.KernelConfig]]

#### transformers.KernelConfig[[transformers.KernelConfig]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/utils/kernel_config.py#L74)

Kernel configuration class. This class is used to configure the kernel mapping for a model.

create_compatible_mappingtransformers.KernelConfig.create_compatible_mappinghttps://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/utils/kernel_config.py#L168[{"name": "model", "val": ""}, {"name": "compile", "val": " = False"}]

Transforms a simple kernel_mapping of the form:
{
"RMSNorm":
"kernels-community/layer_norm:LlamaRMSNorm",
...
},

or

{
"RMSNorm": {
"cuda":
"kernels-community/layer_norm:LlamaRMSNorm",
"rocm":
"kernels-community/layer_norm:LlamaRMSNorm",
...
},
...
}

into a nested mapping:

{
"RMSNorm": {
"cuda": {
Mode.INFERENCE: LayerRepository(
repo_id="kernels-community/layer_norm",
layer_name="LlamaRMSNorm",
)
}
}
}

that's compatible with the kernels library.

The device is inferred from the model's parameters if not provided.
The Mode is inferred from the model's training state.
#### sanitize_kernel_mapping[[transformers.KernelConfig.sanitize_kernel_mapping]]

[Source](https://github.com/huggingface/transformers/blob/v5.0.0rc1/src/transformers/utils/kernel_config.py#L101)

Validates the kernel_mapping to ensure that:
1. Each layer_name in the mapping is registered in the model (i.e., the model contains a module with a matching kernel_layer_name).
2. Each kernel value is either a string of the form 'org/repo:layer_name' or a dict mapping device types ("cuda", "rocm", "xpu", "npu") to such strings.
3. Each device key in a dict is one of "cuda", "rocm", "xpu", or "npu".
4. Each repo_name is a valid repository and layer name in the format 'org/repo:layer_name' (i.e., a string containing both a slash and a colon).

**Parameters:**

model : The model instance whose modules are checked for registered kernel_layer_name attributes.

