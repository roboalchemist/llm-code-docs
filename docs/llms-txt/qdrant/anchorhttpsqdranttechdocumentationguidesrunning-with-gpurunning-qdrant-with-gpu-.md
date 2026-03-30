# [Anchor](https://qdrant.tech/documentation/guides/running-with-gpu/\#running-qdrant-with-gpu-support) Running Qdrant with GPU Support

Starting from version v1.13.0, Qdrant offers support for GPU acceleration.

However, GPU support is not included in the default Qdrant binary due to additional dependencies and libraries. Instead, you will need to use dedicated Docker images with GPU support ( [NVIDIA](https://qdrant.tech/documentation/guides/running-with-gpu/#nvidia-gpus), [AMD](https://qdrant.tech/documentation/guides/running-with-gpu/#amd-gpus)).

## [Anchor](https://qdrant.tech/documentation/guides/running-with-gpu/\#configuration) Configuration

Qdrant includes a number of configuration options to control GPU usage. The following options are available:

```yaml
gpu:
    # Enable GPU indexing.
    indexing: false
    # Force half precision for `f32` values while indexing.
    # `f16` conversion will take place
    # only inside GPU memory and won't affect storage type.
    force_half_precision: false
    # Used vulkan "groups" of GPU.
    # In other words, how many parallel points can be indexed by GPU.
    # Optimal value might depend on the GPU model.
    # Proportional, but doesn't necessary equal
    # to the physical number of warps.
    # Do not change this value unless you know what you are doing.
    # Default: 512
    groups_count: 512
    # Filter for GPU devices by hardware name. Case insensitive.
    # Comma-separated list of substrings to match
    # against the gpu device name.
    # Example: "nvidia"
    # Default: "" - all devices are accepted.
    device_filter: ""
    # List of explicit GPU devices to use.
    # If host has multiple GPUs, this option allows to select specific devices
    # by their index in the list of found devices.
    # If `device_filter` is set, indexes are applied after filtering.
    # By default, all devices are accepted.
    devices: null
    # How many parallel indexing processes are allowed to run.
    # Default: 1
    parallel_indexes: 1
    # Allow to use integrated GPUs.
    # Default: false
    allow_integrated: false
    # Allow to use emulated GPUs like LLVMpipe. Useful for CI.
    # Default: false
    allow_emulated: false

```

It is not recommended to change these options unless you are familiar with the Qdrant internals and the Vulkan API.

## [Anchor](https://qdrant.tech/documentation/guides/running-with-gpu/\#standalone-gpu-support) Standalone GPU Support

For standalone usage, you can build Qdrant with GPU support by running the following command:

```bash
cargo build --release --features gpu

```

Ensure your device supports Vulkan API v1.3. This includes compatibility with Apple Silicon, Intel GPUs, and CPU emulators. Note that `gpu.indexing: true` must be set in your configuration to use GPUs at runtime.

## [Anchor](https://qdrant.tech/documentation/guides/running-with-gpu/\#nvidia-gpus) NVIDIA GPUs

### [Anchor](https://qdrant.tech/documentation/guides/running-with-gpu/\#prerequisites) Prerequisites

To use Docker with NVIDIA GPU support, ensure the following are installed on your host:

- Latest NVIDIA drivers
- [nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

Most AI or CUDA images on Amazon/GCP come pre-configured with the NVIDIA container toolkit.

### [Anchor](https://qdrant.tech/documentation/guides/running-with-gpu/\#docker-images-with-nvidia-gpu-support) Docker images with NVIDIA GPU support

Docker images with NVIDIA GPU support use the tag suffix `gpu-nvidia`, e.g., `qdrant/qdrant:v1.13.0-gpu-nvidia`. These images include all necessary dependencies.

To enable GPU support, use the `--gpus=all` flag with Docker settings. Example:

```bash