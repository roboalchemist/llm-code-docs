# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/device-manager.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/device-manager.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/device-manager.md

# Source: https://docs.roboflow.com/deploy/device-manager.md

# Deployment Manager

The Roboflow Deployment Manager provides everything you need to set up, deploy, and manage computer vision devices on the edge. Once you've trained your model and built a workflow for your computer vision application, Roboflow Deployment Manager is designed to give you a "batteries included" deployment option to manage deployment of vision models at scale.

You can use Deployment Manager to:

1. Set up new devices with the [Roboflow Inference server](https://inference.roboflow.com/).
2. Configure camera streams for use in a deployment.
3. Deploy [Workflows](https://docs.roboflow.com/workflows/what-is-workflows) on the edge.
4. Monitor logs, stream status, and telemetry for deployed edge devices.

In this section of the documentation, we will cover how to set up and use Deployment Manager with your hardware.

{% hint style="info" %}
Deployment Manager is available exclusively for Enterprise customers. [Contact the Roboflow sales team](https://roboflow.com/sales) to learn more about this feature and how it can be used to manage your deployments at scale.
{% endhint %}

### Key Requirements:

Deployment Manager was designed to work with hardware purchased via Roboflow. Deployment to alternative edge devices, like the NVIDIA Jetson or x86 machines running Debian-based Linux operating systems with NVIDIA GPUs, are at your own risk. We do not currently support managing Mac or Windows-based deployments with Deployment Manager.

Your device needs to be connected to the internet to install required tools and function. Your device will also need access to Roboflow at all times so you can manage and monitor your deployments remotely from the Roboflow web interface.
