# Source: https://docs.vllm.ai/en/stable/getting_started/installation/cpu/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/getting_started/installation/cpu.md "Edit this page")

# CPU[¶](#cpu "Permanent link")

vLLM is a Python library that supports the following CPU variants. Select your CPU type to see vendor specific instructions:

Intel/AMD x86ARM AArch64Apple siliconIBM Z (S390X)

vLLM supports basic model inferencing and serving on x86 CPU platform, with data types FP32, FP16 and BF16.

vLLM offers basic model inferencing and serving on Arm CPU platform, with support NEON, data types FP32, FP16 and BF16.

vLLM has experimental support for macOS with Apple Silicon. For now, users must build from source to natively run on macOS.

Currently the CPU implementation for macOS supports FP32 and FP16 datatypes.

vLLM has experimental support for s390x architecture on IBM Z platform. For now, users must build from source to natively run on IBM Z platform.

Currently, the CPU implementation for s390x architecture supports FP32 datatype only.

## Requirements[¶](#requirements "Permanent link")

-   Python: 3.10 \-- 3.13

Intel/AMD x86ARM AArch64Apple siliconIBM Z (S390X)

-   OS: Linux
-   CPU flags: `avx512f` (Recommended), `avx512_bf16` (Optional), `avx512_vnni` (Optional)

Tip

Use `lscpu` to check the CPU flags.

-   OS: Linux
-   Compiler: `gcc/g++ >= 12.3.0` (optional, recommended)
-   Instruction Set Architecture (ISA): NEON support is required

-   OS: `macOS Sonoma` or later
-   SDK: `XCode 15.4` or later with Command Line Tools
-   Compiler: `Apple Clang >= 15.0.0`

-   OS: `Linux`
-   SDK: `gcc/g++ >= 12.3.0` or later with Command Line Tools
-   Instruction Set Architecture (ISA): VXE support is required. Works with Z14 and above.
-   Build install python packages: `pyarrow`, `torch` and `torchvision`

## Set up using Python[¶](#set-up-using-python "Permanent link")

### Create a new Python environment[¶](#create-a-new-python-environment "Permanent link")

On NVIDIA CUDA only, it\'s recommended to use [uv](https://docs.astral.sh/uv/), a very fast Python environment manager, to create and manage Python environments. Please follow the [documentation](https://docs.astral.sh/uv/#getting-started) to install `uv`. After installing `uv`, you can create a new Python environment using the following commands:

    uv venv --python 3.12 --seed
    source .venv/bin/activate

### Pre-built wheels[¶](#pre-built-wheels "Permanent link")

When specifying the index URL, please make sure to use the `cpu` variant subdirectory. For example, the nightly build index is: `https://wheels.vllm.ai/nightly/cpu/`.

Intel/AMD x86ARM AArch64Apple siliconIBM Z (S390X)

Currently, there are no pre-built x86 CPU wheels.

