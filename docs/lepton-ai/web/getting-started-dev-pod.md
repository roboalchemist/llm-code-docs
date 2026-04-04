# Source: https://docs.nvidia.com/dgx-cloud/lepton/get-started/dev-pod

Toggle Menu

Menu

[](/dgx-cloud/lepton/)

Get Started

  * [Introduction](/dgx-cloud/lepton/get-started/)
  * [Endpoint](/dgx-cloud/lepton/get-started/endpoint/)
  * [Dev Pod](/dgx-cloud/lepton/get-started/dev-pod/)
  * [Batch Job](/dgx-cloud/lepton/get-started/batch-job/)
  * [Node Group](/dgx-cloud/lepton/get-started/node-group/)
  * [Workspace](/dgx-cloud/lepton/get-started/workspace/)



Compute

  * Bring Your Own Compute



Features

  * Endpoints
  * Dev Pods
  * Batch Jobs
  * Nodes
  * Clusters
  * Utilities
  * Workspace



Examples

  * Batch Job
  * Connections
  * Dev Pod
  * Endpoint
  * Fine Tuning
  * Raycluster



Reference

  * CLI
  * [Python SDK Reference](/dgx-cloud/lepton/reference/api/)
  * Workload Identity
  * Limits
  * [Support](/dgx-cloud/lepton/reference/support/)



# Dev Pod

Copy page

Learn how to create and use a development pod on DGX Cloud Lepton.

For AI application developers, having a convenient development environment is essential for building and testing applications.

DGX Cloud Lepton provides a solution called **Dev Pods** âlightweight, container-based AI development environments.

There are two ways to launch a Dev Pod: start from a blank container image or launch a Starter Kit, which contains a predefined notebook following various AI tasks and workflows.

## Create a Dev Pod from a Container Image

Navigate to the [create pod page](https://dashboard.dgxc-lepton.nvidia.com/workspace-redirect/compute/pods/create/image) on the dashboard, where you can configure and launch a Dev Pod using a custom container image.

Enter a name, select a node group and machine type in the **Resource** section, then click **Create**. The Dev Pod starts shortly.

![create 0.75x](/dgx-cloud/lepton/_next/static/media/create.2f5b6352.png)

You need to have a [node group](/dgx-cloud/lepton/get-started/node-group/) with available nodes in the workspace first.

## Create from Notebooks

To launch a Dev Pod with a connected Jupyter session, go to the [Starter Kits page](https://dashboard.dgxc-lepton.nvidia.com/workspace-redirect/compute/pods/create/notebook/list) to view curated notebooks. Select a notebook to open a read-only preview. To run it, click **Create pod from this notebook** at the top of the page and complete the Dev Pod settings.

For more information on using Starter Kits, refer to the [Starter Kits on Dev Pods](/dgx-cloud/lepton/features/dev-pods/create-from-starter-kits/) guide.

## Access via Web Terminal

After creation, visit the details page to check the Dev Pod's status, connection information, metrics, and more.

Switch to the **Terminal** tab. DGX Cloud Lepton automatically establishes a connection to the Dev Pod, allowing you to control it through a full web terminal.

![details and web terminal 0.75x](/dgx-cloud/lepton/_next/static/media/details-and-web-terminal.7f5811ca.png)

## Next Steps

With these steps, you can launch a Dev Pod and start developing.

Refer to the following guides to learn more about Dev Pods:

  * [Configure your Dev Pod](/dgx-cloud/lepton/features/dev-pods/configurations/)
  * [Use SSH to access your Dev Pod](/dgx-cloud/lepton/features/dev-pods/create-from-container-image/ssh-access/)
  * [Enable JupyterLab in a Dev Pod](/dgx-cloud/lepton/features/dev-pods/create-from-container-image/enable-jupyter-lab/)
  * [Run NCCL test](/dgx-cloud/lepton/examples/dev-pod/nccl-test/)



[Endpoint](/dgx-cloud/lepton/get-started/endpoint/)[Batch Job](/dgx-cloud/lepton/get-started/batch-job/)

Create a Dev Pod from a Container Image

Create from Notebooks

Access via Web Terminal

Next Steps

[](/dgx-cloud/lepton/)

### Corporate Info

  * [Privacy Policy](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/)
  * [Manage My Privacy](https://www.nvidia.com/en-us/about-nvidia/privacy-center/)
  * [Terms of Service](https://www.nvidia.com/en-us/about-nvidia/terms-of-service/)
  * [Corporate Policies](https://www.nvidia.com/en-us/about-nvidia/company-policies/)



### NVIDIA Developer

  * [Developer Home](https://developer.nvidia.com/)
  * [Blog](https://blogs.nvidia.com/)



### Resources

  * [Contact Us](https://www.nvidia.com/en-us/contact/)
  * [Developer Program](https://developer.nvidia.com/developer-program)



Copyright @ 2025, NVIDIA Corporation.
