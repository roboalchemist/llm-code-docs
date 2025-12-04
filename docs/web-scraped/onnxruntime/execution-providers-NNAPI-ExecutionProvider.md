# Source: https://onnxruntime.ai/docs/execution-providers/NNAPI-ExecutionProvider.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#nnapi-execution-provider) NNAPI Execution Provider

Accelerate ONNX models on Android devices with ONNX Runtime and the NNAPI execution provider. [Android Neural Networks API (NNAPI)](https://developer.android.com/ndk/guides/neuralnetworks) is a unified interface to CPU, GPU, and NN accelerators on Android.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contents) Contents 

- [Requirements](#requirements)
- [Install](#install)
- [Build](#build)
- [Usage](#usage)
- [Configuration Options](#configuration-options)
- [Supported ops](#supported-ops)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#requirements) Requirements

The NNAPI Execution Provider (EP) requires Android devices with Android 8.1 or higher. It is recommended to use Android devices with Android 9 or higher to achieve optimal performance.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install) Install

Pre-built packages of ONNX Runtime with NNAPI EP for Android are published on Maven.

See [here](/docs/install/#install-on-android) for installation instructions.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build) Build

Please see the [Build Android EP](/docs/build/eps.html#nnapi) for instructions on building a package that includes the NNAPI EP.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#usage) Usage

The ONNX Runtime API details are [here](../api).

The NNAPI EP can be used via the C, C++ or Java APIs

The NNAPI EP must be explicitly registered when creating the inference session. For example:

``` C++
Ort::Env env = Ort::Env;
Ort::SessionOptions so;
uint32_t nnapi_flags = 0;
Ort::ThrowOnError(OrtSessionOptionsAppendExecutionProvider_Nnapi(so, nnapi_flags));
Ort::Session session(env, model_path, so);
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#configuration-options) Configuration Options

There are several run time options available for the NNAPI EP.

To use the NNAPI EP run time options, create an unsigned integer representing the options, and set each individual option by using the bitwise OR operator.

``` highlight
uint32_t nnapi_flags = 0;
nnapi_flags |= NNAPI_FLAG_USE_FP16;
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#available-options) Available Options

##### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#nnapi_flag_use_fp16) NNAPI_FLAG_USE_FP16

Use fp16 relaxation in NNAPI EP.

This may improve performance but can also reduce accuracy due to the lower precision.

##### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#nnapi_flag_use_nchw) NNAPI_FLAG_USE_NCHW

Use the NCHW layout in NNAPI EP.

This is only available for Android API level 29 and higher. Please note that for now, NNAPI might have worse performance using NCHW compared to using NHWC.

##### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#nnapi_flag_cpu_disabled) NNAPI_FLAG_CPU_DISABLED

Prevent NNAPI from using CPU devices.

NNAPI is more efficient using GPU or NPU for execution, however NNAPI might fall back to its CPU implementation for operations that are not supported by GPU/NPU. The CPU implementation of NNAPI (which is called nnapi-reference) is often less efficient than the optimized versions of the operation of ORT. Due to this, it may be advantageous to disable the NNAPI CPU fallback and handle execution using ORT kernels.

For some models, if NNAPI would use CPU to execute an operation, and this flag is set, the execution of the model may fall back to ORT kernels.

This option is only available for Android API level 29 and higher, and will be ignored for Android API level 28 and lower.

For NNAPI device assignments, see <https://developer.android.com/ndk/guides/neuralnetworks#device-assignment>

For NNAPI CPU fallback, see <https://developer.android.com/ndk/guides/neuralnetworks#cpu-fallback>

##### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#nnapi_flag_cpu_only) NNAPI_FLAG_CPU_ONLY

Using CPU only in NNAPI EP, this may decrease the perf but will provide reference output value without precision loss, which is useful for validation.

This option is only available for Android API level 29 and higher, and will be ignored for Android API level 28 and lower.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#supported-ops) Supported ops

Following ops are supported by the NNAPI Execution Provider,

  --------------------------------------------------------------------------------------------------------------------------------------
  Operator                            Note
  ----------------------------------- --------------------------------------------------------------------------------------------------
  ai.onnx:Abs                          

  ai.onnx:Add                          

  ai.onnx:AveragePool                 Only 2D Pool is supported.

  ai.onnx:BatchNormalization           

  ai.onnx:Cast                         

  ai.onnx:Clip                         

  ai.onnx:Concat                       

  ai.onnx:Conv                        Only 2D Conv is supported.\
                                      Weights and bias should be constant.

  ai.onnx:DepthToSpace                Only DCR mode DepthToSpace is supported.

  ai.onnx:DequantizeLinear            All quantization scales and zero points should be constant.

  ai.onnx:Div                          

  ai.onnx:Elu                          

  ai.onnx:Exp                          

  ai.onnx:Flatten                      

  ai.onnx:Floor                        

  ai.onnx:Gather                      Input indices should be constant if not int32 type.

  ai.onnx:Gemm                        If input B is not constant, transB should be 1.

  ai.onnx:GlobalAveragePool           Only 2D Pool is supported.

  ai.onnx:GlobalMaxPool               Only 2D Pool is supported.

  ai.onnx:Identity                     

  ai.onnx:LeakyRelu                    

  ai.onnx:Log                          

  ai.onnx:LRN                          

  ai.onnx:MatMul                       

  ai.onnx:MaxPool                     Only 2D Pool is supported.

  ai.onnx:Max                          

  ai.onnx:Min                          

  ai.onnx:Mul                          

  ai.onnx:Neg                          

  ai.onnx:Pad                         Only constant mode Pad is supported.\
                                      Input pads and constant_value should be constant.\
                                      Input pads values should be non-negative.

  ai.onnx:Pow                          

  ai.onnx:PRelu                        

  ai.onnx:QLinearConv                 Only 2D Conv is supported.\
                                      Weights and bias should be constant.\
                                      All quantization scales and zero points should be constant.

  ai.onnx:QLinearMatMul               All quantization scales and zero points should be constant.

  ai.onnx:QuantizeLinear              All quantization scales and zero points should be constant.

  ai.onnx:ReduceMean                   

  ai.onnx:Relu                         

  ai.onnx:Reshape                      

  ai.onnx:Resize                      Only 2D Resize is supported.

  ai.onnx:Sigmoid                      

  ai.onnx:Sin                          

  ai.onnx:Slice                        

  ai.onnx:Softmax                      

  ai.onnx:Split                       Number of splits must evenly divide split axis size. Input split should be constant if provided.

  ai.onnx:Sqrt                         

  ai.onnx:Squeeze                     Input axes should be constant.

  ai.onnx:Sub                          

  ai.onnx:Tanh                         

  ai.onnx:Transpose                    

  ai.onnx:Unsqueeze                   Input axes should be constant.

  com.microsoft:QLinearAdd            All quantization scales and zero points should be constant.

  com.microsoft:QLinearAveragePool    Only 2D Pool is supported.\
                                      All quantization scales and zero points should be constant.

  com.microsoft:QLinearSigmoid        All quantization scales and zero points should be constant.
  --------------------------------------------------------------------------------------------------------------------------------------