# Source: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/llms.txt

# Amazon Elastic Compute Cloud User Guide

> Use Amazon EC2 to configure, launch, and manage virtual servers in the AWS cloud.

- [What is Amazon EC2?](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)
- [Get started tutorial](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)
- [Best practices](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-best-practices.html)
- [Document history](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/DocumentHistory.html)

## [Amazon Machine Images](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)

### [AMI characteristics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html)

Select an AMI type based on your desired characteristics such as its Region, operating system, architecture, and root volume type.

- [Identify the AMI root volume type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/display-ami-root-device-type.html): Identify the root volume type determined by your AMI using the Amazon EC2 console or AWS CLI.

### [Find an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html)

Find an AMI that meets your needs for launching an instance by searching for criteria such as the operating system that is included.

- [Systems Manager parameters](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-systems-manager-parameter-to-find-AMI.html): When you launch an instance using the EC2 launch instance wizard in the Amazon EC2 console, you can either select an AMI from the list, or you can select an AWS Systems Manager parameter that points to an AMI ID (described in this section).
- [Systems Manager public parameters](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami-parameter-store.html): AWS Systems Manager provides public parameters for public AMIs maintained by AWS.

### [Paid AMIs in the AWS Marketplace](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/paid-amis.html)

Purchase or sell a custom AMI, known as a paid AMI, in the AWS Marketplace for launching Amazon EC2 instances.

- [Find a paid AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-paid-amis-finding-paid-ami.html): Find an AMI that is available for purchase.
- [Purchase a paid AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-paid-amis-purchasing-paid-ami.html): After you purchase a paid AMI you can launch an EC2 instance using the AMI.
- [Retrieve the product code](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/get-product-code.html): Retrieve the product code for your EC2 instance by using its instance metadata.
- [Use paid support](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-paid-amis-support.html): Use paid support for products in the AWS Marketplace by using a developer supplied product code.
- [Manage your subscriptions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/marketplace-manage-subscriptions.html): Manage your subscription details using the AWS Marketplace website where you can check subscription details, view the vendor's usage instructions, and more.

### [AMI lifecycle](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-lifecycle.html)

Understand the actions that you can perform as part of the AMI lifecycle.

- [Create an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html): Create your own Amazon EBS-backed AMI from a customized Amazon EC2 instance or from the snapshot of the root volume of an Amazon EC2 instance.

### [Create an Amazon S3-backed AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-instance-store.html)

Create your own AMI from your customized Amazon S3-backed Linux instance.

- [Set up the AMI tools](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-up-ami-tools.html): Use the AMI tools to create and manage Amazon S3-backed Linux AMIs.
- [AMI tools reference](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-tools-commands.html): Command syntax for the Amazon EC2 AMI tools.
- [Convert your S3-backed AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_ConvertingS3toEBS.html): Learn how to convert an AMI backed by Amazon S3 to an AMI backed by Amazon EBS.

### [Create an AMI using Windows Sysprep](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-create-win-sysprep.html)

Use EC2 launch agents to create an AMI with Windows Sysprep.

- [Use Windows Sysprep with EC2Launch v2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sysprep-using-ec2launchv2.html): Use the EC2Launch v2 agent to create a Windows AMI with Windows Sysprep.
- [Use Windows Sysprep with EC2Launch](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2launch-sysprep.html): Use the EC2Launch agent to create a Windows AMI with Windows Sysprep.
- [Use Windows Sysprep with EC2Config](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sysprep-using.html): Use the EC2Config service to create a Windows AMI with Windows Sysprep.

### [Copy an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/CopyingAMIs.html)

Learn how to copy an Amazon EC2 AMI across AWS Regions or Local Zones, to Outposts, or between AWS accounts, including considerations, costs, and step-by-step instructions for the copy process.

- [Permissions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/copy-ami-permissions.html): Example policies that grant permissions to copy Amazon EC2 AMIs.
- [How AMI copy works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-ami-copy-works.html): Understand how AMI copy works with encryption, multiple Regions, and multiple accounts.

### [Store and restore an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-store-restore.html)

Store a copy of an AMI in an S3 bucket.

- [How AMI store and restore works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/store-restore-how-it-works.html): Understand the key concepts and behavior of AMI store and restore.
- [Create a store image task](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-ami-store-restore.html): Learn how to create a store image task to store an AMI in an S3 bucket.
- [AMI ancestry](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-ancestry.html): Learn how to use AMI ancestry to identify the source AMI used to create an AMI and to trace the lineage of AMIs in Amazon EC2.

### [AMI usage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-ami-usage.html)

Learn how to track, audit, and optimize your Amazon Machine Image (AMI) usage across your AWS resources.

- [View your AMI usage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/your-ec2-ami-usage.html): See how your AMI is being used by other AWS accounts.
- [Check when an AMI was last used](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-last-launched-time.html): Check when your AMI was last used to launch an Amazon EC2 instance.
- [Identify your resources referencing specified AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-ami-references.html): See what AMIs your AWS resources are referencing.
- [Deprecate an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-deprecate.html): Specify a deprecation date for an AMI to indicate when it is out of date.
- [Disable an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/disable-an-ami.html): Disable an AMI to prevent it from being used for instance launches.

### [Deregister an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/deregister-ami.html)

Deregister your AMI when you have finished using it.

- [Protect an AMI from deregistration](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-deregistration-protection.html): Prevent your Amazon EC2 AMI from being accidentally deregistered by enabling deregistration protection.

### [Boot modes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html)

Learn about using either UEFI or Legacy BIOS boot mode with your Amazon EC2 instances.

- [Requirements for UEFI boot mode](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launch-instance-boot-mode.html): Learn about the requirements to launch an EC2 instance in UEFI boot mode.
- [AMI boot mode parameter](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot-mode.html): Determine the boot mode parameter setting of an Amazon EC2 AMI.
- [Instance type boot mode](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-type-boot-mode.html): Determine the supported boot modes of an Amazon EC2 instance type.
- [Instance boot mode](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-boot-mode.html): Determine the boot mode of an Amazon EC2 instance.
- [Operating system boot mode](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/os-boot-mode.html): Determine the boot mode of your Windows or Linux operating system.
- [Set AMI boot mode](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-ami-boot-mode.html): Learn how to set the boot mode for an Amazon EC2 AMI.
- [UEFI variables](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/uefi-variables.html): Understand how UEFI variables are used by Amazon EC2 instances.

### [UEFI Secure Boot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/uefi-secure-boot.html)

Learn how to use UEFI Secure Boot to ensure that an Amazon EC2 instance only boots cryptographically signed software.

- [How UEFI Secure Boot works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-uefi-secure-boot-works.html): Understand how UEFI Secure Boot works with Amazon EC2 instances to verify the state of the boot chain.
- [Requirements for UEFI Secure Boot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launch-instance-with-uefi-sb.html): Understand how to launch an Amazon EC2 instance with support for UEFI Secure Boot.
- [Verify if an instance is enabled for UEFI Secure Boot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/verify-uefi-secure-boot.html): Verify whether an Amazon EC2 instance is enabled to use UEFI Secure Boot.
- [Create a Linux AMI with custom keys](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-ami-with-uefi-secure-boot.html): Create a Linux AMI with your own UEFI Secure Boot variable store with custom-made private keys.
- [Create the AWS binary blob](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/aws-binary-blob-creation.html): Learn how to customize the UEFI Secure Boot variables during AMI creation.
- [AMI encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html): Use Amazon EBS encryption with AMIs in various configurations.

### [Shared AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharing-amis.html)

Understand how to use a public AMI that a developer created or share an AMI that you created for others to use.

- [Find shared AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/usingsharedamis-finding.html): Find a public or private shared AMI to use with the AWS CLI or Amazon EC2 console.
- [Prepare to use shared AMIs for Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/usingsharedamis-confirm.html): Ensure that your AMI is safe to share.

### [Allowed AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-allowed-amis.html)

Control the discovery and use of AMIs in Amazon EC2 with the Allowed AMIs settings.

- [Manage the settings for Allowed AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-settings-allowed-amis.html): Learn how to configure the Allowed AMIs settings to control which Amazon Machine Images (AMIs) can be used to launch EC2 instances in your account.
- [Make your AMI public](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-intro.html): Make your AMI publicly available for all Amazon EC2 users to use for launching instances.

### [Block public access for AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-public-access-to-amis.html)

Manage the block public access setting that controls the public sharing of AMIs.

- [Manage the block public access setting for AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-block-public-access-for-amis.html): Manage the block public access setting for your AMIs to allow or prevent them from being publicly shared.

### [Share an AMI with organizations and organizational units](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/share-amis-with-organizations-and-OUs.html)

Understand shared AMI use with organizations and organizational units.

- [Get the ARN of an organization or organizational unit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/get-org-ou-ARN.html): Get the ARN of an organization or organizational unit in AWS Organizations to share an AMI with.
- [Allow organizations and OUs to use a KMS key](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/allow-org-ou-to-use-key.html): Allow organizations and OUs to use a customer-managed KMS key for a shared AMI backed by encrypted snapshots.
- [Manage AMI sharing with an organization or OU](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/share-amis-org-ou-manage.html): Manage AMI sharing with an organizations and OUs to control whether they can launch Amazon EC2 instances.
- [Share an AMI with specific AWS accounts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html): Share your AMI with specific AWS accounts so that they can launch instances with it.
- [Cancel having an AMI shared with your account](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cancel-sharing-an-AMI.html): You can find AMIs that have been shared with your account and cancel them by removing your account ID from the AMI's launch permissions.
- [Recommendations for creating shared Linux AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/building-shared-amis.html): Follow these recommendations when creating a shared Linux AMI to reduce the attack surface and improve the reliability of the AMIs you create.
- [Monitor AMI events](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitor-ami-events.html): Monitor EC2 AMI State Change events by using Amazon EventBridge to detect and react to these events.

### [Understand AMI billing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-billing-info.html)

Describes how to look up EC2 AMI billing details, and to use the information to help prevent unplanned charges, by choosing the right AMI for your instance.

- [AMI billing fields](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-info-fields.html): Describes fields that are used for AMI billing information, including platform details and usage operation.
- [Find AMI billing information](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/view-billing-info.html): Outlines the steps to find AMI billing information for an AMI or an instance.
- [Verify AMI charges on your bill](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/verify-ami-charges.html): Describes how to verify EC2 AMI charges that you've been billed for to ensure that you're not incurring unplanned costs.
- [AMI quotas](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-quotas.html): Learn about quotas for creating public and private AMIs, and for sharing AMIs.


## [Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Instances.html)

### [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html)

Amazon EC2 provides a variety of instance types with different compute, memory, storage, and network capabilities.

- [Find an instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-discovery.html): Find an Amazon EC2 instance with the compute, memory, and storage that you need.
- [EC2 instance type finder](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/get-ec2-instance-type-recommendations.html): Get recommendations for your Amazon EC2 instances to achieve the best price-performance for your new workloads.
- [Compute Optimizer recommendations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recommendations.html): Get recommendations from Compute Optimizer to help you improve the performance of your Amazon EC2 instances and save money.

### [Instance type changes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html)

Change the instance type of your Amazon EC2 instance to an instance type that is appropriate for its workload or to use features that are available on other instance types.

- [Compatibility](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/resize-limitations.html): Learn about compatibility requirements for changing your instance type.
- [Change the instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/change-instance-type-of-ebs-backed-instance.html): Learn how to change the instance type of an Amazon EC2 instance backed by Amazon EBS.
- [Migrate to a new instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/migrate-instance-configuration.html): Learn how to migrate to a new EC2 instance type by launching a replacement EC2 instance.
- [Troubleshoot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshoot-change-instance-type.html): Troubleshoot common issues with instance type changes in Amazon EC2.

### [Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html)

Learn how to use burstable performance instances for baseline CPU performance and the ability to burst to higher performance as required by your workload.

- [Key concepts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-credits-baseline-concepts.html): Understand the key concepts and definitions of CPU performance for burstable performance instances.

### [Unlimited mode](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-unlimited-mode.html)

Understand the key concepts for unlimited mode burstable performance instances.

- [Concepts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-unlimited-mode-concepts.html): Understand the key concepts for working with burstable Amazon EC2 instances in unlimited mode.
- [Examples](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/unlimited-mode-examples.html): See example scenarios for burstable instances in unlimited mode.

