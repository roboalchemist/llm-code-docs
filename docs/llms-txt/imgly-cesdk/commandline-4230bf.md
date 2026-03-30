# Source: https://img.ly/docs/cesdk/renderer/get-started/commandline-4230bf/

---
title: "Setup and Command-line Export"
description: "Getting started with CE.SDK Renderer"
platform: renderer
url: "https://img.ly/docs/cesdk/renderer/get-started/commandline-4230bf/"
---

> This is one page of the CE.SDK Renderer documentation. For a complete overview, see the [Renderer Documentation Index](https://img.ly/docs/cesdk/renderer.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/renderer/llms-full.txt).

**Navigation:** [Get Started](https://img.ly/docs/cesdk/renderer/get-started/overview-e18f40/) > [Server setup](https://img.ly/docs/cesdk/renderer/get-started/commandline-4230bf/)

---

This guide walks you through exporting sample **CreativeEditor SDK (CE.SDK)** scenes on **Linux using the CE.SDK Renderer Docker container**.

> **Reading time:** 5 minutes
>
> **Resources:**
>
> - [View source on GitHub](https://github.com/imgly/cesdk-renderer-examples/blob/$UBQ_VERSION$/simple/README.md)

## Who is This Guide For?

This guide is for developers who:

- Need to **perform image exporting programmatically** in a **Linux server environment**.
- Want to use an **NVIDIA GPU** for accelerating the export time of CE.SDK scenes and archives.

## What You'll Achieve

- Install and configure **Docker** and the **NVIDIA Container Runtime** for **Ubuntu Linux**.
- Fetch the **CE.SDK Renderer** container and learn how to configure scene exports.
- Export designs as **PNG images** and **MP4 videos** on the server.

> **Note:** Please note that there are special licensing requirements needed for patent
> coverage of H.264 and H.265 video codecs, using open-source H.264 codecs at
> your own risk is possible.

## Prerequisites

Before getting started, ensure you have a server or virtual machine running **Ubuntu 24.04 LTS**.
The server should preferably have a GPU, image exports are possible but significantly slower without GPU acceleration.
You can explore the full hardware requirements [here](https://img.ly/docs/cesdk/renderer/compatibility-139ef9/).

## Container variants

We offer four container variants which are useful in different deployment scenarios: open-source and licensed codec variants, each having a variant that bundles our default assets and one that does not.

The demos provided use open-source codecs to get you up and running quickly, but these codecs do not come with patent license coverage which is required for legal AAC, H.264 and H.265 encoding and decoding.
For production deployments, we offer [licensed codec](https://img.ly/docs/cesdk/renderer/get-started/commandline-4231be/) container variants, switching to them after your evaluation requires only authenticating with our private container registry and switching out the container image names in your deployment.

The other choice available to you is bundled assets vs assetless containers. `cesdk-renderer` containers that bundle the CDN assets in a local directory `/opt/cesdk-renderer/assets`, this allows for quicker exports as no CDN access is required, and gets you up and running quickly by having access to demo scenes for testing with simple commands.
If you have customized your assets tree with custom sources and want to build your own version of the container, or you want to access them over http(s), we offer `assetless` container versions that only bundle the core assets required to run the renderer, saving about 300 MB in container size.

## Step 1: Install the CE.SDK Renderer and see the available options

To fetch the current version of the CE.SDK Renderer, use the following command:

<Tabs syncKey="renderer-assetless">
  <TabItem label="Open-source codecs, bundled assets">
    ```bash
    sudo docker pull docker.io/imgly/cesdk-renderer:$UBQ_VERSION$
    ```
  </TabItem>

  <TabItem label="Open-source codecs, assetless">
    ```bash
    sudo docker pull docker.io/imgly/cesdk-renderer-assetless:$UBQ_VERSION$
    ```
  </TabItem>

  <TabItem label="Licensed codecs, bundled assets">
    ```bash
    sudo docker login container.img.ly -u "oauth" -p "YOUR-API-KEY"
    sudo docker pull container.img.ly/imgly/cesdk-renderer-avlicensed:$UBQ_VERSION$
    ```
  </TabItem>

  <TabItem label="Licensed codecs, assetless">
    ```bash
    sudo docker login container.img.ly -u "oauth" -p "YOUR-API-KEY"
    sudo docker pull container.img.ly/imgly/cesdk-renderer-avlicensed-assetless:$UBQ_VERSION$
    ```
  </TabItem>
</Tabs>

Then list the available command-line options by running the container with a `--help` flag:

<Tabs syncKey="renderer-assetless">
  <TabItem label="Open-source codecs, bundled assets">
    ```bash
    sudo docker run docker.io/imgly/cesdk-renderer:$UBQ_VERSION$ --help
    ```
  </TabItem>

  <TabItem label="Open-source codecs, assetless">
    ```bash
    sudo docker run docker.io/imgly/cesdk-renderer-assetless:$UBQ_VERSION$ --help
    ```
  </TabItem>

  <TabItem label="Licensed codecs, bundled assets">
    ```bash
    sudo docker run container.img.ly/imgly/cesdk-renderer-avlicensed:$UBQ_VERSION$ --help
    ```
  </TabItem>

  <TabItem label="Licensed codecs, assetless">
    ```bash
    sudo docker run container.img.ly/imgly/cesdk-renderer-avlicensed-assetless:$UBQ_VERSION$ --help
    ```
  </TabItem>
</Tabs>

You should get a list of available options:

```
Renders a CE.SDK scene or archive to an image or video file.

Environment variables:
- CESDK_LICENSE - the license to unlock the engine (present)

./cesdk_cli [OPTIONS]

OPTIONS:
  -h,     --help              Print this help message and exit
  -i,     --input design.scene|archive.zip  REQUIRED
                              Input file name
  -o,     --output FILE|DIR   Output file name, automatically generated based on the scene type
                              if not provided. If only a directory is specified, the generated
                              output file is placed there, otherwise it defaults to the input
                              directory.
  -T,     --output-mime-type MIME
                              Manually specify a MIME type of the output instead of relying on
                              extension-based detection, e.g. image/png, video/mp4, etc.
  -v,     --verbose           Verbose output
  -j,     --json-progress     JSON progress output to stdout
  -b,     --base-path DIR|URL [/opt/cesdk-renderer/assets]
                              Assets root directory path. This can be an absolute file path, a
                              path relative to the current working directory, or a URL pointing
                              to an assets server.
[... advanced options listed here ...]
```

## Step 2: Install the Docker and NVIDIA runtimes on the server

For production use, you will need to have a working container runtime and the NVIDIA Container Toolkit on the target server.

If you can already run `sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi` in the context of your target server and successfuly get information about the host GPU, you can skip this step.

<details>
  <summary>NVIDIA Container Toolkit setup on a bare metal server</summary>

  This step closely follows the official [NVIDIA guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) for installing the Container Toolkit.

  If you haven't installed a compatible container engine yet, we recommend installing the [Docker Engine](https://docs.docker.com/engine/install/) first.

  Run the following command to install the required packages and start the Docker daemon, you can skip the GPU runtime commands if only CPU rendering of images is needed:

  <Tabs syncKey="renderer-linux-variant">
    <TabItem label="Ubuntu / Debian">
      ```bash
      # Install GPU video decoding drivers
      sudo apt-get install -y vdpau-driver-all libvdpau-va-gl1

      # Install the NVIDIA container runtime
      curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
        && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
          sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
          sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list \
        && sudo apt-get update -y \
        && export NVIDIA_CONTAINER_TOOLKIT_VERSION=1.18.0-1 \
        && sudo apt-get install -y \
          nvidia-container-toolkit=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
          nvidia-container-toolkit-base=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
          libnvidia-container-tools=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
          libnvidia-container1=${NVIDIA_CONTAINER_TOOLKIT_VERSION}

      # Configure the GPU runtime for the Docker daemon
      sudo nvidia-ctk runtime configure --runtime=docker && sudo systemctl restart docker

      # Test if the GPU runtime was properly configured and can see the GPU hardware
      sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
      ```
    </TabItem>

    <TabItem label="RHEL / CentOS / Fedora">
      ```bash
      # Install GPU video decoding drivers and curl
      sudo dnf install -y libva-vdpau-driver libvdpau-va-gl curl

      # Install the NVIDIA container runtime
      curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \
        sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo \
        && export NVIDIA_CONTAINER_TOOLKIT_VERSION=1.18.0-1 \
        && sudo dnf install -y \
            nvidia-container-toolkit-${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
            nvidia-container-toolkit-base-${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
            libnvidia-container-tools-${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
            libnvidia-container1-${NVIDIA_CONTAINER_TOOLKIT_VERSION}

      # Configure the GPU runtime for the Docker daemon
      sudo nvidia-ctk runtime configure --runtime=docker && sudo systemctl restart docker

      # Test if the GPU runtime was properly configured and can see the GPU hardware
      sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
      ```
    </TabItem>

    <TabItem label="OpenSUSE / SLE">
      ```bash
      # Install GPU video decoding drivers
      sudo zypper install -y mesa-vdpau-drivers

      # Install the NVIDIA container runtime
      sudo zypper ar https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo \
       && export NVIDIA_CONTAINER_TOOLKIT_VERSION=1.18.0-1 \
       && sudo zypper --gpg-auto-import-keys install -y \
            nvidia-container-toolkit-${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
            nvidia-container-toolkit-base-${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
            libnvidia-container-tools-${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
            libnvidia-container1-${NVIDIA_CONTAINER_TOOLKIT_VERSION}

      # Configure the GPU runtime for the Docker daemon
      sudo nvidia-ctk runtime configure --runtime=docker && sudo systemctl restart docker

      # Test if the GPU runtime was properly configured and can see the GPU hardware
      sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
      ```
    </TabItem>
  </Tabs>
</details>

`nvidia-smi` run inside Docker should provide output similar to this:

```

+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.133.07             Driver Version: 570.133.07     CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA L4                      Off |   00000000:00:04.0 Off |                    0 |
| N/A   40C    P8             12W /   72W |       0MiB /  23034MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```

The next steps assume that your current user is not part of the `docker` group for security reasons, if you did add it then you can skip the `sudo` before `sudo docker` invocations.
However, this exposes you to the risk of enabling [full root access](https://docs.docker.com/engine/security/#docker-daemon-attack-surface) from a regular user account, so we do not recommend doing it in production systems.

## Step 3: Set up the project structure

Create the following file and directory structure:

```

/my-processor-project
  ├── .env
  ├── demo.sh
  ├── input/
  ├── output/
```

### Optional: .env (License key)

If you already have a license key, put it in the `.env` file for later usage by the container.
If you don't, you can skip this step and you'll get a watermarked output file.

```bash
CESDK_LICENSE=my.license.key
```

### demo.sh

The following shell script demonstrates how to directly run a one-off instance CE.SDK Renderer CLI via Docker:

<Tabs syncKey="renderer-assetless">
  <TabItem label="Open-source codecs, bundled assets">
    ```bash file=@cesdk_renderer_examples/simple/demo.sh
    #!/bin/bash
    set -euo pipefail

    # Load the license from the .env file if it exists (optional)
    if [[ -f .env ]]; then
      . .env
    fi

    # Set the CESDK_RENDERER_VERSION to the latest version if not explicitly overridden
    CESDK_RENDERER_VERSION=${CESDK_RENDERER_VERSION:-latest}

    # Create the input and output directories if missing and set permissions
    mkdir -p input output
    chmod 0777 input output

    # Run the renderer on one of the template scenes
    # Remove `--runtime=nvidia --gpus all` if running on a system without NVIDIA GPU.
    docker run --rm --runtime=nvidia --gpus all -it \
        -e "CESDK_LICENSE=${CESDK_LICENSE:-}" \
        -v "$(pwd)/output:/output" -v "$(pwd)/input:/input" \
        "docker.io/imgly/cesdk-renderer:${CESDK_RENDERER_VERSION}" \
        --input "${INPUT_FILE:-/opt/cesdk-renderer/assets/demo/v3/ly.img.template/templates/cesdk_postcard_1.scene}" \
        --output "${OUTPUT_FILE:-/output/}"
        "$@"
    ```
  </TabItem>

  <TabItem label="Open-source codecs, assetless">
    ```bash file=@cesdk_renderer_examples/simple/demo-assetless.sh
    #!/bin/bash
    set -euo pipefail

    # Load the license from the .env file if it exists (optional)
    if [[ -f .env ]]; then
      . .env
    fi

    # Set the CESDK_RENDERER_VERSION to the latest version if not explicitly overridden
    CESDK_RENDERER_VERSION=${CESDK_RENDERER_VERSION:-latest}

    # Create the input and output directories if missing and set permissions
    mkdir -p input output
    chmod 0777 input output

    # Run the renderer on one of the template scenes
    # Remove `--runtime=nvidia --gpus all` if running on a system without NVIDIA GPU.
    docker run --rm --runtime=nvidia --gpus all -it \
        -e "CESDK_LICENSE=${CESDK_LICENSE:-}" \
        -v "$(pwd)/output:/output" -v "$(pwd)/input:/input" \
        "docker.io/imgly/cesdk-renderer-assetless:${CESDK_RENDERER_VERSION}" \
        --input "${INPUT_FILE:?INPUT_FILE must be provided}" \
        --output "${OUTPUT_FILE:-/output/}"
        "$@"
    ```
  </TabItem>

  <TabItem label="Licensed codecs, bundled assets">
    ```bash file=@cesdk_renderer_examples/simple/demo-avlicensed.sh
    #!/bin/bash
    set -euo pipefail

    # Load the license from the .env file if it exists (required)
    if [[ -f .env ]]; then
      . .env
    fi

    # Set the CESDK_RENDERER_VERSION to the latest version if not explicitly overridden
    CESDK_RENDERER_VERSION=${CESDK_RENDERER_VERSION:-latest}

    # Create the input and output directories if missing and set permissions
    mkdir -p input output
    chmod 0777 input output

    # Run the renderer on one of the template scenes
    # Remove `--runtime=nvidia --gpus all` if running on a system without NVIDIA GPU.
    docker run --rm --runtime=nvidia --gpus all -it \
        -e "CESDK_LICENSE=${CESDK_LICENSE:?CESDK_LICENSE must be provided to use licensed codecs}" \
        -v "$(pwd)/output:/output" -v "$(pwd)/input:/input" \
        "container.img.ly/imgly/cesdk-renderer-avlicensed:${CESDK_RENDERER_VERSION}" \
        --input "${INPUT_FILE:-/opt/cesdk-renderer/assets/demo/v3/ly.img.template/templates/cesdk_postcard_1.scene}" \
        --output "${OUTPUT_FILE:-/output/}"
        "$@"
    ```
  </TabItem>

  <TabItem label="Licensed codecs, assetless">
    ```bash file=@cesdk_renderer_examples/simple/demo-avlicensed-assetless.sh
    #!/bin/bash
    set -euo pipefail

    # Load the license from the .env file if it exists (required)
    if [[ -f .env ]]; then
      . .env
    fi

    # Set the CESDK_RENDERER_VERSION to the latest version if not explicitly overridden
    CESDK_RENDERER_VERSION=${CESDK_RENDERER_VERSION:-latest}

    # Create the input and output directories if missing and set permissions
    mkdir -p input output
    chmod 0777 input output

    # Run the renderer on one of the template scenes
    # Remove `--runtime=nvidia --gpus all` if running on a system without NVIDIA GPU.
    docker run --rm --runtime=nvidia --gpus all -it \
        -e "CESDK_LICENSE=${CESDK_LICENSE:?CESDK_LICENSE must be provided to use licensed codecs}" \
        -v "$(pwd)/output:/output" -v "$(pwd)/input:/input" \
        "container.img.ly/imgly/cesdk-renderer-avlicensed-assetless:${CESDK_RENDERER_VERSION}" \
        --input "${INPUT_FILE:?INPUT_FILE must be provided}" \
        --output "${OUTPUT_FILE:-/output/}"
        "$@"
    ```
  </TabItem>
</Tabs>

## Step 4: Run the Script

Once everything is set up, run your script using:

```bash
./demo.sh
```

This will process the scene and generate an image file named **`output/postcard.jpg`** in your project directory:

![A postcard with text "Layout, text and photo editing. All in one" on the left and a red-tinted photo of a woman on the right](postcard.png)

> **Note:** We run the docker container via a `sudo` invocation, which might ask you for
> your user password. In a production deployment, the script starting the
> container should be given appropriate permissions to execute the processor
> without user interaction.

If you have your own scene files to test, copy them into the `input/` directory and export to various formats:

```bash
INPUT_FILE=/input/my-scene.scene OUTPUT_FILE=/output/my-scene.png ./demo.sh
INPUT_FILE=/input/my-scene.scene OUTPUT_FILE=/output/my-scene.jpg ./demo.sh
INPUT_FILE=/input/my-scene.scene OUTPUT_FILE=/output/my-scene.pdf ./demo.sh
INPUT_FILE=/input/my-archive.zip OUTPUT_FILE=/output/my-archive.png ./demo.sh
INPUT_FILE=/input/my-video.scene OUTPUT_FILE=/output/my-video.mp4 ./demo.sh
```

### Expected Output

When successful, you should see:

```

{"status":"loading","fractionComplete":0.0}
{"status":"exporting","fractionComplete":0.0}
{"status":"done","fractionComplete":1.0}
```

The `--json-output` flags will generate single-line JSON status reports periodically, these can be monitored on the process standard output to determine the progress of the export.

The default demo scene should output a `output/postcard.jpg` image.

## Troubleshooting & Common Errors

**❌ Error encountered while creating an EGL hardware-accelerated context, falling back to CPU rendering: EGL initialize error: UNKNOWN**

- Make sure the GPU setup instructions were followed, this error indicates that a hardware OpenGL context could not be created inside the container.
- When using `docker run`, ensure you're using **both** `--runtime=nvidia` and `--gpus all` flags together. Using only `--gpus all` without `--runtime=nvidia` can cause this error.
- This could also be expected if testing the container on a machine without a GPU.

**❌ Error: `Invalid license key`**

- Verify that your **license key** is correct and not expired, or remove the key entirely to get watermarked output.

## Next Steps

Congratulations! You've successfully exported a scene with the **CE.SDK Renderer** using **a simple shell script**. Next, explore:

- [Integrating with an Express.js web API](https://img.ly/docs/cesdk/renderer/get-started/expressjs-9f25eb/)
- [Integrating with CE.SDK for Node.js to combine programmatic scene
  manipulation with efficient exports](https://img.ly/docs/cesdk/renderer/get-started/node-processing-a2e4dc/)



---

## More Resources

- **[Renderer Documentation Index](https://img.ly/docs/cesdk/renderer.md)** - Browse all Renderer documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/renderer/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/renderer/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
