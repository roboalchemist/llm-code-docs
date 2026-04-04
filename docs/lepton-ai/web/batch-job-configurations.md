# Source: https://docs.nvidia.com/dgx-cloud/lepton/features/batch-jobs/configurations

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



# Batch Job Configurations

Copy page

Learn how to configure your batch job in DGX Cloud Lepton.

When creating a batch job, you can configure the resource, container, and additional options.

## Resource

  * **Node Group** : Select one or more node groups to determine what resources this job can use.
  * **Priority** : Set the priority of the job. Defaults to Medium (4). If the specified node group has limited resources, you can set the priority accordingly to get higher-priority resource allocation.
  * **Resource shape** : The instance type that the job will run on. Select from a variety of CPU and GPU shapes. Refer to [Node Group Shapes](/dgx-cloud/lepton/features/nodes/resource-shape/) for more details.
  * **Nodes** : Defaults to no specific nodes, but you can specify the nodes you want to launch the job on.
  * **Can preempt lower priority workload** : Whether the job can preempt lower-priority workloads. Defaults to false.
  * **Can be preempted by higher priority workload** : Whether the job can be preempted by higher-priority workloads. Defaults to false.
  * **Workers** : The number of workers to launch for the job. Defaults to 1.



## Container

  * **Image** : The container image that will be used to create the job. You can choose from the default image lists or use your own custom image.
  * **Private image registry auth (optional)** : If you are using a private image, [specify the image registry authentication](/dgx-cloud/lepton/features/workspace/registry/).
  * **Run Command** : The command to run when the container starts.
  * **Container Ports** : The ports that the container will listen on. In this field, you can add multiple ports, and each port can be specified with a protocol (TCP, UDP, or SCTP) and a port number. ![ports](/dgx-cloud/lepton/_next/static/media/ports.48f36ecf.png)
  * **Log Collection** : Whether to collect the logs from the container. Follows the workspace-level setting by default.



## Advanced

  * **Environment Variables** : Environment variables are key-value pairs that are passed to the job. They are automatically set as environment variables in the job container, so the runtime can refer to them as needed. Refer to [this guide](/dgx-cloud/lepton/features/batch-jobs/predefined-env-vars/) for more details.

Your defined environment variables should not start with the name prefix `LEPTON_`, as this prefix is reserved for predefined environment variables. The following environment variables are predefined and will be available in the job:

    * `LEPTON_JOB_NAME`: The name of the job
    * `LEPTON_RESOURCE_ACCELERATOR_TYPE`: The resource accelerator type of the job

  * **Storage** : Mount storage for the job container. Refer to [this guide](/dgx-cloud/lepton/features/utilities/storage/) for more details.
  * **Shared Memory** : The size of the shared memory that will be allocated to the container. The default amount of shared memory is based on the memory of the resource shape. For example, an instance with one TiB of memory will have 100 GiB of shared memory. The mapping is defined by the table below:

Memory| Shared Memory  
---|---  
4 GiB| 2 GiB  
32 GiB| 16 GiB  
128 GiB| 32 GiB  
512 GiB| 64 GiB  
1 TiB| 100 GiB  
  
  * **Max replica failure retry** : Maximum number of times to retry a failed replica. Defaults to zero.
  * **Max job failure retry** : Maximum number of failure restarts of the entire job.
  * **Disable retry when program error occurs** : If enabled, the job will not be retried if a program error is detected in the logs.
  * **Archive time** : The time to keep the job's logs and artifacts after the job is completed. Defaults to 3 days.
  * **Visibility** : Specifies the visibility of the job. If set to private, only the creator can access the job. If set to public, all users in the workspace can access the job.



[Starter Kits on Dev Pods](/dgx-cloud/lepton/features/dev-pods/create-from-starter-kits/)[Environment Variables Reference](/dgx-cloud/lepton/features/batch-jobs/predefined-env-vars/)

Resource

Container

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