### [Standard mode](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-standard-mode.html)

Learn about standard mode for burstable performance instances.

- [Concepts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-standard-mode-concepts.html): Learn the key concepts for working with burstable performance instances in standard mode.
- [Examples](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/standard-mode-examples.html): Understand the details of some standard mode burstable instance examples.
- [Configure burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-how-to.html): Learn how to launch burstable performance instances, and how to set, view, and modify credit specifications in Amazon EC2.
- [Monitor your CPU credits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-monitoring-cpu-credits.html): Learn how to monitor CPU credits for burstable performance instances.

### [GPU instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configure-gpu-instances.html)

Learn how to configure your Amazon EC2 GPU-based instances.

- [Activate NVIDIA GRID Virtual Applications](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/activate_grid.html): Learn how to activate NVIDIA GRID Virtual Applications on your Amazon EC2 instances.
- [Optimize GPU settings](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/optimize_gpu.html): Learn how to configure GPU setting optimizations on NVIDIA GPU instances.
- [Set up dual 4K displays on G4ad](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/activate_g4ad_4k.html): Learn how to set up dual 4K displays on G4ad Linux instances.
- [Get started with GPU accelerated instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/gpu-instances-started.html): Prepare to launch your GPU accelerated EC2 instances.

### [Mac instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html)

Use Amazon EC2 Mac instances to develop, build, test, and sign applications for Apple platforms such as iPhone, iPad, Mac, Safari, Apple Watch, and Apple TV.

- [Launch a Mac instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mac-instance-launch.html): Learn to launch a Mac instance using the AWS Management Console or the AWS CLI.
- [Connect to your Mac instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-mac-instance.html): Connect to your Mac instance using SSH or a GUI.
- [Update operating system and software](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mac-instance-updates.html): Learn how to update the operating system and software on x86 and Apple silicon Mac instances
- [Increase size of EBS volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mac-instance-increase-volume.html): Learn how to increase the size of an EBS volume on your Mac instance.
- [Stop or terminate Mac instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mac-instance-stop.html): Understand what happens when you stop or terminate your Mac instance.
- [Configure SIP settings](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mac-sip-settings.html): Configure System Integrity Protection (SIP) settings for Amazon EC2 Mac instances.
- [Find supported macOS versions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-firmware-visibility.html): Learn how to view the supported macOS versions for your Amazon EC2 Mac Dedicated Host.
- [Subscribe to macOS AMI notifications](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-subscribe-notifications.html): Learn how to get macOS AMI release notifications.
- [Retrieve macOS AMI IDs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-ids-parameter-store.html): Learn how to get the IDs of the macOS AMIs using AWS Systems Manager.
- [macOS AMIs release notes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-ami-overview.html): Discover the details about macOS AMIs releases and default packages included in macOS AMIs.

### [EBS optimization](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html)

Use Amazon EBS-optimized instance types to get the best performance from your Amazon EBS volumes.

- [Get maximum EBS performance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimization-performance.html): Get the best Amazon EBS performance from your Amazon EC2 instance.
- [Find EBS-optimized instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/describe-ebs-optimization.html): Find Amazon EC2 instance types that support Amazon EBS optimization.
- [Enable EBS optimization](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/modify-ebs-optimized-attribute.html): Manually enable EBS optimization for Amazon EC2 instance types that optionally support it.

### [CPU options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html)

Learn how to configure CPU cores and threads to optimize your Amazon EC2 instance for specific workloads or business needs.

- [Rules for specifying CPU options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-cpu-options-rules.html): Understand the rules for specifying CPU options for an Amazon EC2 instance.
- [Supported CPU options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cpu-options-supported-instances-values.html): Learn about the supported CPU core and thread configurations for Amazon EC2 instance types.
- [Specify CPU options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-specify-cpu-options.html): Specify CPU threads and cores, and disable multithreading for an Amazon EC2 instances.
- [View CPU options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/view-cpu-options.html): View the CPU thread and core configuration for an Amazon EC2 instance.
- [Optimize CPUs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/optimize-cpu.html): Optimize the number of CPUs that are active for instances launched from Amazon EC2 license-included Windows and SQL Server AMIs to save on licensing costs that are billed per CPU.

### [AMD SEV-SNP](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sev-snp.html)

Use AMD SEV-SNP to get a cryptographically signed attestation report for your Amazon EC2 instance.

- [Find supported instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snp-find-instance-types.html): Check which Amazon EC2 instance types support AMD SEV-SNP.
- [Enable AMD SEV-SNP](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snp-work-launch.html): Enable AMD SEV-SNP for a supported Amazon EC2 instance.
- [Attestation with AMD SEV-SNP](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snp-attestation.html): Perform the attestation process on an Amazon EC2 instance using the AMD SEV-SNP attestation report.
- [Processor state control](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/processor_state_control.html): Some Amazon EC2 instance types provide the ability for an operating system to control the processor C-states (sleep levels) and P-states (CPU frequency).
- [Managed instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-managed-instances.html): Amazon EC2 managed instances enable you to delegate operational responsibility of your Amazon EC2 instances to services like Amazon EKS, offering streamlined management, while the technical and billing aspects remain the same as non-managed EC2 instances.
- [Nested virtualization](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nested-virtualization.html): Nested virtualization allows you to run hypervisors such as Hyper-V and KVM inside virtual Amazon EC2 instances.

### [Billing and purchasing options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html)

Amazon EC2 provides different billing and purchasing options so that you can optimize your costs based on your needs.

- [On-Demand Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html): Understand pricing, quotas and other key concepts for purchasing Amazon EC2 On-Demand Instances.

### [Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html)

Learn how using Reserved Instances can save you money on Amazon EC2 compute costs compared to On-Demand Instances.

- [Regional and zonal Reserved Instances (scope)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/reserved-instances-scope.html): Learn the details of the two different available scopes of Reserved Instances, regional and zonal.
- [Types of Reserved Instances (offering classes)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/reserved-instances-types.html): Learn about the two types of offering classes for Reserved Instances, Standard or Convertible.
- [How Reserved Instance discounts are applied](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/apply_ri.html): Find out how billing discounts for Reserved Instances are applied to instances in your account.
- [Use your Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-reserved-instances.html): Learn what specifications need to match to use your Reserved Instances.
- [How billing works with Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts-reserved-instances-application.html): Understand how Reserved Instance billing and pricing works.
- [Buy Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-concepts-buying.html): Purchase Amazon EC2 Reserved Instances from third party sellers or AWS using the Amazon EC2 console, a command line tool, or an AWS SDK.
- [Sell Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-general.html): Learn about selling your unused Reserved Instances for Amazon EC2 in the Reserved Instance Marketplace.
- [Modify Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-modifying.html): Modify your Reserved Instances and continue to benefit from your capacity reservation and billing benefit when your computing needs change.
- [Exchange Convertible Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-convertible-exchange.html): Understand the requirements for exchanging your Convertible Reserved Instances.
- [Reserved Instance quotas](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-limits.html): Learn about the quotas for Reserved Instances and how to increase them.

### [Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)

Learn how to lower your Amazon EC2 costs using Spot Instances.

- [Best practices](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-best-practices.html): Learn about the best practices for using Amazon EC2 Spot Instances.
- [How Spot Instances work](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-spot-instances-work.html): Learn how Amazon EC2 Spot Instances work.
- [View pricing history](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances-history.html): View the pricing history for Amazon EC2 Spot Instances.
- [View savings](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-savings.html): View your savings made from using Amazon EC2 Spot Instances and Amazon EC2 Spot Fleets.

### [Create a Spot Instance request](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-requests.html)

Learn how to create a Spot Instance request.

- [Example launch specifications](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-request-examples.html): Learn how to create a launch specification for use with the AWS CLI.

### [Get the status of a Spot Instance request](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-request-status.html)

Track your Spot Instance requests.

- [State changes for a Spot request](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-instances-request-status-lifecycle.html): Learn about the state changes during the lifecycle of a Spot request.
- [Tag Spot Instance requests](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts-spot-instances-request-tags.html): Learn how to tag a Spot Instance request.
- [Cancel a Spot Instance request](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances-cancel.html): Learn how to cancel a Spot Instance request.
- [Manage your Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances-request.html): Learn how to find, stop, and terminate your Spot Instances.

### [Spot Instance interruptions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html)

Understand the key concepts and behavior for Spot Instance interruptions.

- [Interruption behavior](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interruption-behavior.html): Learn about the different interruption behaviors supported for Spot Instances.
- [Prepare for interruptions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/prepare-for-interruptions.html): Learn about best practices to handle Spot Instance interruptions.
- [Initiate an interruption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/initiate-a-spot-instance-interruption.html): Learn how to interrupt a Spot Instance for testing purposes.
- [Spot Instance interruption notices](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-instance-termination-notices.html): Understand Spot Instance interruption notices.
- [Find interrupted Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-interrupted-Spot-Instance.html): Learn how to find any interrupted Spot Instances.
- [Determine whether Amazon EC2 terminated a Spot Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/BidEvictedEvent.html): Learn how to determine whether Amazon EC2 terminated a Spot Instance as part of a Spot Instance interruption.
- [Billing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-for-interrupted-spot-instances.html): Understand what resources you are charged for with an interrupted Spot Instance.
- [Rebalance recommendations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/rebalance-recommendations.html): Learn about EC2 instance rebalance recommendations, which are interruption signals that give you the opportunity to gracefully manage Spot Instance interruptions.

### [Spot placement score](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-placement-score.html)

The Spot placement score feature helps you to find the optimal AWS Regions or Availability Zones for your Amazon EC2 Spot workloads.

- [How Spot placement score works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-sps-works.html): Understand how to use Spot placement score.
- [Required permissions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sps-iam-permission.html): Understand the permissions required to use Spot placement score.
- [Calculate the Spot placement score](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-spot-placement-score.html): Learn how to calculate the Spot placement score for specific target capacity and compute requirements.
- [Spot Instance data feed](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-data-feeds.html): Subscribe to a data feed to track your Spot Instance usage and costs.
- [Service-linked role for Spot Instance requests](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/service-linked-roles-spot-instance-requests.html): Learn how to grant Amazon EC2 permission to launch and manage Spot Instances on your behalf.
- [Spot Instance quotas](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-limits.html): Learn about the quotas for Amazon EC2 Spot Instances and Spot Fleet.

### [Dedicated Hosts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-overview.html)

Dedicated Hosts are physically isolated Amazon EC2 servers that provide dedicated instance capacity and support bring-your-own-license and compliance use cases.

- [Pricing and billing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-billing.html): Understand how Amazon EC2 Dedicated Hosts are billed and how the various billing discounts are applied.
- [Instance capacity configurations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-limits.html): Understand the supported instance capacity configurations for Amazon EC2 Dedicated Hosts.
- [Burstable instances on Dedicated Hosts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-t3.html): Understand how to run burstable T3 instances on an Amazon EC2 Dedicated Host.
- [Bring your own licenses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-BYOL.html): Import and use your existing per-socket, per-core, or per-VM software licenses software license on Amazon EC2 Dedicated Hosts.
- [Auto-placement and affinity](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-understanding.html): Understand how to use Amazon EC2 Dedicated Host auto-placement and affinity to control where your instances launch, run, and restart.
- [Allocate a Dedicated Host](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-allocating.html): Allocate a Dedicated Host for use in your AWS account.
- [Launch instances on a Dedicated Host](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launching-dedicated-hosts-instances.html): Launch instances on an Amazon EC2 Dedicated Host.
- [Launch instances into a host resource group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launching-hrg-instances.html): Launch Amazon EC2 instances into a host resource group.
- [Modify Dedicated Host auto-placement](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/modify-host-auto-placement.html): Modify the auto-placement setting for a Dedicated Host to control which instances can launch and run on it.
- [Modify supported instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/modify-host-support.html): Modify an existing Dedicated Host to support either a single instance type or multiple instance types within an instance family.
- [Modify tenancy and affinity for an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/moving-instances-dedicated-hosts.html): Change the tenancy for an existing instance so that it runs on an Amazon EC2 Dedicated Host.
- [Release Dedicated Host](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-releasing.html): Release an On-Demand Dedicated Host when you no longer need it.
- [Migrate to Nitro-based Amazon EC2 Dedicated Hosts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dh-migrate.html): The Nitro System is a collection of hardware and software components built by AWS that enable high performance, high availability, and high security.

