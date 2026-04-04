# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/precision.html.md

Title: Migrate Precision Configurations from NeMo 1.0 to NeMo 2.0#

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/precision.html

Published Time: Thu, 30 Oct 2025 07:07:29 GMT

Markdown Content:
In NeMo 2.0, precision configuration has been centralized to the `MegatronMixedPrecision` plugin.

NeMo 1.0 (Previous Release)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/precision.html.md#nemo-1-0-previous-release "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In NeMo 1.0, various model and training precision settings (including FP8 configuration) are spread throughout the YAML configuration file.

trainer:
 precision: bf16
 ...
model:
 native_amp_init_scale: 4294967296
 native_amp_growth_interval: 1000
 ...
 fp8: False # enables fp8 in TransformerLayer forward
 fp8_e4m3: False # sets E4M3 FP8 format
 fp8_hybrid: False # sets hybrid FP8 format
 fp8_margin: 0
 fp8_amax_history_len: 1024
 fp8_amax_compute_algo: max

NeMo 2.0 (New Release)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/precision.html.md#nemo-2-0-new-release "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

In NeMo 2.0, these settings are controlled using the `MegatronMixedPrecision` plugin.

from nemo import lightning as nl

plugin = nl.MegatronMixedPrecision(
    precision="bf16",
    fp16_initial_loss_scale=4294967296,
    fp16_loss_scale_window=1000,
    fp8=None, # Can be either "e4m3" or "hybrid"
    fp8_margin=0,
    fp8_amax_history_len=1024,
    fp8_amax_compute_algo="max",

)

trainer = nl.Trainer(
   plugins=plugin,
   ...
)

Migrate Precision Configurations[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/precision.html.md#migrate-precision-configurations "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.   Locate and remove all [precision](https://github.com/NVIDIA/NeMo/blob/00fe96f01baff193418e3d71e78acf3748907b6e/examples/nlp/language_modeling/conf/megatron_gpt_config.yaml#L11) and [fp8](https://github.com/NVIDIA/NeMo/blob/00fe96f01baff193418e3d71e78acf3748907b6e/examples/nlp/language_modeling/conf/megatron_gpt_config.yaml#L222-L228) configurations in your NeMo 1.0 YAML config file.

2.   Add the following import to your Python script:

from nemo import lightning as nl 
3.   Create a `MegatronMixedPrecision` plugin with the appropriate parameters:

plugin = nl.MegatronMixedPrecision(
    precision="bf16",
    fp16_initial_loss_scale=4294967296,
    fp16_loss_scale_window=1000,
    fp8=None, # Can be either "e4m3" or "hybrid"
    fp8_margin=0,
    fp8_amax_history_len=1024,
    fp8_amax_compute_algo="max",

) 
4.   Adjust the arguments in the plugin to match your previous YAML configuration.

5.   Add the precision plugin to your `Trainer` (see [Trainer migration guide](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/trainer.html.md#migration-trainer)):

trainer = nl.Trainer(
    ...
    plugins=plugin,
    ...
) 

Note

*   TransformerEngine must be installed to use FP8 precision.

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/precision.html.md#migrate-precision-configurations)
- [precision](https://github.com/NVIDIA/NeMo/blob/00fe96f01baff193418e3d71e78acf3748907b6e/examples/nlp/language_modeling/conf/megatron_gpt_config.yaml#L11)
- [fp8](https://github.com/NVIDIA/NeMo/blob/00fe96f01baff193418e3d71e78acf3748907b6e/examples/nlp/language_modeling/conf/megatron_gpt_config.yaml#L222-L228)
- [Trainer migration guide](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemo-2.0/migration/trainer.html.md#migration-trainer)
