# Source: https://docs.vllm.ai/en/stable/getting_started/installation/gpu/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/getting_started/installation/gpu.md "Edit this page")

# GPU[¶](#gpu "Permanent link")

vLLM is a Python library that supports the following GPU variants. Select your GPU type to see vendor specific instructions:

NVIDIA CUDAAMD ROCmIntel XPU

vLLM contains pre-compiled C++ and CUDA (12.8) binaries.

vLLM supports AMD GPUs with ROCm 6.3 or above, and torch 2.8.0 and above.

Tip

[Docker](#set-up-using-docker) is the recommended way to use vLLM on ROCm.

vLLM initially supports basic model inference and serving on Intel GPU platform.

## Requirements[¶](#requirements "Permanent link")

-   OS: Linux
-   Python: 3.10 \-- 3.13

Note

vLLM does not support Windows natively. To run vLLM on Windows, you can use the Windows Subsystem for Linux (WSL) with a compatible Linux distribution, or use some community-maintained forks, e.g. <https://github.com/SystemPanic/vllm-windows>.

NVIDIA CUDAAMD ROCmIntel XPU

-   GPU: compute capability 7.0 or higher (e.g., V100, T4, RTX20xx, A100, L4, H100, etc.)

-   GPU: MI200s (gfx90a), MI300 (gfx942), MI350 (gfx950), Radeon RX 7900 series (gfx1100/1101), Radeon RX 9000 series (gfx1200/1201), Ryzen AI MAX / AI 300 Series (gfx1151/1150)
-   ROCm 6.3 or above
    -   MI350 requires ROCm 7.0 or above
    -   Ryzen AI MAX / AI 300 Series requires ROCm 7.0.2 or above

-   Supported Hardware: Intel Data Center GPU, Intel ARC GPU
-   OneAPI requirements: oneAPI 2025.1
-   Python: 3.12

Warning

The provided IPEX whl is Python3.12 specific so this version is a MUST.

## Set up using Python[¶](#set-up-using-python "Permanent link")

### Create a new Python environment[¶](#create-a-new-python-environment "Permanent link")

On NVIDIA CUDA only, it\'s recommended to use [uv](https://docs.astral.sh/uv/), a very fast Python environment manager, to create and manage Python environments. Please follow the [documentation](https://docs.astral.sh/uv/#getting-started) to install `uv`. After installing `uv`, you can create a new Python environment using the following commands:

    uv venv --python 3.12 --seed
    source .venv/bin/activate

NVIDIA CUDAAMD ROCmIntel XPU

Note

PyTorch installed via `conda` will statically link `NCCL` library, which can cause issues when vLLM tries to use `NCCL`. See <https://github.com/vllm-project/vllm/issues/8420> for more details.

In order to be performant, vLLM has to compile many cuda kernels. The compilation unfortunately introduces binary incompatibility with other CUDA versions and PyTorch versions, even for the same PyTorch version with different building configurations.

Therefore, it is recommended to install vLLM with a **fresh new** environment. If either you have a different CUDA version or you want to use an existing PyTorch installation, you need to build vLLM from source. See [below](#build-wheel-from-source) for more details.

There is no extra information on creating a new Python environment for this device.

There is no extra information on creating a new Python environment for this device.

### Pre-built wheels[¶](#pre-built-wheels "Permanent link")

NVIDIA CUDAAMD ROCmIntel XPU

    uv pip install vllm --torch-backend=auto

pip

    # Install vLLM with CUDA 12.9.
    pip install vllm --extra-index-url https://download.pytorch.org/whl/cu129

We recommend leveraging `uv` to [automatically select the appropriate PyTorch index at runtime](https://docs.astral.sh/uv/guides/integration/pytorch/#automatic-backend-selection) by inspecting the installed CUDA driver version via `--torch-backend=auto` (or `UV_TORCH_BACKEND=auto`). To select a specific backend (e.g., `cu128`), set `--torch-backend=cu128` (or `UV_TORCH_BACKEND=cu128`). If this doesn\'t work, try running `uv self update` to update `uv` first.

Note

NVIDIA Blackwell GPUs (B200, GB200) require a minimum of CUDA 12.8, so make sure you are installing PyTorch wheels with at least that version. PyTorch itself offers a [dedicated interface](https://pytorch.org/get-started/locally/) to determine the appropriate pip command to run for a given target configuration.

As of now, vLLM\'s binaries are compiled with CUDA 12.9 and public PyTorch release versions by default. We also provide vLLM binaries compiled with CUDA 12.8, 13.0, and public PyTorch release versions:

    # Install vLLM with a specific CUDA version (e.g., 13.0).
    export VLLM_VERSION=$(curl -s https://api.github.com/repos/vllm-project/vllm/releases/latest | jq -r .tag_name | sed 's/^v//')
    export CUDA_VERSION=130 # or other
    uv pip install https://github.com/vllm-project/vllm/releases/download/v$/vllm-$+cu$-cp38-abi3-manylinux_2_31_x86_64.whl --extra-index-url https://download.pytorch.org/whl/cu$

#### Install the latest code[¶](#install-the-latest-code "Permanent link")

LLM inference is a fast-evolving field, and the latest code may contain bug fixes, performance improvements, and new features that are not released yet. To allow users to try the latest code without waiting for the next release, vLLM provides wheels for every commit since `v0.5.3` on <https://wheels.vllm.ai/nightly>. There are multiple indices that could be used:

-   `https://wheels.vllm.ai/nightly`: the default variant (CUDA with version specified in `VLLM_MAIN_CUDA_VERSION`) built with the last commit on the `main` branch. Currently it is CUDA 12.9.
-   `https://wheels.vllm.ai/nightly/<variant>`: all other variants. Now this includes `cu130`, and `cpu`. The default variant (`cu129`) also has a subdirectory to keep consistency.

To install from nightly index, run:

    uv pip install -U vllm \
        --torch-backend=auto \
        --extra-index-url https://wheels.vllm.ai/nightly # add variant subdirectory here if needed

`pip` caveat

Using `pip` to install from nightly indices is *not supported*, because `pip` combines packages from `--extra-index-url` and the default index, choosing only the latest version, which makes it difficult to install a development version prior to the released version. In contrast, `uv` gives the extra index [higher priority than the default index](https://docs.astral.sh/uv/pip/compatibility/#packages-that-exist-on-multiple-indexes).

If you insist on using `pip`, you have to specify the full URL of the wheel file (which can be obtained from the web page).

    pip install -U https://wheels.vllm.ai/nightly/vllm-0.11.2.dev399%2Bg3c7461c18-cp38-abi3-manylinux_2_31_x86_64.whl # current nightly build (the filename will change!)
    pip install -U https://wheels.vllm.ai/$/vllm-0.11.2.dev399%2Bg3c7461c18-cp38-abi3-manylinux_2_31_x86_64.whl # from specific commit

##### Install specific revisions[¶](#install-specific-revisions "Permanent link")

If you want to access the wheels for previous commits (e.g. to bisect the behavior change, performance regression), you can specify the commit hash in the URL:

    export VLLM_COMMIT=72d9c316d3f6ede485146fe5aabd4e61dbc59069 # use full commit hash from the main branch
    uv pip install vllm \
        --torch-backend=auto \
        --extra-index-url https://wheels.vllm.ai/$ # add variant subdirectory here if needed

Currently, there are no pre-built ROCm wheels.

Currently, there are no pre-built XPU wheels.

### Build wheel from source[¶](#build-wheel-from-source "Permanent link")

NVIDIA CUDAAMD ROCmIntel XPU

#### Set up using Python-only build (without compilation)[¶](#python-only-build "Permanent link") 

If you only need to change Python code, you can build and install vLLM without compilation. Using `uv pip`\'s [`--editable` flag](https://docs.astral.sh/uv/pip/packages/#editable-packages), changes you make to the code will be reflected when you run vLLM:

    git clone https://github.com/vllm-project/vllm.git
    cd vllm
    VLLM_USE_PRECOMPILED=1 uv pip install --editable .

This command will do the following:

1.  Look for the current branch in your vLLM clone.
2.  Identify the corresponding base commit in the main branch.
3.  Download the pre-built wheel of the base commit.
4.  Use its compiled libraries in the installation.

Note

1.  If you change C++ or kernel code, you cannot use Python-only build; otherwise you will see an import error about library not found or undefined symbol.
2.  If you rebase your dev branch, it is recommended to uninstall vllm and re-run the above command to make sure your libraries are up to date.

In case you see an error about wheel not found when running the above command, it might be because the commit you based on in the main branch was just merged and the wheel is being built. In this case, you can wait for around an hour to try again, or manually assign the previous commit in the installation using the `VLLM_PRECOMPILED_WHEEL_LOCATION` environment variable.

    export VLLM_PRECOMPILED_WHEEL_COMMIT=$(git rev-parse HEAD~1) # or earlier commit on main
    export VLLM_USE_PRECOMPILED=1
    uv pip install --editable .

There are more environment variables to control the behavior of Python-only build:

-   `VLLM_PRECOMPILED_WHEEL_LOCATION`: specify the exact wheel URL or local file path of a pre-compiled wheel to use. All other logic to find the wheel will be skipped.
-   `VLLM_PRECOMPILED_WHEEL_COMMIT`: override the commit hash to download the pre-compiled wheel. It can be `nightly` to use the last **already built** commit on the main branch.
-   `VLLM_PRECOMPILED_WHEEL_VARIANT`: specify the variant subdirectory to use on the nightly index, e.g., `cu129`, `cpu`. If not specified, the CUDA variant with `VLLM_MAIN_CUDA_VERSION` will be tried, then fallback to the default variant on the remote index.

You can find more information about vLLM\'s wheels in [Install the latest code](#install-the-latest-code).

Note

There is a possibility that your source code may have a different commit ID compared to the latest vLLM wheel, which could potentially lead to unknown errors. It is recommended to use the same commit ID for the source code as the vLLM wheel you have installed. Please refer to [Install the latest code](#install-the-latest-code) for instructions on how to install a specified wheel.

#### Full build (with compilation)[¶](#full-build "Permanent link") 

If you want to modify C++ or CUDA code, you\'ll need to build vLLM from source. This can take several minutes:

    git clone https://github.com/vllm-project/vllm.git
    cd vllm
    uv pip install -e .

Tip

Building from source requires a lot of compilation. If you are building from source repeatedly, it\'s more efficient to cache the compilation results.

For example, you can install [ccache](https://github.com/ccache/ccache) using `conda install ccache` or `apt install ccache` . As long as `which ccache` command can find the `ccache` binary, it will be used automatically by the build system. After the first build, subsequent builds will be much faster.

When using `ccache` with `pip install -e .`, you should run `CCACHE_NOHASHDIR="true" pip install --no-build-isolation -e .`. This is because `pip` creates a new folder with a random name for each build, preventing `ccache` from recognizing that the same files are being built.

[sccache](https://github.com/mozilla/sccache) works similarly to `ccache`, but has the capability to utilize caching in remote storage environments. The following environment variables can be set to configure the vLLM `sccache` remote: `SCCACHE_BUCKET=vllm-build-sccache SCCACHE_REGION=us-west-2 SCCACHE_S3_NO_CREDENTIALS=1`. We also recommend setting `SCCACHE_IDLE_TIMEOUT=0`.

Faster Kernel Development

For frequent C++/CUDA kernel changes, after the initial `uv pip install -e .` setup, consider using the [Incremental Compilation Workflow](../../../contributing/incremental_build/) for significantly faster rebuilds of only the modified kernel code.

##### Use an existing PyTorch installation[¶](#use-an-existing-pytorch-installation "Permanent link")

There are scenarios where the PyTorch dependency cannot be easily installed with `uv`, for example, when building vLLM with non-default PyTorch builds (like nightly or a custom build).

To build vLLM using an existing PyTorch installation:

    # install PyTorch first, either from PyPI or from source
    git clone https://github.com/vllm-project/vllm.git
    cd vllm
    python use_existing_torch.py
    uv pip install -r requirements/build.txt
    uv pip install --no-build-isolation -e .

Alternatively: if you are exclusively using `uv` to create and manage virtual environments, it has [a unique mechanism](https://docs.astral.sh/uv/concepts/projects/config/#disabling-build-isolation) for disabling build isolation for specific packages. vLLM can leverage this mechanism to specify `torch` as the package to disable build isolation for:

    # install PyTorch first, either from PyPI or from source
    git clone https://github.com/vllm-project/vllm.git
    cd vllm
    # pip install -e . does not work directly, only uv can do this
    uv pip install -e .

##### Use the local cutlass for compilation[¶](#use-the-local-cutlass-for-compilation "Permanent link")

Currently, before starting the build process, vLLM fetches cutlass code from GitHub. However, there may be scenarios where you want to use a local version of cutlass instead. To achieve this, you can set the environment variable VLLM_CUTLASS_SRC_DIR to point to your local cutlass directory.

    git clone https://github.com/vllm-project/vllm.git
    cd vllm
    VLLM_CUTLASS_SRC_DIR=/path/to/cutlass uv pip install -e .

##### Troubleshooting[¶](#troubleshooting "Permanent link")

To avoid your system being overloaded, you can limit the number of compilation jobs to be run simultaneously, via the environment variable `MAX_JOBS`. For example:

    export MAX_JOBS=6
    uv pip install -e .

This is especially useful when you are building on less powerful machines. For example, when you use WSL it only [assigns 50% of the total memory by default](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#main-wsl-settings), so using `export MAX_JOBS=1` can avoid compiling multiple files simultaneously and running out of memory. A side effect is a much slower build process.

Additionally, if you have trouble building vLLM, we recommend using the NVIDIA PyTorch Docker image.

    # Use `--ipc=host` to make sure the shared memory is large enough.
    docker run \
        --gpus all \
        -it \
        --rm \
        --ipc=host nvcr.io/nvidia/pytorch:23.10-py3

If you don\'t want to use docker, it is recommended to have a full installation of CUDA Toolkit. You can download and install it from [the official website](https://developer.nvidia.com/cuda-toolkit-archive). After installation, set the environment variable `CUDA_HOME` to the installation path of CUDA Toolkit, and make sure that the `nvcc` compiler is in your `PATH`, e.g.:

    export CUDA_HOME=/usr/local/cuda
    export PATH="$/bin:$PATH"

Here is a sanity check to verify that the CUDA Toolkit is correctly installed:

    nvcc --version # verify that nvcc is in your PATH
    $/bin/nvcc --version # verify that nvcc is in your CUDA_HOME

#### Unsupported OS build[¶](#unsupported-os-build "Permanent link")

vLLM can fully run only on Linux but for development purposes, you can still build it on other systems (for example, macOS), allowing for imports and a more convenient development environment. The binaries will not be compiled and won\'t work on non-Linux systems.

Simply disable the `VLLM_TARGET_DEVICE` environment variable before installing:

    export VLLM_TARGET_DEVICE=empty
    uv pip install -e .

Tip

-   If you found that the following installation step does not work for you, please refer to [docker/Dockerfile.rocm_base](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm_base). Dockerfile is a form of installation steps.

1.  Install prerequisites (skip if you are already in an environment/docker with the following installed):

    -   [ROCm](https://rocm.docs.amd.com/en/latest/deploy/linux/index.html)
    -   [PyTorch](https://pytorch.org/)

    For installing PyTorch, you can start from a fresh docker image, e.g, `rocm/pytorch:rocm7.0_ubuntu22.04_py3.10_pytorch_release_2.8.0`, `rocm/pytorch-nightly`. If you are using docker image, you can skip to Step 3.

    Alternatively, you can install PyTorch using PyTorch wheels. You can check PyTorch installation guide in PyTorch [Getting Started](https://pytorch.org/get-started/locally/). Example:

    ::: 
        # Install PyTorch
        pip uninstall torch -y
        pip install --no-cache-dir torch torchvision --index-url https://download.pytorch.org/whl/nightly/rocm7.0
    :::

2.  Install [Triton for ROCm](https://github.com/ROCm/triton.git)

    Install ROCm\'s Triton following the instructions from [ROCm/triton](https://github.com/ROCm/triton.git)

    ::: 
        python3 -m pip install ninja cmake wheel pybind11
        pip uninstall -y triton
        git clone https://github.com/ROCm/triton.git
        cd triton
        # git checkout $TRITON_BRANCH
        git checkout f9e5bf54
        if [ ! -f setup.py ]; then cd python; fi
        python3 setup.py install
        cd ../..
    :::

    ::: 
    Note

    -   The validated `$TRITON_BRANCH` can be found in the [docker/Dockerfile.rocm_base](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm_base).
    -   If you see HTTP issue related to downloading packages during building triton, please try again as the HTTP error is intermittent.
    :::

3.  Optionally, if you choose to use CK flash attention, you can install [flash attention for ROCm](https://github.com/Dao-AILab/flash-attention.git)

    Install ROCm\'s flash attention (v2.8.0) following the instructions from [ROCm/flash-attention](https://github.com/Dao-AILab/flash-attention#amd-rocm-support)

    For example, for ROCm 7.0, suppose your gfx arch is `gfx942`. To get your gfx architecture, run `rocminfo |grep gfx`.

    ::: 
        git clone https://github.com/Dao-AILab/flash-attention.git
        cd flash-attention
        # git checkout $FA_BRANCH
        git checkout 0e60e394
        git submodule update --init
        GPU_ARCHS="gfx942" python3 setup.py install
        cd ..
    :::

    ::: 
    Note

    -   The validated `$FA_BRANCH` can be found in the [docker/Dockerfile.rocm_base](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm_base).
    :::

4.  If you choose to build AITER yourself to use a certain branch or commit, you can build AITER using the following steps:

    ::: 
        python3 -m pip uninstall -y aiter
        git clone --recursive https://github.com/ROCm/aiter.git
        cd aiter
        git checkout $AITER_BRANCH_OR_COMMIT
        git submodule sync; git submodule update --init --recursive
        python3 setup.py develop
    :::

    ::: 
    Note

    -   You will need to config the `$AITER_BRANCH_OR_COMMIT` for your purpose.
    -   The validated `$AITER_BRANCH_OR_COMMIT` can be found in the [docker/Dockerfile.rocm_base](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm_base).
    :::

5.  Build vLLM. For example, vLLM on ROCM 7.0 can be built with the following steps:

    Commands

    ::: 
        pip install --upgrade pip

        # Build & install AMD SMI
        pip install /opt/rocm/share/amd_smi

        # Install dependencies
        pip install --upgrade numba \
            scipy \
            huggingface-hub[cli,hf_transfer] \
            setuptools_scm
        pip install -r requirements/rocm.txt

        # To build for a single architecture (e.g., MI300) for faster installation (recommended):
        export PYTORCH_ROCM_ARCH="gfx942"

        # To build vLLM for multiple arch MI210/MI250/MI300, use this instead
        # export PYTORCH_ROCM_ARCH="gfx90a;gfx942"

        python3 setup.py develop
    :::

    This may take 5-10 minutes. Currently, `pip install .` does not work for ROCm installation.

    ::: 
    Tip

    -   The ROCm version of PyTorch, ideally, should match the ROCm driver version.
    :::

Tip

-   For MI300x (gfx942) users, to achieve optimal performance, please refer to [MI300x tuning guide](https://rocm.docs.amd.com/en/latest/how-to/tuning-guides/mi300x/index.html) for performance optimization and tuning tips on system and workflow level. For vLLM, please refer to [vLLM performance optimization](https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference-optimization/vllm-optimization.html).

-   First, install required [driver](https://dgpu-docs.intel.com/driver/installation.html#installing-gpu-drivers) and [Intel OneAPI](https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit.html) 2025.1 or later.
-   Second, install Python packages for vLLM XPU backend building:

    git clone https://github.com/vllm-project/vllm.git
    cd vllm
    pip install --upgrade pip
    pip install -v -r requirements/xpu.txt

-   Then, build and install vLLM XPU backend:

    VLLM_TARGET_DEVICE=xpu python setup.py install

## Set up using Docker[¶](#set-up-using-docker "Permanent link")

### Pre-built images[¶](#pre-built-images "Permanent link")

NVIDIA CUDAAMD ROCmIntel XPU

See [Using Docker](../../../deployment/docker/) for instructions on using the official Docker image.

Another way to access the latest code is to use the docker images:

    export VLLM_COMMIT=33f460b17a54acb3b6cc0b03f4a17876cff5eafd # use full commit hash from the main branch
    docker pull public.ecr.aws/q9t5s3a7/vllm-ci-postmerge-repo:$

These docker images are used for CI and testing only, and they are not intended for production use. They will be expired after several days.

The latest code can contain bugs and may not be stable. Please use it with caution.

The [AMD Infinity hub for vLLM](https://hub.docker.com/r/rocm/vllm/tags) offers a prebuilt, optimized docker image designed for validating inference performance on the AMD Instinct™ MI300X accelerator. AMD also offers nightly prebuilt docker image from [Docker Hub](https://hub.docker.com/r/rocm/vllm-dev), which has vLLM and all its dependencies installed.

Commands

    docker pull rocm/vllm-dev:nightly # to get the latest image
    docker run -it --rm \
    --network=host \
    --group-add=video \
    --ipc=host \
    --cap-add=SYS_PTRACE \
    --security-opt seccomp=unconfined \
    --device /dev/kfd \
    --device /dev/dri \
    -v <path/to/your/models>:/app/models \
    -e HF_HOME="/app/models" \
    rocm/vllm-dev:nightly

Tip

Please check [LLM inference performance validation on AMD Instinct MI300X](https://rocm.docs.amd.com/en/latest/how-to/performance-validation/mi300x/vllm-benchmark.html) for instructions on how to use this prebuilt docker image.

Currently, we release prebuilt XPU images at docker [hub](https://hub.docker.com/r/intel/vllm/tags) based on vLLM released version. For more information, please refer release [note](https://github.com/intel/ai-containers/blob/main/vllm).

### Build image from source[¶](#build-image-from-source "Permanent link")

NVIDIA CUDAAMD ROCmIntel XPU

See [Building vLLM\'s Docker Image from Source](../../../deployment/docker/#building-vllms-docker-image-from-source) for instructions on building the Docker image.

Building the Docker image from source is the recommended way to use vLLM with ROCm.

(Optional) Build an image with ROCm software stack

Build a docker image from [docker/Dockerfile.rocm_base](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm_base) which setup ROCm software stack needed by the vLLM. **This step is optional as this rocm_base image is usually prebuilt and store at [Docker Hub](https://hub.docker.com/r/rocm/vllm-dev) under tag `rocm/vllm-dev:base` to speed up user experience.** If you choose to build this rocm_base image yourself, the steps are as follows.

It is important that the user kicks off the docker build using buildkit. Either the user put DOCKER_BUILDKIT=1 as environment variable when calling docker build command, or the user needs to set up buildkit in the docker daemon configuration /etc/docker/daemon.json as follows and restart the daemon:

    
    }

To build vllm on ROCm 7.0 for MI200 and MI300 series, you can use the default:

    DOCKER_BUILDKIT=1 docker build \
        -f docker/Dockerfile.rocm_base \
        -t rocm/vllm-dev:base .

#### Build an image with vLLM[¶](#build-an-image-with-vllm "Permanent link")

First, build a docker image from [docker/Dockerfile.rocm](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm) and launch a docker container from the image. It is important that the user kicks off the docker build using buildkit. Either the user put `DOCKER_BUILDKIT=1` as environment variable when calling docker build command, or the user needs to set up buildkit in the docker daemon configuration /etc/docker/daemon.json as follows and restart the daemon:

    
    }

[docker/Dockerfile.rocm](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm) uses ROCm 7.0 by default, but also supports ROCm 5.7, 6.0, 6.1, 6.2, 6.3, and 6.4, in older vLLM branches. It provides flexibility to customize the build of docker image using the following arguments:

-   `BASE_IMAGE`: specifies the base image used when running `docker build`. The default value `rocm/vllm-dev:base` is an image published and maintained by AMD. It is being built using [docker/Dockerfile.rocm_base](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm_base)
-   `ARG_PYTORCH_ROCM_ARCH`: Allows to override the gfx architecture values from the base docker image

Their values can be passed in when running `docker build` with `--build-arg` options.

To build vllm on ROCm 7.0 for MI200 and MI300 series, you can use the default:

Commands

    DOCKER_BUILDKIT=1 docker build -f docker/Dockerfile.rocm -t vllm-rocm .

To run the above docker image `vllm-rocm`, use the below command:

Commands

    docker run -it \
    --network=host \
    --group-add=video \
    --ipc=host \
    --cap-add=SYS_PTRACE \
    --security-opt seccomp=unconfined \
    --device /dev/kfd \
    --device /dev/dri \
    -v <path/to/model>:/app/model \
    vllm-rocm

Where the `<path/to/model>` is the location where the model is stored, for example, the weights for llama2 or llama3 models.

    docker build -f docker/Dockerfile.xpu -t vllm-xpu-env --shm-size=4g .
    docker run -it \
                 --rm \
                 --network=host \
                 --device /dev/dri:/dev/dri \
                 -v /dev/dri/by-path:/dev/dri/by-path \
                 --ipc=host \
                 --privileged \
                 vllm-xpu-env

## Supported features[¶](#supported-features "Permanent link")

NVIDIA CUDAAMD ROCmIntel XPU

See [Feature x Hardware](../../../features/#feature-x-hardware) compatibility matrix for feature support information.

See [Feature x Hardware](../../../features/#feature-x-hardware) compatibility matrix for feature support information.

XPU platform supports **tensor parallel** inference/serving and also supports **pipeline parallel** as a beta feature for online serving. For **pipeline parallel**, we support it on single node with mp as the backend. For example, a reference execution like following:

    vllm serve facebook/opt-13b \
         --dtype=bfloat16 \
         --max_model_len=1024 \
         --distributed-executor-backend=mp \
         --pipeline-parallel-size=2 \
         -tp=8

By default, a ray instance will be launched automatically if no existing one is detected in the system, with `num-gpus` equals to `parallel_config.world_size`. We recommend properly starting a ray cluster before execution, referring to the [examples/online_serving/run_cluster.sh](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/run_cluster.sh) helper script.

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [December 2, 2025] ]