### [Cross-account sharing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dh-sharing.html)

Share Amazon EC2 Dedicated Host capacity across multiple AWS accounts.

- [Share a Dedicated Host](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharing-dh.html): Share an Amazon EC2 Dedicated Host across AWS accounts or within an AWS organization.
- [Unshare a Dedicated Host](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/unsharing-dh.html): Unshare a Dedicated Host when you no longer want to share its capacity with other AWS accounts.
- [View shared Dedicated Hosts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/identifying-shared-dh.html): View Dedicated Hosts that you are sharing and that are shared with you, along with the instance running on them.

### [Dedicated Hosts on Outposts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dh-outposts.html)

Understand how Amazon EC2 Dedicated Hosts work with AWS Outposts.

- [Allocate Dedicated Host on Outpost](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dh-outpost-allocate.html): Allocate and use an Amazon EC2 Dedicated Host on AWS Outposts.

### [Host recovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-recovery.html)

Host recovery automatically restarts your running instances onto a new host if failures are detected on your Dedicated Host under certain conditions.

- [How host recovery works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-recovery-basics.html): Understand how Amazon EC2 Dedicated Host recovery works to automatically recover your instances on an impaired Dedicated Host.
- [Manage host recovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-recovery-enable.html): Enable host recovery to automatically recovery instances on an impaired Amazon EC2 Dedicated Host.
- [View host recovery setting](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-recovery-view.html): View the current host recovery setting for your Amazon EC2 Dedicated Hosts.
- [Manually recovery unsupported instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-recovery-unsupported.html): Manually recover instances that are not supported by Amazon EC2 Dedicated Host recovery.

### [Host maintenance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-maintenance.html)

Use host maintenance to automatically recover instances on an Amazon EC2 Dedicated Host during scheduled events.

- [How host maintenance works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-maintenance-basics.html): Understand how host recovery works to recover instances on an Amazon EC2 Dedicated Host during a scheduled event.
- [Configure host maintenance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-maintenance-configuring.html): Enable host maintenance to ensure that your instances running on a Dedicated Host are automatically recovered onto a new Dedicated Host during a scheduled maintenance event.
- [Monitor Dedicated Hosts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-monitoring.html): Monitor the status of your Amazon EC2 Dedicated Hosts.
- [Track configuration changes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-aws-config.html): Track instance and Dedicated Host configuration changes using AWS Config.

### [Dedicated Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-instance.html)

Run an Amazon EC2 instance on single-tenant hardware that is physically isolated from other AWS instances and accounts.

- [Launch Dedicated Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicatedinstancesintovpc.html): Launch an Dedicated Instance into a VPC that uses default tenancy.
- [Change the tenancy of an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-change-tenancy.html): Change between dedicated and host tenancy for an Amazon EC2 instance.
- [Change the tenancy of a VPC](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/change-tenancy-vpc.html): Change between default and dedicated tenancy for an Amazon VPC.

### [Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservation-overview.html)

Learn about Capacity Reservations and Capacity Blocks to reserve Amazon EC2 capacity.

### [On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html)

Learn about reserving compute capacity in a specific Availability Zone with Capacity Reservations.

- [Concepts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-concepts.html): Understand the concepts related to Amazon EC2 Capacity Reservations.
- [Pricing and billing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-pricing-billing.html): Learn about pricing and billing for Capacity Reservations.
- [Create a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-create.html): Create Capacity Reservations to reserve EC2 capacity.
- [View the state of a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-view.html): View the state of your Capacity Reservations.
- [Launch instances into Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-launch.html): Launch instances into an existing Capacity Reservation in your account and specify whether to launch into any open Capacity Reservation, a specific Capacity Reservation, or a group of Capacity Reservations.
- [Modify Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-modify.html): Modify active Capacity Reservations by updating quantity, instance eligibility or release behavior.
- [Modify instance Capacity Reservation settings](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-modify-instance.html): Modify Capacity Reservation settings to set up instance to run in any Capacity Reservation, a specific Capacity Reservation, a reservation with matching attributes and available capacity, or prevent from running in reservation.
- [Move capacity](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-move.html): Learn how to move capacity from one Capacity Reservation to another Capacity Reservation.
- [Split off capacity](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-split.html): Learn how to split off capacity from an existing Capacity Reservation and create a new Capacity Reservation.
- [Cancel a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-release.html): Cancel a Capacity Reservation that you no longer need.
- [Use Capacity Reservations with cluster placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-cpg.html): Learn how to create Capacity Reservations in a cluster placement group

### [Capacity Reservation groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-cr-group.html)

Create logical collections of Capacity Reservations in the same AWS Region with Resource Groups and target instances to a group of reservations.

- [Create a group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-group.html): Learn how to create a Capacity Reservation group using the AWS CLI.
- [Add Capacity Reservation to group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/add-to-group.html): Learn how to add a Capacity Reservation to a group using the AWS CLI.
- [Remove Capacity Reservation from group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/remove-from-group.html): Learn how to remove a Capacity Reservation from a group using the AWS CLI.
- [Delete group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/delete-group.html): Learn how to delete a Capacity Reservation group using the AWS CLI.
- [Using Capacity Reservation in cluster placement groups with a Capacity Reservation group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cpg-odcr-crg.html): Learn how to use Capacity Reservation in cluster placement groups with a Capacity Reservation group.
- [Capacity Reservations in Local Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-localzones.html): Understand how to use Capacity Reservations in a Local Zone.
- [Capacity Reservations in Wavelength Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-wavelengthzones.html): Understand how to use Capacity Reservations in a Wavelength Zone
- [Capacity Reservations on AWS Outposts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-outposts.html): Understand how to use Capacity Reservations on a Outpost.

### [Shared Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservation-sharing.html)

Understand how shared Capacity Reservations work.

- [Share a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharing-cr.html): Learn how to share your Capacity Reservations.
- [Stop sharing a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/unsharing-cr.html): Learn how to unshare your Capacity Reservations.

### [Billing assignment](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/assign-billing.html)

Learn how to assign billing of available capacity of a shared Capacity Reservation to another AWS account.

- [Assign billing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/request-billing-transfer.html): To assign billing of the available capacity of a shared Capacity Reservation to another account, the Capacity Reservation owner must initiate a request to the required account.
- [View billing assignment requests](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/view-billing-transfers.html): View billing assignment requests for shared Amazon EC2 Capacity Reservations in your account.
- [Accept or reject billing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/accept-decline-billing-transfer.html): Learn how to accept or reject a billing assignment request for the unused capacity of a shared Amazon EC2 Capacity Reservation.
- [Cancel or revoke requests](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cancel-billing-transfer.html): Learn how to cancel a billing assignment request for a shared Amazon EC2 Capacity Reservation.
- [Monitor requests](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-ownership-events.html): Learn how to monitor shared Capacity Reservation billing assignments using EventBridge rules.

### [Capacity Reservation Fleets](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-fleets.html)

Use a Capacity Reservation Fleet to create and manage a group of Capacity Reservations that reserve capacity for across multiple instance types, up to a target capacity that you specify.

- [Concepts and planning](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html): Learn how to plan for a Capacity Reservation Fleet.
- [Create](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-crfleet.html): Learn how to create a Capacity Reservation Fleet that creates Capacity Reservations for the specified instance types up to the specified total target capacity.
- [Modify](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/modify-crfleet.html): Learn how to modify the total target capacity and end date of a Capacity Reservation Fleet.
- [Cancel](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cancel-crfleet.html): Learn how to cancel a Capacity Reservation Fleet.
- [Example configurations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-example-configs.html): Learn about example Capacity Reservation Fleet configurations
- [Using service-linked roles](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-service-linked-roles.html): How to use service-linked roles to give Capacity Reservation Fleet access to resources in your AWS account.
- [Monitor with CloudWatch metrics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservation-cw-metrics.html): Learn about the CloudWatch usage metrics that Amazon EC2 provides for Capacity Reservations including in use instance count, available instance count, total instance count, and percent utilization of instance.
- [Monitor underutilization](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-eventbridge.html): Learn how to monitor Capacity Reservation utilization by establishing a EventBridge rule to trigger a programmatic action.
- [Monitor state changes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitor-fcr-state.html): Amazon EC2 sends an event to Amazon EventBridge when the state of a future-dated Capacity Reservation changes.

### [Interruptible Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interruptible-capacity-reservations.html)

Make unused capacity temporarily available for other workloads within your account while retaining control to reclaim it when needed.

- [Capacity owners](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-owner-procedures.html): The capacity owner is the account that owns the source Capacity Reservation and creates the interruptible Capacity Reservation to share unused capacity with other teams while retaining control to reclaim it when needed.
- [Capacity consumers](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-consumer-procedures.html): The capacity consumer is the account that launches instances into shared interruptible Capacity Reservations, understanding that their instances may be terminated when the owner reclaims capacity.
- [Monitor with EventBridge and CloudTrail](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitor-interruptible-cr.html): Interruptible Capacity Reservations send EventBridge notifications and CloudTrail events to help you monitor and respond to capacity changes.

### [Capacity Blocks for ML](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-blocks.html)

Reserve GPU capacity on Amazon EC2 for machine learning tasks.

- [How it works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-blocks-how.html): You can reserve a Capacity Block with the following specifications:
- [Pricing and billing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-blocks-pricing-billing.html): Learn about pricing and billing of Capacity Blocks.
- [Find and purchase](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-blocks-purchase.html): Find and purchase Capacity Blocks to reserve capacity.
- [Launch instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-blocks-launch.html): Launch instances into an active Capacity Block using the reservation ID.
- [View](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-blocks-view.html): View the start and end date of your Capacity Blocks and how many instances will be available.
- [Extend](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-blocks-extend.html): Extend the end date of your Capacity Blocks.
- [Share](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-blocks-share.html): Share your Capacity Blocks.
- [Create UltraServer group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cb-group.html): Learn how to create a resource group for UltraServer Capacity Blocks.
- [Monitor using EventBridge](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-blocks-monitor.html): Monitor your Capacity Blocks using EventBridge.
- [Logging API calls with CloudTrail](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-blocks-logging-using-cloudtrail.html): Learn about logging Capacity Blocks with AWS CloudTrail.

### [Launch templates](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html)

Learn how to create launch templates to use for storing Amazon EC2 instance launch parameters so that you don't have to specify them every time you launch an Amazon EC2 instance.

- [Restrictions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launch-template-restrictions.html): The restrictions to consider when creating and using Amazon EC2 launch templates.
- [Permissions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/permissions-for-launch-templates.html): Find examples of IAM policy statements that grant users and roles IAM permissions to create and manage launch templates and launch template versions.
- [Control launching instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/use-launch-templates-to-control-launching-instances.html): Learn how to further restrict permissions to help secure your Amazon EC2 resources when using launch templates.
- [Create](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html): Learn how to create Amazon EC2 launch templates.
- [Modify (manage versions)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-launch-template-versions.html): Learn how to create and manage versions of an Amazon EC2 launch template.
- [Delete](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/delete-launch-template.html): Learn how to delete Amazon EC2 launch templates or launch template version.

### [Launch an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html)

Learn about the different methods and options for launching (creating) an Amazon EC2 instance.

### [Tutorials](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-launch-tutorials.html)

Tutorials to help you learn how to launch Amazon EC2 instances for different use cases.

- [Tutorial 1: Launch my first instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/tutorial-launch-my-first-ec2-instance.html): Learn how to launch an Amazon EC2 instance.
- [Tutorial 2: Launch a test instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/tutorial-launch-a-test-ec2-instance.html): Learn how to launch an Amazon EC2 instance to use for testing purposes and connect to it.
- [Instance parameter reference](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-launch-parameters.html): Learn about all the parameters in the Amazon EC2 launch instance wizard and launch template.
- [Launch using the launch instance wizard](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.html): Launch an Amazon EC2 instance from an AMI using the launch instance wizard in the Amazon EC2 console.
- [Launch using a launch template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launch-instances-from-launch-template.html): Learn how to launch Amazon EC2 instances using an Amazon EC2 launch template.
- [Launch from an existing instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launch-more-like-this.html): Use the Launch more like this option in the Amazon EC2 console to launch an Amazon EC2 instance based on an existing instance.
- [Launch from an AWS Marketplace AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launch-marketplace-console.html): Subscribe to an AWS Marketplace AMI and launch an instance from it using the Amazon EC2 console or a command line tool.

