# Source: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/llms.txt

# Amazon Elastic Container Service Developer Guide

> Run, stop, and manage Docker containers on a cluster using the Amazon Elastic Container Service Developer Guide.

- [What is Amazon ECS?](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)
- [Best practices](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-best-practices.html)
- [Amazon ECS Anywhere](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch-type-external.html)
- [Amazon ECS API reference](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ProgrammingGuide.html)
- [Document history](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/document_history.html)

## [Getting started](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started.html)

- [Set up](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/get-set-up-for-amazon-ecs.html): Complete these steps to use Amazon ECS for the first time.
- [Creating a container image](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-container-image.html): Learn how to create a container image to use with Amazon ECS.
- [Learn how to create a task for Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started-managed-instances.html): Learn how to get started using Amazon ECS Managed Instances on Amazon ECS
- [Learn how to create a task for Amazon ECS Managed Instances with the AWS CLI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started-managed-instances-cli.html): The following steps help you set up a cluster, create a capacity provider, register a task definition, run a Linux task, and perform other common scenarios in Amazon ECS with Amazon ECS Managed Instances using the AWS CLI.
- [Learn how to create a Linux task for Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started-fargate.html): Learn how to get started using Fargate Linux containers on Amazon ECS
- [Learn how to create a Windows task for Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Windows_fargate-getting_started.html): Get started with Amazon ECS on AWS Fargate by using Fargate for your tasks in the Regions where Amazon ECS supports AWS Fargate.
- [Learn how to create a Windows task for EC2](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started-ecs-ec2-v2.html): Learn how to get started using EC2Windows containers on Amazon ECS
- [Using the AWS CDK](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/tutorial-ecs-web-server-cdk.html): Learn how to deploy a containerized web server with Amazon Elastic Container Service using the AWS Cloud Development Kit (AWS CDK).

### [Creating resources using the AWS Copilot CLI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Copilot.html)

The AWS Copilot CLI provides high-level commands to simplify modeling, creating, releasing, and managing containerized applications on Amazon ECS from a local development environment.

- [Installing the AWS Copilot CLI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/copilot-install.html): Install the AWS Copilot CLI manually or using Homebrew by following these steps
- [Deploying a sample Amazon ECS application using the AWS Copilot CLI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/copilot-deploy.html): Learn how to use AWS Copilot CLI to deploy your Amazon ECS application by following these demo steps.


## [Amazon ECS with CloudFormation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-with-cloudformation.html)

- [Creating Amazon ECS resources using the CloudFormation console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-cloudformation-console.html): Learn how to create Amazon ECS resources using the CloudFormation console
- [Creating Amazon ECS resources using AWS CLI commands for CloudFormation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-cloudformation-cli.html): Learn how to create Amazon ECS resources using AWS CLI commands for CloudFormation
- [Example CloudFormation templates](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/working-with-templates.html): CloudFormation template reference for Amazon ECS


## [Architect your solution for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-configuration.html)

- [Launch types and capacity providers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/capacity-launch-type-comparison.html): Amazon ECS provides multiple ways to manage the underlying compute capacity for containerized applications.
- [Using dual-stack endpoints](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/dual-stack-endpoint.html): Explains how to make requests to Amazon ECS dual-stack endpoints.
- [Applications in shared subnets, Local Zones, and Wavelength Zones](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-regions-zones.html): Learn how Amazon ECS supports workloads that use Local Zones, Wavelength Zones, and AWS Outposts for when low latency or local data processing is a requirement.
- [Amazon Elastic Container Service on AWS Outposts](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-outposts.html): You can use Amazon ECS with AWS Outposts.
- [Best practices for container images](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-considerations.html): Learn the best practices for creating container images for Amazon ECS.

### [Networking best practices](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/networking-best-practices.html)

Learn about the best practices for Amazon ECS networking.

- [Connect applications to the internet](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/networking-outbound.html): Learn about the best practices for connecting Amazon ECS applications to the internet.
- [Best practices for receiving inbound connections to Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/networking-inbound.html): Learn about the best practices for receiving inbound connections to Amazon ECS from the internet.
- [Best practices for connecting to AWS services](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/networking-connecting-vpc.html): Learn about the best practices for connecting Amazon ECS to other AWS services.
- [Best practices for connecting services](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/networking-connecting-services.html): Learn about te best practices for connecting your Amazon ECS services.
- [Best practices for networking services across AWS accounts and VPCs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/networking-connecting-services-crossaccount.html): Learn about the best practices for networking services across accounts.
- [AWS services for networking troubleshooting](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/networking-troubleshooting.html): Learn about the AWS services to use for troubleshooting Amazon ECS networking issues.
- [Optimize task launch time](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-recommendations.html): Learn how to use best practices to improve Amazon ECS task launch time

### [Operating at scale](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/operating-at-scale-best-practice.html)

Operate Amazon Amazon ECS at scale by understanding service quotas, API throttling limits, and scaling considerations for Amazon ECS and integrated AWS services.

- [Amazon ECS service quotas and API throttling limits](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/operating-at-scale-service-quotas-best-practice.html): Understand Amazon ECS service quotas and API throttling limits that affect scaling workloads.
- [Handle throttling issues](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/operating-at-scale-dealing-with-throttles.html): Learn the best practices for monitoring and handling Amazon ECS throttling issues.

### [Auto scaling and capacity management best practices](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/capacity-availability.html)

These are the auto scaling and capacity management best practices for Amazon ECS that you should be mindful of when using Amazon ECS in a production environment.

- [Determining the task size](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/capacity-tasksize-best-practice.html): Learn how to determine appropriate CPU and memory sizes for your ECS tasks based on your application's resource requirements and scaling needs.
- [Optimizing service auto scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/capacity-autoscaling-best-practice.html): Learn about the best practices for configuring Application Auto Scaling for Amazon ECS.
- [Capacity and availability](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/capacity-availability-best-practice.html): Application availability is crucial for providing an error-free experience and for minimizing application latency.
- [Cluster capacity](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/capacity-cluster-best-practice.html): Learn about the best practices for Amazon ECS cluster cpacity
- [Choosing Fargate task sizes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-task-size-best-practice.html): Learn about the best practices for Fargate task sizes.
- [Speeding up cluster auto scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/capacity-cluster-speed-up-ec2-best-practice.html): Learn how to speed up Amazon ECS Cluster Auto Scaling

### [Access features with account settings](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html)

View and manage access to Amazon ECS features.

- [Viewing account settings using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-viewing-longer-id-settings.html): View your account settings in the console.
- [Modifying account settings](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-modifying-longer-id-settings.html): Manage your account settings using the AWS Management Console.
- [Reverting to the default account settings](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-reverting-account.html): Revert your account settings to the default values.
- [Managing account settings using the AWS CLI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/account-setting-management-cli.html): Manage your account settings using the AWS Command Line Interface.
- [IAM roles for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-iam-role-overview.html): Learn about the IAM roles that are used in Amazon ECS.


## [Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ManagedInstances.html)

- [Amazon ECS Managed Instances instance types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-instance-types.html): Learn about EC2 instance type selection options for Amazon ECS Managed Instances tasks and how to configure them.
- [Instance selection best practices for Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-instance-selection-best-practices.html): Learn best practices for selecting instance types and configurations when using Amazon ECS Managed Instances to optimize performance, cost, and placement success rates.
- [Amazon ECS Managed Instances pull behavior](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instance-pull-behavior.html): Learn about the best practices for Amazon ECS Managed Instances container image pull behavior.
- [Patching in Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-patching.html): Learn how AWS automatically manages patching and maintenance for Amazon ECS Managed Instances to ensure security and compliance while maintaining workload availability.
- [Security considerations for Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-security.html): Amazon ECS Managed Instances provides a fully managed container compute experience that enables you to run workloads on specific Amazon EC2 instance types while offloading security responsibilities to AWS.
- [Enabling VPC Encryption control for Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-vpc-encryption.html): Learn how to configure Amazon ECS Managed Instances to work with VPC Encryption Controls for encryption in transit compliance.
- [Infrastructure optimization](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-infrastructure-optimization.html): Learn how Amazon ECS Managed Instances optimize costs and performance through intelligent infrastructure optimization during the operational phase.
- [Migrate from Fargate to Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/migrate-fargate-to-managed-instances.html): Learn how to migrate your existing Fargate workloads to Amazon ECS Managed Instances for enhanced capabilities and cost optimization.
- [Migrate from EC2 to Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/migrate-ec2-to-managed-instances.html): Learn how to migrate your existing Amazon EC2 workloads to Amazon ECS Managed Instances for enhanced capabilities and cost optimization.


## [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)

- [Security considerations for when to use Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-fargate-ec2.html): Learn when to use Fargate.

### [Fargate security best practices](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-fargate.html)

These are the security best practices forFargate on Amazon ECS that you should be mindful of when using Amazon ECS in a production environment.

- [Fargate security considerations](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-security-considerations.html): These are the Fargate security considerations for Amazon ECS.

### [Fargate platform versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform-fargate.html)

Learn about supported AWS Fargate Linux and Windows platform versions.

- [Migrating to Linux platform version 1.4.0](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform-version-migration.html): Learn about the considerations needed for migrating to Fargate Linux platform version 1.4.0.
- [Linux Platform version change log](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform-versions-changelog.html): Learn about the Fargate versions changelog.
- [Linux platform version deprecation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform-versions-retired.html): Learn about the deprecated Fargate versions.
- [Windows platform version change log](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform-windows-fargate.html): Learn about supported AWS Fargate Linux platform versions.
- [Windows containers on Fargate considerations for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/windows-considerations.html): Learn how Fargate on Windows differs from Fargate on Linux for Amazon ECS.
- [Linux containers on Fargate container image pull behavior](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-pull-behavior.html): Learn about the container pull behavior for Linux containers on Fargate and what the best practices are.
- [Windows containers on Fargate container image pull behavior](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-windows-behavior.html): Learn about the container pull behavior for Windows containers on Fargate and what the best practices are.

