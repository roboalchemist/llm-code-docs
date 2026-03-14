# Source: https://novita.ai/docs/guides/gpu-instance-quickstart-create-instances.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Instances

## Step 1: Prepare Docker Image

You need to package your runtime environment into a Docker image and upload it to an image repository in advance. Currently, <a href="https://novita.ai">Novita AI</a> supports specifying both "public image repository" and "private image repository" (including access credentials).

Additionally, you can use the <a href="https://novita.ai/gpus-console/explore" target="_blank">public image templates</a> provided by the platform to quickly create instances.

## Step 2: Create GPU Instance

After entering the <a href="https://novita.ai/gpus-console/explore">Explore</a> page, select an image template and choose your desired specifications, then click the "Deploy" button.

<Tip>
  You can use the "Filter" feature in the bottom right corner to find the instance specifications you need.
</Tip>

## Configuration Explanation

| Configuration          | Description                                                                                                                                                                                                                                |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| CPU                    | The number of vCPU cores you select for your instance. The vCPU count will affect the instance's processing capability and performance, with more vCPUs being beneficial for compute-intensive applications.                               |
| Memory                 | The size of RAM in GB specified for each instance. Memory is crucial for running applications and overall instance speed.                                                                                                                  |
| Supported CUDA Version | CUDA is a parallel computing platform and API model developed by NVIDIA. Choosing the correct CUDA version is important if you plan to run applications optimized for NVIDIA GPUs, such as machine learning and 3D rendering applications. |
| Ports                  | You can expose your ports according to your service needs. The platform will provide port mapping services for your service. Multiple ports can be entered, separated by commas.                                                           |
| Environment Variables  | Used to specify parameters for the operating system's runtime environment. You can set environment variables here directly, and the platform will automatically initialize them for you.                                                   |
| GPU Instance Pricing   | More details can be found at [GPU Instance Pricing](/guides/gpu-instance-pricing).                                                                                                                                                         |
| Base Image             | The Docker image provided by the platform.                                                                                                                                                                                                 |
| Custom Image           | The Docker image name you specify, which the platform will default to pulling from DockerHub. Ensure that the image name is entered correctly.                                                                                             |

After the instance is successfully created, you can refer to the [Manage Instances](/guides/gpu-instance-quickstart-manage-instances) guide to access the instance.


Built with [Mintlify](https://mintlify.com).