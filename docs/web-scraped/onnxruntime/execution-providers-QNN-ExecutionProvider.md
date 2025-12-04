# Source: https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#qnn-execution-provider) QNN Execution Provider 

The QNN Execution Provider for ONNX Runtime enables hardware accelerated execution on Qualcomm chipsets. It uses the Qualcomm AI Engine Direct SDK (QNN SDK) to construct a QNN graph from an ONNX model which can be executed by a supported accelerator backend library. OnnxRuntime QNN Execution Provider can be used on Android and Windows devices with Qualcomm Snapdragon SOC's.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contents) Contents 

- [Install Pre-requisites (Build from Source Only)](#install-pre-requisites-build-from-source-only)
  - [QNN Version Requirements](#qnn-version-requirements)
- [Build (Android and Windows)](#build-android-and-windows)
- [Pre-built Packages (Windows Only)](#pre-built-packages-windows-only)
- [Qualcomm AI Hub](#qualcomm-ai-hub)
- [Configuration Options](#configuration-options)
  - [EP Provider Options](#ep-provider-options)
  - [Run Options](#run-options)
- [Supported ONNX operators](#supported-onnx-operators)
- [Running a model with QNN EP's HTP backend (Python)](#running-a-model-with-qnn-eps-htp-backend-python)
  - [Model requirements](#model-requirements)
  - [Generating a quantized model (x64 only)](#generating-a-quantized-model-x64-only)
  - [Running a quantized model on Windows ARM64 (onnxruntime-qnn version \>= 1.18.0)](#running-a-quantized-model-on-windows-arm64-onnxruntime-qnn-version--1180)
- [Running a model with QNN EP's GPU backend](#running-a-model-with-qnn-eps-gpu-backend)
- [QNN context binary cache feature](#qnn-context-binary-cache-feature)
  - [Dump QNN context binary](#dump-qnn-context-binary)
  - [Configure the context binary file path](#configure-the-context-binary-file-path)
  - [Enable the embed mode](#enable-the-embed-mode)
- [QNN EP Profiling](#qnn-ep-profiling)
  - [General Usage](#general-usage)
  - [Optrace-Level Profiling](#optrace-level-profiling)
  - [Optrace Setup](#optrace-setup)
  - [Generating QHAS Data](#generating-qhas-data)
  - [Additional References](#additional-references)
- [QNN EP weight sharing](#qnn-ep-weight-sharing)
- [Usage](#usage)
  - [C++](#c)
  - [Python](#python)
  - [Inference example](#inference-example)
- [Error handling](#error-handling)
  - [HTP SubSystem Restart - SSR](#htp-subsystem-restart---ssr)
- [Add new operator support in QNN EP](#add-new-operator-support-in-qnn-ep)
  - [Example PRs to enable new operators:](#example-prs-to-enable-new-operators)
- [Mixed precision support](#mixed-precision-support)
- [LoRAv2 support](#lorav2-support)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-pre-requisites-build-from-source-only) Install Pre-requisites (Build from Source Only)

If you build QNN Execution Provider from source, you should first download the Qualcomm AI Engine Direct SDK (QNN SDK) from <https://qpm.qualcomm.com/#/main/tools/details/Qualcomm_AI_Runtime_SDK>

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#qnn-version-requirements) QNN Version Requirements

ONNX Runtime QNN Execution Provider has been built and tested with QNN 2.22.x and Qualcomm SC8280, SM8350, Snapdragon X SOC's on Android and Windows

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-android-and-windows) Build (Android and Windows)

For build instructions, please see the [BUILD page](/docs/build/eps.html#qnn).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#pre-built-packages-windows-only) Pre-built Packages (Windows Only)

Note: Starting version 1.18.0 , you do not need to separately download and install QNN SDK. The required QNN dependency libraries are included in the OnnxRuntime packages.

- [NuGet package](https://www.nuget.org/packages/Microsoft.ML.OnnxRuntime.QNN)
  - Feed for nightly packages of Microsoft.ML.OnnxRuntime.QNN can be found [here](https://aiinfra.visualstudio.com/PublicPackages/_artifacts/feed/ORT-Nightly)
- [Python package](https://pypi.org/project/onnxruntime-qnn/)
  - Requirements:
    - Windows ARM64 (for inferencing on local device with Qualcomm NPU)
    - Windows X64 (for quantizing models. see [Generating a quantized model](/docs/execution-providers/QNN-ExecutionProvider.html#generating-a-quantized-model-x64-only))
    - Python 3.11.x
    - Numpy 1.25.2 or \>= 1.26.4
  - Install: `pip install onnxruntime-qnn`
  - Install nightly package `python -m pip install --pre --extra-index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/ORT-Nightly/pypi/simple onnxruntime-qnn`

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#qualcomm-ai-hub) Qualcomm AI Hub

Qualcomm AI Hub can be used to optimize and run models on Qualcomm hosted devices. OnnxRuntime QNN Execution Provider is a supported runtime in [Qualcomm AI Hub](https://aihub.qualcomm.com/)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#configuration-options) Configuration Options

The QNN Execution Provider supports a number of configuration options. These provider options are specified as key-value string pairs.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ep-provider-options) EP Provider Options

  `"backend_type"`   Description
  ---------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------
  'cpu'                                                      Enable CPU backend. Useful for integration testing. The CPU backend is a reference implementation of QNN operators.
  'gpu'                                                      Enable GPU backend.
  'htp'                                                      Enable HTP backend. Offloads compute to NPU. Default.
  'saver'                                                    Enable Saver backend.

  `"backend_path"`   Description
  ---------------------------------------------------------- ---------------------------------------------------------------------------------------
  'libQnnCpu.so' or 'QnnCpu.dll'                             Enable CPU backend. See `backend_type` 'cpu'.
  'libQnnHtp.so' or 'QnnHtp.dll'                             Enable HTP backend. See `backend_type` 'htp'.
  'libQnnGpu.so' or 'QnnGpu.dll'                             Enable GPU backend. See `backend_type` 'gpu'.

**Note:** `backend_path` is an alternative to `backend_type`. At most one of the two should be specified. `backend_path` requires a platform-specific path (e.g., `libQnnCpu.so` vs. `QnnCpu.dll`) but also allows one to specify an arbitrary path.

  `"profiling_level"`   Description
  ------------------------------------------------------------- ------------------------------
  'off'                                                         default.
  'basic'                                                        
  'detailed'                                                     
  'optrace'                                                     Requires QAIRT 2.39 or later

  `"profiling_file_path"`   Description
  ----------------------------------------------------------------- ------------------------------------------------------------
  'your_qnn_profile_path.csv'                                       Specify the csv file path to dump the QNN profiling events

See [profiling-tools](/docs/performance/tune-performance/profiling-tools.html) for more info on profiling\
Alternatively to setting profiling_level at compile time, profiling can be enabled dynamically with ETW (Windows). See [tracing](/docs/performance/tune-performance/logging_tracing.html) for more details

  `"rpc_control_latency"`   Description
  ----------------------------------------------------------------- -------------------------------------------------------------
  microseconds (string)                                             allows client to set up RPC control latency in microseconds

  `"vtcm_mb"`   Description
  ----------------------------------------------------- ----------------------------------------------
  size in MB (string)                                   QNN VTCM size in MB, defaults to 0 (not set)

  `"htp_performance_mode"`   Description
  ------------------------------------------------------------------ -------------
  'burst'                                                             
  'balanced'                                                          
  'default'                                                          default.
  'high_performance'                                                  
  'high_power_saver'                                                  
  'low_balanced'                                                      
  'low_power_saver'                                                   
  'power_saver'                                                       
  'sustained_high_performance'                                        

  `"qnn_saver_path"`   Description
  ------------------------------------------------------------ -----------------------------------------------------------------------------------------------
  filpath to 'QnnSaver.dll' or 'libQnnSaver.so'                File path to the QNN Saver backend library. Dumps QNN API calls to disk for replay/debugging.

  `"qnn_context_priority"`   [Description](https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-50/htp_yielding.html)
  ------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------
  'low'                                                               
  'normal'                                                           default.
  'normal_high'                                                       
  'high'                                                              

  `"htp_graph_finalization_optimization_mode"`   Description
  -------------------------------------------------------------------------------------- ----------------------------------------------------------------
  '0'                                                                                    default.
  '1'                                                                                    faster preparation time, less optimal graph.
  '2'                                                                                    longer preparation time, more optimal graph.
  '3'                                                                                    longest preparation time, most likely even more optimal graph.

  `"soc_model"`   Description
  ------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Model number (string)                                   The SoC model number. Refer to the [QNN SDK documentation](https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-50/overview.html#supported-snapdragon-devices) for valid values. Defaults to "0" (unknown).

  `"htp_arch"`   Description
  ------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Hardware Architecture                                  HTP Architecture number. Refer to the [QNN SDK documentation](https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-50/enum_QnnHtpDevice_8h_1a0ed976142af98a86143459dfd326f717.html#exhale-enum-qnnhtpdevice-8h-1a0ed976142af98a86143459dfd326f717) for valid values. Default (none)

  `"device_id"`   Description
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------
  Device ID (string)                                      The ID of the device to use when setting `htp_arch`. Defaults to "0" (for single device).

  `"enable_htp_fp16_precision"`   Description [Example](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/c_cxx/QNN_EP/mobilenetv2_classification)
  ----------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------
  '0'                                                                     Disabled. Inferenced with fp32 precision if it's fp32 model.
  '1'                                                                     Default. Enable the float32 model to be inferenced with fp16 precision.

  `"offload_graph_io_quantization"`   Description
  --------------------------------------------------------------------------- -----------------------------------------------------------------------------------
  '0'                                                                         Disabled. QNN EP will handle quantization and dequantization of graph I/O.
  '1'                                                                         Default. Enabled. Offload quantization and dequantization of graph I/O to CPU EP.

  `"enable_htp_shared_memory_allocator"`   Description
  -------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  '0'                                                                              Default. Disabled.
  '1'                                                                              Enable the QNN HTP shared memory allocator. Requires libcdsprpc.so/dll to be available. [Code example](https://github.com/microsoft/onnxruntime/blob/544bdd60730270f49f6a5baafdff54065f626776/onnxruntime/test/shared_lib/test_inference.cc#L2262-L2354)

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#run-options) Run Options

  `"qnn.lora_config"`   Description
  ------------------------------------------------------------- ------------------------------------------------------------------------------------------------
  Config path                                                   LoRAv2 config file path. The format of the config will be mentioned in the **LoraV2 support**.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#supported-onnx-operators) Supported ONNX operators

  Operator                         Notes
  -------------------------------- ---------------------------------------------------------------------------------------------
  ai.onnx:Abs                       
  ai.onnx:Add                       
  ai.onnx:And                       
  ai.onnx:ArgMax                    
  ai.onnx:ArgMin                    
  ai.onnx:Asin                      
  ai.onnx:Atan                      
  ai.onnx:AveragePool               
  ai.onnx:BatchNormalization       fp16 supported since 1.18.0
  ai.onnx:Cast                      
  ai.onnx:Clip                     fp16 supported since 1.18.0
  ai.onnx:Concat                    
  ai.onnx:Conv                     3d supported since 1.18.0
  ai.onnx:ConvTranspose            3d supported since 1.18.0
  ai.onnx:Cos                       
  ai.onnx:DepthToSpace              
  ai.onnx:DequantizeLinear          
  ai.onnx:Div                       
  ai.onnx:Elu                       
  ai.onnx:Equal                     
  ai.onnx:Exp                       
  ai.onnx:Expand                    
  ai.onnx:Flatten                   
  ai.onnx:Floor                     
  ai.onnx:Gather                   Only supports positive indices
  ai.onnx:Gelu                      
  ai.onnx:Gemm                      
  ai.onnx:GlobalAveragePool         
  ai.onnx:Greater                   
  ai.onnx:GreaterOrEqual            
  ai.onnx:GridSample                
  ai.onnx:HardSwish                 
  ai.onnx:InstanceNormalization     
  ai.onnx:LRN                       
  ai.onnx:LayerNormalization        
  ai.onnx:LeakyRelu                 
  ai.onnx:Less                      
  ai.onnx:LessOrEqual               
  ai.onnx:Log                       
  ai.onnx:LogSoftmax                
  ai.onnx:LpNormalization          p == 2
  ai.onnx:MatMul                   Supported input data types on HTP backend: (uint8, uint8), (uint8, uint16), (uint16, uint8)
  ai.onnx:Max                       
  ai.onnx:MaxPool                   
  ai.onnx:Min                       
  ai.onnx:Mul                       
  ai.onnx:Neg                       
  ai.onnx:Not                       
  ai.onnx:Or                        
  ai.onnx:Prelu                    fp16, int32 supported since 1.18.0
  ai.onnx:Pad                       
  ai.onnx:Pow                       
  ai.onnx:QuantizeLinear            
  ai.onnx:ReduceMax                 
  ai.onnx:ReduceMean                
  ai.onnx:ReduceMin                 
  ai.onnx:ReduceProd                
  ai.onnx:ReduceSum                 
  ai.onnx:Relu                      
  ai.onnx:Resize                    
  ai.onnx:Round                     
  ai.onnx:Sigmoid                   
  ai.onnx:Sign                      
  ai.onnx:Sin                       
  ai.onnx:Slice                     
  ai.onnx:Softmax                   
  ai.onnx:SpaceToDepth              
  ai.onnx:Split                     
  ai.onnx:Sqrt                      
  ai.onnx:Squeeze                   
  ai.onnx:Sub                       
  ai.onnx:Tanh                      
  ai.onnx:Tile                      
  ai.onnx:TopK                      
  ai.onnx:Transpose                 
  ai.onnx:Unsqueeze                 
  ai.onnx:Where                     
  com.microsoft:DequantizeLinear   Provides 16-bit integer dequantization support
  com.microsoft:Gelu                
  com.microsoft:QuantizeLinear     Provides 16-bit integer quantization support

Supported data types vary by operator and QNN backend. Refer to the [QNN SDK documentation](https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-50/operations.html) for more information.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#running-a-model-with-qnn-eps-htp-backend-python) Running a model with QNN EP's HTP backend (Python)

![Offline workflow for quantizing an ONNX model for use on QNN EP](../../images/qnn_ep_quant_workflow.png)

The QNN HTP backend only supports quantized models. Models with 32-bit floating-point activations and weights must first be quantized to use a lower integer precision (e.g., 8-bit or 16-bit integers).

This section provides instructions for quantizing a model and then running the quantized model on QNN EP's HTP backend using Python APIs. Please refer to the [quantization page](/docs/performance/model-optimizations/quantization.html) for a broader overview of quantization concepts.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#model-requirements) Model requirements

QNN EP does not support models with dynamic shapes (e.g., a dynamic batch size). Dynamic shapes must be fixed to a specific value. Refer to the documentation for [making dynamic input shapes fixed](/docs/tutorials/mobile/helpers/make-dynamic-shape-fixed.html) for more information.

Additionally, QNN EP supports a subset of ONNX operators (e.g., Loops and Ifs are not supported). Refer to the [list of supported ONNX operators](/docs/execution-providers/QNN-ExecutionProvider.html#supported-onnx-operators).

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#generating-a-quantized-model-x64-only) Generating a quantized model (x64 only)

The ONNX Runtime python package provides utilities for quantizing ONNX models via the `onnxruntime.quantization` import. The quantization utilities are currently only supported on x86_64 due to issues installing the `onnx` package on ARM64. Therefore, it is recommended to either use an x64 machine to quantize models or, alternatively, use a separate x64 python installation on Windows ARM64 machines.

Install the ONNX Runtime x64 python package. (please note, you must use x64 package for quantizing the model. use the arm64 package for inferencing and utilizing the HTP/NPU)

``` highlight
python -m pip install onnxruntime-qnn
```

Quantization for QNN EP requires the use of calibration input data. Using a calibration dataset that is representative of typical model inputs is crucial in generating an accurate quantized model.

The following snippet defines a sample `DataReader` class that generates random float32 input data. Note that using random input data will most likely produce an inaccurate quantized model. Refer to the [implementation of a Resnet data reader](https://github.com/microsoft/onnxruntime-inference-examples/blob/main/quantization/image_classification/cpu/resnet50_data_reader.py) for one example of how to create a `CalibrationDataReader` that provides input from image files on disk.

``` highlight
# data_reader.py

import numpy as np
import onnxruntime
from onnxruntime.quantization import CalibrationDataReader

class DataReader(CalibrationDataReader):
    def __init__(self, model_path: str):
        self.enum_data = None

        # Use inference session to get input shape.
        session = onnxruntime.InferenceSession(model_path, providers=['CPUExecutionProvider'])

        inputs = session.get_inputs()

        self.data_list = []

        # Generate 10 random float32 inputs
        # TODO: Load valid calibration input data for your model
        for _ in range(10):
            input_data = 
            self.data_list.append(input_data)

        self.datasize = len(self.data_list)

    def get_next(self):
        if self.enum_data is None:
            self.enum_data = iter(
                self.data_list
            )
        return next(self.enum_data, None)

    def rewind(self):
        self.enum_data = None
```

The following snippet pre-processes the original model and then quantizes the pre-processed model to use `uint16` activations and `uint8` weights. Although the quantization utilities expose the `uint8`, `int8`, `uint16`, and `int16` quantization data types, QNN operators typically support the `uint8` and `uint16` data types. Refer to the [QNN SDK operator documentation](https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-50/HtpOpDefSupplement.html) for the data type requirements of each QNN operator.

``` highlight
# quantize_model.py

import data_reader
import numpy as np
import onnx
from onnxruntime.quantization import QuantType, quantize
from onnxruntime.quantization.execution_providers.qnn import get_qnn_qdq_config, qnn_preprocess_model

if __name__ == "__main__":
    input_model_path = "model.onnx"  # TODO: Replace with your actual model
    output_model_path = "model.qdq.onnx"  # Name of final quantized model
    my_data_reader = data_reader.DataReader(input_model_path)

    # Pre-process the original float32 model.
    preproc_model_path = "model.preproc.onnx"
    model_changed = qnn_preprocess_model(input_model_path, preproc_model_path)
    model_to_quantize = preproc_model_path if model_changed else input_model_path

    # Generate a suitable quantization configuration for this model.
    # Note that we're choosing to use uint16 activations and uint8 weights.
    qnn_config = get_qnn_qdq_config(model_to_quantize,
                                    my_data_reader,
                                    activation_type=QuantType.QUInt16,  # uint16 activations
                                    weight_type=QuantType.QUInt8)       # uint8 weights

    # Quantize the model.
    quantize(model_to_quantize, output_model_path, qnn_config)
```

Running `python quantize_model.py` will generate a quantized model called `model.qdq.onnx` that can be run on Windows ARM64 devices via ONNX Runtime's QNN EP.

Refer to the following pages for more information on usage of the quantization utilities:

- [Quantization example for mobilenet on CPU EP](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/quantization/image_classification/cpu)
- [quantization/execution_providers/qnn/preprocess.py](https://github.com/microsoft/onnxruntime/blob/23996bbbbe0406a5c8edbf6b7dbd71e5780d3f4b/onnxruntime/python/tools/quantization/execution_providers/qnn/preprocess.py#L16)
- [quantization/execution_providers/qnn/quant_config.py](https://github.com/microsoft/onnxruntime/blob/23996bbbbe0406a5c8edbf6b7dbd71e5780d3f4b/onnxruntime/python/tools/quantization/execution_providers/qnn/quant_config.py#L20-L27)

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#running-a-quantized-model-on-windows-arm64-onnxruntime-qnn-version--1180) Running a quantized model on Windows ARM64 (onnxruntime-qnn version \>= 1.18.0) 

Install the ONNX Runtime ARM64 python package for QNN EP (requires Python 3.11.x and Numpy 1.25.2 or \>= 1.26.4):

``` highlight
python -m pip install onnxruntime-qnn
```

The following Python snippet creates an ONNX Runtime session with QNN EP and runs the quantized model `model.qdq.onnx` on the HTP backend.

``` highlight
# run_qdq_model.py

import onnxruntime
import numpy as np

options = onnxruntime.SessionOptions()

# (Optional) Enable configuration that raises an exception if the model can't be
# run entirely on the QNN HTP backend.
options.add_session_config_entry("session.disable_cpu_ep_fallback", "1")

# Create an ONNX Runtime session.
# TODO: Provide the path to your ONNX model
session = onnxruntime.InferenceSession("model.qdq.onnx",
                                       sess_options=options,
                                       providers=["QNNExecutionProvider"],
                                       provider_options=[]) # Provide path to Htp dll in QNN SDK

# Run the model with your input.
# TODO: Use numpy to load your actual input from a file or generate random input.
input0 = np.ones((1,3,224,224), dtype=np.float32)
result = session.run(None, )

# Print output.
print(result)
```

Running `python run_qdq_model.py` will execute the quantized `model.qdq.onnx` model on the QNN HTP backend.

Notice that the session has been optionally configured to raise an exception if the entire model cannot be executed on the QNN HTP backend. This is useful for verifying that the quantized model is fully supported by QNN EP. Available session configurations include:

- [session.disable_cpu_ep_fallback](https://github.com/microsoft/onnxruntime/blob/a4cfdc1c28ac95ec6fd0667e856b6a6b8dd1020c/include/onnxruntime/core/session/onnxruntime_session_options_config_keys.h#L229): Disables fallback of unsupported operators to the CPU EP.
- [ep.context_enable](https://github.com/microsoft/onnxruntime/blob/a4cfdc1c28ac95ec6fd0667e856b6a6b8dd1020c/include/onnxruntime/core/session/onnxruntime_session_options_config_keys.h#L243): [Enable QNN context cache](/docs/execution-providers/QNN-ExecutionProvider.html#qnn-context-binary-cache-feature) feature to dump a cached version of the model in order to decrease session creation time.

The above snippet only specifies the `backend_path` provider option. Refer to the [Configuration options section](/docs/execution-providers/QNN-ExecutionProvider.html#configuration-options) for a list of all available QNN EP provider options.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#running-a-model-with-qnn-eps-gpu-backend) Running a model with QNN EP's GPU backend

The QNN GPU backend can run models with 32-bit/16-bit floating-point activations and weights as such without prior quantization. A 16-bit floating-point model generally can run inference faster on the GPU compared to its 32-bit version. To help reduce the size of large models, quantizing weights to `uint8`, while keeping activations in float is also supported.

Other than the quantized model requirement mentioned in the above HTP backend section, all other requirements are valid for the GPU backend also. So is the model inference sample code except for the portion where you specify the backend.

``` highlight
# Create an ONNX Runtime session.
# TODO: Provide the path to your ONNX model
session = onnxruntime.InferenceSession("model.onnx",
                                       sess_options=options,
                                       providers=["QNNExecutionProvider"],
                                       provider_options=[]) # Provide path to Gpu dll in QNN SDK
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#qnn-context-binary-cache-feature) QNN context binary cache feature

There's a QNN context which contains QNN graphs after converting, compiling, finalizing the model. QNN can serialize the context into binary file, so that user can use it for futher inference directly (without the QDQ model) to improve the model loading cost. The QNN Execution Provider supports a number of session options to configure this.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#dump-qnn-context-binary) Dump QNN context binary

1.  Create session option, set "ep.context_enable" to "1" to enable QNN context dump. The key "ep.context_enable" is defined as kOrtSessionOptionEpContextEnable in [onnxruntime_session_options_config_keys.h](https://github.com/microsoft/onnxruntime/blob/8931854528b1b2a3f320d012c78d37186fbbdab8/include/onnxruntime/core/session/onnxruntime_session_options_config_keys.h#L239-L252).
2.  Create the session with the QDQ model using session options created in step 1, and use HTP backend A Onnx model with QNN context binary will be created once the session is created/initialized. No need to run the session. The QNN context binary generation can be done on the QualComm device which has HTP using Arm64 build. It can also be done on x64 machine using x64 build (not able to run it since there's no HTP device).

The generated Onnx model which has QNN context binary can be deployed to production/real device to run inference. This Onnx model is treated as a normal model by QNN Execution Provider. Inference code keeps same as inference with QDQ model on HTP backend.

[Code example](https://github.com/microsoft/onnxruntime-inference-examples/blob/733ce6f3e8dd2ede8b67a8465684bca2f62a4a33/c_cxx/QNN_EP/mobilenetv2_classification/main.cpp#L90-L97)

``` highlight
#include "onnxruntime_session_options_config_keys.h"

// C++
Ort::SessionOptions so;
so.AddConfigEntry(kOrtSessionOptionEpContextEnable, "1");

// C
const OrtApi* g_ort = OrtGetApiBase()->GetApi(ORT_API_VERSION);
OrtSessionOptions* session_options;
CheckStatus(g_ort, g_ort->CreateSessionOptions(&session_options));
g_ort->AddSessionConfigEntry(session_options, kOrtSessionOptionEpContextEnable, "1");
```

``` highlight
# Python
import onnxruntime

options = onnxruntime.SessionOptions()
options.add_session_config_entry("ep.context_enable", "1")
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#configure-the-context-binary-file-path) Configure the context binary file path

The generated Onnx model with QNN context binary is default to \[input_QDQ_model_name\]\_ctx.onnx in case user does not specify the path. User can to set the path in the session option with the key "ep.context_file_path". Example code below:

``` highlight
// C++
so.AddConfigEntry(kOrtSessionOptionEpContextFilePath, "./model_a_ctx.onnx");

// C
g_ort->AddSessionConfigEntry(session_options, kOrtSessionOptionEpContextFilePath, "./model_a_ctx.onnx");
```

``` highlight
# Python
options.add_session_config_entry("ep.context_file_path", "./model_a_ctx.onnx")
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#enable-the-embed-mode) Enable the embed mode

The QNN context binary content is not embedded in the generated Onnx model by default. A bin file will be generated separately. The file name looks like \[input_model_file_name\]*QNN*\[hash_id\].bin. The name is provided by Ort and tracked in the generated Onnx model. It will cause problems if any changes are made to the bin file. This bin file needs to sit together with the generated Onnx file. User can enable it by setting "ep.context_embed_mode" to "1". In that case the content of the context binary is embedded inside the Onnx model.

``` highlight
// C++
so.AddConfigEntry(kOrtSessionOptionEpContextEmbedMode, "1");

// C
g_ort->AddSessionConfigEntry(session_options, kOrtSessionOptionEpContextEmbedMode, "1");
```

``` highlight
# Python
options.add_session_config_entry("ep.context_embed_mode", "1")
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#qnn-ep-profiling) QNN EP Profiling

Profiling data is available with the HTP backend. Enabling QNN profiling will generate a user-readable .csv file that will contain information from initialization, execution, and de-initialization.

If onnxruntime is compiled with a more recent QAIRT SDK (2.39 or later), then a \_qnn.log file will also be generated alongside the .csv file. This .log file is parsable by [qnn-profile-viewer](https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/general_tools.html#qnn-profile-viewer), which is provided in the SDK.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#general-usage) General Usage

To utilize QNN profiling, simply set the EP option profiling_level to basic, detailed, or optrace. Additionally, the EP option profiling_file_path must also be set to the output .csv filepath you would like to write data to:

``` highlight
# Python on Windows on Snapdragon device
import onnxruntime as ort
import numpy as np

provider_options = [
    "backend_path": "path/to/QnnHtp.dll", # Use libQnnHtp.so if on Linux
    "htp_performance_mode": "burst",
    "device_id": "0",
    "htp_graph_finalization_optimization_mode":"3",
    "soc_model": "60",
    "htp_arch": "73",
    "vtcm_mv": "8",
    "profiling_level": "basic",
    "profiling_file_path": "output.csv"
]

sess_options = ort.SessionOptions()

session = ort.InferenceSession(
    "model.onnx",
    sess_options=sess_options,
    providers=["QNNExecutionProvider"],
    provider_options=provider_options
)

input0 = np.ones((1,2,3,4), dtype=np.float32)
result = session.run(None, )
```

With the example above, a file "output.csv" will be generated containing the profiling data. Additionally, if using QAIRT 2.39 SDK or later, another file "output_qnn.log" will be generated.

"output_qnn.log" can then be parsed with the appropriate qnn-profile-viewer binary:

``` highlight
> qnn-profile-viewer.exe --input_log .\output_qnn.log --output output_2.csv
```

The above will output basic information, such as the profiling data for the fastest and slowest execution as well as the average case. A .csv file can also be generated this way, too, though the information will likely not differ from the "output.csv".

Additionally, if the profiling_level is set to "detailed" or "optrace", additional data will be shown per-network-layer.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#optrace-level-profiling) Optrace-Level Profiling

[Optrace-level profiling](https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/htp_backend.html#qnn-htp-profiling) generates a profiling .log file that contains [Qualcomm Hexagon Tensor Processor Analaysis Summary (QHAS)](https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/htp_backend.html#qnn-htp-analysis-summary-qhas-) data. This data can be used to generate chrometraces and provide a web browser-friendly UI to visualize data.

**This feature is only available with the QAIRT 2.39 SDK and later.**

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#optrace-setup) Optrace Setup

To utilize this feature, a context binary must be generated prior to execution:

``` highlight
# Python on Windows on Snapdragon device
import onnxruntime as ort
import numpy as np

provider_options = [
    "backend_path": "path/to/QnnHtp.dll", # Use libQnnHtp.so if on Linux
    "htp_performance_mode": "burst",
    "device_id": "0",
    "htp_graph_finalization_optimization_mode":"3",
    "soc_model": "60",
    "htp_arch": "73",
    "vtcm_mv": "8",
    "profiling_level": "optrace",   # Set profiling_level to optrace
    "profiling_file_path": "optrace.csv"
]

sess_options = ort.SessionOptions()

# Enable context bin generation
sess_options.add_session_config_entry("ep.context_embed_mode", "0")
sess_options.add_session_config_entry("ep.context_enable", "1")

session = ort.InferenceSession(
    "model.onnx",
    sess_options=sess_options,
    providers=["QNNExecutionProvider"],
    provider_options=provider_options
)
```

Upon successful session creation, three files will be generated:

- model_ctx.onnx
- model_qnn.bin
- QNNExecutionProvider_QNN\_\<number\>\_schematic.bin

model_ctx.onnx is an onnx model with a node that points to the model_qnn.bin context binary, which will be used by the HTP backend for execution. The \_schematic.bin file will be used by qnn-profile-viewer to generate QHAS data.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#generating-qhas-data) Generating QHAS Data

Previously for general profiling data, a session was created and executed with "model.onnx". However, now there is a new \_ctx.onnx model that utilizes a newly generated context binary. As such, a new inference session must be created with the new \_ctx.onnx model:

``` highlight
# Continuing from Optrace Setup:

sess_options.add_session_config_entry("ep.context_enable", "0")

optrace_session = ort.InferenceSession(
    "model_ctx.onnx",
    sess_options=sess_options,
    providers=["QNNExecutionProvider"],
    provider_options=provider_options
)

input0 = np.ones((1,2,3,4), dtype=np.float32)
result = optrace_session.run(None, )
```

As before under "General Usage", a .csv file (optrace.csv) and a \_qnn.log file (optrace_qnn.log) are generated.

qnn-profile-viewer can be used with different parameters and files to parse all the data written to optrace_qnn.log:

``` highlight
> qnn-profile-viewer.exe --config .\config.json --reader .\QnnHtpOptraceProfilingReader.dll --input_log .\optrace_qnn.log  --schematic .\QNNExecutionProvider_QNN_12345_schematic.bin --output optrace.json
```

Please note:

- Three new files are used:
  - config.json: Please refer to the "Post Process (Chrometrace Generation)" section [on this page](https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/htp_backend.html#qnn-htp-optrace-profiling).
  - QnnHtpOptraceProfilingReader.dll: Provided as part of the QAIRT SDK. The corresponding file for Linux is libQnnHtpOptraceProfilingReader.so.
  - QNNExecutionProvider_QNN_12345_schematic.bin: The name will vary. This file must be the same one generated alongside the context binary under "Optrace Setup".
- The output file is now a .json file containing chrometrace data. This .json file can be opened with either [Perfetto Trace Vizualizer](https://ui.perfetto.dev/) or with chrome://tracing.

After running qnn-profile-viewer, you should see a handful of .json files generated with the same prefix as the --output filename parameter. You should also see an .html file generated as well. This .html file can be opened by Chrome to view the chrometrace in a more user-friendly GUI.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#additional-references) Additional References

For more information how to interpret QHAS data, please refer to [this page](https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/htp_backend.html#qnn-htp-analysis-summary-qhas-).

For more information on the data collected with optrace profiling, please refer to [this page](https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-10/htp_backend.html#qnn-htp-optrace-profiling).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#qnn-ep-weight-sharing) QNN EP weight sharing

Refers to the [EPContext design doc](https://onnxruntime.ai/docs/execution-providers/EP-Context-Design.html#epcontext-with-weight-sharing)

Note: QNN EP requires **Linux x86_64** or **Windows x86_64** platform.

Additionally, if user creates the QNN context binary (`qnn_ctx.bin`) with weight sharing using the QNN toolchain (`qnn-context-binary-generator`), they can use a script to generate the wrapper Onnx model from the context: [gen_qnn_ctx_onnx_model.py](https://github.com/microsoft/onnxruntime/blob/main/onnxruntime/python/tools/qnn/gen_qnn_ctx_onnx_model.py). The script creates multiple `model_x_ctx.onnx` files, each containing an `EPContext` node that references the shared `qnn_ctx.bin` file. Each `EPContext` node specifies a unique node name, referring to different Qnn graph from the QNN context.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#usage) Usage

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#c) C++

C API details are [here](/docs/get-started/with-c.html).

``` highlight
Ort::Env env = Ort::Env;
std::unordered_map<std::string, std::string> qnn_options;
qnn_options["backend_path"] = "QnnHtp.dll";
Ort::SessionOptions session_options;
session_options.AppendExecutionProvider("QNN", qnn_options);
Ort::Session session(env, model_path, session_options);
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#python) Python

``` highlight
import onnxruntime as ort
# Create a session with QNN EP using HTP (NPU) backend.
sess = ort.InferenceSession(model_path, providers=['QNNExecutionProvider'], provider_options=[])`
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#inference-example) Inference example

[Image classification with Mobilenetv2 in CPP using QNN Execution Provider with QNN CPU & HTP Backend](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/c_cxx/QNN_EP/mobilenetv2_classification)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#error-handling) Error handling

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#htp-subsystem-restart---ssr) HTP SubSystem Restart - [SSR](https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-50/htp_backend.html#subsystem-restart-ssr-)

QNN EP returns StatusCode::ENGINE_ERROR regarding QNN HTP SSR issue. Uppper level framework/application should recreate Onnxruntime session if this error detected during session run.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#add-new-operator-support-in-qnn-ep) Add new operator support in QNN EP

To enable new operator support in EP, areas to visit:

- QDQ script support this Op? [code example](https://github.com/microsoft/onnxruntime/pull/14867/files#diff-b1ea073c326fef46054382117c256f106d39bd7c34539d44c6e6d9e9eacc059c)
- Onnxruntime QDQ node unit support this Op? [code example](https://github.com/microsoft/onnxruntime/pull/14867/files#diff-ce0281aaf63e03ecadd592240e41f18742bf8eb095b3725c0e55e589c890946f)
- Is it layout sensitive operator?
  - Registered in LayoutTransformer? [code example](https://github.com/microsoft/onnxruntime/blob/6d464748ba7fed2275ecba3a7406298cabc93438/onnxruntime/core/optimizer/transpose_optimizer/transpose_optimizer.cc#L2168)
  - NHWC op schema registered? Example error message: ::operator ()\] Model face_det_qdq failed to load:Fatal error: com.ms.internal.nhwc:BatchNormalization(9) is not a registered function/op \[Example PR\](https://github.com/microsoft/onnxruntime/pull/15278)

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#example-prs-to-enable-new-operators) Example PRs to enable new operators:

- Non-layout sensitive operator. [Enable Hardsigmoid for QNN EP using SDK support direct support](https://github.com/microsoft/onnxruntime/pull/20956)

- Layout sensitive operator. [Add InstanceNormalization operator to QNN EP](https://github.com/microsoft/onnxruntime/pull/14867)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#mixed-precision-support) Mixed precision support

The following figure demonstrates an example of mixed precision model.

![mixed precision model](../../images/quantization_mixed_precision_1.png)

A mixed precision QDQ model consists of regions with different activation/weight quantization data types. The boundary between regions converts between activation quantization data types (e.g., uint8 to uint16) using a DQ to Q sequence.

The ability to specify regions with different quantization data types enables exploring the tradeoffs between accuracy and latency. A higher integer precision may improve accuracy at the expense of latency, so selectively promoting certain regions to a higher precision can aid in achieving a desirable balance in key metrics.

The following figure shows a model with a region that has been promoted to 16-bit from the default 8-bit activation type.

![mixed precision layers](../../images/quantization_mixed_precision_2.png)

This model is quantized to uint8 precision, but tensor "Op4_out" is quantized to 16-bit. This can be achieved by specifying the following initial tensor quantization overrides:

``` highlight
# Op4_out could be an inaccurate tensor that should be upgraded to 16bit
initial_overrides = ]}

qnn_config = get_qnn_qdq_config(
    float_model_path,
    data_reader,
    activation_type=QuantType.QUInt8,
    weight_type=QuantType.QUInt8,
    init_overrides=initial_overrides,  # These initial overrides will be "fixed"
)
```

The above snippet generates the following "fixed" overrides (get via qnn_config.extra_options\["TensorQuantOverrides"\]):

``` highlight
overrides = }}],
  “Op3_out”: [}}],
  “Op4_out”: [],
  “Op5_out”: [}}]
}
```

After the override, the model works like this:

- Op2's output is consumed by Op4, Op7, and Op8. Op4 consumes the converted u16 type, while Op7 and Op8 consume the original u8 type.
- Op3's output is converted from u8 to u16. Op5 consumes the converted u16 type.
- Op4's output is just u16 (not converted).
- Op5's output is converted from u16 to u8. Op6 consumes the u8 type.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#lorav2-support) LoRAv2 support

Currently, only pre-compiled models with EPContext nodes are supported. The example script for reference [gen_qnn_ctx_onnx_model.py](https://github.com/microsoft/onnxruntime/blob/main/onnxruntime/python/tools/qnn/gen_qnn_ctx_onnx_model.py). After applying the model LoRAv2 using the [QNN SDK](https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-50/tutorials.html#lora-(low-rank-adaptation)), a main qnn context binary and several adapter binary sections will be generated. We use the LoRAv2 config and place it into RunOptions for inference.

- The format of the LoRAv2 config:
  - graph name: QNN graph in QNN pre-built context binary.
  - adapter binary section path: binary section generated by qnn-context-binary-generator \`\`\`

; \`\`\`