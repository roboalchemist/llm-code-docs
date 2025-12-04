# Source: https://onnxruntime.ai/docs/install/

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-onnx-runtime) Install ONNX Runtime

See the [installation matrix](https://onnxruntime.ai) for recommended instructions for desired combinations of target operating system, hardware, accelerator, and language.

Details on OS versions, compilers, language versions, dependent libraries, etc can be found under [Compatibility](../reference/compatibility).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contents) Contents 

- [Requirements](#requirements)
  - [CUDA and CuDNN](#cuda-and-cudnn)
- [Python Installs](#python-installs)
  - [Install ONNX Runtime CPU](#install-onnx-runtime-cpu)
    - [Install nightly](#install-nightly)
  - [Install ONNX Runtime GPU (DirectML) - Sustained Engineering Mode](#install-onnx-runtime-gpu-directml---sustained-engineering-mode)
    - [Install nightly](#install-nightly-1)
  - [Install ONNX Runtime GPU (CUDA or TensorRT)](#install-onnx-runtime-gpu-cuda-or-tensorrt)
    - [CUDA 12.x](#cuda-12x)
    - [Nightly for CUDA 13.x](#nightly-for-cuda-13x)
    - [Nightly for CUDA 12.x](#nightly-for-cuda-12x)
    - [CUDA 11.x](#cuda-11x)
  - [Install ONNX Runtime QNN](#install-onnx-runtime-qnn)
    - [Install nightly](#install-nightly-2)
  - [Install ONNX Runtime GPU (ROCm)](#install-onnx-runtime-gpu-rocm)
- [C#/C/C++/WinML Installs](#cccwinml-installs)
  - [Install ONNX Runtime](#install-onnx-runtime-1)
    - [Install ONNX Runtime CPU](#install-onnx-runtime-cpu-1)
    - [Install ONNX Runtime GPU (CUDA 12.x)](#install-onnx-runtime-gpu-cuda-12x)
    - [Install ONNX Runtime GPU (CUDA 11.8)](#install-onnx-runtime-gpu-cuda-118)
    - [DirectML (sustained engineering - use WinML for new projects)](#directml-sustained-engineering---use-winml-for-new-projects)
    - [WinML (recommended for Windows)](#winml-recommended-for-windows)
- [Install on web and mobile](#install-on-web-and-mobile)
  - [JavaScript Installs](#javascript-installs)
    - [Install ONNX Runtime Web (browsers)](#install-onnx-runtime-web-browsers)
    - [Install ONNX Runtime Node.js binding (Node.js)](#install-onnx-runtime-nodejs-binding-nodejs)
    - [Install ONNX Runtime for React Native](#install-onnx-runtime-for-react-native)
  - [Install on iOS](#install-on-ios)
    - [C/C++](#cc)
    - [Objective-C](#objective-c)
    - [Custom build](#custom-build)
  - [Install on Android](#install-on-android)
    - [Java/Kotlin](#javakotlin)
    - [C/C++](#cc-1)
    - [Custom build](#custom-build-1)
- [Install for On-Device Training](#install-for-on-device-training)
  - [Offline Phase - Prepare for Training](#offline-phase---prepare-for-training)
  - [Training Phase - On-Device Training](#training-phase---on-device-training)
- [Large Model Training](#large-model-training)
- [Inference install table for all languages](#inference-install-table-for-all-languages)
- [Training install table for all languages](#training-install-table-for-all-languages)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#requirements) Requirements

- All builds require the English language package with `en_US.UTF-8` locale. On Linux, install [language-pack-en package](https://packages.ubuntu.com/search?keywords=language-pack-en) by running `locale-gen en_US.UTF-8` and `update-locale LANG=en_US.UTF-8`

- Windows builds require [Visual C++ 2019 runtime](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#latest-microsoft-visual-c-redistributable-version). The latest version is recommended.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#cuda-and-cudnn) CUDA and CuDNN

For ONNX Runtime GPU package, it is required to install [CUDA](https://developer.nvidia.com/cuda-toolkit) and [cuDNN](https://developer.nvidia.com/cudnn). Check [CUDA execution provider requirements](/docs/execution-providers/CUDA-ExecutionProvider.html#requirements) for compatible version of CUDA and cuDNN.

- Zlib is required by cuDNN 9.x for Linux only (zlib is statically linked into the cuDNN 9.x Windows dynamic libraries), or cuDNN 8.x for Linux and Windows. Follow the [cuDNN 8.9 installation guide](https://docs.nvidia.com/deeplearning/cudnn/archives/cudnn-890/install-guide/index.html) to install zlib in Linux or Windows.
- In Windows, the path of CUDA `bin` and cuDNN `bin` directories must be added to the `PATH` environment variable.
- In Linux, the path of CUDA `lib64` and cuDNN `lib` directories must be added to the `LD_LIBRARY_PATH` environment variable.

For `onnxruntime-gpu` package, it is possible to work with PyTorch without the need for manual installations of CUDA or cuDNN. Refer to [Compatibility with PyTorch](/docs/execution-providers/CUDA-ExecutionProvider.html#compatibility-with-pytorch) for more information.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#python-installs) Python Installs

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-onnx-runtime-cpu) Install ONNX Runtime CPU

``` highlight
pip install onnxruntime
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-nightly) Install nightly

``` highlight
pip install coloredlogs flatbuffers numpy packaging protobuf sympy
pip install --pre --index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/ORT-Nightly/pypi/simple/ onnxruntime
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-onnx-runtime-gpu-directml---sustained-engineering-mode) Install ONNX Runtime GPU (DirectML) - Sustained Engineering Mode

**Note**: DirectML is in sustained engineering. For new Windows projects, consider [WinML](#winml-recommended-for-windows) instead.

``` highlight
pip install onnxruntime-directml
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-nightly-1) Install nightly

``` highlight
pip install coloredlogs flatbuffers numpy packaging protobuf sympy
pip install --pre --index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/ORT-Nightly/pypi/simple/ onnxruntime-directml
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-onnx-runtime-gpu-cuda-or-tensorrt) Install ONNX Runtime GPU (CUDA or TensorRT)

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#cuda-12x) CUDA 12.x 

The default CUDA version for [onnxruntime-gpu in pypi](https://pypi.org/project/onnxruntime-gpu) is 12.x since 1.19.0.

``` highlight
pip install onnxruntime-gpu
```

For previous versions, you can download here: [1.18.1](https://aiinfra.visualstudio.com/PublicPackages/_artifacts/feed/onnxruntime-cuda-12/PyPI/onnxruntime-gpu/overview/1.18.1), [1.18.0](https://aiinfra.visualstudio.com/PublicPackages/_artifacts/feed/onnxruntime-cuda-12/PyPI/onnxruntime-gpu/overview/1.18.0)

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#nightly-for-cuda-13x) Nightly for CUDA 13.x 

``` highlight
pip install coloredlogs flatbuffers numpy packaging protobuf sympy
pip install --pre --index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/ort-cuda-13-nightly/pypi/simple/ onnxruntime-gpu
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#nightly-for-cuda-12x) Nightly for CUDA 12.x 

``` highlight
pip install coloredlogs flatbuffers numpy packaging protobuf sympy
pip install --pre --index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/ORT-Nightly/pypi/simple/ onnxruntime-gpu
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#cuda-11x) CUDA 11.x 

For Cuda 11.x, please use the following instructions to install from [ORT Azure Devops Feed](https://aiinfra.visualstudio.com/PublicPackages/_artifacts/feed/onnxruntime-cuda-11/PyPI/onnxruntime-gpu/overview) for 1.19.2 or later.

``` highlight
pip install coloredlogs flatbuffers numpy packaging protobuf sympy
pip install onnxruntime-gpu --index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/onnxruntime-cuda-11/pypi/simple/
```

For previous versions, you can download here: [1.18.1](https://pypi.org/project/onnxruntime-gpu/1.18.1/), [1.18.0](https://pypi.org/project/onnxruntime-gpu/1.18.0/)

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-onnx-runtime-qnn) Install ONNX Runtime QNN

``` highlight
pip install onnxruntime-qnn
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-nightly-2) Install nightly

``` highlight
pip install coloredlogs flatbuffers numpy packaging protobuf sympy
pip install --pre --index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/ORT-Nightly/pypi/simple/ onnxruntime-qnn
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-onnx-runtime-gpu-rocm) Install ONNX Runtime GPU (ROCm)

For ROCm, please follow instructions to install it at the [AMD ROCm install docs](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.2.0/). The ROCm execution provider for ONNX Runtime is built and tested with ROCm 6.2.0.

To build from source on Linux, follow the instructions [here](https://onnxruntime.ai/docs/build/eps.html#amd-rocm).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#cccwinml-installs) C#/C/C++/WinML Installs

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-onnx-runtime-1) Install ONNX Runtime

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-onnx-runtime-cpu-1) Install ONNX Runtime CPU

``` highlight
# CPU
dotnet add package Microsoft.ML.OnnxRuntime
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-onnx-runtime-gpu-cuda-12x) Install ONNX Runtime GPU (CUDA 12.x) 

The default CUDA version for ORT is 12.x

``` highlight
# GPU
dotnet add package Microsoft.ML.OnnxRuntime.Gpu
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-onnx-runtime-gpu-cuda-118) Install ONNX Runtime GPU (CUDA 11.8) 

1.  Project Setup

Ensure you have installed the latest version of the Azure Artifacts keyring from the its [Github Repo](https://github.com/microsoft/artifacts-credprovider#azure-artifacts-credential-provider).\
Add a nuget.config file to your project in the same directory as your .csproj file.

``` highlight
<?xml version="1.0" encoding="utf-8"?>
<configuration>
    <packageSources>
        <clear/>
        <add key="onnxruntime-cuda-11"
             value="https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/onnxruntime-cuda-11/nuget/v3/index.json"/>
    </packageSources>
</configuration>
```

1.  Restore packages

Restore packages (using the interactive flag, which allows dotnet to prompt you for credentials)

``` highlight
dotnet add package Microsoft.ML.OnnxRuntime.Gpu
```

Note: You don't need --interactive every time. dotnet will prompt you to add --interactive if it needs updated credentials.

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#directml-sustained-engineering---use-winml-for-new-projects) DirectML (sustained engineering - use WinML for new projects)

``` highlight
dotnet add package Microsoft.ML.OnnxRuntime.DirectML
```

**Note**: DirectML is in sustained engineering. For new Windows projects, use WinML instead:

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#winml-recommended-for-windows) WinML (recommended for Windows)

``` highlight
dotnet add package Microsoft.AI.MachineLearning
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-on-web-and-mobile) Install on web and mobile

The pre-built packages have full support for all ONNX opsets and operators.

If the pre-built package is too large, you can create a [custom build](/docs/build/custom.html). A custom build can include just the opsets and operators in your model/s to reduce the size.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#javascript-installs) JavaScript Installs

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-onnx-runtime-web-browsers) Install ONNX Runtime Web (browsers)

``` highlight
# install latest release version
npm install onnxruntime-web

# install nightly build dev version
npm install onnxruntime-web@dev
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-onnx-runtime-nodejs-binding-nodejs) Install ONNX Runtime Node.js binding (Node.js) 

``` highlight
# install latest release version
npm install onnxruntime-node
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-onnx-runtime-for-react-native) Install ONNX Runtime for React Native

``` highlight
# install latest release version
npm install onnxruntime-react-native
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-on-ios) Install on iOS

In your CocoaPods `Podfile`, add the `onnxruntime-c` or `onnxruntime-objc` pod, depending on which API you want to use.

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#cc) C/C++

``` highlight
  use_frameworks!

  pod 'onnxruntime-c'
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#objective-c) Objective-C

``` highlight
  use_frameworks!

  pod 'onnxruntime-objc'
```

Run `pod install`.

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#custom-build) Custom build

Refer to the instructions for creating a [custom iOS package](/docs/build/custom.html#ios).

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-on-android) Install on Android

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#javakotlin) Java/Kotlin

In your Android Studio Project, make the following changes to:

1.  build.gradle (Project):

    :::: 
    ::: highlight
    ``` highlight
     repositories 
    ```
    :::
    ::::

2.  build.gradle (Module):

    :::: 
    ::: highlight
    ``` highlight
     dependencies 
    ```
    :::
    ::::

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#cc-1) C/C++

Download the [onnxruntime-android](https://mvnrepository.com/artifact/com.microsoft.onnxruntime/onnxruntime-android) AAR hosted at MavenCentral, change the file extension from `.aar` to `.zip`, and unzip it. Include the header files from the `headers` folder, and the relevant `libonnxruntime.so` dynamic library from the `jni` folder in your NDK project.

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#custom-build-1) Custom build

Refer to the instructions for creating a [custom Android package](/docs/build/custom.html#android).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-for-on-device-training) Install for On-Device Training

Unless stated otherwise, the installation instructions in this section refer to pre-built packages designed to perform on-device training.

If the pre-built training package supports your model but is too large, you can create a [custom training build](/docs/build/custom.html).

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#offline-phase---prepare-for-training) Offline Phase - Prepare for Training

``` highlight
python -m pip install cerberus flatbuffers h5py numpy>=1.16.6 onnx packaging protobuf sympy setuptools>=41.4.0
pip install -i https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/ORT/pypi/simple/ onnxruntime-training-cpu
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#training-phase---on-device-training) Training Phase - On-Device Training

+-----------------+------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Device          | Language               | PackageName                                                                                                               | Installation Instructions                                                                                                                                                   |
+=================+========================+===========================================================================================================================+=============================================================================================================================================================================+
| Windows         | C, C++, C#             | [Microsoft.ML.OnnxRuntime.Training](https://www.nuget.org/packages/Microsoft.ML.OnnxRuntime)                              | `dotnet add package Microsoft.ML.OnnxRuntime.Training`                                                                                                                      |
+-----------------+------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Linux           | C, C++                 | [onnxruntime-training-linux\*.tgz](https://github.com/microsoft/onnxruntime/releases)                                     | - Download the `*.tgz` file from [here](https://github.com/microsoft/onnxruntime/releases).                                                                                 |
|                 |                        |                                                                                                                           | - Extract it.                                                                                                                                                               |
|                 |                        |                                                                                                                           | - Move and include the header files in the `include` directory.                                                                                                             |
|                 |                        |                                                                                                                           | - Move the `libonnxruntime.so` dynamic library to a desired path and include it.                                                                                            |
+-----------------+------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                 | Python                 | [onnxruntime-training](https://pypi.org/project/onnxruntime-training/)                                                    | `pip install onnxruntime-training`                                                                                                                                          |
+-----------------+------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Android         | C, C++                 | [onnxruntime-training-android](https://mvnrepository.com/artifact/com.microsoft.onnxruntime/onnxruntime-training-android) | - Download the [onnxruntime-training-android (full package)](https://mvnrepository.com/artifact/com.microsoft.onnxruntime/onnxruntime-android) AAR hosted at Maven Central. |
|                 |                        |                                                                                                                           | - Change the file extension from `.aar` to `.zip`, and unzip it.                                                                                                            |
|                 |                        |                                                                                                                           | - Include the header files from the `headers` folder.                                                                                                                       |
|                 |                        |                                                                                                                           | - Include the relevant `libonnxruntime.so` dynamic library from the `jni` folder in your NDK project.                                                                       |
+-----------------+------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                 | Java/Kotlin            | [onnxruntime-training-android](https://mvnrepository.com/artifact/com.microsoft.onnxruntime/onnxruntime-android)          | In your Android Studio Project, make the following changes to:                                                                                                              |
|                 |                        |                                                                                                                           |                                                                                                                                                                             |
|                 |                        |                                                                                                                           | 1.  build.gradle (Project): ` repositories  `                                                                                                             |
|                 |                        |                                                                                                                           | 2.  build.gradle (Module): ` dependencies  `                                      |
+-----------------+------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| iOS             | C, C++                 | **CocoaPods: onnxruntime-training-c**                                                                                     | - In your CocoaPods `Podfile`, add the `onnxruntime-training-c` pod:                                                                                                        |
|                 |                        |                                                                                                                           |                                                                                                                                                                             |
|                 |                        |                                                                                                                           |                                                                                                                                                                             |
|                 |                        |                                                                                                                           |       use_frameworks!                                                                                                                                                       |
|                 |                        |                                                                                                                           |       pod 'onnxruntime-training-c'                                                                                                                                          |
|                 |                        |                                                                                                                           |                                                                                                                                                                             |
|                 |                        |                                                                                                                           |                                                                                                                                                                             |
|                 |                        |                                                                                                                           | - Run `pod install`.                                                                                                                                                        |
+-----------------+------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                 | Objective-C            | **CocoaPods: onnxruntime-training-objc**                                                                                  | - In your CocoaPods `Podfile`, add the `onnxruntime-training-objc` pod:                                                                                                     |
|                 |                        |                                                                                                                           |                                                                                                                                                                             |
|                 |                        |                                                                                                                           |                                                                                                                                                                             |
|                 |                        |                                                                                                                           |       use_frameworks!                                                                                                                                                       |
|                 |                        |                                                                                                                           |       pod 'onnxruntime-training-objc'                                                                                                                                       |
|                 |                        |                                                                                                                           |                                                                                                                                                                             |
|                 |                        |                                                                                                                           |                                                                                                                                                                             |
|                 |                        |                                                                                                                           | - Run `pod install`.                                                                                                                                                        |
+-----------------+------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Web             | JavaScript, TypeScript | onnxruntime-web                                                                                                           |     npm install onnxruntime-web                                                                                                                                             |
|                 |                        |                                                                                                                           |                                                                                                                                                                             |
|                 |                        |                                                                                                                           | - Use either `import * as ort from 'onnxruntime-web/training';` or `const ort = require('onnxruntime-web/training');`                                                       |
+-----------------+------------------------+---------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#large-model-training) Large Model Training

``` highlight
pip install torch-ort
python -m torch_ort.configure
```

**Note**: This installs the default version of the `torch-ort` and `onnxruntime-training` packages that are mapped to specific versions of the CUDA libraries. Refer to the install options in [onnxruntime.ai](https://onnxruntime.ai).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#inference-install-table-for-all-languages) Inference install table for all languages

The table below lists the build variants available as officially supported packages. Others can be [built from source](../build/inferencing) from each [release branch](https://github.com/microsoft/onnxruntime/tags).

In addition to general [requirements](#requirements), please note additional requirements and dependencies in the table below:

                                      Official build                                                                                                                                        Nightly build                                                                                                                                       Reqs
  ----------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------
  Python                              If using pip, run `pip install --upgrade pip` prior to downloading.                                                                                                                                                                                                
                                      CPU: [**onnxruntime**](https://pypi.org/project/onnxruntime)                                                                                          [onnxruntime (nightly)](https://aiinfra.visualstudio.com/PublicPackages/_artifacts/feed/ORT-Nightly/PyPI/onnxruntime/overview)                       
                                      GPU (CUDA/TensorRT) for CUDA 12.x: [**onnxruntime-gpu**](https://pypi.org/project/onnxruntime-gpu)                                                    [onnxruntime-gpu (nightly)](https://aiinfra.visualstudio.com/PublicPackages/_artifacts/feed/ORT-Nightly/PyPI/onnxruntime-gpu/overview/)             [View](/docs/execution-providers/CUDA-ExecutionProvider.html#requirements)
                                      GPU (DirectML) **sustained engineering**: [**onnxruntime-directml**](https://pypi.org/project/onnxruntime-directml/)                                  [onnxruntime-directml (nightly)](https://aiinfra.visualstudio.com/PublicPackages/_artifacts/feed/ORT-Nightly/PyPI/onnxruntime-directml/overview/)   [View](/docs/execution-providers/DirectML-ExecutionProvider.html#requirements)
                                      OpenVINO: [**intel/onnxruntime**](https://github.com/intel/onnxruntime/releases/latest) - *Intel managed*                                                                                                                                                                                                 [View](/docs/build/eps.html#openvino)
                                      TensorRT (Jetson): [**Jetson Zoo**](https://elinux.org/Jetson_Zoo#ONNX_Runtime) - *NVIDIA managed*                                                                                                                                                                                                         
                                      Azure (Cloud): [**onnxruntime-azure**](https://pypi.org/project/onnxruntime-azure/)                                                                                                                                                                                                                        
  C#/C/C++                            CPU: [**Microsoft.ML.OnnxRuntime**](https://www.nuget.org/packages/Microsoft.ML.OnnxRuntime)                                                          [onnxruntime (nightly)](https://aiinfra.visualstudio.com/PublicPackages/_packaging?_a=feed&feed=ORT-Nightly)                                         
                                      GPU (CUDA/TensorRT): [**Microsoft.ML.OnnxRuntime.Gpu**](https://www.nuget.org/packages/Microsoft.ML.OnnxRuntime.gpu)                                  [onnxruntime (nightly)](https://aiinfra.visualstudio.com/PublicPackages/_packaging?_a=feed&feed=ORT-Nightly)                                        [View](../execution-providers/CUDA-ExecutionProvider)
                                      GPU (DirectML) **sustained engineering**: [**Microsoft.ML.OnnxRuntime.DirectML**](https://www.nuget.org/packages/Microsoft.ML.OnnxRuntime.DirectML)   [onnxruntime (nightly)](https://aiinfra.visualstudio.com/PublicPackages/_artifacts/feed/ORT-Nightly/PyPI/ort-nightly-directml/overview)             [View](../execution-providers/DirectML-ExecutionProvider)
  WinML **recommended for Windows**   [**Microsoft.AI.MachineLearning**](https://www.nuget.org/packages/Microsoft.AI.MachineLearning)                                                       [onnxruntime (nightly)](https://aiinfra.visualstudio.com/PublicPackages/_artifacts/feed/ORT-Nightly/NuGet/Microsoft.AI.MachineLearning/overview)    [View](https://docs.microsoft.com/en-us/windows/ai/windows-ml/port-app-to-nuget#prerequisites)
  Java                                CPU: [**com.microsoft.onnxruntime:onnxruntime**](https://search.maven.org/artifact/com.microsoft.onnxruntime/onnxruntime)                                                                                                                                                                                 [View](../api/java)
                                      GPU (CUDA/TensorRT): [**com.microsoft.onnxruntime:onnxruntime_gpu**](https://search.maven.org/artifact/com.microsoft.onnxruntime/onnxruntime_gpu)                                                                                                                                                         [View](../api/java)
  Android                             [**com.microsoft.onnxruntime:onnxruntime-android**](https://search.maven.org/artifact/com.microsoft.onnxruntime/onnxruntime-android)                                                                                                                                                                      [View](/docs/install/#install-on-android)
  iOS (C/C++)                         CocoaPods: **onnxruntime-c**                                                                                                                                                                                                                                                                              [View](/docs/install/#install-on-ios)
  Objective-C                         CocoaPods: **onnxruntime-objc**                                                                                                                                                                                                                                                                           [View](/docs/install/#install-on-ios)
  React Native                        [**onnxruntime-react-native** (latest)](https://www.npmjs.com/package/onnxruntime-react-native)                                                       [onnxruntime-react-native (dev)](https://www.npmjs.com/package/onnxruntime-react-native?activeTab=versions)                                         [View](../api/js)
  Node.js                             [**onnxruntime-node** (latest)](https://www.npmjs.com/package/onnxruntime-node)                                                                       [onnxruntime-node (dev)](https://www.npmjs.com/package/onnxruntime-node?activeTab=versions)                                                         [View](../api/js)
  Web                                 [**onnxruntime-web** (latest)](https://www.npmjs.com/package/onnxruntime-web)                                                                         [onnxruntime-web (dev)](https://www.npmjs.com/package/onnxruntime-web?activeTab=versions)                                                           [View](../api/js)

*Note: Nightly builds created from the main branch are available for testing newer changes between official releases. Please use these at your own risk. We strongly advise against deploying these to production workloads as support is limited for nightly builds.*

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#training-install-table-for-all-languages) Training install table for all languages

Refer to the getting started with [Optimized Training](https://onnxruntime.ai/getting-started) page for more fine-grained installation instructions.