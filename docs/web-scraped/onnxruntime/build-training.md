# Source: https://onnxruntime.ai/docs/build/training.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-for-on-device-training) Build for On-Device Training 

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#prerequisites) Prerequisites

- Python 3.x
- CMake

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-instructions-for-the-training-phase) Build Instructions for the Training Phase

1.  Clone the repository

    :::: 
    ::: highlight
    ``` highlight
     git clone --recursive https://github.com/Microsoft/onnxruntime.git
     cd onnxruntime
    ```
    :::
    ::::

2.  Build ONNX Runtime for `On-Device Training`

    a\. For Windows

    :::: 
    ::: highlight
    ``` highlight
     .\build.bat --config RelWithDebInfo --cmake_generator "Visual Studio 17 2022" --build_shared_lib --parallel --enable_training_apis
    ```
    :::
    ::::

    b\. For Linux

    :::: 
    ::: highlight
    ``` highlight
     ./build.sh --config RelWithDebInfo --build_shared_lib --parallel --enable_training_apis
    ```
    :::
    ::::

    c\. For Android

    Refer to the [Android build instructions](/docs/build/android.html) and add the `--enable_training_apis` build flag.

    d\. For MacOS

    Refer to the [macOS inference build instructions](/docs/build/inferencing.html) and add the `--enable_training_apis` build flag.

    e\. For iOS

    Refer to the [iOS build instructions](/docs/build/ios.html) and add the `--enable_training_apis` build flag.

    f\. For web

    Refer to the [web build instructions](/docs/build/web.html).

> **Note**
>
> - To build the C# bindings, add the `--build_nuget` flag to the build command above.
>
> - To build the Python wheel:
>   - add the `--build_wheel` flag to the build command above.
>   - install the wheel using `python -m pip install build/Linux/RelWithDebInfo/dist/*.whl`
>
> - The `config` flag can be one of `Debug`, `RelWithDebInfo`, `Release`, `MinSizeRel`. Use the one that suits your use case.
>
> - The `--enable_training_apis` flag can be used in conjunction with the `--minimal_build` flag.
>
> - The offline phase of generating the training artifacts can only be done with Python (using the `--build_wheel` flag).
>
> - The build commands above only build for the cpu execution provider. To build for cuda execution provider, add these flags
>   - `--use_cuda`
>   - `--cuda_home `
>   - `--cudnn_home `
>   - `--cuda_version=`

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-for-large-model-training) Build for Large Model Training 

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contents) Contents 

- [Prerequisites](#prerequisites)
- [Build Instructions for the Training Phase](#build-instructions-for-the-training-phase)
  - [Linux](#linux)
- [GPU / CUDA](#gpu--cuda)
- [GPU / ROCm](#gpu--rocm)
- [DNNL and MKLML](#dnnl-and-mklml)
  - [Linux](#linux-1)
  - [Windows](#windows)

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#linux) Linux

``` highlight
./build.sh --config RelWithDebInfo --build_shared_lib --parallel --enable_training
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#gpu--cuda) GPU / CUDA 

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#prerequisites-1) Prerequisites 

The default NVIDIA GPU build requires CUDA runtime libraries installed on the system:

- [CUDA](https://developer.nvidia.com/cuda-toolkit)
- [cuDNN](https://developer.nvidia.com/cudnn)

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-instructions) Build instructions 

1.  Checkout this code repo with

    :::: 
    ::: highlight
    ``` highlight
     git clone https://github.com/microsoft/onnxruntime
     cd onnxruntime
    ```
    :::
    ::::

2.  Set the environment variables: *adjust the paths for locations on your build machine*

    :::: 
    ::: highlight
    ``` highlight
     export CUDA_HOME=<location for CUDA libs> # e.g. /usr/local/cuda
     export CUDNN_HOME=<location for cuDNN libs> # e.g. /usr/local/cuda
     export CUDACXX=<location for NVCC> #e.g. /usr/local/cuda/bin/nvcc
    ```
    :::
    ::::

3.  Create the ONNX Runtime Python wheel

    :::: 
    ::: highlight
    ``` highlight
    ./build.sh --config=RelWithDebInfo --enable_training --build_wheel --use_cuda --cuda_home  --cudnn_home  --cuda_version=
    ```
    :::
    ::::

4.  Install the .whl file in `./build/Linux/RelWithDebInfo/dist` for ONNX Runtime Training.

    :::: 
    ::: highlight
    ``` highlight
     python -m pip install build/Linux/RelWithDebInfo/dist/*.whl
    ```
    :::
    ::::

That's it! Once the build is complete, you should be able to use the ONNX Runtime libraries and executables in your projects. Note that these steps are general and may need to be adjusted based on your specific environment and requirements. For more information, you can ask for help on the [ONNX Runtime GitHub community](https://github.com/microsoft/onnxruntime/discussions/new?category=q-a).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#gpu--rocm) GPU / ROCm 

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#prerequisites-2) Prerequisites 

The default AMD GPU build requires ROCm software toolkit installed on the system:

- [ROCm](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.0.0/) 6.0.0

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-instructions-1) Build instructions 

1.  Checkout this code repo with

    :::: 
    ::: highlight
    ``` highlight
     git clone https://github.com/microsoft/onnxruntime
     cd onnxruntime
    ```
    :::
    ::::

2.  Create the ONNX Runtime Python wheel

    :::: 
    ::: highlight
    ``` highlight
    ./build.sh --config Release --enable_training --build_wheel --parallel --skip_tests --use_rocm --rocm_home /opt/rocm
    ```
    :::
    ::::

3.  Install the .whl file in `./build/Linux/RelWithDebInfo/dist` for ONNX Runtime Training.

    :::: 
    ::: highlight
    ``` highlight
     python -m pip install build/Linux/RelWithDebInfo/dist/*.whl
    ```
    :::
    ::::

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#dnnl-and-mklml) DNNL and MKLML

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-instructions-2) Build Instructions 

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#linux-1) Linux

`./build.sh --enable_training --use_dnnl`

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#windows) Windows

`.\build.bat --enable_training --use_dnnl`

Add `--build_wheel` to build the ONNX Runtime wheel.

This will produce a .whl file in `build/Linux/RelWithDebInfo/dist` for ONNX Runtime Training.