### [Connect to your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect.html)

Learn about the different options to connect to your Amazon EC2 instances.

- [General connection prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connection-prereqs-general.html): Review the general prerequisites required to connect to Amazon EC2 instances.

### [Connect to your Linux instance using SSH](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html)

How to connect to your Linux instances using SSH.

- [Connect using an SSH client](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-ssh.html): Connect to your Linux instances using an SSH client.
- [Connect using PuTTY](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-from-windows.html): Connect to your Linux instances from your Windows computer using PuTTY.
- [Transfer files using SCP](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/linux-file-transfer-scp.html): Learn how to transfer files from your computer to your EC2 Linux instance using secure copy protocol (SCP).
- [Manage Linux system users](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/managing-users.html): Add or remove Linux system users on your Amazon EC2 Linux instance.

### [Connect to your Windows instance using RDP](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connecting_to_windows_instance.html)

How to connect to your Windows instance using RDP.

- [Connect using an RDP client](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-rdp.html): Learn how to connect to your EC2 Windows instance using RDP.
- [Connect using Fleet Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-rdp-fleet-manager.html): Learn how to connect to your EC2 Windows instance using Fleet Manager from AWS Systems Manager.
- [Transfer files using RDP](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instanceWindowsFileTransfer.html): Learn how to transfer files from your computer to your EC2 Windows instance using RDP.
- [Connect using Session Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-with-systems-manager-session-manager.html): Learn how to connect to your EC2 instance using Session Manager, a capability of AWS Systems Manager.

### [Connect using a public IP and EC2 Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-eic.html)

Connect to your Linux instances using EC2 Instance Connect.

- [Tutorial](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-tutorial.html): Complete the configuration for EC2 Instance Connect and connect to your Linux instance.
- [Prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-prerequisites.html): Understand the requirements for EC2 Instance Connect.
- [Permissions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-configure-IAM-role.html): Example policies that grant the permissions required by EC2 Instance Connect.
- [Install EC2 Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-set-up.html): Configure your Amazon EC2 instance to support EC2 Instance Connect.
- [Connect to an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-methods.html): Connect to your Linux instances using EC2 Instance Connect using the Amazon EC2 console, the AWS CLI, or an SSH client.
- [Uninstall EC2 Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-uninstall.html): Learn how to disable EC2 Instance Connect by uninstalling the package.

### [Connect using a private IP and EC2 Instance Connect Endpoint](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-with-ec2-instance-connect-endpoint.html)

Connect to your instance using EC2 Instance Connect Endpoint.

- [Permissions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/permissions-for-ec2-instance-connect-endpoint.html): Example policies that grant permissions to create, describe, or modify EC2 Instance Connect Endpoints.
- [Security groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/eice-security-groups.html): Example security group rules for EC2 Instance Connect Endpoint.
- [Create an EC2 Instance Connect Endpoint](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-ec2-instance-connect-endpoints.html): Learn how to create an EC2 Instance Connect Endpoint for your VPC.
- [Modify an EC2 Instance Connect Endpoint](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/modify-ec2-instance-connect-endpoint.html): Modify EC2 Instance Connect Endpoints to change the IP address type, security groups, or client IP settings.
- [Delete an EC2 Instance Connect Endpoint](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/delete-ec2-instance-connect-endpoint.html): Learn how to delete an EC2 Instance Connect Endpoint.
- [Connect to an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-using-eice.html): Learn how to connect to an EC2 instance using EC2 Instance Connect Endpoint.
- [Log connections](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/log-ec2-instance-connect-endpoint-using-cloudtrail.html): Capture detailed information about EC2 Instance Connect Endpoint connections.
- [Service-linked role](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/eice-slr.html): How service-linked roles grant EC2 Instance Connect Endpoint the required access to resources in your AWS account.
- [Quotas](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/eice-quotas.html): Learn about the quotas for EC2 Instance Connect Endpoint.

### [Instance state changes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html)

Describes the state changes for an Amazon EC2, from launch to termination.

### [Stop and start](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html)

Stop and start any instance with an Amazon EBS volume as its root volume.

- [How it works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-ec2-instance-stop-start-works.html): Understand what happens when you stop and start your Amazon EC2 instance.
- [Methods for stopping an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-stop-methods.html): There are four ways to perform a user-initiated stop: default stop, stop with skip OS shutdown, force stop, and force stop with skip OS shutdown.
- [Enable stop protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-stop-protection.html): Learn how to enable stop protection for your Amazon EC2 instances.

### [Hibernate](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html)

Hibernate an Amazon EC2 On-Demand Instance or Spot Instance with an encrypted EBS root volume.

- [How it works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-hibernate-overview.html): Understand how Amazon EC2 instance hibernation works.
- [Prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernating-prerequisites.html): Prerequisites for Amazon EC2 instance hibernation.
- [Configure a Linux AMI to support hibernation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernation-enabled-AMI.html): Instructions for configuring Linux AMIs that require additional configuration to support hibernating Amazon EC2 instances.
- [Enable instance hibernation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enabling-hibernation.html): Learn how to enable hibernation for Amazon EC2 On-Demand Instances and Spot Instances, and see whether hibernation is enabled for an Amazon EC2 instance.
- [Disable KASLR on an instance (Ubuntu only)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernation-disable-kaslr.html): Instructions for disabling KASLR on Amazon EC2 Ubuntu instance before hibernating it.
- [Hibernate an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernating-instances.html): Instructions for hibernating an Amazon EC2 instance and seeing whether an instance has been hibernated using the Amazon EC2 console, AWS CLI and AWS Tools for Windows PowerShell.
- [Start a hibernated instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernating-resuming.html): Instructions for resuming a hibernated Amazon EC2 instance using the Amazon EC2 console, AWS CLI and AWS Tools for Windows PowerShell.
- [Troubleshoot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshoot-instance-hibernate.html): Learn how to diagnose and fix issues that you might encounter when hibernating an Amazon EC2 instance.
- [Reboot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-reboot.html): Use Amazon EC2 to reboot your instance for necessary maintenance.

### [Terminate](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html)

Learn how to terminate and troubleshoot terminating Amazon EC2 instances.

- [How it works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-ec2-instance-termination-works.html): Learn how Amazon EC2 instance termination works and the effects of terminating an instance.
- [Methods for terminating an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-terminate-methods.html): Learn about methods for terminating Amazon EC2 instances, including default termination and termination with skip OS shutdown.
- [Change termination protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_ChangingDisableAPITermination.html): Prevent your Amazon EC2 instance from being accidentally terminated by enabling termination protection.
- [Change initiated shutdown behavior](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_ChangingInstanceInitiatedShutdownBehavior.html): Change the instance initiated shutdown behavior.
- [Preserve data when an instance is terminated](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/preserving-volumes-on-termination.html): Preserve data when an instance is terminated by setting the DeleteOnTermination attribute.
- [Retire](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-retirement.html): Identify Amazon EC2 instances that are scheduled for retirement, and learn what actions to take to manage retirement.

### [Automatic instance recovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html)

Amazon EC2 provides mechanisms for automatic instance recovery that attempt to recover supported instances impacted by underlying AWS hardware or software failures.

- [Verify if automatic recovery occurred](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/verify-if-automatic-recovery-occurred.html): If your instance appears to have been offline and then unexpectedly rebooted, it might have undergone automatic instance recovery in response to an underlying hardware or software issue.
- [Simplified automatic recovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-configuration-recovery.html): Understand the key concepts, requirements, and how to configure simplified automatic recovery for Amazon EC2 instances.
- [CloudWatch action based recovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cloudwatch-recovery.html): Understand the key concepts and requirements for CloudWatch action based instance recovery.

### [Instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html)

Use instance metadata, dynamic data, and user data to configure and manage a running Amazon EC2 instance.

### [Access instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html)

Access instance metadata for an EC2 instance to get current settings for metadata properties, dynamic data, and user data.

- [Use the IMDS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html): Use the Instance Metadata Service (IMDS) to access instance metadata from an Amazon EC2 instance.
- [Transition to IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-metadata-transition-to-version-2.html): Learn how to transition your Amazon EC2 instances to Instance Metadata Service Version 2 (IMDSv2) using recommended tools and a step-by-step migration path.
- [Limit access to IMDS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-metadata-limiting-access.html): To protect your instance metadata, you can configure your instance to limit access to the Instance Metadata Service.

### [Configure IMDS options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html)

Configure instance metadata options to control the accessibility and behavior of the IMDS on an EC2 instance.

- [For new instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html): Learn how to configure instance metadata for your Amazon EC2 instances.
- [For existing instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-existing-instances.html): Learn how to modify the instance metadata configuration for your Amazon EC2 instances.
- [Run commands at launch](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html): You can run commands to perform configuration tasks when you launch an instance by passing in a user data script as input.
- [Example: AMI launch index value](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMI-launch-index-examples.html): See an example that demonstrates how you can use both user data and instance metadata to configure your EC2 instances.
- [Detect whether a host is an EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/identify_ec2_instances.html): Identify whether your application or website is running on an EC2 instance.

### [Instance identity documents](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-identity-documents.html)

The instance identity document is a signed document that includes information about your Amazon EC2 instance.

- [Retrieve the instance identity document](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/retrieve-iid.html): Retrieve an Amazon EC2 instance's instance identity document, in plaintext format, from the Instance Metadata Service.
- [Verify instance identity document](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/verify-iid.html): Cryptographically verify the contents and authenticity of an instance's instance identity document using the PKCS7, base64-encoded, or RSA-2048 signature.
- [Public certificates](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/regions-certs.html): This topic provides the AWS public certificates required to verify the contents of an Amazon EC2 instance's instance identity document.

### [STIG compliance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-configure-stig.html)

Apply Security Technical Implementation Guides (STIG) compliance standards to your EC2 instance.

- [STIG settings](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-stig-settings.html): Determine which STIG hardening settings apply to your EC2 instance based on the operating system and compliance level.
- [Download STIG scripts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-stig-downloads.html): Download STIG hardening script bundles from Amazon S3 to apply to your EC2 instance.
- [Apply STIG settings with Systems Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-stig-ssm-cmd-doc.html): Use Systems Manager to apply STIG settings to your EC2 instance with the AWSEC2-ConfigureSTIG command document.

### [Clock synchronization](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-time.html)

Ensure a consistent and accurate time reference on your Amazon EC2 instance by using the Amazon Time Sync Service on your EC2 instance.

- [Use the local Amazon Time Sync Service](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configure-ec2-ntp.html): Set the time reference on your Amazon EC2 instance to use the local Amazon Time Sync Service or connect to the PTP hardware clock.
- [Use the public Amazon Time Sync Service](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configure-time-sync.html): Set the time reference on your Amazon EC2 instance or any internet-connected device to use the public Amazon Time Sync Service.
- [Compare timestamps for your Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/compare-timestamps-with-clockbound.html): Compare the timestamps on your Amazon EC2 Linux instances with ClockBound to determine the true time of an event.
- [Change the time zone of your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/change-time-zone-of-instance.html): Change the time zone of your Amazon EC2 instance.

### [EC2 Capacity Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-manager.html)

Monitor, analyze, and manage your capacity usage across On-Demand Instances, Spot Instances, and Capacity Reservations from a single location.

### [Enabling Capacity Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enable-capacity-manager.html)

Enable EC2 Capacity Manager with at the account or organization level.

- [Enabling at the Organization-level](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enable-capacity-manager-organizations.html): Enable organization-level visibility and management of your capacity across all member accounts by integrating EC2 Capacity Manager with AWS Organizations.
- [Enabling at the account-level](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enable-capacity-manager-account.html): Enable Capacity Manager within a single AWS account to monitor and analyze capacity usage for On-Demand Instances, Spot Instances, and Capacity Reservations.
- [Registering a delegated administrator](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enable-capacity-manager-da.html): You can register a delegated administrator for Capacity Manager.
- [Using service-linked roles](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-service-linked-roles-cm.html): How to use service-linked roles to give EC2 Capacity Manager access to resources in your AWS account.

### [Organizing your data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-manager-data-organization.html)

