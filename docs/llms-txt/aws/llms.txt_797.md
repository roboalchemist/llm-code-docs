# Source: https://docs.aws.amazon.com/snowball/latest/developer-guide/llms.txt

# AWS Snowball Edge Developer Guide 

- [AWS Snowball Edge availability change](https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-availability-change.html)
- [How Snowball Edge Works](https://docs.aws.amazon.com/snowball/latest/developer-guide/how-it-works.html)
- [Long-term pricing for Snowball Edge devices](https://docs.aws.amazon.com/snowball/latest/developer-guide/pricing.html)
- [Shipping considerations](https://docs.aws.amazon.com/snowball/latest/developer-guide/shipping.html)
- [Configuring and using the Snowball Edge Client](https://docs.aws.amazon.com/snowball/latest/developer-guide/using-client-commands.html)
- [Managing the NFS interface](https://docs.aws.amazon.com/snowball/latest/developer-guide/shared-using-nfs.html)
- [Using AWS IoT Greengrass on EC2-compatible instances](https://docs.aws.amazon.com/snowball/latest/developer-guide/using-green-grass.html)
- [Using AWS Lambda](https://docs.aws.amazon.com/snowball/latest/developer-guide/using-lambda.html)
- [Using IAM locally](https://docs.aws.amazon.com/snowball/latest/developer-guide/using-local-iam.html)
- [Using AWS STS](https://docs.aws.amazon.com/snowball/latest/developer-guide/using-sts.html)
- [Managing public key certificates](https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-certificates-cli.html)
- [Port requirements for AWS services](https://docs.aws.amazon.com/snowball/latest/developer-guide/port-requirements.html)
- [Using Snowball Edge Device Management to manage devices](https://docs.aws.amazon.com/snowball/latest/developer-guide/aws-sdm.html)
- [Best practices](https://docs.aws.amazon.com/snowball/latest/developer-guide/BestPractices.html)
- [Data validation](https://docs.aws.amazon.com/snowball/latest/developer-guide/validation.html)
- [Notifications](https://docs.aws.amazon.com/snowball/latest/developer-guide/notifications.html)
- [Logging with AWS CloudTrail](https://docs.aws.amazon.com/snowball/latest/developer-guide/logging-using-cloudtrail.html)
- [Document history](https://docs.aws.amazon.com/snowball/latest/developer-guide/doc-history.html)

## [What is Snowball Edge?](https://docs.aws.amazon.com/snowball/latest/developer-guide/whatisedge.html)

- [Device hardware information](https://docs.aws.amazon.com/snowball/latest/developer-guide/device-differences.html): Compare the configuration options for Snowball Edge devices, including Snowball Edge storage-optimized and Snowball Edge compute-optimized devices.
- [Prerequisites for using Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-prereqs.html): Before using a Snowball Edge, you will need an AWS account, an administrative IAM user, and to understand prerequisties for using a Snowball Edge with other AWS services.


## [Getting started](https://docs.aws.amazon.com/snowball/latest/developer-guide/getting-started.html)

- [Creating a job to order a Snowball Edge device](https://docs.aws.amazon.com/snowball/latest/developer-guide/create-job-common.html): Create a job in the AWS Snow Family Management Console to order a Snowball Edge device.
- [Cancelling a job](https://docs.aws.amazon.com/snowball/latest/developer-guide/cancel-job-order.html): Cancel the job to not receive a Snowball Edge.
- [Cloning a job to order a Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/clonejob.html): Create additional import jobs or local compute and storage jobs in the AWS Snow Family Management Console by cloning an existing job.
- [Receiving the Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/receive-device.html): Inspect your Snowball Edge device for any obvious damage or tampering.
- [Unlocking the Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/unlockdevice.html): Unlock the Snowball Edge using the Snowball Edge Client.
- [Rebooting the Snowball Edge device](https://docs.aws.amazon.com/snowball/latest/developer-guide/reboot.html): Learn how to reboot a Snowball Edge using the device's power button or a CLI command.
- [Powering off the Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/turnitoff.html): Turn off the AWS Snowball Edge device and prepare it for its return trip to AWS.
- [Returning the device](https://docs.aws.amazon.com/snowball/latest/developer-guide/return-device.html): Use the shipping information on the E Ink display to return the AWS Snowball Edge device to AWS.
- [Return shipping](https://docs.aws.amazon.com/snowball/latest/developer-guide/mailing-storage.html): Find information about shipping your AWS Snowball Edge device, including the supported carriers by region.
- [Monitoring the import status](https://docs.aws.amazon.com/snowball/latest/developer-guide/monitor-status.html): Monitor the status of your AWS Snowball Edge device import job.
- [Getting job completion report and logs](https://docs.aws.amazon.com/snowball/latest/developer-guide/report.html): Get a downloadable PDF job report for data imported into or exported out of Amazon S3 with a Snowball Edge.


## [Large data migration](https://docs.aws.amazon.com/snowball/latest/developer-guide/LargeDataMigration.html)

- [Calibrating a large data transfer](https://docs.aws.amazon.com/snowball/latest/developer-guide/calibrating-large-transfer.html): Information about how to carry out a proof-of-concept to calibrate the data transfer performance of your environment in preparation for large data migration.
- [Creating a large data migration plan](https://docs.aws.amazon.com/snowball/latest/developer-guide/create-data-migration-plan.html): Steps to use the AWS Snow Family Management Console to create a large data migration plan to track, monitor, and manage your large data migration.
- [Using the large data migration plan](https://docs.aws.amazon.com/snowball/latest/developer-guide/understanding-data-migration-plan.html): Steps to use the schedule and dashboard in a large data migration plan to guide your large data migration.


## [Using AWS OpsHub to Manage Devices](https://docs.aws.amazon.com/snowball/latest/developer-guide/aws-opshub.html)

- [Downloading AWS OpsHub](https://docs.aws.amazon.com/snowball/latest/developer-guide/download-OpsHub-for-snow-family.html)
- [Unlocking a device](https://docs.aws.amazon.com/snowball/latest/developer-guide/connect-unlock-device.html): Unlock your Snowball Edge using AWS OpsHub.
- [Verifying the signature of AWS OpsHub](https://docs.aws.amazon.com/snowball/latest/developer-guide/verify-signature.html): Verify the PGP signature of the AWS OpsHub application.

### [Managing AWS services](https://docs.aws.amazon.com/snowball/latest/developer-guide/manage-services.html)

Use AWS OpsHub to manage local Snowball services, including Amazon EC2-compatible instances, Amazon S3 storage, and Amazon EBS volumes.

- [Launching an Amazon EC2-compatible instance](https://docs.aws.amazon.com/snowball/latest/developer-guide/launch-instance.html): Steps to launch an Amazon EC2-compatible instance on a Snowball Edge with AWS OpsHub.
- [Stopping an Amazon EC2-compatible instance](https://docs.aws.amazon.com/snowball/latest/developer-guide/stop-instance.html): Steps to stop an Amazon EC2-compatible instance on a Snowball Edge with AWS OpsHub.
- [Starting an Amazon EC2-compatible instance](https://docs.aws.amazon.com/snowball/latest/developer-guide/start-instance.html): Steps to start an Amazon EC2-compatible instance using AWS OpsHub.
- [Working with key pairs](https://docs.aws.amazon.com/snowball/latest/developer-guide/working-with-key-pair.html): Steps to create, import, or manage key paris for an Amazon EC2-compatible instance using AWS OpsHub.
- [Terminating an Amazon EC2-compatible instance](https://docs.aws.amazon.com/snowball/latest/developer-guide/terminate-instance.html): Steps to terminate an Amazon EC2-compatible instance using AWS OpsHub.
- [Managing EBS volumes](https://docs.aws.amazon.com/snowball/latest/developer-guide/manage-ebs-volumes.html): Steps to create an Amazon EBS storage volume and attach it to an Amazon EC2-compatible instance using AWS OpsHub
- [Importing an image into your device as an Amazon EC2-compatible AMI](https://docs.aws.amazon.com/snowball/latest/developer-guide/ec2-ami-import.html): Import an Amazon Machine Image from and external source to a Snowball Edge using AWS OpsHub.
- [Deleting a snapshot](https://docs.aws.amazon.com/snowball/latest/developer-guide/delete-snapshot.html): Steps to delete a snapshot from a Snowball Edge using AWS OpsHub.
- [Deregistering an AMI](https://docs.aws.amazon.com/snowball/latest/developer-guide/deregister-ami.html): Steps to deregister an Amazon EC2-compatible AMI on a Snowball Edge using AWS OpsHub.
- [Managing clusters](https://docs.aws.amazon.com/snowball/latest/developer-guide/manage-clusters.html): Create and manage an Amazon EC2 cluster using AWS OpsHub.
- [Set up Amazon S3 compatible storage on Snowball Edge with AWS OpsHub](https://docs.aws.amazon.com/snowball/latest/developer-guide/s3-edge-snow-opshub.html): Set up Amazon S3 compatible storage on Snowball Edge using AWS OpsHub.
- [Managing S3 storage](https://docs.aws.amazon.com/snowball/latest/developer-guide/manage-s3.html): Create and manage Amazon S3 storage on Snowball Edge using AWS OpsHub.
- [Managing the NFS interface](https://docs.aws.amazon.com/snowball/latest/developer-guide/manage-nfs.html): Managing the NFS interface on Snowball Edge.
- [Rebooting the device](https://docs.aws.amazon.com/snowball/latest/developer-guide/reboot-device.html): Steps to reboot a Snowball Edge using AWS OpsHub.
- [Shutting down the device](https://docs.aws.amazon.com/snowball/latest/developer-guide/shutdown-device.html): Steps to shut down a Snowball Edge with AWS OpsHub.
- [Editing the device alias](https://docs.aws.amazon.com/snowball/latest/developer-guide/edit-device-alias.html): Steps to change the alias of a Snowball Edge with AWS OpsHub.
- [Managing public key certificates using OpsHub](https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-certificates-opshub.html): Steps to download or renew the public key certificate of a Snowball Edge with AWS OpsHub.
- [Getting device updates](https://docs.aws.amazon.com/snowball/latest/developer-guide/get-updates.html): Steps to check for and download updates for a Snowball Edge with AWS OpsHub.
- [Updating AWS OpsHub](https://docs.aws.amazon.com/snowball/latest/developer-guide/update-opshub.html): Steps to automatically update AWS OpsHub to the latest version.
- [Automating your management tasks with AWS OpsHub](https://docs.aws.amazon.com/snowball/latest/developer-guide/automate-task.html): Automate your device management tasks using AWS OpsHub.
- [Setting the NTP time servers for the device](https://docs.aws.amazon.com/snowball/latest/developer-guide/setting-ntp.html): Setting up NTP time server.


## [Transferring files using the S3 adapter](https://docs.aws.amazon.com/snowball/latest/developer-guide/using-adapter.html)

- [Batching small files](https://docs.aws.amazon.com/snowball/latest/developer-guide/batching-small-files.html): Batch together small files that you want to transfer to Amazon S3 using an AWS Snowball Edge device.
- [Supported AWS CLI commands for data transfer](https://docs.aws.amazon.com/snowball/latest/developer-guide/using-adapter-cli.html): Use AWS CLI commands to transfer data to the AWS Snowball Edge device using the Amazon S3 adapter or Amazon S3 compatible storage on Snowball Edge.
- [Supported Amazon S3 REST API actions for data transfer](https://docs.aws.amazon.com/snowball/latest/developer-guide/using-adapter-supported-api.html): Use REST API actions with an AWS Snowball Edge device.


## [Using Amazon EC2-compatible compute instances](https://docs.aws.amazon.com/snowball/latest/developer-guide/using-ec2.html)

- [Using AMIs on Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/using-ami.html): Add and use Amazon Machine Images (AMI) on your Snowball Edge.
- [Importing a VM image to a Snowball Edge device](https://docs.aws.amazon.com/snowball/latest/developer-guide/ec2-ami-import-cli.html): Import a virtual machine (VM) image from your local environment or an Amazon EC2 Amazon Machine Image (AMI) to a Snowball Edge device.
- [Using the AWS CLI and API Operations](https://docs.aws.amazon.com/snowball/latest/developer-guide/using-ec2-cli-specify-region.html): Use the AWS CLI or API operations to issue IAM, Amazon S3, and Amazon EC2-compatible commands on a Snowball Edge device.
- [Network configurations for compute instances](https://docs.aws.amazon.com/snowball/latest/developer-guide/network-config-ec2.html): Setting up direct and virtual network interfaces (DNIs and VNIs) for compute instances on Snowball Edge.
- [Using SSH to connect to a compute instance](https://docs.aws.amazon.com/snowball/latest/developer-guide/ssh-ec2-edge.html): Use SSH to connect to compute instances on a Snowball Edge.
- [Transferring data from compute instances to buckets on the same device](https://docs.aws.amazon.com/snowball/latest/developer-guide/data-transfer-ec2-s3-edge.html): Transfer data between compute instances and Amazon S3 buckets on the same Snowball Edge device using AWS CLI commands and endpoints.
- [Starting instances automatically](https://docs.aws.amazon.com/snowball/latest/developer-guide/using-ec2-edge-client.html): Learn about how to use Snowball Edge Client commands to start EC2-compatible instances automatically on a Snowball Edge.
- [Using the Amazon EC2-compatible endpoint](https://docs.aws.amazon.com/snowball/latest/developer-guide/using-ec2-endpoint.html): Manage your AMIs and compute instances on a Snowball Edge device programmatically using the Amazon EC2-compatible endpoint.
- [Autostarting EC2-compatible instances](https://docs.aws.amazon.com/snowball/latest/developer-guide/ec2-autostart.html): Use launch templates and Snowball Edge client launch configuration commands to automatically start your Amazon EC2-compatible instances on an AWS Snowball Edge device.

### [Using IMDS for Snow with EC2-compatible instances](https://docs.aws.amazon.com/snowball/latest/developer-guide/imds.html)

Instance Metadata Service (IMDS) for Snow is used with Amazon EC2-compatible instances is used to retrieve data about instances.

- [IMDS versions on a Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/imds-versions.html): IMDS for Snow provides the option of accessing instance metadata through a sessionâoriented or requestâresponse method.
- [Examples of retrieving instance metadata using IMDSV1 and IMDSv2](https://docs.aws.amazon.com/snowball/latest/developer-guide/imds-code-examples.html): Examples for a Linux instance of retrieving instance metadata on a Snowball Edge using IMDSV1 and IMDSv2.
- [Using block storage with EC2-compatible instances](https://docs.aws.amazon.com/snowball/latest/developer-guide/edge-ebs.html): Add or remove block storage on Snowball Edge devices based on application needs.
- [Controlling network traffic with security groups](https://docs.aws.amazon.com/snowball/latest/developer-guide/edge-security-groups.html): Use security groups on Snowball Edge devices to control network traffic for one or more EC2-compatible instances.
- [Supported EC2-compatible instance metadata and user data](https://docs.aws.amazon.com/snowball/latest/developer-guide/edge-compute-instance-metadata.html): Use instance metadata to configure and manage a running EC2-compatible instance on a Snowball Edge device.


## [Using Amazon S3 compatible storage on Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/s3compatible-on-snow.html)

- [Order Amazon S3 compatible storage on Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/s3-edge-snow-order-device.html): Create a job to order a Snowball Edge device or a cluster of devices for use with Amazon S3 compatible storage on Snowball Edge.
- [Setting up and starting Amazon S3 compatible storage on Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/s3-edge-snow-setting-up.html): Set up your local environment to interact with Amazon S3 compatible storage on Snowball Edge running on Snowball Edge devices, set up the Snowball Edge device or cluster, and start Amazon S3 compatible storage on Snowball Edge.
- [Working with S3 buckets](https://docs.aws.amazon.com/snowball/latest/developer-guide/working-s3-snow-buckets.html): Use the AWS CLI or Java SDK to perform S3 API actions like creating and deleting buckets on a Snowball Edge device with Amazon S3 compatible storage on Snowball Edge.
- [Determining bucket access](https://docs.aws.amazon.com/snowball/latest/developer-guide/working-s3-snow-buckets-determine-bucket-access-s3-snow.html): Steps to determine if a bucket exists and if you have permission to access it in Amazon S3 compatible storage on Snowball Edge on a Snowball Edge.
- [Retrieving a list of buckets or regional buckets](https://docs.aws.amazon.com/snowball/latest/developer-guide/working-s3-snow-buckets-list-buckets-s3-snow.html): Steps to list buckets in Amazon S3 compatible storage on Snowball Edge using the AWS CLI.
- [Getting a bucket](https://docs.aws.amazon.com/snowball/latest/developer-guide/working-s3-snow-buckets-get-bucket-s3-snow.html): Steps to get a bucket in Amazon S3 compatible storage on Snowball Edge with the AWS CLI.
- [Creating an S3 bucket](https://docs.aws.amazon.com/snowball/latest/developer-guide/working-s3-snow-buckets-creating-s3-snow-bucket.html): Steps on creating an S3 bucket with Amazon S3 compatible storage on Snowball Edge.
- [Deleting a bucket](https://docs.aws.amazon.com/snowball/latest/developer-guide/working-s3-snow-buckets-delete-bucket-s3-snow.html): Steps to delete a bucket in Amazon S3 compatible storage on Snowball Edge using the AWS CLI.
- [Creating and managing an object lifecycle configuration using the AWS CLI](https://docs.aws.amazon.com/snowball/latest/developer-guide/working-s3-snow-buckets-lifecycle-s3-snow.html): Steps to create an object lifecycle configuration in Amazon S3 compatible storage on Snowball Edge.
- [Copying an object](https://docs.aws.amazon.com/snowball/latest/developer-guide/objects-copy-s3-snow.html): Steps to copy an object to an Amazon S3 compatible storage on Snowball Edge bucket on a Snowball Edge.
- [Listing objects](https://docs.aws.amazon.com/snowball/latest/developer-guide/objects-list-s3-snow.html): Steps to list the objects in an Amazon S3 compatible storage on Snowball Edge bucket on a Snowball Edge.
- [Getting an object](https://docs.aws.amazon.com/snowball/latest/developer-guide/objects-get-s3-snow.html): Steps to get an object from an Amazon S3 compatible storage on Snowball Edge bucket on a Snowball Edge.
- [Deleting objects](https://docs.aws.amazon.com/snowball/latest/developer-guide/objects-delete-s3-snow.html): Steps to delete objects from Amazon S3 compatible storage on Snowball Edge buckets.
- [Supported REST API actions for Amazon S3 compatible storage on Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/s3-snow-api.html): List of the API operations supported by Amazon S3 compatible storage on Snowball Edge.

### [Using Amazon S3 compatible storage on Snowball Edge with a cluster of Snow devices](https://docs.aws.amazon.com/snowball/latest/developer-guide/ClusterOverview.html)

Using Amazon S3 compatible storage on Snowball Edge clusters Use a cluster of devices for increased durability and storage of S3 data.

- [Reconnecting an unavailable cluster node](https://docs.aws.amazon.com/snowball/latest/developer-guide/reconnectingclusternodefortpoint.html): Steps to reconnect an unavailable node in a cluster of Snowball Edge devices.
- [Replacing a node in a cluster](https://docs.aws.amazon.com/snowball/latest/developer-guide/replacement.html): Steps to replace a node in cluster of Snowball Edge devices.
- [Configuring Amazon S3 compatible storage on Snowball Edge event notifications](https://docs.aws.amazon.com/snowball/latest/developer-guide/s3-snow-event-notifications.html): Configure MQTT notifications for Amazon S3 compatible storage on Snowball Edge events.
- [Configuring local SMTP notifications](https://docs.aws.amazon.com/snowball/latest/developer-guide/s3-snow-smtp-notifications.html): Configure SMTP notifications to monitor Amazon S3 compatible storage on Snowball Edge service health.


## [Using Amazon EKS Anywhere on Snowball Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/using-eksa.html)

- [Actions to complete before ordering a Snowball Edge device for Amazon EKS Anywhere on AWS Snow](https://docs.aws.amazon.com/snowball/latest/developer-guide/eksa-gettingstarted.html): Actions to complete before ordering a Snowball Edge device for Amazon EKS Anywhere on AWS Snow.
- [Ordering a Snowball Edge device for use with Amazon EKS Anywhere on AWS Snow](https://docs.aws.amazon.com/snowball/latest/developer-guide/order-sbe.html): When ordering a Snowball Edge device, choose the AMI built according to and .
- [Configuring and running Amazon EKS Anywhere on Snowball Edge devices](https://docs.aws.amazon.com/snowball/latest/developer-guide/eksa-configuration.html): Follow these procedures to configure and start Amazon EKS Anywhere on all Snowball Edge devices.
- [Configuring Amazon EKS Anywhere on AWS Snow for disconnected operation](https://docs.aws.amazon.com/snowball/latest/developer-guide/configure-disconnected.html): Follow these procedures to prepare Amazon EKS Anywhere to run on a Snowball Edge device without an external network connection.
- [Creating and maintaining clusters](https://docs.aws.amazon.com/snowball/latest/developer-guide/maintain-eks-a-clusters-snow.html)


## [Updating Snowball Edge devices](https://docs.aws.amazon.com/snowball/latest/developer-guide/updating-device.html)

- [Downloading updates](https://docs.aws.amazon.com/snowball/latest/developer-guide/download-updates.html): Learn about the two ways to download software updates for Snowball Edge.
- [Installing updates](https://docs.aws.amazon.com/snowball/latest/developer-guide/install-updates.html): Learn how to install software updates on Snowball Edge.
- [Updating the SSL certificate](https://docs.aws.amazon.com/snowball/latest/developer-guide/update-ssl-cert.html): Learn how to update Secure Sockets Layer (SSL) ceritificates on a Snowball Edge to prevent interruption of your use of the device.
- [Updating your Amazon Linux 2 AMIs](https://docs.aws.amazon.com/snowball/latest/developer-guide/update-ami.html): Learn how to update your Amazon Linux 2 AMIs runnning on Snowball Edge.


## [Understanding jobs](https://docs.aws.amazon.com/snowball/latest/developer-guide/jobs.html)

- [Job statuses](https://docs.aws.amazon.com/snowball/latest/developer-guide/jobstatuses.html): Track the current state of your AWS Snowball Edge device jobs using job statuses.
- [Import jobs](https://docs.aws.amazon.com/snowball/latest/developer-guide/importtype.html): Use an import job to copy data to your AWS Snowball Edge device with the built-in Amazon S3 adapter or an Network File System (NFS) mount point.
- [Export jobs](https://docs.aws.amazon.com/snowball/latest/developer-guide/exporttype.html): Use an export job to move data for a job part from Amazon S3 to an AWS Snowball Edge device and download a job report.
- [Information about local compute and storage jobs](https://docs.aws.amazon.com/snowball/latest/developer-guide/computetype.html): Access Amazon S3 buckets and run Amazon EC2-compatible images locally, without an internet connection with an AWS Snowball Edge device.


## [Security](https://docs.aws.amazon.com/snowball/latest/developer-guide/security.html)

- [Data Protection](https://docs.aws.amazon.com/snowball/latest/developer-guide/data-protection.html): AWS Snowball Edge enables you to use and configure data protection to meet the needs of your company.

### [Identity and Access Management](https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-iam.html)

Learn about identity and access management, logging and monitoring, and compliance for Snowball Edge.

### [Access Control for Console and Jobs](https://docs.aws.amazon.com/snowball/latest/developer-guide/authentication-and-access-control.html)

How to authenticate requests and manage permissions to access your AWS Snowball Edge resources through the API.

### [Identity and Access Management](https://docs.aws.amazon.com/snowball/latest/developer-guide/security-iam.html)

How to authenticate requests and manage access to your AWS Snow Family resources.

- [How AWS Snow Family works with IAM](https://docs.aws.amazon.com/snowball/latest/developer-guide/security_iam_service-with-iam.html): Before you use IAM to manage access to AWS Snow Family, learn what IAM features are available to use with AWS Snow Family.
- [Identity-based policy examples](https://docs.aws.amazon.com/snowball/latest/developer-guide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify AWS Snow Family resources.
- [Troubleshooting](https://docs.aws.amazon.com/snowball/latest/developer-guide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS Snow Family and IAM.
- [Access Control in the AWS Cloud](https://docs.aws.amazon.com/snowball/latest/developer-guide/access-control.html): Learn about the concepts of access control and permissions to AWS resouces in the cloud.
- [Using Identity-Based Policies (IAM Policies)](https://docs.aws.amazon.com/snowball/latest/developer-guide/access-control-managing-permissions.html): Find examples of identity-based policies for AWS Snowball Edge resources in the AWS Cloud.
- [Customer Managed Policy Examples](https://docs.aws.amazon.com/snowball/latest/developer-guide/access-policy-examples-for-sdk-cli.html): Find example user policies for AWS Snowball Edge job management actions for use with AWS SDKs or the AWS CLI.
- [Logging and Monitoring](https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-security-logging-and-monitoring.html): Use AWS tools for monitoring and responding to incidents.
- [Compliance validation](https://docs.aws.amazon.com/snowball/latest/developer-guide/snowball-edge-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/snowball/latest/developer-guide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy as well as specific AWS Snowball Edge features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/snowball/latest/developer-guide/infrastructure-security.html): Learn how AWS Snowball Edge isolates service traffic.


## [Quotas](https://docs.aws.amazon.com/snowball/latest/developer-guide/limits.html)

- [Quotas for compute instances](https://docs.aws.amazon.com/snowball/latest/developer-guide/ec2-edge-limits.html): Storage quotas and shared resource limitations for compute resources on a Snowball Edge device.


## [Troubleshooting](https://docs.aws.amazon.com/snowball/latest/developer-guide/troubleshooting.html)

- [Identify a device](https://docs.aws.amazon.com/snowball/latest/developer-guide/identifying-device.html): Learn how to determine your Snowball Edge configuration using the describe-device command and interpret the DeviceType value with a reference table.
- [Troubleshooting bootâup problems](https://docs.aws.amazon.com/snowball/latest/developer-guide/boot-troubleshoot.html): Learn how to troubleshoot boot-up issues with Snowball Edge, including problems with LCD and E Ink displays, and understand device configurations using the describe-device command output.
- [Troubleshooting connection problems](https://docs.aws.amazon.com/snowball/latest/developer-guide/connection-troubleshooting.html): Troubleshoot connection issues with a Snowball Edge device using these tips and advanced steps for network configuration, port testing, and device resets.
- [Troubleshooting unlock-device command problems](https://docs.aws.amazon.com/snowball/latest/developer-guide/unlock-command-troubleshooting.html): Troubleshoot connection issues with the unlock-device command for Snowball Edge and learn how to manage manifest files for different jobs.
- [Troubleshooting credentials problems](https://docs.aws.amazon.com/snowball/latest/developer-guide/credentials-troubleshooting.html): Resolve credentials issues for Snowball Edge, including locating AWS CLI credentials and troubleshooting signature mismatch errors when using the S3 interface.
- [Troubleshooting data transfer problems](https://docs.aws.amazon.com/snowball/latest/developer-guide/transfer-troubleshooting.html): Learn how to troubleshoot and resolve issues with the NFS interface and data transfer on Snowball Edge, including restarting services and improving performance.
- [Troubleshooting AWS CLI problems](https://docs.aws.amazon.com/snowball/latest/developer-guide/cli-troubleshooting.html): Use the following topics to help you resolve problems when working with an AWS Snowball Edge device and the AWS CLI.
- [Troubleshooting compute instances](https://docs.aws.amazon.com/snowball/latest/developer-guide/troubleshooting-ec2-edge.html): Troubleshooting issues with compute instances on Snowball Edge.