### [Fargate task ephemeral storage](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-task-storage.html)

When provisioned, each Amazon ECS task hosted on Linux containers on AWS Fargate receives the following ephemeral storage for bind mounts.

### [Customer managed keys for AWS Fargate ephemeral storage](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-storage-encryption.html)

AWS Fargate supports customer managed keys for ephemeral storage.

- [Create an encryption key for Fargate ephemeral storage](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-create-storage-key.html): Create customer managed encryption keys for Fargate ephemeral storage in AWS KMS.
- [Managing AWS KMS keys for Fargate ephemeral storage](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-managing-kms-key.html): Learn how to AWS KMS keys for Fargate ephemeral storage.

### [Task retirement and maintenance](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-maintenance.html)

Being prepared for Fargate task retirement.

- [Prepare for AWS Fargate task retirement on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/prepare-task-retirement.html): Being prepared for Fargate task retirement.
- [AWS Fargate Regions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate-Regions.html): Learn about the Region support for Linux containers on AWS Fargate and Windows containers on AWS Fargate.


## [EC2](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch-type-ec2.html)

- [Container image pull behavior for EC2 and external instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/pull-behavior.html): Learn about the best practices for EC2 container image pull behavior on Amazon ECS.


## [Amazon ECS Express Mode](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-overview.html)

- [Creating an Express Mode service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-create-full.html): Learn how to create a new Express Mode service in Amazon ECS with pre-configured settings for common use cases, including networking, load balancing, and auto scaling configurations using the console.
- [Create your first Express Mode service in the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-first-run.html): Get started quickly with Express Mode service using the simplified first-run experience.
- [Create your first Express Mode service using the AWS CLI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-getting-started.html): Learn how to create your first Express Mode service application and deploy a containerized web application.
- [Resources created by Express Mode services](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-work.html): Learn about the resources Express Mode services create.
- [Viewing the details of an Express Mode service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-view-service.html): Learn how to view details about your Express Mode service using the Amazon ECS console.
- [Updating an Amazon ECS Express Mode service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-update-full.html): Learn how to update an existing Express Service in Amazon ECS with modified settings for networking, load balancing, auto scaling, and other configurations using the ECS console.
- [Delete Express Mode services](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-delete-task.html): Delete an Express Mode service and its associated resources.
- [Best practices for Amazon ECS Express Mode services](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-best-practices.html): Learn best practices for deploying, managing, and optimizing Express Mode service applications.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-troubleshooting.html): Diagnose and resolve common issues with Express Mode service applications.
- [Updating Resources Outside of Express Mode](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-advanced-customization.html): Learn how to customize Express Mode service resources beyond Express Mode APIs and understand the shared responsibility model.


## [Task definitions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html)

- [Task definition states](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-definition-state.html): Learn about Amazon ECS task definition states.

### [Architect your application](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/application_architecture.html)

Learn how to structure your application for Amazon ECS by creating effective task definitions.

- [Best practices for task sizes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/capacity-tasksize.html): Learn about the best practices for Amazon ECS task sizes.

### [Task networking for Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instance-networking.html)

Learn about the networking options for Amazon ECS tasks when using Amazon ECS Managed Instances.

- [AWSVPC network mode](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-awsvpc-mode.html): awsvpc mode in Amazon ECS Managed Instances provides the same networking capabilities as traditional Fargate while supporting multiple tasks per instance.
- [Host network mode](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-host-modes.html): Host network mode in Amazon ECS Managed Instances provide the same functionality as Amazon ECS on Amazon EC2 for specialized networking requirements.

### [Task networking for EC2](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html)

Learn about the networking options for Amazon ECS when you use Amazon EC2 instances.

- [AWSVPC network mode](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking-awsvpc.html): The task networking features that are provided by the awsvpc network mode give Amazon ECS tasks the same networking properties as Amazon EC2 instances.
- [Host network mode](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/networking-networkmode-host.html): The host network mode is the most basic network mode that's supported in Amazon ECS.
- [Bridge network mode](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/networking-networkmode-bridge.html): With bridge mode, you're using a virtual network bridge to create a layer between the host and the networking of the container.
- [Task networking for Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-task-networking.html): Learn abut the networking option for Fargate tasks.

### [Storage options for tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_data_volumes.html)

Learn about the storage options for your Amazon ECS tasks.

### [Amazon EBS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html)

Learn how to use Amazon Elastic Block Store (Amazon EBS) volumes with your Amazon ECS tasks.

- [Non-root user behavior](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-non-root-behavior.html): When you specify a non-root user in your container definition, Amazon ECS automatically configures the Amazon EBS volume with group-based permissions that allow the specified user to read and write to the volume.
- [Defer volume configuration to launch time in a task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specify-ebs-config.html): Learn about deferring volume configuration to launch time in your task definition.
- [Encrypt data stored in Amazon EBS volumes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-kms-encryption.html): Learn about AWS Key Management Service (AWS KMS) key encryption of Amazon EBS volumes that are attached to your Amazon ECS tasks.
- [Specify Amazon EBS volume configuration at deployment](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/configure-ebs-volume.html): Learn about configuring an Amazon EBS volume when you run a standalone task, create a service, or update a service using the AWS CLI.
- [Performance of Amazon EBS volumes for Fargate on-demand tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-fargate-performance-limits.html): Learn about the baseline Amazon EBS volume IOPS and throughput available for a Fargate on-demand task.
- [Performance of Amazon EBS volumes for EC2 tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-fargate-performance-limits-ec2.html): Learn about the baseline Amazon EBS volume IOPS and throughput available for EC2 tasks.
- [Performance of Amazon EBS volumes for Amazon ECS Managed Instances tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-managed-instances-performance.html): Learn about the baseline Amazon EBS volume IOPS and throughput available for Amazon ECS Managed Instances tasks.

### [Troubleshooting Amazon EBS volume attachment](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/troubleshoot-ebs-volumes.html)

Learn how to troubleshoot issues with attaching Amazon EBS volumes to Amazon ECS tasks.