How Capacity Manager uses metrics, data points, dimensions, date ranges and periods to organize your capacity data.

- [Capacity Manager metrics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cm-metrics-units.html): Comprehensive selection of metrics for tracking your capacity across different resource types with various measurement units.
- [Grouping and filtering data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/grouping-filtering-data.html): Capacity Manager aggregates your metrics based on the dimensions and date period you choose.
- [Navigating Capacity Manager in the console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-manager-console.html): The Capacity Manager console is organized into tabs that provide different views of your capacity data:

### [Exporting your data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/exporting-cm-data.html)

Export capacity data from EC2 Capacity Manager to Amazon S3 for further analysis, reporting, and integration with other AWS services.

- [Setting up an Amazon S3 bucket for data exports](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cm-set-up-s3-export.html): To receive Capacity Manager data exports, you must have an Amazon S3 bucket in your AWS account to receive and store your export files.
- [Creating a data exports](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-cm-export.html): To create a data export, you can use the Data Exports page in the Capacity Manager console or the AWS CLI.

### [Manage device drivers](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-device-drivers.html)

Manage device drivers for your EC2 instance.

- [AMD drivers](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-amd-driver.html): AMD driver information and install instructions for EC2 instances.

### [NVIDIA drivers](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-nvidia-driver.html)

NVIDIA driver information and install instructions for EC2 instances.

- [AMIs with NVIDIA drivers](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/preinstalled-nvidia-driver.html): Use AMIs that come with NVIDIA drivers to launch your EC2 instances.
- [Install public drivers](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/public-nvidia-driver.html): Download and install NVIDIA public drivers on your EC2 instance.
- [Install GRID drivers](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nvidia-GRID-driver.html): Download and install NVIDIA GRID drivers on your EC2 instance.
- [Install gaming drivers](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nvidia-gaming-driver.html): Download and install NVIDIA gaming drivers on your EC2 instance.

### [Install the ENA driver on Windows](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-adapter-driver-install-upgrade-win.html)

Install the ENA driver on Amazon EC2 Windows instances.

- [ENA Windows driver releases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-driver-releases-windows.html): Track ENA Windows driver version releases.

### [Windows PV drivers](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/xen-drivers-overview.html)

Describes the Windows paravirtual (PV) drivers used by Amazon EC2, including how to upgrade and troubleshoot drivers.

- [Upgrade PV drivers](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Upgrading_PV_drivers.html): Upgrade paravirtual drivers on your EC2 Windows instances.
- [Troubleshoot PV drivers](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/pvdrivers-troubleshooting.html): Troubleshoot PV drivers on Windows instances.

### [AWS NVMe drivers](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/aws-nvme-drivers.html)

AWS NVMe driver information and install instructions for EC2 Windows instances.

- [NVMe Windows driver releases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nvme-driver-version-history.html): AWS NVMe Windows driver version history for EC2 Windows instances.

### [Configure Windows instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-windows-instances.html)

Customize your Windows instance.

### [Windows launch agents](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configure-launch-agents.html)

Learn about Windows launch agents on Amazon EC2 Windows instances, and compare features and operating system support between versions.

- [Configure DNS Suffix](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launch-agents-set-dns.html): Configure the DNS Suffix that Windows launch agents use for domain name resolution.
- [Subscribe to SNS notifications](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launch-agents-subscribe-notifications.html): Subscribe to SNS Topics to receive notifications for Amazon EC2 Windows launch agent notifications.
- [Windows Service administration](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launch-agents-service-admin.html): Perform system administration for the EC2Launch v2 and EC2Config launch agents using Windows Administrative tools and menus.

### [EC2Launch v2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2launch-v2.html)

Use EC2Launch v2 to perform tasks during instance launch or restart, for EC2 Windows instances.

- [Install EC2Launch v2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2launch-v2-install.html): Download and install the latest version of the EC2Launch v2 agent for Windows instances.
- [Configure EC2Launch v2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2launch-v2-settings.html): Configure the EC2Launch v2 agent tasks and settings on Windows instances.
- [Task definitions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2launch-v2-task-definitions.html): Refer to definitions and syntax for EC2Launch v2 tasks that run during launch and restart for EC2 Windows instances.
- [Troubleshoot EC2Launch v2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2launchv2-troubleshooting.html): Review troubleshooting scenarios and view related application and event logs for the EC2Launch v2 agent.
- [Version histories](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2launchv2-versions.html): Review release notes for EC2Launch v2 launch agent versions and the launch agent migration tool.

### [EC2Launch](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2launch.html)

Use EC2Launch v1 to perform tasks during instance launch or restart on Windows Server 2016 and 2019 instances.

- [Install EC2Launch](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2launch-download.html): Manually download and install the latest version of the EC2Launch v1 agent for Windows instances.
- [Configure EC2Launch](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2launch-config.html): After your instance has been initialized the first time, you can configure the EC2Launch v1 agent to customize startup tasks and settings.
- [Version history](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2launch-version-details.html): Review release notes for EC2Launch agent versions.

### [EC2Config service](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2config-service.html)

Configure a Windows instance using the EC2Config service to access advanced features.

- [Install EC2Config](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UsingConfig_Install.html): Manually install the EC2Config launch agent on your instance.
- [Configure proxy settings](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2config-proxy.html): You can configure the EC2Config service to communicate through a proxy.
- [Set EC2Config service properties](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-ec2config-service-properties.html): Use the EC2 Service Properties system dialog to set EC2Config service properties.
- [Troubleshoot EC2Config](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/repair-ec2config.html): Troubleshoot issues with the EC2Config launch agent installed on your instance, such as updating the agent on an instance that is not accessible from RDP.
- [Version history](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2config-version-details.html): Review release notes for EC2Config service launch agent versions.

### [EC2 Fast Launch for Windows](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/win-ami-config-fast-launch.html)

Use EC2 Fast Launch to configure faster launching for Windows instances from pre-provisioned instance snapshots.

- [EC2 Fast Launch prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/win-start-fast-launch-prereqs.html): Prerequisites to set up EC2 Fast Launch to launch Windows instances faster.
- [Configure EC2 Fast Launch settings](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/win-fast-launch-configure.html): Configure fast launch settings for your Amazon EC2 Windows Server AMI.
- [View EC2 Fast Launch AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/win-view-fast-launch.html): Get details for Windows AMIs that have EC2 Fast Launch enabled, with EC2 commands in the AWS CLI, or with Tools for PowerShell Cmdlets.
- [Manage resource costs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/win-fast-launch-manage-costs.html): Manage underlying resource costs for EC2 Fast Launch
- [Monitor EC2 Fast Launch](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/win-fast-launch-monitor.html): Monitor EC2 Fast Launch Windows AMIs that you own.
- [Service-linked role](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/slr-windows-fast-launch.html): Get information about the service-linked role for EC2 Fast Launch that grants Amazon EC2 access to resources to pre-provision Windows instances and create snapshots.
- [Troubleshoot EC2 Fast Launch](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/win-fast-launch-troubleshoot.html): Troubleshoot known issues for EC2 Fast Launch.
- [Change the Windows Administrator password](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-windows-passwords.html): Change the Administrator password for your Amazon EC2 Windows instances.
- [Add Windows System components](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/windows-optional-components.html): Add or configure optional Windows Server components on your Amazon EC2 Windows instance.
- [Install WSL on Windows](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-wsl-on-ec2-windows-instance.html): Install Windows Subsystem for Linux on your Windows instance

### [Windows utilities](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/windows-troubleshooting-utils.html)

Learn about the Amazon EC2 Windows troubleshooting utilities that are available from the EC2WinUtil driver.

- [Windows Utility Driver releases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2winutil-driver-version-history.html): Amazon EC2 troubleshooting utilities (ec2winutil) driver version history for Windows instances.

### [Upgrade Windows instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/serverupgrade.html)

Upgrade an EC2 Windows Server instance to a newer version of Windows.

- [Perform an in-place upgrade](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/os-inplaceupgrade.html): Perform an in-place upgrade on your EC2 Windows instance.
- [Perform an automated upgrade](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/automated-upgrades.html): Use Systems Manager Automation runbooks to upgrade an EC2 Windows instance.
- [Migrate to a Nitro-based instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/migrating-latest-types.html): Migrate a Windows instance to a Nitro-based instance type.
- [Troubleshoot an upgrade](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/os-upgrade-trbl.html): Troubleshoot an operating system upgrade on an EC2 Windows instance.

### [Tutorial: Connect EC2 instance to RDS database](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/tutorial-connect-ec2-instance-to-rds-database.html)

Learn how to connect an Amazon EC2 instance to an Amazon RDS database using the AWS Management Console.

- [Option 1: Automatically connect using EC2 console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/tutorial-ec2-rds-option1.html): Learn how to use the Amazon EC2 console to automatically create the security groups required to connect an Amazon EC2 instance to an Amazon RDS database.
- [Option 2: Automatically connect using RDS console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/tutorial-ec2-rds-option2.html): Learn how to use the Amazon RDS console to automatically create the security groups required to connect an Amazon EC2 instance to an Amazon RDS database.
- [Option 3: Manually connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/tutorial-ec2-rds-option3.html): Learn how to manually create the security groups required to connect an Amazon EC2 instance to an Amazon RDS database.


## [Fleets](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Fleets.html)

- [Which fleet method to use?](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/which-fleet-method-to-use.html): Learn how to decide which fleet method to use when launching Amazon EC2 instances.

### [Configuration options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-configuration-strategies.html)

Learn about the different options for configuring your EC2 Fleet and Spot Fleet.

### [Request types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-request-type.html)

An EC2 Fleet or Spot Fleet request type defines whether the request is synchronous or asynchronous, and whether it makes a one-time request for the desired target capacity or makes a continued effort to maintain the target capacity over time, with options including request and maintain, and instant for EC2 Fleets.

- [EC2 Fleet 'instant' type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instant-fleet.html): Learn how to configure an EC2 Fleet of type instant with detailed examples for different use cases.
- [Spending limit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-control-spending.html): You can set a limit on how much you're willing to spend per hour on your On-Demand Instances and Spot Instances in your EC2 Fleet or Spot Fleet.
- [Attribute-based instance type selection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html): Learn how to use attribute-based instance type selection in your EC2 Fleet or Spot Fleet, where you specify the attributes that an instance must have, and Amazon EC2 identifies all the instance types with those attributes.
- [Instance weighting](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-instance-weighting.html): You can assign a weight to each instance type in your EC2 Fleet or Spot Fleet to reflect their capacity and performance relative to each other, helping you manage the cost and performance of the capacity in your fleet.
- [Allocation strategies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.html): When you use multiple instance types and Availability Zones (referred to as capacity pools) in an EC2 Fleet or Spot Fleet, you can use allocation strategies to manage how Amazon EC2 fulfills your Spot and On-Demand capacities from those capacity pools.
- [Capacity Rebalancing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-capacity-rebalance.html): With Capacity Rebalancing, your EC2 Fleet or Spot Fleet can maintain the desired Spot capacity by proactively replacing Spot Instances at risk of interruption.
- [Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-on-demand-capacity-reservations.html): You can configure an EC2 Fleet to use On-Demand Capacity Reservations first when launching On-Demand Instances.

### [Work with EC2 Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-ec2-fleet.html)

Learn how to create, tag, describe, modify, and delete an EC2 Fleet of On-Demand Instances and Spot Instances.

- [EC2 Fleet request states](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2-fleet-states.html): Learn about the different stages of an EC2 Fleet request lifecycle and the management of instances in each stage.
- [EC2 Fleet prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-prerequisites.html): To create an EC2 Fleet, the following prerequisites must be in place:
- [Create an EC2 Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-ec2-fleet.html): Learn how to create an EC2 Fleet, including the limitations, prerequisites, AWS CLI command, and EC2 Fleet configuration parameters.
- [Tag an EC2 Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/tag-ec2-fleet.html): Learn how to assign tags to an EC2 Fleet request and the instances and volumes it launches when you create the EC2 Fleet, or afterward.
- [Describe an EC2 Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/describe-ec2-fleet.html): Learn how to describe your EC2 Fleet configuration, the instances in your EC2 Fleet, and the event history of your EC2 Fleet.
- [Modify an EC2 Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/modify-ec2-fleet.html): Learn about the parameters that you can modify for an EC2 Fleet of type maintain, including total target capacity, Spot capacity, and On-Demand capacity, and whether running instances should be terminated if the total target capacity is reduced below the current size.
- [Delete an EC2 Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/delete-fleet.html): Learn how to delete an EC2 Fleet request and terminate all its instances, or delete only the EC2 Fleet request but leave the instances running.

