# Source: https://onnxruntime.ai/docs/build/eps.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-onnx-runtime-with-execution-providers) Build ONNX Runtime with Execution Providers 

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contents) Contents 

- [Execution Provider Shared Libraries](#execution-provider-shared-libraries)
- [CUDA](#cuda)
  - [Windows](#windows)
  - [Linux](#linux)
  - [Build Options](#build-options)
- [TensorRT](#tensorrt)
  - [**\[Note to ORT 1.21/1.22 open-sourced parser users\]**](#note-to-ort-121122-open-sourced-parser-users)
    - [Windows](#windows-1)
    - [Linux](#linux-1)
- [NVIDIA TensorRT RTX](#nvidia-tensorrt-rtx)
  - [Minimum requirements](#minimum-requirements)
  - [Pre-requisites](#pre-requisites)
  - [Windows](#windows-2)
  - [Linux](#linux-2)
  - [Run unit test](#run-unit-test)
  - [Python wheel](#python-wheel)
- [NVIDIA Jetson TX1/TX2/Nano/Xavier/Orin](#nvidia-jetson-tx1tx2nanoxavierorin)
- [oneDNN](#onednn)
  - [Windows](#windows-3)
  - [Linux](#linux-3)
  - [Windows](#windows-4)
  - [Linux](#linux-4)
  - [Build Phython Wheel](#build-phython-wheel)
- [OpenVINO](#openvino)
  - [Windows](#windows-5)
  - [Linux](#linux-5)
  - [Disable subgraph partition Feature](#disable-subgraph-partition-feature)
- [QNN](#qnn)
  - [Windows (native x86-64 or native Arm64)](#windows-native-x86-64-or-native-arm64)
  - [Windows (Arm64 cross-compile target)](#windows-arm64-cross-compile-target)
  - [Windows (Arm64EC cross-compile target)](#windows-arm64ec-cross-compile-target)
  - [Windows (Arm64X cross-compile target)](#windows-arm64x-cross-compile-target)
  - [Linux (x86_64)](#linux-x86_64)
  - [Android (cross-compile):](#android-cross-compile)
- [DirectML](#directml)
- [Arm Compute Library](#arm-compute-library)
- [Arm NN](#arm-nn)
- [RKNPU](#rknpu)
  - [Linux](#linux-6)
- [AMD Vitis AI](#amd-vitis-ai)
- [AMD MIGraphX](#amd-migraphx)
  - [Linux](#linux-8)
  - [Build Phython Wheel](#build-phython-wheel-1)
- [AMD ROCm](#amd-rocm)
  - [Linux](#linux-9)
  - [Build Phython Wheel](#build-phython-wheel-2)
- [NNAPI](#nnapi)
  - [Create a minimal build with NNAPI EP support](#create-a-minimal-build-with-nnapi-ep-support)
    - [Example build commands with the NNAPI EP enabled](#example-build-commands-with-the-nnapi-ep-enabled)
- [CoreML](#coreml)
  - [Create a minimal build with CoreML EP support](#create-a-minimal-build-with-coreml-ep-support)
- [XNNPACK](#xnnpack)
  - [Build for Android](#build-for-android)
    - [Create a minimal build with XNNPACK EP support](#create-a-minimal-build-with-xnnpack-ep-support)
  - [Build for iOS (available since 1.14)](#build-for-ios-available-since-114)
    - [Create a minimal build with XNNPACK EP support](#create-a-minimal-build-with-xnnpack-ep-support-1)
  - [Build for Windows](#build-for-windows)
  - [Build for Linux](#build-for-linux)
- [CANN](#cann)
  - [Linux](#linux-10)
- [Azure](#azure)
  - [Prerequisites](#prerequisites-9)
  - [Build Instructions](#build-instructions-12)
    - [Windows](#windows-8)
    - [Linux](#linux-11)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#execution-provider-shared-libraries) Execution Provider Shared Libraries

The oneDNN, TensorRT, OpenVINO™, CANN, and QNN providers are built as shared libraries vs being statically linked into the main onnxruntime. This enables them to be loaded only when needed, and if the dependent libraries of the provider are not installed onnxruntime will still run fine, it just will not be able to use that provider. For non shared library providers, all dependencies of the provider must exist to load onnxruntime.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#built-files) Built files 

On Windows, shared provider libraries will be named 'onnxruntime_providers\_\*.dll' (for example onnxruntime_providers_openvino.dll). On Unix, they will be named 'libonnxruntime_providers\_\*.so' On Mac, they will be named 'libonnxruntime_providers\_\*.dylib'.

There is also a shared library that shared providers depend on called onnxruntime_providers_shared (with the same naming convension applied as above).

Note: It is not recommended to put these libraries in a system location or added to a library search path (like LD_LIBRARY_PATH on Unix). If multiple versions of onnxruntime are installed on the system this can make them find the wrong libraries and lead to undefined behavior.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#loading-the-shared-providers) Loading the shared providers 

Shared provider libraries are loaded by the onnxruntime code (do not load or depend on them in your client code). The API for registering shared or non shared providers is identical, the difference is that shared ones will be loaded at runtime when the provider is added to the session options (through a call like OrtSessionOptionsAppendExecutionProvider_OpenVINO or SessionOptionsAppendExecutionProvider_OpenVINO in the C API). If a shared provider library cannot be loaded (if the file doesn't exist, or its dependencies don't exist or not in the path) then an error will be returned.

The onnxruntime code will look for the provider shared libraries in the same location as the onnxruntime shared library is (or the executable statically linked to the static library version).

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#cuda) CUDA

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#prerequisites) Prerequisites 

- Install [CUDA](https://developer.nvidia.com/cuda-toolkit) and [cuDNN](https://developer.nvidia.com/cudnn)
  - The CUDA execution provider for ONNX Runtime is built and tested with CUDA 12.x and cuDNN 9. Check [here](/docs/execution-providers/CUDA-ExecutionProvider.html#requirements) for more version information.
  - The path to the CUDA installation must be provided via the CUDA_HOME environment variable, or the `--cuda_home` parameter. The installation directory should contain `bin`, `include` and `lib` sub-directories.
  - The path to the CUDA `bin` directory must be added to the PATH environment variable so that `nvcc` is found.
  - The path to the cuDNN installation must be provided via the CUDNN_HOME environment variable, or `--cudnn_home` parameter. In Windows, the installation directory should contain `bin`, `include` and `lib` sub-directories.
  - cuDNN 8.\* requires ZLib. Follow the [cuDNN 8.9 installation guide](https://docs.nvidia.com/deeplearning/cudnn/archives/cudnn-890/install-guide/index.html) to install zlib in Linux or Windows.
  - In Windows, the path to the cuDNN bin directory must be added to the PATH environment variable so that cudnn64_8.dll is found.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-instructions) Build Instructions 

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#windows) Windows

``` highlight
.\build.bat --use_cuda --cudnn_home <cudnn home path> --cuda_home <cuda home path>
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#linux) Linux

``` highlight
./build.sh --use_cuda --cudnn_home <cudnn home path> --cuda_home <cuda home path>
```

A Dockerfile is available [here](https://github.com/microsoft/onnxruntime/blob/main/dockerfiles#cuda).

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-options) Build Options

To specify GPU architectures (see [Compute Capability](https://developer.nvidia.com/cuda-gpus)), you can append parameters like `--cmake_extra_defines CMAKE_CUDA_ARCHITECTURES=80;86;89`.

With `--cmake_extra_defines onnxruntime_USE_CUDA_NHWC_OPS=ON`, the CUDA EP can be compiled with additional NHWC ops. This option is not enabled by default due to the small amount of supported NHWC operators.

Another very helpful CMake build option is to build with NVTX support (`--cmake_extra_defines onnxruntime_ENABLE_NVTX_PROFILE=ON`) that will enable much easier profiling using [Nsight Systems](https://developer.nvidia.com/nsight-systems) and correlates CUDA kernels with their actual ONNX operator.

`--enable_cuda_line_info` or `--cmake_extra_defines onnxruntime_ENABLE_CUDA_LINE_NUMBER_INFO=ON` will enable [NVCC generation of line-number information for device code](https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc/index.html#generate-line-info-lineinfo). It might be helpful when you run [Compute Sanitizer](https://docs.nvidia.com/compute-sanitizer/ComputeSanitizer/index.html) tools on CUDA kernels.

If your Windows machine has multiple versions of CUDA installed and you want to use an older version of CUDA, you need append parameters like `--cuda_version <cuda version>`.

When your build machine has many CPU cores and less than 64 GB memory, there is chance of out of memory error like `nvcc error : 'cicc' died due to signal 9`. The solution is to limit number of parallel NVCC threads with parameters like `--parallel 4 --nvcc_threads 1`.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#notes-on-older-versions-of-onnx-runtime-cuda-and-visual-studio) Notes on older versions of ONNX Runtime, CUDA and Visual Studio 

- Depending on compatibility between the CUDA, cuDNN, and Visual Studio versions you are using, you may need to explicitly install an earlier version of the MSVC toolset.
- For older version of ONNX Runtime and CUDA, and Visual Studio:
  - CUDA 10.0 is [known to work](https://devblogs.microsoft.com/cppblog/cuda-10-is-now-available-with-support-for-the-latest-visual-studio-2017-versions/) with toolsets from 14.11 up to 14.16 (Visual Studio 2017 15.9), and should continue to work with future Visual Studio versions
  - CUDA 9.2 is known to work with the 14.11 MSVC toolset (Visual Studio 15.3 and 15.4)
    - To install the 14.11 MSVC toolset, see [this page](https://blogs.msdn.microsoft.com/vcblog/2017/11/15/side-by-side-minor-version-msvc-toolsets-in-visual-studio-2017).
    - To use the 14.11 toolset with a later version of Visual Studio 2017 you have two options:
      1.  Setup the Visual Studio environment variables to point to the 14.11 toolset by running vcvarsall.bat, prior to running the build script. e.g. if you have VS2017 Enterprise, an x64 build would use the following command `"C:\Program Files (x86)\Microsoft Visual Studio\2017\Enterprise\VC\Auxiliary\Build\vcvarsall.bat" amd64 -vcvars_ver=14.11` For convenience, .\\build.amd64.1411.bat will do this and can be used in the same way as .\\build.bat. e.g. \` .\\build.amd64.1411.bat --use_cuda\`

      2.  Alternatively, if you have CMake 3.13 or later you can specify the toolset version via the `--msvc_toolset` build script parameter. e.g. `.\build.bat --msvc_toolset 14.11`
- If you have multiple versions of CUDA installed on a Windows machine and are building with Visual Studio, CMake will use the build files for the highest version of CUDA it finds in the BuildCustomization folder. e.g. C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Enterprise\\Common7\\IDE\\VC\\VCTargets\\BuildCustomizations. If you want to build with an earlier version, you must temporarily remove the 'CUDA x.y.\*' files for later versions from this directory.

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#tensorrt) TensorRT

See more information on the TensorRT Execution Provider [here](/docs/execution-providers/TensorRT-ExecutionProvider.html).

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#prerequisites-1) Prerequisites 

- Follow [instructions for CUDA execution provider](#cuda) to install CUDA and cuDNN, and setup environment variables.
- Follow [instructions for installing TensorRT](https://docs.nvidia.com/deeplearning/tensorrt/latest/installing-tensorrt/installing.html)
  - The TensorRT execution provider for ONNX Runtime is built and tested with TensorRT 10.9.
  - The path to TensorRT installation must be provided via the `--tensorrt_home` parameter.
  - ONNX Runtime uses [TensorRT built-in parser](https://developer.nvidia.com/tensorrt/download) from `tensorrt_home` by default.
  - To use open-sourced [onnx-tensorrt](https://github.com/onnx/onnx-tensorrt/tree/main) parser instead, add `--use_tensorrt_oss_parser` parameter in build commands below.
    - The default version of open-sourced onnx-tensorrt parser is specified in [cmake/deps.txt](https://github.com/microsoft/onnxruntime/blob/main/cmake/deps.txt).
    - To specify a different version of onnx-tensorrt parser:
      - Select the commit of [onnx-tensorrt](https://github.com/onnx/onnx-tensorrt/commits) that you preferred;
      - Run `sha1sum` command with downloaded onnx-tensorrt zip file to acquire the SHA1 hash
      - Update [cmake/deps.txt](https://github.com/microsoft/onnxruntime/blob/main/cmake/deps.txt) with updated onnx-tensorrt commit and hash info.
    - Please make sure TensorRT built-in parser/open-sourced onnx-tensorrt specified in [cmake/deps.txt](https://github.com/microsoft/onnxruntime/blob/main/cmake/deps.txt) are **version-matched**, if enabling `--use_tensorrt_oss_parser`.
      - i.e It's version-matched if assigning `tensorrt_home` with path to TensorRT-10.9 built-in binaries and onnx-tensorrt [10.9-GA branch](https://github.com/onnx/onnx-tensorrt/tree/release/10.9-GA) specified in [cmake/deps.txt](https://github.com/microsoft/onnxruntime/blob/main/cmake/deps.txt).

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#note-to-ort-121122-open-sourced-parser-users) **\[Note to ORT 1.21/1.22 open-sourced parser users\]** 

- ORT 1.21/1.22 link against onnx-tensorrt 10.8-GA/10.9-GA, which requires newly released onnx 1.18.
  - Here's a temporarily fix to preview on onnx-tensorrt 10.8-GA/10.9-GA when building ORT 1.21/1.22:
    - Replace the [onnx line in cmake/deps.txt](https://github.com/microsoft/onnxruntime/blob/rel-1.21.0/cmake/deps.txt#L38) with `onnx;https://github.com/onnx/onnx/archive/e709452ef2bbc1d113faf678c24e6d3467696e83.zip;c0b9f6c29029e13dea46b7419f3813f4c2ca7db8`
    - Download [this](https://github.com/microsoft/onnxruntime/blob/7b2733a526c12b5ef4475edd47fd9997ebc2b2c6/cmake/patches/onnx/onnx.patch) as raw file and save file to [cmake/patches/onnx/onnx.patch](https://github.com/microsoft/onnxruntime/blob/rel-1.21.0/cmake/patches/onnx/onnx.patch) (do not copy/paste from browser, as it might alter line break type)
    - Build ORT with trt-related flags above (including `--use_tensorrt_oss_parser`)
  - The [onnx 1.18](https://github.com/onnx/onnx/releases/tag/v1.18.0) is supported by latest ORT main branch. Please checkout main branch and build ORT-TRT with `--use_tensorrt_oss_parser` to enable OSS parser with full onnx 1.18 support.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-instructions-1) Build Instructions 

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#windows-1) Windows

``` highlight
# to build with tensorrt built-in parser
.\build.bat --config Release --parallel  --cmake_extra_defines 'CMAKE_CUDA_ARCHITECTURES=native' --cudnn_home <path to cuDNN home> --cuda_home <path to CUDA home> --use_tensorrt --tensorrt_home <path to TensorRT home> --cmake_generator "Visual Studio 17 2022"

# to build with specific version of open-sourced onnx-tensorrt parser configured in cmake/deps.txt
.\build.bat --config Release --parallel  --cmake_extra_defines 'CMAKE_CUDA_ARCHITECTURES=native' --cudnn_home <path to cuDNN home> --cuda_home <path to CUDA home> --use_tensorrt --tensorrt_home <path to TensorRT home> --use_tensorrt_oss_parser --cmake_generator "Visual Studio 17 2022" 
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#linux-1) Linux

``` highlight
# to build with tensorrt built-in parser
./build.sh --config Release --parallel --cmake_extra_defines 'CMAKE_CUDA_ARCHITECTURES=native' --cudnn_home <path to cuDNN e.g. /usr/lib/x86_64-linux-gnu/> --cuda_home <path to folder for CUDA e.g. /usr/local/cuda> --use_tensorrt --tensorrt_home <path to TensorRT home>

# to build with specific version of open-sourced onnx-tensorrt parser configured in cmake/deps.txt
./build.sh --config Release --parallel --cmake_extra_defines 'CMAKE_CUDA_ARCHITECTURES=native' --cudnn_home <path to cuDNN e.g. /usr/lib/x86_64-linux-gnu/> --cuda_home <path to folder for CUDA e.g. /usr/local/cuda> --use_tensorrt --use_tensorrt_oss_parser --tensorrt_home <path to TensorRT home> --skip_submodule_sync
```

Dockerfile instructions are available [here](https://github.com/microsoft/onnxruntime/tree/main/dockerfiles#tensorrt)

**Note** Building with `--use_tensorrt_oss_parser` with TensorRT 8.X requires additional flag --cmake_extra_defines onnxruntime_USE_FULL_PROTOBUF=ON

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#nvidia-tensorrt-rtx) NVIDIA TensorRT RTX

See more information on the TensorRT RTX Execution Provider [here](/docs/execution-providers/TensorRTRTX-ExecutionProvider.html).

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#minimum-requirements) Minimum requirements

  ONNX Runtime   TensorRT-RTX   CUDA Toolkit
  -------------- -------------- --------------
  main branch    1.1            12.9
  1.23           1.1            12.9
  1.22           1.0            12.8

TensorRT RTX EP supports RTX GPUs based on Ampere (GeForce RTX 30xx) and later architectures with minimum recommended NVIDIA driver version 555.85.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#pre-requisites) Pre-requisites

- Install git, cmake, Python 3.12
- Install latest [NVIDIA driver](https://www.nvidia.com/en-us/drivers/)
- Install [CUDA toolkit 12.9](https://developer.nvidia.com/cuda-12-9-1-download-archive)
- Install [TensorRT RTX](https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/installing-tensorrt-rtx/installing.html)
- For Windows only, install [Visual Studio](https://visualstudio.microsoft.com/downloads/)
- Set TensorRT-RTX dlls in `PATH` or put it in same folder as application exe

``` highlight
git clone https://github.com/microsoft/onnxruntime.git
cd onnxruntime
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#windows-2) Windows

``` highlight
.\build.bat --config Release --build_dir build --parallel --use_nv_tensorrt_rtx --tensorrt_rtx_home "path\to\tensorrt-rtx" --cuda_home "path\to\cuda\home" --cmake_generator "Visual Studio 17 2022" --build_shared_lib --skip_tests --build --update --use_vcpkg        
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#linux-2) Linux

``` highlight
./build.sh --config Release --build_dir build --parallel --use_nv_tensorrt_rtx --tensorrt_rtx_home "path/to/tensorrt-rtx" --cuda_home "path/to/cuda/home" --build_shared_lib --skip_tests --build --update          
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#run-unit-test) Run unit test

``` highlight
.\build\Release\Release\onnxruntime_test_all.exe --gtest_filter=*NvExecutionProviderTest.*
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#python-wheel) Python wheel

``` highlight
# build the python wheel
.\build.bat --config Release --build_dir build --parallel --use_nv_tensorrt_rtx --tensorrt_rtx_home "path\to\tensorrt-rtx" --cuda_home "path\to\cuda\home" --cmake_generator "Visual Studio 17 2022" --build_shared_lib --skip_tests --build_wheel

# install
pip install "build\Release\Release\dist\onnxruntime-1.23.0-cp312-cp312-win_amd64.whl"
```

> NOTE: TensorRT-RTX .dll or .so are in `PATH` or in the same folder as the application

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#nvidia-jetson-tx1tx2nanoxavierorin) NVIDIA Jetson TX1/TX2/Nano/Xavier/Orin

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-instructions-2) Build Instructions 

These instructions are for the latest [JetPack SDK](https://developer.nvidia.com/embedded/jetpack).

1.  Clone the ONNX Runtime repo on the Jetson host

    :::: 
    ::: highlight
    ``` highlight
    git clone --recursive https://github.com/microsoft/onnxruntime
    ```
    :::
    ::::

2.  Specify the CUDA compiler, or add its location to the PATH.

    1.  JetPack 5.x users can upgrade to the latest CUDA release without updating the JetPack version or Jetson Linux BSP (Board Support Package).

        1.  For JetPack 5.x users, CUDA\>=11.8 and GCC\>9.4 are required to be installed on and after ONNX Runtime 1.17.

        2.  Check [this official blog](https://developer.nvidia.com/blog/simplifying-cuda-upgrades-for-nvidia-jetson-users/) for CUDA upgrade instruction (CUDA 12.2 has been verified on JetPack 5.1.2 on Jetson Xavier NX).

            1.  If there's no `libnvcudla.so` under `/usr/local/cuda-12.2/compat`: `sudo apt-get install -y cuda-compat-12-2` and add `export LD_LIBRARY_PATH="/usr/local/cuda-12.2/lib64:/usr/local/cuda-12.2/compat:$LD_LIBRARY_PATH"` to `~/.bashrc`.

        3.  Check [here](https://developer.nvidia.com/cuda-gpus#collapse5) for compute capability datasheet.

    2.  CMake can't automatically find the correct `nvcc` if it's not in the `PATH`. `nvcc` can be added to `PATH` via:

        :::: 
        ::: highlight
        ``` highlight
        export PATH="/usr/local/cuda/bin:$"
        ```
        :::
        ::::

        or:

        :::: 
        ::: highlight
        ``` highlight
        export CUDACXX="/usr/local/cuda/bin/nvcc"
        ```
        :::
        ::::

    3.  Update TensorRT libraries

        1.  Jetpack 5.x supports up to TensorRT 8.5. Jetpack 6.x are equipped with TensorRT 8.6-10.3.

        2.  Jetpack 6.x users can download latest TensorRT 10 TAR package for **jetpack** on [TensorRT SDK website](https://developer.nvidia.com/tensorrt/download/10x).

        3.  Check [here](/docs/execution-providers/TensorRT-ExecutionProvider.html#requirements) for TensorRT/CUDA support matrix among all ONNX Runtime versions.

3.  Install the ONNX Runtime build dependencies on the Jetpack host:

    :::: 
    ::: highlight
    ``` highlight
    sudo apt install -y --no-install-recommends \
      build-essential software-properties-common libopenblas-dev \
      libpython3.10-dev python3-pip python3-dev python3-setuptools python3-wheel
    ```
    :::
    ::::

4.  Cmake is needed to build ONNX Runtime. Please check the minimum required CMake version [here](https://github.com/microsoft/onnxruntime/blob/main/cmake/CMakeLists.txt#L6). Download from https://cmake.org/download/ and add cmake executable to `PATH` to use it.

5.  Build the ONNX Runtime Python wheel:

    1.  Build `onnxruntime-gpu` wheel with CUDA and TensorRT support (update paths to CUDA/CUDNN/TensorRT libraries if necessary):

        :::: 
        ::: highlight
        ``` highlight
        ./build.sh --config Release --update --build --parallel --build_wheel \
        --use_tensorrt --cuda_home /usr/local/cuda --cudnn_home /usr/lib/aarch64-linux-gnu \
        --tensorrt_home /usr/lib/aarch64-linux-gnu
        ```
        :::
        ::::

​Notes:

- By default, `onnxruntime-gpu` wheel file will be captured under `path_to/onnxruntime/build/Linux/Release/dist/` (build path can be customized by adding `--build_dir` followed by a customized path to the build command above).

- Append `--skip_tests --cmake_extra_defines 'CMAKE_CUDA_ARCHITECTURES=native' 'onnxruntime_BUILD_UNIT_TESTS=OFF' 'onnxruntime_USE_FLASH_ATTENTION=OFF' 'onnxruntime_USE_MEMORY_EFFICIENT_ATTENTION=OFF'` to the build command to opt out optional features and reduce build time.

- For a portion of Jetson devices like the Xavier series, higher power mode involves more cores (up to 6) to compute but it consumes more resource when building ONNX Runtime. Set `--parallel 1` in the build command if OOM happens and system is hanging.

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#onednn) oneDNN

See more information on oneDNN (formerly DNNL) [here](/docs/execution-providers/oneDNN-ExecutionProvider.html).

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-instructions-3) Build Instructions 

The DNNL execution provider can be built for Intel CPU or GPU. To build for Intel GPU, install [Intel SDK for OpenCL Applications](https://software.intel.com/content/www/us/en/develop/tools/opencl-sdk.html) or build OpenCL from [Khronos OpenCL SDK](https://github.com/KhronosGroup/OpenCL-SDK). Pass in the OpenCL SDK path as dnnl_opencl_root to the build command. Install the latest GPU driver - [Windows graphics driver](https://downloadcenter.intel.com/product/80939/Graphics), [Linux graphics compute runtime and OpenCL driver](https://github.com/intel/compute-runtime/releases).

For CPU

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#windows-3) Windows

`.\build.bat --use_dnnl`

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#linux-3) Linux

`./build.sh --use_dnnl`

For GPU

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#windows-4) Windows

`.\build.bat --use_dnnl --dnnl_gpu_runtime ocl --dnnl_opencl_root "c:\program files (x86)\intelswtools\sw_dev_tools\opencl\sdk"`

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#linux-4) Linux

`./build.sh --use_dnnl --dnnl_gpu_runtime ocl --dnnl_opencl_root "/opt/intel/sw_dev_tools/opencl-sdk"`

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-phython-wheel) Build Phython Wheel

OneDNN EP build supports building Python wheel for both Windows and linux using flag --build_wheel

`.\build.bat --config RelWithDebInfo --parallel --build_shared_lib --cmake_generator "Visual Studio 16 2019" --build_wheel --use_dnnl --dnnl_gpu_runtime ocl --dnnl_opencl_root "C:\Program Files (x86)\IntelSWTools\system_studio_2020\OpenCL\sdk"`

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#openvino) OpenVINO

See more information on the OpenVINO™ Execution Provider [here](/docs/execution-providers/OpenVINO-ExecutionProvider.html).

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#prerequisites-2) Prerequisites 

1.  Install the OpenVINO™ offline/online installer from Intel^®^ Distribution of OpenVINO™^TM^ Toolkit **Release 2025.3** for the appropriate OS and target hardware:

    - [Windows - CPU, GPU, NPU](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/download.html?PACKAGE=OPENVINO_BASE&VERSION=v_2025_3_0&OP_SYSTEM=WINDOWS&DISTRIBUTION=ARCHIVE).
    - [Linux - CPU, GPU, NPU](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/download.html?PACKAGE=OPENVINO_BASE&VERSION=v_2025_3_0&OP_SYSTEM=LINUX&DISTRIBUTION=ARCHIVE)

    Follow [documentation](https://docs.openvino.ai/2025/index.html) for detailed instructions.

    *2025.3 is the current recommended OpenVINO™ version. [OpenVINO™ 2025.0](https://docs.openvino.ai/2025/index.html) is minimal OpenVINO™ version requirement.*

2.  Install CMake 3.28 or higher. Download from the [official CMake website](https://cmake.org/download/).

3.  Configure the target hardware with specific follow on instructions:
    - To configure Intel^®^ Processor Graphics(GPU) please follow these instructions: [Windows](https://docs.openvino.ai/2025/get-started/install-openvino/configurations/configurations-intel-gpu.html#windows), [Linux](https://docs.openvino.ai/2025/get-started/install-openvino/configurations/configurations-intel-gpu.html#linux)

4.  Initialize the OpenVINO™ environment by running the setupvars script as shown below. This is a required step:
    - For Windows:

      :::: 
      ::: highlight
      ``` highlight
       C:\<openvino_install_directory>\setupvars.bat
      ```
      :::
      ::::
    - For Linux:

      :::: 
      ::: highlight
      ``` highlight
       $ source <openvino_install_directory>/setupvars.sh
      ```
      :::
      ::::

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-instructions-4) Build Instructions 

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#windows-5) Windows

``` highlight
.\build.bat --config Release --use_openvino <hardware_option> --build_shared_lib --build_wheel
```

*Note: The default Windows CMake Generator is Visual Studio 2019, but you can also use the newer Visual Studio 2022 by passing `--cmake_generator "Visual Studio 17 2022"` to `.\build.bat`*

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#linux-5) Linux

``` highlight
./build.sh --config Release --use_openvino <hardware_option> --build_shared_lib --build_wheel
```

- `--build_wheel` Creates python wheel file in dist/ folder. Enable it when building from source.
- `--use_openvino` builds the OpenVINO™ Execution Provider in ONNX Runtime.
- `<hardware_option>`: Specifies the default hardware target for building OpenVINO™ Execution Provider. This can be overriden dynamically at runtime with another option (refer to [OpenVINO™-ExecutionProvider](/docs/execution-providers/OpenVINO-ExecutionProvider.html#configuration-options) for more details on dynamic device selection). Below are the options for different Intel target devices.

Refer to [Intel GPU device naming convention](https://docs.openvino.ai/2025/openvino-workflow/running-inference/inference-devices-and-modes/gpu-device.html#device-naming-convention) for specifying the correct hardware target in cases where both integrated and discrete GPU's co-exist.

  Hardware Option   Target Device
  ----------------- --------------------------------
  `CPU`             Intel^®^ CPUs
  `GPU`             Intel^®^ Integrated Graphics
  `GPU.0`           Intel^®^ Integrated Graphics
  `GPU.1`           Intel^®^ Discrete Graphics
  `NPU`             Intel^®^ Neural Processor Unit

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#disable-subgraph-partition-feature) Disable subgraph partition Feature

- Builds the OpenVINO™ Execution Provider in ONNX Runtime with graph partitioning disabled, which will run fully supported models on OpenVINO Execution Provider else they completely fall back to default CPU EP,

- To enable this feature during build time. Use `--use_openvino ` `<hardware_option>_NO_PARTITION`

``` highlight
Usage: --use_openvino CPU_NO_PARTITION or --use_openvino GPU_NO_PARTITION or --use_openvino NPU_NO_PARTITION 
```

For more information on OpenVINO™ Execution Provider\'s ONNX Layer support, Topology support, and Intel hardware enabled, please refer to the document [OpenVINO™-ExecutionProvider](/docs/execution-providers/OpenVINO-ExecutionProvider.html#support-coverage)

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#qnn) QNN

See more information on the QNN execution provider [here](/docs/execution-providers/QNN-ExecutionProvider.html).

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#prerequisites-3) Prerequisites 

- Install the Qualcomm AI Engine Direct SDK (Qualcomm Neural Network SDK) [Linux/Android/Windows](https://qpm.qualcomm.com/main/tools/details/qualcomm_ai_engine_direct)

- Install [cmake-3.28](https://cmake.org/download/) or higher.

- Install Python 3.10 or higher.
  - [Python 3.12 for Windows Arm64](https://www.python.org/ftp/python/3.12.9/python-3.12.9-arm64.exe)
  - [Python 3.12 for Windows x86-64](https://www.python.org/ftp/python/3.12.9/python-3.12.9-amd64.exe)
  - Note: Windows on Arm supports a x86-64 Python environment via emulation. Ensure that the Arm64 Python environment is actived for a native Arm64 ONNX Runtime build.

- Checkout the source tree:

  :::: 
  ::: highlight
  ``` highlight
   git clone --recursive https://github.com/Microsoft/onnxruntime.git
   cd onnxruntime
  ```
  :::
  ::::

- Install ONNX Runtime Python dependencies.

  :::: 
  ::: highlight
  ``` highlight
   pip install -r requirements.txt
  ```
  :::
  ::::

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-options-1) Build Options 

- `--use_qnn [QNN_LIBRARY_KIND]`: Builds the QNN Execution provider. `QNN_LIBRARY_KIND` is optional and specifies whether to build the QNN Execution Provider as a shared library (default) or static library.
  - `--use_qnn` or `--use_qnn shared_lib`: Builds the QNN Execution Provider as a shared library.
  - `--use_qnn static_lib`: Builds QNN Execution Provider as a static library linked into ONNX Runtime. This is required for Android builds.
- `--qnn_home QNN_SDK_PATH`: The path to the Qualcomm AI Engine Direct SDK.
  - Example on Windows: `--qnn_home 'C:\Qualcomm\AIStack\QAIRT\2.31.0.250130'`
  - Example on Linux: `--qnn_home /opt/qcom/aistack/qairt/2.31.0.250130`
- `--build_wheel`: Enables Python bindings and builds Python wheel.
- `--arm64`: Cross-compile for Arm64.
- `--arm64ec`: Cross-compile for Arm64EC. Arm64EC code runs with native performance and is interoperable with x64 code running under emulation within the same process on a Windows on Arm device. Refer to the [Arm64EC Overview](https://learn.microsoft.com/en-us/windows/arm/arm64ec).

Run `python tools/ci_build/build.py --help` for a description of all available build options.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-instructions-5) Build Instructions 

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#windows-native-x86-64-or-native-arm64) Windows (native x86-64 or native Arm64)

``` highlight
.\build.bat --use_qnn --qnn_home [QNN_SDK_PATH] --build_shared_lib --build_wheel --cmake_generator "Visual Studio 17 2022" --config Release --parallel --skip_tests --build_dir build\Windows
```

Notes:

- Not all Qualcomm backends (e.g., HTP) are supported for model execution on a native x86-64 build. Refer to the [Qualcomm SDK backend documentation](https://docs.qualcomm.com/bundle/publicresource/topics/80-63442-50/backend.html) for more information.
- Even if a Qualcomm backend does not support execution on x86-64, the QNN Execution provider may be able to [generate compiled models](/docs/execution-providers/QNN-ExecutionProvider.html#qnn-context-binary-cache-feature) for the Qualcomm backend.

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#windows-arm64-cross-compile-target) Windows (Arm64 cross-compile target)

``` highlight
.\build.bat --arm64 --use_qnn --qnn_home [QNN_SDK_PATH] --build_shared_lib --build_wheel --cmake_generator "Visual Studio 17 2022" --config Release --parallel --build_dir build\Windows
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#windows-arm64ec-cross-compile-target) Windows (Arm64EC cross-compile target)

``` highlight
.\build.bat --arm64ec --use_qnn --qnn_home [QNN_SDK_PATH] --build_shared_lib --build_wheel --cmake_generator "Visual Studio 17 2022" --config Release --parallel --build_dir build\Windows
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#windows-arm64x-cross-compile-target) Windows (Arm64X cross-compile target)

Use the `build_arm64x.bat` script to build Arm64X binaries. Arm64X binaries bundle both Arm64 and Arm64EC code, making Arm64X compatible with both Arm64 and Arm64EC processes on a Windows on Arm device. Refer to the [Arm64X PE files overview](https://learn.microsoft.com/en-us/windows/arm/arm64x-pe).

``` highlight
.\build_arm64x.bat --use_qnn --qnn_home [QNN_SDK_PATH] --build_shared_lib --cmake_generator "Visual Studio 17 2022" --config Release --parallel
```

Notes:

- Do not specify a `--build_dir` option because `build_arm64x.bat` sets specific build directories.
- The above command places Arm64X binaries in the `.\build\arm64ec-x\Release\Release\` directory.

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#linux-x86_64) Linux (x86_64)

``` highlight
./build.sh --use_qnn --qnn_home [QNN_SDK_PATH] --build_shared_lib --build_wheel --config Release --parallel --skip_tests --build_dir build/Linux
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#android-cross-compile) Android (cross-compile):

Please reference [Build OnnxRuntime For Android](/docs/build/android.html)

``` highlight
# on Windows
.\build.bat --build_shared_lib --android --config Release --parallel --use_qnn static_lib --qnn_home [QNN_SDK_PATH] --android_sdk_path [android_SDK path] --android_ndk_path [android_NDK path] --android_abi arm64-v8a --android_api [api-version] --cmake_generator Ninja --build_dir build\Android

# on Linux
./build.sh --build_shared_lib --android --config Release --parallel --use_qnn static_lib --qnn_home [QNN_SDK_PATH] --android_sdk_path [android_SDK path] --android_ndk_path [android_NDK path] --android_abi arm64-v8a --android_api [api-version] --cmake_generator Ninja --build_dir build/Android
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#directml) DirectML

See more information on the DirectML execution provider [here](/docs/execution-providers/DirectML-ExecutionProvider.html).

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#windows-6) Windows 

``` highlight
.\build.bat --use_dml
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#notes) Notes 

The DirectML execution provider supports building for both x64 and x86 architectures. DirectML is only supported on Windows.

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#arm-compute-library) Arm Compute Library

See more information on the ACL Execution Provider [here](/docs/execution-providers/community-maintained/ACL-ExecutionProvider.html).

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-instructions-6) Build Instructions 

You must first build Arm Compute Library 24.07 for your platform as described in the [documentation](https://github.com/ARM-software/ComputeLibrary). See [here](/docs/build/inferencing.html#arm) for information on building for Arm®-based devices.

Add the following options to `build.sh` to enable the ACL Execution Provider:

``` highlight
--use_acl --acl_home=/path/to/ComputeLibrary --acl_libs=/path/to/ComputeLibrary/build
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#arm-nn) Arm NN

See more information on the Arm NN Execution Provider [here](/docs/execution-providers/community-maintained/ArmNN-ExecutionProvider.html).

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#prerequisites-4) Prerequisites 

- Supported backend: i.MX8QM Armv8 CPUs
- Supported BSP: i.MX8QM BSP
  - Install i.MX8QM BSP: `source fsl-imx-xwayland-glibc-x86_64-fsl-image-qt5-aarch64-toolchain-4*.sh`
- Set up the build environment

``` highlight
source /opt/fsl-imx-xwayland/4.*/environment-setup-aarch64-poky-linux
alias cmake="/usr/bin/cmake -DCMAKE_TOOLCHAIN_FILE=$OECORE_NATIVE_SYSROOT/usr/share/cmake/OEToolchainConfig.cmake"
```

- See [here](/docs/build/inferencing.html#arm) for information on building for Arm-based devices

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-instructions-7) Build Instructions 

``` highlight
./build.sh --use_armnn
```

The Relu operator is set by default to use the CPU execution provider for better performance. To use the Arm NN implementation build with --armnn_relu flag

``` highlight
./build.sh --use_armnn --armnn_relu
```

The Batch Normalization operator is set by default to use the CPU execution provider. To use the Arm NN implementation build with --armnn_bn flag

``` highlight
./build.sh --use_armnn --armnn_bn
```

To use a library outside the normal environment you can set a custom path by providing the --armnn_home and --armnn_libs parameters to define the path to the Arm NN home directory and build directory respectively. The Arm Compute Library home directory and build directory must also be available, and can be specified if needed using --acl_home and --acl_libs respectively.

``` highlight
./build.sh --use_armnn --armnn_home /path/to/armnn --armnn_libs /path/to/armnn/build  --acl_home /path/to/ComputeLibrary --acl_libs /path/to/acl/build
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#rknpu) RKNPU

See more information on the RKNPU Execution Provider [here](/docs/execution-providers/community-maintained/RKNPU-ExecutionProvider.html).

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#prerequisites-5) Prerequisites 

- Supported platform: RK1808 Linux
- See [here](/docs/build/inferencing.html#arm) for information on building for Arm-based devices
- Use gcc-linaro-6.3.1-2017.05-x86_64_aarch64-linux-gnu instead of gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf, and modify CMAKE_CXX_COMPILER & CMAKE_C_COMPILER in tool.cmake:

``` highlight
set(CMAKE_CXX_COMPILER aarch64-linux-gnu-g++)
set(CMAKE_C_COMPILER aarch64-linux-gnu-gcc)
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-instructions-8) Build Instructions 

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#linux-6) Linux

1.  Download [rknpu_ddk](https://github.com/airockchip/rknpu_ddk.git) to any directory.

2.  Build ONNX Runtime library and test:

    :::: 
    ::: highlight
    ``` highlight
     ./build.sh --arm --use_rknpu --parallel --build_shared_lib --build_dir build_arm --config MinSizeRel --cmake_extra_defines RKNPU_DDK_PATH=<Path To rknpu_ddk> CMAKE_TOOLCHAIN_FILE=<Path To tool.cmake> ONNX_CUSTOM_PROTOC_EXECUTABLE=<Path To protoc>
    ```
    :::
    ::::

3.  Deploy ONNX runtime and librknpu_ddk.so on the RK1808 board:

    :::: 
    ::: highlight
    ``` highlight
     libonnxruntime.so.1.2.0
     onnxruntime_test_all
     rknpu_ddk/lib64/librknpu_ddk.so
    ```
    :::
    ::::

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#amd-vitis-ai) AMD Vitis AI

See more information on the Vitis AI Execution Provider [here](/docs/execution-providers/Vitis-AI-ExecutionProvider.html).

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#windows-7) Windows 

From the Visual Studio Developer Command Prompt or Developer PowerShell, execute the following command:

``` highlight
.\build.bat --use_vitisai --build_shared_lib --parallel --config Release
```

If you wish to leverage the Python APIs, please include the `--build_wheel` flag:

``` highlight
.\build.bat --use_vitisai --build_shared_lib --parallel --config Release --build_wheel
```

You can override also override the installation location by specifying CMAKE_INSTALL_PREFIX via the cmake_extra_defines parameter. e.g.

``` highlight
.\build.bat --use_vitisai --build_shared_lib --parallel --config Release --cmake_extra_defines CMAKE_INSTALL_PREFIX=D:\onnxruntime
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#linux-7) Linux 

Currently Linux support is only enabled for AMD Adapable SoCs. Please refer to the guidance [here](/docs/execution-providers/Vitis-AI-ExecutionProvider.html#installation-for-amd-adaptable-socs) for SoC targets.

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#amd-migraphx) AMD MIGraphX

See more information on the MIGraphX Execution Provider [here](/docs/execution-providers/MIGraphX-ExecutionProvider.html).

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#prerequisites-6) Prerequisites 

- Install [ROCm](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.3.1/)
  - The MIGraphX execution provider for ONNX Runtime is built and tested with ROCm6.3.1
- Install [MIGraphX](https://github.com/ROCmSoftwarePlatform/AMDMIGraphX)
  - The path to MIGraphX installation must be provided via the `--migraphx_home parameter`.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-instructions-9) Build Instructions 

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#linux-8) Linux

``` highlight
./build.sh --config <Release|Debug|RelWithDebInfo> --parallel --use_migraphx --migraphx_home <path to MIGraphX home>
```

Dockerfile instructions are available [here](https://github.com/microsoft/onnxruntime/blob/main/dockerfiles#migraphx).

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-phython-wheel-1) Build Phython Wheel

`./build.sh --config Release --build_wheel --parallel --use_migraphx --migraphx_home /opt/rocm`

Then the python wheels(\*.whl) could be found at `./build/Linux/Release/dist`.

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#amd-rocm) AMD ROCm

See more information on the ROCm Execution Provider [here](/docs/execution-providers/ROCm-ExecutionProvider.html).

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#prerequisites-7) Prerequisites 

- Install [ROCm](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.3.1/)
  - The ROCm execution provider for ONNX Runtime is built and tested with ROCm6.3.1

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-instructions-10) Build Instructions 

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#linux-9) Linux

``` highlight
./build.sh --config <Release|Debug|RelWithDebInfo> --parallel --use_rocm --rocm_home <path to ROCm home>
```

Dockerfile instructions are available [here](https://github.com/microsoft/onnxruntime/tree/main/dockerfiles#rocm).

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-phython-wheel-2) Build Phython Wheel

`./build.sh --config Release --build_wheel --parallel --use_rocm --rocm_home /opt/rocm`

Then the python wheels(\*.whl) could be found at `./build/Linux/Release/dist`.

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#nnapi) NNAPI

Usage of NNAPI on Android platforms is via the NNAPI Execution Provider (EP).

See the [NNAPI Execution Provider](/docs/execution-providers/NNAPI-ExecutionProvider.html) documentation for more details.

The pre-built ONNX Runtime Mobile package for Android includes the NNAPI EP.

If performing a custom build of ONNX Runtime, support for the NNAPI EP or CoreML EP must be enabled when building.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#create-a-minimal-build-with-nnapi-ep-support) Create a minimal build with NNAPI EP support

Please see [the instructions](/docs/build/android.html) for setting up the Android environment required to build. The Android build can be cross-compiled on Windows or Linux.

Once you have all the necessary components setup, follow the instructions to [create the custom build](/docs/build/custom.html), with the following changes:

- Replace `--minimal_build` with `--minimal_build extended` to enable support for execution providers that dynamically create kernels at runtime, which is required by the NNAPI EP.
- Add `--use_nnapi` to include the NNAPI EP in the build

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#example-build-commands-with-the-nnapi-ep-enabled) Example build commands with the NNAPI EP enabled

Windows example:

``` dos
<ONNX Runtime repository root>.\build.bat --config MinSizeRel --android --android_sdk_path D:\Android --android_ndk_path D:\Android\ndk\21.1.6352462\ --android_abi arm64-v8a --android_api 29 --cmake_generator Ninja --minimal_build extended --use_nnapi --disable_ml_ops --disable_exceptions --build_shared_lib --skip_tests --include_ops_by_config <config file from model conversion>
```

Linux example:

``` highlight
<ONNX Runtime repository root>./build.sh --config MinSizeRel --android --android_sdk_path /Android --android_ndk_path /Android/ndk/21.1.6352462/ --android_abi arm64-v8a --android_api 29 --minimal_build extended --use_nnapi --disable_ml_ops --disable_exceptions --build_shared_lib --skip_tests --include_ops_by_config <config file from model conversion>`
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#coreml) CoreML

Usage of CoreML on iOS and macOS platforms is via the CoreML EP.

See the [CoreML Execution Provider](/docs/execution-providers/CoreML-ExecutionProvider.html) documentation for more details.

The pre-built ONNX Runtime Mobile package for iOS includes the CoreML EP.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#create-a-minimal-build-with-coreml-ep-support) Create a minimal build with CoreML EP support

Please see [the instructions](/docs/build/ios.html) for setting up the iOS environment required to build. The iOS/macOS build must be performed on a mac machine.

Once you have all the necessary components setup, follow the instructions to [create the custom build](/docs/build/custom.html), with the following changes:

- Replace `--minimal_build` with `--minimal_build extended` to enable support for execution providers that dynamically create kernels at runtime, which is required by the CoreML EP.
- Add `--use_coreml` to include the CoreML EP in the build

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#xnnpack) XNNPACK

Usage of XNNPACK on Android/iOS/Windows/Linux platforms is via the XNNPACK EP.

See the [XNNPACK Execution Provider](/docs/execution-providers/Xnnpack-ExecutionProvider.html) documentation for more details.

The pre-built ONNX Runtime package([`onnxruntime-android`](https://mvnrepository.com/artifact/com.microsoft.onnxruntime/onnxruntime-android)) for Android includes the XNNPACK EP.

The pre-built ONNX Runtime Mobile package for iOS, `onnxruntime-c` and `onnxruntime-objc` in [CocoaPods](https://cocoapods.org/), includes the XNNPACK EP. (Package `onnxruntime-objc` with XNNPACK will be available since 1.14.)

If performing a custom build of ONNX Runtime, support for the XNNPACK EP must be enabled when building.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-for-android) Build for Android

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#create-a-minimal-build-with-xnnpack-ep-support) Create a minimal build with XNNPACK EP support

Please see [the instructions](/docs/build/android.html) for setting up the Android environment required to build. The Android build can be cross-compiled on Windows or Linux.

Once you have all the necessary components setup, follow the instructions to [create the custom build](/docs/build/custom.html), with the following changes:

- Replace `--minimal_build` with `--minimal_build extended` to enable support for execution providers that dynamically create kernels at runtime, which is required by the XNNPACK EP.
- Add `--use_xnnpack` to include the XNNPACK EP in the build

##### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#example-build-commands-with-the-xnnpack-ep-enabled) Example build commands with the XNNPACK EP enabled

Windows example:

``` highlight
<ONNX Runtime repository root>.\build.bat --config MinSizeRel --android --android_sdk_path D:\Android --android_ndk_path D:\Android\ndk\21.1.6352462\ --android_abi arm64-v8a --android_api 29 --cmake_generator Ninja --minimal_build extended --use_xnnpack --disable_ml_ops --disable_exceptions --build_shared_lib --skip_tests --include_ops_by_config <config file from model conversion>
```

Linux example:

``` highlight
<ONNX Runtime repository root>./build.sh --config MinSizeRel --android --android_sdk_path /Android --android_ndk_path /Android/ndk/21.1.6352462/ --android_abi arm64-v8a --android_api 29 --minimal_build extended --use_xnnpack --disable_ml_ops --disable_exceptions --build_shared_lib --skip_tests --include_ops_by_config <config file from model conversion>`
```

If you don't mind MINIMAL build, you can use the following command to build XNNPACK EP for Android: Linux example:

``` highlight
./build.sh --cmake_generator "Ninja" --android  --android_sdk_path /Android --android_ndk_path /Android/ndk/21.1.6352462/ --android_abi arm64-v8a --android_api 29 --use_xnnpack
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-for-ios-available-since-114) Build for iOS (available since 1.14) 

A Mac machine is required to build package for iOS. Please follow this [guide](/docs/build/ios.html) to set up environment firstly.

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#create-a-minimal-build-with-xnnpack-ep-support-1) Create a minimal build with XNNPACK EP support

Once you have all the necessary components setup, follow the instructions to [create the custom build](/docs/build/custom.html), with the following changes:

- Replace `--minimal_build` with `--minimal_build extended` to enable support for execution providers that dynamically create kernels at runtime, which is required by the XNNPACK EP.
- Add `--use_xnnpack` to include the XNNPACK EP in the build

``` dos
<ONNX Runtime repository root>./build.sh --config <Release|Debug|RelWithDebInfo|MinSizeRel> --use_xcode \
           --ios --ios_sysroot iphoneos --osx_arch arm64 --apple_deploy_target <minimal iOS version> --use_xnnpack --minimal_build extended --disable_ml_ops --disable_exceptions --build_shared_lib --skip_tests --include_ops_by_config <config file from model conversion>
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-for-windows) Build for Windows

``` dos
<ONNX Runtime repository root>.\build.bat --config <Release|Debug|RelWithDebInfo> --use_xnnpack
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-for-linux) Build for Linux

``` highlight
<ONNX Runtime repository root>./build.sh --config <Release|Debug|RelWithDebInfo> --use_xnnpack
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#cann) CANN

See more information on the CANN Execution Provider [here](/docs/execution-providers/community-maintained/CANN-ExecutionProvider.html).

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#prerequisites-8) Prerequisites 

1.  Install the CANN Toolkit for the appropriate OS and target hardware by following [documentation](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/51RC1alphaX/softwareinstall/instg/atlasdeploy_03_0017.html) for detailed instructions, please.

2.  Initialize the CANN environment by running the script as shown below.

    :::: 
    ::: highlight
    ``` highlight
    # Default path, change it if needed.
    source /usr/local/Ascend/ascend-toolkit/set_env.sh
    ```
    :::
    ::::

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-instructions-11) Build Instructions 

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#linux-10) Linux

``` highlight
./build.sh --config <Release|Debug|RelWithDebInfo> --build_shared_lib --parallel --use_cann
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#notes-1) Notes 

- The CANN execution provider supports building for both x64 and aarch64 architectures.
- CANN excution provider now is only supported on Linux.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#azure) Azure

See the [Azure Execution Provider](/docs/execution-providers/Azure-ExecutionProvider.html) documentation for more details.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#prerequisites-9) Prerequisites

For Linux, before building, please:

- install openssl dev package into the system, which is openssl-dev for redhat and libssl-dev for ubuntu.
- if have multiple openssl dev versions installed in the system, please set environment variable "OPENSSL_ROOT_DIR" to the desired version, for example:

``` base
set OPENSSL_ROOT_DIR=/usr/local/ssl3.x/
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-instructions-12) Build Instructions

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#windows-8) Windows

``` dos
build.bat --config <Release|Debug|RelWithDebInfo> --build_shared_lib --build_wheel --use_azure
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#linux-11) Linux

``` highlight
./build.sh --config <Release|Debug|RelWithDebInfo> --build_shared_lib --build_wheel --use_azure
```