# Using SkyPilot to deploy a Kubernetes cluster -

Source: https://docs.lambda.ai/education/scheduling-and-orchestration/skypilot-deploy-kubernetes/

---

[api](../../../tags/#tag:api) [kubernetes](../../../tags/#tag:kubernetes)

# Using SkyPilot to deploy a Kubernetes cluster

## Introduction

[SkyPilot](https://skypilot.readthedocs.io/en/latest/docs/index.html) makes it easy to deploy a Kubernetes cluster using [Lambda Cloud](https://lambda.ai/service/gpu-cloud) on-demand instances. The [NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html) is preinstalled so you can immediately use your instances' GPUs.

In this tutorial, you'll:

- [Configure your Lambda Cloud firewall and a Cloud API key for SkyPilot and Kubernetes](#configure-your-lambda-cloud-firewall-and-generate-a-cloud-api-key).
- [Install SkyPilot](#install-skypilot).
- [Configure SkyPilot for Lambda Cloud](#configure-skypilot-for-lambda-cloud).
- [Use SkyPilot to launch 2 1x H100 on-demand instances and deploy a 2-node Kubernetes cluster using these instances](#use-skypilot-to-launch-instances-and-deploy-kubernetes).

Note

[**You're billed for all of the time the instances are running.**](../../../public-cloud/billing/#on-demand-cloud-odc-instances)