### [Work with Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-spot-fleets.html)

Learn how to create, tag, describe, modify, and delete a Spot Fleet of On-Demand Instances and Spot Instances.

- [Spot Fleet request states](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-states.html): Learn about the different stages of a Spot Fleet request lifecycle and the management of instances in each stage.
- [Spot Fleet permissions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-prerequisites.html): If your users will create or manage a Spot Fleet, you need to grant them the required permissions.
- [Create a Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-spot-fleet.html): Learn how to create a Spot Fleet, including the limitations, prerequisites, and Spot Fleet configuration parameters.
- [Tag a Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/tag-spot-fleet.html): Learn how to assign tags to a Spot Fleet request and the instances and volumes it launches when you create the Spot Fleet, or afterward.
- [Describe a Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-spot-fleet.html): Learn how to describe your Spot Fleet configuration, the instances in your Spot Fleet, and the event history of your Spot Fleet.
- [Modify a Spot Fleet request](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/modify-spot-fleet.html): Learn about the parameters that you can modify for a Spot Fleet of type maintain, including total target capacity, Spot capacity, and On-Demand capacity, and whether running instances should be terminated if the total target capacity is reduced below the current size.
- [Cancel (delete) a Spot Fleet request](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cancel-spot-fleet.html): Learn how to cancel (delete) a Spot Fleet request and terminate all its instances, or cancel (delete) only the Spot Fleet request but leave the instances running.

### [Automatic scaling for Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-automatic-scaling.html)

Learn how to use automatically increase or decrease the target capacity of your Spot Fleet based on demand.

- [IAM permissions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-auto-scaling-IAM.html): Grant permission to use the actions and services that support automatic scaling for Spot Fleet by using the provided IAM policy.
- [Target tracking scaling](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-target-tracking.html): Learn how to increase or decreaseâ¨the current capacity of your Spot Fleet by targeting a value for a specific metric.
- [Step scaling](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-step-scaling.html): Learn how to increase or decreaseâ¨the current capacity of your Spot Fleet based on a set of scaling adjustments, known as step adjustments, that vary based on the size of the alarm breach.
- [Scheduled scaling](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-scheduled-scaling.html): Learn how to increase or decrease the current capacity of your Spot Fleet on a scheduled date and time.

### [Monitor your fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/fleet-monitor.html)

Learn how to monitor your EC2 Fleet or Spot Fleet using Amazon CloudWatch and Amazon EventBridge.

- [Monitor your fleet using CloudWatch](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-cloudwatch-metrics.html): Learn about the CloudWatch metrics that Amazon EC2 provides for EC2 Fleet and Spot Fleet.
- [Monitor your fleet using EventBridge](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitor-ec2-fleet-using-eventbridge.html): Learn how to monitor the events that your Amazon EC2 Fleet and Spot Fleet emit, and create rules that trigger programmatic actions in response to the events, using Amazon EventBridge.

### [Tutorials](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/fleet-tutorials.html)

Learn about different ways to configure an EC2 Fleet for different use cases through step-by-step procedures.

- [Tutorial: Configure EC2 Fleet to use instance weighting](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-instance-weighting-walkthrough.html): Learn how to use instance weighting to enable your EC2 Fleet to use any combination of the specified instance types to fulfill the desired target capacity.
- [Tutorial: Configure EC2 Fleet to use On-Demand Instances as the primary capacity](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-on-demand-walkthrough.html): Learn how to specify On-Demand and Spot capacity in your EC2 Fleet configuration.
- [Tutorial: Configure EC2 Fleet to launch On-Demand Instances using targeted Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-launch-on-demand-instances-using-targeted-capacity-reservations-walkthrough.html): Learn how to configure your EC2 Fleet to use Capacity Reservations first when launching On-Demand Instances.
- [Tutorial: Configure your EC2 Fleet to launch instances into Capacity Blocks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-launch-instances-capacity-blocks-walkthrough.html): Learn how to configure your EC2 Fleet to launch instances into Capacity Blocks.
- [Example CLI configurations for EC2 Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-examples.html): Learn how to create EC2 Fleet launch configurations that you can use with the create-fleet command.
- [Example CLI configurations Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-examples.html): Learn how to create Spot Fleet launch configurations that you can use with the request-spot-fleet AWS CLI command.
- [Fleet quotas](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/fleet-quotas.html): Learn about the quotas and limits for Amazon EC2 Spot Fleet and EC2 Fleet.


## [Networking](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-networking.html)

- [Regions and Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html): Describes the Regions, Availability Zones, Local Zones, Outposts, and Wavelength Zones world-wide where you can host your instances.

### [Instance IP addressing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html)

Learn how Amazon EC2 provides your instances with public and private IP addresses and DNS hostnames as well as how to optimize IP address usage.

- [IPv4 addresses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-ip-addresses.html): Learn how to view and assign IPv4 addresses for your EC2 instances.
- [IPv6 addresses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-ipv6-addresses.html): Learn how to view and assign IPv6 addresses for your EC2 instances.
- [Secondary IP addresses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-secondary-ip-addresses.html): Learn how to specify secondary IP addresses for your instances.
- [IPv4 addresses on Windows](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/config-windows-multiple-ip.html): Configure your Windows instance to recognize a secondary private IPv4 address.

### [EC2 instance hostnames and domains](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html)

Understanding EC2 instance hostnames and domains is important for effectively managing and accessing your Amazon EC2 instances.

- [Understanding EC2 instance hostnames and domains](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/understanding-ec2-instance-hostnames-domains.html): A EC2 instance address is made up of different components.
- [Hostname types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hostname-types.html): AWS provides two types of hostnames: private and public.

### [Bring your own IP addresses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html)

Understand the key concepts, benefits, and requirements for BYOIP in Amazon EC2.

- [Prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/prepare-for-byoip.html): Understand the requirements to bring your IP address to Amazon EC2.
- [Onboard your address range](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/byoip-onboard.html): Learn how to onboard your address range to Amazon EC2.
- [Use your address range](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/byoip-working-with.html): Learn how to view and use your BYOIP address ranges.

### [Elastic IP addresses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)

Understand the key concepts, benefits, and behavior for Elastic IP addresses.

- [Associate an Elastic IP address](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-eips.html): Learn how to allocate, associate, and disassociate Elastic IP addresses.
- [Transfer an Elastic IP address](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/transfer-EIPs-intro-ec2.html): Learn how to transfer an Elastic IP address between AWS accounts.
- [Release an Elastic IP address](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing-eips-releasing.html): Learn how to release an Elastic IP address.
- [Use reverse DNS for email applications](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Elastic_Addressing_Reverse_DNS.html): Create a reverse DNS record for your Elastic IP address.

### [Network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html)

Understand the key concepts and requirements for network interfaces.

- [IP addresses per network interface](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AvailableIpPerENI.html): Understand how many network interfaces you can assign to an EC2 instance.
- [Create a network interface](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-network-interface.html): Learn how to create network interfaces for your EC2 instances.
- [Network interface attachments](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/network-interface-attachments.html): Learn how to attach and detach network interfaces.
- [Manage IP addresses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/managing-network-interface-ip-addresses.html): Learn how to assign IP addresses to and unassign IP address from your network interfaces.
- [Modify network interface attributes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/modify-network-interface-attributes.html): Learn how to change the description, security groups, and attributes for a network interface.
- [Multiple network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/scenarios-enis.html): Learn about scenarios for assigning multiple network interfaces to an EC2 instance.
- [Requester-managed network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/requester-managed-eni.html): Understand the creation and use of requester-managed network interfaces.

### [Prefix delegation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-prefix-eni.html)

Understand the key concepts and behavior for network interface prefix delegation.

- [Manage prefixes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-prefixes.html): Learn how to assign prefixes to and unassign prefixes from your network interfaces.
- [Delete a network interface](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/delete_eni.html): Learn how to delete a network interface.

### [Network bandwidth](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html)

Understand the EC2 instance network bandwidth for inbound and outbound traffic.

- [Bandwidth weighting](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configure-bandwidth-weighting.html): Configure bandwidth weighting preferences to direct more bandwidth for your EC2 instance towards network processing or EBS operations depending on your workload.

### [Enhanced networking](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html)

Learn about enhanced networking capabilities on supported EC2 instances.

### [Elastic Network Adapter (ENA)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html)

Enable enhanced networking capabilities with the Elastic Network Adapter (ENA) on supported EC2 instances.

- [Check whether ENA is enabled](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/test-enhanced-networking-ena.html): Test whether enhanced networking is enabled in your instances and your AMIs.
- [Enable ENA for an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enabling_enhanced_networking.html): Enable ENA on an Amazon EC2 instance.
- [ENA queues](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-queues.html): Specify the number of ENA queues to add to an instance.
- [Troubleshoot ENA on Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshooting-ena.html): Troubleshoot the Elastic Network Adapter (ENA) kernel driver on Linux instances.
- [Troubleshoot ENA on Windows](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshoot-ena-driver.html): Troubleshoot the Elastic Network Adapter (ENA) driver for Windows.

### [ENA Express](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-express.html)

Improve network performance between EC2 instances with ENA Express on supported instance types.

- [Review instance settings](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-express-list-view.html): Review ENA Express settings for your EC2 instances
- [Configure instance settings](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-express-configure.html): Configure ENA Express settings for your EC2 instance
- [Intel 82599 VF](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sriov-networking.html): Enable enhanced networking with the Intel 82599 VF interface on EC2 instances.
- [Monitor network performance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-network-performance-ena.html): Monitor network performance for ENA settings for your EC2 instance.
- [Improve network latency on Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-improve-network-latency-linux.html): Improve network latency for EC2 instances that run on Linux.
- [Nitro performance considerations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-nitro-perf.html): Understand performance considerations for Nitro based Amazon EC2 instances.
- [Optimize network performance on Windows](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-os.html): Optimize network performance on EC2 Windows instances.

### [Elastic Fabric Adapter](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html)

Elastic Fabric Adapter (EFA) is a network device that you can attach to your Amazon EC2 instances to accelerate Artificial Intelligence (AI), Machine learning (ML), and High Performance Computing (HPC) workloads.

- [Get started with EFA and MPI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-start.html): Learn how to launch an EFA and MPI-enabled cluster for HPC workloads on Amazon EC2
- [Get started with EFA and NCCL](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-start-nccl.html): Learn how to launch an EFA and NCCL-enabled cluster for machine learning workloads on Amazon EC2
- [Maximize network bandwidth](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-acc-inst-types.html): Learn how to maximize network bandwidth on accelerated computing instance types such as P5 or G6e with Elastic Fabric Adapter (EFA).
- [Create and attach an EFA](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-efa.html): Learn how to create an Elastic Fabric Adapter and attach it to a stopped Amazon EC2 instance.
- [Detach and delete an EFA](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/detach-efa.html): Learn how to detach an Elastic Fabric Adapter from a stopped Amazon EC2 instance, and how to delete it when it is no longer needed.
- [Monitor an EFA](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-working-monitor.html): Learn how to monitor the performance of your Elastic Fabric Adapters.
- [Verify the EFA installer](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-verify.html): Learn how to verify the integrity and authenticity of the EFA installer tarball.
- [Release notes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-changelog.html): The following table describes the version history and changelog for the Elastic Fabric Adapter software.

### [EC2 topology](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-topology.html)

Learn about Amazon EC2 topology, which provides a hierarchical view of the physical host placement of your Amazon EC2 instances and Capacity Reservations.

- [How it works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-ec2-instance-topology-works.html): Understand the key concepts and benefits of Amazon EC2 topology.
- [Prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-topology-prerequisites.html): Understand the requirements to describe the topology of your instances and Capacity Reservations.
- [Examples](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-topology-examples.html): Learn how to use the AWS CLI to describe the instance topology for your EC2 instances.

### [Placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html)

Launch instances in a placement group to cluster them logically into a low-latency group, or to spread them across hardware to reduce the risk of simultaneous failures.

