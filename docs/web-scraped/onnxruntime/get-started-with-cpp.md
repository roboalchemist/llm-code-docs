# Source: https://onnxruntime.ai/docs/get-started/with-cpp.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#get-started-with-ort-for-c) Get started with ORT for C++ 

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contents) Contents 

- [Builds](#builds)
- [API Reference](#api-reference)
- [Samples](#samples)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#builds) Builds

  Artifact                                                                                                Description                                Supported Platforms
  ------------------------------------------------------------------------------------------------------- ------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------
  [Microsoft.ML.OnnxRuntime](https://www.nuget.org/packages/Microsoft.ML.OnnxRuntime)                     CPU (Release)                              Windows, Linux, Mac, X64, X86 (Windows-only), ARM64 (Windows-only)...more details: [compatibility](/docs/reference/compatibility.html)
  [Microsoft.ML.OnnxRuntime.Gpu](https://www.nuget.org/packages/Microsoft.ML.OnnxRuntime.gpu)             GPU - CUDA (Release)                       Windows, Linux, Mac, X64...more details: [compatibility](/docs/reference/compatibility.html)
  [Microsoft.ML.OnnxRuntime.DirectML](https://www.nuget.org/packages/Microsoft.ML.OnnxRuntime.directml)   GPU - DirectML (Release)                   Windows 10 1709+
  [onnxruntime](https://aiinfra.visualstudio.com/PublicPackages/_packaging?_a=feed&feed=ORT-Nightly)      CPU, GPU (Dev), CPU (On-Device Training)   Same as Release versions
  [Microsoft.ML.OnnxRuntime.Training](https://www.nuget.org/packages/Microsoft.ML.OnnxRuntime)            CPU On-Device Training (Release)           Windows, Linux, Mac, X64, X86 (Windows-only), ARM64 (Windows-only)...more details: [compatibility](/docs/reference/compatibility.html)

.zip and .tgz files are also included as assets in each [Github release](https://github.com/microsoft/onnxruntime/releases).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#api-reference) API Reference

The C++ API is a thin wrapper of the C API. Please refer to [C API](/docs/get-started/with-c.html) for more details.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#samples) Samples

See [Tutorials: API Basics - C++](../tutorials/api-basics)