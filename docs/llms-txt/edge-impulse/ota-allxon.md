# Source: https://docs.edgeimpulse.com/tutorials/topics/lifecycle-management/ota-allxon.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Allxon

[Allxon](https://www.allxon.com/) provides essential remote device management solutions to simplify and optimize edge AI device operations. As an AI/IoT ecosystem enabler, connecting hardware (IHV), software (ISV), and service providers (SI/MSP), Allxon serves as the catalyst for fast, seamless connectivity across all systems.

<Frame caption="Allxon - Device management">
  <img src="https://mintcdn.com/edgeimpulse/mgw9p71KrE70NXBr/.assets/images/allxon-devices.png?fit=max&auto=format&n=mgw9p71KrE70NXBr&q=85&s=c39e462316f1acff13d47f3634cc3243" width="1600" height="400" data-path=".assets/images/allxon-devices.png" />
</Frame>

Allxon Over-the-Air (OTA) deployment works perfectly with Edge Impulse OTA model update on [NVIDIA Jetson devices](https://www.allxon.com/jetson). This tutorial guides you through the steps to deploy a new impulse on multiple devices.

## Introduction

This guide demonstrates how to deploy and manage Edge Impulse models on NVIDIA Jetson devices using Allxon's Over-the-Air (OTA) deployment capabilities. Allxon provides essential remote device management solutions to streamline and optimize edge AI device operations.

## Prerequisites

Before you begin, ensure you have the following:

1. Updated impulse as a [Docker container](/hardware/deployments/run-docker) from Edge Impulse.
2. Get Allxon officially [supported devices](https://www.allxon.com/jetson)([https://www.allxon.com/](https://www.allxon.com/)).
3. Create an Allxon [account](https://dms.allxon.com/signup).

## Getting Started with Allxon

Allxon's services are compatible with a variety of hardware models. Follow these steps to complete the required preparations.

### Add a Device to Allxon Portal

1. **Install Allxon Agent**: Use the [command prompt](https://www.allxon.com/knowledge/install-allxon-agent-via-command-prompt) to install the Allxon Agent on your device.
2. **Pair Your Device**: Follow the instructions to [add your device to Allxon Portal](https://www.allxon.com/knowledge/add-your-device-on-allxon-dms-portal).

Once added, your devices will appear in the Allxon Portal for management and monitoring.

## Allxon OTA Deployment

To perform an OTA deployment, ensure you have your updated Impulse deployed as a [Docker container from Edge Impulse](/hardware/deployments/run-docker).

### Steps to Deploy

1. **Generate OTA Artifact**: Use the [Allxon CLI](https://www.allxon.com/knowledge/generate-allxon-ota-artifact-linux) to generate the OTA artifact.
2. **Deploy OTA Artifact**: Follow the [Deploy OTA Artifact](https://www.allxon.com/knowledge/deploy-ota-artifact) guide to complete the deployment.

### Example Scripts

Below are example scripts to help you set up the OTA deployment.

#### ota\_deploy.sh

```bash  theme={"system"}
#!/bin/bash
set -e
mkdir -p /opt/allxon/tmp/core/appies_ota/model_logs/
./install.sh > /opt/allxon/tmp/core/appies_ota/model_logs/log.txt 2>&1
echo "Model deployment has started. Please check /opt/allxon/tmp/core/appies_ota/model_logs/log.txt for progress."
```

#### install.sh

```bash  theme={"system"}

#!/bin/bash
docker run --rm --privileged --runtime nvidia \
 -v /dev/bus/usb/001/002:/dev/video0 \
 -p 80:80 \
 public.ecr.aws/z9b3d4t5/inferencecontainer:73d6ea64bf931f338de5183438915dc390120d5d \
 --api-key <replace with your project api key e.g. ei_07XXX > \
 --run-http-server 1337 &
```

Two minor modifications have been made to the standard Docker command from Edge Impulse docker deploy:

The `-it` option has been removed from the Docker command to avoid an error related to the lack of standard input during deployment.
An `&` has been added to the end of the Docker command to send the process to the background.

## Conclusion

By following these steps, you can efficiently deploy and manage Edge Impulse models on NVIDIA Jetson devices using Docker through Allxon. This setup leverages Allxon's remote management capabilities to streamline the process of updating and maintaining your edge AI devices.

We hope this section has helped you understand the process of Lifecycle Management and how to implement it in your own project. If you have any questions, please reach out to us on our [forum](https://forum.edgeimpulse.com/).


Built with [Mintlify](https://mintlify.com).