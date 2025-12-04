# Source: https://onnxruntime.ai/docs/execution-providers/community-maintained/RKNPU-ExecutionProvider.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#rknpu-execution-provider) RKNPU Execution Provider

*PREVIEW*

RKNPU DDK is an advanced interface to access Rockchip NPU. The RKNPU Execution Provider enables deep learning inference on Rockchip NPU via RKNPU DDK.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contents) Contents 

- [Build](#build)
- [Usage](#usage)
- [Support Coverage](#support-coverage)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build) Build

For build instructions, please see the [BUILD page](/docs/build/eps.html#rknpu).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#usage) Usage

**C/C++**

To use RKNPU as an execution provider for inferencing, please register it as below.

``` highlight
Ort::Env env = Ort::Env;
Ort::SessionOptions sf;
Ort::ThrowOnError(OrtSessionOptionsAppendExecutionProvider_RKNPU(sf));
Ort::Session session(env, model_path, sf);
```

The C API details are [here](/docs/get-started/with-c.html).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#support-coverage) Support Coverage

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#supported-platform) Supported Platform 

- RK1808 Linux

*Note: RK3399Pro platform is not supported.*

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#supported-operators) Supported Operators 

The table below shows the ONNX Ops supported using the RKNPU Execution Provider and the mapping between ONNX Ops and RKNPU Ops.

  **ONNX Ops**         **RKNPU Ops**
  -------------------- ---------------
  Add                  ADD
  Mul                  MULTIPLY
  Conv                 CONV2D
  QLinearConv          CONV2D
  Gemm                 FULLCONNECT
  Softmax              SOFTMAX
  AveragePool          POOL
  GlobalAveragePool    POOL
  MaxPool              POOL
  GlobalMaxPool        POOL
  LeakyRelu            LEAKY_RELU
  Concat               CONCAT
  BatchNormalization   BATCH_NORM
  Reshape              RESHAPE
  Flatten              RESHAPE
  Squeeze              RESHAPE
  Unsqueeze            RESHAPE
  Transpose            PERMUTE
  Relu                 RELU
  Sub                  SUBTRACT
  Clip(0\~6)           RELU6
  DequantizeLinear     DATACONVERT
  Clip                 CLIP

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#supported-models) Supported Models 

The following models from the ONNX model zoo are supported using the RKNPU Execution Provider

**Image Classification**

- squeezenet
- mobilenetv2-1.0
- resnet50v1
- resnet50v2
- inception_v2

**Object Detection**

- ssd
- yolov3