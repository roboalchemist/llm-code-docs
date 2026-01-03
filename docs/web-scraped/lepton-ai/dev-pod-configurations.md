# Source: https://docs.nvidia.com/dgx-cloud/lepton/features/dev-pods/configurations

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



# Dev Pod Configurations

Copy page

Learn how to configure your dev pod in Lepton.

When creating a dev pod, you can configure resources, the container, and other options.

## Resource

  * **Node Group** : First, select one or more node groups to determine which resources the pod can use.
  * **Priority** : Set the priority of the pod (defaults to Medium (4)). If the specified node group has limited resources, you can raise the priority to get higher priority allocation.
  * **Resource shape** : The instance type the pod will run on. Select from a variety of CPU and GPU shapes. Refer to [Node Group Shapes](/dgx-cloud/lepton/features/nodes/resource-shape/) for more details.
  * **Nodes** : No specific nodes are selected by default, but you can target particular nodes to launch the pod on.
  * **Can preempt lower priority workload** : Whether the pod can preempt lower-priority workloads (defaults to false).
  * **Can be preempted by higher priority workload** : Whether the pod can be preempted by higher-priority workloads (defaults to false).



## Container

  * **Image** : The container image used to create the pod. Choose from default images or use your own custom image.
  * **SSH Public Key** : The SSH public key used to access the pod. Available for **default images** with **Dev Pod entrypoint**. See [this guide](/dgx-cloud/lepton/features/dev-pods/create-from-container-image/ssh-access/) for details.
  * **Enable JupyterLab** : Whether to enable JupyterLab in the pod (defaults to false). Available for **default images** with **Dev Pod entrypoint**. See [this guide](/dgx-cloud/lepton/features/dev-pods/create-from-container-image/enable-jupyter-lab/) for details.
  * **Private image registry auth (optional)** : If you are using a private image, [specify image registry credentials](/dgx-cloud/lepton/features/workspace/registry/).
  * **Entrypoint (Run Command)** : Entrypoint of the Dev Pod container. Choose from:
    * **Dev Pod entrypoint** : Automatically applies a run command based on the selected image.
    * **Image default entrypoint** : Uses the image's default run command.
    * **Custom entrypoint** : Specify a custom entrypoint for the container. This overrides the default entrypoint.
  * **Run as** : When using a custom image, choose to run the container as root or the image's default user (defaults to image default user).
  * **Container Ports** : Ports to expose from the container (maximum of 3). See [this guide](/dgx-cloud/lepton/features/dev-pods/container-ports/) for details.
  * **Enable SSH Host Network** : Whether to enable SSH Host Network port configuration (defaults to false). Available for **default images** with **Dev Pod entrypoint**. See [this guide](/dgx-cloud/lepton/features/dev-pods/create-from-container-image/ssh-access/) for details.
  * **Enable JupyterLab Proxy** : Whether to enable JupyterLab Proxy port configuration (defaults to false). Available for **default images** with **Dev Pod entrypoint**. See [this guide](/dgx-cloud/lepton/features/dev-pods/create-from-container-image/enable-jupyter-lab/) for details.



## Storage

Mount storage for the pod container. See [this guide](/dgx-cloud/lepton/features/utilities/storage/) for details.

## Advanced

  * **Log Collection** : Whether to collect logs from the container (follows the workspace-level setting by default).
  * **Shared Memory** : The size of shared memory allocated to the container.
  * **Archive time** : How long to keep the job's logs and artifacts after completion (defaults to 3 days).
  * **Visibility** : If set to private, only the creator can access the job. If set to public, all users in the workspace can access the job.
  * **Environment Variables** : Keyâvalue pairs passed to the pod container for use at runtime.



[Create LLM Endpoints](/dgx-cloud/lepton/features/endpoints/create-llm/)[Container Ports](/dgx-cloud/lepton/features/dev-pods/container-ports/)

Resource

Container

Storage

Advanced

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
