# Source: https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html

Title: Run Inference Using FP8 — Gaudi Documentation 1.23.0 documentation

URL Source: https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html

Published Time: Tue, 27 Jan 2026 14:00:21 GMT

Markdown Content:
Run Inference Using FP8[¶](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#run-inference-using-fp8 "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This guide provides the steps required to enable FP8 inference on your Intel® Gaudi® 2 and Intel® Gaudi® 3 AI accelerator.

Using FP8 data type for inference on large language models halves the required memory bandwidth compared to BF16. In addition, FP8 compute is twice as fast as BF16 compute, so even compute-bound workloads, such as offline inference on large batch sizes, benefit.

To see an example of FP8 inference with Hugging Face, refer to the Hugging Face [text-generation example](https://github.com/huggingface/optimum-habana/tree/main/examples/text-generation#running-with-fp8). Follow the full instructions to set up the Optimum for Intel Gaudi library and text-generation.

Note

Typical LLMs such as Llama2-70b, Llama2-7b, Llama3-70b, Llama3-8b, Mixtral-8x7B, Falcon-7B, Falcon-40B, Falcon-180B and Phi-2 have been validated with FP8 using the INC.

The [Intel® Neural Compressor (INC)](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/index.html#quantization-prerequisites) performs model measurement and quantization for FP8 in PyTorch models with Gaudi. It provides these capabilities for models that include the modules listed in [Supported Modules](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#supported-modules).

To enable and run INC with Gaudi:

*   Modify your model script. For examples, refer to [Enabling and Running INC in PyTorch Models](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#enabling-and-running-inc-pt-models) section below.

*   Run INC in measurement mode to measure statistics and calculate scales based on the measurements.

*   Run INC in quantization mode to automatically quantize the model to FP8 where possible.

Note

INC also supports DeepSpeed models.

Measurement and Quantization Mechanisms[¶](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#measurement-and-quantization-mechanisms "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

INC measures statistics, calculates scales based on the measurements, and quantizes the model to FP8 where possible. It supports both measurement and quantization modes using the `prepare` and `convert` APIs:

### Measurement Mode[¶](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#measurement-mode "Permalink to this headline")

In this mode, INC collects statistics on the data flowing through the model by replacing [Supported Modules](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#supported-modules) before the model is run on the dataset. It records data such as the maximum absolute value (max abs) and stores this information in a file.

The primary purpose of this mode is to gather and save data statistics needed for static quantization.

### Quantization Mode[¶](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#quantization-mode "Permalink to this headline")

INC supports two quantization approaches: **static** and **dynamic**.

#### Static Quantization[¶](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#static-quantization "Permalink to this headline")

After collecting measurements, the model can be statically quantized to FP8. This process involves:

*   Loading the measurement file.

*   Calculating the scale of each tensor from its measurement.

*   Injecting scale and cast operations into the model around selected operations to enable FP8 execution.

This transforms the model to efficiently run using the FP8 data type, offering significant performance improvements.

#### Dynamic Quantization[¶](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#dynamic-quantization "Permalink to this headline")

Dynamic quantization does not require prior measurement. Instead, quantization parameters (e.g., scales) are computed at runtime per token, based on the input data.

This method is lightweight and flexible but may deliver more modest performance gains compared to static quantization.

Note

Currently, dynamic quantization only applies to linear layers, while the rest of the model runs in BF16.

Enabling and Running INC in PyTorch Models[¶](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#enabling-and-running-inc-in-pytorch-models "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

See the [LlaMA 2 model](https://github.com/huggingface/optimum-habana/tree/main/examples/text-generation#running-with-fp8) for an example model quantization using INC. To run INC with your own pytorch model scripts, follow the steps below:

1.   Call `hpu_set_env()` to enable inference optimizations:

> import habana_frameworks.torch.core as htcore
> htcore.hpu_set_env()
> 
> [![Image 1: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html)

2.   Call `import FP8Config, convert, prepare` after loading the model to set up INC. The `prepare` API prepares the model for measurement by replacing `nn.Modules` while the `convert` API quantizes the model. Load the [INC JSON config](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#json-options) by passing the path to `FP8Config.from_json_file(args.config_file_path)`:

> from neural_compressor.torch.quantization import FP8Config, convert, prepare
> config = FP8Config.from_json_file(args.config_file_path)
> if config.measure:
>     model = prepare(model, config)
> elif config.quantize:
>     model = convert(model, config)
> 
> [![Image 2: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html) Note
> 
> 
> You should add code to parse the `--config_file_path` flag in your script and pass it to `from_json_file(args.config_file_path)` as shown above. The `QUANT_CONFIG` environment variable is no longer supported for loading the JSON config file, unless you parse it in your script and pass it to the `from_json_file` function. 
> If DeepSpeed is used, INC should be called after `deepspeed.init_inference`. The below shows a full initialization with DeepSpeed example:
> 
> import habana_frameworks.torch.core as htcore
> htcore.hpu_set_env()
> 
> model = deepspeed.init_inference(model, **ds_inference_kwargs)
> model = model.module
> 
> from neural_compressor.torch.quantization import FP8Config, convert, prepare
> config = FP8Config.from_json_file(args.config_file_path)
> if config.measure:
>     model = prepare(model, config)
> elif config.quantize:
>     model = convert(model, config)
> 
> [![Image 3: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html)

3.   The below call is also required in any inference scenario. It enables passing scales as constants to the Intel Gaudi software to allow compile-time optimizations:

> htcore.hpu_initialize(model, mark_scales=True, mark_non_scales=False)
> 
> [![Image 4: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html)

4.   At the end of the run, call `finalize_calibration` which saves the measurements to file. This call does not affect quantization mode:

> from neural_compressor.torch.quantization import finalize_calibration
> finalize_calibration(model)
> 
> [![Image 5: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html)

### Running INC in Measurement Mode[¶](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#running-inc-in-measurement-mode "Permalink to this headline")

1.   Create a config JSON file for measurement. The JSON is loaded by INC. Refer to [Supported JSON Config File Options](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#json-options) for more information. Use the following JSON example:

> {
>     "mode": "MEASURE",
>     "observer": "maxabs",
>     "dump_stats_path": "./inc_output/measure"
> }
> 
> [![Image 6: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html)

2.   Run measurement on your model with the JSON file path in the model run command:

> <model run command> --config_file_path <path to json file>
> 
> [![Image 7: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html)

### Running INC in Quantization Mode[¶](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#running-inc-in-quantization-mode "Permalink to this headline")

1.   Create a config JSON file for quantization. The JSON file is loaded by INC. Refer to [Supported JSON Config File Options](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#json-options) for more information. Note that the `dump_stats_path` attribute should have the same path used in the measurement JSON file. Use the following JSON example for per-tensor quantization:

> {
>     "mode": "QUANTIZE",
>     "observer": "maxabs",
>     "scale_method": "maxabs_hw",
>     "blocklist": {"types": [], "names":  ["lm_head"]},
>     "dump_stats_path": "./inc_output/measure"
> }
> 
> [![Image 8: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html) 
> Alternatively, use this JSON example for weights-per-channel, activations-per-tensor quantization:
> 
> {
>     "mode": "QUANTIZE",
>     "observer": "maxabs",
>     "scale_method": "ACT_MAXABS_POW2_WEIGHTS_PCS_OPT_POW2",
>     "dump_stats_path": "./inc_output/measure"
> }
> 
> [![Image 9: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html) 
> For dynamic quantization, use the following JSON example:
> 
> {
>     "mode": "QUANTIZE",
>     "observer": "maxabs",
>     "scale_format": "CONST",
>     "scale_method": "act_maxabs_pcs_pow2_weight_maxabs_pts_pow2_hw",
>     "dynamic_quantization": true,
>     "dump_stats_path": ""
> }
> 
> [![Image 10: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html)

2.   Run your quantized model with the path to the JSON file in the model run command.

`PT_HPU_WEIGHT_SHARING=0` is required to free the full precision weights from the device and ensure only the FP8 weights are stored:

> PT_HPU_WEIGHT_SHARING=0 <model run command> --config_file_path <path to json file>
> 
> [![Image 11: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html)

3.   Set the `LOG_LEVEL_INC=1` environment variable to print the status of the patched modules which INC replaced, in addition to more debug prints. Search for “Patched modules” in the printed output.

Supported Modules[¶](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#supported-modules "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`Linear nn.Module` is supported and replaced by INC during quantization. In DeepSpeed, `LinearAllreduce`, `LinearLayer`, and `LmHeadLinearAllreduce` modules are supported. In Transformers, `FalconLinear` is supported. In diffusers, `LoRACompatibleLinear` and `LoRACompatibleConv` modules are supported partially. They can be applied in quantization only when their `lora_layer` member is not used. In case your model contains those modules with `lora_layer` used, add them to `blocklist` field in the [json config file](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#json-options).

Note

> Supported modules should be wrapped in a top level module `nn.Module`:

class Model(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        return nn.Linear(*args, **kwargs)

[![Image 12: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html)

### Supported Functions[¶](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#supported-functions "Permalink to this headline")

In addition to the above supported modules, `torch.matmul` and `torch.nn.functional.softmax` are supported and replaced by INC during quantization. You can simply wrap each function with an `nn.module`. See the below example:

class Matmul(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *args, **kwargs):
        return torch.matmul(*args, **kwargs)

[![Image 13: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html)

`torch.nn.functional.scaled_dot_product_attention()` is also supported and can be replaced during quantization. You can simply wrap each function with `ModuleFusedSDPA(torch.nn.Module)`. See [ModuleFusedSDPA](https://github.com/HabanaAI/optimum-habana-fork/blob/8f996eb20f300c48fc005df2e9eb3be9354a518e/optimum/habana/transformers/models/llama/modeling_llama.py#L111) for code usage example.

Note

For FusedSDPA:

*   Recompute mode should be enabled as detailed in [hpex/kernels/FusedSDPA](https://docs.habana.ai/en/latest/PyTorch/Reference/Python_Packages.html#fusedsdpa-section).

*   In the quantization JSON config file, the supported scale method is `maxabs_hw`. For more details, see [Supported JSON Config File Options](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#json-options).

### Custom Patched Modules[¶](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#custom-patched-modules "Permalink to this headline")

Custom modules were added to topologies and corresponding quantized modules to INC allowing quantization of more code in the user script, for example in the [LlaMA 2 model](https://github.com/huggingface/optimum-habana/tree/main/examples/text-generation#running-with-fp8). The following replaces the existing code: [KVCache](https://github.com/huggingface/optimum-habana/blob/dd3cc08937a85175eafd3b511484c86fed889b79/optimum/habana/transformers/models/llama/modeling_llama.py#L221) and [ScopedLinearAllReduce](https://github.com/huggingface/optimum-habana/blob/dd3cc08937a85175eafd3b511484c86fed889b79/optimum/habana/transformers/models/modeling_all_models.py#L150).

### Supported JSON Config File Options[¶](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#supported-json-config-file-options "Permalink to this headline")

The following table summarizes the options for the JSON config file:

| Attribute | Description | Values |
| --- | --- | --- |
| Mode | The mode, measure or quantize, to run INC with. | * MEASURE - Measure statistics of all modules and emit the results to `dump_stats_path`. * QUANTIZE (default) - Quantize and run the model according to the provided measurements. |
| Observer | The observer to measure the statistics. | * maxabs (default) * save - Saves all tensors to files. |
| Allowlist | List of nn.Module names or types to quantize. When setting an empty list, all the supported modules will be quantized by default. See [Supported Modules](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#supported-modules). | Default = empty list |
| Blocklist | List of nn.Module names or types not to quantize. Defaults to empty list, so you may omit it from the config file. | Default = empty list |
| dump_stats_path | The path to save and load the measurements. The path is created up until the level before last “/”. The string after the last / will be used as prefix to all the measurement files that will be created. | Default = stats |
| scale_method | The method for calculating the scale from the measurement. | * `unit_scale` (default) - Always use scale of 1. * `maxabs_arbitrary` - Scale is calculated to stretch/compress the maxabs measurement to the full-scale of FP8. * `maxabs_hw` - Scale is calculated to stretch/compress the maxabs measurement to the full-scale of FP8 and then replace it by an appropriate HW accelerated scale. `device_for_scales` parameter determines the possible exponent-bias values. These values are automatically used instead of their corresponding scales to optimize timing. * `maxabs_pow2` - Scale is calculated to stretch/compress the maxabs measurement to the full-scale of FP8 and then rounded to the power of 2. * `maxabs_hw_opt_weight` - Scale of model params (weights) is chosen as the scale that provides minimal mean-square-error between quantized and non-quantized weights, from all possible HW accelerated scales. Scale of activations is calculated the same as `maxabs_hw`. * `act_maxabs_pow2_weights_pcs_opt_pow2` - Scale of model params (weights) is calculated per-channel of the params tensor. The scale per-channel is calculated the same as `maxabs_hw_opt_weight`. Scale of activations is calculated the same as `maxabs_pow2`. * `act_maxabs_hw_weights_pcs_maxabs_pow2` - Scale of model params (weights) is calculated per-channel of the params tensor. The scale per-channel is calculated the same as `maxabs_pow2`. Scale of activations is calculated the same as `maxabs_hw`. * `act_maxabs_pcs_pow2_weight_maxabs_pts_pow2_hw` - Dynamic quantization only. Scale of model params (weights) is calculated per-tensor the same as `maxabs_hw`. Scale of activations is calculated dynamically per-token with the same method as `maxabs_pow2`. |
| measure_exclude | If this attribute is not defined, the default is `OUTPUT`. Since most models do not require measuring output tensors, you can exclude it to speed up the measurement process. | * `NONE` - All tensors are measured. * `OUTPUT` (default) - Excludes measurement of output tensors. |
| scale_format | The format of scales passed to custom PyTorch ops for quantization (such as `torch.ops.hpu.fp8_gemm_v2`). The default is `scalar`. | * `const` - Scales passed as tensors. * `scalar` - Scales passed as scalar values. This format enables compile time and throughput optimizations. See [Compile Time and Throughput Optimization](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#compile-time-and-throughput-optimization). |
| device_for_scales | Set the exponent-bias values of the device, that may be chosen in converting a high-precision tensor (FP32 or BF16) to FP8-143 tensor. By default, the parameter value is set to the device in use. This parameter is used exclusively for the `maxabs_hw` scale method. | * `GAUDI3` - In Gaudi 3, the exponent-bias range is expanded to (0, 63) to enhance accuracy. * `GAUDI2` - In Gaudi 2 there are 4 possible exponent-bias values (3, 7, 11, 15), where 7 is the default exponent bias. This option is utilized in the Gaudi 3 device to minimize compilation time by decreasing the number of distinct graphs created. |
| dynamic_quantization | Set to `true` to enable dynamic quantization, which allows the model to run in FP8 with dynamic scales per token. By default, the parameter value is set to `false`. Dynamic quantization is only supported in scale method `act_maxabs_pcs_pow2_weight_maxabs_pts_pow2_hw`. | * `true` - Enables dynamic quantization. * `false` (default) - Disables dynamic quantization. |

### Configuring Backoff Factors[¶](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#configuring-backoff-factors "Permalink to this headline")

The maxabs measurement based scaling methods support configuring backoff factors `input_backoff` and `weight_backoff` to leave some margin in the conversion of inputs and weights to FP8, respectively. For example, to account for a case where an activation with a larger absolute value than in the calibration dataset is encountered. The maxabs measured value of an activation is scaled to `input_backoff*FP8_143_FULLSCALE`. Similarly, the maxabs value of a weight is scaled to `weight_backoff*FP8_143_FULLSCALE`. The default values are `input_backoff=0.25` and `weight_backoff=0.5`. To change these values, add the following to the quantization configuration JSON file:

"scale_params": {"input_backoff": <INPUT_BACKOFF>, "weight_backoff": <WEIGHT_BACKOFF>},

[![Image 14: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html)

### Compile Time and Throughput Optimization[¶](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#compile-time-and-throughput-optimization "Permalink to this headline")

The `"scale_format": "scalar"` configuration setting activates the below optimizations:

*   Improves overall compile time in FP8 inference by reducing the number of recipes compiled.

*   Reduces host time spent on launch logic in FP8. This optimization improves throughput when device time is host bound (for example if batch size is low).

Note

*   Improving overall compile time depends on model properties such as the number of compiled recipes and the distribution of scale values.

*   This mode is not relevant for PCQ.

### Running Quantized Models on a Small Amount of Cards[¶](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#running-quantized-models-on-a-small-amount-of-cards "Permalink to this headline")

Due to common memory limitations, large BF16 models do not fit on one Gaudi card, however, using FP8 precision allows large models to fit on one card. Since measurement is calculated in BF16 precision, to be able to run FP8 model on less cards than the amount used during measurement of a BF16 model, you can use the `unify_measurements` script, located in the [Optimum for Intel Gaudi GitHub repository](https://github.com/huggingface/optimum-habana/blob/main/examples/text-generation/quantization_tools/unify_measurements.py). The script unifies the measurements according to the grouping of cards specified.

1.   Measure the model on a number of cards that are enough for the model to fit in BF16.

2.   Run `unify_measurements` script using the measurement files created after running first step. A unified measurement is then calculated:

> python unify_measurements.py -g 01234567 -m *path_to_8x_measurements* -o *path_to_output_1x_measurement*
> 
> [![Image 15: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html) 
> In the above example, the measurements of cards 0-7 will be unified to a single measurement. For example, if you specify `-g 0123 4567`, cards 0-3 and cards 4-7 will be unified in two different measurement files:
> 
> python unify_measurements.py -g 0123 4567 -m *path_to_8x_measurements* -o *path_to_output_1x_measurement*
> 
> [![Image 16: Copy to clipboard](https://docs.habana.ai/en/latest/_static/copy-button.svg)](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html) 
> All different group combinations are supported. For further details, use `$ unify_measurements.py --help`.

3.   Run quantization as detailed in [Running INC in Quantization Mode](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#id2) using the unified measurement file/s.

Note

If you run the model on more than one card, set `LOCAL_RANK` and `WORLD_SIZE` environment variables properly. The environment variables are already set in DeepSpeed.

### Generating INC Log Files for Gaudi[¶](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#generating-inc-log-files-for-gaudi "Permalink to this headline")

1.   Use the `LOG_LEVEL_INC` environment variable to run INC with logging. The default logging value for INC is Info (2). All log messages with logging value >= 2 are written to the log file.

2.   Set the `HABANA_LOGS` environment variable to `$HOME/.habana_logs` directory. When running on one card, an `inc_log.txt` file is placed under this directory. When running on multiple cards, each card will have its own directory, represented by its number, containing the log file. To print log messages to the screen, set `ENABLE_CONSOLE=true`.

3.   To change the logging value, use the `LOG_LEVEL_INC` environment variable with the desired logging level number, for example: `LOG_LEVEL_INC=3`. The possible logging values with their representative numbers are detailed in [Using Log Levels](https://docs.habana.ai/en/latest/PyTorch/Reference/Debugging_Guide/Debugging_with_Intel_Gaudi_Logs.html#logs-levels). If `LOG_LEVEL_INC` is not set, the `LOG_LEVEL_ALL` environment variable will also generate INC logs.

4.   To disable INC logging, use `LOG_LEVEL_INC=6`.

In case of massive INC logging, more INC log files will be generated once the maximum log file size is reached: `inc_log.txt.1`, `inc_log.txt.2`. The default log file size is 10MB (10 * 1024 * 1024). To change the default, set the size using the `INC_LOG_FILE_SIZE` environment variable. The default amount of backup log files is 5 (total of 6 log files). To change the default, set the amount using the `INC_LOG_FILE_AMOUNT` environment variable. The latest log messages will be shown in the `inc_log.txt` file, while previous log messages will be shown in `inc_log.txt.1` and so on.

Reducing FP8 Warmup Time[¶](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#reducing-fp8-warmup-time "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Runtime Scale Patching[¶](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#runtime-scale-patching "Permalink to this headline")

Warmup time for FP8 models is significantly longer than for BF16 due to additional graph compilations triggered by varying constant scale values in quantized model layers.

FP8 warmup time can be reduced by setting the `RUNTIME_SCALE_PATCHING=1` environment variable and selecting a hardware-aligned per-tensor `scale_method` provided by the [INC JSON config](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#json-options).

Note

*   This is an experimental feature. It reduces FP8 warmup time but may lower model throughput by 5-20%. Future releases will improve performance and extend support to more ops.

*   Supported with Lazy mode (`PT_HPU_LAZY_MODE=1`) and `torch.compile`.

*   Supports Llama workloads using FP8 execution of Linear and FSDPA layers, and casting ops between BF16 and FP8. MoE and Convolution ops are not yet supported.

#### Trivial Scales Optimization[¶](https://docs.habana.ai/en/latest/PyTorch/Inference_on_PyTorch/Quantization/Inference_Using_FP8.html#trivial-scales-optimization "Permalink to this headline")

The `PT_HPU_H2D_TRIVIAL_SCALES_MODE` flag controls trivial scales (i.e. scale value is equal to 1.0) optimization in the `RUNTIME_SCALE_PATCHING` mode. Enabling this optimization can increase warmup and compilation time due to the generation of additional graphs, but may improve runtime performance by reducing the number of multiplication operations.

The following values are supported:

*   `0` - No optimization (default).

*   `1` - Removes scales equal to 1.0 in `cast_to_fp8_v2` and `cast_from_fp8`, disabling the corresponding `mult_fwd` (multiplication) node.

*   `2` - Applies the same optimization as mode `1`, and additionally removes reciprocal scales in `fp8_gemm_v2`.
