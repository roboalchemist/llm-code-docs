# Source: https://onnxruntime.ai/docs/tutorials/csharp/csharp-gpu.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#configure-cuda-and-cudnn-for-gpu-with-onnx-runtime-and-c-on-windows-11) Configure CUDA and cuDNN for GPU with ONNX Runtime and C# on Windows 11

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#prerequisites) Prerequisites 

- Windows 11
- Visual Studio 2019 or 2022

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#steps-to-configure-cuda-and-cudnn-for-onnx-runtime-with-c-on-windows-11) Steps to Configure CUDA and cuDNN for ONNX Runtime with C# on Windows 11

- [Download and install the CUDA toolkit](https://developer.nvidia.com/cuda-toolkit-archive) based on the supported version for the ONNX Runtime Version.

- [Download and install the cuDNN version](https://developer.nvidia.com/rdp/cudnn-archive) based on the supported version for the ONNX Runtime Version.

See this table for supported versions:

  ONNX Runtime Version   CUDA Toolkit Version   cuDNN Version
  ---------------------- ---------------------- ---------------
  1.13 - 1.16            11.6                   8.5.0.96
  1.9 - 1.12             11.4                   8.2.2.26

NOTE: Full table can be found [here](https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html#requirements)

- Follow section [2. Installing cuDNN on Windows](https://docs.nvidia.com/deeplearning/cudnn/installation/latest/windows.html). NOTE: Skip step 5 in section 2.3 on updating Visual Studio settings, this is only for C++ projects.

- Restart your computer and verify the installation by running the following command or in python with PyTorch:

``` highlight
nvcc --version
```

``` highlight
import torch
torch.cuda.is_available()
```

- Now you can enable GPU in the C# ONNX Runtime API with the following code:

``` highlight
// keep in mind almost all of the classes are disposable.
using var gpuSessionOptions = SessionOptions.MakeSessionOptionWithCudaProvider(0);
using var session = new InferenceSession(modelPath, gpuSessionOptions);
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#checkout-more-c-onnx-runtime-resources) Checkout more C# ONNX Runtime resources

- [C# API Doc](https://onnxruntime.ai/docs/api/csharp/api)
- [Get Started with C# in ONNX Runtime](https://onnxruntime.ai/docs/get-started/with-csharp.html)