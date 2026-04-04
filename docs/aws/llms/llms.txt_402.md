# Source: https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/llms.txt

# Amazon File Cache File Cache User Guide

> This is the official Amazon Web Services documentation for Amazon File Cache. Amazon File Cache is an AWS service that makes it easier to launch and run is a high-speed cache in the AWS Cloud and link to data repositories that are on premises or in the AWS Cloud. The Amazon File Cache User Guide describes key concepts for Amazon File Cache and provides instructions for launching and using your cache.

- [What is Amazon File Cache?](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/what-is.html)
- [Setting up](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/setting-up.html)
- [Performance](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/performance.html)
- [Quotas](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/limits.html)
- [Document history](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/doc-history.html)

## [Getting started](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/getting-started.html)

- [Prerequisites](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/prerequisites.html): To perform this getting started exercise, you'll need the following:
- [Step 1: Create your cache](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/getting-started-step1.html): Next, you create your cache.
- [Step 2: Install the Lustre client](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/getting-started-step2.html): To mount your cache from your Amazon EC2 instance, first install the Lustre 2.12 client.
- [Step 3: Run your analysis](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/getting-started-step3.html): Now that your cache is created and mounted to a compute instance, you can use it to run your high-performance compute workload.
- [Step 4: Clean up resources](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/getting-started-step4.html): After you finish this exercise, we recommend that you follow these steps to clean up your resources and protect your AWS account.


## [Using data repositories](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/using-data-repositories.html)

### [Overview of data repositories](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/overview-data-repo.html)

Overview of using data repositories for durable data storage with Amazon File Cache.

- [POSIX Metadata Support](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/posix-metadata-support.html): Amazon File Cache automatically transfers Portable Operating System Interface (POSIX) metadata for files, directories, and symbolic links (symlinks) when importing and exporting data to and from a linked Amazon S3 or NFS data repository.
- [Attaching POSIX permissions to an S3 bucket](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/attach-s3-posix-permissions.html): How to attach POSIX permissions when uploading objects to an Amazon S3 bucket for use with Amazon File Cache.
- [NFS on-premises prerequisites](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/nfs-filer-prereqs.html): Before you can link your cache to an on-premises NFS data store, verify that your resources and configurations meet the following requirements:

### [Linking your cache to a data repository](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/create-linked-data-repo.html)

You can link your Amazon File Cache to data repositories in Amazon S3 or on NFS (Network File System) file systems that support the NFSv3 protocol.

- [Creating a link to a data repository](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/create-linked-repo.html): The following procedure walks you through the process of creating a data repository association (DRA) while creating an Amazon File Cache resource, using the AWS Management Console.
- [Working with server-side encrypted Amazon S3 buckets](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/s3-server-side-encryption-support.html): Amazon File Cache supports Amazon Simple Storage Service (Amazon S3) buckets that use server-side encryption with S3-managed keys (SSE-S3), and with AWS Key Management Service (AWS KMS) stored in AWS KMS (SSE-KMS).

### [Importing files from your data repository](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/importing-files.html)

When you create a Amazon File Cache resource, you can create a data repository association (DRA) to link your cache to an Amazon S3 or NFS data repository.

- [Lazy load](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/mdll-lazy-load.html): When you access data on a linked Amazon S3 or NFS data repository using the cache, Amazon File Cache automatically loads the metadata (the name, ownership, timestamps, and permissions) and file contents if they're not already present in the cache.
- [Preloading files into your cache](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/preload-file-contents-hsm.html): If the data you're accessing doesn't already exist in the cache, Amazon File Cache copies the data from your Amazon S3 or NFS data repository into the cache in line with file access.

### [Exporting changes to the data repository](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/export-changed-data.html)

You can export data and metadata changes, including POSIX metadata, from Amazon File Cache to a linked Amazon S3 or NFS data repository.

- [Exporting files using HSM commands](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/exporting-files-hsm.html): To export an individual file to your data repository and verify the success of the export, run the following commands.
- [Cache eviction](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/cache-eviction.html): Files can be evicted (released) from the cache to free up space for new files.


## [Accessing caches](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/accessing-caches.html)

- [Installing the Lustre client](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/install-lustre-client.html): Mount your cache by first installing the open-source Lustre client on your compute instance, including Amazon Linux, CentOS, Red Hat, Rocky Linux, and Ubuntu.
- [Mount from Amazon EC2](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/mounting-ec2-instance.html): You can mount your cache from an Amazon EC2 instance.
- [Mounting from Amazon ECS](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/mounting-ecs.html): You can access your cache from an Amazon Elastic Container Service (Amazon ECS) Docker container on an Amazon EC2 instance.
- [Mounting from on-premises or another VPC](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/mounting-on-premises.html): You can access your cache in two ways.
- [Mounting Amazon File Cache automatically](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/mount-fs-auto-mount-onreboot.html): How to mount your cache automatically.
- [Mounting specific filesets](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/mounting-from-fileset.html): Using the Lustre fileset feature.
- [Unmounting caches](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/unmounting-fs.html): Unmount a cache.
- [Using EC2 Spot Instances](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/working-with-ec2-spot-instances.html): Considerations for working with Amazon EC2 Spot Instances in FSx for Lustre.