Pre-built vLLM wheels for Arm are available since version 0.11.2. These wheels contain pre-compiled C++ binaries.

    export VLLM_VERSION=$(curl -s https://api.github.com/repos/vllm-project/vllm/releases/latest | jq -r .tag_name | sed 's/^v//')
    uv pip install vllm --extra-index-url https://wheels.vllm.ai/$/cpu

pip

    pip install vllm==$+cpu --extra-index-url https://wheels.vllm.ai/$/cpu

The `uv` approach works for vLLM `v0.6.6` and later. A unique feature of `uv` is that packages in `--extra-index-url` have [higher priority than the default index](https://docs.astral.sh/uv/pip/compatibility/#packages-that-exist-on-multiple-indexes). If the latest public release is `v0.6.6.post1`, `uv`\'s behavior allows installing a commit before `v0.6.6.post1` by specifying the `--extra-index-url`. In contrast, `pip` combines packages from `--extra-index-url` and the default index, choosing only the latest version, which makes it difficult to install a development version prior to the released version.

**Install the latest code**

LLM inference is a fast-evolving field, and the latest code may contain bug fixes, performance improvements, and new features that are not released yet. To allow users to try the latest code without waiting for the next release, vLLM provides working pre-built Arm CPU wheels for every commit since `v0.11.2` on <https://wheels.vllm.ai/nightly>. For native CPU wheels, this index should be used:

-   `https://wheels.vllm.ai/nightly/cpu/vllm`

To install from nightly index, run:

    uv pip install vllm --extra-index-url https://wheels.vllm.ai/nightly/cpu

pip (there\'s a caveat)

Using `pip` to install from nightly indices is *not supported*, because `pip` combines packages from `--extra-index-url` and the default index, choosing only the latest version, which makes it difficult to install a development version prior to the released version. In contrast, `uv` gives the extra index [higher priority than the default index](https://docs.astral.sh/uv/pip/compatibility/#packages-that-exist-on-multiple-indexes).

If you insist on using `pip`, you have to specify the full URL (link address) of the wheel file (which can be obtained from https://wheels.vllm.ai/nightly/cpu/vllm).

    pip install https://wheels.vllm.ai/4fa7ce46f31cbd97b4651694caf9991cc395a259/vllm-0.13.0rc2.dev104%2Bg4fa7ce46f.cpu-cp38-abi3-manylinux_2_35_aarch64.whl # current nightly build (the filename will change!)

**Install specific revisions**

If you want to access the wheels for previous commits (e.g. to bisect the behavior change, performance regression), you can specify the commit hash in the URL:

    export VLLM_COMMIT=730bd35378bf2a5b56b6d3a45be28b3092d26519 # use full commit hash from the main branch
    uv pip install vllm --extra-index-url https://wheels.vllm.ai/$/cpu

Currently, there are no pre-built Apple silicon CPU wheels.

Currently, there are no pre-built IBM Z CPU wheels.

### Build wheel from source[¶](#build-wheel-from-source "Permanent link")

#### Set up using Python-only build (without compilation)[¶](#python-only-build "Permanent link") 

Please refer to the instructions for [Python-only build on GPU](../gpu/#python-only-build), and replace the build commands with:

    VLLM_USE_PRECOMPILED=1 VLLM_PRECOMPILED_WHEEL_VARIANT=cpu VLLM_TARGET_DEVICE=cpu uv pip install --editable .

#### Full build (with compilation)[¶](#full-build "Permanent link") 

Intel/AMD x86ARM AArch64Apple siliconIBM Z (s390x)

Install recommended compiler. We recommend to use `gcc/g++ >= 12.3.0` as the default compiler to avoid potential problems. For example, on Ubuntu 22.4, you can run:

    sudo apt-get update -y
    sudo apt-get install -y gcc-12 g++-12 libnuma-dev python3-dev
    sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 10 --slave /usr/bin/g++ g++ /usr/bin/g++-12

Clone the vLLM project:

    git clone https://github.com/vllm-project/vllm.git vllm_source
    cd vllm_source

Install the required dependencies:

    uv pip install -r requirements/cpu-build.txt --torch-backend cpu
    uv pip install -r requirements/cpu.txt --torch-backend cpu

pip

    pip install --upgrade pip
    pip install -v -r requirements/cpu-build.txt --extra-index-url https://download.pytorch.org/whl/cpu
    pip install -v -r requirements/cpu.txt --extra-index-url https://download.pytorch.org/whl/cpu

Build and install vLLM:

    VLLM_TARGET_DEVICE=cpu uv pip install . --no-build-isolation

If you want to develop vLLM, install it in editable mode instead.

    VLLM_TARGET_DEVICE=cpu uv pip install -e . --no-build-isolation

Optionally, build a portable wheel which you can then install elsewhere:

    VLLM_TARGET_DEVICE=cpu uv build --wheel

    uv pip install dist/*.whl

pip

    VLLM_TARGET_DEVICE=cpu python -m build --wheel --no-isolation

    pip install dist/*.whl

Troubleshooting

-   **NumPy ≥2.0 error**: Downgrade using `pip install "numpy<2.0"`.
-   **CMake picks up CUDA**: Add `CMAKE_DISABLE_FIND_PACKAGE_CUDA=ON` to prevent CUDA detection during CPU builds, even if CUDA is installed.
-   `AMD` requires at least 4th gen processors (Zen 4/Genoa) or higher to support [AVX512](https://www.phoronix.com/review/amd-zen4-avx512) to run vLLM on CPU.
-   If you receive an error such as: `Could not find a version that satisfies the requirement torch==X.Y.Z+cpu+cpu`, consider updating [pyproject.toml](https://github.com/vllm-project/vllm/blob/main/pyproject.toml) to help pip resolve the dependency.

    ::: 
    [pyproject.toml]
        [build-system]
        requires = [
          "cmake>=3.26.1",
          ...
          "torch==X.Y.Z+cpu"   # <-------
        ]
    :::
-   If you are building vLLM from source and not using the pre-built images, remember to set `LD_PRELOAD="/usr/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4:$LD_PRELOAD"` on x86 machines before running vLLM.

First, install the recommended compiler. We recommend using `gcc/g++ >= 12.3.0` as the default compiler to avoid potential problems. For example, on Ubuntu 22.4, you can run:

    sudo apt-get update  -y
    sudo apt-get install -y --no-install-recommends ccache git curl wget ca-certificates gcc-12 g++-12 libtcmalloc-minimal4 libnuma-dev ffmpeg libsm6 libxext6 libgl1 jq lsof
    sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 10 --slave /usr/bin/g++ g++ /usr/bin/g++-12

Second, clone the vLLM project:

    git clone https://github.com/vllm-project/vllm.git vllm_source
    cd vllm_source

Third, install required dependencies:

    uv pip install -r requirements/cpu-build.txt --torch-backend cpu
    uv pip install -r requirements/cpu.txt --torch-backend cpu

pip

    pip install --upgrade pip
    pip install -v -r requirements/cpu-build.txt --extra-index-url https://download.pytorch.org/whl/cpu
    pip install -v -r requirements/cpu.txt --extra-index-url https://download.pytorch.org/whl/cpu

Finally, build and install vLLM:

    VLLM_TARGET_DEVICE=cpu uv pip install . --no-build-isolation

If you want to develop vLLM, install it in editable mode instead.

    VLLM_TARGET_DEVICE=cpu uv pip install -e . --no-build-isolation

Testing has been conducted on AWS Graviton3 instances for compatibility.

After installation of XCode and the Command Line Tools, which include Apple Clang, execute the following commands to build and install vLLM from source.

    git clone https://github.com/vllm-project/vllm.git
    cd vllm
    uv pip install -r requirements/cpu.txt --index-strategy unsafe-best-match
    uv pip install -e .

Tip

The `--index-strategy unsafe-best-match` flag is needed to resolve dependencies across multiple package indexes (PyTorch CPU index and PyPI). Without this flag, you may encounter `typing-extensions` version conflicts.

The term \"unsafe\" refers to the package resolution strategy, not security. By default, `uv` only searches the first index where a package is found to prevent dependency confusion attacks. This flag allows `uv` to search all configured indexes to find the best compatible versions. Since both PyTorch and PyPI are trusted package sources, using this strategy is safe and appropriate for vLLM installation.

Note

On macOS the `VLLM_TARGET_DEVICE` is automatically set to `cpu`, which is currently the only supported device.

Troubleshooting

If the build fails with errors like the following where standard C++ headers cannot be found, try to remove and reinstall your [Command Line Tools for Xcode](https://developer.apple.com/download/all/).

    [...] fatal error: 'map' file not found
            1 | #include <map>
                |          ^~~~~
        1 error generated.
        [2/8] Building CXX object CMakeFiles/_C.dir/csrc/cpu/pos_encoding.cpp.o

    [...] fatal error: 'cstddef' file not found
            10 | #include <cstddef>
                |          ^~~~~~~~~
        1 error generated.

------------------------------------------------------------------------

If the build fails with C++11/C++17 compatibility errors like the following, the issue is that the build system is defaulting to an older C++ standard:

    [...] error: 'constexpr' is not a type
    [...] error: expected ';' before 'constexpr'
    [...] error: 'constexpr' does not name a type

**Solution**: Your compiler might be using an older C++ standard. Edit `cmake/cpu_extension.cmake` and add `set(CMAKE_CXX_STANDARD 17)` before `set(CMAKE_CXX_STANDARD_REQUIRED ON)`.

To check your compiler\'s C++ standard support:

    clang++ -std=c++17 -pedantic -dM -E -x c++ /dev/null | grep __cplusplus

On Apple Clang 16 you should see: `#define __cplusplus 201703L`

Install the following packages from the package manager before building the vLLM. For example on RHEL 9.4:

    dnf install -y \
        which procps findutils tar vim git gcc g++ make patch make cython zlib-devel \
        libjpeg-turbo-devel libtiff-devel libpng-devel libwebp-devel freetype-devel harfbuzz-devel \
        openssl-devel openblas openblas-devel wget autoconf automake libtool cmake numactl-devel

Install rust\>=1.80 which is needed for `outlines-core` and `uvloop` python packages installation.

    curl https://sh.rustup.rs -sSf | sh -s -- -y && \
        . "$HOME/.cargo/env"

Execute the following commands to build and install vLLM from source.

Tip

Please build the following dependencies, `torchvision`, `pyarrow` from source before building vLLM.

        sed -i '/^torch/d' requirements/build.txt    # remove torch from requirements/build.txt since we use nightly builds
        uv pip install -v \
            --torch-backend auto \
            -r requirements/build.txt \
            -r requirements/cpu.txt \
        VLLM_TARGET_DEVICE=cpu python setup.py bdist_wheel && \
            uv pip install dist/*.whl

pip

        sed -i '/^torch/d' requirements/build.txt    # remove torch from requirements/build.txt since we use nightly builds
        pip install -v \
            --extra-index-url https://download.pytorch.org/whl/nightly/cpu \
            -r requirements/build.txt \
            -r requirements/cpu.txt \
        VLLM_TARGET_DEVICE=cpu python setup.py bdist_wheel && \
            pip install dist/*.whl

## Set up using Docker[¶](#set-up-using-docker "Permanent link")

### Pre-built images[¶](#pre-built-images "Permanent link")

Intel/AMD x86ARM AArch64Apple siliconIBM Z (S390X)

<https://gallery.ecr.aws/q9t5s3a7/vllm-cpu-release-repo>

Warning

If deploying the pre-built images on machines without `avx512f`, `avx512_bf16`, or `avx512_vnni` support, an `Illegal instruction` error may be raised. It is recommended to build images for these machines with the appropriate build arguments (e.g., `--build-arg VLLM_CPU_DISABLE_AVX512=true`, `--build-arg VLLM_CPU_AVX512BF16=false`, or `--build-arg VLLM_CPU_AVX512VNNI=false`) to disable unsupported features. Please note that without `avx512f`, AVX2 will be used and this version is not recommended because it only has basic feature support.

See [Using Docker](../../../deployment/docker/) for instructions on using the official Docker image.

Stable vLLM Docker images are being pre-built for Arm from version 0.12.0. Available image tags are here: <https://gallery.ecr.aws/q9t5s3a7/vllm-arm64-cpu-release-repo>.

    export VLLM_VERSION=$(curl -s https://api.github.com/repos/vllm-project/vllm/releases/latest | jq -r .tag_name | sed 's/^v//')
    docker pull public.ecr.aws/q9t5s3a7/vllm-arm64-cpu-release-repo:v$

You can also access the latest code with Docker images. These are not intended for production use and are meant for CI and testing only. They will expire after several days.

The latest code can contain bugs and may not be stable. Please use it with caution.

    export VLLM_COMMIT=6299628d326f429eba78736acb44e76749b281f5 # use full commit hash from the main branch
    docker pull public.ecr.aws/q9t5s3a7/vllm-ci-postmerge-repo:$-arm64-cpu

Currently, there are no pre-built Arm silicon CPU images.

Currently, there are no pre-built IBM Z CPU images.

### Build image from source[¶](#build-image-from-source "Permanent link")

Intel/AMD x86ARM AArch64Apple siliconIBM Z (S390X)

    docker build -f docker/Dockerfile.cpu \
            --build-arg VLLM_CPU_AVX512BF16=false (default)|true \
            --build-arg VLLM_CPU_AVX512VNNI=false (default)|true \
            --build-arg VLLM_CPU_DISABLE_AVX512=false (default)|true \ 
            --tag vllm-cpu-env \
            --target vllm-openai .

    # Launching OpenAI server
    docker run --rm \
                --security-opt seccomp=unconfined \
                --cap-add SYS_NICE \
                --shm-size=4g \
                -p 8000:8000 \
                -e VLLM_CPU_KVCACHE_SPACE=<KV cache space> \
                -e VLLM_CPU_OMP_THREADS_BIND=<CPU cores for inference> \
                vllm-cpu-env \
                --model=meta-llama/Llama-3.2-1B-Instruct \
                --dtype=bfloat16 \
                other vLLM OpenAI server arguments

    docker build -f docker/Dockerfile.cpu \
            --tag vllm-cpu-env .

    # Launching OpenAI server
    docker run --rm \
                --privileged=true \
                --shm-size=4g \
                -p 8000:8000 \
                -e VLLM_CPU_KVCACHE_SPACE=<KV cache space> \
                -e VLLM_CPU_OMP_THREADS_BIND=<CPU cores for inference> \
                vllm-cpu-env \
                --model=meta-llama/Llama-3.2-1B-Instruct \
                --dtype=bfloat16 \
                other vLLM OpenAI server arguments

Tip

An alternative of `--privileged=true` is `--cap-add SYS_NICE --security-opt seccomp=unconfined`.

    docker build -f docker/Dockerfile.cpu \
            --tag vllm-cpu-env .

    # Launching OpenAI server
    docker run --rm \
                --privileged=true \
                --shm-size=4g \
                -p 8000:8000 \
                -e VLLM_CPU_KVCACHE_SPACE=<KV cache space> \
                -e VLLM_CPU_OMP_THREADS_BIND=<CPU cores for inference> \
                vllm-cpu-env \
                --model=meta-llama/Llama-3.2-1B-Instruct \
                --dtype=bfloat16 \
                other vLLM OpenAI server arguments

Tip

An alternative of `--privileged=true` is `--cap-add SYS_NICE --security-opt seccomp=unconfined`.

    docker build -f docker/Dockerfile.s390x \
        --tag vllm-cpu-env .

    # Launch OpenAI server
    docker run --rm \
        --privileged true \
        --shm-size 4g \
        -p 8000:8000 \
        -e VLLM_CPU_KVCACHE_SPACE=<KV cache space> \
        -e VLLM_CPU_OMP_THREADS_BIND=<CPU cores for inference> \
        vllm-cpu-env \
        --model meta-llama/Llama-3.2-1B-Instruct \
        --dtype float \
        other vLLM OpenAI server arguments

Tip

An alternative of `--privileged true` is `--cap-add SYS_NICE --security-opt seccomp=unconfined`.

## Related runtime environment variables[¶](#related-runtime-environment-variables "Permanent link")

-   `VLLM_CPU_KVCACHE_SPACE`: specify the KV Cache size (e.g, `VLLM_CPU_KVCACHE_SPACE=40` means 40 GiB space for KV cache), larger setting will allow vLLM to run more requests in parallel. This parameter should be set based on the hardware configuration and memory management pattern of users. Default value is `0`.
-   `VLLM_CPU_OMP_THREADS_BIND`: specify the CPU cores dedicated to the OpenMP threads, can be set as CPU id lists, `auto` (by default), or `nobind` (to disable binding to individual CPU cores and to inherit user-defined OpenMP variables). For example, `VLLM_CPU_OMP_THREADS_BIND=0-31` means there will be 32 OpenMP threads bound on 0-31 CPU cores. `VLLM_CPU_OMP_THREADS_BIND=0-31|32-63` means there will be 2 tensor parallel processes, 32 OpenMP threads of rank0 are bound on 0-31 CPU cores, and the OpenMP threads of rank1 are bound on 32-63 CPU cores. By setting to `auto`, the OpenMP threads of each rank are bound to the CPU cores in each NUMA node respectively. If set to `nobind`, the number of OpenMP threads is determined by the standard `OMP_NUM_THREADS` environment variable.
-   `VLLM_CPU_NUM_OF_RESERVED_CPU`: specify the number of CPU cores which are not dedicated to the OpenMP threads for each rank. The variable only takes effect when VLLM_CPU_OMP_THREADS_BIND is set to `auto`. Default value is `None`. If the value is not set and use `auto` thread binding, no CPU will be reserved for `world_size == 1`, 1 CPU per rank will be reserved for `world_size > 1`.
-   `CPU_VISIBLE_MEMORY_NODES`: specify visible NUMA memory nodes for vLLM CPU workers, similar to `CUDA_VISIBLE_DEVICES`. The variable only takes effect when VLLM_CPU_OMP_THREADS_BIND is set to `auto`. The variable provides more control for the auto thread-binding feature, such as masking nodes and changing nodes binding sequence.
-   `VLLM_CPU_SGL_KERNEL` (x86 only, Experimental): whether to use small-batch optimized kernels for linear layer and MoE layer, especially for low-latency requirements like online serving. The kernels require AMX instruction set, BFloat16 weight type and weight shapes divisible by 32. Default is `0` (False).

## FAQ[¶](#faq "Permanent link")

### Which `dtype` should be used?[¶](#which-dtype-should-be-used "Permanent link")

-   Currently, vLLM CPU uses model default settings as `dtype`. However, due to unstable float16 support in torch CPU, it is recommended to explicitly set `dtype=bfloat16` if there are any performance or accuracy problem.

### How to launch a vLLM service on CPU?[¶](#how-to-launch-a-vllm-service-on-cpu "Permanent link")

-   When using the online serving, it is recommended to reserve 1-2 CPU cores for the serving framework to avoid CPU oversubscription. For example, on a platform with 32 physical CPU cores, reserving CPU 31 for the framework and using CPU 0-30 for inference threads:

    export VLLM_CPU_KVCACHE_SPACE=40
    export VLLM_CPU_OMP_THREADS_BIND=0-30
    vllm serve facebook/opt-125m --dtype=bfloat16

or using default auto thread binding:

    export VLLM_CPU_KVCACHE_SPACE=40
    export VLLM_CPU_NUM_OF_RESERVED_CPU=1
    vllm serve facebook/opt-125m --dtype=bfloat16

Note, it is recommended to manually reserve 1 CPU for vLLM front-end process when `world_size == 1`.

### What are supported models on CPU?[¶](#what-are-supported-models-on-cpu "Permanent link")

For the full and up-to-date list of models validated on CPU platforms, please see the official documentation: [Supported Models on CPU](https://docs.vllm.ai/en/latest/models/hardware_supported_models/cpu)

### How to find benchmark configuration examples for supported CPU models?[¶](#how-to-find-benchmark-configuration-examples-for-supported-cpu-models "Permanent link")

For any model listed under [Supported Models on CPU](https://docs.vllm.ai/en/latest/models/hardware_supported_models/cpu), optimized runtime configurations are provided in the vLLM Benchmark Suite's CPU test cases, defined in [cpu test cases](https://github.com/vllm-project/vllm/blob/main/.buildkite/performance-benchmarks/tests/serving-tests-cpu.json) For details on how these optimized configurations are determined, see: [performance-benchmark-details](https://github.com/vllm-project/vllm/tree/main/.buildkite/performance-benchmarks#performance-benchmark-details). To benchmark the supported models using these optimized settings, follow the steps in [running vLLM Benchmark Suite manually](https://docs.vllm.ai/en/latest/contributing/benchmarks/#manually-trigger-the-benchmark) and run the Benchmark Suite on a CPU environment.

Below is an example command to benchmark all CPU-supported models using optimized configurations.

    ON_CPU=1 bash .buildkite/performance-benchmarks/scripts/run-performance-benchmarks.sh

The benchmark results will be saved in `./benchmark/results/`. In the directory, the generated `.commands` files contain all example commands for the benchmark.

We recommend configuring tensor-parallel-size to match the number of NUMA nodes on your system. Note that the current release does not support tensor-parallel-size=6. To determine the number of NUMA nodes available, use the following command:

    lscpu | grep "NUMA node(s):" | awk ''

For performance reference, users may also consult the [vLLM Performance Dashboard](https://hud.pytorch.org/benchmark/llms?repoName=vllm-project%2Fvllm&deviceName=cpu) , which publishes default-model CPU results produced using the same Benchmark Suite.

### How to decide `VLLM_CPU_OMP_THREADS_BIND`?[¶](#how-to-decide-vllm_cpu_omp_threads_bind "Permanent link")

-   Default `auto` thread-binding is recommended for most cases. Ideally, each OpenMP thread will be bound to a dedicated physical core respectively, threads of each rank will be bound to the same NUMA node respectively, and 1 CPU per rank will be reserved for other vLLM components when `world_size > 1`. If you have any performance problems or unexpected binding behaviours, please try to bind threads as following.

-   On a hyper-threading enabled platform with 16 logical CPU cores / 8 physical CPU cores:

Commands

    $ lscpu -e # check the mapping between logical CPU cores and physical CPU cores

    # The "CPU" column means the logical CPU core IDs, and the "CORE" column means the physical core IDs. On this platform, two logical cores are sharing one physical core.
    CPU NODE SOCKET CORE L1d:L1i:L2:L3 ONLINE    MAXMHZ   MINMHZ      MHZ
    0    0      0    0 0:0:0:0          yes 2401.0000 800.0000  800.000
    1    0      0    1 1:1:1:0          yes 2401.0000 800.0000  800.000
    2    0      0    2 2:2:2:0          yes 2401.0000 800.0000  800.000
    3    0      0    3 3:3:3:0          yes 2401.0000 800.0000  800.000
    4    0      0    4 4:4:4:0          yes 2401.0000 800.0000  800.000
    5    0      0    5 5:5:5:0          yes 2401.0000 800.0000  800.000
    6    0      0    6 6:6:6:0          yes 2401.0000 800.0000  800.000
    7    0      0    7 7:7:7:0          yes 2401.0000 800.0000  800.000
    8    0      0    0 0:0:0:0          yes 2401.0000 800.0000  800.000
    9    0      0    1 1:1:1:0          yes 2401.0000 800.0000  800.000
    10   0      0    2 2:2:2:0          yes 2401.0000 800.0000  800.000
    11   0      0    3 3:3:3:0          yes 2401.0000 800.0000  800.000
    12   0      0    4 4:4:4:0          yes 2401.0000 800.0000  800.000
    13   0      0    5 5:5:5:0          yes 2401.0000 800.0000  800.000
    14   0      0    6 6:6:6:0          yes 2401.0000 800.0000  800.000
    15   0      0    7 7:7:7:0          yes 2401.0000 800.0000  800.000

    # On this platform, it is recommended to only bind openMP threads on logical CPU cores 0-7 or 8-15
    $ export VLLM_CPU_OMP_THREADS_BIND=0-7
    $ python examples/offline_inference/basic/basic.py

-   When deploying vLLM CPU backend on a multi-socket machine with NUMA and enable tensor parallel or pipeline parallel, each NUMA node is treated as a TP/PP rank. So be aware to set CPU cores of a single rank on the same NUMA node to avoid cross NUMA node memory access.

### How to decide `VLLM_CPU_KVCACHE_SPACE`?[¶](#how-to-decide-vllm_cpu_kvcache_space "Permanent link")

This value is 4GB by default. Larger space can support more concurrent requests, longer context length. However, users should take care of memory capacity of each NUMA node. The memory usage of each TP rank is the sum of `weight shard size` and `VLLM_CPU_KVCACHE_SPACE`, if it exceeds the capacity of a single NUMA node, the TP worker will be killed with `exitcode 9` due to out-of-memory.

### How to do performance tuning for vLLM CPU?[¶](#how-to-do-performance-tuning-for-vllm-cpu "Permanent link")

First of all, please make sure the thread-binding and KV cache space are properly set and take effect. You can check the thread-binding by running a vLLM benchmark and observing CPU cores usage via `htop`.

Use multiples of 32 as `--block-size`, which is 128 by default.

Inference batch size is an important parameter for the performance. A larger batch usually provides higher throughput, a smaller batch provides lower latency. Tuning the max batch size starting from the default value to balance throughput and latency is an effective way to improve vLLM CPU performance on specific platforms. There are two important related parameters in vLLM:

-   `--max-num-batched-tokens`, defines the limit of token numbers in a single batch, has more impacts on the first token performance. The default value is set as:
    -   Offline Inference: `4096 * world_size`
    -   Online Serving: `2048 * world_size`
-   `--max-num-seqs`, defines the limit of sequence numbers in a single batch, has more impacts on the output token performance.
    -   Offline Inference: `256 * world_size`
    -   Online Serving: `128 * world_size`

vLLM CPU supports data parallel (DP), tensor parallel (TP) and pipeline parallel (PP) to leverage multiple CPU sockets and memory nodes. For more details of tuning DP, TP and PP, please refer to [Optimization and Tuning](../../../configuration/optimization/). For vLLM CPU, it is recommended to use DP, TP and PP together if there are enough CPU sockets and memory nodes.

### Which quantization configs does vLLM CPU support?[¶](#which-quantization-configs-does-vllm-cpu-support "Permanent link")

-   vLLM CPU supports quantizations:
    -   AWQ (x86 only)
    -   GPTQ (x86 only)
    -   compressed-tensor INT8 W8A8 (x86, s390x)

### (x86 only) What is the purpose of `VLLM_CPU_SGL_KERNEL`?[¶](#x86-only-what-is-the-purpose-of-vllm_cpu_sgl_kernel "Permanent link")

-   Both of them require `amx` CPU flag.
    -   `VLLM_CPU_SGL_KERNEL` can provide better performance for MoE models and small-batch scenarios.

### Why do I see `get_mempolicy: Operation not permitted` when running in Docker?[¶](#why-do-i-see-get_mempolicy-operation-not-permitted-when-running-in-docker "Permanent link")

In some container environments (like Docker), NUMA-related syscalls used by vLLM (e.g., `get_mempolicy`, `migrate_pages`) are blocked/denied in the runtime\'s default seccomp/capabilities settings. This may lead to warnings like `get_mempolicy: Operation not permitted`. Functionality is not affected, but NUMA memory binding/migration optimizations may not take effect and performance can be suboptimal.

To enable these optimizations inside Docker with the least privilege, you can follow below tips:

    docker run ... --cap-add SYS_NICE --security-opt seccomp=unconfined  ...

    # 1) `--cap-add SYS_NICE` is to address `get_mempolicy` EPERM issue.

    # 2) `--security-opt seccomp=unconfined` is to enable `migrate_pages` for `numa_migrate_pages()`.
    # Actually, `seccomp=unconfined` bypasses the seccomp for container,
    # if it's unacceptable, you can customize your own seccomp profile,
    # based on docker/runtime default.json and add `migrate_pages` to `SCMP_ACT_ALLOW` list.

    # reference : https://docs.docker.com/engine/security/seccomp/

Alternatively, running with `--privileged=true` also works but is broader and not generally recommended.

In K8S, the following configuration can be added to workload yaml to achieve the same effect as above:

    securityContext:
      seccompProfile:
        type: Unconfined
      capabilities:
        add:
        - SYS_NICE

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [December 3, 2025] ]