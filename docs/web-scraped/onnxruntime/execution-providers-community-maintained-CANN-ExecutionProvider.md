# Source: https://onnxruntime.ai/docs/execution-providers/community-maintained/CANN-ExecutionProvider.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#cann-execution-provider) CANN Execution Provider 

Huawei Compute Architecture for Neural Networks (CANN) is a heterogeneous computing architecture for AI scenarios and provides multi-layer programming interfaces to help users quickly build AI applications and services based on the Ascend platform.

Using CANN Excution Provider for ONNX Runtime can help you accelerate ONNX models on Huawei Ascend hardware.

The CANN Execution Provider (EP) for ONNX Runtime is developed by Huawei.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contents) Contents 

- [Install](#install)
- [Requirements](#requirements)
- [Build](#build)
- [Configuration Options](#configuration-options)
  - [device_id](#device_id)
  - [npu_mem_limit](#npu_mem_limit)
  - [arena_extend_strategy](#arena_extend_strategy)
  - [enable_cann_graph](#enable_cann_graph)
  - [enable_cann_subgraph](#enable_cann_subgraph)
  - [dump_graphs](#dump_graphs)
  - [dump_om_model](#dump_om_model)
  - [precision_mode](#precision_mode)
  - [op_select_impl_mode](#op_select_impl_mode)
  - [optypelist_for_implmode](#optypelist_for_implmode)
- [Performance tuning](#performance-tuning)
  - [IO Binding](#io-binding)
- [Samples](#samples)
  - [Python](#python)
  - [C/C++](#cc)
- [Supported ops](#supported-ops)
- [Additional Resources](#additional-resources)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install) Install

Pre-built binaries of ONNX Runtime with CANN EP are published, but only for python currently, please refer to [onnxruntime-cann](https://pypi.org/project/onnxruntime-cann/).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#requirements) Requirements

Please reference table below for official CANN packages dependencies for the ONNX Runtime inferencing package.

  ONNX Runtime   CANN
  -------------- -------
  v1.20.0        8.2.0
  v1.21.0        8.2.0
  v1.22.1        8.2.0

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build) Build

For build instructions, please see the [BUILD page](/docs/build/eps.html#cann).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#configuration-options) Configuration Options

The CANN Execution Provider supports the following configuration options.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#device_id) device_id

The device ID.

Default value: 0

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#npu_mem_limit) npu_mem_limit

The size limit of the device memory arena in bytes. This size limit is only for the execution provider's arena. The total device memory usage may be higher.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#arena_extend_strategy) arena_extend_strategy

The strategy for extending the device memory arena.

  Value              Description
  ------------------ ------------------------------------------------------------------------------
  kNextPowerOfTwo    subsequent extensions extend by larger amounts (multiplied by powers of two)
  kSameAsRequested   extend by the requested amount

Default value: kNextPowerOfTwo

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#enable_cann_graph) enable_cann_graph

Whether to use the graph inference engine to speed up performance. The recommended setting is true. If false, it will fall back to the single-operator inference engine.

Default value: true

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#enable_cann_subgraph) enable_cann_subgraph

The CANN backend supports automatic splitting of ONNX models. If set to true, it will support more ONNX models, but it may also introduce some performance overhead (as some nodes may fall back to the CPU).

Default value: false

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#dump_graphs) dump_graphs

Whether to dump the subgraph into onnx format for analysis of subgraph segmentation.

Default value: false

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#dump_om_model) dump_om_model

Whether to dump the offline model for Ascend AI Processor to an .om file.

Default value: true

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#precision_mode) precision_mode

The precision mode of the operator.

  Value                                          Description
  ---------------------------------------------- ----------------------------------------------------------------
  force_fp32/cube_fp16in_fp32out                 convert to float32 first according to operator implementation
  force_fp16                                     convert to float16 when float16 and float32 are both supported
  allow_fp32_to_fp16                             convert to float16 when float32 is not supported
  must_keep_origin_dtype                         keep it as it is
  allow_mix_precision/allow_mix_precision_fp16   mix precision mode

Default value: force_fp16

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#op_select_impl_mode) op_select_impl_mode

Some built-in operators in CANN have high-precision and high-performance implementation.

  Value              Description
  ------------------ --------------------------
  high_precision     aim for high precision
  high_performance   aim for high preformance

Default value: high_performance

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#optypelist_for_implmode) optypelist_for_implmode

Enumerate the list of operators which use the mode specified by the op_select_impl_mode parameter.

The supported operators are as follows:

- Pooling
- SoftmaxV2
- LRN
- ROIAlign

Default value: None

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#performance-tuning) Performance tuning

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#io-binding) IO Binding

The [I/O Binding feature](../../performance/tune-performance/iobinding.html) should be utilized to avoid overhead resulting from copies on inputs and outputs.

- Python

``` highlight
import numpy as np
import onnxruntime as ort

providers = [
    (
        "CANNExecutionProvider",
        ,
    ),
    "CPUExecutionProvider",
]

model_path = '<path to model>'

options = ort.SessionOptions()
options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_DISABLE_ALL
options.execution_mode = ort.ExecutionMode.ORT_PARALLEL

session = ort.InferenceSession(model_path, sess_options=options, providers=providers)

x = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]], dtype=np.int64)
x_ortvalue = ort.OrtValue.ortvalue_from_numpy(x, "cann", 0)

io_binding = sess.io_binding()
io_binding.bind_ortvalue_input(name="input", ortvalue=x_ortvalue)
io_binding.bind_output("output", "cann")

sess.run_with_iobinding(io_binding)

return io_binding.get_outputs()[0].numpy()
```

- C/C++(future)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#samples) Samples

Currently, users can use C/C++ and Python API on CANN EP.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#python) Python

``` highlight
import onnxruntime as ort

model_path = '<path to model>'

options = ort.SessionOptions()

providers = [
    (
        "CANNExecutionProvider",
        ,
    ),
    "CPUExecutionProvider",
]

session = ort.InferenceSession(model_path, sess_options=options, providers=providers)
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#cc) C/C++

Note: This sample shows model inference using [resnet50_Opset16.onnx](https://github.com/onnx/models/tree/main/Computer_Vision/resnet50_Opset16_timm) as an example. You need to modify the model_path, and the input_prepare() and output_postprocess() functions according to your needs.

``` highlight
#include <iostream>
#include <vector>

#include "onnxruntime_cxx_api.h"

// path of model, Change to user's own model path
const char* model_path = "./onnx/resnet50_Opset16.onnx";

/**
 * @brief Input data preparation provided by user.
 *
 * @param num_input_nodes The number of model input nodes.
 * @return  A collection of input data.
 */
std::vector<std::vector<float>> input_prepare(size_t num_input_nodes) 

/**
 * @brief Model output data processing logic(For User updates).
 *
 * @param output_tensors The results of the model output.
 */
void output_postprocess(std::vector<Ort::Value>& output_tensors) 
  
  std::cout << "Done!" << std::endl;
}

/**
 * @brief The main functions for model inference.
 *
 *  The complete model inference process, which generally does not need to be
 * changed here
 */
void inference() ;
  std::vector<const char*> values;
  api.UpdateCANNProviderOptions(
      cann_options, keys.data(), values.data(), keys.size());

  // Convert to general session options
  Ort::SessionOptions session_options;
  api.SessionOptionsAppendExecutionProvider_CANN(
      static_cast<OrtSessionOptions*>(session_options), cann_options);

  Ort::Session session(env, model_path, session_options);

  Ort::AllocatorWithDefaultOptions allocator;

  // Input Process
  const size_t num_input_nodes = session.GetInputCount();
  std::vector<const char*> input_node_names;
  std::vector<Ort::AllocatedStringPtr> input_names_ptr;
  input_node_names.reserve(num_input_nodes);
  input_names_ptr.reserve(num_input_nodes);
  std::vector<std::vector<int64_t>> input_node_shapes;
  std::cout << num_input_nodes << std::endl;
  for (size_t i = 0; i < num_input_nodes; i++) 

  // Output Process
  const size_t num_output_nodes = session.GetOutputCount();
  std::vector<const char*> output_node_names;
  std::vector<Ort::AllocatedStringPtr> output_names_ptr;
  output_names_ptr.reserve(num_input_nodes);
  output_node_names.reserve(num_output_nodes);
  for (size_t i = 0; i < num_output_nodes; i++) 

  //  User need to generate input date according to real situation.
  std::vector<std::vector<float>> input_datas = input_prepare(num_input_nodes);

  auto memory_info = Ort::MemoryInfo::CreateCpu(
      OrtAllocatorType::OrtArenaAllocator, OrtMemTypeDefault);

  std::vector<Ort::Value> input_tensors;
  input_tensors.reserve(num_input_nodes);
  for (size_t i = 0; i < input_node_shapes.size(); i++) 

  auto output_tensors = session.Run(
      Ort::RunOptions,
      input_node_names.data(),
      input_tensors.data(),
      num_input_nodes,
      output_node_names.data(),
      output_node_names.size());

  // Processing of out_tensor
  output_postprocess(output_tensors);
}

int main(int argc, char* argv[]) 
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#supported-ops) Supported ops

Following ops are supported by the CANN Execution Provider in single-operator Inference mode.

  --------------------------------------------------------------------------
  Operator                            Note
  ----------------------------------- --------------------------------------
  ai.onnx:Abs                          

  ai.onnx:Add                          

  ai.onnx:AveragePool                 Only 2D Pool is supported.

  ai.onnx:BatchNormalization           

  ai.onnx:Cast                         

  ai.onnx:Ceil                         

  ai.onnx:Conv                        Only 2D Conv is supported.\
                                      Weights and bias should be constant.

  ai.onnx:Cos                          

  ai.onnx:Div                          

  ai.onnx:Dropout                      

  ai.onnx:Exp                          

  ai.onnx:Erf                          

  ai.onnx:Flatten                      

  ai.onnx:Floor                        

  ai.onnx:Gemm                         

  ai.onnx:GlobalAveragePool            

  ai.onnx:GlobalMaxPool                

  ai.onnx:Identity                     

  ai.onnx:Log                          

  ai.onnx:MatMul                       

  ai.onnx:MaxPool                     Only 2D Pool is supported.

  ai.onnx:Mul                          

  ai.onnx:Neg                          

  ai.onnx:Reciprocal                   

  ai.onnx:Relu                         

  ai.onnx:Reshape                      

  ai.onnx:Round                        

  ai.onnx:Sin                          

  ai.onnx:Sqrt                         

  ai.onnx:Sub                          

  ai.onnx:Transpose                    
  --------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#additional-resources) Additional Resources

Additional operator support and performance tuning will be added soon.

- [Ascend](https://www.hiascend.com/en/)
- [CANN](https://www.hiascend.com/cann)