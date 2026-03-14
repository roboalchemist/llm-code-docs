# Source: https://docs.edgeimpulse.com/tutorials/topics/lifecycle-management/ota-jetson-nano.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# NVIDIA Jetson

## Introduction

Welcome to the tutorial series on OTA Model Updates with Edge Impulse Docker Deploy on Jetson Nano! In this series, we will explore how to update machine learning models over-the-air (OTA) using Edge Impulse and Docker on the Jetson Nano platform.

## Prerequisites

Before getting started, make sure you have the following prerequisites:

* Jetson Nano Developer Kit
* Docker installed on Jetson Nano
* Edge Impulse account
* Be familiar with Edge Impulse and Docker deploy

## Overview

In this tutorial, we will explore how to enable GPU usage and use a camera with the Jetson Nano. We will then deploy a machine learning model using Edge Impulse and Docker on the Jetson Nano. Finally, we will update the model over-the-air (OTA) using Edge Impulse.

## Step 1: Enable GPU Usage on Jetson Nano

```bash  theme={"system"}
sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit
```

After installing the toolkit, restart the Docker service:

```bash  theme={"system"}

sudo systemctl restart docker
```

Now you can use the GPU for machine learning tasks in Docker containers.

## Step 2: Use a Camera with Jetson Nano

To use a camera with Jetson Nano, you need to install the libgstreamer and libv4l libraries. Run the following commands to install the libraries:

```bash  theme={"system"}

sudo apt-get update
sudo apt-get install -y libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav libgstrtspserver-1.0-0 libv4l-0 v4l-utils
```

After installing the libraries, you can use a camera with Jetson Nano.

## Step 3: Deploy Machine Learning Model with Edge Impulse and Docker

To deploy a machine learning model with Edge Impulse and Docker, follow these steps:

Export your model from Edge Impulse as a Docker container.
Copy the generated Docker command from the deployment section.
Modify the Docker command to use the GPU and camera on Jetson Nano.
Run the Docker command on Jetson Nano to deploy the model.

## Step 4: Update Model Over-the-Air (OTA) with Edge Impulse

To update the model over-the-air (OTA) with Edge Impulse, follow these steps:

Train a new model in Edge Impulse.
Export the new model as a Docker container.
Copy the generated Docker command from the deployment section and build a new Docker image.

````bash  theme={"system"}

docker build -t my_video_inference_container .
Modify the Docker command to use the GPU and camera on Jetson Nano.

```Dockerfile

FROM nvcr.io/nvidia/l4t-base:r32.5.0

RUN apt-get update && apt-get install -y \
    ffmpeg \
    v4l-utils \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV DISPLAY=:0
ENV QT_X11_NO_MITSHM=1

# Expose port for streaming
EXPOSE 80

# Mount USB camera device
RUN ln -s /dev/bus/usb/001/002 /dev/video0

# Command to run your model as a Docker container
CMD ["docker", "run", "--rm", "-it", \
    "-p", "80:80", \
    "public.ecr.aws/z9b3d4t5/inference-container:73d6ea64bf931f338de5183438915dc390120d5d", \
    "--api-key", "ei_07e1e4fad55f06b30839c062076a2ad4bbc174386330493011e75566405a5603", \
    "--run-http-server", "1337"]
````

5. Run the Docker command on Jetson Nano to deploy the new model.

docker run --rm -it --privileged --runtime nvidia -v /dev/bus/usb/001/002:/dev/video0 -p 80:80 public.ecr.aws/z9b3d4t5/inference-container:73d6ea64bf931f338de5183438915dc390120d5d --api-key ei\_07e1e4fad55f06b30839c062076a2ad4bbc174386330493011e75566405a5603 --run-http-server 1337

6. Test the new model on Jetson Nano.

7. Monitor the model performance and update as needed.

## Summary

In this tutorial series, we explored how to update machine learning models over-the-air (OTA) using Edge Impulse and Docker on the Jetson Nano platform. We enabled GPU usage, used a camera with Jetson Nano, deployed a machine learning model, and updated the model over-the-air.

Now you can easily update your machine learning models on Jetson Nano devices using Edge Impulse and Docker.


Built with [Mintlify](https://mintlify.com).