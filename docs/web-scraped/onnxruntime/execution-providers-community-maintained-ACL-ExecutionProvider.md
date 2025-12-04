# Source: https://onnxruntime.ai/docs/execution-providers/community-maintained/ACL-ExecutionProvider.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#acl-execution-provider) ACL Execution Provider 

The ACL Execution Provider enables accelerated performance on Arm®-based CPUs through [Arm Compute Library](https://github.com/ARM-software/ComputeLibrary).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build) Build

For build instructions, please see the [build page](/docs/build/eps.html#arm-compute-library).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#usage) Usage

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#cc) C/C++ 

``` highlight
Ort::Env env = Ort::Env;
Ort::SessionOptions sf;
bool enable_fast_math = true;
Ort::ThrowOnError(OrtSessionOptionsAppendExecutionProvider_ACL(sf, enable_fast_math));
```

The C API details are [here](../../get-started/with-c.html).

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#python) Python 

``` highlight
import onnxruntime

providers = [("ACLExecutionProvider", )]
sess = onnxruntime.InferenceSession("model.onnx", providers=providers)
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#performance-tuning) Performance Tuning

Arm Compute Library has a fast math mode that can increase performance with some potential decrease in accuracy for MatMul and Conv operators. It is disabled by default.

When using [onnxruntime_perf_test](https://github.com/microsoft/onnxruntime/tree/main/onnxruntime/test/perftest), use the flag `-e acl` to enable the ACL Execution Provider. You can additionally use `-i 'enable_fast_math|true'` to enable fast math.

Arm Compute Library uses the ONNX Runtime intra-operator thread pool when running via the execution provider. You can control the size of this thread pool using the `-x` option.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#supported-operators) Supported Operators

  Operator               Supported types
  ---------------------- -------------------------
  AveragePool            float
  BatchNormalization     float
  Concat                 float
  Conv                   float, float16
  FusedConv              float
  FusedMatMul            float, float16
  Gemm                   float
  GlobalAveragePool      float
  GlobalMaxPool          float
  MatMul                 float, float16
  MatMulIntegerToFloat   uint8, int8, uint8+int8
  MaxPool                float
  NhwcConv               float
  Relu                   float
  QLinearConv            uint8, int8, uint8+int8