# Source: https://onnxruntime.ai/docs/genai/howto/install.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-onnx-runtime-generate-api) Install ONNX Runtime generate() API 

- [Python package installation](#python-package-installation)
  - [CPU](#cpu)
  - [DirectML](#directml)
  - [CUDA](#cuda)
    - [CUDA 12](#cuda-12)
    - [CUDA 11](#cuda-11)
- [Nuget package installation](#nuget-package-installation)
  - [Pre-requisites](#pre-requisites)
    - [ONNX Runtime dependency](#onnx-runtime-dependency)
  - [CPU](#cpu-1)
  - [CUDA](#cuda-1)
  - [DirectML](#directml-1)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#python-package-installation) Python package installation

Note: only one of these sets of packages (CPU, DirectML, CUDA) should be installed in your environment.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#cpu) CPU

``` highlight
pip install onnxruntime-genai
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#directml) DirectML

``` highlight
pip install onnxruntime-genai-directml
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#cuda) CUDA

If you are installing the CUDA variant of onnxruntime-genai, the CUDA toolkit must be installed.

The CUDA toolkit can be downloaded from the [CUDA Toolkit Archive](https://developer.nvidia.com/cuda-toolkit-archive).

Ensure that the `CUDA_PATH` environment variable is set to the location of your CUDA installation.

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#cuda-12) CUDA 12

``` highlight
pip install onnxruntime-genai-cuda
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#cuda-11) CUDA 11

To use this API with CUDA 11, you need to [build and install from source](/docs/genai/howto/build-from-source.html).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#nuget-package-installation) Nuget package installation

Note: install only one of these packages (CPU, DirectML, CUDA) in your project.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#pre-requisites) Pre-requisites

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#onnx-runtime-dependency) ONNX Runtime dependency

ONNX Runtime generate() versions 0.3.0 and earlier came bundled with the core ONNX Runtime binaries. From version 0.4.0 onwards, the packages are separated to allow a more flexible developer experience.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#cpu-1) CPU

``` highlight
dotnet add package Microsoft.ML.OnnxRuntimeGenAI
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#cuda-1) CUDA

Note: only CUDA 11 is supported for versions 0.3.0 and earlier, and only CUDA 12 is supported for versions 0.4.0 and later.

``` highlight
dotnet add package Microsoft.ML.OnnxRuntimeGenAI.Cuda
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#directml-1) DirectML

``` highlight
dotnet add package Microsoft.ML.OnnxRuntimeGenAI.DirectML
```