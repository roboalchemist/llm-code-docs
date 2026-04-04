# Source: https://docs.aws.amazon.com/pcs/latest/userguide/llms.txt

# AWS PCS User Guide

> AWS PCS is a managed service that makes it easier for you to run and scale your HPC workloads, and build scientific and engineering models on AWS using Slurm.

- [Network file systems](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_file-systems.html)
- [Supported operating systems](https://docs.aws.amazon.com/pcs/latest/userguide/operating-systems.html)
- [AWS PCS agent versions](https://docs.aws.amazon.com/pcs/latest/userguide/pcs-agent-versions.html)
- [Endpoints and service quotas](https://docs.aws.amazon.com/pcs/latest/userguide/service-endpoints-quotas.html)
- [Document history](https://docs.aws.amazon.com/pcs/latest/userguide/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/pcs/latest/userguide/glossary.html)

## [What is AWS PCS?](https://docs.aws.amazon.com/pcs/latest/userguide/what-is-service.html)

- [Concepts](https://docs.aws.amazon.com/pcs/latest/userguide/key-concepts.html): A cluster in AWS PCS has 1 or more queues, associated with at least 1 compute node group.


## [Get started with AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/getting-started.html)

### [Prerequisites](https://docs.aws.amazon.com/pcs/latest/userguide/getting-started_prerequisites.html)

Refer to the following topics to prepare your AWS account and local development environment for AWS PCS.

- [Sign up for AWS and create an administrative user](https://docs.aws.amazon.com/pcs/latest/userguide/setting-up.html): Complete the following tasks to set up for AWS Parallel Computing Service (AWS PCS).
- [Install the AWS CLI for AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/setting-up_cli.html): Learn how to make sure you have the right version of the AWS CLI for use with AWS PCS.
- [Required IAM permissions](https://docs.aws.amazon.com/pcs/latest/userguide/required-iam-permissions.html): The IAM security principal that you're using must have permissions to work with AWS PCS IAM roles, service linked roles, AWS CloudFormation, a VPC, and related resources.
- [Using CloudFormation](https://docs.aws.amazon.com/pcs/latest/userguide/getting-started_cfn-note.html): The AWS PCS tutorial has many steps and is intended to help you understand the parts of an AWS PCS cluster and the procedures required to create it.
- [Create a VPC and subnets](https://docs.aws.amazon.com/pcs/latest/userguide/getting-started_create-vpc.html): You can create a VPC and subnets with a CloudFormation template.
- [Create security groups](https://docs.aws.amazon.com/pcs/latest/userguide/getting-started_create-sg.html): AWS PCS relies on security groups to manage network traffic into and out of a cluster and its compute node groups.
- [Create a cluster](https://docs.aws.amazon.com/pcs/latest/userguide/getting-started_create-cluster.html): In AWS PCS, a cluster is a persistent resource for managing resources and running workloads.
- [Create shared storage in Amazon EFS](https://docs.aws.amazon.com/pcs/latest/userguide/getting-started_create-efs.html): Amazon Elastic File System (Amazon EFS) is an AWS service that provides serverless, fully elastic file storage so that you can share file data without provisioning or managing storage capacity and performance.
- [Create shared storage in FSx for Lustre](https://docs.aws.amazon.com/pcs/latest/userguide/getting-started_create-fsx.html): Amazon FSx for Lustre makes it easy and cost-effective to launch and run the popular, high-performance Lustre file system.

### [Create compute node groups](https://docs.aws.amazon.com/pcs/latest/userguide/getting-started_create-cng.html)

A compute node group is virtual collection of compute nodes (EC2 instances) that AWS PCS launches and manages.

- [Create an instance profile](https://docs.aws.amazon.com/pcs/latest/userguide/getting-started_create-cng_instance-profile.html): Compute node groups require an instance profile when they are created.
- [Create launch templates](https://docs.aws.amazon.com/pcs/latest/userguide/getting-started_create-cng_launch-templates.html): When you create a compute node group, you provide an EC2 launch template that AWS PCS uses to configure EC2 instances it launches.
- [Create compute node group for login nodes](https://docs.aws.amazon.com/pcs/latest/userguide/getting-started_create-cng_login-nodes.html): A compute node group is virtual collection of compute nodes (EC2 instances) that AWS PCS launches and manages.
- [Create compute node group for jobs](https://docs.aws.amazon.com/pcs/latest/userguide/getting-started_create-cng_workers.html): In this step, you will launch a compute node group that scales elastically to run jobs submitted to the cluster.
- [Create a queue](https://docs.aws.amazon.com/pcs/latest/userguide/getting-started_create-queue.html): You submit a job to a queue to run it.
- [Connect to your cluster](https://docs.aws.amazon.com/pcs/latest/userguide/getting-started_connect.html): After the status of the login compute node group becomes Active, you can connect to the EC2 instance it created.
- [Explore the cluster environment](https://docs.aws.amazon.com/pcs/latest/userguide/getting-started_explore.html): After you have logged into the cluster, you can run shell commands.
- [Run a single node job](https://docs.aws.amazon.com/pcs/latest/userguide/getting-started_run-job.html): To run a job using Slurm, you prepare a submission script specifying job requirements and submit it to a queue with the sbatch command.
- [Run a multi-node MPI job with Slurm](https://docs.aws.amazon.com/pcs/latest/userguide/getting-started_run-mpi-job.html): These instructions demonstrate using Slurm to run a message passing interface (MPI) job in AWS PCS.
- [Delete your AWS resources](https://docs.aws.amazon.com/pcs/latest/userguide/getting-started_delete.html): After you are done with the cluster and node groups that you created for this tutorial, you should delete the resources that you created.


## [Get started with CloudFormation and AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/get-started-cfn.html)

- [Use CloudFormation to create a cluster](https://docs.aws.amazon.com/pcs/latest/userguide/get-started-cfn-create.html): Follow step-by-step procedures to use CloudFormation to create a sample cluster.
- [Connect to a cluster](https://docs.aws.amazon.com/pcs/latest/userguide/get-started-cfn-connect.html): Learn how to get connection information to connect to a AWS PCS cluster created with CloudFormation.
- [Clean up a cluster](https://docs.aws.amazon.com/pcs/latest/userguide/get-started-cfn-cleanup.html): Learn how to clean up an AWS PCS cluster created with CloudFormation
- [Parts of a CloudFormation template for AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/get-started-cfn-template-parts.html): Learn about the parts of a CloudFormation template for AWS PCS, using the template to create a sample cluster.
- [Templates to create a sample cluster](https://docs.aws.amazon.com/pcs/latest/userguide/get-started-cfn-sample-templates.html): Find the CloudFormation templates to create a sample AWS PCS cluster, for all supported AWS Regions.


## [Clusters](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters.html)

- [Creating a cluster](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_create.html): Learn how to use AWS Parallel Computing Service to create a Slurm cluster on AWS for high-performance computing (HPC) workloads.

### [Updating a cluster](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_update.html)

Use the UpdateCluster API or console to update cluster configurations without rebuilding infrastructure.

- [Update cluster](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_update_procedure.html): Update cluster configurations that include scheduler settings, accounting configuration, and Slurm custom settings using the console or AWS CLI.
- [FAQ](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_update_faq.html): Answers to common questions about updating cluster configurations in AWS PCS.
- [Troubleshooting](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_update_troubleshooting.html): Identify and resolve common issues that occur when updating cluster configurations.
- [Deleting a cluster](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_delete.html): This topic provides an overview of how to delete an AWS PCS cluster.
- [Cluster size](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_size.html): AWS PCS provides highly available and secure clusters, while automating key tasks such as patching, node provisioning, and updates.

### [Cluster secrets](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_secrets.html)

As part of creating a cluster, AWS PCS creates a cluster secret that is required to connect to the job scheduler on the cluster.

- [Use AWS Secrets Manager to find the cluster secret](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_secrets_find_secrets-manager.html)
- [Use AWS PCS to find the cluster secret](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_secrets_find_pcs.html): You can use the AWS CLI to find the ARN for an AWS PCS cluster secret.
- [Get the Slurm cluster secret](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_secrets_get.html): You can use Secrets Manager to get the current base64-encoded version of a Slurm cluster secret The following example uses the AWS CLI.

### [Secret rotation](https://docs.aws.amazon.com/pcs/latest/userguide/cluster-secret-rotation.html)

Rotate cluster secrets to maintain security compliance and remediate potential security compromises.

- [Rotate secret](https://docs.aws.amazon.com/pcs/latest/userguide/cluster-secret-rotation-procedure.html): Rotate your cluster secret through AWS Secrets Manager to maintain security compliance.
- [FAQ](https://docs.aws.amazon.com/pcs/latest/userguide/cluster-secret-rotation-faq.html): Answers to common questions about cluster secret rotation in AWS PCS.
- [Troubleshooting](https://docs.aws.amazon.com/pcs/latest/userguide/cluster-secret-rotation-troubleshooting.html): Resolve common issues with cluster secret rotation.


## [Compute node groups](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_cng.html)

- [Creating a compute node group](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_cng_create.html): This topic provides an overview of available options and describes what to consider when you create a compute node group in AWS Parallel Computing Service (AWS PCS).
- [Updating a compute node group](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_cng_update.html): This topic provides an overview of available options and describes what to consider when you update an AWS PCS compute node group.
- [Deleting a compute node group](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_cng_delete.html): This topic provides an overview of available options and describes what to consider when you delete an compute node group in AWS PCS.
- [Get compute node group details](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_cng_get-details.html): Learn how to get details for an AWS PCS compute node group, such as its ID, ARN, and AMI ID.
- [Finding compute node group instances](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_compute-instances.html): Each AWS PCS compute node group can launch EC2 instances with shared configurations.


## [Using launch templates](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_launch-templates.html)

- [Overview](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_launch-templates_overview.html): There are over 30 parameters available you can include in an EC2 launch template, controlling many aspects of how instances are configured.
- [Create a basic launch template](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_launch-templates_create.html): You can create a launch template using the AWS Management Console or the AWS CLI.

### [Working with Amazon EC2 user data](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_ec2-user-data.html)

Learn how you can use EC2 user data to perform tasks for your AWS PCS compute node when it starts.

- [Example: Install software from a package repository](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_ec2-user-data_repo.html): Provide this script as the value of "userData" in your launch template.
- [Example: Run scripts from an S3 bucket](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_ec2-user-data_s3.html): Provide this script as the value of "userData" in your launch template.
- [Example: Set global environment variables](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_ec2-user-data_env.html): Provide this script as the value of "userData" in your launch template.

### [Example: Use an EFS file system as a shared home directory](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_ec2-user-data_efs.html)

Provide this script as the value of "userData" in your launch template.

- [Example: Enabling passwordless SSH](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_ec2-user-data_efs_ssh.html): You can build on the shared home directory example to implement SSH connections between cluster instances using SSH keys.

### [Capacity Reservations](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_capacity-reservations.html)

You can reserve Amazon EC2 capacity in a specific Availability Zone and for a specific duration using On-Demand Capacity Reservations or Amazon EC2 Capacity Blocks for ML to make sure that you have the necessary compute capacity available when you need it.

- [Using ODCRs with AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/capacity-reservations-odcr.html): Configure compute node groups to use On-Demand Capacity Reservations (ODCR) for guaranteed EC2 capacity in your AWS PCS clusters.

### [Capacity Blocks](https://docs.aws.amazon.com/pcs/latest/userguide/capacity-blocks.html)

Use Amazon EC2 Capacity Blocks for ML to reserve GPU-based accelerated computing instances for your AWS PCS clusters.

- [Configure a compute node group to use a Capacity Block](https://docs.aws.amazon.com/pcs/latest/userguide/capacity-blocks-configure-cng.html): Learn how to configure AWS PCS compute node groups to use an Amazon EC2 Capacity Blocks reservation.
- [FAQ for Capacity Blocks with AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/capacity-blocks-faq.html): Frequently asked questions about using Amazon EC2 Capacity Blocks with AWS PCS.
- [Useful launch template parameters](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_launch-templates_parameters.html): This section describes some launch template parameters that may be broadly useful with AWS PCS.


## [Queues](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_queues.html)

- [Creating a queue](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_queues_create.html): This topic provides an overview of available options and describes what to consider when you create a queue in AWS PCS.
- [Updating a queue](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_queues_update.html): This topic provides an overview of available options and describes what to consider when you update an AWS PCS queue.
- [Deleting a queue](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_queues_delete.html): This topic provides an overview of how to delete an queue in AWS PCS.


## [Login nodes](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_login-nodes.html)

- [Using a compute node group for login](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_login-nodes_compute-node-group-for-login.html): This topic provides an overview of suggested configuration options and describes what to consider when you use an AWS PCS compute node group to provide persistent, interactive access to your cluster.

### [Using standalone instances as login nodes](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_login-nodes_standalone.html)

You can set up independent EC2 instances to interact with an AWS PCS cluster's Slurm scheduler.

- [Step 1 â Retrieve the address and secret for the target AWS PCS cluster](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_login-nodes_standalone_get-addr.html): Retrieve details about the target AWS PCS cluster using the AWS CLI with the command that follows.
- [Step 2 â Launch an EC2 instance](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_login-nodes_standalone_launch.html)
- [Step 3 â Install Slurm on the instance](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_login-nodes_standalone_install-slurm.html): When the instance has launched and becomes active, connect to it using your preferred mechanism.
- [Step 4 â Retrieve and store the cluster secret](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_login-nodes_standalone_get-secret.html): These instructions require the AWS CLI.
- [Step 5 â Configure the connection to the AWS PCS cluster](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_login-nodes_standalone_configure-connection.html): To establish a connection to the AWS PCS cluster, launch sackd as a system service by following these steps.
- [Step 6 â (Optional) Test the connection](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_login-nodes_standalone_test.html): Confirm that the sackd service is running.

### [Connecting a standalone login node to multiple clusters](https://docs.aws.amazon.com/pcs/latest/userguide/multi-cluster-login-script.html)

Learn about an automated way to configure a single standalone login node to communicate with multiple AWS PCS clusters.

- [Prerequisites](https://docs.aws.amazon.com/pcs/latest/userguide/multi-cluster-login-script-prerequisites.html): Prerequisites and requirements for the AWS PCS multi-cluster login node configuration script.
- [Script code](https://docs.aws.amazon.com/pcs/latest/userguide/multi-cluster-login-script-code.html): The complete code for a script to configure AWS PCS multi-cluster login nodes.
- [Using the script](https://docs.aws.amazon.com/pcs/latest/userguide/multi-cluster-login-script-usage.html): How to run the AWS PCS multi-cluster login node configuration script and use the activation scripts it creates.


## [Networking](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_networking.html)

- [VPC and subnet requirements](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_networking_vpc-requirements.html): Requirements and further considerations when setting up an AWS Parallel Computing Service (AWS PCS) VPC and a subnet.
- [Creating a VPC](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_networking_create-vpc.html): Create a VPC for AWS PCS to launch resources into a virtual network.
- [Security groups](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_networking_sg.html): Security groups in Amazon EC2 act as virtual firewalls to control inbound and outbound traffic to instances.
- [Multiple network interfaces](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_networking_multi-nic.html): Some EC2 instances have multiple network cards.
- [Placement groups](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_networking_placement-groups.html): You can use a placement group to influence the placement of EC2 instances to suit the needs of the workload that runs on them.

### [Using Elastic Fabric Adapter (EFA)](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_networking_efa.html)

Elastic Fabric Adapter (EFA) is a high performance advanced networking interconnect from AWS that you can attach to your EC2 instance to accelerate High Performance Computing (HPC) and machine learning applications.

- [Identify EFA-enabled EC2 instances](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_networking_efa_identify-instances.html): To use EFA, all instance types that are allowed for an AWS PCS compute group must support EFA, and must have the same number of vCPUs (and GPUs if appropriate).
- [Create a security group to support EFA communications](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_networking_efa_create-sg.html)
- [(Optional) Create a placement group](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_networking_efa_create-placement-group.html): We recommended you launch all instances that use EFA in a cluster placement group to minimize the physical distance between them.
- [Create or update an EC2 launch template](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_networking_efa_create-lt.html): EFA network interfaces are set up in the EC2 launch template for an AWS PCS compute node group.
- [Create or update compute node groups for EFA](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_networking_efa_create-cng.html): Your AWS PCS compute node groups must contain instances that have the same number of vCPUs, processor architecture, and EFA support.
- [(Optional) Test EFA](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_networking_efa_test-efa.html): You can demonstrate EFA-enabled communication between two nodes in a compute node group by running the fi_pingpong program, which is included in the EFA software installation.
- [(Optional) Use a CloudFormation template to create an EFA-enabled launch template](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_networking_efa_create-lt-cfn.html): Because there are several dependencies to setting up EFA, a CloudFormation template has been provided that you can use to configure a compute node group.


## [Amazon Machine Images (AMIs)](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_ami.html)

- [Using sample AMIs](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_ami_samples.html): AWS provides sample AMIs that you can use as a starting point for working with AWS PCS.

### [Custom AMIs](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_ami_custom.html)

AWS PCS is designed to work with Amazon Machine Images (AMI) that you bring to the service.

- [Step 1 â Launch a temporary instance](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_ami_custom_launch-instance.html): Launch a temporary instance that you can use to install and configure the AWS PCS software and Slurm scheduler.
- [Step 2 â Install the AWS PCS agent](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_ami_custom_install-agent.html): Install the agent that configures the instances launched by AWS PCS for use with Slurm.
- [Step 3 â Install Slurm](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_ami_custom_install-slurm.html): Install a version of Slurm that is compatible with AWS PCS.
- [Step 4 â (Optional) Install additional drivers, libraries, and application software](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_ami_custom_install-software.html): Install additional drivers, libraries, and application software on the temporary instance.
- [Step 5 â Create an AMI compatible with AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_ami_custom_create-ami.html): After you have installed the required software components, you create an AMI that you can reuse to launch instances in AWS PCS compute node groups.
- [Step 6 â Use the custom AMI with an AWS PCS compute node group](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_ami_custom_use-ami.html): You can use your custom AMI with a new or existing AWS PCS compute node group.
- [Step 7 â Terminate the temporary instance](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_ami_custom_terminate-instance.html): After you have confirmed that your AMI works as intended with AWS PCS, you can terminate the temporary instance to stop incurring charges for it.
- [Installers to build AMIs](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_ami_installers.html): AWS provides a downloadable file that can install the AWS PCS software on an instance.
- [Release notes for AMIs](https://docs.aws.amazon.com/pcs/latest/userguide/ami-release-notes.html): AMIs for the latest supported major versions of the scheduler receive security updates and critical bug fixes.


## [Slurm](https://docs.aws.amazon.com/pcs/latest/userguide/slurm.html)

### [Slurm versions](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-versions.html)

SchedMD continually enhances Slurm with new capabilities, optimizations, and security patches.

- [Release notes](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-versions_release-notes.html): This topic describes important changes for each Slurm version currently supported in AWS PCS.
- [Frequently asked questions](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-versions_faq.html): AWS PCS maintains support for multiple Slurm versions.
- [Slurm accounting](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-accounting.html): Learn about AWS PCS support for Slurm's native accounting feature.

### [Slurm REST API](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-rest-api.html)

Use the Slurm REST API to programmatically interact with your AWS PCS cluster through HTTP requests instead of command-line tools.

- [Enable REST API](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-rest-api-enable.html): Enable the Slurm REST API on new clusters during creation or on existing compatible clusters.
- [REST API authentication](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-rest-api-authenticate.html): Generate JWT tokens and authenticate with the Slurm REST API using AWS PCS-provided signing keys.
- [Use REST API](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-rest-api-use.html): Submit jobs, monitor cluster status, and manage resources using the Slurm REST API.
- [REST API FAQ](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-rest-api-faq.html): Find answers to common questions about using the Slurm REST API in AWS PCS.

### [Slurm reboot](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-reboot.html)

Use Slurm's native reboot command to reboot compute nodes without triggering instance replacement.

- [Reboot a compute node](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-reboot-procedure.html): Use the scontrol reboot command to reboot compute nodes without instance replacement.
- [Cancel reboot](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-reboot-cancel.html): Cancel a pending reboot to avoid unnecessary downtime when the underlying issue has been resolved.
- [FAQ](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-reboot-faq.html): Answers to common questions about Slurm reboot support in AWS PCS.
- [Troubleshooting](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-reboot-troubleshooting.html): Identify, diagnose, and resolve problems with Slurm reboot operations.

### [Custom Slurm settings](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-custom-settings.html)

Use custom Slurm parameters to implement advanced scheduling policies, resource management, and job lifecycle controls across Cluster, Queue, and Compute Node Group resources.

- [Cluster settings](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-custom-settings-cluster.html): Reference table of supported custom Slurm settings for cluster resources.
- [Compute node group settings](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-custom-settings-cng.html): Reference table of supported custom Slurm settings for compute node group resources.
- [Queue settings](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-custom-settings-queue.html): Reference table of supported custom Slurm settings for queue resources.
- [Troubleshooting](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-custom-settings-troubleshooting.html): Troubleshoot errors related to custom Slurm settings in AWS PCS operations.

### [SPANK plugins](https://docs.aws.amazon.com/pcs/latest/userguide/spank.html)

Use SPANK (Slurm Plug-in Architecture for Node and job Kontrol) plugins to extend and modify Slurm's behavior during job launch and execution on AWS PCS clusters.

- [Install SPANK plugins](https://docs.aws.amazon.com/pcs/latest/userguide/spank_install.html): Follow the plugin's documentation to install SPANK plugins on your AMI.
- [Configure SPANK plugins](https://docs.aws.amazon.com/pcs/latest/userguide/spank_configure.html): By default, store configuration files in /etc/aws/pcs/scheduler/slurm-version/plugstack.conf.d/.
- [SPANK plugins FAQ](https://docs.aws.amazon.com/pcs/latest/userguide/spank_faq.html): This section addresses common questions about installing and configuring SPANK plugins on AWS PCS clusters.

### [Slurm CLI Filter Plugins](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-cli-filter-plugins.html)

Use Slurm CLI Filter Plugins to run custom Lua scripts that validate and modify job submission parameters before they reach the Slurm controller.

- [Configure CLI Filter Plugins](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-cli-filter-plugins-configure.html): Create a new AWS PCS cluster with CLI Filter Plugins turned on and deploy your Lua script to all cluster nodes.
- [Using Amazon S3 to deploy a CLI Filter Plugin script](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-cli-filter-plugins-deploy-s3.html): Deploy and update your CLI Filter Plugin script from S3 so you can modify job submission logic on a live cluster without rebuilding AMIs.
- [Translate a Job Submit plugin script](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-cli-filter-plugins-translate.html): Translate your existing Job Submit Plugin Lua script to CLI Filter Plugins so you can maintain the same job submission policies in AWS PCS.
- [FAQ](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-cli-filter-plugins-faq.html): Find answers to common questions about CLI Filter Plugins in AWS PCS.
- [Troubleshooting](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-cli-filter-plugins-troubleshooting.html): Resolve common issues with CLI Filter Plugin configuration and script execution.


## [Security](https://docs.aws.amazon.com/pcs/latest/userguide/security.html)

### [Data protection](https://docs.aws.amazon.com/pcs/latest/userguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in AWS PCS.

- [KMS key policy for encrypted EBS volumes](https://docs.aws.amazon.com/pcs/latest/userguide/security-key-policy-for-encrypted-volumes.html): AWS PCS uses service-linked roles to delegate permissions to other AWS services.
- [VPC interface endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/pcs/latest/userguide/vpc-interface-endpoints.html): You can use an AWS PrivateLink to create a private connection between your VPC and AWS Parallel Computing Service.

### [Identity and Access Management](https://docs.aws.amazon.com/pcs/latest/userguide/security-iam.html)

How to authenticate requests and manage access to your AWS PCS resources.

- [How AWS Parallel Computing Service works with IAM](https://docs.aws.amazon.com/pcs/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to AWS PCS, learn what IAM features are available to use with AWS PCS.
- [Identity-based policy examples](https://docs.aws.amazon.com/pcs/latest/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify AWS PCS resources.
- [AWS managed policies](https://docs.aws.amazon.com/pcs/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS PCS and recent changes to those policies.
- [Service-linked roles](https://docs.aws.amazon.com/pcs/latest/userguide/service-linked-roles.html): How AWS PCS uses service-linked roles to access to resources in your AWS account.
- [EC2 Spot role](https://docs.aws.amazon.com/pcs/latest/userguide/spot-role.html): If you want to create an AWS PCS compute node group that uses Spot as its purchase option, you must also have the AWSServiceRoleForEC2Spot service-linked role in your AWS account.
- [Minimum permissions](https://docs.aws.amazon.com/pcs/latest/userguide/security-min-permissions.html): This section describes the minimum IAM permissions required for an IAM identity (user, group, or role) to use the service.

### [Instance profiles](https://docs.aws.amazon.com/pcs/latest/userguide/security-instance-profiles.html)

Applications that run on an EC2 instance must include AWS credentials in any AWS API requests they make.

- [Create an instance profile](https://docs.aws.amazon.com/pcs/latest/userguide/security-instance-profiles_create.html)
- [Find instance profiles](https://docs.aws.amazon.com/pcs/latest/userguide/security-instance-profiles_find.html)
- [Troubleshooting](https://docs.aws.amazon.com/pcs/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS PCS and IAM.
- [Compliance validation](https://docs.aws.amazon.com/pcs/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/pcs/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS PCS features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/pcs/latest/userguide/infrastructure-security.html): Learn how AWS Parallel Computing Service isolates service traffic.
- [Vulnerability analysis and management](https://docs.aws.amazon.com/pcs/latest/userguide/vulnerability-analysis-and-management.html): Vulnerability analysis and management in AWS PCS
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/pcs/latest/userguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more privileged entity to perform the action.
- [Security best practices](https://docs.aws.amazon.com/pcs/latest/userguide/security-best-practices.html): Learn about security best practices for AWS Parallel Computing Service.


## [Logging and monitoring](https://docs.aws.amazon.com/pcs/latest/userguide/monitoring-overview.html)

- [Job completion logs](https://docs.aws.amazon.com/pcs/latest/userguide/monitoring_job-completion-logs.html): Learn how to use job completion logs in AWS Parallel Computing Service to get key details about your jobs when they complete, such as job ID, start/end times, resources used, and more.
- [Scheduler logs](https://docs.aws.amazon.com/pcs/latest/userguide/monitoring_scheduler-logs.html): You can configure AWS PCS to send detailed logging data from your cluster scheduler to Amazon CloudWatch Logs, Amazon Simple Storage Service (Amazon S3), and Amazon Data Firehose.

### [Monitoring with CloudWatch](https://docs.aws.amazon.com/pcs/latest/userguide/monitoring-cloudwatch.html)

Amazon CloudWatch provides monitoring of your AWS Parallel Computing Service (AWS PCS) cluster health and performance by collecting metrics from the cluster at intervals.

- [Monitoring metrics](https://docs.aws.amazon.com/pcs/latest/userguide/monitoring-cloudwatch_metrics.html): You can monitor AWS PCS cluster health using Amazon CloudWatch, which collects data from your cluster and turns it into near real-time metrics.
- [Monitoring instances](https://docs.aws.amazon.com/pcs/latest/userguide/monitoring-cloudwatch_instances.html): AWS PCS launches Amazon EC2 instances as needed to meet the scaling requirements defined in your PCS compute node groups.
- [CloudTrail logs](https://docs.aws.amazon.com/pcs/latest/userguide/logging-using-cloudtrail.html): Learn about logging AWS Parallel Computing Service with AWS CloudTrail.


## [Troubleshooting](https://docs.aws.amazon.com/pcs/latest/userguide/troubleshooting.html)

- [EC2 instance is terminated and replaced after reboot](https://docs.aws.amazon.com/pcs/latest/userguide/troubleshooting_instance-terminated-after-reboot.html): Learn why your EC2 instances are terminated and replaced in AWS Parallel Computing Service.
- [Troubleshoot compute node bootstrap and registration problems in AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/troubleshooting-compute-node-bootstrap.html): Learn how to diagnose and resolve common problems that occur when compute nodes fail to bootstrap or register with your AWS PCS cluster.
