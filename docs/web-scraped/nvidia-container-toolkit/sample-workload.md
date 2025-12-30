# Source: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/sample-workload.html

Running a Sample Workload &#8212; NVIDIA Container Toolkit

  - 

[Skip to main content](#main-content)

    **Back to top

  **
  *
  Ctrl+K

[

NVIDIA Container Toolkit

](index.html)

    Choose version  

  *
  **
  **

# Running a Sample Workload[#](#running-a-sample-workload)

## Running a Sample Workload with Docker[#](#running-a-sample-workload-with-docker)

After you install and configure the toolkit and install an NVIDIA GPU Driver,
you can verify your installation by running a sample workload.

Run a sample CUDA container:

sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi

Your output should resemble the following output:

+-----------------------------------------------------------------------------+
| NVIDIA-SMI 535.86.10    Driver Version: 535.86.10    CUDA Version: 12.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla T4            On   | 00000000:00:1E.0 Off |                    0 |
| N/A   34C    P8     9W /  70W |      0MiB / 15109MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+

## Running a Sample Workload with Podman[#](#running-a-sample-workload-with-podman)

After you install and configure the toolkit (including [generating a CDI specification](cdi-support.html)) and install an NVIDIA GPU Driver,
you can verify your installation by running a sample workload.

- 
Run a sample CUDA container:

podman run --rm --security-opt=label=disable \
   --device=nvidia.com/gpu=all \
   ubuntu nvidia-smi

Your output should resemble the following output:

+-----------------------------------------------------------------------------+
| NVIDIA-SMI 535.86.10    Driver Version: 535.86.10    CUDA Version: 12.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla T4            On   | 00000000:00:1E.0 Off |                    0 |
| N/A   34C    P8     9W /  70W |      0MiB / 15109MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+

## Running Sample Workloads with containerd or CRI-O[#](#running-sample-workloads-with-containerd-or-cri-o)

These runtimes are more common with Kubernetes than desktop computing.
Refer to [About the NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html) in the NVIDIA GPU Operator documentation for more information.

    ** On this page

   so the DOM is not blocked -->