- [Placement strategies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-strategies.html): Understand the concepts and benefits of placement strategies for your placement groups.
- [Create a placement group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-placement-group.html): Learn how to create a placement group for your Amazon EC2 instances.
- [Change instance placement](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/change-instance-placement-group.html): Learn how to change the placement group for an Amazon EC2 instance.
- [Delete a placement group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/delete-placement-group.html): Learn how to delete a placement group for your Amazon EC2 instances.
- [Shared placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/share-placement-group.html): Learn how to share a placement group with another AWS account.
- [Placement groups on AWS Outposts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups-outpost.html): Using placement groups with AWS Outposts.

### [Network MTU](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/network_mtu.html)

The maximum supported MTU for an EC2 instance depends on its instance type.

- [Set the MTU for your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-mtu.html): Learn how to set the MTU for your instances to standard or jumbo frames.
- [Virtual private clouds](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-vpc.html): Learn about the virtual network in which you launch your EC2 instances.
- [Secondary Networks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/secondary-networks.html): Learn about Secondary Networks for high-performance east-west connectivity in machine learning workloads.


## [Security](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security.html)

- [Data protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Amazon Elastic Compute Cloud.
- [Infrastructure security](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/infrastructure-security.html): Learn how Amazon Elastic Compute Cloud isolates service traffic.
- [Resilience](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon EC2 features for data resiliency.
- [Compliance validation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.

### [Identity and access management](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-iam.html)

Control access to Amazon EC2 resources by setting up security groups and using IAM.

- [Identity-based policies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html): Learn how to control user access to your Amazon EC2 resources.
- [Example policies for the API](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ExamplePolicies_EC2.html): Grant users permissions to view and work with specific resources using the Amazon EC2 API.
- [Example policies for the console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-ec2-console.html): Grant users permissions to view and work with specific resources in the Amazon EC2 console.
- [AWS managed policies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon EC2 and recent changes to those policies.

### [IAM roles](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html)

Grant applications on your EC2 instances permissions to make secure API requests to AWS.

- [Retrieve security credentials](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-metadata-security-credentials.html): Get the security credentials for your EC2 instance from the instance metadata.
- [Permissions to attach a role to an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/permission-to-pass-iam-roles.html): Grant a user permissions to attach or remove an IAM role for an EC2 instance.
- [Attach a role to an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/attach-iam-role.html): Learn how to attach, replace, or detach IAM roles for your EC2 instance.
- [Update management](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/update-management.html): Learn about AWS recommendations to maintain your EC2 instances.
- [Best practices for Windows instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-windows-security-best-practices.html): Learn about AWS security recommendations for your Windows instances.

### [Key pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html)

Learn about key pairs which are a set of security credentials you use to connect to your Amazon EC2 instance.

- [Create a key pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html): Learn how to create key pairs using Amazon EC2 or a third-party tool.
- [Describe your key pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/describe-keys.html): Learn how to describe stored key pairs, how to retrieve the public key material, and identify the public key used at launch.
- [Delete your key pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/delete-key-pair.html): Learn how to delete a key pair which removes the stored public key.
- [Add or replace a public key on your Linux instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/replacing-key-pair.html): Learn how to add or replace lost public key on Linux instance.
- [Verify the fingerprint](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/verify-keys.html): Learn how to verify the fingerprint of your key pair.

### [Security groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)

Use security groups and security group rules as a firewall to control traffic to and from your EC2 instances.

- [Create a security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-security-group.html): Learn how to create a security group that controls the inbound and outbound traffic to your Amazon EC2 instance.
- [Change security groups for your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/changing-security-group.html): Learn how to and or remove security groups, or update security group rules.
- [Delete a security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/deleting-security-group.html): Learn how to delete a security group.
- [Connection tracking](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html): Understand the concepts for security group connection tracking.
- [Security group rules for different use cases](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html): Add rules to your security group for specific kinds of access.

### [NitroTPM](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html)

Learn about how the Nitro Trusted Platform Module (NitroTPM) enables measured boot and remote attestation for Amazon EC2 instances.

- [Requirements](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enable-nitrotpm-prerequisites.html): Learn about the prerequisites for enabling and using NitroTPM with Amazon EC2 instances.
- [Enable a Linux AMI for NitroTPM](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enable-nitrotpm-support-on-ami.html): Learn how to configure a new Linux AMI with NitroTPM support during image registration.
- [Verify that an AMI is enabled for NitroTPM](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/verify-nitrotpm-support-on-ami.html): Learn how to verify whether an AMI is enabled for NitroTPM.
- [Enable or stop using NitroTPM](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm-instance.html): Learn how to enable NitroTPM for an Amazon EC2 instance and how to stop using NitroTPM if it is no longer needed.
- [Verify that an instance is enabled for NitroTPM](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/verify-nitrotpm-support-on-instance.html): Learn how to verify whether an Amazon EC2 instance is enabled for NitroTPM.
- [Retrieve the public endorsement key](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/retrieve-ekpub.html): Learn how to securely retrieve the public endorsement key for an Amazon EC2 instance.

### [EC2 instance attestation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm-attestation.html)

Learn how to use NitroTPM for attestation to verify the integrity of your EC2 instances.

### [Attestable AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/attestable-ami.html)

An Attestable AMI is an Amazon Machine Image (AMI) with a corresponding cryptographic hash that represents all of its contents.

- [Build the sample image description](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/build-sample-ami.html): AWS provides a sample Amazon Linux 2023 image description that you can use as a starting point for creating your own custom Attestable AMIs for your workloads.
- [Sample Amazon Linux 2023 image description](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/al2023-isolated-compute-recipe.html): The sample Amazon Linux 2023 image description has the following characteristics:
- [Customize the sample image description](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/customize-sample-ami.html): Learn how to customize the sample Amazon Linux 2023 image description for your workload.
- [Compute PCR measurements](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-pcr-compute.html): The nitro-tpm-pcr-compute utility enables you to generate the reference measurements for an Attestable AMI during build time based on its Unified Kernel Image (UKI).
- [Prepare AWS KMS for attestation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/prepare-attestation-service.html)

### [Get the NitroTPM Attestation Document](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/attestation-get-doc.html)

The Attestation Document is a key component of the NitroTPM attestation process.

- [NitroTPM Attestation Document](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm-attestation-document-content.html): An Attestation Document is generated by the NitroTPM and it is signed by the Nitro Hypervisor.
- [Validate Attestation Document](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm-attestation-document-validate.html)
- [Integrating with AWS KMS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/attestation-attest.html): Your instance should have an application that can make AWS KMS API requests with the Attestation Document retrieved from the NitroTPM.

### [Isolate data from your own operators](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/isolate-data-operators.html)

The AWS Nitro System has zero operator access.

- [Updating Attestable AMIs that have no interactive access](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-isolated-amis.html): Once you launch an instance using an isolated compute environment AMI, there is no way for any user or operator to connect to the instance.
- [Credential Guard for Windows instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/credential-guard.html): Understand the concepts, requirements, and usage of Credential Guard.
- [AWS PrivateLink](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interface-vpc-endpoints.html): Learn how to use AWS PrivateLink to connect to Amazon EC2 using private connectivity.


## [Storage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Storage.html)

### [Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/storage_ebs.html)

Learn how Amazon EBS provides scalable, high-performance block storage resources that can be used with Amazon EC2 instances.

- [EBS volume limits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/volume_limits.html): Understand the volume limits for your Amazon EC2 instances.
- [EBS cards](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs_cards.html): Learn about EBS cards and how they affect EBS-optimized performance for EC2 instances.

### [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)

Learn how Amazon EC2 instance store provides local, temporary block storage for Amazon EC2 instances.

- [Data persistence](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-lifetime.html): Learn how data stored on Amazon EC2 instance store volumes persists during various instance events.
- [Instance store volume limits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-volumes.html): Learn about which Amazon EC2 instance types support instance store volumes.
- [SSD instance store volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ssd-instance-store.html): Some Amazon EC2 instances support solid state drives (SSD) to deliver high random I/O performance.

### [Add instance store volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/add-instance-store-volumes.html)

Add an instance store volume to an Amazon EC2 instance at launch and then prepare it for use.

- [Add instance store volumes to an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/adding-instance-storage-ami.html): Learn how to add block device mappings for Amazon EC2 instance store volumes to an AMI.
- [Add instance store volumes to an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/adding-instance-storage-instance.html): Learn how to add block device mappings for Amazon EC2 instance store volumes to an instance during launch.
- [Make instance store volumes available for use](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/making-instance-stores-available-on-your-instances.html): Learn how to format and mount an instance store volume to make it available for use with an Amazon EC2 instance.
- [Enable swap volume for M1 and C1 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-swap-volumes.html): Use instance store swap volume as swap space on a Amazon EC2 M1 and C1 instance with limited physical memory.
- [Initialize instance store volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/disk-performance.html): Initialize instance store volumes on previous generation Amazon EC2 instances to optimize disk performance.
- [Detailed performance statistics instance store volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nvme-detailed-performance-stats.html): EBS detailed performance statistics provide real-time, high-resolution I/O performance statistics for Amazon EBS volumes attached to Nitro-based Amazon EC2 instances.

### [Root volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/RootDeviceStorage.html)

Learn about the types of root volumes available for your Amazon EC2 instances.

- [Keep root volume after instance termination](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configure-root-volume-delete-on-termination.html): Configure whether the Amazon EBS root volume of your Amazon EC2 instance is deleted or preserved at instance termination.
- [Replace a root volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/replace-root.html): Replace the Amazon EBS root volume for an Amazon EC2 instance with a replacement volume while it is in the running state.
- [Device names for volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html): Learn about the device names you can use for Amazon EBS and instance store volumes of your Amazon EC2 instance.

### [Block device mappings](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html)

Use a block device mapping to specify additional EBS volumes or instance store volumes for your instance when it's launched.

- [Add block device mapping to AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-block-device-mapping.html): Learn how to specify a block device mapping for an Amazon EC2 AMI.
- [Add block device mapping to instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-block-device-mapping.html): Learn how to specify a block device mapping for an Amazon EC2 instance.

### [How volumes are attached and mapped for Windows instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-windows-volumes.html)

Map Windows disks to the Amazon EBS and instance store volumes that are attached to an Amazon EC2 Windows instance.

- [Map NVME disks to volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/windows-list-disks-nvme.html): Learn how to find the NVMe disks on an Amazon EC2 Windows instance and how to map the Windows disk numbers to Amazon EBS volume IDs.
- [Map non-NVME disks to volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/windows-list-disks.html): Learn how to find the non-NVME disks on an Amazon EC2 Windows instance and how to map the Windows disk numbers to Amazon EBS volume IDs.

### [Torn write prevention](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/storage-twp.html)

Use torn write prevention with block storage on your Amazon EC2 Linux instance to accelerate your relational database workloads.

- [Supported block sizes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/supported-block-sizes.html): Learn about the supported block sizes and block boundary alignments for using torn write prevention on Amazon EC2 instances.
- [Requirements](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/twp-reqs.html): Learn about the requirements for using torn write prevention on Amazon EC2 Linux instances.
- [Check instance support](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/twp-namespace.html): Confirm whether an Amazon EC2 instance and its attached volumes support torn write prevention.
- [Configure workload](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configure-twp.html): Learn how to configure a MySQL or MariaDB workload on an Amazon EC2 Linux instance for torn write prevention.

### [Windows VSS EBS snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/application-consistent-snapshots.html)

Use the Windows VSS based Amazon EBS snapshot components and Systems Manager scripts to create EBS snapshots for Windows instances.

### [VSS prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/application-consistent-snapshots-prereqs.html)

Before you create VSS based EBS snapshots for your EC2 Windows instance, you must meet system requirements and other prerequisites.

- [IAM permissions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vss-iam-reqs.html): Use the AWSEC2VssSnapshotPolicy managed policy to grant permissions for your EC2 Windows instance to create VSS based EBS snapshots.
- [VSS components](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/application-consistent-snapshots-getting-started.html): Ensure that you have the latest version of the VSS components package installed on your Windows instance before you create VSS based EBS snapshots.

### [Create VSS snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-vss-snaps.html)

You can create VSS based snapshots of EBS volumes that are attached to your EC2 instances.

- [Use Systems Manager command documents](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-vss-snapshots-ssm.html): You can use AWS Systems Manager command documents to create VSS based EBS snapshots for your EC2 Windows instance.
- [Troubleshoot VSS snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/application-consistent-snapshots-troubleshooting.html): Check events and logs to help troubleshoot issues with Windows VSS based EBS snapshots.
- [Restore options for the AWS VSS solution](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/application-consistent-snapshots-restore.html): You can restore EBS volumes for a Windows instance from VSS based snapshots created by the AWS VSS solution.
- [Version history](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vss-comps-history.html): Review release notes for the AwsVssComponents package, as well as component and script version requirements for each supported version of Windows Server.

### [Object storage, file storage, and file caching](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/file-storage.html)

Learn about the object storage, file storage, and file caching storage solutions that can be used along with the block storage on your Amazon EC2 instances.

- [Amazon S3](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonS3.html): Use Amazon S3 as a repository for internet data that provides access to reliable, fast, and inexpensive data storage infrastructure.
- [Amazon EFS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEFS.html): Use Amazon EFS to create an EFS file system and mount it to one or more of your Linux instances.
- [Amazon FSx](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/storage_fsx.html): Use Amazon FSx to launch highly durable and available file systems that can be accessed from thousands of instances using the industry-standard protocols.
- [Amazon File Cache](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEFC.html): Use Amazon File Cache as a temporary, high-performance storage location for data.


## [Manage resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/resources.html)

- [Select a Region for your resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones-setup.html): Learn how to use the Region selector to select a Region for your Amazon EC2 resources.
- [Find your resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html): List and filter your Amazon EC2 resources using the AWS Management Console.
- [AWS Global View](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/global-view.html): View your Amazon EC2 and Amazon VPC resources across AWS Regions using AWS Global View.

### [Tag your resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html)

Manage your Amazon EC2 instances, images, and other resources by assigning your own metadata tags.

- [Tag resource permissions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/supported-iam-actions-tagging.html): Create IAM policies to enable users to tag Amazon EC2 resources on creation.
- [Add and remove tags](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags_Console.html): Learn how to add tags to your Amazon EC2 resources.
- [Filter resources by tag](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/filtering-the-list-by-tag.html): Learn how to filter Amazon EC2 resources by tag.
- [View tags using instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.html): Learn how to view the tags for your Amazon EC2 instances using instance metadata.
- [Service quotas](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html): View your current quotas (also referred to as limits) for Amazon EC2 and request increases in these quotes as needed.


## [Monitor resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring_ec2.html)

### [Monitor the status of your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check.html)

Learn about the monitoring tools available for Amazon EC2 instances.

### [Status checks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html)

Learn about the different types of status checks available for Amazon EC2 instances and how they can be used to detect any problems with your instances.

- [View status checks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_status.html): Learn how to view the status checks for your Amazon EC2 instances.
- [Create status check alarms](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating_status_check_alarms.html): Create or edit a CloudWatch alarm that notifies you when an instance has a failed status check.

### [State change events](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instance-state-changes.html)

Learn about state change events for Amazon EC2 instances.

- [Create alarm for instance state changes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-events-eventbridge-example.html): Create an Amazon EventBridge alarm that sends an email notification when an Amazon EC2 instance's state changes.

### [Scheduled events](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.html)

Learn about scheduled events for Amazon EC2 instances.

- [Manage instances scheduled to stop or retire](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/schedevents_actions_retire.html): Learn about the recommended actions that you can take when your Amazon EC2 instance is scheduled to stop or retire.
- [Manage instances scheduled for reboot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/schedevents_actions_reboot.html): Learn about the recommended actions that you can take when your Amazon EC2 instance is scheduled to reboot.
- [Manage instances scheduled for maintenance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/schedevents_actions_maintenance.html): Learn about the recommended actions that you can take when your Amazon EC2 instance is scheduled for maintenance.
- [View scheduled events](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_scheduled_events.html): View scheduled events that affect your Amazon EC2 instances and related resources.
- [Customize scheduled event notifications](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/customizing_scheduled_event_notifications.html): Customize the information included in email notifications for scheduled events that affect your Amazon EC2 instances.
- [Reschedule scheduled events](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/reschedule-event.html): Reschedule a scheduled event that affects your Amazon EC2 instance so that it occurs at a date and time that suits you.
- [Create custom event windows](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html): Create custom event windows for scheduled events that reboot, stop, or terminate your Amazon EC2 instances.

### [Monitor your instances using CloudWatch](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch.html)

Monitor your Amazon EC2 instances using Amazon CloudWatch to collect and process raw data from instances into readable, near real-time metrics.

- [Instance alarms](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-alarms.html): From the Instances screen in the Amazon EC2 console, you can view, create, and edit Amazon CloudWatch alarms for your instances.
- [Manage detailed monitoring](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-detailed-monitoring.html): Enable detailed monitoring for your EC2 instance.
- [CloudWatch metrics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html): Learn about the default metrics that Amazon EC2 sends to CloudWatch for the following 5 minutes of activity from the start time.
- [Install and configure the CloudWatch agent](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-and-configure-cloudwatch-agent-using-ec2-console.html): To collect additional CloudWatch metrics beyond the basic default metrics, use the Amazon EC2 console to install the CloudWatch agent on your Amazon EC2 instances and configure the agent to emit selected metrics.

### [Statistics for metrics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring_get_statistics.html)

Learn about statistics for the CloudWatch metrics for your instances.

- [Get statistics for a specific instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/US_SingleMetricPerInstance.html): Learn how to get statistics for a specific EC2 instance using the AWS Management Console or the AWS CLI.
- [Aggregate statistics across instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/GetSingleMetricAllDimensions.html): Learn how to get and aggregate statistics across instances using the AWS Management Console or the AWS CLI.
- [Aggregate statistics by Auto Scaling group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/GetMetricAutoScalingGroup.html): Learn how to get statistics aggregated according to the Auto Scaling group.
- [Aggregate statistics by AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/US_SingleMetricPerAMI.html): Learn how to get statistics aggregated by AMI for instances that have detailed monitoring enabled.
- [View monitoring graphs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/graphs-in-the-aws-management-console.html): Learn how to view the monitoring graphs for your instance.
- [Create an alarm](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-createalarm.html): Learn how to create an CloudWatch alarm for a CloudWatch metric.

### [Create alarms that stop, terminate, reboot, or recover an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UsingAlarmActions.html)

Create CloudWatch alarms that automatically stop, terminate, reboot, or recover your Amazon EC2 instances.

- [Amazon CloudWatch alarm action scenarios](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AlarmActionScenarios.html): Learn about the scenarios for Amazon CloudWatch alarm actions for Amazon EC2.
- [Automate using EventBridge](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/automating_with_eventbridge.html): Use EventBridge to automate Amazon EC2 and respond automatically to system events.
- [Log API calls using CloudTrail](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitor-with-cloudtrail.html): Capture detailed information about the calls make to the Amazon EC2 API calls using AWS CloudTrail.
- [Monitor .NET and SQL Server applications](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-appinsights.html): Information about CloudWatch Application Insights.
- [Track your Free Tier usage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-free-tier-usage.html): Monitor your usage of the Free Tier offers for Amazon EC2.
- [Billing and usage reports](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-billing-usage-reports.html): Learn about activity related to Amazon EC2 in the AWS billing and usage reports.
- [Inventory your EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-data-inventory.html): Learn how to identify key characters of your Amazon EC2 instances so that you can create functionally equivalent servers.


## [Troubleshoot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-troubleshoot.html)

- [Instance launch issues](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshooting-launch.html): Troubleshoot issues that occur when you attempt to launch an Amazon EC2 instance.
- [Instance stop issues](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesStopping.html): Troubleshoot issues where your Amazon EC2 instance appears stuck in the stopping process.
- [Instance termination issues](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesShuttingDown.html): Troubleshoot issues where your Amazon EC2 instance fails to terminate or shut down.

### [Unreachable instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshoot-unreachable-instance.html)

Troubleshoot unreachable Amazon EC2 instances.

- [Common screenshots for Windows instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ics-common.html): Learn how to troubleshoot an unreachable Windows instance based on screenshots returned by the service.
- [Linux instance SSH issues](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.html): Troubleshoot issues when attempting to connect to your Amazon EC2 Linux instance using SSH.
- [Linux instance failed status checks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstances.html): Troubleshoot issues when your Amazon EC2 Linux instance fails a status check.
- [Linux instance boots from wrong volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-booting-from-wrong-volume.html): Troubleshoot issues that cause your Amazon EC2 Linux instance to boot from the wrong volume.
- [Windows instance RDP issues](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshoot-connect-windows-instance.html): Troubleshoot issues when attempting to connect to your Amazon EC2 Windows instance using RDP.
- [Windows instance start issues](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/common-messages.html): Learn how to solve password and activation issues with your Amazon EC2 Windows instances.
- [Windows instance issues](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/win-ts-common-issues.html): Learn how to solve issues with your Amazon EC2 Windows instances.

### [Reset Windows administrator password](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ResettingAdminPassword.html)

Learn how to reset a lost or expired Windows administrator password for an Amazon EC2 Windows instance.

- [Reset password using EC2Launch v2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ResettingAdminPassword_EC2Launchv2.html): Reset the Windows administrator password for an Amazon EC2 instance using a Windows 2016 or later AMI with the EC2Launch v2 agent.
- [Reset password using EC2Launch](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ResettingAdminPassword_EC2Launch.html): Reset the Windows administrator password for an Amazon EC2 instance using a Windows Server 2016 or later AMI.
- [Reset password using EC2Config](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ResettingAdminPassword_EC2Config.html): Reset the Windows administrator password for an Amazon EC2 instance using a Windows AMI before Windows Server 2016.
- [Troubleshoot Sysprep issues](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sysprep-troubleshoot.html): Learn how to troubleshoot system preparation (Sysprep) errors when you create an image from an Amazon EC2 Windows instance.

### [EC2Rescue for Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Linux-Server-EC2Rescue.html)

Learn how to diagnose and troubleshoot impaired Amazon EC2 Linux instances using EC2Rescue.

- [Install EC2Rescue](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2rl_install.html): Learn how to install EC2Rescue on an Amazon EC2 Linux instance.
- [Run EC2Rescue commands](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2rl_working.html): Learn how to run EC2Rescue commands to diagnose, analyze, and remediate an impaired Amazon EC2 Linux instance.
- [Develop EC2Rescue modules](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2rl_moduledev.html): Learn how to create your own custom EC2Rescue modules for diagnosing, troubleshooting, and remediating Amazon EC2 Linux instances.

### [EC2Rescue for Windows instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Windows-Server-EC2Rescue.html)

Learn how to diagnose and troubleshoot impaired Amazon EC2 Windows Server instances using EC2Rescue.

- [Troubleshoot using EC2Rescue GUI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2rw-gui.html): Troubleshoot impaired Amazon EC2 Windows Server instances using the EC2Rescue GUI.
- [Troubleshoot using EC2Rescue CLI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2rw-cli.html): Troubleshoot impaired Amazon EC2 Windows Server instances using the EC2Rescue command line interface.
- [Troubleshoot using EC2Rescue and Systems Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2rw-ssm.html): Troubleshoot impaired Amazon EC2 Windows Server instances using EC2Rescue and AWS Systems Manager automation.

### [EC2 Serial Console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-serial-console.html)

Use the Amazon EC2 serial console to diagnose and troubleshoot possible issues with your Amazon EC2 Linux and Windows instances.

- [Prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-serial-console-prerequisites.html): Learn the prerequisites for gaining access to the serial console on Amazon EC2 instances.
- [Configure access to the EC2 Serial Console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configure-access-to-serial-console.html): Learn about the different levels of access to the EC2 Serial Console and how to configure access.
- [Connect to the EC2 Serial Console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-serial-console.html): Learn how to Connect to the EC2 Serial Console and details about different types of clients.
- [Disconnect from the EC2 Serial Console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/disconnect-serial-console-session.html): Learn how to disconnect from the EC2 Serial Console session.
- [Troubleshoot your instance using the EC2 Serial Console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshoot-using-serial-console.html): See examples of troubleshooting your Windows or Linux instance using the EC2 Serial Console.
- [Send diagnostic interrupts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/diagnostic-interrupt.html): Send a diagnostic interrupt to an unreachable Amazon EC2 instance to generate a crash dump file.