- [Container can't write to Amazon EBS volume](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/troubleshoot-non-root-container.html): If your container can't write to the mounted Amazon EBS volume, the issue is typically related to file system permissions.
- [Status reasons for Amazon EBS volume attachment](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/troubleshoot-ebs-volumes-scenarios.html): Troubleshoot volume attachment failure status reasons

### [Amazon EFS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/efs-volumes.html)

You can use Amazon EFS file systems with Amazon ECS to export file system data across your fleet of container instances.

- [Best practices for using Amazon EFS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/efs-best-practices.html): Learn about the best practices for using Amazon EFS with Amazon ECS.
- [Specify an Amazon EFS file system in a task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specify-efs-config.html): Learn how to specify an Amazon EFS file system volume in your task definition.
- [Configuring Amazon EFS file systems](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/tutorial-efs-volumes.html): Learn how to use Amazon Elastic File System (Amazon EFS) file systems with Amazon ECS.

### [FSx for Windows File Server](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/wfsx-volumes.html)

You can use FSx for Windows File Server to deploy Windows workloads that require access to shared external storage, highly-available Regional storage, or high-throughput storage.

- [Best practices for using FSx for Windows File Server](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/wfsx-best-practices.html): Learn about the best practices for use FSx for Windows File Server with Amazon ECS
- [Specify an FSx for Windows File Server file system in a task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specify-wfsx-config.html): Learn how to use FSx for Windows File Server file system volumes for your containers.
- [Learn how to configure FSx for Windows File Server file systems](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/tutorial-wfsx-volumes.html): Learn how to launch an Amazon ECS-Optimized Windows instance that hosts an FSx for Windows File Server file system and containers that can access the FSx for Windows File Server file system.

### [Docker volumes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-volumes.html)

You can use Docker volumes for your Amazon ECS container volumes.

- [Specify a Docker volume in a task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specify-volume-config.html): Learn how to configure Docker volumes for Amazon ECS.
- [Docker volume examples](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-volume-examples.html): View examples on how to use Docker volumes on Amazon ECS.

### [Bind mounts](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/bind-mounts.html)

With bind mounts, a file or directory on a host, such as an Amazon EC2 instance is mounted into a container.

- [Specify a bind mount in a task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specify-bind-mount-config.html): Learn how to specify a bind mount in your task definition.
- [Bind mount examples for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/bind-mount-examples.html): View some task definitions that specify bind mounts.
- [Managing container swap memory space](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-swap.html): Learn how to manage EC2 Linux container swap space on Amazon ECS.
- [Task definition differences for Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-tasks-services.html): Learn about task definition considerations for Amazon ECS Managed Instances on Amazon ECS.
- [Task definition differences for Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-tasks-services.html): Learn about task definition considerations for Fargate on Amazon ECS.
- [Task definition differences for EC2 instances running Windows](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/windows_task_definitions.html): Tasks that run on EC2 Windows instances don't support all of the Amazon ECS task definition parameters that are available.
- [Creating a task definition using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-task-definition.html): Use the console to create an Amazon ECS task definition.
- [Using Amazon Q Developer to provide task definition recommendations in the Amazon ECS console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-amazon-q.html): You can use Amazon Q Developer to provide task definition recommendations in the console.
- [Updating a task definition using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-task-definition-console-v2.html): Create a task definition revision when you need to modify a task definition parameter.
- [Deregistering a task definition revision using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deregister-task-definition-v2.html): When you deregister a task definition, it no longer displays in your ListTaskDefinition API calls or in the console.
- [Deleting a task definition revision using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/delete-task-definition-v2.html): When no longer need a specific task definition revision in Amazon ECS, you can delete the task definition revision.

### [Task definition use cases](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/use-cases.html)

Learn more about how to write task definitions for various AWS services and features.

### [Task definitions for GPU workloads](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-gpu.html)

Amazon ECS supports workloads that use GPUs, when you create clusters with container instances that support GPUs.

- [Use GPUs with Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-gpu.html): Amazon ECS Managed Instances supports GPU-accelerated computing for workloads such as machine learning, high-performance computing, and video processing through the following Amazon EC2 instance types.
- [Launch a GPU container instance for Amazon ECS on Amazon EC2](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/gpu-launch.html): Learn how to launch a GPU container for Amazon ECS.
- [Specifying GPUs in a task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-gpu-specifying.html): To use the GPUs on a container instance and the Docker GPU runtime, make sure that you designate the number of GPUs your container requires in the task definition.

### [Task definitions for video trancoding workloads](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-vt1.html)

Register VT1 instances to your cluster so that you can run live and pre-rendered video transcoding workloads as tasks on Amazon ECS.

- [Specifying video transcoding in a task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-def-video-transcode.html): Register VT1 instances to your cluster so that you can run live and pre-rendered video transcoding workloads as tasks on Amazon ECS.

### [Task definitions for AWS Neuron machine learning workloads](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-inference.html)

You can register Trn1, Inf1, or Inf2 instances to your cluster for machine learning workloads.

- [Specifying AWS Neuron machine learning in a task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-inference-task-def.html): You can register Trn1, Inf1, or Inf2 instances to your cluster for machine learning workloads.

### [Task definitions for deep learning instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-dl1.html)

You can register DL1 instances to your cluster for deep learning workloads.

- [Specifying deep learning in a task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-dl1-requirements.html): You can register DL1 instances to your cluster for deep learning workloads.

### [Task definitions for 64-bit ARM workloads](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-arm64.html)

Run your high-performance computing, CPU-based machine learning inference, video encoding, electronic design automation, gaming, open-source databases, and in-memory caches applications on 64-but ARM instances that are registered to your cluster.

- [Specifying the ARM architecture in a task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-arm-specifying.html): Run your high-performance computing, CPU-based machine learning inference, video encoding, electronic design automation, gaming, open-source databases, and in-memory caches applications on 64-but ARM instances that are registered to your cluster.

### [Send logs to CloudWatch](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_awslogs.html)

You can configure the containers in your tasks to send log information to CloudWatch Logs.

- [Example task definition: Route logs to CloudWatch](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specify-log-config.html): Learn how to specify the awslogs driver

### [Send logs to an AWS service or AWS Partner](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html)

You can configure your task definition to route logs to an AWS service or AWS Partner Network (APN) destination for log storage and analytics.

- [Configuring logs for high throughput](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/firelens-docker-buffer-limit.html): Learn how to optimize Fluent Bit with FireLens for high log throughput scenarios, including filesystem buffering, memory management, and output optimization.
- [AWS for Fluent Bit image repositories](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/firelens-using-fluentbit.html): AWS provides a Fluent Bit image with plugins for both CloudWatch Logs and Firehose.
- [Example task definition: Route logs to FireLens](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/firelens-taskdef.html): Use custom log routing in your task definition to route logs to FireLens.
- [Using non-AWS container images](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/private-auth.html): Use private registry to store your credentials securely and then reference them in your task definition.

### [Restart individual containers in tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-restart-policy.html)

Learn about restart policies for containers defined in your task definition.

- [Specifying a container restart policy in a task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-restart-policy-example.html): Learn how to specify container restart policies in a task definition

### [Pass sensitive data to a container](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html)

Learn how to pass sensitive data to an Amazon ECS container.

- [Pass an individual environment variable to a container](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/taskdef-envfiles.html): Use the environment container definition parameter to pass environment variables to a container.
- [Pass environment variables to a container](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/use-environment-file.html): Use an environment variable file to pass environment variables to a container.
- [Pass Secrets Manager secrets programmatically](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/secrets-app-secrets-manager.html): You can safely pass sensitive data, such as credentials to a database, into your container.
- [Pass Systems Manager Parameter Store secrets programmatically](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/secrets-app-ssm-paramstore.html): Instead of hardcoding sensitive information in plain text in your application, you can use Systems Manager Parameter Store to store the sensitive data.
- [Pass Secrets Manager secrets through environment variables](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/secrets-envvar-secrets-manager.html): When you inject a secret as an environment variable, you can specify the full contents of a secret, a specific JSON key within a secret, or a specific version of a secret to inject.
- [Pass Systems Manager parameters through environment variables](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/secrets-envvar-ssm-paramstore.html): Amazon ECS allows you to inject sensitive data into your containers by storing your sensitive data in Systems Manager Parameter Store parameters and then referencing them in your container definition.
- [Pass secrets for logging configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/secrets-logconfig.html): You can use the secretOptions parameter in logConfiguration to pass sensitive data used for logging.
- [Specifying sensitive data using Secrets Manager secrets](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data-tutorial.html): Learn how to create an Secrets Manager secret, reference the secret in an Amazon ECS task definition, and then verify it worked by querying the environment variable inside a container showing the contents of the secret.
- [Task definition parameters for Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters-managed-instances.html): Learn about the task definition parameters that you can use to define your Amazon ECS tasks.
- [Task definition parameters for Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html): Learn about the task definition parameters that you can use to define your Amazon ECS tasks.
- [Task definition parameters for EC2](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters_ec2.html): Learn about the task definition parameters that you can use to define your Amazon ECS tasks.
- [Task definition template](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-definition-template.html): View Amazon ECS task definition templates.
- [Example task definitions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/example_task_definitions.html): You can copy the examples and snippets to start creating your own task definitions.


## [Clusters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/clusters.html)

### [Clusters for Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instance-clusters.html)

Learn how to create and manage clusters for Amazon ECS Managed Instances, including capacity providers, scaling strategies, and infrastructure management.

- [Creating a cluster for Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-cluster-managed-instances.html): Learn how to create a cluster for Amazon ECS Managed Instances using the ECS console or AWS CLI.
- [Updating a cluster to use Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-cluster-managed-instances.html): Learn how to update a cluster for Amazon ECS Managed Instances using the ECS console or AWS CLI.

### [Managed Instances capacity providers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-capacity-providers-concept.html)

Learn about Amazon ECS Managed Instances capacity providers that provide AWS-managed container compute bridging the simplicity of Fargate with the full range of Amazon EC2 capabilities and instance types.

- [Best practices for updating capacity providers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/capacity-provider-managed-instances-best-practices.html): Learn best practices for safely updating capacity providers for Amazon ECS Managed Instances using an immutable approach.
- [Creating a capacity provider for Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-capacity-provider-managed-instances.html): Learn how to create a capacity provider for Amazon ECS Managed Instances to specify custom instance requirements and attributes.
- [Updating Amazon ECS Managed Instances monitoring](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-capacity-provider-managed-instances.html): Learn how to update the monitoring configuration for your Amazon ECS Managed Instances capacity provider.
- [Deleting a capacity provider](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/delete-capacity-provider-managed-instances-console-v2.html): Learn how to delete your Amazon ECS capacity provider.

### [Task scale-in protection](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instance-task-scale-in-protect.html)

Learn how to protect your Amazon ECS tasks from being terminated by scale-in events.

- [Task scale-in protection endpoint](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instance-task-scale-in-protection-endpoint.html): Learn about the Amazon ECS task scale-in protection endpoint request and response parameters.

### [Clusters for Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-capacity-providers.html)

Learn about the Fargate capacity provider options.

- [Creating a cluster for Fargate workloads](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-cluster-console-v2.html): Learn how to create a cluster for Fargate.

### [Amazon ECS capacity providers for EC2 workloads](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/asg-capacity-providers.html)

Learn how to use Auto Scaling groups to manage the Amazon EC2 instances registered to their clusters.

- [EC2 container instance security](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ec2-security-considerations.html): These are the EC2 container instance security considerations for Amazon ECS
- [Creating a cluster for Amazon EC2 workloads](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-ec2-cluster-console-v2.html): Learn how to create a cluster with EC2 instances.

### [Cluster auto scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-auto-scaling.html)

Learn how Amazon ECS can manage the scaling of Amazon EC2 instances that are registered to your cluster.

- [Optimize cluster auto scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/capacity-cluster-speed-up-ec2.html): Learn about te best practices for Amazon ECS cluster auto scaling.
- [Managed scaling behavior](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-scaling-behavior.html): Learn about how managed scaling works on Amazon ECS.

### [Control the instances Amazon ECS terminates](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-termination-protection.html)

Cluster auto scaling can control which instances are terminated if you turn on managed termination protection.

- [Updating managed termination protection for Amazon ECS capacity providers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-managed-termination-protection.html): Learn how to update the managed termination protection setting for existing capacity providers.
- [Turning on cluster auto scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/turn-on-cluster-auto-scaling.html): Learn how to use cluster auto scaling by using the AWS CLI.
- [Turning off cluster auto scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/turn-off-cluster-auto-scaling.html): Learn how to deactivate cluster auto scaling by using the AWS CLI.
- [Creating a capacity provider](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-capacity-provider-console-v2.html): Learn how to create an Amazon ECS capacity provider when you use EC2 instances.
- [Updating a capacity provider](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-capacity-provider-console-v2.html): Learn how to change the Auto Scaling scaling policy for your Amazon ECS capacity provider.
- [Deleting a capacity provider](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/delete-capacity-provider-console-v2.html): Learn how to delete your Amazon ECS capacity provider.

### [Safely stop workloads](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instance-draining.html)

Managed instance draining facilitates graceful termination of Amazon EC2 instances.

- [Configuring Amazon ECS capacity providers to safely shut down instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/enable-managed-instance-draining.html): Learn how to configure manged instance draining for your Amazon ECS Auto Scaling group capacity providers.
- [Creating resources for cluster auto scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/tutorial-cluster-auto-scaling-console.html): Learn how to create resources for cluster auto scaling using the AWS Management Console.

### [Amazon EC2 container instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-capacity.html)

Learn how to create Amazon ECS container instance that runs either Linux or Windows.

### [Amazon ECS-optimized Linux AMIs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html)

Amazon ECS provides Linux Amazon ECS-optimized AMIs that are preconfigured with the requirements and recommendations to run your container workloads.

- [Retrieving Amazon ECS-optimized Linux AMI metadata](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/retrieve-ecs-optimized_AMI.html): Use the AWS CLI to retrieve the Amazon ECS-optimized AMI metadata.
- [Migrating from an Amazon Linux 2 to an Amazon Linux 2023 Amazon ECS-optimized AMI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/al2-to-al2023-ami-transition.html): Learn how to migrate your Amazon ECS workloads from Amazon Linux 2 to Amazon Linux 2023 Amazon ECS-optimized AMIs.
- [Amazon ECS-optimized Linux AMI build script](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-ami-build-scripts.html): Learn how to use the Amazon ECS open-sourced build scripts that are used to build the Linux variants of the Amazon ECS-optimized AMI.

### [Amazon ECS-optimized Bottlerocket AMIs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-bottlerocket.html)

Bottlerocket is a Linux based open-source operating system that's purpose built by AWS for running containers on virtual machines or bare metal hosts.

- [Retrieving Amazon ECS-optimized Bottlerocket AMI metadata](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-bottlerocket-retrieve-ami.html): Use the AWS CLI to retrieve the Amazon ECS-optimized AMI Bottlerocket metadata.
- [Launching a Bottlerocket instance](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/bottlerocket-launch.html): You can launch a Bottlerocket instance with the AWS CLI so that you can run your container workloads.

### [Linux container instance management](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/manage-linux.html)

Learn what is involved in managing your Linux container instances.

- [Launching a container instance](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_container_instance.html): Launch a Linux instance by various methods including the Amazon EC2 console, AWS CLI, and SDK.
- [Bootstrapping Linux container instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/bootstrap_container_instance.html): When you launch an Amazon EC2 instance, you have the option of passing user data to the instance.
- [Configuring container instances to receive Spot Instance notices](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/spot-instance-draining-linux-container.html): Learn how Linux Spot Instance draining works on Amazon ECS.
- [Running a script when you launch a container instance](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/start_task_at_launch.html): Learn how run a script on every container instance to deal with operations or security concerns such as monitoring, security, metrics, service discovery, or logging.

### [Increasing Amazon ECS Linux container instance network interfaces](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-eni.html)

Amazon ECS supports launching container instances with increased ENI density using supported Amazon EC2 instance types.

- [Supported EC2 instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/eni-trunking-supported-instance-types.html): Learn which EC2 instances support ENI trunking for Amazon ECS.
- [Reserving container instance memory](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/memory-management.html): When the Amazon ECS container agent registers a container instance into a cluster, the agent must determine how much memory the container instance has available to reserve for your tasks.
- [Manage container instances remotely](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ec2-run-command.html): You can use the Run Command capability in AWS Systems Manager (Systems Manager) to securely and remotely manage the configuration of your Amazon ECS container instances.
- [Using an HTTP proxy for Linux container instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/http_proxy_config.html): You can configure your Amazon ECS container instances to use an HTTP proxy for both the Amazon ECS container agent and the Docker daemon.
- [Configuring pre-initialized instances for your Auto Scaling group](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-warm-pool.html): Amazon ECS supports Amazon EC2 Auto Scaling warm pools.

### [Updating the Amazon ECS container agent](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html)

Occasionally, you might need to update the Amazon ECS container agent to pick up bug fixes and new features.

- [Updating the Amazon ECS container agent on an Amazon ECS-optimized AMI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/agent-update-ecs-ami.html): If you are using an Amazon ECS-optimized AMI, you have several options to get the latest version of the Amazon ECS container agent.
- [Manually updating the Amazon ECS container agent (for non-Amazon ECS-Optimized AMIs)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/manually_update_agent.html): Learn how to update the Amazon ECS container agent for non-Amazon ECS-optimized AMI.

### [Amazon ECS-optimized Windows AMIs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_windows_AMI.html)

Amazon ECS provides Windows Amazon ECS-optimized AMIs that are preconfigured with the requirements and recommendations to run your container workloads.

- [Retrieving Amazon ECS-optimized Windows AMI metadata](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/retrieve-ecs-optimized_windows_AMI.html): Use the AWS CLI to retrieve the Amazon ECS-optimized AMI metadata.
- [AMI versions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-windows-ami-versions.html): View the current and previous versions of the Amazon ECS-optimized AMIs and their corresponding versions of the Amazon ECS container agent, Docker, and the ecs-init package.
- [Building your own AMI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/windows-custom-ami.html): Use EC2 Image Builder to build your own custom Amazon ECS-optimized Windows AMI.

### [Windows container instance management](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/manage-windows.html)

Learn how to manage your Amazon ECS Windows container instances.

- [Launching a container instance](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_window-container_instance.html): Launch a instance instanceusing the Amazon EC2 console.
- [Bootstrapping container instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/bootstrap_windows_container_instance.html): Pass user data to a Windows container instance.
- [Using an HTTP proxy for Windows container instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/http_proxy_config-windows.html): You can configure your Amazon ECS container instances to use an HTTP proxy for both the Amazon ECS container agent and the Docker daemon.
- [Configuring container instances to receive Spot Instance notices](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/windows-spot-instance-draining-container.html): Learn how Windows Spot Instance draining works on Amazon ECS.

### [Clusters for external instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere.html)

Use Amazon ECS Anwhere when you want to run your container workloads on on-premises server or virtual machine (VM).

- [Creating a cluster for External instance workloads](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-cluster-console-v2-ecs-anywhere.html): Learn how to create a cluster for the external launch type.
- [Registering an external instance to an Amazon ECS cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere-registration.html): Learn how to register an external instance to your cluster.
- [Deregistering an external instance](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere-deregistration.html): We recommend that, after you finish using an external instance, you deregister the instance from both Amazon ECS and AWS Systems Manager.
- [Updating the AWS Systems Manager agent and Amazon ECS container agent](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere-updates.html): Your on-premises server or VM must run both the AWS Systems Manager Agent (SSM Agent) and the Amazon ECS container agent when running Amazon ECS workloads.
- [Updating a cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-cluster-v2.html): Learn how to update an Amazon ECS cluster.
- [Deleting a cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/delete_cluster-new-console.html): Learn how to delete your Amazon ECS cluster.
- [Deregistering a container instance](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deregister_container_instance.html): When you are finished with an Amazon EC2 backed container instance, you should deregister it from your cluster.
- [Container instance draining](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-draining.html): Learn how to remove an Amazon ECS from a cluster so that you can perform maintenance on it.
- [Changing the instance type or size outside of the Auto Scaling group](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-change-type.html): Learn how to safely change an EC2 instance type.

### [Amazon EC2 Container Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-versions.html)

The Amazon ECS container agent version supports a different feature set and provides bug fixes from previous versions.

### [Container agent configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html)

Use the Amazon ECS container agent to configure container to configure environment variables for your container instance.

- [Storing container instance configuration in Amazon S3](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-config-s3.html): Learn how to store your Amazon ECS agent configuration in Amazon S3.
- [Installing the Amazon ECS container agent](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-install.html): Manually install the Amazon ECS container agent when you lauched a non Amazon ECS-optimized AMI instance.
- [Configuring container instances for private Docker images](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/private-auth-container-instances.html): The Amazon ECS container agent can authenticate with private registries, using basic authentication.
- [Clean up tasks and images](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/automated_image_cleanup.html): Learn how to configure Amazon ECS to automatically clean up tasks and images.


## [Schedule your containers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html)

- [Task lifecycle](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-lifecycle-explanation.html): Learn about the states that Amazon ECS tasks pass through.

### [How Amazon ECS places tasks on container instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement.html)

Learn how to define which container instances Amazon ECS uses for placing tasks.

- [Amazon ECS Managed Instances auto scaling and task placement](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instance-auto-scaling.html): Amazon ECS Managed Instances use intelligent algorithms to automatically scale your cluster capacity and place tasks efficiently across your infrastructure.

### [Use strategies to define task placement](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html)

Learn how to configure Amazon ECS to place tasks according to a strategy.

- [Example task placement strategies](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/strategy-examples.html): Learn how to create Amazon ECS task placement strategies.
- [Group related tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-groups.html): Learn how to group Amazon ECS so that you define a strategy for how the tasks are placed.

### [Define which container instances are used for tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html)

Learn how to configure Amazon ECS to place tasks on container instances that meet certain criteria.

- [Create expressions to define container instances for tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html): Learn how to group container instances by attributes so that Amazon ECS only places tasks on container instances that match the expression.
- [Example task placement constraints](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/constraint-examples.html): Learn how to create Amazon ECS task placement constraints.

### [Standalone tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/standalone-tasks.html)

Learn when to use an Amazon ECS task.

- [Running an application as a task](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/standalone-task-create.html): Run an Amazon ECS task for a container application that runs once and then stops.
- [Using Amazon EventBridge Scheduler to schedule tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/tasks-scheduled-eventbridge-scheduler.html): Use EventBridge Scheduler to run Amazon ECS tasks on a one-time or recurring schedule.
- [Stopping a task](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/standalone-task-stop.html): Learn how to stop an Amazon ECS task that is not part of a service.

### [Services](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html)

You can use an Amazon ECS service to run and maintain a specified number of instances of a task definition simultaneously in an Amazon ECS cluster.

### [Service deployment controllers and strategies](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_service-options.html)

You can use an Amazon ECS service to run and maintain a specified number of instances of a task definition simultaneously in an Amazon ECS cluster.

### [Amazon ECS deployment failure detection](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-failure-detection.html)

Learn how the Amazon ECS can detect deployment failures.

- [How the deployment circuit breaker detects failures](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-circuit-breaker.html): Learn how the Amazon ECS circuit breaker determines if the tasks reach a steady state.
- [How CloudWatch alarms detect deployment failures](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-alarm-failure.html): You can configure Amazon ECS to set the deployment to failed when it detects that a specified CloudWatch alarm has gone into the ALARM state.
- [Lifecycle hooks for Amazon ECS service deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-lifecycle-hooks.html): When a deployment starts, it goes through lifecycle stages.
- [Stopping service deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/stop-service-deployment.html): Learn how to stop your Amazon ECS service deployments.

### [Rolling update deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-ecs.html)

When you create a service that uses the rolling update deployment type, the Amazon ECS service scheduler replaces the currently running tasks with new tasks.

- [Service parameters best practices](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-options.html): Learn about the Amazon ECS task deployment process and the parameters you can modify to speed up deployments.
- [Creating a rolling update deployment](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-service-console-v2.html): Learn how to create an Amazon ECS service using the Amazon ECS console.

### [Blue/green deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-blue-green.html)

Amazon ECS blue/green deployments enable you to test service changes in a staging environment before routing production traffic to them.

- [Amazon ECS blue/green service deployments workflow](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/blue-green-deployment-how-it-works.html): Learn the comprehensive step-by-step process of how Amazon ECS blue/green deployments work, from initial deployment preparation through final traffic shift.

### [Required resources for Amazon ECS blue/green deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/blue-green-deployment-implementation.html)

Learn how to configure and implement Amazon ECS blue/green deployments with load balancers or Service Connect, including required resources and step-by-step instructions.

- [Application Load Balancer resources for blue/green, linear, and canary deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/alb-resources-for-blue-green.html): Learn about the required Application Load Balancer resources for Amazon ECS blue/green deployments.
- [Network Load Balancer resources for blue/green, linear and canary deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/nlb-resources-for-blue-green.html): Learn about the required Network Load Balancer resources for Amazon ECS blue/green deployments.
- [Service Connect resources for Amazon ECS blue/green, linear, and canary deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect-blue-green.html): Learn about the required Service Connect components for blue/green deployments.
- [Creating a blue/green deployment](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deploy-blue-green-service.html): Learn how to deploy an Amazon ECS service using blue/green deployments.
- [Troubleshooting blue/green deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/troubleshooting-blue-green.html): Learn about common issues and solutions for blue/green deployments in Amazon ECS.

### [Linear deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-linear.html)

Amazon ECS linear deployments enable you to gradually shift traffic from the current service revision to a new revision in equal percentage increments.

- [Required resources for Amazon ECS linear deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/linear-deployment-implementation.html): Learn how to configure and implement Amazon ECS linear deployments with load balancers or Service Connect, including required resources and step-by-step instructions.
- [Creating a linear deployment](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deploy-linear-service.html): Learn how to deploy an Amazon ECS service using linear deployments with incremental traffic shifting.

### [Canary deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/canary-deployment.html)

Amazon ECS canary deployments enable you to test new application versions by routing a small percentage of traffic to the new version while maintaining the majority on the stable version.

- [Required resources for Amazon ECS canary deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/canary-deployment-implementation.html): Overview of the AWS resources required to implement canary deployments with Amazon ECS services, including load balancer configurations and Service Connect setup.
- [Creating a canary deployment](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deploy-canary-service.html): Learn how to deploy an Amazon ECS service using canary deployments with two-stage traffic shifting.
- [External deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-external.html): Use any third-party deployment controller for full control over the deployment process for an Amazon ECS service.

### [CodeDeploy blue/green deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-bluegreen.html)

Use a blue/green deployment to verify a new deployment of a service before sending production traffic to it.

### [Migrate CodeDeploy blue/green deployments to Amazon ECS blue/green deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/migrate-codedeploy-to-ecs-bluegreen.html)

Learn how to migrate your services from CodeDeploy blue/green deployments to Amazon ECS blue/green deployments.

- [Migrating from a CodeDeploy blue/green to an Amazon ECS blue/green service deployment](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/migrate-code-deploy-to-ecs-blue-green.html): Learn how to migrate a CodeDeploy blue/green deployment to an Amazon ECS blue/green deployment.
- [Migrating an CloudFormation CodeDeploy blue/green deployment template to an Amazon ECS blue/green CloudFormation template](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/migrate-codedeploy-to-ecs-bluegreen-cloudformation-template.html): Learn how to migrate your CloudFormation templates from CodeDeploy blue/green to Amazon ECS blue/green deployments.
- [Migrating from a CodeDeploy blue/green to an Amazon ECS rolling update service deployment](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/migrate-code-deploy-to-ecs-rolling.html): Learn how to migrate a CodeDeploy blue/green deployment to an Amazon ECS rolling deployment.

### [Update the Amazon ECS deployment strategy](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/migrate-deployment-strategies.html)

Learn how to migrate between rolling and blue/green deployment strategies for your Amazon ECS services.

- [Updating the deployment strategy from rolling update to Amazon ECS blue/green](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-rolling-to-bluegreen.html): Learn how to migrate your Amazon ECS service from a rolling deployment strategy to a blue/green deployment strategy.
- [Updating the deployment strategy from Amazon ECS blue/green to rolling update](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-bluegreen-to-rolling.html): Learn how to migrate your Amazon ECS service from a blue/green deployment strategy to a rolling deployment strategy.
- [Troubleshooting Amazon ECS deployment strategy updates](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/troubleshooting-deployment-controller-migration.html): Learn about common issues and solutions for blue/green deployments in Amazon ECS.

### [Service deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-deployment.html)

Learn about Amazon ECS service deployments.

- [Service deployment properties](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-deployment-property.html): Learn what information is included in a service deployment.
- [Permissions required for viewing service deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-deployment-permissions.html): Learn about the permissions required for viewing Amazon ECS service deployments in the console.
- [Viewing service deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/view-service-deployment.html): Learn how to view your Amazon ECS service deployments.

### [Service revisions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-revision.html)

A service revision contains a record of the workload configuration Amazon ECSis attempting to deploy.

- [Service revision properties](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-revision-property.html): Learn what information is included in a service revision.
- [Viewing service revision details](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/view-service-revision.html): Learn how to view your Amazon ECS service revision.

### [Availability Zone rebalancing](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-rebalancing.html)

Learn how Amazon ECS can rebalance your service across Availability Zones.

- [Track Availability Zone rebalancing](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/track-service-rebalancing.html): Learn about the events sent for Availability Zone rebalancing.

### [Use load balancing to distribute service traffic](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html)

Use Elastic Load Balancing to distribute traffic evenly across the tasks in your service

- [Optimize load balancer health check parameters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/load-balancer-healthcheck.html): Learn which Elastic Load Balancing health check parameters can be configured to improve Amazon ECS deployment times.
- [Optimize load balancer connection draining parameters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/load-balancer-connection-draining.html): Learn how to configure the load balancer container draining to speed up Amazon ECS deployments.
- [Use an Application Load Balancer for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/alb.html): Learn how to use Application Load Balancers with Amazon ECS.
- [Use a Network Load Balancer for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/nlb.html): Learn how to use Network Load Balancers with Amazon ECS.
- [Use a Gateway Load Balancer for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/glb.html): Learn how to use Gateway Load Balancers with Amazon ECS.
- [Registering multiple target groups with a service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/register-multiple-targetgroups.html): Your Amazon ECS service can serve traffic from multiple load balancers and expose multiple load balanced ports when you specify multiple target groups in a service definition.

### [Service auto scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html)

Learn how to configure your service so that Amazon ECS increases or decreases the desired number of tasks in your service automatically.

### [Target tracking](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-autoscaling-targettracking.html)

Learn how to configure your service so that Amazon ECS increases or decreases the number of tasks based on a target value for a specific metric.

- [Create a target tracking scaling policy](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/target-tracking-create-policy.html): Learn how to create a target tracking scaling policy in Amazon ECS.

### [Step scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-autoscaling-stepscaling.html)

Learn how to configure your service so that Amazon ECS increases or decreases the number of tasks based on a set of scaling adjustments, known as step adjustments, that vary based on the size of the alarm breach.

- [Create a step scaling policy](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/step-scaling-create-policy.html): Learn how to create a target tracking scaling policy in Amazon ECS.

### [Schedule scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-autoscaling-schedulescaling.html)

Learn how to configure your service so that Amazon ECS increases or decreases the number of tasks based on a the date and time.

- [Create a scheduled action](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduled-action-create-policy.html): Learn how to create a predictive scaling action for Amazon ECS.

### [Predictive scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/predictive-auto-scaling.html)

Learn how to use predictive scaling with Amazon ECS.

- [Create a predictive scaling policy](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/predictive-scaling-create-policy.html): Learn how to create a predictive scaling policy in Amazon ECS.

### [Evaluate your predictive scaling policies](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/predictive-scaling-graphs.html)

Evaluate your predictive scaling policies by reviewing the recommendations and other data.

- [Predictive auto scaling monitoring with CloudWatch](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/predictive-scaling-monitoring.html): Learn how to use CloudWatch to monitor predictive auto scaling with Amazon ECS.
- [Override the forecast](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/predictive-scaling-overriding-forecast-capacity.html): Override predictive scaling forecast values using scheduled actions.

### [Use custom metrics](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/predictive-scaling-custom-metrics.html)

Use a custom metrics configuration in an Auto Scaling predictive scaling policy.

### [Constructing the JSON for predictive scaling custom metrics with Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/predictive-scaling-custom-metrics-example.html)

Constructing JSON for predictive scaling policy custom metrics.

- [Use metric math expressions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/predictive-scaling-math-expression.html): Metric math expressions for predictive scaling policy custom metrics.

### [Interconnect services](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/interconnecting-services.html)

Learn about the options for connecting your Amazon ECS services.

### [Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html)

Learn how to use Service Connect to connect related Amazon ECS services.

- [Service Connect components](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect-concepts-deploy.html): Learn about Service Connect components.
- [Service Connect configuration overview](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect-concepts.html): Learn about Service Connect concepts.

### [Service Connect with shared namespaces](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect-shared-namespaces.html)

Learn how to use shared AWS Cloud Map namespaces with Service Connect.

- [Using shared AWS Cloud Map namespaces](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect-shared-namespaces-setup.html): Setting up shared AWS Cloud Map namespaces for Service Connect involves the following steps: Namespace owner creating the namespace, owner sharing it through AWS Resource Access Manager (AWS RAM), consumer accepting the resource share, and consumer configuring Service Connect to use the shared namespace.
- [Troubleshooting shared namespaces](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect-shared-namespaces-troubleshooting.html): Use the following information to troubleshoot issues with shared AWS Cloud Map namespaces and Service Connect.

### [Service Connect access logs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect-envoy-access-logs.html)

Learn how to configure and use access logs with Service Connect for detailed request-level observability.

- [Enabling access logs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect-access-logs-configuration.html): Access logs are not enabled by default for Amazon ECS services that use Service Connect.

### [Encrypt Service Connect traffic](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect-tls.html)

Learn how to use TLS with Service Connect.

- [Enabling TLS for Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/enable-service-connect-tls.html): Learn how to enable TLS so that you can encrypt your Amazon ECS Service Connect traffic.
- [Verifying TLS is enabled for Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/verify-tls-enabled.html): Learn how to verify TLS is enabled for Service Connect.
- [Configuring Service Connect with the AWS CLI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-service-connect.html): Learn how to create an Amazon ECS service with a Fargate task that uses Service Connect with the AWS CLI.

### [Service discovery](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html)

Learn how to connect Amazon ECS services using DNS names.

- [Creating a service that uses Service Discovery](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-service-discovery.html): Learn how to create a service containing a Fargate task that uses service discovery with the AWS CLI.

### [Amazon VPC Lattice](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-vpc-lattice.html)

Learn how to use VPC Lattice with Amazon ECS services.

- [Create a service with Amazon VPC Lattice](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-vpc-lattice-create-service.html): Learn how to create an Amazon ECS service with VPC Lattice.

### [Task scale-in protection](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-scale-in-protection.html)

Learn how to protect your Amazon ECS tasks from being terminated by scale-in events.

- [Task scale-in protection endpoint](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-scale-in-protection-endpoint.html): Learn about the Amazon ECS task scale-in protection endpoint request and response parameters.

### [Fault injection with Amazon ECS and Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fault-injection.html)

Learn how to use fault injection with your Amazon ECS and Fargate workloads.

- [Amazon ECS fault injection endpoints](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fault-injection-endpoints.html): L:earn about the Amazon ECS fault inject endpoints.

### [Update Amazon ECS service parameters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-parameters.html)

Learn which Amazon ECS service parameters you can update.

- [Updating a service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html): Learn how to update your Amazon ECS service.
- [Updating a service to use a capacity provider](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-managed-instances.html): Learn how to use an Amazon ECS capacity provider for a service.
- [Deleting a service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/delete-service-v2.html): Use the Amazon ECS console to delete a service.
- [Migrate a service short ARN](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-arn-migration.html): Learn how to migrate your Amazon ECS services to a long ARN.
- [Service throttle logic](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-throttle-logic.html): Learn how the Amazon ECS service scheduler manages task launches when tasks repeatedly fail to start.
- [Service definition parameters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service_definition_parameters.html): Learn about the service definition parameters that define how to run your Amazon ECS service.
- [Service definition template](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/sd-template.html): The following shows the JSON representation of an Amazon ECS service definition.


## [Tagging resources](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html)

- [Adding tags to resources](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/tag-resources-console.html): You can use the Amazon ECS console, you can manage the tags that are associated with new or existing tasks, services, task definitions, clusters, or container instances.
- [Tags for Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/instance-details-tags-managed-instances.html): Learn how to tag your Amazon ECS Managed Instances.
- [Adding tags to an EC2 container instance](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/instance-details-tags.html): Learn how to tag your Amazon EC2 container instances.
- [Adding tags to an External container instance](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/instance-details-tags-external.html): Learn how to tag your External container instances.
- [Usage Reports](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/usage-reports.html): Analyze your usage of your Amazon ECS resources using the Amazon ECS usage reports.


## [Monitoring](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_monitoring.html)

- [Best practices for monitoring Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/monitoring-best-practices.html): Learn about best practices for monitoring Amazon ECS.
- [Monitoring tools](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/monitoring-automated-manual.html): Configure AWS tools to monitor Amazon ECS.

### [Monitor Amazon ECS using CloudWatch](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html)

You can monitor your Amazon ECS resources using Amazon CloudWatch, which collects and processes raw data from Amazon ECS into readable, near real-time metrics.

- [Viewing Amazon ECS metrics](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/viewing_cloudwatch_metrics.html): After you have resources running in your cluster, you can view the metrics on the Amazon ECS and CloudWatch consoles.
- [Amazon ECS CloudWatch metrics](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/available-metrics.html): Learn what CloudWatch metrics are available for Amazon ECS.
- [AWS Fargate usage metrics](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/monitoring-fargate-usage.html): You can use CloudWatch usage metrics to provide visibility into your accounts usage of resources.
- [Amazon ECS cluster reservation metrics](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster_reservation.html): Learn about the Amazon ECS cluster reservation metrics;.
- [Amazon ECS cluster utilization metrics](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster_utilization.html): Learn about the Amazon ECS cluster utilization metrics;.

### [Amazon ECS service utilization metrics](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service_utilization.html)

Learn about the Amazon ECS service metrics.

- [Service utilization metrics use cases](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service_utilization-metrics-explanation.html): Learn about the Amazon ECS service metrics.

### [Automate responses to Amazon ECS errors using EventBridge](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch_event_stream.html)

Using Amazon EventBridge, you can automate your AWS services and respond automatically to system events such as application availability issues or resource changes.

### [Amazon ECS events](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_cwe_events.html)

Amazon ECS tracks the state of each of your tasks and services.

- [Container instance state change events](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_container_instance_events.html): Learn about the Amazon ECS container instance state change events.
- [Task state change events](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_task_events.html): Learn about Amazon ECS task state change events.
- [Service action events](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_service_events.html): Learn about Amazon ECS service action events.
- [Service deployment state change events](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_service_deployment_events.html): Learn about Amazon ECS service deployment state change events.
- [Handling events](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_cwet_handling.html): Learn how to handle duplicate Amazon ECS events.

### [Monitor Amazon ECS containers using Container Insights with enhanced observability](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-container-insights.html)

CloudWatch Container Insights collects, aggregates, and summarizes metrics and logs from your containerized applications and microservices.

- [Additional metrics for Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/additional-metrics-managed-instances.html): The following table lists the additional metrics available for Amazon ECS Managed Instances when using Container Insights.
- [Monitoring Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/monitoring-managed-instances.html): Learn how to monitor your Amazon ECS Managed Instances workloads using CloudWatch and Container Insights.

### [Determine task health using container health checks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/healthcheck.html)

Learn how Amazon ECS container health checks work.

- [View container health](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/view-container-health.html): Learn about the available methods for viewing Amazon ECS container health.
- [Monitor Amazon ECS container instance health](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-health.html): Learn how to monitor your Amazon ECS container instance.

### [Identify Amazon ECS optimization opportunities using application trace data](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/trace-data.html)

Amazon ECS integrates with AWS Distro for OpenTelemetry to collect trace data from your application.

- [Specifying the AWS Distro for OpenTelemetry sidecar for AWS X-Ray integration in your task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/trace-data-containerdefinitions.html): If you're not using the Amazon ECS console, you can add the AWS Distro for OpenTelemetry sidecar container to your task definition.

### [Correlate Amazon ECS application performance using application metrics](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/metrics-data.html)

Amazon ECS on Fargate supports collecting metrics from your applications running on Fargate and exporting them to either Amazon CloudWatch or Amazon Managed Service for Prometheus.

- [Exporting application metrics to Amazon CloudWatch](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/application-metrics-cloudwatch.html): Amazon ECS on Fargate supports collecting metrics from your applications running on Fargate and exporting them to Amazon CloudWatch.
- [Exporting application metrics to Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/application-metrics-prometheus.html): Amazon ECS supports exporting your task-level CPU, memory, network, and storage metrics and your custom application metrics to Amazon Managed Service for Prometheus.
- [Log Amazon ECS API calls using AWS CloudTrail](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/logging-using-cloudtrail.html): Learn about logging Amazon Elastic Container Service with AWS CloudTrail.
- [Viewing CloudWatch Logs Live Tail for Amazon ECS services and tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/monitoring-cloudwatchlogs-view.html): You can view CloudWatch Logs for your Amazon ECS services using the Amazon ECS console, the CloudWatch console, or the AWS CLI.

### [Monitor workloads using metadata](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint.html)

Amazon ECS provides various metadata for your configuration.

- [Environment variables](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-environment-variables.html): Learn about Amazon ECS environment variables..

### [Container metadata file](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-metadata.html)

Beginning with version 1.15.0 of the Amazon ECS container agent, various container metadata is available within your containers or the host container instance.

- [Turning on container metadata](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/enable-metadata.html): You can turn on container metadata at the container instance level by setting the ECS_ENABLE_CONTAINER_METADATA container agent variable to true.
- [Container metadata file format](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/metadata-file-format.html): Learn about the information available in the Amazon ECS metadata file.

### [Task metadata available for tasks on Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-metadata.html)

Learn about Amazon ECS Managed Instances task metadata.

### [Task metadata endpoint version 4 for tasks on Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint-v4-managed-instances.html)

Learn about the available Amazon ECS Managed Instances v4 task metadata.

- [Task metadata v4 JSON response for tasks on Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint-v4-managed-instances-response.html): View the JSON response for Amazon ECS Managed Instances v4 task metadata.
- [Task metadata v4 examples for tasks on Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint-v4-managed-instances-examples.html): View example responses for Amazon ECS Managed Instances v4 task metadata.

### [Task metadata available for Amazon ECS tasks on EC2](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ec2-metadata.html)

Learn about the available Amazon ECS metadata for EC2.

### [Task metadata endpoint version 4](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint-v4.html)

Learn about the available v4 task metadata.

- [Task metadata V4 JSON response](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint-v4-response.html): View the JSON response for v4 task metadata.
- [Task metadata v4 examples](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint-v4-examples.html): View the JSON example response for Amazon ECS v4 task metadata.

### [Task metadata endpoint version 3](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint-v3.html)

Learn about Amazon ECS v3 task metadata.

- [Task metadata v3 JSON response](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint-v3-response.html): View the JSON response for v3 task metadata.
- [Task metadata v3 examples](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint-v3-examples.html): View example JSON responses for v3 task metadata.
- [Task metadata endpoint version 2](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint-v2.html): The task metadata version 2 endpoint is no longer being actively maintained.

### [Task metadata available for tasks on Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-metadata.html)

Learn about Fargate task metadata.

### [Task metadata endpoint version 4 for tasks on Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint-v4-fargate.html)

Learn about the available Fargate v4 task metadata.

- [Task metadata v4 JSON response for tasks on Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint-v4-fargate-response.html): View the JSON response for Fargate v4 task metadata.
- [Task metadata v4 examples for tasks on Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint-v4-fargate-examples.html): View example responses for Fargate v4 task metadata.

### [Fargate task metadata endpoint v3](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint-v3-fargate.html)

Learn about the available Fargate v3 task metadata.

- [Task metadata v3 JSON response for tasks on Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint-v3-fargate-response.html): View the JSON response for Fargate v3 task metadata.
- [Task metadata v3 examples for tasks on Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint-fargate-example-task-metadata-response.html): View example response for Fargate v3 task metadata.
- [Container introspection](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-introspection.html): The Amazon ECS container agent provides an API operation for gathering details about the container instance on which the agent is running and the associated tasks running on that instance.

### [Identify unauthorized behavior using Runtime Monitoring](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-guard-duty-integration.html)

Runtime Monitoring in GuardDuty is an intelligent threat detection service that protects workloads running on Fargate and EC2 container instances by continuously monitoring AWS log and networking activity to identify malicious or unauthorized behavior.

### [Runtime Monitoring for Fargate workloads](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-guard-configure-automatic.html)

For the Fargate, GuardDuty can manage Runtime Monitoring.

- [Turning on Runtime Monitoring](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-guard-duty-configure-automatic-guard-duty.html): learn how to turn on Runtime Monitoring for all your Fargate clusters.
- [Adding Runtime Monitoring to existing Fargate tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-guard-duty-configure-automatic-existing-tasks.html): Learn how to turn on Runtime Monitoring for all your existing Fargate tasks.
- [Removing Runtime Monitoring from a cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-guard-duty-manage-subset-automatic.html): Learn how to remove Runtime Monitoring from an Amazon ECS cluster.
- [Removing Runtime Monitoring from an account](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-guard-duty-manage-remove-automatic.html): Learn how to turn off Runtime Monitoring for your account.

### [Runtime Monitoring for EC2 workloads](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-guard-duty-configure-manual.html)

Learn how to manually manage Runtime Monitoring.

- [Turning on Runtime Monitoring](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-guard-duty-configure-manual-guard-duty.html): learn how to turn on Runtime Monitoring for Amazon ECS clusters with EC2 container instances.
- [Adding Runtime Monitoring to a cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-guard-duty-configure-manual-customize.html): Learn how to turn on Runtime Monitoring for a cluster.
- [Adding Runtime Monitoring to existing tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-guard-duty-configure-manual-existing-tasks.html): Learn how to turn on Runtime Monitoring for all your existing Fargate tasks.
- [Removing Runtime Monitoring from a cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-guard-duty-remove-manual.html): Learn how to remove Runtime Monitoring from an Amazon ECS cluster.
- [Updating the GuardDuty security agent](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-guard-duty-manage-update-agent.html): Learn how to update the GuardDuty security agent on your Amazon ECS container instances.
- [Removing Runtime Monitoring from an account](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-guard-duty-manage-remove-protection-manual.html): Learn how to turn off Runtime Monitoring for your account.
- [Troubleshooting Runtime Monitoring](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-guard-duty-troubleshooting.html): Troubleshoot Runtime Monitoring issues.

### [Monitor Amazon ECS containers with ECS Exec](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html)

You can use Amazon ECS Exec to collect diagnostic information related to your containers and troubleshoot errors that are encountered throughout the lifecycle of your containers.

- [Running commands using ECS Exec](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec-run.html): Learn how to run commands using ECS Exec.
- [Compute Optimizer recommendations](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-recommendations.html): ECS; usage recommendations from Compute Optimizer


## [Amazon ECS MCP server](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-mcp-introduction.html)

- [Getting started](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-mcp-getting-started.html): Learn how to set up and use the Amazon ECS MCP Server with your AI code assistants.
- [Tool configurations](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-mcp-tool-configurations.html): Learn about all the configurations available for the fully managed Amazon ECS MCP Server.


## [Troubleshooting](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/troubleshooting.html)

### [Resolve stopped task errors](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/resolve-stopped-errors.html)

Resolve issues for stopped tasks error codes and Amazon ECS.

- [Stopped task error messages updates](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/stopped-tasks-error-messages-updates.html): Learn about the changes to Amazon ECS stopped task error message updates
- [Viewing stopped task errors](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/stopped-task-errors.html): Learn how to view Amazon ECS stopped task errors

### [Stopped tasks error messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/stopped-task-error-codes.html)

Resolve issues for stopped tasks errors and Amazon ECS.

- [TaskFailedToStart errors](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/failed-to-start-error.html): Learn how to diagnose Fargate TaskFailed to start errors in Amazon ECS.
- [ResourceInitializationError errors](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/resource-initialization-error.html): Learn how to diagnose ResourceInitializationError errors
- [ResourceNotFoundException errors](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/resource-not-found-error.html): Learn how to diagnose ResourceNotFoundException errors
- [SpotInterruption errors](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/spot-interruption-errors.html): Learn how to diagnoseSpot interruption errors
- [InternalError errors](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/internal-error.html): Learn how to diagnose Internalerror errors
- [OutOfMemoryError errors](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/out-of-memory.html): Learn how to diagnose OutOfMemoryError errors
- [ContainerRuntimeError errors](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-runtime-error.html): Learn how to diagnose Fargate ContainerRuntimeError errors
- [ContainerRuntimeTimeoutError errors](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-runtime-timeout-error.html): Learn how to diagnose ContainerRuntimeTimeoutError errors
- [CannotStartContainerError errors](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cannot-start-container.html): Learn how to diagnose CannotStartContainerError errors
- [CannotStopContainerError errors](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cannot-stop-container.html): Learn how to diagnose Fargate CannotStopContainerError errors
- [CannotInspectContainerError errors](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cannot-inspect-container.html): Learn how to diagnose Fargate CannotInspectContainerError errors.
- [CannotCreateVolumeError errors](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cannot-create-volume.html): Learn how to diagnose CannotCreateVolumeError errors
- [CannotPullContainer task errors](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_cannot_pull_image.html): Learn how to resolve Amazon ECS stopped tasks with CannotPullContainer task errors.
- [Verifying task connectivity](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/verify-connectivity.html): Learn how to resolve task connectivity issues.
- [Viewing IAM role requests](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_iam_roles-logs.html): Learn how to view the Amazon ECS task role information.

### [Viewing service event messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages.html)

Learn how to view Amazon ECS service event messages and what they mean.

- [Amazon ECS service event messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html): Learn how to resolve Amazon ECS service event messages.
- [Amazon ECS service unhealthy event messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-unhealthy-event-messages.html): Learn about Amazon ECS service unhealthy event messages that include task IDs.
- [Amazon ECS Availability Zone service rebalancing service event messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-rebalancing-event-messages-list.html): Learn how to resolve Amazon ECS Availability Zone rebalancing events.
- [Troubleshooting service load balancers in Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/troubleshoot-service-load-balancers.html): Resolve issues with service load blancers and Amazon ECS.
- [Troubleshooting service auto scaling in Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/troubleshoot-service-auto-scaling.html): Resolve issues for service auto scaling and Amazon ECS.

### [Event capture](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-lifecycle-events.html)

Capture and query Amazon ECS-generated events using EventBridge and Amazon CloudWatch Logs for monitoring and troubleshooting.

- [Turn on event capture for an existing cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/turn-on-event-capture-existing-cluster.html): Enable event capture on an existing Amazon ECS cluster to monitor task lifecycle events and service actions.
- [Viewing service and task state change events](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/viewing-state-events.html): Learn how to view your Amazon ECS service and task state change events.
- [Troubleshoot task definition invalid CPU or memory errors](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-cpu-memory-error.html): Learn how to resolve Amazon ECS task definition invalid CPU and memory errors.
- [Viewing container agent logs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/logs.html): Learn how to view the Amazon ECS ecs-init log file.
- [Collecting container logs with Amazon ECS logs collector](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-logs-collector.html): Amazon ECS logs collector
- [Agent introspection](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/introspection-diag.html): Use Amazon ECS agent introspection to retrieve diagnostic information.
- [Docker diagnostics in Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-diags.html): Docker diagnostics and Amazon ECS.
- [Configuring verbose output from the Docker daemon in Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-debug-mode.html): Resolve issues with Docker debug and Amazon ECS.
- [Troubleshoot the Docker API error (500): devmapper in Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/CannotCreateContainerError.html): Troubleshoot Amazon ECS CannotCreateContainerError.
- [Troubleshoot ECS Exec issues](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec-troubleshooting.html): Troubleshoot ECS Exec issues.
- [Troubleshoot Amazon ECS Anywhere issues](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere-troubleshooting.html): Learn how to resolve issues for Amazon ECS Anywhere.
- [Troubleshoot Java class loading issues on Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-java-class-loading.html): Learn how to resolve Java class loading issues that can occur on Fargate after platform updates.
- [AWS Fargate throttling quotas](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/throttling.html): AWS Fargate throttling quotas.

### [Troubleshooting Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/troubleshooting-managed-instances-complete.html)

Comprehensive troubleshooting procedures for Amazon ECS Managed Instances, including common issues, diagnostic techniques, and resolution steps.

- [Troubleshooting Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/troubleshooting-managed-instances.html): Troubleshoot common issues with Amazon ECS Managed Instances.
- [Amazon ECS Managed Instances errors](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-errors.html): Learn how to diagnose Amazon ECS Managed Instances errors in Amazon ECS.
- [API failure reasons](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/api_failures_messages.html): Learn about the Amazon ECS API failure reasons.
- [Troubleshooting with Amazon Q Developer](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/troubleshooting-with-Q.html): Use Amazon Q Developer to troubleshoot Amazon ECS issues in the console.


## [Security](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security.html)

### [Identity and Access Management](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-iam.html)

How to authenticate requests and manage access your Amazon ECS resources.

- [How Amazon Elastic Container Service works with IAM](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_service-with-iam.html): Learn how to use IAM for Amazon ECS
- [Identity-based policy examples](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_id-based-policy-examples.html): Learn how to configure IAM policies for Amazon ECS.

### [AWS managed policies for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-iam-awsmanpol.html)

Learn about AWS managed policies for Amazon ECS and recent changes to those policies.

- [AWS managed policies that are phased out for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-iam-awsmanpol-deprecated-policies.html): Learn about phased out AWS managed IAM policies for Amazon ECS.
- [Migrating to AmazonECS_FullAccess](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-iam-awsmanpol-amazonecs-full-access-migration.html): Learn how to migrate to the AmazonECS_FullAccess managed policy.

### [Using service-linked roles](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html)

How to use service-linked roles to give Amazon ECS access to resources in your AWS account.

- [Allow Amazon ECS to manage clusters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles-for-clusters.html): How to use service-linked roles to give Amazon ECS access to resources in your AWS account.
- [Allow Amazon ECS to manage Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles-instances.html): How to use service-linked roles to give Amazon ECS access to resources in your AWS account.

### [IAM roles for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-ecs-iam-role-overview.html)

Learn about the IAM roles that are used in Amazon ECS.

- [Best practices for IAM roles](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-iam-roles.html): These are the security best practices for IAM roles in Amazon ECS.
- [Task execution IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html): Learn when to use a task execution AWS Identity and Access Management (IAM) role and how to create and use such a role.
- [Task IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html): Learn when to use a task AWS Identity and Access Management (IAM) role and how to create and use such a role.
- [Container instance IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/instance_IAM_role.html): Learn when to use a container instance AWS Identity and Access Management (IAM) role and how to create and use such a role.
- [Amazon ECS Anywhere IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/iam-role-ecsanywhere.html): Learn when to use an Amazon ECS Anywhere AWS Identity and Access Management (IAM) role and how to create and use such a role.
- [Infrastructure IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/infrastructure_IAM_role.html): Learn when to use an Amazon ECS infrastructure AWS Identity and Access Management (IAM) role and how to create and use such a role.
- [Amazon ECS Managed Instances instance profile](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-instance-profile.html): Learn about the IAM instance profile used by Amazon ECS Managed Instances and how it provides the necessary permissions for container operations and infrastructure management.
- [Infrastructure IAM role for load balancers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AmazonECSInfrastructureRolePolicyForLoadBalancers.html): Learn about the Amazon ECS infrastructure IAM role for load balancers and how to create and use such a role.
- [CodeDeploy IAM Role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/codedeploy_IAM_role.html): Learn when to use a CodeDeploy AWS Identity and Access Management (IAM) role and how to create and use such a role.
- [EventBridge IAM Role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/CWE_IAM_role.html): Learn when to use a EventBridge AWS Identity and Access Management (IAM) role and how to create and use such a role.

### [Permissions required for the Amazon ECS console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/console-permissions.html)

Learn about the permissions required for the Amazon ECS console.

- [Permissions required for the Amazon ECS console with CloudFormation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudformation-console-permissions.html): Learn about the permissions required for the Amazon ECS console with CloudFormation.
- [Permissions required for Lambda functions in Amazon ECS blue/green deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/blue-green-permissions.html): Learn about the permissions required for Amazon ECS blue/green deployments.
- [IAM permissions required for Amazon ECS service auto scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/auto-scaling-IAM.html): Learn about the permissions required for Amazon ECS Service Auto Scaling.

### [Tag resources during creation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/supported-iam-actions-tagging.html)

Create IAM policies to allow users to tag Amazon ECS resources on creation.

- [Control access to Amazon ECS resources using resource tags](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/control-access-with-tags.html): Use resource tags in your IAM policies to control access to your Amazon ECS resources.
- [Example policies](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/iam-policies-ecs-console.html): Learn how to grant IAM users permissions to view and work with specific resources in the Amazon ECS console.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security_iam_troubleshoot.html): Learn about IAM issues with Amazon ECS.
- [IAM best practices](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-iam-bestpractices.html): These are the security best practices for IAM used for Amazon ECS.
- [Logging and Monitoring](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-logging-monitoring.html): Tools in Amazon ECS for monitoring resources and responding to incidents.

