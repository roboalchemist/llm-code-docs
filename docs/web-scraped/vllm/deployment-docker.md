# Source: https://docs.vllm.ai/en/stable/deployment/docker/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/deployment/docker.md "Edit this page")

# Using Docker[¶](#using-docker "Permanent link")

## Use vLLM\'s Official Docker Image[¶](#use-vllms-official-docker-image "Permanent link")

vLLM offers an official Docker image for deployment. The image can be used to run OpenAI compatible server and is available on Docker Hub as [vllm/vllm-openai](https://hub.docker.com/r/vllm/vllm-openai/tags).

    docker run --runtime nvidia --gpus all \
        -v ~/.cache/huggingface:/root/.cache/huggingface \
        --env "HF_TOKEN=$HF_TOKEN" \
        -p 8000:8000 \
        --ipc=host \
        vllm/vllm-openai:latest \
        --model Qwen/Qwen3-0.6B

This image can also be used with other container engines such as [Podman](https://podman.io/).

    podman run --device nvidia.com/gpu=all \
      -v ~/.cache/huggingface:/root/.cache/huggingface \
      --env "HF_TOKEN=$HF_TOKEN" \
      -p 8000:8000 \
      --ipc=host \
      docker.io/vllm/vllm-openai:latest \
      --model Qwen/Qwen3-0.6B

You can add any other [engine-args](../../configuration/engine_args/) you need after the image tag (`vllm/vllm-openai:latest`).

Note

You can either use the `ipc=host` flag or `--shm-size` flag to allow the container to access the host\'s shared memory. vLLM uses PyTorch, which uses shared memory to share data between processes under the hood, particularly for tensor parallel inference.

Note

Optional dependencies are not included in order to avoid licensing issues (e.g. [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] Issue #8030](https://github.com/vllm-project/vllm/issues/8030)).

If you need to use those dependencies (having accepted the license terms), create a custom Dockerfile on top of the base image with an extra layer that installs them:

    FROM vllm/vllm-openai:v0.11.0

    # e.g. install the `audio` optional dependencies
    # NOTE: Make sure the version of vLLM matches the base image!
    RUN uv pip install --system vllm[audio]==0.11.0

Tip

Some new models may only be available on the main branch of [HF Transformers](https://github.com/huggingface/transformers).

To use the development version of `transformers`, create a custom Dockerfile on top of the base image with an extra layer that installs their code from source:

    FROM vllm/vllm-openai:latest

    RUN uv pip install --system git+https://github.com/huggingface/transformers.git

## Building vLLM\'s Docker Image from Source[¶](#building-vllms-docker-image-from-source "Permanent link")

You can build and run vLLM from source via the provided [[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTggMGM0LjQyIDAgOCAzLjU4IDggOGE4LjAxIDguMDEgMCAwIDEtNS40NSA3LjU5Yy0uNC4wOC0uNTUtLjE3LS41NS0uMzggMC0uMjcuMDEtMS4xMy4wMS0yLjIgMC0uNzUtLjI1LTEuMjMtLjU0LTEuNDggMS43OC0uMiAzLjY1LS44OCAzLjY1LTMuOTUgMC0uODgtLjMxLTEuNTktLjgyLTIuMTUuMDgtLjIuMzYtMS4wMi0uMDgtMi4xMiAwIDAtLjY3LS4yMi0yLjIuODItLjY0LS4xOC0xLjMyLS4yNy0yLS4yN3MtMS4zNi4wOS0yIC4yN2MtMS41My0xLjAzLTIuMi0uODItMi4yLS44Mi0uNDQgMS4xLS4xNiAxLjkyLS4wOCAyLjEyLS41MS41Ni0uODIgMS4yOC0uODIgMi4xNSAwIDMuMDYgMS44NiAzLjc1IDMuNjQgMy45NS0uMjMuMi0uNDQuNTUtLjUxIDEuMDctLjQ2LjIxLTEuNjEuNTUtMi4zMy0uNjYtLjE1LS4yNC0uNi0uODMtMS4yMy0uODItLjY3LjAxLS4yNy4zOC4wMS41My4zNC4xOS43My45LjgyIDEuMTMuMTYuNDUuNjggMS4zMSAyLjY5Ljk0IDAgLjY3LjAxIDEuMy4wMSAxLjQ5IDAgLjIxLS4xNS40NS0uNTUuMzhBNy45OTUgNy45OTUgMCAwIDEgMCA4YzAtNC40MiAzLjU4LTggOC04Ij48L3BhdGg+PC9zdmc+)] docker/Dockerfile](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile). To build vLLM:

    # optionally specifies: --build-arg max_jobs=8 --build-arg nvcc_threads=2
    DOCKER_BUILDKIT=1 docker build . \
        --target vllm-openai \
        --tag vllm/vllm-openai \
        --file docker/Dockerfile

Note

By default vLLM will build for all GPU types for widest distribution. If you are just building for the current GPU type the machine is running on, you can add the argument `--build-arg torch_cuda_arch_list=""` for vLLM to find the current GPU type and build for that.

If you are using Podman instead of Docker, you might need to disable SELinux labeling by adding `--security-opt label=disable` when running `podman build` command to avoid certain [existing issues](https://github.com/containers/buildah/discussions/4184).

## Building for Arm64/aarch64[¶](#building-for-arm64aarch64 "Permanent link")

A docker container can be built for aarch64 systems such as the Nvidia Grace-Hopper and Grace-Blackwell. Using the flag `--platform "linux/arm64"` will build for arm64.

Note

Multiple modules must be compiled, so this process can take a while. Recommend using `--build-arg max_jobs=` & `--build-arg nvcc_threads=` flags to speed up build process. However, ensure your `max_jobs` is substantially larger than `nvcc_threads` to get the most benefits. Keep an eye on memory usage with parallel jobs as it can be substantial (see example below).

Command

    # Example of building on Nvidia GH200 server. (Memory usage: ~15GB, Build time: ~1475s / ~25 min, Image size: 6.93GB)
    DOCKER_BUILDKIT=1 docker build . \
    --file docker/Dockerfile \
    --target vllm-openai \
    --platform "linux/arm64" \
    -t vllm/vllm-gh200-openai:latest \
    --build-arg max_jobs=66 \
    --build-arg nvcc_threads=2 \
    --build-arg torch_cuda_arch_list="9.0 10.0+PTX" \
    --build-arg RUN_WHEEL_CHECK=false

For (G)B300, we recommend using CUDA 13, as shown in the following command.

Command

    DOCKER_BUILDKIT=1 docker build \
    --build-arg CUDA_VERSION=13.0.1 \
    --build-arg BUILD_BASE_IMAGE=nvidia/cuda:13.0.1-devel-ubuntu22.04 \
    --build-arg max_jobs=256 \
    --build-arg nvcc_threads=2 \
    --build-arg RUN_WHEEL_CHECK=false \
    --build-arg torch_cuda_arch_list='9.0 10.0+PTX' \
    --platform "linux/arm64" \
    --tag vllm/vllm-gb300-openai:latest \
    --target vllm-openai \
    -f docker/Dockerfile \
    .

Note

If you are building the `linux/arm64` image on a non-ARM host (e.g., an x86_64 machine), you need to ensure your system is set up for cross-compilation using QEMU. This allows your host machine to emulate ARM64 execution.

Run the following command on your host machine to register QEMU user static handlers:

    docker run --rm --privileged multiarch/qemu-user-static --reset -p yes

After setting up QEMU, you can use the `--platform "linux/arm64"` flag in your `docker build` command.

## Use the custom-built vLLM Docker image[¶](#use-the-custom-built-vllm-docker-image "Permanent link")

To run vLLM with the custom-built Docker image:

    docker run --runtime nvidia --gpus all \
        -v ~/.cache/huggingface:/root/.cache/huggingface \
        -p 8000:8000 \
        --env "HF_TOKEN=<secret>" \
        vllm/vllm-openai <args...>

The argument `vllm/vllm-openai` specifies the image to run, and should be replaced with the name of the custom-built image (the `-t` tag from the build command).

Note

**For version 0.4.1 and 0.4.2 only** - the vLLM docker images under these versions are supposed to be run under the root user since a library under the root user\'s home directory, i.e. `/root/.config/vllm/nccl/cu12/libnccl.so.2.18.1` is required to be loaded during runtime. If you are running the container under a different user, you may need to first change the permissions of the library (and all the parent directories) to allow the user to access it, then run vLLM with environment variable `VLLM_NCCL_SO_PATH=/root/.config/vllm/nccl/cu12/libnccl.so.2.18.1` .

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [December 13, 2025] ]