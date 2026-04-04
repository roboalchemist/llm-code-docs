# Source: https://docs.nvidia.com/dgx-cloud/lepton/get-started/batch-job

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



# Batch Job

Copy page

Learn about Batch Jobs on DGX Cloud Lepton.

A **Batch Job** is a one-off task that runs to completion, such as training a model or processing data. DGX Cloud Lepton provides a simple way to run and manage batch jobs in the cloud.

## Create Batch Job

Navigate to the [create job page](https://dashboard.dgxc-lepton.nvidia.com/workspace-redirect/compute/jobs/create).

In the **Resource** section, select the node group and your desired resource shape. For example, select `H100-80GB-HBM3` x 1 from node group `h100sxm-0`, and leave the worker and priority settings at their default values.

![create 0.75x](/dgx-cloud/lepton/_next/static/media/create.e4111fb5.png)

In the **Container** section, use the default image. In the **Run Command** field, specify the following command to run in the container:


By configuring the above settings, you can create a batch job that:

  * Uses one H100 GPU from node group `h100sxm-0`
  * Uses the default image and runs a simple counter that processes 10 items with a 2-second delay between each
  * Completes after approximately 20 seconds and is archived after 3 days



You need to have a [node group](/dgx-cloud/lepton/get-started/node-group/) with available nodes in your workspace first.

## View the Batch Job

After the job is created, you can check the status and results on the details page.

Click **Logs** under the **Replicas** tab to see the logs for each replica. Because the worker count is one, there will be only one replica, and the logs should display the following:


![logs](/dgx-cloud/lepton/_next/static/media/logs.f7d72907.png)

## Next Steps

For more information about batch jobs, refer to the following:

  * [Configure your Batch Job](/dgx-cloud/lepton/features/batch-jobs/configurations/)
  * [Job templates](/dgx-cloud/lepton/features/batch-jobs/templates/)
  * [Predefined environment variables](/dgx-cloud/lepton/features/batch-jobs/predefined-env-vars/)



[Dev Pod](/dgx-cloud/lepton/get-started/dev-pod/)[Node Group](/dgx-cloud/lepton/get-started/node-group/)

Create Batch Job

View the Batch Job

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
