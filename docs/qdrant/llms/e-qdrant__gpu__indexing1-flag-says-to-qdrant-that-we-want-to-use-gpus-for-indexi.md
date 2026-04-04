# `-e QDRANT__GPU__INDEXING=1` flag says to Qdrant that we want to use GPUs for indexing.
docker run \
	--rm \
	--gpus=all \
	-p 6333:6333 \
	-p 6334:6334 \
	-e QDRANT__GPU__INDEXING=1 \
	qdrant/qdrant:gpu-nvidia-latest

```

To ensure that the GPU was initialized correctly, you may check it in logs. First Qdrant prints all found GPU devices without filtering and then prints list of all created devices:

```text
2025-01-13T11:58:29.124087Z  INFO gpu::instance: Found GPU device: NVIDIA GeForce RTX 3090
2025-01-13T11:58:29.124118Z  INFO gpu::instance: Found GPU device: llvmpipe (LLVM 15.0.7, 256 bits)
2025-01-13T11:58:29.124138Z  INFO gpu::device: Create GPU device NVIDIA GeForce RTX 3090

```

Here you can see that two devices were found: RTX 3090 and llvmpipe (a CPU-emulated GPU which is included in the Docker image). Later, you will see that only RTX was initialized.

This concludes the setup. Now, you can start using this Qdrant instance.

### [Anchor](https://qdrant.tech/documentation/guides/running-with-gpu/\#troubleshooting-nvidia-gpus) Troubleshooting NVIDIA GPUs

If your GPU is not detected in Docker, make sure your driver and `nvidia-container-toolkit` are up-to-date.
If needed, you can install latest version of `nvidia-container-toolkit` from it’s GitHub Releases [page](https://github.com/NVIDIA/nvidia-container-toolkit/releases)

Verify Vulkan API visibility in the Docker container using:

```bash
docker run --rm --gpus=all qdrant/qdrant:gpu-nvidia-latest vulkaninfo --summary

```

The system may show you an error message explaining why the NVIDIA device is not visible.
Note that if your NVIDIA GPU is not visible in Docker, the Docker image cannot use libGLX\_nvidia.so.0 on your host. Here is what an error message could look like:

```text
ERROR: [Loader Message] Code 0 : loader_scanned_icd_add: Could not get `vkCreateInstance` via `vk_icdGetInstanceProcAddr` for ICD libGLX_nvidia.so.0
WARNING: [Loader Message] Code 0 : terminator_CreateInstance: Failed to CreateInstance in ICD 0. Skipping ICD.

```

To resolve errors, update your NVIDIA container runtime configuration:

```bash
sudo nano /etc/nvidia-container-runtime/config.toml

```

Set `no-cgroups=false`, save the configuration, and restart Docker:

```bash
sudo systemctl restart docker

```

## [Anchor](https://qdrant.tech/documentation/guides/running-with-gpu/\#amd-gpus) AMD GPUs

### [Anchor](https://qdrant.tech/documentation/guides/running-with-gpu/\#prerequisites-1) Prerequisites

Running Qdrant with AMD GPUs requires [ROCm](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/detailed-install.html) to be installed on your host.

### [Anchor](https://qdrant.tech/documentation/guides/running-with-gpu/\#docker-images-with-amd-gpu-support) Docker images with AMD GPU support

Docker images for AMD GPUs use the tag suffix `gpu-amd`, e.g., `qdrant/qdrant:v1.13.0-gpu-amd`. These images include all required dependencies.

To enable GPU for Docker, you need additional `--device /dev/kfd --device /dev/dri` flags. To enable GPU for Qdrant you need to set the enable flag. Here is an example:

```bash