### [Compliance validation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-compliance.html)

Learn what AWS services are in scope of a specific compliance program.

- [Compliance and security best practices](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-compliance.html): These are the compliance best practices for Amazon ECS that you should be mindful of when using Amazon ECS in a production environment.
- [AWS Fargate FIPS-140 compliance](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-fips-compliance.html): Learn about AWS Fargate FIPS-140 compliance.

### [Infrastructure Security](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/infrastructure-security.html)

Learn how Amazon Elastic Container Service isolates service traffic.

- [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/vpc-endpoints.html): You can use a VPC endpoint to create a private connection between your VPC and Amazon ECS without requiring access over the internet or through a NAT instance, a VPN connection, or Direct Connect.
- [Shared responsibility model](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-shared-model.html): Learn about the shared responsibility model for Amazon ECS.
- [Amazon ECS Managed Instances shared responsibility](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-shared-model-managed-instances.html): Learn about the shared responsibility model for Amazon ECS Managed Instances.
- [Network security best practices](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-network.html): These are the security best practices for network security in Amazon ECS that you should be mindful of when using Amazon ECS in a production environment.
- [Task and container security best practices](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-tasks-containers.html): Learn about the best practices for Amazon ECS task and container security.


## [Tutorials](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-tutorials.html)

- [Creating a Linux task for Fargate with the AWS CLI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_AWSCLI_Fargate.html): Learn how to create a Fargate cluster using the AWS CLI.
- [Creating a Windows task for the Fargate with the AWS CLI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_AWSCLI_Fargate_windows.html): Complete these steps with the AWS CLI to run IIS in a container on Windows on Fargate without any EC2 instances.
- [Creating a task for EC2 with the AWS CLI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_AWSCLI_EC2.html): Learn how to set up a cluster, register a task definition, run a task, and perform other common scenarios in Amazon ECS with the AWS CLI.
- [Configuring Amazon ECS to listen for CloudWatch Events events](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_cwet.html): Learn how to set up a simple AWS Lambda function that listens for Amazon ECS task events and writes them out to a CloudWatch Logs log stream.
- [Sending Amazon Simple Notification Service alerts for task stopped events](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_cwet2.html): Learn how to configure an Amazon EventBridge event rule that only captures task events where the task has stopped running because one of its essential containers has terminated.
- [Concatenating multiline or stack-trace log messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/firelens-concatanate-multiline.html): The multiline filter helps concatenate log messages that originally belong to one context but were split across multiple records or log lines.
- [Deploying Fluent Bit on Windows containers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/tutorial-deploy-fluentbit-on-windows.html): Learn how to use Fluent Bit on Amazon ECS.
- [Using gMSA for EC2 Linux containers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/linux-gmsa.html): Learn how to use group Managed Service Account with Linux containers on EC2.
- [Using gMSA for Linux containers on Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-linux-gmsa.html): Learn how to use group Managed Service Account with Linux containers on Fargate.
- [Using Windows containers with domainless gMSA using the AWS CLI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/tutorial-gmsa-windows.html): Complete these steps with the AWS CLI to run IIS in a container on Windows with Active Directory credentials on an EC2 instance.
- [Learn how to use gMSAs for EC2 Windows containers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/windows-gmsa.html): Learn how to use gMSAs for Windows Containers on Amazon EC2 in Amazon ECS.
- [Using Image Builder to build customized Amazon ECS-optimized AMIs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/image-builder-tutorial.html): You can use EC2 Image Builder for the creation, management, and deployment of your custom Amazon ECS-optimized AMIs server images.
- [Using AWS Deep Learning Containers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deep-learning-containers.html): Learn how to use deep lerning instances with Amazon ECS
- [Tutorial: Creating a Service Using a Blue/Green Deployment](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-blue-green.html): Amazon ECS has integrated blue/green deployments into the Create Service wizard on the Amazon ECS console.


## [Service quotas](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-quotas.html)

- [Managing your service quotas in the AWS Management Console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-quotas-manage.html): Learn how to manage your Amazon ECS and Fargate quotas.
- [Handle service quotas and API throttling limits](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/operating-at-scale-service-quotas.html): Learn about the best practices for Amazon ECS service quotas and API throttling.
