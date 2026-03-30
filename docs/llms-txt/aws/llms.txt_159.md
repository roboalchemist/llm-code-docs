# Source: https://docs.aws.amazon.com/batch/latest/userguide/llms.txt

# AWS Batch User Guide

> AWS Batch makes it easier than ever to run batch computing workloads on the AWS Cloud. Batch computing is a common way for developers, scientists and engineers to access large amounts of compute resources, and AWS Batch removes the undifferentiated heavy lifting of configuring and managing the required infrastructure.

- [Elastic Fabric Adapter](https://docs.aws.amazon.com/batch/latest/userguide/efa.html)
- [Resource: Service quotas](https://docs.aws.amazon.com/batch/latest/userguide/service_limits.html)
- [Document history](https://docs.aws.amazon.com/batch/latest/userguide/document_history.html)

## [What is AWS Batch?](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html)

- [Components of AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/batch_components.html): Learn about AWS Batch components including jobs, job definitions, job queues, and compute environments for efficient batch computing across multiple Availability Zones.


## [Setting up AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/get-set-up-for-aws-batch.html)

- [Create IAM account and administrative user](https://docs.aws.amazon.com/batch/latest/userguide/create-an-iam-account.html): Create an AWS account and IAM administrative user to get started with AWS Batch services and resource management.
- [Create IAM roles](https://docs.aws.amazon.com/batch/latest/userguide/create-an-iam-role.html): Create IAM roles for AWS Batch compute environments and container instances to provide AWS API access credentials.
- [Create a key pair](https://docs.aws.amazon.com/batch/latest/userguide/create-a-key-pair.html): Create Amazon EC2 key pairs for secure SSH access to AWS Batch compute environment container instances using public-key cryptography.
- [Create a VPC](https://docs.aws.amazon.com/batch/latest/userguide/create-a-vpc.html): Create a Virtual Private Cloud (VPC) to launch AWS Batch container instances in a secure, isolated virtual network environment.
- [Create a security group](https://docs.aws.amazon.com/batch/latest/userguide/create-a-base-security-group.html): Create security groups for AWS Batch compute environment container instances to control inbound and outbound network traffic.
- [Install the AWS CLI](https://docs.aws.amazon.com/batch/latest/userguide/install_aws_cli.html): Install the latest AWS CLI version to use AWS Batch commands and manage batch computing resources from the command line.


## [Getting started tutorials](https://docs.aws.amazon.com/batch/latest/userguide/Batch_GetStarted.html)

- [Getting started with Amazon EC2 using the Wizard](https://docs.aws.amazon.com/batch/latest/userguide/getting-started-ec2.html): Learn how to create an Amazon EC2 orchestration type using the Wizard.
- [Getting started with Fargate orchestration using the Wizard](https://docs.aws.amazon.com/batch/latest/userguide/getting-started-fargate.html): Learn how to create a Fargate orchestration type and run Hello World.
- [Getting started with AWS Batch and Fargate using the AWS CLI](https://docs.aws.amazon.com/batch/latest/userguide/getting-started-with-fargate-using-the-aws-cli.html): Get started with AWS Batch on Fargate using the AWS CLI to create compute environments, job queues, and run your first Hello World job.
- [Getting started with Amazon EKS](https://docs.aws.amazon.com/batch/latest/userguide/getting-started-eks.html): Get started with AWS Batch on Amazon EKS to schedule and scale batch workloads in existing Amazon EKS clusters using managed orchestration.
- [Getting started with AWS Batch on Amazon EKS Private Clusters](https://docs.aws.amazon.com/batch/latest/userguide/getting-started-eks-privateclusters.html): Get started with AWS Batch on private Amazon EKS clusters to orchestrate batch workloads with queuing, dependency tracking, and managed scaling.
- [Getting started with AWS Batch on SageMaker AI](https://docs.aws.amazon.com/batch/latest/userguide/getting-started-sagemaker.html): This tutorial shows you how to run SageMaker Training jobs using AWS Batch service jobs.


## [The AWS Batch widget dashboard](https://docs.aws.amazon.com/batch/latest/userguide/custom-dashboard.html)

- [Add the Single job queue widget](https://docs.aws.amazon.com/batch/latest/userguide/single-job-queue.html): Discusses how to add the Single job queue widget to the AWS Batch dashboard.
- [How to add the CloudWatch Container Insights widget](https://docs.aws.amazon.com/batch/latest/userguide/container-insight.html): Discusses how to add the Container Insights widget to the AWS Batch dashboard.
- [Add the Job logs widget](https://docs.aws.amazon.com/batch/latest/userguide/job-logs.html): Discusses how to add the Job logs widget to the AWS Batch dashboard.


## [Compute environments for AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html)

- [Managed compute environments](https://docs.aws.amazon.com/batch/latest/userguide/managed_compute_environments.html): You can use a managed compute environment to have AWS Batch manage the capacity and instance types of the compute resources within the environment.
- [Unmanaged compute environments](https://docs.aws.amazon.com/batch/latest/userguide/unmanaged_compute_environments.html): In an unmanaged compute environment, you manage your own compute resources.

### [Create a compute environment](https://docs.aws.amazon.com/batch/latest/userguide/create-compute-environment.html)

Create AWS Batch compute environments with managed or unmanaged configurations for Amazon EC2 instances and Fargate resources.

- [Tutorial: Create a managed compute environment using Fargate resources](https://docs.aws.amazon.com/batch/latest/userguide/create-compute-environment-fargate.html): Complete the following steps to create a managed compute environment using AWS Fargate resources.
- [Tutorial: Create a managed compute environment using Amazon EC2 resources](https://docs.aws.amazon.com/batch/latest/userguide/create-compute-environment-managed-ec2.html): Complete the following steps to create a managed compute environment using Amazon Elastic Compute Cloud (Amazon EC2) resources.
- [Tutorial: Create an unmanaged compute environment using Amazon EC2 resources](https://docs.aws.amazon.com/batch/latest/userguide/create-compute-environment-unmanaged-ec2.html): Complete the following steps to create an unmanaged compute environment using Amazon Elastic Compute Cloud (Amazon EC2) resources.
- [Tutorial: Create a managed compute environment using Amazon EKS resources](https://docs.aws.amazon.com/batch/latest/userguide/create-compute-environment-managed-eks.html): Complete the following steps to create a managed compute environment using Amazon Elastic Kubernetes Service (Amazon EKS) resources.
- [Tutorial: Create an unmanaged compute environment using Amazon EKS resources](https://docs.aws.amazon.com/batch/latest/userguide/create-compute-environment-unmanaged-eks.html): Complete the following steps to create an unmanaged compute environment using Amazon Elastic Kubernetes Service (Amazon EKS) resources.
- [Resource: Compute environment template](https://docs.aws.amazon.com/batch/latest/userguide/compute-environment-template.html): Use compute environment templates to create AWS Batch compute environments with the AWS CLI using JSON configuration files.
- [Instance type compute table](https://docs.aws.amazon.com/batch/latest/userguide/instance-type-compute-table.html): The following table lists the AWS Region, instance family keyword, and available instance families.

### [Update a compute environment](https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html)

Learn about different strategies for updating compute environments in AWS Batch and when to use each approach.

- [Perform scaling updates](https://docs.aws.amazon.com/batch/latest/userguide/scaling-updates.html): Learn how to perform scaling updates to adjust the capacity of your AWS Batch compute environments.
- [Perform infrastructure updates](https://docs.aws.amazon.com/batch/latest/userguide/infrastructure-updates.html): Learn how to perform infrastructure updates to modify the configuration of your AWS Batch compute environments.
- [Perform Blue/green updates](https://docs.aws.amazon.com/batch/latest/userguide/blue-green-updates.html): Learn how to perform blue/green updates for AWS Batch compute environments to safely update AMIs with minimal disruption to your workloads.

### [Compute resource AMIs](https://docs.aws.amazon.com/batch/latest/userguide/compute_resource_AMIs.html)

Learn about AWS Batch compute resource AMIs, including default Amazon ECS optimized AMIs and when to create custom AMIs for specific requirements.

- [Compute resource AMI specification](https://docs.aws.amazon.com/batch/latest/userguide/batch-ami-spec.html): The basic AWS Batch compute resource AMI specification consists of the following:
- [Tutorial: Create a compute resource AMI](https://docs.aws.amazon.com/batch/latest/userguide/create-batch-ami.html): Tutorial on creating custom compute resource AMIs for AWS Batch managed and unmanaged compute environments, starting from a base AMI.
- [Use a GPU workload AMI](https://docs.aws.amazon.com/batch/latest/userguide/batch-gpu-ami.html): Configure GPU workload AMIs for AWS Batch compute resources to run GPU-enabled jobs using Amazon ECS GPU-optimized AMIs.
- [Amazon Linux deprecation](https://docs.aws.amazon.com/batch/latest/userguide/al1-ami-deprecation.html): The Amazon Linux AMI (also called Amazon Linux 1) reached its end of life on December 31, 2023.
- [Amazon EKS Amazon Linux 2 AMI deprecation](https://docs.aws.amazon.com/batch/latest/userguide/eks-al2-ami-deprecation.html): AWS will end support for Amazon EKS optimized Amazon Linux 2 AMIs, effective 11/26/25.
- [Amazon ECS Amazon Linux 2 AMI deprecation](https://docs.aws.amazon.com/batch/latest/userguide/ecs-al2-ami-deprecation.html): AWS will end support for Amazon Linux 2.

### [Use Amazon EC2 launch templates](https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html)

AWS Batch supports using Amazon EC2 launch templates with your EC2 compute environments.

- [Reference: Launch template examples](https://docs.aws.amazon.com/batch/latest/userguide/launch-template-examples.html): Examples of using Amazon EC2 launch templates with your EC2 compute environments.
- [Instance Metadata Service (IMDS) configuration](https://docs.aws.amazon.com/batch/latest/userguide/imds-compute-environments.html): Configure Instance Metadata Service Version 2 (IMDSv2) for enhanced security in your AWS Batch compute environments.

### [EC2 configurations](https://docs.aws.amazon.com/batch/latest/userguide/ec2-configurations.html)

Configure Amazon EC2 settings for AWS Batch compute environments using Amazon ECS optimized AMIs including Amazon Linux 2 and AL2023 options.

- [How to migrate from ECS AL2 to ECS AL2023](https://docs.aws.amazon.com/batch/latest/userguide/ecs-migration-2023.html): Upgrade AWS Batch on Amazon ECS compute environments from Amazon Linux 2 to Amazon Linux 2023 using different configuration methods.
- [Instance type allocation strategies](https://docs.aws.amazon.com/batch/latest/userguide/allocation-strategies.html): Configure instance type allocation strategies for AWS Batch managed compute environments to optimize cost and capacity selection.

### [Memory management](https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html)

Understand how AWS Batch manages memory allocation on compute resources, including platform overhead and available memory for job containers.

- [Reserve system memory](https://docs.aws.amazon.com/batch/latest/userguide/ecs-reserved-memory.html): Configure memory reservation for critical system processes in AWS Batch compute resources using the ECS_RESERVED_MEMORY configuration variable.
- [Tutorial: View compute resource memory](https://docs.aws.amazon.com/batch/latest/userguide/viewing-memory.html): Tutorial on viewing compute resource memory in AWS Batch using the Amazon ECS console to maximize resource utilization for job memory allocation.
- [Memory and vCPU considerations for AWS Batch on Amazon EKS](https://docs.aws.amazon.com/batch/latest/userguide/memory-cpu-batch-eks.html): Discusses limits and reservations for memory and vCPU resources in AWS Batch on Amazon EKS jobs.

### [Fargate compute environments](https://docs.aws.amazon.com/batch/latest/userguide/fargate.html)

AWS Fargate is a technology that you can use with AWS Batch to run containers without having to manage servers or clusters of Amazon EC2 instances.

- [When to use Fargate](https://docs.aws.amazon.com/batch/latest/userguide/when-to-use-fargate.html): We recommend using Fargate in most scenarios.
- [Job definitions on Fargate](https://docs.aws.amazon.com/batch/latest/userguide/fargate-job-definitions.html): AWS Batch jobs on AWS Fargate don't support all of the job definition parameters that are available.
- [Job queues on Fargate](https://docs.aws.amazon.com/batch/latest/userguide/fargate-job-queues.html): AWS Batch job queues on AWS Fargate are essentially unchanged.
- [Compute environments on Fargate](https://docs.aws.amazon.com/batch/latest/userguide/fargate-compute-environments.html): AWS Batch compute environments on AWS Fargate don't support all of the compute environment parameters that are available.

### [Amazon EKS compute environments](https://docs.aws.amazon.com/batch/latest/userguide/eks.html)

AWS Batch simplifies your batch workloads on Amazon EKS clusters by providing managed batch capabilities.

- [Amazon EKS default AMI](https://docs.aws.amazon.com/batch/latest/userguide/eks-ce-ami-selection.html): Understand how AWS Batch automatically selects Amazon EKS optimized AMIs for compute environments based on Kubernetes version and instance types.
- [Mixed AMI environments](https://docs.aws.amazon.com/batch/latest/userguide/mixed-ami-environments.html): Create AWS Batch compute environments with mixed AMI types using launch template overrides to support both Amazon Linux 2 and Amazon Linux 2023.
- [Supported Kubernetes versions](https://docs.aws.amazon.com/batch/latest/userguide/supported_kubernetes_version.html): View the currently supported Kubernetes versions for AWS Batch on Amazon EKS compute environments.
- [Update the Kubernetes version of the compute environment](https://docs.aws.amazon.com/batch/latest/userguide/updating-k8s-version-ce.html): Update the Kubernetes version of AWS Batch compute environments to support Amazon EKS cluster upgrades using the UpdateComputeEnvironment API.
- [Shared responsibility of the Kubernetes nodes](https://docs.aws.amazon.com/batch/latest/userguide/eks-ce-shared-responsibility.html): Understand the shared responsibility model for AWS Batch managed Kubernetes nodes and restrictions on node modifications and pod targeting.
- [Run a DaemonSet on AWS Batch managed nodes](https://docs.aws.amazon.com/batch/latest/userguide/daemonset-on-batch-eks-nodes.html): Configure DaemonSets to run on AWS Batch managed Kubernetes nodes using tolerations to handle node taints.
- [Customize Amazon EKS launch templates](https://docs.aws.amazon.com/batch/latest/userguide/eks-launch-templates.html): Customize Amazon EKS launch templates for AWS Batch on Amazon EKS compute environments with constraints and configuration requirements.
- [How to upgrade from EKS AL2 to EKS AL2023](https://docs.aws.amazon.com/batch/latest/userguide/eks-migration-2023.html): Upgrade AWS Batch on Amazon EKS compute environments from Amazon Linux 2 to Amazon Linux 2023 using different configuration methods.


## [Service environments](https://docs.aws.amazon.com/batch/latest/userguide/service-environments.html)

- [What are service environments](https://docs.aws.amazon.com/batch/latest/userguide/what-are-service-environments.html): Understand AWS Batch service environments and how they integrate with SageMaker Training jobs.

### [Service environment states and lifecycle](https://docs.aws.amazon.com/batch/latest/userguide/service-environment-states.html)

Discover the lifecycle states of AWS Batch service environments and how they impact SageMaker Training job processing.

- [Service environment state definitions](https://docs.aws.amazon.com/batch/latest/userguide/service-environment-state-definitions.html): Service environments can be in one of four possible states that indicate their current operational status and readiness to process SageMaker Training jobs.
- [Create a service environment](https://docs.aws.amazon.com/batch/latest/userguide/create-service-environments.html): Learn how to create AWS Batch service environments for SageMaker Training integration.
- [Update a service environment](https://docs.aws.amazon.com/batch/latest/userguide/updating-service-environments.html): Learn how to modifyAWS Batch service environments to adjust capacity limits, update operational state, or manage tags.
- [Delete a service environment](https://docs.aws.amazon.com/batch/latest/userguide/deleting-service-environments.html): Learn the proper procedures for safely deleting AWS Batch service environments when they're no longer needed.


## [Job queues](https://docs.aws.amazon.com/batch/latest/userguide/job_queues.html)

### [Create a job queue](https://docs.aws.amazon.com/batch/latest/userguide/create-job-queue.html)

Create AWS Batch job queues by associating compute environments and setting priorities to control job scheduling order.

- [Create an Amazon EC2 job queue](https://docs.aws.amazon.com/batch/latest/userguide/create-job-queue-ec2.html): Complete the following steps to create a job queue for Amazon Elastic Compute Cloud (Amazon EC2).
- [Create a Fargate job queue](https://docs.aws.amazon.com/batch/latest/userguide/create-job-queue-fargate.html): Complete the following steps to create a job queue for AWS Fargate.
- [Create an Amazon EKS job queue](https://docs.aws.amazon.com/batch/latest/userguide/create-job-queue-eks.html): Complete the following steps to create a job queue for Amazon Elastic Kubernetes Service (Amazon EKS).
- [Create a SageMaker job queue](https://docs.aws.amazon.com/batch/latest/userguide/create-sagemaker-job-queue.html): Learn how to create and configure an AWS Batch job queue for SageMaker Training jobs.
- [Job queue template](https://docs.aws.amazon.com/batch/latest/userguide/job-queue-template.html): The following is an empty job queue template.
- [View a job queue](https://docs.aws.amazon.com/batch/latest/userguide/job_queue_viewing_status.html): Monitor and view the status of AWS Batch job queues using the console to track job progress and manage queue operations.
- [Delete a job queue](https://docs.aws.amazon.com/batch/latest/userguide/delete-job-queue.html): Learn how to properly disable and delete AWS Batch job queues when they're no longer needed.

### [Fair-share scheduling policies](https://docs.aws.amazon.com/batch/latest/userguide/job_scheduling.html)

Discusses how to use share identifiers and fair-share scheduling to determine the order that AWS Batch jobs are run in.

- [Use share identifiers](https://docs.aws.amazon.com/batch/latest/userguide/share-identifiers.html): You can use share identifiers to tag jobs and differentiate between users and workloads.
- [Use scheduling policies](https://docs.aws.amazon.com/batch/latest/userguide/scheduling-policies.html): Discusses using scheduling policies to allocate resources in an AWS Batch job queue.
- [Use fair-share scheduling](https://docs.aws.amazon.com/batch/latest/userguide/fair-share-scheduling.html): Fair-share scheduling provides a set of controls to help schedule jobs.
- [Tutorial: Create a fair-share scheduling policy](https://docs.aws.amazon.com/batch/latest/userguide/create-scheduling-policy.html): Tutorial on creating fair-share scheduling policies for AWS Batch job queues with share identifiers, weights, and compute reservations.
- [Reference: Fair-share scheduling policy template](https://docs.aws.amazon.com/batch/latest/userguide/scheduling-policy-template.html): Reference template for creating AWS Batch fair-share scheduling policies using the AWS CLI with JSON configuration files and CreateSchedulingPolicy API.

### [Resource-aware scheduling](https://docs.aws.amazon.com/batch/latest/userguide/resource-aware-scheduling.html)

How to use resource-aware scheduling to run a job only when the consumable resources you define are available.

- [Create consumable resources](https://docs.aws.amazon.com/batch/latest/userguide/resource-aware-scheduling-how-to-create.html): You must first create the consumable resources that represent the non-CE resources that are consumed when a job is running and are only available in limited quantities.
- [Specify resources for a job](https://docs.aws.amazon.com/batch/latest/userguide/resource-aware-scheduling-how-to-for-jobs.html): When you register a job you can specify the name of one or more resources you created (consumableResource) and the quantity of that resource each instance of the job requires (quantity).
- [Check resource usage](https://docs.aws.amazon.com/batch/latest/userguide/resource-aware-scheduling-how-to-check-resources-check-resources.html): Batch lets you query the number of available resources (availableQuantity), the number of resources in use (inUseQuantity), and the total resources (totalQuantity) at a given moment.
- [Update in-use resource quantities](https://docs.aws.amazon.com/batch/latest/userguide/resource-aware-scheduling-how-to-update-quantity.html): You can reset the total quantity of a resource to a new value, add to the total quantity or subtract from it.
- [Find jobs requiring a consumable resource](https://docs.aws.amazon.com/batch/latest/userguide/resource-aware-scheduling-how-to-find-jobs.html): Batch lets you retrieve a list of jobs that require a specific consumable resource.
- [Delete a consumable resource](https://docs.aws.amazon.com/batch/latest/userguide/resource-aware-scheduling-how-to-delete.html): You can delete a consumable resource at any time, even when the jobs that require the resource are still running.


## [Job definitions](https://docs.aws.amazon.com/batch/latest/userguide/job_definitions.html)

### [Create a single-node job definition](https://docs.aws.amazon.com/batch/latest/userguide/create-job-definition.html)

Create single-node job definitions for AWS Batch jobs across different compute platforms including Amazon EC2, Fargate, and Amazon EKS.

- [Tutorial: Create a single-node job definition on Amazon EC2 resources](https://docs.aws.amazon.com/batch/latest/userguide/create-job-definition-EC2.html): Tutorial on creating single-node job definitions for AWS Batch jobs running on Amazon EC2 resources using the console.
- [Create a single-node job definition on Fargate resources](https://docs.aws.amazon.com/batch/latest/userguide/create-job-definition-Fargate.html): Tutorial on creating single-node job definitions for AWS Batch jobs running on Fargate resources using the console.
- [Create a single-node job definition on Amazon EKS resources](https://docs.aws.amazon.com/batch/latest/userguide/create-job-definition-eks.html): Tutorial on creating single-node job definitions for AWS Batch jobs running on Amazon EKS resources using the console.
- [Create a single-node job definition with multiple containers on Amazon EC2 resources](https://docs.aws.amazon.com/batch/latest/userguide/create-job-definition-single-node-multi-container.html): Tutorial on creating single-node job definitions with multiple containers for AWS Batch jobs running on Amazon EC2 resources.

### [Create a multi-node parallel job definition](https://docs.aws.amazon.com/batch/latest/userguide/create-multi-node-job-def.html)

Create job definitions for AWS Batch multi-node parallel jobs with gang scheduling to run distributed workloads across multiple compute resources.

- [Tutorial: Create a multi-node parallel job definition on Amazon EC2 resources](https://docs.aws.amazon.com/batch/latest/userguide/multi-node-job-def-ec2.html): To create a multi-node parallel job definition on Amazon Elastic Compute Cloud (Amazon EC2) resources.

### [Reference: Job definition template using ContainerProperties](https://docs.aws.amazon.com/batch/latest/userguide/job-definition-template.html)

Reference template for creating AWS Batch job definitions using ContainerProperties with the AWS CLI and JSON configuration files.

- [Job definition parameters for ContainerProperties](https://docs.aws.amazon.com/batch/latest/userguide/job_definition_parameters.html): Reference guide for job definition parameters when using ContainerProperties in AWS Batch job definitions across different compute platforms.

### [Create job definitions using EcsProperties](https://docs.aws.amazon.com/batch/latest/userguide/multi-container-jobs.html)

Create AWS Batch job definitions using EcsProperties to organize workload components in separate containers across Amazon ECS, Amazon EKS, and Fargate.

- [Reference: AWS Batch job scenarios using EcsProperties](https://docs.aws.amazon.com/batch/latest/userguide/multi-container-jobs-scenarios.html): Reference examples of AWS Batch job scenarios using EcsProperties with RegisterJobDefinition payloads for Amazon ECS, Amazon EKS, and Fargate platforms.
- [Use the awslogs log driver](https://docs.aws.amazon.com/batch/latest/userguide/using_awslogs.html): Configure the awslogs log driver in AWS Batch job definitions to send container logs to CloudWatch Logs for centralized logging and monitoring.

### [Specify sensitive data](https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html)

Inject sensitive data into AWS Batch jobs using Secrets Manager secrets or Systems Manager Parameter Store parameters as environment variables or log configuration.

- [Use Secrets Manager](https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data-secrets.html): Inject sensitive data into AWS Batch jobs by storing data in Secrets Manager secrets and referencing them in job definitions as environment variables.
- [Use Systems Manager Parameter Store](https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data-parameters.html): Inject sensitive data into AWS Batch containers by storing data in Systems Manager Parameter Store and referencing parameters in container definitions.

### [Private registry authentication for jobs](https://docs.aws.amazon.com/batch/latest/userguide/private-registry.html)

Configure private registry authentication for AWS Batch jobs using AWS Secrets Manager to securely store credentials and access container images from external registries.

- [Required IAM permissions for private registry authentication](https://docs.aws.amazon.com/batch/latest/userguide/private-auth-iam.html): The execution role is required to use this feature.
- [Tutorial: Create a secret for private registry authentication](https://docs.aws.amazon.com/batch/latest/userguide/private-auth-enable.html): Complete the following steps to create a secret for your private registry credentials with AWS Secrets Manager.
- [Amazon EFS volumes](https://docs.aws.amazon.com/batch/latest/userguide/efs-volumes.html): Use Amazon EFS volumes with AWS Batch jobs to provide scalable, persistent file storage across container instances in your compute environments.

### [Job definition examples](https://docs.aws.amazon.com/batch/latest/userguide/example-job-definitions.html)

Reference examples of AWS Batch job definitions demonstrating common patterns like environment variables, parameter substitution, and volume mounts.

- [Environment variables](https://docs.aws.amazon.com/batch/latest/userguide/example-use-envvars.html): The following example job definition uses environment variables to specify a file type and Amazon S3 URL.
- [Parameter substitution](https://docs.aws.amazon.com/batch/latest/userguide/example-use-parameters.html): The following example job definition illustrates how to allow for parameter substitution and to set default values.
- [Test GPU functionality](https://docs.aws.amazon.com/batch/latest/userguide/example-test-gpu.html): The following example job definition tests if the GPU workload AMI described in is configured properly.
- [Multi-node parallel job](https://docs.aws.amazon.com/batch/latest/userguide/example-mnp-job-definition.html): The following example job definition illustrates a multi-node parallel job.


## [Jobs](https://docs.aws.amazon.com/batch/latest/userguide/jobs.html)

- [Tutorial: submit a job](https://docs.aws.amazon.com/batch/latest/userguide/submit_job.html): Learn how to submit jobs to AWS Batch job queues using the console, including overriding job definition parameters at runtime.

### [Service jobs](https://docs.aws.amazon.com/batch/latest/userguide/service-jobs.html)

Explore AWS Batch service jobs for SageMaker Training jobs.

- [Service job payloads](https://docs.aws.amazon.com/batch/latest/userguide/service-job-payload.html): Learn how to structure AWS Batch service job payloads for SageMaker Training jobs.
- [Submit a service job](https://docs.aws.amazon.com/batch/latest/userguide/service-job-submit.html): Learn the process of submitting SageMaker Training jobs through AWS Batch.
- [Service job status](https://docs.aws.amazon.com/batch/latest/userguide/service-job-status.html): Understand how AWS Batch service job status values map to SageMaker Training job states.
- [Service job retry strategies](https://docs.aws.amazon.com/batch/latest/userguide/service-job-retries.html): Configure retry strategies for service jobs.
- [Monitor service jobs in the queue](https://docs.aws.amazon.com/batch/latest/userguide/monitor-sagemaker-job-queue.html): Monitor and track SageMaker Training jobs in AWS Batch queues using the AWS CLI.
- [Terminate service jobs](https://docs.aws.amazon.com/batch/latest/userguide/terminate-service-jobs.html): Use the TerminateServiceJob operation to stop a running service job.
- [Job states](https://docs.aws.amazon.com/batch/latest/userguide/job_states.html): Understand AWS Batch job states and lifecycle transitions from SUBMITTED through RUNNABLE to completion or failure.
- [Job environment variables](https://docs.aws.amazon.com/batch/latest/userguide/job_env_vars.html): Learn about environment variables that AWS Batch automatically sets in container jobs, including AWS_BATCH_ prefixed variables for job introspection.
- [Automated job retries](https://docs.aws.amazon.com/batch/latest/userguide/job_retries.html): Configure automated retry strategies for AWS Batch jobs to handle failures from container exits, instance termination, and service errors.
- [Job dependencies](https://docs.aws.amazon.com/batch/latest/userguide/job_dependencies.html): Configure job dependencies in AWS Batch to control job execution order and ensure jobs run only after their dependencies complete successfully.
- [Job timeouts](https://docs.aws.amazon.com/batch/latest/userguide/job_timeouts.html): Configure timeout duration for AWS Batch jobs using attemptDurationSeconds to automatically terminate long-running or stuck jobs.

### [Amazon EKS jobs](https://docs.aws.amazon.com/batch/latest/userguide/eks-jobs.html)

A job is the smallest unit of work in AWS Batch.

- [Tutorial: Map a running job to a pod and a node](https://docs.aws.amazon.com/batch/latest/userguide/eks-jobs-map-running-job.html): The podProperties of a running job have podName and nodeName parameters set for the current job attempt.
- [Tutorial: Map a running pod back to its job](https://docs.aws.amazon.com/batch/latest/userguide/eks-jobs-map-running-pod-to-job.html): A pod has labels that indicate the jobId and uuid of the compute environment that it belongs to.

### [Multi-node parallel jobs](https://docs.aws.amazon.com/batch/latest/userguide/multi-node-parallel-jobs.html)

Run large-scale, high-performance computing applications using AWS Batch multi-node parallel jobs that span multiple Amazon EC2 instances with gang scheduling.

- [Environment variables](https://docs.aws.amazon.com/batch/latest/userguide/mnp-env-vars.html): At runtime, each node is configured the standard environment variables that all AWS Batch jobs receive.
- [Node groups](https://docs.aws.amazon.com/batch/latest/userguide/mnp-node-groups.html): A node group is an identical group of job nodes that all share the same container properties.
- [Job lifecycle](https://docs.aws.amazon.com/batch/latest/userguide/job-lifecycle.html): When you submit a multi-node parallel job, the job enters the SUBMITTED status.
- [Compute environment considerations](https://docs.aws.amazon.com/batch/latest/userguide/mnp-ce.html): There are several things to consider when configuring compute environments to run multi-node parallel jobs with AWS Batch.

### [Multi-node parallel jobs on Amazon EKS](https://docs.aws.amazon.com/batch/latest/userguide/mnp-eks-jobs.html)

You can use AWS Batch on Amazon Elastic Kubernetes Service to run multi-node parallel (MNP) jobs on your managed Kubernetes clusters.

- [Running MNP jobs](https://docs.aws.amazon.com/batch/latest/userguide/mnp-eks-running-mnp-jobs.html): AWS Batch supports MNP jobs on Amazon Elastic Container Service and Amazon EKS using Amazon EC2.
- [Create an Amazon EKS MNP job definition](https://docs.aws.amazon.com/batch/latest/userguide/mnp-eks-create-eks-mnp-job-definition.html): To define and run MNP jobs on Amazon EKS, there are new parameters within the RegisterJobDefinition and SubmitJob API operations.
- [Submit an Amazon EKS MNP job](https://docs.aws.amazon.com/batch/latest/userguide/mnp-eks-submit-eks-mnp-job.html): To submit a job using the registered job definition, enter the following command.
- [Override an Amazon EKS MNP job definition](https://docs.aws.amazon.com/batch/latest/userguide/mnp-eks-override-eks-mnp-job-definition.html): Optionally, you can override the job definition details (such as changing the MNP job size or child job details).

### [Array jobs](https://docs.aws.amazon.com/batch/latest/userguide/array_jobs.html)

Submit and manage array jobs in AWS Batch for parallel processing of large workloads such as Monte Carlo simulations and parametric sweeps.

- [Example of an array job workflow](https://docs.aws.amazon.com/batch/latest/userguide/example_array_job.html): Reference example of an array job workflow in AWS Batch showing setup, parallel processing, and aggregation phases with job dependencies.

### [Using array job index](https://docs.aws.amazon.com/batch/latest/userguide/array_index_example.html)

Tutorial on using the AWS_BATCH_JOB_ARRAY_INDEX environment variable to differentiate child jobs in AWS Batch array jobs.

- [Prerequisites](https://docs.aws.amazon.com/batch/latest/userguide/array-tutorial-prereqs.html): This tutorial workflow has the following prerequisites:
- [Build a container image](https://docs.aws.amazon.com/batch/latest/userguide/build-index-container.html): You can use the AWS_BATCH_JOB_ARRAY_INDEX in a job definition in the command parameter.
- [Push your image to Amazon ECR](https://docs.aws.amazon.com/batch/latest/userguide/push-array-image.html): Now that you built and tested your Docker container, push it to an image repository.
- [Create and register a job definition](https://docs.aws.amazon.com/batch/latest/userguide/create-array-job-def.html): Now that your Docker image is in an image registry, you can specify it in an AWS Batch job definition.
- [Submit an AWS Batch array job](https://docs.aws.amazon.com/batch/latest/userguide/submit-array-job.html): After you registered your job definition, you can submit an AWS Batch array job that uses your new container image.

### [Run GPU jobs](https://docs.aws.amazon.com/batch/latest/userguide/gpu-jobs.html)

Run GPU-enabled jobs in AWS Batch using GPU-based Amazon EC2 instance types for compute-intensive workloads requiring graphics processing.

- [Create a GPU-based Kubernetes cluster on Amazon EKS](https://docs.aws.amazon.com/batch/latest/userguide/create-gpu-cluster-eks.html): This section covers how to run an Amazon EKS GPU workload on AWS Batch.
- [Create an Amazon EKS GPU job definition](https://docs.aws.amazon.com/batch/latest/userguide/create-eks-gpu-job-definition.html): Only nvidia.com/gpu is supported at this time and resource value that you set must be a whole number.
- [Run a GPU job in your Amazon EKS cluster](https://docs.aws.amazon.com/batch/latest/userguide/run-gpu-job-eks-cluster.html): The GPU resource is non-compressible.
- [View jobs in a job queue](https://docs.aws.amazon.com/batch/latest/userguide/view-jobs.html): View a job queue to find jobs status.
- [Search for jobs in a job queue](https://docs.aws.amazon.com/batch/latest/userguide/searching-filtering-jobs.html): Use in AWS Batch to find jobs in a job queue.
- [Networking modes for AWS Batch jobs](https://docs.aws.amazon.com/batch/latest/userguide/networking-modes-jobs.html): Use in AWS Batch to find jobs in a job queue.
- [View job logs in CloudWatch Logs](https://docs.aws.amazon.com/batch/latest/userguide/review-job-logs.html): Use Job logs to monitor or troubleshoot an AWS Batch job.
- [Review AWS Batch job information](https://docs.aws.amazon.com/batch/latest/userguide/review-job-info.html): Review AWS Batch job information and details


## [Security in AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/security.html)

### [Identity and Access Management](https://docs.aws.amazon.com/batch/latest/userguide/security-iam.html)

How to authenticate requests and manage access your AWS Batch resources.

- [How AWS Batch works with IAM](https://docs.aws.amazon.com/batch/latest/userguide/security_iam_service-with-iam.html): Understand how AWS Batch integrates with IAM for authentication, authorization, and access control using policies, roles, and permissions.
- [Identity-based policy examples](https://docs.aws.amazon.com/batch/latest/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify AWS Batch resources.
- [AWS managed policies](https://docs.aws.amazon.com/batch/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS Batch and recent changes to those policies.

### [IAM policies, roles, and permissions](https://docs.aws.amazon.com/batch/latest/userguide/IAM_policies.html)

Control which AWS Batch resources can be viewed, created, and modified by users.

- [IAM policy structure](https://docs.aws.amazon.com/batch/latest/userguide/iam-policy-structure.html): Learn about the structure of an IAM policy for controlling access to AWS Batch.

### [Resource: Example policies](https://docs.aws.amazon.com/batch/latest/userguide/ExamplePolicies_BATCH.html)

Learn to create policy statements to control the permissions that users have for AWS Batch.

- [Read-only access](https://docs.aws.amazon.com/batch/latest/userguide/iam-example-read-only.html): The following policy grants users permissions to use all AWS Batch API actions with a name that starts with Describe and List.
- [Resource: Restrict user, image, privilege, role](https://docs.aws.amazon.com/batch/latest/userguide/iam-example-job-def.html): The following policy allows a POSIX user to manage their own set of restricted job definitions.
- [Restrict job submission](https://docs.aws.amazon.com/batch/latest/userguide/iam-example-restrict-job-submission.html): Use the following policy to submit jobs to any job queue with any job definition name that starts with JobDefA.
- [Restrict to a job queue](https://docs.aws.amazon.com/batch/latest/userguide/iam-example-restrict-job-queue.html): Use the following policy to submit jobs to a specific job queue that's named queue1 with any job definition name.
- [Deny action when all conditions match strings](https://docs.aws.amazon.com/batch/latest/userguide/iam-example-job-def-deny-all-image-logdriver.html): The following policy denies access to the RegisterJobDefinition API operation when both the batch:Image (container image ID) condition key is "string1" and the batch:LogDriver (container log driver) condition key is "string2." AWS Batch evaluates condition keys on each container.
- [Resource: Deny action when any condition keys match strings](https://docs.aws.amazon.com/batch/latest/userguide/iam-example-job-def-deny-any-image-logdriver.html): The following policy denies access to the RegisterJobDefinition API operation when either the batch:Image (container image ID) condition key is "string1" or the batch:LogDriver (container log driver) condition key is "string2." When a job spans multiple containers such as a multi-node parallel job, it's possible for the containers to have different configurations.
- [Use the batch:ShareIdentifier condition key](https://docs.aws.amazon.com/batch/latest/userguide/iam-example-share-identifier.html): Use the following policy to submit jobs that use the jobDefA job definition to the jobqueue1 job queue with the lowCpu share identifier.
- [Manage SageMaker AI resources with AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/iam-example-full-access-service-environment.html): This policy allows AWS Batch to manage SageMaker AI resources.
- [Restrict job submission by resource tags](https://docs.aws.amazon.com/batch/latest/userguide/iam-example-restrict-job-submission-by-tags.html): Use the following policy to submit jobs only when both the job queue has the tag Environment=dev and the job definition has the tag Project=calc.
- [Resource: AWS Batch managed policy](https://docs.aws.amazon.com/batch/latest/userguide/batch_managed_policies.html): Use AWS managed policies for AWS Batch to provide predefined permissions for users, or as starting points for custom policies.

### [AWS Batch IAM execution role](https://docs.aws.amazon.com/batch/latest/userguide/execution-IAM-role.html)

Discusses how to verify or create an IAM execution role for AWS Batch.

- [Supported resource-level permissions](https://docs.aws.amazon.com/batch/latest/userguide/batch-supported-iam-actions-resources.html): Learn about the AWS Batch API actions that currently support resource-level permissions.
- [Tutorial: Create the IAM execution role](https://docs.aws.amazon.com/batch/latest/userguide/create-execution-role.html): If your account doesn't already have an IAM execution role, use the following steps to create the role.
- [Tutorial: Check the IAM execution role](https://docs.aws.amazon.com/batch/latest/userguide/check-execution-role.html): Use the following procedure to check that your account already has the IAM execution role and attach the managed IAM policy, if needed.

### [Using service-linked roles](https://docs.aws.amazon.com/batch/latest/userguide/using-service-linked-roles.html)

How to use service-linked roles to give AWS Batch access to resources in your AWS account.

- [Compute Environment integration role](https://docs.aws.amazon.com/batch/latest/userguide/using-service-linked-roles-batch-general.html): How to use service-linked roles to give AWS Batch access to resources in your AWS account.
- [SageMaker integration role](https://docs.aws.amazon.com/batch/latest/userguide/using-service-linked-roles-batch-sagemaker.html): How to use service-linked roles to give AWS Batch access to resources in your AWS account.

### [Amazon ECS instance role](https://docs.aws.amazon.com/batch/latest/userguide/instance_IAM_role.html)

Configure Amazon ECS instance roles for AWS Batch compute environment container instances to enable Amazon ECS container agent AWS API access.

- [Check your instance role](https://docs.aws.amazon.com/batch/latest/userguide/batch-check-ecsinstancerole.html): The Amazon ECS instance role and instance profile are automatically created for you in the console first-run experience.

### [Amazon EC2 spot fleet role](https://docs.aws.amazon.com/batch/latest/userguide/spot_fleet_IAM_role.html)

Create the AmazonEC2SpotFleetTaggingRole and service-linked roles required for AWS Batch managed compute environments using Amazon EC2 Spot Fleet instances.

- [Create Amazon EC2 spot fleet roles in the AWS Management Console](https://docs.aws.amazon.com/batch/latest/userguide/spot-fleet-roles-console.html)
- [Create Amazon EC2 spot fleet roles with the AWS CLI](https://docs.aws.amazon.com/batch/latest/userguide/spot-fleet-roles-cli.html)
- [EventBridge IAM role](https://docs.aws.amazon.com/batch/latest/userguide/CWE_IAM_role.html): Configure EventBridge IAM roles to enable EventBridge to submit AWS Batch jobs on your behalf using event-driven rules and targets.
- [Create a virtual private cloud](https://docs.aws.amazon.com/batch/latest/userguide/create-public-private-vpc.html): Create a VPC with both public and private subnets for AWS Batch compute environments to provide flexible network access options.

### [VPC endpoints](https://docs.aws.amazon.com/batch/latest/userguide/vpc-interface-endpoints.html)

You can use an AWS PrivateLink to create a private connection between your VPC and AWS Batch.

- [Considerations](https://docs.aws.amazon.com/batch/latest/userguide/vpc-endpoint-considerations.html): Before you set up an interface endpoint for AWS Batch, review Interface endpoint properties and limitations in the AWS PrivateLink Guide.
- [Create an interface endpoint](https://docs.aws.amazon.com/batch/latest/userguide/vpc-endpoint-create.html): You can create an interface endpoint for AWS Batch using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI).
- [Create an endpoint policy](https://docs.aws.amazon.com/batch/latest/userguide/vpc-endpoint-policy.html): An endpoint policy is an IAM resource that you can attach to an interface endpoint.
- [Compliance validation](https://docs.aws.amazon.com/batch/latest/userguide/compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Infrastructure security](https://docs.aws.amazon.com/batch/latest/userguide/infrastructure-security.html): Learn how AWS Batch isolates service traffic.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/batch/latest/userguide/cross-service-confused-deputy-prevention.html): Prevent cross-service confused deputy attacks in AWS Batch by implementing proper IAM policies and security controls for service-to-service interactions.

### [CloudTrail](https://docs.aws.amazon.com/batch/latest/userguide/logging-using-cloudtrail.html)

Learn about logging AWS Batch with AWS CloudTrail.

- [AWS Batch information in CloudTrail](https://docs.aws.amazon.com/batch/latest/userguide/service-name-info-in-cloudtrail.html): CloudTrail is enabled on your AWS account when you create the account.
- [Reference: Understanding AWS Batch log file entries](https://docs.aws.amazon.com/batch/latest/userguide/understanding-service-name-entries.html): A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify.
- [Troubleshoot AWS Batch IAM](https://docs.aws.amazon.com/batch/latest/userguide/security_iam_troubleshoot.html): Troubleshoot common IAM authentication and authorization issues when working with AWS Batch resources and API operations.


## [AWS Step Functions](https://docs.aws.amazon.com/batch/latest/userguide/stepfunctions-batch-console.html)

- [Tutorial: View state machine details](https://docs.aws.amazon.com/batch/latest/userguide/stepfunctions-configure.html): The AWS Batch console displays a list of your state machines in the current AWS Region that contain at least one workflow step that submits a AWS Batch job.
- [Tutorial: Edit a state machine](https://docs.aws.amazon.com/batch/latest/userguide/stepfunctions-edit.html): When you want to edit a state machine, AWS Batch opens the Edit definition page of the Step Functions console.
- [Tutorial: Run a state machine](https://docs.aws.amazon.com/batch/latest/userguide/stepfunctions-run.html): When you want to run a state machine, AWS Batch opens the New execution page of the Step Functions console.


## [Amazon EventBridge](https://docs.aws.amazon.com/batch/latest/userguide/cloudwatch_event_stream.html)

### [AWS Batch events](https://docs.aws.amazon.com/batch/latest/userguide/batch_cwe_events.html)

AWS Batch sends job status change events to EventBridge.

- [Job state change events](https://docs.aws.amazon.com/batch/latest/userguide/batch_job_events.html): Anytime that an existing (previously submitted) job changes states, an event is created.
- [Job queue blocked events](https://docs.aws.amazon.com/batch/latest/userguide/batch-job-queue-blocked-events.html): Anytime that AWS Batch detects a job in the RUNNABLE state and thus blocking a queue, an event is created in Amazon CloudWatch Events.
- [Service job state change events](https://docs.aws.amazon.com/batch/latest/userguide/service-job-events.html): Anytime that an existing service job changes states, an event is created.
- [Service job queue blocked events](https://docs.aws.amazon.com/batch/latest/userguide/batch-service-job-queue-blocked-events.html): Anytime that AWS Batch detects a blocked queue, an event is created in Amazon CloudWatch Events.
- [Tutorial: Use AWS user notifications with AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/using-user-notifications.html): Learn how to get notifications for AWS Batch.

### [AWS Batch jobs as EventBridge targets](https://docs.aws.amazon.com/batch/latest/userguide/batch-cwe-target.html)

Discusses how to submit AWS Batch jobs with EventBridge rules and targets.

- [Tutorial: Create a scheduled job](https://docs.aws.amazon.com/batch/latest/userguide/scheduled-batch-job.html): The following procedure covers how to create a scheduled AWS Batch job and the required EventBridge IAM role.
- [Tutorial: Create a rule with an event pattern](https://docs.aws.amazon.com/batch/latest/userguide/event-pattern-batch-job.html): The following procedure covers how to create a rule with an event pattern.
- [Tutorial: Pass input transformer](https://docs.aws.amazon.com/batch/latest/userguide/cwe-input-transformer.html): You can use the EventBridge input transformer to pass event information to AWS Batch in a job submission.

### [Tutorial: Listen for AWS Batch job events](https://docs.aws.amazon.com/batch/latest/userguide/batch_cwet.html)

Tutorial on setting up a Lambda function to listen for AWS Batch job events using EventBridge and write them to CloudWatch Logs.

- [Tutorial: Create the Lambda function](https://docs.aws.amazon.com/batch/latest/userguide/cwet_create_lam.html): In this procedure, you create a simple Lambda function to serve as a target for AWS Batch event stream messages.
- [Tutorial: Register the event rule](https://docs.aws.amazon.com/batch/latest/userguide/cwet_register_event_rule.html): In this section, you create an EventBridge event rule that captures job events that are coming from your AWS Batch resources.
- [Tutorial: Test your configuration](https://docs.aws.amazon.com/batch/latest/userguide/cwet_test.html): You can now test your EventBridge configuration by submitting a job to your job queue.

### [Tutorial: Sending Amazon Simple Notification Service alerts for failed job events](https://docs.aws.amazon.com/batch/latest/userguide/batch_sns_tutorial.html)

Tutorial on configuring Amazon SNS alerts for failed AWS Batch job events using EventBridge event rules to monitor job failures.

- [Tutorial: Create and subscribe to an Amazon SNS topic](https://docs.aws.amazon.com/batch/latest/userguide/batch_sns_create_topic.html): For this tutorial, you configure an Amazon SNS topic to serve as an event target for your new event rule.
- [Tutorial: Register an event rule](https://docs.aws.amazon.com/batch/latest/userguide/batch_sns_reg_rule.html): Next, register an event rule that captures only job-failed events.
- [Tutorial: Test your rule](https://docs.aws.amazon.com/batch/latest/userguide/batch_sns_test_rule.html): To test your rule, submit a job that exits shortly after it starts with a non-zero exit code.


## [Monitor AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/logging-and-moritoring-batch.html)

### [CloudWatch Logs](https://docs.aws.amazon.com/batch/latest/userguide/using_cloudwatch_logs.html)

Configure AWS Batch jobs to send log information to CloudWatch Logs for centralized monitoring and troubleshooting of job execution.

- [Tutorial: Add a CloudWatch Logs IAM policy](https://docs.aws.amazon.com/batch/latest/userguide/cwl_iam_policy.html): Before your jobs can send log data and detailed metrics to CloudWatch Logs, you must create an IAM policy that uses the CloudWatch Logs APIs.
- [Install and configure the CloudWatch agent](https://docs.aws.amazon.com/batch/latest/userguide/installing_cwl_agent.html): You can create an Amazon EC2 launch template that includes CloudWatch monitoring.
- [Tutorial: View CloudWatch Logs](https://docs.aws.amazon.com/batch/latest/userguide/viewing_cwlogs.html): You can view and search CloudWatch Logs logs in the AWS Management Console.

### [CloudWatch Container Insights](https://docs.aws.amazon.com/batch/latest/userguide/cloudwatch-container-insights.html)

Turn on CloudWatch Container Insights to view aggregated metrics for AWS Batch compute environments and jobs.

- [Turn on Container Insights](https://docs.aws.amazon.com/batch/latest/userguide/cloudwatch-container-insights-working.html): Complete the following steps to turn on Container Insights for AWS Batch compute environments.
- [Use CloudWatch Logs to monitor AWS Batch on Amazon EKS jobs](https://docs.aws.amazon.com/batch/latest/userguide/batch-eks-cloudwatch-logs.html): Install the AWS for Fluent Bit image to monitor AWS Batch on Amazon EKS jobs using CloudWatch Logs.


## [Tag your resources](https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html)

- [Tag basics](https://docs.aws.amazon.com/batch/latest/userguide/tag-basics.html): A tag is a label that you assign to an AWS resource.
- [Tag your resources](https://docs.aws.amazon.com/batch/latest/userguide/tag-resources.html): You can tag new or existing AWS Batch compute environments, jobs, job definitions, job queues, and scheduling policies.
- [Tag restrictions](https://docs.aws.amazon.com/batch/latest/userguide/tag-restrictions.html): The following basic restrictions apply to tags:
- [Tutorial: Manage tags using the console](https://docs.aws.amazon.com/batch/latest/userguide/tag-resources-console.html): Using the AWS Batch console, you can manage the tags associated with new or existing compute environments, jobs, job definitions, and job queues.
- [Manage tags using the CLI or API](https://docs.aws.amazon.com/batch/latest/userguide/tag-resources-api-sdk.html): Use the following AWS CLI commands or AWS Batch API operations to add, update, list, and delete the tags for your resources.


## [Best practices](https://docs.aws.amazon.com/batch/latest/userguide/best-practices.html)

- [When to use AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/bestpractice1.html): AWS Batch runs jobs at scale and at low cost, and provides queuing services and cost-optimized scaling.
- [Checklist to run at scale](https://docs.aws.amazon.com/batch/latest/userguide/bestpractice2.html): Before you run a large workload on 50 thousand or more vCPUs, consider the following checklist.
- [Optimize containers and AMIs](https://docs.aws.amazon.com/batch/latest/userguide/bestpractice3.html): Container size and structure are important for the first set of jobs that you run.
- [Choose the right compute environment resource](https://docs.aws.amazon.com/batch/latest/userguide/bestpractice4.html): AWS Fargate requires less initial setup and configuration than Amazon EC2 and is likely easier to use, particularly if it's your first time.
- [Amazon EC2 On-Demand or Amazon EC2 Spot](https://docs.aws.amazon.com/batch/latest/userguide/bestpractice5.html): Most AWS Batch customers use Amazon EC2 Spot instances because of the savings over On-Demand instances.
- [Use Amazon EC2 Spot best practices for AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/bestpractice6.html): When you choose Amazon Elastic Compute Cloud (EC2) Spot instances, you likely can optimize your workflow to save costs, sometimes significantly.
- [Common errors and troubleshooting](https://docs.aws.amazon.com/batch/latest/userguide/bestpractice7.html): Errors in AWS Batch often occur at the application level or are caused by instance configurations that donât meet your specific job requirements.


## [Troubleshooting](https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html)

### [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/batch-troubleshooting.html)

Review the following topics to find review processes and potential solutions to common issues that you may encounter when using AWS Batch.

- [Optimal instance type configuration to receive automatic instance family updates](https://docs.aws.amazon.com/batch/latest/userguide/optimal-default-instance-troubleshooting.html)
- [INVALID compute environment](https://docs.aws.amazon.com/batch/latest/userguide/invalid_compute_environment.html): Troubleshoot AWS Batch compute environments in INVALID state by identifying configuration issues and understanding managed resource constraints.
- [Jobs stuck in a RUNNABLE status](https://docs.aws.amazon.com/batch/latest/userguide/job_stuck_in_runnable.html): Troubleshoot AWS Batch jobs stuck in RUNNABLE status by identifying queue blocking issues and using CloudWatch Events for monitoring.
- [Spot Instances not tagged on creation](https://docs.aws.amazon.com/batch/latest/userguide/spot-instance-no-tag.html): Troubleshoot Spot Instance tagging issues in AWS Batch compute environments and apply the correct IAM managed policy for tagging permissions.
- [Spot Instances not scaling down](https://docs.aws.amazon.com/batch/latest/userguide/spot-fleet-not-authorized.html): Troubleshoot Spot Instances scaling issues related to AWSServiceRoleForBatch service-linked role and AmazonEC2SpotFleetTaggingRole policy requirements.
- [Can't retrieve Secrets Manager secrets](https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting-cant-specify-secrets.html): Troubleshoot issues retrieving Secrets Manager secrets in AWS Batch jobs by configuring the Amazon ECS agent with proper execution role settings.
- [Can't override job definition resource requirements](https://docs.aws.amazon.com/batch/latest/userguide/override-resource-requirements.html): Troubleshoot issues when attempting to override job definition resource requirements using containerOverrides in SubmitJob operations.
- [Error message when you update the desiredvCpus setting](https://docs.aws.amazon.com/batch/latest/userguide/error-desired-vcpus-update.html): Troubleshoot error messages when updating the desiredvCpus setting in AWS Batch compute environments and understand scaling constraints.

### [AWS Batch on Amazon EKS](https://docs.aws.amazon.com/batch/latest/userguide/batch-eks-troubleshooting.html)

- [INVALID compute environment](https://docs.aws.amazon.com/batch/latest/userguide/batch_eks_invalid_compute_environment.html): Troubleshoot AWS Batch on Amazon EKS compute environments in INVALID state by identifying configuration issues and resolving common problems.
- [AWS Batch on Amazon EKS job is stuck in RUNNABLE status](https://docs.aws.amazon.com/batch/latest/userguide/batch_eks_job_stuck_in_runnable.html): Troubleshoot AWS Batch jobs stuck in RUNNABLE state on Amazon EKS by verifying aws-auth ConfigMap configuration and RBAC permissions.
- [AWS Batch on Amazon EKS job is stuck in STARTING status](https://docs.aws.amazon.com/batch/latest/userguide/batch-eks-job-stuck-in-starting.html): Troubleshoot AWS Batch on Amazon EKS jobs stuck in STARTING status by diagnosing Pod issues and using kubectl to identify problems.
- [Verify that the aws-auth ConfigMap is configured correctly](https://docs.aws.amazon.com/batch/latest/userguide/verify-configmap-config.html): Verify that the aws-auth ConfigMap is configured correctly for AWS Batch on Amazon EKS by checking role mappings and service role configuration.
- [RBAC permissions or bindings aren't configured properly](https://docs.aws.amazon.com/batch/latest/userguide/batch_eks_rbac.html): Troubleshoot RBAC permissions and bindings for AWS Batch on Amazon EKS by verifying aws-batch role access to Kubernetes namespaces.