## [Managing resources](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/managing-resources.html)

- [Managing caches](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/managing-caches.html): How to create, update, list, and delete Amazon File Cache cache resources.
- [Storage quotas](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/lustre-quotas.html): Limit the amount of disk space that a user or a group can consume by creating storage quotas on Amazon File Cache caches.
- [Tag your resources](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/tag-resources.html): Working with tags to create metadata for your Amazon File Cache resources.
- [Maintenance](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/maintenance-windows.html): Describes what maintenance windows are and how to use them.


## [Monitoring caches](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/monitoring_overview.html)

### [Monitoring with CloudWatch](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/monitoring-cloudwatch.html)

You can monitor caches using Amazon CloudWatch, which collects and processes raw data from Amazon File Cache into readable, near real-time metrics.

- [Front-end I/O metrics](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/frontend-io-metrics.html): The following metrics report cache-level information on system read and write operations.
- [Backend I/O metrics](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/backend-io-metrics.html): The following metrics report information on read and write operations between the cache and its linked data repository.
- [Cache utilization metrics](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/utilization-metrics.html): The following metrics report cache-level storage information.
- [How to use Amazon File Cache metrics](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/how_to_use_metrics.html): The metrics reported by Amazon File Cache provide information that you can analyze in different ways.
- [Accessing CloudWatch metrics](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/accessingmetrics.html): You can see Amazon File Cache metrics for Amazon CloudWatch Logs in many ways.
- [Creating alarms](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/creating_alarms.html): You can create an Amazon CloudWatch Logs alarm that sends an Amazon SNS message when the alarm's state changes.
- [Logging with AWS CloudTrail](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/logging-using-cloudtrail.html): Learn about logging Amazon File Cache with AWS CloudTrail.


## [Security](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/security.html)

### [Data protection](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon File Cache.

### [Data encryption](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/encryption.html)

Amazon File Cache supports two forms of data encryption for caches, encryption of data at rest and encryption in transit.

- [Encrypting data at rest](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/encryption-at-rest.html): Encryption of data at rest is automatically enabled when you create an Amazon File Cache resource through the AWS Management Console, the AWS CLI, or programmatically through the AWS API or one of the AWS SDKs.
- [Encrypting data in transit](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/encryption-in-transit.html): Encryption of data in transit is automatically enabled when you access an Amazon File Cache resource from compute instances that support encryption in transit.
- [AWS KMS key management](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/FileCacheKMS.html): Amazon File Cache integrates with AWS Key Management Service (AWS KMS) for key management for encrypting data at rest.
- [Internetwork traffic privacy](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/internetwork-privacy.html): Describes how Amazon File Cache secures connections from the service to other locations.

### [Identity and Access Management](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/security-iam.html)

How to authenticate requests and manage access to your File Cache resources.

- [How Amazon File Cache works with IAM](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/security_iam_service-with-iam.html): Before you use IAM to manage access to File Cache, learn what IAM features are available to use with File Cache.
- [Identity-based policy examples](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify File Cache resources.
- [AWS managed policies](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon FSx and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with File Cache and IAM.
- [Using tags with Amazon File Cache](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/using-tags.html): Learn which Amazon File Cache permissions are required to apply tags to resources during resource creation.
- [Using service-linked roles](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/using-service-linked-roles.html): How to use service-linked roles to give Amazon FSx access to resources in your AWS account.
- [Cache access control with Amazon VPC](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/limit-access-security-groups.html): A cache is accessible through an elastic network interface that resides in the virtual private cloud (VPC) based on the Amazon VPC service that you associate with your cache.
- [Amazon VPC Network ACLs](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/limit-access-acl.html): Another option for securing access to the cache within your VPC is to establish network access control lists (network ACLs).
- [Compliance Validation](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/filecache-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Interface VPC endpoints](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/vpc-endpoints.html): You can use interface VPC endpoints (AWS PrivateLink) to access the AWS API from your VPC without sending traffic over the internet.


## [Troubleshooting](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/troubleshooting.html)

- [Cache mount fails](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/mount-troubleshooting.html): There are a number of potential causes when a cache mount command fails, as described in the following topics.
- [File access issues](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/file-access-issues.html): There are a number of potential causes for being unable to access files.
- [CSI driver issues](https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/csi-driver-issues.html): If youâre experiencing issues with the Amazon File Cache CSI driver for containers running on Amazon EKS, see Troubleshooting CSI Driver (Common Issues) which is available on GitHub.
