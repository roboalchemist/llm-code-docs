# Source: https://docs.nvidia.com/dgx-cloud/lepton/reference/api

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



# Python SDK Reference

Copy page

Tutorial on using the Python SDK to interact with DGX Cloud Lepton

DGX Cloud Lepton supports the REST API protocol and includes a Python SDK for interacting with workspaces. Common tasks include monitoring and launching batch jobs and endpoints. This document provides an overview of how to interact with the Python SDK for DGX Cloud Lepton.

# Installation and authentication

First, install the Python SDK and authenticate with your workspace. Install the SDK with:


Next, authenticate with your workspace:


This prompts you to authenticate with your DGX Cloud Lepton workspace. If you're in a GUI-supported environment such as a desktop, a browser will open to the credentials page in your workspace. Otherwise, a URL will be displayed. Open this URL in a browser.

On the credentials page, create an authentication token by following the prompts. The page will display a secret token which is used for authentication. Copy the workspace ID and token shown in the second field and paste it back into your terminal. The format should look like `xxxxxx:**************************`. You should now be authenticated with DGX Cloud Lepton. You only need to authenticate once locally as long as your credentials remain valid.

## Validate installation

After authentication, validate the installation by running:


This lists your available workspaces and should look similar to the following if authentication was successful:


## Basic Python SDK flow

Nearly all workflows using the Python SDK follow the same basic flow:

  1. Initialize a client
  2. Define the task to perform
  3. Execute the task



The following sections break down these steps and provide a complete example.

## Initialize a client

Initializing the client is straightforwardâsimply import the Lepton API module and instantiate the client:


The `client` variable can be reused for multiple tasks.

## Define the task to perform

Most tasks available to users on DGX Cloud Lepton are supported via the SDK. The following API resources are accessible:

  1. Batch Jobs
  2. Dev Pods
  3. Endpoints
  4. Events
  5. Health Checks
  6. Ingress
  7. Logs
  8. Monitoring
  9. Node Groups
  10. Queue
  11. Readiness
  12. Replicas
  13. Secrets
  14. Templates
  15. Workspaces



Each of these resources has a specific template they expect for the API request. For example, the Batch Jobs API expects a job to have a `leptonai.api.v1.types.job.LeptonJob` type for submission. Similarly, Endpoints (also known as "Deployments" in the SDK), expect a `leptonai.api.v1.types.deployment.LeptonDeployment` object for submission, as do Dev Pods which are handled similarly to Endpoints by the backend. The list of API specs can be found [here](https://github.com/leptonai/leptonai/tree/main/leptonai/api/v1/types). Open the file for the specific task you need and review its specification.

All jobs require a Resource Shape to be specified. This tells the platform what resources should be allocated in the container, such as number and type of GPUs, CPU cores and memory, and local storage. To view available shapes, run `lep node resource-shape` in CLI version 0.26.4 or later. This returns a table of all available resource shapes in your node groups. The **Shapes** column shows the name of the shape. Use the desired name for the `resource_shape` field in the job specifications.

For a batch job, you need a `LeptonJob` object with a `LeptonJobUserSpec`. Review the `LeptonJobUserSpec` in the [Python script](https://github.com/leptonai/leptonai/blob/main/leptonai/api/v1/types/job.py#L22) for the list of settings which are required for launching a job. The following is a quick example of defining a batch job spec (this expands upon the previous code which instantiated the client):


The example above does the following:

  1. Imports all required modules
  2. Finds the ID of the specified node group - Update the listed node group for your specific needs
  3. Get the list of the node IDs for all nodes in your node group - this specifies which nodes the job can be scheduled on
  4. Specify the job spec - this includes defining the resource shape, container, command, and number of workers
  5. Define the job by passing the job spec and giving it a name



## Mounting shared storage

If shared storage is available in your node group, you can mount it in a job by pointing to the storage address and indicating which directory to mount from storage and where to mount it in the container.

To find your shared storage name, navigate to **Nodes** in the UI and select your desired node group. Next, click **Actions > Config > Storage** in the top-right corner of the page to list the available storage in the node group. If you have shared storage available, you should see something similar to the following image:

![shared-storage](/dgx-cloud/lepton/_next/static/media/shared-storage.c4493fbf.png)

As indicated in the image, `lepton-shared-fs` is the name of the shared storage which is mountable in containers.

With the storage name captured, we can define the mount specifications. To mount the volume, you will need to create a Python dictionary as follows:


More information on each value:

  * `path`: This is the directory from your shared storage to be mounted. Putting `/` will mount the root directory of the shared storage inside your container.
  * `mount_path`: This is the directory the `path` directory from storage will be mounted inside the container. Putting `/my-mount` will mount the `path` directory from storage at `/my-mount` inside the container. Note that this value cannot be `/`.
  * `from`: This is the name of the storage to mount. When using shared storage, you must first specify the storage type followed by a colon and your storage name. The storage type is very commonly `node-nfs`. Following the example above, this should be `node-nfs:lepton-shared-fs`.



You can also specify multiple mounts by making the dictionary above a list of dictionaries, similar to the following:


After defining your mount points, add them to a job template with the following syntax:


If you have a single dictionary and not a list, this would be:


## Authenticating with private container registries

If you are using a private container registry that requires authentication, you need to specify the private container secret in the job definition.

To create a new secret, navigate to the **Settings > Registries** page in the UI and click the green **\+ New registry auth** button in the top-right corner of the page. Follow the prompts to add your private image token.

To add your secret to the job specification, enter it in the `image_pull_secrets` field like below:


Note that `image_pull_secrets` expects a list of strings, allowing multiple secrets to be added.

## Running in a node reservation

If you have an existing node reservation for scheduling jobs on dedicated resources, you can add that to your request using the `node_reservation` field as follows:


## Execute the task

After the job has been defined in the previous step, it can be launched using the client. Since we are launching a job, we would use:


This adds the job to the queue and schedules it when resources become available. The job should appear in the UI after the `create` function runs.

# Example job submission via SDK

The following is a self-contained example of launching a batch job using the Python SDK following the flow outlined earlier.


Save the script above to a file such as `run.py` and launch it with:


Once the script completes, the launched job should be viewable in the UI.

[lep workspace](/dgx-cloud/lepton/reference/cli/lep_workspace/)[Workload Overview](/dgx-cloud/lepton/reference/workload-identity/1st-workload-identity/)

Installation and authentication

Validate installation

Basic Python SDK flow

Initialize a client

Define the task to perform

Mounting shared storage

Authenticating with private container registries

Running in a node reservation

Execute the task

Example job submission via SDK

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
