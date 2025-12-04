# Source: https://onnxruntime.ai/docs/genai/howto/build-from-source.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-the-generate-api-from-source) Build the generate() API from source 

- [Pre-requisites](#pre-requisites)
- [Clone the onnxruntime-genai repo](#clone-the-onnxruntime-genai-repo)
- [Build the generate() API](#build-the-generate-api)
  - [Build Python API](#build-python-api)
    - [Windows CPU build](#windows-cpu-build)
    - [Windows DirectML build](#windows-directml-build)
    - [Windows NvTensorRtRtx build](#windows-nvtensorrtrtx-build)
    - [Linux build](#linux-build)
    - [Linux CUDA build](#linux-cuda-build)
    - [Mac build](#mac-build)
  - [Build Java API](#build-java-api)
  - [Build for Android](#build-for-android)
- [Install the library into your application](#install-the-library-into-your-application)
  - [Install Python wheel](#install-python-wheel)
  - [Install NuGet](#install-nuget)
  - [Install JAR](#install-jar)
  - [Install AAR](#install-aar)
  - [Install C/C++ header file and library](#install-cc-header-file-and-library)
    - [Windows](#windows)
    - [Linux](#linux)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#pre-requisites) Pre-requisites

- `cmake`
- `.NET6` (if building C#)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#clone-the-onnxruntime-genai-repo) Clone the onnxruntime-genai repo

``` highlight
git clone https://github.com/microsoft/onnxruntime-genai
cd onnxruntime-genai
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-the-generate-api) Build the generate() API

This step assumes that you are in the root of the onnxruntime-genai repo.

All of the build commands below have a `--config` argument, which takes the following options:

- `Release` builds release binaries
- `Debug` build binaries with debug symbols
- `RelWithDebInfo` builds release binaries with debug info

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-python-api) Build Python API

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#windows-cpu-build) Windows CPU build

``` highlight
python build.py --config Release
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#windows-directml-build) Windows DirectML build

``` highlight
python build.py --use_dml --config Release
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#windows-nvtensorrtrtx-build) Windows NvTensorRtRtx build

``` highlight
python build.py --use_trt_rtx --config Release --cuda_home <cuda_path>
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#linux-build) Linux build

``` highlight
python build.py --config Release
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#linux-cuda-build) Linux CUDA build

``` highlight
python build.py --use_cuda --config Release
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#mac-build) Mac build

``` highlight
python build.py --config Release
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-java-api) Build Java API

``` highlight
python build.py --build_java --config Release
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-for-android) Build for Android

If building on Windows, install `ninja`.

``` highlight
pip install ninja
```

Run the build script.

``` highlight
python build.py --build_java --android --android_home <path to your Android SDK> --android_ndk_path <path to your NDK installation> --android_abi  [armeabi-v7a|arm64-v8a|x86|x86_64] --config Release
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-the-library-into-your-application) Install the library into your application

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-python-wheel) Install Python wheel

``` highlight
# Change dir to the folder containing the onnxruntime-genai wheel
# Example for Linux: cd build/Linux/Release/wheel/
pip install *.whl
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-nuget) Install NuGet

*Coming soon*

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-jar) Install JAR

Copy `build/Windows/Release/src/java/build/libs/*.jar` into your application.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-aar) Install AAR

Copy `build/Android/Release/src/java/build/android/outputs/aar/onnxruntime-genai-release.aar` into your application.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-cc-header-file-and-library) Install C/C++ header file and library

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#windows) Windows

Use the header in `src\ort_genai.h` and the libraries in `build\Windows\Release`

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#linux) Linux

Use the header in `src/ort_genai.h` and the libraries in `build/Linux/Release`