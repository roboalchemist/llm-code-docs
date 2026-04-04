# Source: https://docs.aws.amazon.com/appstream2/latest/developerguide/llms.txt

# Amazon WorkSpaces Applications Administration Guide

> Use WorkSpaces Applications to stream stream desktop applications to users without rewriting applications.

- [Setting Up](https://docs.aws.amazon.com/appstream2/latest/developerguide/setting-up.html)
- [Get Started: Set Up With Sample Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/getting-started.html)
- [Quotas](https://docs.aws.amazon.com/appstream2/latest/developerguide/limits.html)
- [Document History](https://docs.aws.amazon.com/appstream2/latest/developerguide/doc-history.html)

## [What Is Amazon WorkSpaces Applications?](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html)

- [Features](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-features.html): Using Amazon WorkSpaces Applications provides the following advantages:
- [Key Concepts](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-concepts.html): To get the most out of WorkSpaces Applications, be familiar with the following concepts:
- [How to Get Started](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-how-to-start.html): If you are using WorkSpaces Applications for the first time, you can use the Try it Now feature or follow the tutorial (both are available in the WorkSpaces Applications console).
- [Accessing](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-accessing.html): You can work with WorkSpaces Applications using any of the following interfaces:


## [Networking and Access](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-network.html)

- [Internet Access](https://docs.aws.amazon.com/appstream2/latest/developerguide/internet-access.html): If your fleets, app block builders, and image builders require internet access, you can enable internet access in several ways.

### [VPC Requirements](https://docs.aws.amazon.com/appstream2/latest/developerguide/appstream-vpc.html)

When you set up WorkSpaces Applications, you must specify the virtual private cloud (VPC) and at least one subnet in which to launch your fleet instances and image builders.

- [VPC Setup Recommendations](https://docs.aws.amazon.com/appstream2/latest/developerguide/vpc-setup-recommendations.html): When you create a fleet, or launch an image builder or app block builder, you specify the VPC and one or more subnets to use.

### [Configure a VPC with Private Subnets and a NAT Gateway](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-network-internet-NAT-gateway.html)

If you plan to provide your streaming instances (fleet instances, app block builders, and image builders) with access to the internet, we recommend that you configure a VPC with two private subnets for your streaming instances and a NAT gateway in a public subnet.

- [Create and Configure a New VPC](https://docs.aws.amazon.com/appstream2/latest/developerguide/create-configure-new-vpc-with-private-public-subnets-nat.html): This topic describes how to use the VPC wizard to create a VPC with a public subnet and one private subnet.
- [Add a NAT Gateway to an Existing VPC](https://docs.aws.amazon.com/appstream2/latest/developerguide/add-nat-gateway-existing-vpc.html): If you have already configured a VPC, complete the following steps to add a NAT gateway to your VPC.

### [Internet Access for Your Fleet, Image Builder, or App Block Builder](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-network-manual-enable-internet-access.html)

After your NAT gateway is available on a VPC, you can enable internet access for your fleet, image builder, and app block builder.

- [Internet Access for Your Fleet](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-network-manual-fleet-enable-internet-access-fleet.html): You can enable internet access either when you create the fleet or later.
- [Internet Access for Your Image Builder](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-network-manual-enable-internet-access-image-builder.html): If you plan to enable internet access for your image builder, you must do so when you create the image builder.
- [Internet Access for Your App Block Builder](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-network-enable-internet-access-app-block-builder.html): If you plan to enable internet access for your app block builder, you must do so when you create the app block builder.
- [Configure a VPC with a Public Subnet](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-network-default-internet-access.html): If you created your Amazon Web Services account after 2013-12-04, you have a default VPC in each AWS Region that includes default public subnets.
- [Use the Default VPC and Public Subnet](https://docs.aws.amazon.com/appstream2/latest/developerguide/default-vpc-with-public-subnet.html): Your Amazon Web Services account, if it was created after 2013-12-04, has a default VPC in each AWS Region.
- [Amazon S3 VPC Endpoints](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-network-vpce-iam-policy.html): When you enable Application Settings Persistence or Home folders on a stack, WorkSpaces Applications uses the VPC you specify for your fleet to provide access to Amazon Simple Storage Service (Amazon S3) buckets.

### [Connections to Your VPC](https://docs.aws.amazon.com/appstream2/latest/developerguide/appstream2-port-requirements-appstream2.html)

Learn how to set up the ports required for WorkSpaces Applications connections to your VPC

- [Network Interfaces](https://docs.aws.amazon.com/appstream2/latest/developerguide/network-interfaces.html): Each WorkSpaces Applications streaming instance has the following network interfaces:
- [Management Network Interface IP Address Range and Ports](https://docs.aws.amazon.com/appstream2/latest/developerguide/management_ports.html): The management network interface IP address range is 198.19.0.0/16.
- [Customer Network Interface Ports](https://docs.aws.amazon.com/appstream2/latest/developerguide/primary_ports.html): Follow the guidance below for customer network interface ports.

### [User Connections to WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/user-connections-to-appstream2.html)

Learn about user connections to WorkSpaces Applications, including bandwidth recommendations, required ports and domains, and how to create and stream from interface VPC endpoints (interface endpoints).

- [Bandwidth Recommendations](https://docs.aws.amazon.com/appstream2/latest/developerguide/bandwidth-recommendations-user-connections.html): To optimize the performance of WorkSpaces Applications, make sure that your network bandwidth and latency can sustain your users' needs.
- [IP Address and Port Requirements](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-ports.html): WorkSpaces Applications users' devices require outbound access on port 443 (TCP) and port 8433 (UDP) when using the internet endpoints, and if you are using DNS servers for domain name resolution, port 53 (UDP).
- [Allowed Domains](https://docs.aws.amazon.com/appstream2/latest/developerguide/allowed-domains.html): For WorkSpaces Applications users to access streaming instances, you must allow the following domain on the network from which users initiate access to the streaming instances.


## [Image Builders](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-image-builders.html)

- [Launch an Image Builder](https://docs.aws.amazon.com/appstream2/latest/developerguide/tutorial-image-builder-create.html): To install and configure applications to stream to your users, you start by launching an image builder instance as described in the following procedure.

### [Connect to an Image Builder](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-image-builders-connect.html)

You can connect to an image builder by doing either of the following:

- [Console (Web Connection)](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-image-builders-connect-console.html): To use the WorkSpaces Applications console to connect to an image builder through a web browser, complete the following steps.
- [Streaming URL (Client or Web Connection)](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-image-builders-connect-streaming-URL.html): You can create a streaming URL to connect to an image builder through a web browser or the WorkSpaces Applications client.
- [Image Builder Actions](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-image-builders-actions.html): You can perform the following actions on an image builder, depending on the current state (status) of the image builder instance.
- [Instance Metadata for Image Builders](https://docs.aws.amazon.com/appstream2/latest/developerguide/user-instance-metadata-image-builders.html): Learn about instance metadata for WorkSpaces Applications image builders
- [Install AMD Driver on Graphics Design Instances](https://docs.aws.amazon.com/appstream2/latest/developerguide/AMD-driver.html): If you need to update the AMD driver on your Windows Image Builder that is using a Graphics Design instance, you can either use the latest WorkSpaces Applications Graphics Design base images, or download the AMD driver and install it on your Image Builder.
- [Base Image and Managed Image Update Release Notes](https://docs.aws.amazon.com/appstream2/latest/developerguide/base-image-version-history.html): Version and release history for WorkSpaces Applications base and managed images


## [Images](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-images.html)

### [Default Settings and Application Launch Performance](https://docs.aws.amazon.com/appstream2/latest/developerguide/customizing-appstream-images.html)

Learn about defining default application and Windows settings for users and optimizing the launch performance of applications.

- [Creating Default Application and Windows Settings](https://docs.aws.amazon.com/appstream2/latest/developerguide/creating-default-app-Windows-settings.html): Learn about creating default application and Windows settings for your WorkSpaces Applications users
- [Optimizing the Launch Performance of Your Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/optimizing-app-launch-performance.html): Learn about optimizing the launch performance of your applications

### [Manage Agent Versions](https://docs.aws.amazon.com/appstream2/latest/developerguide/base-images-agent.html)

Learn how to manage WorkSpaces Applications agent versions.

- [Create an Image That Uses the Latest Version of the Agent](https://docs.aws.amazon.com/appstream2/latest/developerguide/create-image-that-always-uses-latest-agent.html): Learn how to create an image that always uses the latest version of the WorkSpaces Applications agent.
- [Create an Image That Uses a Specific Version of the Agent](https://docs.aws.amazon.com/appstream2/latest/developerguide/create-image-that-uses-specific-agent.html): Learn how to create an image that uses a specific version of the WorkSpaces Applications agent.
- [Create an Image That Uses a Newer Version of the Agent](https://docs.aws.amazon.com/appstream2/latest/developerguide/create-image-that-uses-newer-agent.html): Learn how to create an image that uses a newer version of the WorkSpaces Applications agent
- [Agent Release Notes](https://docs.aws.amazon.com/appstream2/latest/developerguide/agent-software-versions.html): Version and release history for the WorkSpaces Applications agent
- [Tutorial: Create a Custom Image by Using the Console](https://docs.aws.amazon.com/appstream2/latest/developerguide/tutorial-image-builder.html): Complete these steps to learn how to create a custom WorkSpaces Applications image by using the WorkSpaces Applications console.

### [Administer Your Images](https://docs.aws.amazon.com/appstream2/latest/developerguide/administer-images.html)

Learn how to administer your WorkSpaces Applications images.

- [Delete a Private Image](https://docs.aws.amazon.com/appstream2/latest/developerguide/delete-private-image.html): You can delete your private images when you no longer need them.
- [Copy an Image That You Own to Another Region](https://docs.aws.amazon.com/appstream2/latest/developerguide/copy-image-different-region.html)
- [Share an Image That You Own With Another Account](https://docs.aws.amazon.com/appstream2/latest/developerguide/share-image-with-another-account.html): WorkSpaces Applications images are a regional resource, so you can share an image that you own with other AWS accounts within the same AWS Region.
- [Stop Sharing an Image That You Own](https://docs.aws.amazon.com/appstream2/latest/developerguide/stop-sharing-image-with-all-accounts.html): Follow these steps to stop sharing an image that you own with any other AWS account.

### [Keep Your Image Up-to-Date](https://docs.aws.amazon.com/appstream2/latest/developerguide/keep-image-updated.html)

You can keep your WorkSpaces Applications image up-to-date by doing either of the following:

- [Update an Image by Using Managed WorkSpaces Applications Image Updates](https://docs.aws.amazon.com/appstream2/latest/developerguide/keep-image-updated-managed-image-updates.html): WorkSpaces Applications provides an automated way to update your image with the latest Windows operating system updates, license included application updates, driver updates, and WorkSpaces Applications agent software.
- [Update the WorkSpaces Applications Agent Software by Using Managed WorkSpaces Applications Agent Versions](https://docs.aws.amazon.com/appstream2/latest/developerguide/keep-image-updated-manage-image-versions.html): WorkSpaces Applications provides an automated way to update your image builder with newer WorkSpaces Applications agent software.
- [Windows Update and Antivirus Software](https://docs.aws.amazon.com/appstream2/latest/developerguide/windows-update-antivirus-software.html): WorkSpaces Applications streaming instances are non-persistent.
- [Programmatically Create a New Image](https://docs.aws.amazon.com/appstream2/latest/developerguide/create-image-programmatically.html): You can create WorkSpaces Applications images programmatically by connecting to an image builder and using the Image Assistant command line interface (CLI) operations.

### [Manage License Included Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/license-included-applications.html)

You can stream the following Microsoft license included applications using WorkSpaces Applications.

- [View the list of license included applications installed on your image](https://docs.aws.amazon.com/appstream2/latest/developerguide/view-list-image.html)
- [View the list of license included applications on your image builder](https://docs.aws.amazon.com/appstream2/latest/developerguide/view-list-apps.html)
- [Install or uninstall license included applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/install-uninstall-apps.html)
- [Enable updates for license included applications on image builder](https://docs.aws.amazon.com/appstream2/latest/developerguide/updates-image-builder.html)
- [Enable updates for license included applications on image builder with Powershell](https://docs.aws.amazon.com/appstream2/latest/developerguide/enable-updates-managed-powershell.html)
- [Enable updates for license included applications on image builder with Managed Image Update](https://docs.aws.amazon.com/appstream2/latest/developerguide/enable-updates-managed.html)

### [Import Image](https://docs.aws.amazon.com/appstream2/latest/developerguide/import-image.html)

Learn how to import EC2 AMIs to create WorkSpaces Applications images.

- [Applications Details](https://docs.aws.amazon.com/appstream2/latest/developerguide/applications-details.html): Learn about application PreWarm manifests and app catalog configurations.
- [Export Image](https://docs.aws.amazon.com/appstream2/latest/developerguide/export-image.html): Learn how to export WorkSpaces Applications images to create EC2 AMIs.

### [Create Your Image Programmatically](https://docs.aws.amazon.com/appstream2/latest/developerguide/programmatically-create-image.html)

Learn how to create a custom WorkSpaces Applications image by using the Image Assistant CLI operations.

- [Default Application and Windows Settings](https://docs.aws.amazon.com/appstream2/latest/developerguide/create-default-app-windows-settings-image-assistant.html): You can create default application and Windows settings so that your users can get started with their applications quickly.
- [Launch Performance of Your Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/optimize-app-launch-performance-image-assistant-cli.html): WorkSpaces Applications lets you optimize the launch performance of your applications for your usersâ streaming sessions.
- [Process Overview](https://docs.aws.amazon.com/appstream2/latest/developerguide/process-overview-creating-image-programmatically-image-assistant-cli.html): You can use the Image Assistant CLI operations with your application installation automation to create a fully programmatic WorkSpaces Applications image creation workflow.
- [Image Assistant CLI Operations](https://docs.aws.amazon.com/appstream2/latest/developerguide/cli-operations-managing-creating-image-image-assistant.html): This section describes the Image Assistant CLI operations that you can use to create and manage your WorkSpaces Applications image.

### [Create Your Linux-Based Images](https://docs.aws.amazon.com/appstream2/latest/developerguide/create-linux-based-images.html)

Learn how to create Linux-based images.

- [Creating Default Application Settings for Your Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/create-default-app-settings.html): Follow these steps to create default application settings for your users.
- [Creating Default Environment Variables for Your Linux Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/create-default-variables-linux.html): You can create environment variables on a Linux Image Builder instance.
- [Optimizing the Launch Performance of Your Linux Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/optimize-launch-performance.html): If you are using the Image Assistant GUI tool, the tool optimizes launch performance for your applications automatically.
- [Creating Session Scripts](https://docs.aws.amazon.com/appstream2/latest/developerguide/create-session-scripts.html): WorkSpaces Applications provides on-instance session scripts on both Windows- and Linux-based streaming instances.
- [Using the Image Assistant CLI Tool for Linux](https://docs.aws.amazon.com/appstream2/latest/developerguide/image-assistant-cli.html): On a Linux-based image builder, you can use the Image Assistant CLI tool AppStreamImageAssistant to create and manage your WorkSpaces Applications image.
- [Enabling and Disabling Webcam Support](https://docs.aws.amazon.com/appstream2/latest/developerguide/webcam-support.html): WorkSpaces Applications supports real-time audio-video (AV) by redirecting local webcam video input to WorkSpaces Applications streaming sessions.
- [Enabling and Disabling Heavy File Sync Mode for Home Folders](https://docs.aws.amazon.com/appstream2/latest/developerguide/heavy-file-sync.html): You can enable Amazon Simple Storage Service Home Folders options for your organization.
- [Tutorial: Create a Custom Linux-Based Image](https://docs.aws.amazon.com/appstream2/latest/developerguide/tutorial-create-linux-image.html): Complete these steps to learn how to create a custom Linux-based WorkSpaces Applications image.
- [Tutorial: Enable Japanese Support](https://docs.aws.amazon.com/appstream2/latest/developerguide/enable-japanese-support-linux.html): Complete these steps to learn how to enable japanese support for your linux images.

### [Session Scripts to Manage Your Users' Streaming Experience](https://docs.aws.amazon.com/appstream2/latest/developerguide/use-session-scripts.html)

Learn about using on-instance session scripts to manage your users' streaming experience.

- [Run Scripts Before Streaming Sessions Begin](https://docs.aws.amazon.com/appstream2/latest/developerguide/run-scripts-before-streaming-sessions-begin.html): Learn about running scripts before streaming sessions begin.
- [Run Scripts After Streaming Sessions End](https://docs.aws.amazon.com/appstream2/latest/developerguide/run-scripts-after-streaming-sessions-end.html): Learn about running scripts after streaming sessions end.
- [Create and Specify Session Scripts](https://docs.aws.amazon.com/appstream2/latest/developerguide/create-specify-session-scripts.html): Learn how to create and specify session scripts.
- [Session Scripts Configuration File](https://docs.aws.amazon.com/appstream2/latest/developerguide/session-script-configuration-file.html): Learn about the session scripts configuration file.
- [Using Windows PowerShell Files](https://docs.aws.amazon.com/appstream2/latest/developerguide/using-powershell-files-with-session-scripts.html): Learn about using Windows PowerShell files.
- [Logging Session Script Output](https://docs.aws.amazon.com/appstream2/latest/developerguide/logging-session-output.html): Learn about logging session script output.
- [Use Storage Connectors with Session Scripts](https://docs.aws.amazon.com/appstream2/latest/developerguide/use-storage-connectors-with-session-scripts.html): Learn how to use storage connectors with session scripts.
- [Enable Amazon S3 Bucket Storage for Session Script Logs](https://docs.aws.amazon.com/appstream2/latest/developerguide/enable-S3-bucket-storage-session-script-logs.html): Learn how to enable Amazon S3 bucket storage for your session script logs.
- [Use Session Scripts on Multi-Session Fleets](https://docs.aws.amazon.com/appstream2/latest/developerguide/session-scripts-multi-session-fleets.html): Learn how to use session scripts with multi-session fleets


## [Applications Manager](https://docs.aws.amazon.com/appstream2/latest/developerguide/app-blocks-applications.html)

### [App Blocks](https://docs.aws.amazon.com/appstream2/latest/developerguide/app-blocks.html)

App blocks represent a virtual hard disk (VHD) that is stored within an Amazon S3 bucket within your account that contains the application files and binaries necessary to launch the applications your users will use.

### [Custom App Blocks](https://docs.aws.amazon.com/appstream2/latest/developerguide/custom-app-blocks.html)

Elastic fleet streaming instances utilize applications that are installed on virtual hard disk (VHD) files stored within an Amazon S3 bucket in your account.

- [Create the VHD](https://docs.aws.amazon.com/appstream2/latest/developerguide/create-vhd.html): A VHD is a single file that when mounted to the operating system is treated like a hard disk.

### [Create the Setup Script for the VHD](https://docs.aws.amazon.com/appstream2/latest/developerguide/create-setup-script.html)

WorkSpaces Applications uses a setup script that you provide to mount the VHD before the application launches.

- [App block setup script execution](https://docs.aws.amazon.com/appstream2/latest/developerguide/script-execution.html): The following diagrams indicate where in the process the setup script runs.
- [Create a Custom App Block](https://docs.aws.amazon.com/appstream2/latest/developerguide/create-app-block.html): You can use the WorkSpaces Applications console to create the app block resource once you have your VHD and setup script created and uploaded to an S3 bucket in your AWS account.
- [Update the App Block, VHD, and Setup Script](https://docs.aws.amazon.com/appstream2/latest/developerguide/update-app-block.html): App block resources are immutable and do not allow you to change them once created.

### [WorkSpaces Applications App Blocks](https://docs.aws.amazon.com/appstream2/latest/developerguide/appstream-app-blocks.html)

Elastic fleet streaming instances utilize applications that are installed on virtual hard disk (VHD) files stored within an Amazon S3 bucket in your account.

- [Overview](https://docs.aws.amazon.com/appstream2/latest/developerguide/appstream-app-blocks-overview.html): To create an app block with WorkSpaces Applications packaging, you need to initiate a streaming session with an app block builder.
- [Unsupported Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/appstream-app-blocks-unsupported.html): Applications might encounter failures when installing or running in the following scenarios:
- [Create an WorkSpaces Applications App Block](https://docs.aws.amazon.com/appstream2/latest/developerguide/appstream-app-blocks-create.html): Follow these steps to create an app block with the WorkSpaces Applications packaging type.
- [Activate an App Block](https://docs.aws.amazon.com/appstream2/latest/developerguide/appstream-app-blocks-activate.html): If an app block with WorkSpaces Applications packaging was created, but the application package (VHD) was not attached to it, then the app block will be in an inactive state, and it can't be used to associate applications with Elastic fleets.
- [Create an App Block with an Existing App Package](https://docs.aws.amazon.com/appstream2/latest/developerguide/appstream-app-blocks-create-VHD.html): You can use your existing application package (VHD) with WorkSpaces Applications packaging to create WorkSpaces Applications app blocks.
- [Test an App Block](https://docs.aws.amazon.com/appstream2/latest/developerguide/appstream-app-blocks-test.html): You can use an app block builder to test your app block and verify your application functionalities.
- [Associate an App Block](https://docs.aws.amazon.com/appstream2/latest/developerguide/appstream-app-blocks-associate.html): In order to create, test, or activate your app block with WorkSpaces Applications packaging, you need to associate it with an app block builder.
- [Disassociate an App Block](https://docs.aws.amazon.com/appstream2/latest/developerguide/appstream-app-blocks-disassociate.html): If all your app block builders are associated with other app blocks, and you want to test, create, or activate another app block, then you can either create a new app block builder, or disassociate an existing app block builder from the app block and use it with the new app block.
- [Unsupported Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/app-blocks-unsupported.html): Applications might encounter failures when installing or running in the following scenarios:

### [App Block Builder](https://docs.aws.amazon.com/appstream2/latest/developerguide/app-block-builder.html)

An app block builder is a reusable resource that you can use to package your applications (or app block).

- [Create an App Block Builder](https://docs.aws.amazon.com/appstream2/latest/developerguide/create-app-block-builder.html): You can use app block builder instance to create your application package for WorkSpaces Applications Elastic fleets.

### [Connect to an App Block Builder](https://docs.aws.amazon.com/appstream2/latest/developerguide/connect-app-block-builder.html)

You can connect to an app block builder by doing either of the following:

- [Console (Browser Connection)](https://docs.aws.amazon.com/appstream2/latest/developerguide/connect-app-block-builder-console.html): To use the WorkSpaces Applications console to connect to an app block builder through a browser, complete the following steps.
- [Streaming URL (Client or Browser Connection)](https://docs.aws.amazon.com/appstream2/latest/developerguide/connect-app-block-builder-streaming.html): You can create a streaming URL to connect to an app block builder through a browser or the WorkSpaces Applications client.
- [App Block Builder Actions](https://docs.aws.amazon.com/appstream2/latest/developerguide/app-block-builder-actions.html): You can perform the following actions on an app block builder, depending on the current state (status) of the app block builder instance.
- [Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/applications-elastic.html): Applications contain the details necessary to launch your application after the VHD has been mounted.

### [Store Application Icon, Setup Script, Session Script, and VHD in an S3 Bucket](https://docs.aws.amazon.com/appstream2/latest/developerguide/store-s3-bucket.html)

You must store the application icons, setup scripts, session scripts, and VHDs that you use for your applications and app blocks in an Amazon Simple Storage Service (Amazon S3) bucket in your AWS account.

- [Amazon S3 Bucket Permissions](https://docs.aws.amazon.com/appstream2/latest/developerguide/s3-permissions.html): The Amazon S3 bucket that you choose must have a bucket policy that provides sufficient access to the WorkSpaces Applications service principal to access and download objects from the Amazon S3 bucket.
- [Associate Applications to Elastic Fleets](https://docs.aws.amazon.com/appstream2/latest/developerguide/associate-elastic.html): Applications must be associated to Elastic fleets before they appear to users in the application catalog to be launched.
- [Additional Resources](https://docs.aws.amazon.com/appstream2/latest/developerguide/additional-resources-app-blocks.html): The following links provide information and other resources to help you package and deliver your applications with Elastic fleets.


## [Fleets and Stacks](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-stacks-fleets.html)

- [Session Context](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-stacks-fleets-session-context.html): You can pass parameters to your streaming application by using either of the following methods:
- [Fleet Types](https://docs.aws.amazon.com/appstream2/latest/developerguide/fleet-type.html): Learn about Amazon WorkSpaces Applications fleet types.
- [Instance Families](https://docs.aws.amazon.com/appstream2/latest/developerguide/instance-types.html): Learn about Amazon WorkSpaces Applications instance types.

### [Create a Fleet and Stack](https://docs.aws.amazon.com/appstream2/latest/developerguide/set-up-stacks-fleets.html)

Learn how to create an WorkSpaces Applications fleet and stack.

- [Create a Fleet](https://docs.aws.amazon.com/appstream2/latest/developerguide/set-up-stacks-fleets-create.html): Set up and create a fleet from which user applications are launched and streamed.
- [Create a Stack](https://docs.aws.amazon.com/appstream2/latest/developerguide/set-up-stacks-fleets-install.html): Set up and create a stack to control access to your fleet.
- [Provide Access to Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/set-up-stacks-fleets-add.html): After you create a stack with an associated fleet, you can provide access to users through the WorkSpaces Applications user pool, SAML 2.0 [single sign-on (SSO)], or the WorkSpaces Applications API.
- [Clean Up Resources](https://docs.aws.amazon.com/appstream2/latest/developerguide/set-up-stacks-fleets-finish.html): You can stop your running fleet and delete your active stack to free up resources and to avoid unintended charges to your account.

### [Customize a Fleet](https://docs.aws.amazon.com/appstream2/latest/developerguide/customize-fleets.html)

Learn how to customize an WorkSpaces Applications fleet to optimize your users' application streaming experience.

### [Persist Environment Variables](https://docs.aws.amazon.com/appstream2/latest/developerguide/customize-fleets-persist-environment-variables.html)

Environment variables enable you to dynamically pass settings across applications.

- [Change System Environment Variables](https://docs.aws.amazon.com/appstream2/latest/developerguide/customize-fleets-system-environment-variables.html): Follow these steps to change system environment variables across your fleet instances.
- [Change User Environment Variables](https://docs.aws.amazon.com/appstream2/latest/developerguide/customize-fleets-user-environment-variables.html): Follow these steps to change user environment variables across your fleet instances.
- [Create an Environment Variable That is Limited in Scope](https://docs.aws.amazon.com/appstream2/latest/developerguide/customize-fleets-environment-variable-limited-scope.html): Follow these steps to create an environment variable that is limited in scope to the processes that are spawned off the script.
- [Set Default File Associations](https://docs.aws.amazon.com/appstream2/latest/developerguide/customize-fleets-set-default-file-associations.html): The associations for application file extensions are set on a per-user basis and so are not automatically applied to all users who launch WorkSpaces Applications streaming sessions.
- [Disable Internet Explorer Enhanced Security Configuration](https://docs.aws.amazon.com/appstream2/latest/developerguide/customize-fleets-disable-ie-esc.html): Internet Explorer Enhanced Security Configuration (ESC) places servers and Internet Explorer in a configuration that limits exposure to the internet.

### [Change the Default Internet Explorer Home Page](https://docs.aws.amazon.com/appstream2/latest/developerguide/customize-fleets-change-ie-homepage.html)

You can use Group Policy to change the default Internet Explorer home page for users' streaming sessions.

- [Use Group Policy to Change the Default Internet Explorer Home Page](https://docs.aws.amazon.com/appstream2/latest/developerguide/customize-fleets-change-ie-homepage-group-policy.html): In Active Directory environments, you use the Group Policy Management (GPMC) MMC-snap-in to set a default home page that users can't change.
- [Use the WorkSpaces Applications Template User Account to Change the Default Internet Explorer Home Page](https://docs.aws.amazon.com/appstream2/latest/developerguide/customize-fleets-change-ie-homepage-template-user.html): Follow these steps to use the Template User account to change the default Internet Explorer home page.
- [User and Instance Metadata](https://docs.aws.amazon.com/appstream2/latest/developerguide/customize-fleets-user-instance-metadata-fleets.html): WorkSpaces Applications fleet instances have user and instance metadata available through Windows environment variables.

### [Update a Fleet](https://docs.aws.amazon.com/appstream2/latest/developerguide/update-fleets-new-image.html)

Learn how to update an WorkSpaces Applications fleet.

- [Update a Fleet with a New Image](https://docs.aws.amazon.com/appstream2/latest/developerguide/update-fleets.html): To apply operating system updates or make new applications available to users, create a new image that has these changes.
- [Manage Applications Associated to an Elastic Fleet](https://docs.aws.amazon.com/appstream2/latest/developerguide/manage-apps.html): You can associate and disassociate applications from an Elastic fleet at any time.

### [Fleet Auto Scaling](https://docs.aws.amazon.com/appstream2/latest/developerguide/autoscaling.html)

Use or disable scaling with Amazon WorkSpaces Applications fleets.

- [Scaling Concepts](https://docs.aws.amazon.com/appstream2/latest/developerguide/autoscaling-concepts.html): WorkSpaces Applications scaling is provided by Application Auto Scaling.
- [Managing Fleet Scaling Using the Console](https://docs.aws.amazon.com/appstream2/latest/developerguide/autoscaling-console.html): You can set up and manage fleet scaling by using the WorkSpaces Applications console in either of the following two ways: During fleet creation, or any time, by using the Fleets tab.
- [Managing Fleet Scaling Using the CLI](https://docs.aws.amazon.com/appstream2/latest/developerguide/autoscaling-cli.html): You can set up and manage fleet scaling by using the AWS Command Line Interface (AWS CLI).
- [Additional Resources](https://docs.aws.amazon.com/appstream2/latest/developerguide/autoscaling-additional-resources.html): For step-by-step guidance for working with WorkSpaces Applications Fleet Auto Scaling, see Scaling Your Desktop Application Streams with Amazon AppStream 2.0 in the AWS Compute Blog.
- [Multi-Session Recommendations](https://docs.aws.amazon.com/appstream2/latest/developerguide/multi-session-recs.html): When deciding the maximum number of user sessions on an instance in a multi-session environment, you should consider several factors to ensure optimal performance and streaming experience.


## [User Authentication](https://docs.aws.amazon.com/appstream2/latest/developerguide/authentication-authorization.html)

### [User Pools](https://docs.aws.amazon.com/appstream2/latest/developerguide/user-pool.html)

Use the WorkSpaces Applications user pool to manage users.

- [User Pool End User Experience](https://docs.aws.amazon.com/appstream2/latest/developerguide/user-pool-end-user.html): The following steps summarize the initial connection experience for users in the user pool.
- [Resetting a Forgotten Password](https://docs.aws.amazon.com/appstream2/latest/developerguide/user-pool-end-user-reset-password.html): If users forget their password, follow these steps to connect to the login portal link (provided in the welcome email) and choose a new password.

### [User Pool Administration](https://docs.aws.amazon.com/appstream2/latest/developerguide/user-pool-admin.html)

To create and manage users in the user pool, sign in to the WorkSpaces Applications console for the AWS Region you want and choose User Pool in the left navigation pane.

- [Creating a User](https://docs.aws.amazon.com/appstream2/latest/developerguide/user-pool-admin-create.html): You must enter a valid and unique email address for each new user within a Region.
- [Deleting a User](https://docs.aws.amazon.com/appstream2/latest/developerguide/user-pool-admin-deleting-user.html): You can enable or disable a user, but you cannot delete a user by using the WorkSpaces Applications console.
- [Assigning Stacks to Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/user-pool-admin-assigning.html): You can assign one or more stacks to one or more users in the user pool.
- [Unassigning Stacks from Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/user-pool-admin-unassigning.html): You can unassign a stack from one or more users in the user pool.
- [Disabling Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/user-pool-admin-disabling.html): You can disable one or more users in the user pool, one at a time.
- [Enabling Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/user-pool-admin-enabling.html): You can enable one or more users in the user pool, one at a time.
- [Re-Sending Welcome Email](https://docs.aws.amazon.com/appstream2/latest/developerguide/user-pool-admin-email.html): You can re-send the welcome email with connection instructions to users in the user pool.

### [SAML 2.0 Integration](https://docs.aws.amazon.com/appstream2/latest/developerguide/external-identity-providers.html)

Use external identity providers for single sign-on WorkSpaces Applications access.

- [Example Authentication Workflow](https://docs.aws.amazon.com/appstream2/latest/developerguide/external-identity-providers-example.html): The following diagram illustrates the authentication flow between WorkSpaces Applications and a third-party identity provider (IdP).
- [Setting Up SAML](https://docs.aws.amazon.com/appstream2/latest/developerguide/external-identity-providers-setting-up-saml.html): To enable users to sign in to WorkSpaces Applications by using their existing credentials, and start streaming applications, you can set up identity federation using SAML 2.0.
- [WorkSpaces Applications Integration with SAML 2.0](https://docs.aws.amazon.com/appstream2/latest/developerguide/external-identity-providers-further-info.html): The following links help you configure third-party SAML 2.0 identity provider solutions to work with WorkSpaces Applications.


## [Using Active Directory](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory.html)

- [Active Directory Domains](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-overview.html): Using Active Directory domains with WorkSpaces Applications requires an understanding of how they work together and the configuration tasks that you'll need to complete.

### [Before You Begin](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-prerequisites.html)

Before you use Microsoft Active Directory domains with WorkSpaces Applications, be aware of the following requirements and considerations.

- [Active Directory Domain Environment](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-prerequisites-domain-environment.html): Your active directory domain environment must meet the following requirements.
- [Domain-Joined WorkSpaces Applications Streaming Instances](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-prerequisites-streaming-instances.html): SAML 2.0-based user federation is required for application streaming from domain-joined Always-On and On-Demand fleets.
- [Group Policy Settings](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-prerequisites-group-policy-settings.html): Verify your configuration for the following Group Policy settings.
- [Smart Card Authentication](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-prerequisites-smart-card-authentication.html): WorkSpaces Applications supports the use of Active Directory domain passwords or smart cards such as Common Access Card (CAC) and Personal Identity Verification (PIV) smart cards for Windows sign in to WorkSpaces Applications streaming instances.
- [Tutorial: Setting Up](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-directory-setup.html): To use Active Directory with WorkSpaces Applications, you must first register your directory configuration by creating a Directory Config object in WorkSpaces Applications.

### [Certificate-Based Authentication](https://docs.aws.amazon.com/appstream2/latest/developerguide/certificate-based-authentication.html)

You can use certificate-based authentication with WorkSpaces Applications fleets joined to Microsoft Active Directory.

- [Prerequisites](https://docs.aws.amazon.com/appstream2/latest/developerguide/certificate-based-authentication-prereq.html): Complete the following steps before you use certificate-based authentication.
- [Enable Certificate-based Authentication](https://docs.aws.amazon.com/appstream2/latest/developerguide/certificate-based-authentication-enable.html): Complete the following steps to enable certificate-based authentication.

### [Manage Certificate-based Authentication](https://docs.aws.amazon.com/appstream2/latest/developerguide/certificate-based-authentication-manage.html)

After you enable certificate-based authentication, review the following tasks.

- [Private CA Certificate](https://docs.aws.amazon.com/appstream2/latest/developerguide/certificate-based-authentication-manage-CA.html): In a typical configuration, the private CA certificate has a validity period of 10 years.
- [End User Certificates](https://docs.aws.amazon.com/appstream2/latest/developerguide/certificate-based-authentication-manage-certs.html): End user certificates issued by AWS Private CA for WorkSpaces Applications certificate-based authentication don't require renewal or revocation.
- [Audit Reports](https://docs.aws.amazon.com/appstream2/latest/developerguide/certificate-based-authentication-manage-audit.html): You can create an audit report to list all of the certificates that your private CA has issued or revoked.
- [Logging and Monitoring](https://docs.aws.amazon.com/appstream2/latest/developerguide/certificate-based-authentication-manage-logging.html): You can use CloudTrail to record API calls to a private CA by WorkSpaces Applications.
- [Enable Cross-account PCA Sharing](https://docs.aws.amazon.com/appstream2/latest/developerguide/pca-sharing.html): Private CA (PCA) cross-account sharing offers the ability to grant permissions for other accounts to use a centralized CA.

### [Administration](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-admin.html)

Setting up and using Active Directory with WorkSpaces Applications involves the following administrative tasks.

- [Granting Permissions to Create and Manage Active Directory Computer Objects](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-permissions.html): To allow WorkSpaces Applications to perform Active Directory computer object operations, you need an account with sufficient permissions.
- [Finding the Organizational Unit Distinguished Name](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-oudn.html): When you register your Active Directory domain with WorkSpaces Applications, you must provide an organizational unit (OU) distinguished name.

### [Granting Local Administrator Rights on Image Builders](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-image-builder-local-admin.html)

By default, Active Directory domain users do not have local administrator rights on image builder instances.

- [Using Group Policy preferences](https://docs.aws.amazon.com/appstream2/latest/developerguide/group-policy.html): You can use Group Policy preferences to grant local administrator rights to Active Directory users or groups and to all computer objects in the specified OU.
- [Using the local Administrators group on the image builder](https://docs.aws.amazon.com/appstream2/latest/developerguide/manual-procedure.html): To grant Active Directory users or groups local administrator rights on your image builder, you can manually add these users or groups to the local Administrators group on the image builder.
- [Updating the Service Account Used for Joining the Domain](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-service-acct.html): To update the service account that WorkSpaces Applications uses for joining the domain, we recommend using two separate service accounts for joining image builders and fleets to your Active Directory domain.
- [Locking the Streaming Session When the User is Idle](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-session-lock.html): WorkSpaces Applications relies on a setting that you configure in the GPMC to lock the streaming session after your user is idle for specified amount of time.
- [Editing the Directory Configuration](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-config-edit.html): After a WorkSpaces Applications directory configuration has been created, you can edit it to add, remove, or modify organizational units, update the service account username, or update the service account password.
- [Deleting a Directory Configuration](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-config-delete.html): You can delete an WorkSpaces Applications directory configuration that is no longer needed.
- [Configuring WorkSpaces Applications to Use Domain Trusts](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-domain-trusts.html): WorkSpaces Applications supports Active Directory domain environments where network resources such as file servers, applications, and computer objects reside in one domain, and the user objects reside in another.
- [Managing WorkSpaces Applications Computer Objects in Active Directory](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-identify-objects.html): WorkSpaces Applications does not delete computer objects from Active Directory.
- [More Info](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-more-info.html): For more information related to this topic, see the following resources:


## [Add Custom Branding](https://docs.aws.amazon.com/appstream2/latest/developerguide/branding.html)

- [Custom Branding Options](https://docs.aws.amazon.com/appstream2/latest/developerguide/branding-options.html): You can customize the appearance of the streaming application catalog page by using the following branding options.
- [Adding Custom Branding](https://docs.aws.amazon.com/appstream2/latest/developerguide/branding-add-custom-branding.html): To customize WorkSpaces Applications with your organizational branding, use the WorkSpaces Applications console to select the stack to customize, and then add your branding.
- [Custom Redirect URL and Feedback URL](https://docs.aws.amazon.com/appstream2/latest/developerguide/branding-specifying-feedback-URL.html): You can specify a URL to which your users are redirected when they end their streaming session, as well as a URL where your users can submit feedback.
- [Previewing Custom Branding Changes](https://docs.aws.amazon.com/appstream2/latest/developerguide/branding-previewing-changes.html): You can preview how your branding changes will appear to your users by applying your branding changes to a test stack before you apply them to a production stack, and then creating a streaming URL for the test stack.
- [Color Theme Palettes](https://docs.aws.amazon.com/appstream2/latest/developerguide/branding-color-themes.html): When you choose a color theme, the colors for that theme are applied to the website links, text, and buttons in your streaming application catalog page.


## [Embed Streaming Sessions](https://docs.aws.amazon.com/appstream2/latest/developerguide/embed-streaming-sessions.html)

- [Prerequisites](https://docs.aws.amazon.com/appstream2/latest/developerguide/embed-streaming-sessions-prerequisites.html): To embed an WorkSpaces Applications streaming session in a website, you must have the following:
- [Recommendations and Usage Considerations](https://docs.aws.amazon.com/appstream2/latest/developerguide/embed-streaming-sessions-recommendations-considerations.html): Consider the following recommendations and usage notes for embedded WorkSpaces Applications streaming sessions.
- [Step 1: Specify a Host Domain](https://docs.aws.amazon.com/appstream2/latest/developerguide/specify-host-domain-embedded-streaming-sessions.html): To embed an WorkSpaces Applications streaming session in a webpage, first update your stack to specify the domain to host the embedded streaming session.
- [Step 2: Create a Streaming URL](https://docs.aws.amazon.com/appstream2/latest/developerguide/create-streaming-url-user-authentication.html): You must create a streaming URL to authenticate users for embedded WorkSpaces Applications streaming sessions.
- [Step 3: Download the Embedded Files](https://docs.aws.amazon.com/appstream2/latest/developerguide/download-embed-files.html): To host embedded WorkSpaces Applications streaming sessions, you must download and configure the provided WorkSpaces Applications API JavaScript file.
- [Step 4. Configure Your Website for Integration](https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-website-for-integration.html): The following sections provide information about how to configure your webpage to host embedded WorkSpaces Applications streaming sessions.
- [Constants, Functions, and Events](https://docs.aws.amazon.com/appstream2/latest/developerguide/constants-functions-events-embedded-sessions.html): The following topics provide reference information for constants, functions, and events that you can use to configure embedded WorkSpaces Applications streaming sessions.


## [Administer Persistent Storage](https://docs.aws.amazon.com/appstream2/latest/developerguide/persistent-storage.html)

### [Administer Home Folders](https://docs.aws.amazon.com/appstream2/latest/developerguide/home-folders.html)

Enable and administer home folders to provide persistent storage for your WorkSpaces Applications users.

- [Files and Directories Associated with Compute-Intensive Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/storage-solutions-files-directories-associated-with-compute-intensive-applications.html): During WorkSpaces Applications streaming sessions, saving large files and directories associated with compute-intensive applications to persistent storage can take longer than saving files and directories required for basic productivity applications.
- [Enable Home Folders for Your WorkSpaces Applications Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/enable-home-folders.html): Before enabling home folders, you must do the following:

### [Administer Your Home Folders](https://docs.aws.amazon.com/appstream2/latest/developerguide/home-folders-admin.html)

Review the following topics to learn how to administer your home folders.

- [Disable Home Folders](https://docs.aws.amazon.com/appstream2/latest/developerguide/home-folders-admin-disabling.html): You can disable home folders for a stack without losing user content already stored in home folders.
- [Amazon S3 Bucket Storage](https://docs.aws.amazon.com/appstream2/latest/developerguide/home-folders-s3.html): WorkSpaces Applications manages user content stored in home folders by using Amazon S3 buckets created in your account.
- [Home Folder Content Synchronization](https://docs.aws.amazon.com/appstream2/latest/developerguide/home-folders-content-synchronization.html): When home folders are enabled, WorkSpaces Applications creates a unique folder for each user in which to store their content.
- [Home Folder Formats](https://docs.aws.amazon.com/appstream2/latest/developerguide/home-folders-admin-folders.html): The hierarchy of a user folder depends on how a user launches a streaming session, as described in the following sections.
- [Using the AWS Command Line Interface or AWS SDKs](https://docs.aws.amazon.com/appstream2/latest/developerguide/home-folders-admin-cli.html): You can enable and disable home folders for a stack by using the AWS CLI or AWS SDKs.
- [Additional Resources](https://docs.aws.amazon.com/appstream2/latest/developerguide/home-folders-admin-additional.html): For more information about managing Amazon S3 buckets and best practices, see the following topics in the Amazon Simple Storage Service User Guide:

### [Administer Google Drive](https://docs.aws.amazon.com/appstream2/latest/developerguide/google-drive.html)

Enable Google Drive for Google Workspace to provide persistent storage for your WorkSpaces Applications users.

- [Enable Google Drive for Your WorkSpaces Applications Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/enable-google-drive.html): Before enabling Google Drive, you must do the following:
- [Disable Google Drive for Your WorkSpaces Applications Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/disable-google-drive.html): You can disable Google Drive for a stack without losing user content that is already stored on Google Drive.

### [Administer OneDrive for Business](https://docs.aws.amazon.com/appstream2/latest/developerguide/onedrive.html)

Enable OneDrive for Business to provide persistent storage for your WorkSpaces Applications users.

- [Enable OneDrive for Your WorkSpaces Applications Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/enable-onedrive.html): Before enabling OneDrive, you must do the following:
- [Disable OneDrive for Your WorkSpaces Applications Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/disable-onedrive.html): You can disable OneDrive for a stack without losing user content that is already stored on OneDrive.

### [Administer Custom Shared Folders (SMB Network Drives)](https://docs.aws.amazon.com/appstream2/latest/developerguide/enable-smb-network-drives.html)

You can enable one or more options for your organization.

- [Map Server Message Block (SMB) Network Drives](https://docs.aws.amazon.com/appstream2/latest/developerguide/map-smb-network-drives.html): You can use any machine that is under the targeted network of the SMBs.


## [Enable Application Settings Persistence for Your Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/app-settings-persistence.html)

- [How Application Settings Persistence Works](https://docs.aws.amazon.com/appstream2/latest/developerguide/how-it-works-app-settings-persistence.html): Learn how application settings persistence works.

### [Enabling Application Settings Persistence](https://docs.aws.amazon.com/appstream2/latest/developerguide/enabling-app-settings-persistence.html)

Learn how to enable application settings persistence for your WorkSpaces Applications users.

- [Prerequisites for Enabling Application Settings Persistence](https://docs.aws.amazon.com/appstream2/latest/developerguide/prerequisites-app-settings-persistence.html): Learn about the prerequisites for enabling application settings persistence for your WorkSpaces Applications users.
- [Best Practices for Application Settings Persistence](https://docs.aws.amazon.com/appstream2/latest/developerguide/best-practices-app-settings-persistence.html): Learn about best practices for enabling application settings persistence for your WorkSpaces Applications users.
- [How to Enable Application Settings Persistence](https://docs.aws.amazon.com/appstream2/latest/developerguide/howto-enable-app-settings-persistence.html): Learn how to enable application settings persistence for your WorkSpaces Applications users.

### [Administer the VHDs for Your Users' Application Settings](https://docs.aws.amazon.com/appstream2/latest/developerguide/administer-app-settings-vhds.html)

Learn how to administer the Virtual Hard Disks (VHD) files for your WorkSpaces Applications users' application settings.

- [Amazon S3 Bucket Storage](https://docs.aws.amazon.com/appstream2/latest/developerguide/app-persistence-s3-buckets.html): When you enable application settings persistence, your usersâ application customizations and Windows settings are automatically saved to a Virtual Hard Disk (VHD) file that is stored in an Amazon S3 bucket created in your AWS account.
- [Reset a User's Application Settings](https://docs.aws.amazon.com/appstream2/latest/developerguide/app-persistence-s3-reset.html): To reset a user's application settings, you must find and delete the VHD and associated metadata file from the S3 bucket in your AWS account.
- [Enable Amazon S3 Object Versioning and Revert a User's Application Settings](https://docs.aws.amazon.com/appstream2/latest/developerguide/app-persistence-enable-versions-revert-settings.html): You can use Amazon S3 object versioning and lifecycle policies to manage your usersâ application settings when your users change them.
- [Increase the Size of the Application Settings VHD](https://docs.aws.amazon.com/appstream2/latest/developerguide/app-persistence-increase-VHD-size.html): The default VHD maximum size is 1 GB for Elastic fleets and 5GB for Always-On and On-Demand fleets.


## [Enable Regional Settings for Your Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-regional-settings-admins-users.html)

### [Configure Default Regional Settings for Your Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-default-regional-settings.html)

Learn how to configure default regional settings for your WorkSpaces Applications users.

- [Specify a Default Time Zone](https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-default-time-zone.html): To specify a default time zone to be used in your usersâ streaming sessions, perform the steps in either of the following two procedures.
- [Specify a Default Display Language](https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-default-display-language.html): There are two ways to specify the default display language for your usersâ streaming sessions.
- [Specify a Default System Locale](https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-default-system-locale.html): To specify a default system locale for your usersâ streaming sessions, perform the following steps.
- [Specify a Default User Locale](https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-default-user-locale.html): To specify a default user locale for your usersâ streaming sessions, perform the following steps.
- [Specify a Default Input Method](https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-default-input-method.html): To specify a default input method to be used in your usersâ streaming sessions, perform the following steps.
- [Special Considerations for Application Settings Persistence](https://docs.aws.amazon.com/appstream2/latest/developerguide/special-considerations-app-settings-persistence.html): When you create a stack in the WorkSpaces Applications console, in Step 3: User Settings, if you use the same settings group under Application settings persistence as another stack that uses different regional settings, only one set of regional settings is used for both stacks.
- [Special Considerations for Japanese Language Settings](https://docs.aws.amazon.com/appstream2/latest/developerguide/special-considerations-japanese-language-settings.html): This section describes key points to keep in mind when configuring Japanese language settings for your WorkSpaces Applications users.

### [Enable Your Users to Configure Their Regional Settings](https://docs.aws.amazon.com/appstream2/latest/developerguide/regional-settings.html)

Learn about the regional settings that your users can configure.

- [Supported Locales](https://docs.aws.amazon.com/appstream2/latest/developerguide/supported-locales.html): WorkSpaces Applications supports the following locales:
- [Enable Regional Settings for Your WorkSpaces Applications Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/regional-settings-enable.html): To enable users to configure regional settings for a given stack during their WorkSpaces Applications streaming sessions, your stack must be associated with a fleet based on an image that uses a version of the WorkSpaces Applications agent released on or after June 6, 2018.


## [Manage Application Entitlements](https://docs.aws.amazon.com/appstream2/latest/developerguide/manage-application-entitlements.html)

- [Attribute-Based Application Entitlements](https://docs.aws.amazon.com/appstream2/latest/developerguide/application-entitlements-saml.html): Application entitlements control access to specific applications within your WorkSpaces Applications stacks.

### [Dynamic Application Framework](https://docs.aws.amazon.com/appstream2/latest/developerguide/dynamic-app-framework.html)

- [Example API Operations WorkFlow](https://docs.aws.amazon.com/appstream2/latest/developerguide/manage-app-entitlement-sample-api-workflow.html): Learn about the API operations workflow for the dynamic application framework.

### [Use the Dynamic Application Framework](https://docs.aws.amazon.com/appstream2/latest/developerguide/build-dynamic-app-provider.html)

Learn how to use the WorkSpaces Applications dynamic application framework to build a dynamic app provider.

- [About the Dynamic Application Framework](https://docs.aws.amazon.com/appstream2/latest/developerguide/about-dynamic-framework.html): Learn about the dynamic application framework.
- [Dynamic Application Framework Thrift Definitions and Named Pipe name](https://docs.aws.amazon.com/appstream2/latest/developerguide/dynamic-application-framework-thrift-definitions.html): Learn about the thrift definitions for the dynamic application framework.
- [API Actions for Managing App Entitlement](https://docs.aws.amazon.com/appstream2/latest/developerguide/manage-app-entitlement-api-actions.html): Learn about the API operations for managing app entitlement.
- [Enable Dynamic App Providers](https://docs.aws.amazon.com/appstream2/latest/developerguide/enable-dynamic-app-providers.html): Learn how to enable dynamic app providers
- [Test Dynamic App Providers](https://docs.aws.amazon.com/appstream2/latest/developerguide/test-dynamic-app-providers.html): Learn how to test dynamic app providers
- [Additional Resources](https://docs.aws.amazon.com/appstream2/latest/developerguide/additional-resources-dynamic-app-providers.html): Additional resources to help you learn more about dynamic app providers and the dynamic application framework


## [Provide User Access](https://docs.aws.amazon.com/appstream2/latest/developerguide/accessing-as-user.html)

- [Supported Features](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-features.html): The following table compares the features that are supported by the different access types.

### [Provide Access Through a Web Browser](https://docs.aws.amazon.com/appstream2/latest/developerguide/access-through-web-browser-admin.html)

Your users can start an WorkSpaces Applications streaming session by using a web browser or the WorkSpaces Applications client application for a supported device.

### [Requirements and Features](https://docs.aws.amazon.com/appstream2/latest/developerguide/requirements-and-features-web-browser-admin.html)

This topic provides information to help you understand the requirements for providing user access to WorkSpaces Applications through a web browser.

- [System Requirements and Considerations](https://docs.aws.amazon.com/appstream2/latest/developerguide/system-requirements-considerations-web-browser-admin.html): Users can access WorkSpaces Applications through an HTML5-capable web browser on a desktop computer such as a Windows, Mac, Chromebook, or Linux computer.

### [Feature and Device Support](https://docs.aws.amazon.com/appstream2/latest/developerguide/feature-support-web-access-admin.html)

WorkSpaces Applications provides the following feature and peripheral device support for users who access WorkSpaces Applications through a web browser.

- [Dual-Monitor Support](https://docs.aws.amazon.com/appstream2/latest/developerguide/dual-monitor-support-web-access-admin.html): WorkSpaces Applications supports the use of multiple monitors during streaming sessions, including monitors that have different resolutions.
- [Touchscreen Device Support](https://docs.aws.amazon.com/appstream2/latest/developerguide/touchscreen-device-web-access-admin.html): WorkSpaces Applications supports gestures on touch-enabled iPads, Android tablets, and Windows devices.
- [Drawing Tablet Support](https://docs.aws.amazon.com/appstream2/latest/developerguide/drawing-tablet-support-web-access-admin.html): Drawing tablets, also known as pen tablets, are computer input devices that let users draw with a stylus (pen).
- [Relative Mouse Offset](https://docs.aws.amazon.com/appstream2/latest/developerguide/relative-mouse-offset-web-access-admin.html): By default, during users' streaming sessions, WorkSpaces Applications transmits information about mouse movements to the streaming instance by using absolute coordinates and rendering the mouse movements locally.

### [Configure a Connection Method for Your Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-connection-method-web-access-admin.html)

Depending on your organizational requirements, you can provide users with access to WorkSpaces Applications through a web browser by doing one of the following: Setting up identity federation using SAML 2.0, using an WorkSpaces Applications user pool, or creating a streaming URL.

- [SAML 2.0](https://docs.aws.amazon.com/appstream2/latest/developerguide/use-web-browser-start-streaming-session-SAML.html): Users enter the URL that you provide for them to access your internal organizational portal.
- [WorkSpaces Applications User Pool](https://docs.aws.amazon.com/appstream2/latest/developerguide/use-web-browser-start-streaming-session-user-pool.html): When you create a new user in the WorkSpaces Applications user pool, or assign a user pool user to an WorkSpaces Applications stack, WorkSpaces Applications sends email to users on your behalf.
- [Streaming URL](https://docs.aws.amazon.com/appstream2/latest/developerguide/use-web-browser-start-streaming-session-streaming-URL.html): To create a streaming URL, use one of the following methods:
- [Next Steps](https://docs.aws.amazon.com/appstream2/latest/developerguide/use-web-browser-start-streaming-session-next-steps.html): After you configure a web browser connection method, you can provide your users with the following step-by-step guidance to help them connect to WorkSpaces Applications and start a streaming session: .

### [Provide Access Through the Client](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application.html)

Learn how to configure and use the WorkSpaces Applications client

### [Requirements and Features](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-system-requirements-feature-support.html)

This topic provides information to help you understand the requirements for the WorkSpaces Applications client and supported features.

- [Requirements and Considerations](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-system-requirements.html): The WorkSpaces Applications client requires the following:

### [Feature and Device Support](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-feature-support.html)

The WorkSpaces Applications client supports the following features and devices.

- [Native Application Mode](https://docs.aws.amazon.com/appstream2/latest/developerguide/feature-support-native-application-mode.html)
- [Automatic and On-Demand Diagnostic Log Uploads](https://docs.aws.amazon.com/appstream2/latest/developerguide/feature-support-diagnostic-log-upload.html): To help with troubleshooting issues that might occur when your users are using the WorkSpaces Applications client, you can enable automatic or on-demand diagnostic log uploads, or let your users do so themselves.

### [Peripheral Devices](https://docs.aws.amazon.com/appstream2/latest/developerguide/feature-support-peripheral-devices.html)

The WorkSpaces Applications client provides the following support for peripheral devices such as monitors, webcams, mice, keyboards, and drawing tablets.

- [Multiple Monitors](https://docs.aws.amazon.com/appstream2/latest/developerguide/feature-support-multiple-monitors.html): WorkSpaces Applications supports the use of multiple monitors during streaming sessions, including monitors that have different resolutions.
- [Real-Time Audio-Video](https://docs.aws.amazon.com/appstream2/latest/developerguide/feature-support-real-time-av.html): WorkSpaces Applications supports real-time audio-video (AV) by redirecting local webcam video input to WorkSpaces Applications streaming sessions.
- [USB Devices](https://docs.aws.amazon.com/appstream2/latest/developerguide/feature-support-USB-devices-qualified.html): The following sections provide information about WorkSpaces Applications support for USB devices.
- [Drawing Tablets](https://docs.aws.amazon.com/appstream2/latest/developerguide/feature-support-drawing-tablets.html): Drawing tablets, also known as pen tablets, are computer input devices that let users draw with a stylus (pen).
- [Keyboard Shortcuts](https://docs.aws.amazon.com/appstream2/latest/developerguide/feature-support-keyboard-shortcuts.html): For the Windows client, most operating system keyboard shortcuts are supported.
- [Relative Mouse Offset](https://docs.aws.amazon.com/appstream2/latest/developerguide/feature-support-relative-mouse-offset.html): By default, during users' streaming sessions, WorkSpaces Applications transmits information about mouse movements to the streaming instance by using absolute coordinates and rendering the mouse movements locally.

### [Install and Configure the Client](https://docs.aws.amazon.com/appstream2/latest/developerguide/install-configure-client.html)

You can have your users install the WorkSpaces Applications client themselves, or you can install the WorkSpaces Applications client for them by running PowerShell scripts remotely.

- [Have Your Users Install the Client Themselves](https://docs.aws.amazon.com/appstream2/latest/developerguide/user-install-client.html): For step-by-step guidance that you can provide your users to help them install the WorkSpaces Applications client, see or .
- [Tutorial: Install the Client And Customize the Client Experience](https://docs.aws.amazon.com/appstream2/latest/developerguide/install-client-configure-settings.html): The following sections describe how to install the WorkSpaces Applications client and customize the client experience for your users.
- [Update the WorkSpaces Applications Enterprise Deployment Tool, Client, and USB Driver Manually](https://docs.aws.amazon.com/appstream2/latest/developerguide/update-enterprise-deployment-tool-client-usb-driver-manually.html): By default, the WorkSpaces Applications client and USB driver are updated automatically when a new client version is released.

### [Qualify USB Devices for Use with Streaming Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/qualify-usb-devices.html)

There are two methods for specifying which USB devices your users can redirect into their WorkSpaces Applications streaming instances:

- [Working with USB Device Filter Strings](https://docs.aws.amazon.com/appstream2/latest/developerguide/USB-device-filter-strings.html): This section describes the filter strings that are available for qualifying USB devices for WorkSpaces Applications streaming sessions.

### [Configure a Connection Method for Your Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/use-client-start-streaming-session.html)

After you install the WorkSpaces Applications client on your users' local computers, they can use the WorkSpaces Applications client to connect to a streaming session.

- [SAML 2.0](https://docs.aws.amazon.com/appstream2/latest/developerguide/use-client-start-streaming-session-SAML.html): If you use external identity providers to federate your users to an WorkSpaces Applications stack, you must create a registry value to configure the WorkSpaces Applications client with a prepopulated URL whenever the client is launched.
- [WorkSpaces Applications User Pool](https://docs.aws.amazon.com/appstream2/latest/developerguide/use-client-start-streaming-session-user-pool.html): When you create a new user in the WorkSpaces Applications user pool, or assign a user pool user to an WorkSpaces Applications stack, WorkSpaces Applications sends email to users on your behalf.
- [Streaming URL](https://docs.aws.amazon.com/appstream2/latest/developerguide/use-client-start-streaming-session-streaming-URL.html): To create a streaming URL, use one of the following methods:
- [Next Steps](https://docs.aws.amazon.com/appstream2/latest/developerguide/use-client-start-streaming-session-next-steps.html): After you configure a client connection method, you can provide your users with the following step-by-step guidance to help them connect to WorkSpaces Applications and start a streaming session: or .
- [Share a USB Device with a Streaming Session](https://docs.aws.amazon.com/appstream2/latest/developerguide/share-usb-devices-with-session.html): Before users share their USB devices with an WorkSpaces Applications session, the USB devices must be qualified.
- [Redirect a Streaming Session from the Web Browser to the WorkSpaces Applications Client](https://docs.aws.amazon.com/appstream2/latest/developerguide/redirect-streaming-session-from-web-to-client.html): You can configure WorkSpaces Applications to redirect a streaming session from a web browser to the WorkSpaces Applications client.

### [Enable File System Redirection](https://docs.aws.amazon.com/appstream2/latest/developerguide/enable-file-system-redirection.html)

WorkSpaces Applications file system redirection lets users who have the WorkSpaces Applications client installed access files on their local computer from within their streaming session.

- [Prerequisites for File System Redirection](https://docs.aws.amazon.com/appstream2/latest/developerguide/file-system-redirection-prerequisites.html): To enable WorkSpaces Applications file redirection:
- [How to Enable File System Redirection](https://docs.aws.amazon.com/appstream2/latest/developerguide/how-to-enable-file-system-redirection.html): Perform the following steps to enable both file upload and download on the stack that your users access for streaming sessions.
- [Make Default Drives and Folders Available for Your Users to Share](https://docs.aws.amazon.com/appstream2/latest/developerguide/prepopulate-drives-folders-system-redirection.html): By default, when you enable file direction for users of a stack, the following drives and folders are made available for those users to share in their streaming session:
- [Provide Your WorkSpaces Applications Users with Guidance for Working with File System Redirection](https://docs.aws.amazon.com/appstream2/latest/developerguide/end-user-guidance-file-system-redirection.html): To help your users understand how to work with file redirection during their streaming sessions, you can provide them with the information in .

### [Enable Local Printer Redirection for Your WorkSpaces Applications Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/enable-local-printer-redirection.html)

With local printer redirection, your WorkSpaces Applications users can redirect print jobs from their streaming application to a printer that is connected to their local computer, including any network printers that the users have mapped.

- [Prerequisites for Local Printer Redirection](https://docs.aws.amazon.com/appstream2/latest/developerguide/local-printer-redirection-prerequisites.html): To ensure that your users can use local printer redirection, you must:
- [How to Enable Local Printer Redirection](https://docs.aws.amazon.com/appstream2/latest/developerguide/how-to-enable-disable-local-printer-redirection.html): By default, local printer redirection is enabled when the WorkSpaces Applications client is installed.
- [How to Disable Local Printer Redirection](https://docs.aws.amazon.com/appstream2/latest/developerguide/disable-local-printer-redirection.html): To disable local printer redirection follow these steps.


## [Tagging Your Resources](https://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-basic.html)

- [Tagging Basics](https://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-introduction.html): Tags consist of a key-value pair, similar to other AWS services tags.
- [Tag Restrictions](https://docs.aws.amazon.com/appstream2/latest/developerguide/tag-restrictions.html)
- [Adding Tags during Resource Creation](https://docs.aws.amazon.com/appstream2/latest/developerguide/basic-tagging-resource-creation-console.html): When you create a resource in the WorkSpaces Applications console, you can add one or more tags to manage the resource.
- [Adding, Editing, and Deleting Tags](https://docs.aws.amazon.com/appstream2/latest/developerguide/basic-tagging-console.html): You can add, edit, and delete tags for existing resources by using the WorkSpaces Applications console.
- [Using the API, SDK, or CLI](https://docs.aws.amazon.com/appstream2/latest/developerguide/basic-tagging-API-SDK-CLI.html): If you're using the WorkSpaces Applications API, an AWS SDK, or the AWS Command Line Interface (AWS CLI), you can use the following WorkSpaces Applications operations with the tags parameter to add tags when you create new resources.


## [Monitoring and Reporting](https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-monitoring-reporting.html)

### [Monitoring Resources](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring.html)

Monitor Amazon WorkSpaces Applications service activity using available tools.

- [Viewing Fleet Usage Using the Console](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring-console.html): You can monitor your Amazon WorkSpaces Applications fleet usage using the WorkSpaces Applications or CloudWatch console.
- [Viewing Instance and Session Performance Metrics Using the Console](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring-instance-session-performance.html): You can monitor Amazon WorkSpaces Applications fleet instances and session performance using the WorkSpaces Applications console or the CloudWatch console.

### [WorkSpaces Applications Metrics and Dimensions](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring-with-cloudwatch.html)

Amazon WorkSpaces Applications sends the following metrics and dimension information to Amazon CloudWatch.

- [Fleet Usage Metrics for Single-session Fleets](https://docs.aws.amazon.com/appstream2/latest/developerguide/appstream-dimensions.html): The following are fleet usage metrics for single-session fleets.
- [Fleet Usage Metrics for Multi-session Fleets](https://docs.aws.amazon.com/appstream2/latest/developerguide/usage-metrics-multi-session.html): The following are fleet usage metrics for multi-session fleets.
- [Instance and Session Performance Metrics for Single-session and Multi-session Fleets](https://docs.aws.amazon.com/appstream2/latest/developerguide/instance-session-metrics-single-session-multi-session.html): The following are instance and session performance metrics for single-session and multi-session fleets.
- [Dimensions for Amazon WorkSpaces Applications Metrics](https://docs.aws.amazon.com/appstream2/latest/developerguide/dimensions-metrics.html): The AWS/AppStream namespace includes the following dimensions and dimension groups.

### [Usage Reports](https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-usage-reports.html)

Learn about usage reporting for WorkSpaces Applications.

### [Enable Usage Reports](https://docs.aws.amazon.com/appstream2/latest/developerguide/enable-usage-reports.html)

Learn how to enable usage reports for WorkSpaces Applications.

- [Sessions Reports](https://docs.aws.amazon.com/appstream2/latest/developerguide/usage-report-types-sessions-reports.html): Learn about WorkSpaces Applications sessions reports.
- [Applications Reports](https://docs.aws.amazon.com/appstream2/latest/developerguide/usage-report-types-applications-reports.html): Learn about WorkSpaces Applications applications reports.

### [Usage Reports Fields](https://docs.aws.amazon.com/appstream2/latest/developerguide/usage-reports-fields.html)

Learn about the information included in WorkSpaces Applications usage reports.

- [Sessions Report Fields](https://docs.aws.amazon.com/appstream2/latest/developerguide/usage-reports-fields-sessions-reports.html): Learn about the information included in WorkSpaces Applications sessions reports
- [Applications Report Fields](https://docs.aws.amazon.com/appstream2/latest/developerguide/usage-reports-fields-applications-reports.html): Learn about the information included in WorkSpaces Applications applications reports

### [Create Custom Reports](https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-custom-reports-analyze-usage-data.html)

Learn how to create custom reports and analyze usage data for WorkSpaces Applications.

- [Create an AWS Glue Crawler](https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-custom-reports-create-crawler.html): Learn how to create an AWS Glue crawler.
- [Create a Data Catalog by Using the AWS Glue Crawler](https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-custom-reports-create-data-catalog.html): Learn how to create a Data Catalog.
- [Create and Run Athena Queries](https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-custom-reports-create-run-athena-queries.html): Learn how to create and run Athena queries.
- [Working with Athena Queries](https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-custom-reports-example-sql-queries.html): Learn how to work with SQL queries that you can run in Athena to analyze WorkSpaces Applications usage reports.

### [Logging WorkSpaces Applications API Calls](https://docs.aws.amazon.com/appstream2/latest/developerguide/logging-using-cloudtrail.html)

Learn how to log WorkSpaces Applications API Calls with AWS CloudTrail.

- [WorkSpaces Applications Information in CloudTrail](https://docs.aws.amazon.com/appstream2/latest/developerguide/service-name-info-in-cloudtrail.html): CloudTrail is enabled on your AWS account when you create the account.
- [Example: WorkSpaces Applications Log File Entries](https://docs.aws.amazon.com/appstream2/latest/developerguide/understanding-service-name-entries.html): A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify.


## [Security](https://docs.aws.amazon.com/appstream2/latest/developerguide/security.html)

### [Data Protection](https://docs.aws.amazon.com/appstream2/latest/developerguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon WorkSpaces Applications.

- [Encryption at Rest](https://docs.aws.amazon.com/appstream2/latest/developerguide/encryption-rest.html): WorkSpaces Applications fleet instances are ephemeral in nature.
- [Encryption in Transit](https://docs.aws.amazon.com/appstream2/latest/developerguide/encryption-transit.html): The following table provides information about how data is encrypted in transit.
- [Administrator Controls](https://docs.aws.amazon.com/appstream2/latest/developerguide/administrator-controls.html): WorkSpaces Applications provides administrative controls that you can use to limit the ways in which users can transfer data between their local computer and an WorkSpaces Applications fleet instance.
- [Application Access](https://docs.aws.amazon.com/appstream2/latest/developerguide/application-access.html): By default, WorkSpaces Applications enables the applications that you specify in your image to launch other applications and executable files on the image builder and fleet instance.

### [Identity and Access Management](https://docs.aws.amazon.com/appstream2/latest/developerguide/controlling-access.html)

Learn how to use AWS Identity and Access Management (IAM) policies and roles to manage access to WorkSpaces Applications resources.

- [Network Access](https://docs.aws.amazon.com/appstream2/latest/developerguide/network-access-to-streaming-instances.html): A security group acts as a stateful firewall that controls what traffic is allowed to reach your streaming instances.

### [Access to WorkSpaces Applications Resources](https://docs.aws.amazon.com/appstream2/latest/developerguide/controlling-administrator-access-with-policies-roles.html)

By default, IAM users don't have the permissions required to create or modify WorkSpaces Applications resources, or perform tasks by using the WorkSpaces Applications API.

- [AWS Managed Policies Required to Access WorkSpaces Applications Resources](https://docs.aws.amazon.com/appstream2/latest/developerguide/managed-policies-required-to-access-appstream-resources.html): To provide full administrative or read-only access to WorkSpaces Applications, you must attach one of the following AWS managed policies to the IAM users or groups that require those permissions.
- [Roles Required for WorkSpaces Applications, Application Auto Scaling, and AWS Certificate Manager Private CA](https://docs.aws.amazon.com/appstream2/latest/developerguide/roles-required-for-appstream.html): In AWS, IAM roles are used to grant permissions to an AWS service so it can access AWS resources.
- [Checking for the AmazonAppStreamServiceAccess Service Role and Policies](https://docs.aws.amazon.com/appstream2/latest/developerguide/controlling-access-checking-for-iam-service-access.html): Complete the steps in this section to check whether the AmazonAppStreamServiceAccess service role is present and has the correct policies attached.
- [Checking for the ApplicationAutoScalingForAmazonAppStreamAccess Service Role and Policies](https://docs.aws.amazon.com/appstream2/latest/developerguide/controlling-access-checking-for-iam-autoscaling.html): Complete the steps in this section to check whether the ApplicationAutoScalingForAmazonAppStreamAccess service role is present and has the correct policies attached.
- [Checking for the AWSServiceRoleForApplicationAutoScaling_AppStreamFleet Service-Linked Role and Policies](https://docs.aws.amazon.com/appstream2/latest/developerguide/controlling-access-checking-for-iam-service-linked-role-application-autoscaling-appstream-fleet.html): Complete the steps in this section to check whether the AWSServiceRoleForApplicationAutoScaling_AppStreamFleet service-linked role is present and has the correct policies attached.
- [Checking for the AmazonAppStreamPCAAccess Service Role and Policies](https://docs.aws.amazon.com/appstream2/latest/developerguide/controlling-access-checking-for-AppStreamPCAAccess.html): Complete the steps in this section to check whether the AmazonAppStreamPCAAccess service role is present and has the correct policies attached.
- [Access to Application Auto Scaling](https://docs.aws.amazon.com/appstream2/latest/developerguide/autoscaling-iam-policy.html): Automatic scaling for fleets is made possible by a combination of the WorkSpaces Applications, Amazon CloudWatch, and Application Auto Scaling APIs.

### [Access to the S3 Bucket for Home Folders and Application Settings Persistence](https://docs.aws.amazon.com/appstream2/latest/developerguide/s3-iam-policy.html)

The following examples show how you can use IAM policies to manage access to the Amazon S3 bucket for home folders and application settings persistence.

- [Deleting the Amazon S3 Bucket for Home Folders and Application Settings Persistence](https://docs.aws.amazon.com/appstream2/latest/developerguide/s3-iam-policy-delete.html): WorkSpaces Applications adds an Amazon S3 bucket policy to the buckets that it creates to prevent them from being accidentally deleted.
- [Restricting Administrator Access to the Amazon S3 Bucket for Home Folders and Application Settings Persistence](https://docs.aws.amazon.com/appstream2/latest/developerguide/s3-iam-policy-restricted-access.html): By default, administrators who can access the Amazon S3 buckets created by WorkSpaces Applications can view and modify content that is part of users' home folders and persistent application settings.

### [Access to Applications and Scripts on Streaming Instances](https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html)

Applications and scripts that run on WorkSpaces Applications streaming instances must include AWS credentials in their AWS API requests.

- [Best Practices for Using IAM Roles With WorkSpaces Applications Streaming Instances](https://docs.aws.amazon.com/appstream2/latest/developerguide/best-practices-for-using-iam-role-with-streaming-instances.html): When you use IAM roles with WorkSpaces Applications streaming instances, we recommend that you follow these practices:
- [Configuring an Existing IAM Role to Use With WorkSpaces Applications Streaming Instances](https://docs.aws.amazon.com/appstream2/latest/developerguide/configuring-existing-iam-role-to-use-with-streaming-instances.html): This topic describes how to configure an existing IAM role so that you can use it with image builders and fleet streaming instances.
- [How to Create an IAM Role to Use With WorkSpaces Applications Streaming Instances](https://docs.aws.amazon.com/appstream2/latest/developerguide/how-to-create-iam-role-to-use-with-streaming-instances.html): This topic describes how to create a new IAM role so that you can use it with image builders and fleet streaming instances.
- [How to Use the IAM Role With WorkSpaces Applications Streaming Instances](https://docs.aws.amazon.com/appstream2/latest/developerguide/how-to-use-iam-role-with-streaming-instances.html): After you create an IAM role, you can apply it to an image builder or fleet streaming instance when you launch the image builder or create a fleet.
- [SELinux](https://docs.aws.amazon.com/appstream2/latest/developerguide/selinux.html): By default, Security Enhanced Linux (SELinux) is enabled and set to enforcing mode for WorkSpaces Applications image builders and streaming instances powered by Red Hat Enterprise Linux and Rocky Linux.
- [Cookie-Based Authentication](https://docs.aws.amazon.com/appstream2/latest/developerguide/cookie-auth.html): WorkSpaces Applications uses browser cookies to authenticate streaming sessions and allow users to reconnect to an active session without re-entering their sign-in credentials every time.
- [Logging and Monitoring](https://docs.aws.amazon.com/appstream2/latest/developerguide/logging-monitoring-alerting.html): Learn about logging, monitoring, and alerting in Amazon WorkSpaces Applications.
- [Compliance Validation](https://docs.aws.amazon.com/appstream2/latest/developerguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/appstream2/latest/developerguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon WorkSpaces Applications features for data resiliency.

### [Infrastructure Security](https://docs.aws.amazon.com/appstream2/latest/developerguide/infrastructure-security.html)

Learn how Amazon WorkSpaces Applications isolates service traffic.

- [Network Isolation](https://docs.aws.amazon.com/appstream2/latest/developerguide/network-isolation.html): A virtual private cloud (VPC) is a virtual network in your own logically isolated area in the Amazon Web Services Cloud.
- [Isolation on Physical Hosts](https://docs.aws.amazon.com/appstream2/latest/developerguide/physical-isolation.html): Different streaming instances on the same physical host are isolated from each other as though they are on separate physical hosts.
- [Controlling Network Traffic](https://docs.aws.amazon.com/appstream2/latest/developerguide/control-network-traffic.html): To help control network traffic to your WorkSpaces Applications streaming instances, consider these options:

### [Interface VPC Endpoints](https://docs.aws.amazon.com/appstream2/latest/developerguide/interface-vpc-endpoints.html)

Learn about WorkSpaces Applications interface endpoints

- [Tutorial: Creating and Streaming from Interface VPC Endpoints](https://docs.aws.amazon.com/appstream2/latest/developerguide/creating-streaming-from-interface-vpc-endpoints.html): You can use an interface VPC endpoint in your Amazon Web Services account to restrict all network traffic between your Amazon VPC and WorkSpaces Applications to the Amazon network.

### [Access the WorkSpaces Applications API and CLI Through an Interface VPC Endpoint](https://docs.aws.amazon.com/appstream2/latest/developerguide/access-api-cli-through-interface-vpc-endpoint.html)

Learn how to access WorkSpaces Applications API operations and CLI commands through an interface VPC endpoint (interface endpoint).

- [Create an Interface Endpoint to Access WorkSpaces Applications API Operations and CLI Commands](https://docs.aws.amazon.com/appstream2/latest/developerguide/access-api-cli-through-interface-vpc-endpoint-create-interface-endpoint.html): Learn how to create an interface endpoint that you can use to access WorkSpaces Applications API operations and CLI commands.
- [Use an Interface Endpoint to Access WorkSpaces Applications API Operations and CLI Commands](https://docs.aws.amazon.com/appstream2/latest/developerguide/how-to-access-api-cli-through-interface-vpc-endpoint.html): Learn how to use an interface endpoint to access WorkSpaces Applications API operations and CLI commands.

### [FIPS Endpoints](https://docs.aws.amazon.com/appstream2/latest/developerguide/protecting-data-in-transit-FIPS-endpoints.html)

Learn how to protect data in transit by using FIPS-compliant endpoints (FIPS endpoints)

- [FIPS Endpoints for Administrative Use](https://docs.aws.amazon.com/appstream2/latest/developerguide/FIPS-for-administrative-use.html): To specify a FIPS endpoint when you run an AWS CLI command for WorkSpaces Applications, use the endpoint-url parameter.
- [FIPS Endpoints for User Streaming Sessions](https://docs.aws.amazon.com/appstream2/latest/developerguide/FIPS-for-user-streaming-sessions.html): If you use SAML 2.0 or a streaming URL to authenticate users, you can configure FIPS-compliant connections for your users' streaming sessions.
- [Exceptions](https://docs.aws.amazon.com/appstream2/latest/developerguide/FIPS-exceptions.html): FIPS-compliant connections are not supported in the following scenarios:
- [Security Groups](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-network-security-groups.html): You can provide additional access control to your VPC from streaming instances in a fleet or an image builder in Amazon WorkSpaces Applications by associating them with VPC security groups.
- [Update Management](https://docs.aws.amazon.com/appstream2/latest/developerguide/update-management.html): Learn about update management in Amazon WorkSpaces Applications.

### [Confused Deputy Prevention](https://docs.aws.amazon.com/appstream2/latest/developerguide/confused-deputy.html)

Learn about the confused deputy problem, as well as resources available within Amazon WorkSpaces Applications to prevent this problem from impacting account resources.

- [Example: WorkSpaces Applications service role cross-service confused deputy prevention](https://docs.aws.amazon.com/appstream2/latest/developerguide/example-confused-deputy.html): WorkSpaces Applications assumes a service role using a variety of resource ARNs, which leads to a complicated conditional statement.
- [Example: WorkSpaces Applications fleet machine role cross-service confused deputy prevention](https://docs.aws.amazon.com/appstream2/latest/developerguide/example-fleet-machine.html)
- [Example: WorkSpaces Applications Elastic fleets session script Amazon S3 bucket policy cross-service confused deputy prevention](https://docs.aws.amazon.com/appstream2/latest/developerguide/example-elastic-fleets.html)
- [Example: WorkSpaces Applications Application Amazon S3 bucket policy cross-service confused deputy prevention](https://docs.aws.amazon.com/appstream2/latest/developerguide/example-s3-bucket.html): When you store data in an Amazon S3 bucket, the bucket might be exposed to confused deputy issues.

### [Security Best Practices](https://docs.aws.amazon.com/appstream2/latest/developerguide/security-best-practices.html)

Learn security best practices.

- [Securing Persistent Data](https://docs.aws.amazon.com/appstream2/latest/developerguide/securing-persistent-data.html): Deployments of WorkSpaces Applications can require the user state to persist in some form.
- [Endpoint Security and Antivirus](https://docs.aws.amazon.com/appstream2/latest/developerguide/endpoint-security-antivirus.html): The brief ephemeral nature of WorkSpaces Applications instances and the lack of persistency of data means a different approach is required to ensure user experience and performance is not compromised by activities that would be required on a persistent desktop.
- [Network Exclusions](https://docs.aws.amazon.com/appstream2/latest/developerguide/network-exclusions.html): The WorkSpaces Applications management network range (198.19.0.0/16) and following ports and addresses should not be blocked by any security / firewall or antivirus solutions within WorkSpaces Applications instances.
- [Securing an WorkSpaces Applications Session](https://docs.aws.amazon.com/appstream2/latest/developerguide/securing-session.html)
- [Firewalls and Routing](https://docs.aws.amazon.com/appstream2/latest/developerguide/firewalls-routing.html): When creating an WorkSpaces Applications fleet, subnets and a Security Group must be assigned.
- [Data Loss Prevention](https://docs.aws.amazon.com/appstream2/latest/developerguide/data-loss-prevention.html): We'll look at two kinds of data loss prevention.
- [Controlling egress traffic](https://docs.aws.amazon.com/appstream2/latest/developerguide/controlling-egress-traffic.html): Where data loss is a concern, itâs important to cover off what a User can access once they are inside of their WorkSpaces Applications instance.
- [Using AWS services](https://docs.aws.amazon.com/appstream2/latest/developerguide/using-services.html)


## [Troubleshooting](https://docs.aws.amazon.com/appstream2/latest/developerguide/troubleshooting.html)

- [General Troubleshooting](https://docs.aws.amazon.com/appstream2/latest/developerguide/troubleshooting-general.html): The following are general issues that might occur when you use Amazon WorkSpaces Applications.
- [Troubleshooting Image Builders](https://docs.aws.amazon.com/appstream2/latest/developerguide/troubleshooting-image-builder.html): The following are issues that might occur when you use Amazon WorkSpaces Applications image builders.
- [Troubleshooting Fleets](https://docs.aws.amazon.com/appstream2/latest/developerguide/troubleshooting-fleets.html): The following are issues that might occur when users connect to Amazon WorkSpaces Applications streaming sessions launched from fleet instances.
- [Troubleshooting Active Directory](https://docs.aws.amazon.com/appstream2/latest/developerguide/troubleshooting-active-directory.html): The following are issues that might occur when you set up and use Active Directory with Amazon WorkSpaces Applications.
- [Troubleshooting WorkSpaces Applications User Issues](https://docs.aws.amazon.com/appstream2/latest/developerguide/troubleshooting-user-issues.html)
- [Troubleshooting Persistent Storage Issues](https://docs.aws.amazon.com/appstream2/latest/developerguide/troubleshooting-persistent-storage.html): Amazon WorkSpaces Applications supports the following options for persistent storage: Home folders, Google Drive for G Suite, and OneDrive for Business.
- [Troubleshooting Notification Codes](https://docs.aws.amazon.com/appstream2/latest/developerguide/troubleshooting-notification-codes.html): The following are notification codes and resolution steps for notifications that you might see when you set up and use Amazon WorkSpaces Applications.


## [Guidance for WorkSpaces Applications Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/user-guidance.html)

### [Access Methods and Clients](https://docs.aws.amazon.com/appstream2/latest/developerguide/clients-access-methods-user.html)

You can connect to WorkSpaces Applications by using a web browser or the WorkSpaces Applications client for Windows.

### [Web Browser Access](https://docs.aws.amazon.com/appstream2/latest/developerguide/web-browser-user.html)

The following information helps you use a web browser to connect to WorkSpaces Applications and stream applications.

- [Requirements](https://docs.aws.amazon.com/appstream2/latest/developerguide/web-browser-requirements-user.html): You can connect to WorkSpaces Applications from any location by using an HTML5-capable web browser.
- [Setup](https://docs.aws.amazon.com/appstream2/latest/developerguide/web-browser-setup-user.html): No browser extensions or plugins are required to use WorkSpaces Applications in a web browser.
- [Connect to WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/web-browser-start-streaming-session-user.html): Follow these steps to connect to WorkSpaces Applications and start an application streaming session.
- [WorkSpaces Applications Web Browser Access (Version 2)](https://docs.aws.amazon.com/appstream2/latest/developerguide/web-browser-access-v2.html): WorkSpaces Applications web browser access version 2 offers an enhanced end user experience, including menu options that are easily discoverable and textual guidance for end users.
- [Monitors and Display Resolution](https://docs.aws.amazon.com/appstream2/latest/developerguide/web-browser-monitors-display-resolution-user.html): WorkSpaces Applications supports the use of multiple monitors during streaming sessions, including monitors that have different resolutions.
- [USB Devices](https://docs.aws.amazon.com/appstream2/latest/developerguide/web-browser-usb-devices-user.html): USB devices are not supported for browser-based WorkSpaces Applications streaming sessions.
- [Touchscreen Devices](https://docs.aws.amazon.com/appstream2/latest/developerguide/web-browser-using-touchscreen-devices-user.html): WorkSpaces Applications supports gestures on touch-enabled iPads, Android tablets, and Windows devices.
- [Function Keys](https://docs.aws.amazon.com/appstream2/latest/developerguide/web-browser-using-function-keys-user.html): You can use keyboard shortcuts during WorkSpaces Applications streaming sessions to enter special keystrokes or key combinations.
- [Remap the Mac Option and Command Keys](https://docs.aws.amazon.com/appstream2/latest/developerguide/web-browser-remap-mac-keys-user.html): When you use a device that runs macOS or Mac OS X to connect to WorkSpaces Applications, you can remap the Mac Option and Command keys on your keyboard.
- [Video and Audio Conferencing](https://docs.aws.amazon.com/appstream2/latest/developerguide/web-browser-video-audio.html): WorkSpaces Applications real-time audio-video (AV) redirects your local webcam video and microphone audio input to WorkSpaces Applications streaming sessions.
- [Drawing Tablets](https://docs.aws.amazon.com/appstream2/latest/developerguide/web-browser-drawing-tablets-user.html): Drawing tablets, also known as pen tablets, are computer input devices that let you draw with a stylus (pen).
- [Relative Mouse Offset](https://docs.aws.amazon.com/appstream2/latest/developerguide/web-browser-relative-mouse-offset-web-access-user.html): By default, during a streaming session, WorkSpaces Applications transmits information about mouse movements by using absolute coordinates and rendering the mouse movements locally.
- [Troubleshooting](https://docs.aws.amazon.com/appstream2/latest/developerguide/web-browser-troubleshooting-user.html): If issues occur when you use WorkSpaces Applications, your WorkSpaces Applications session ID can help your administrator with troubleshooting.

### [Client for Windows](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-windows-user.html)

The following information helps you use the WorkSpaces Applications client for Windows to connect to WorkSpaces Applications and stream applications.

- [Features](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-windows-features-user.html): The WorkSpaces Applications client for Windows is an application that you install on your Windows PC.
- [Requirements](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-windows-requirements-user.html): The WorkSpaces Applications client for Windows must be installed on a computer that meets the following requirements:
- [Setup for Windows](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-windows-installation-user.html): Follow these steps to install the client.

### [Connect to WorkSpaces Applications on Windows Client](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-windows-start-streaming-session-user.html)

After the WorkSpaces Applications client for Windows is installed on your PC, you can use it to connect to WorkSpaces Applications.

- [WorkSpaces Applications Client Connection Modes](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-windows-connection-modes-user.html): The WorkSpaces Applications client provides two connection modes: Native application mode and classic mode.
- [Connect to WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-windows-how-to-connect-user.html): Follow these steps to connect to WorkSpaces Applications and start an application streaming session.
- [How to Switch WorkSpaces Applications Connection Modes](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-windows-how-to-switch-connection-modes-user.html): If your administrator has not disabled native application mode for your streaming sessions, you can switch between native application mode and classic mode.
- [Monitors](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-windows-monitors-display-resolution-user.html)

### [USB Devices](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-windows-how-to-share-usb-devices-user.html)

With certain exceptions, USB redirection is required for the WorkSpaces Applications client to support USB devices.

- [How to Use a Smart Card During a Streaming Session](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-windows-how-to-use-smart-card-during-streaming-session-user.html): Depending on the authentication settings that your administrator has enabled, you might need to use a smart card for authentication during an WorkSpaces Applications streaming session.
- [How to Share a USB Device with WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-windows-how-to-share-usb-device-user.html): If you are using a drawing tablet, USB redirection might not be required to use it with WorkSpaces Applications.
- [Local File Access](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-windows-file-system-redirection.html): WorkSpaces Applications file redirection lets you access files on your local computer from your WorkSpaces Applications streaming session.
- [Printer Redirection](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-windows-local-printer-redirection.html): WorkSpaces Applications local printer redirection lets you access printers that are connected to your local computer from your WorkSpaces Applications streaming session.
- [Video and Audio Conferencing](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-windows-how-to-use-local-webcam-user.html): WorkSpaces Applications real-time audio-video (AV) redirects your local webcam video input to WorkSpaces Applications streaming sessions.
- [Drawing Tablets](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-windows-drawing-tablets-user.html): Drawing tablets, also known as pen tablets, are computer input devices that let you draw with a stylus (pen).
- [Relative Mouse Offset](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-windows-relative-mouse-offset-user.html): By default, during a streaming session, WorkSpaces Applications transmits information about mouse movements by using absolute coordinates and rendering the mouse movements locally.
- [Logging](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-windows-how-to-enable-diagnostic-logging-user.html): To help with troubleshooting if an issue with the WorkSpaces Applications client occurs, you can enable diagnostic logging.
- [Troubleshooting](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-windows-troubleshooting-user.html): If issues occur when you use the WorkSpaces Applications client for Windows, your WorkSpaces Applications client ID and version number can help your administrator with troubleshooting.
- [Client Release Notes](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-release-versions.html): Version and release history for the WorkSpaces Applications client

### [Client for macOS](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-mac-user.html)

The following information helps you use the WorkSpaces Applications client for macOS to connect to WorkSpaces Applications and stream applications.

- [Requirements](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-mac-requirements-user.html): The WorkSpaces Applications client for macOS must be installed on a computer that meets the following requirements:
- [Setup and installation for macOS](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-mac-installation-user.html): Follow these steps to download and install the client application.

### [Connect to WorkSpaces Applications on macOS client](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-mac-start-streaming-session-user.html)

After the WorkSpaces Applications client for macOS is installed on your PC, you can use it to connect to WorkSpaces Applications.

- [WorkSpaces Applications macOS Client Connection Mode](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-mac-connection-modes-user.html): The WorkSpaces Applications macOS client supports two connection modes: Classic mode and Desktop view.
- [Connect to WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-mac-how-to-connect-user.html): Follow these steps to connect to WorkSpaces Applications and start an application streaming session.
- [Monitors](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-windows-mac-display-resolution-user.html)
- [Video and Audio Conferencing](https://docs.aws.amazon.com/appstream2/latest/developerguide/video-audio-mac.html): WorkSpaces Applications real-time audio-video (AV) redirects your local webcam video input to WorkSpaces Applications streaming sessions.
- [Relative Mouse Offset](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-mac-relative-mouse-offset-user.html): By default, during a streaming session, WorkSpaces Applications transmits information about mouse movements by using absolute coordinates and rendering the mouse movements locally.
- [Remap the Windows Logo Key or Command Key](https://docs.aws.amazon.com/appstream2/latest/developerguide/remap-windows-logo-key.html): You can remap the Mac Option and Command keys on your keyboard.
- [Remember My Settings](https://docs.aws.amazon.com/appstream2/latest/developerguide/remember-settings-mac.html): The WorkSpaces Applications macOS client application can save the preferences you configured in Settings for future sessions, except for Audio & Video settings.
- [Printer Redirection](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-mac-local-printer-redirection.html): WorkSpaces Applications local printer redirection lets you access printers that are connected to your local computer from your WorkSpaces Applications streaming session.
- [Disconnect and End Session](https://docs.aws.amazon.com/appstream2/latest/developerguide/disconnect-end-mac.html): To disconnect the streaming session, choose one of the following options:
- [Troubleshooting](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-mac-troubleshooting-user.html): Use the following steps to enable diagnostic log uploads and determine your client version and client ID.
- [Client Release Notes](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-release-versions-mac.html): Version and release history for the WorkSpaces Applications macOS client

### [File Storage Options](https://docs.aws.amazon.com/appstream2/latest/developerguide/file-folder-storage-user.html)

If your WorkSpaces Applications administrator has enabled it, you can use one or more of the following storage options for your files and folders during application streaming sessions.

- [Use Home Folders](https://docs.aws.amazon.com/appstream2/latest/developerguide/home-folders-end-user.html): If your WorkSpaces Applications administrator has enabled this file storage option, when you are signed in to an WorkSpaces Applications streaming session, you can use your home folder.
- [Use Google Drive](https://docs.aws.amazon.com/appstream2/latest/developerguide/google-drive-end-user.html)
- [Use OneDrive for Business](https://docs.aws.amazon.com/appstream2/latest/developerguide/onedrive-end-user.html)
- [Use Custom Shared Network Folders](https://docs.aws.amazon.com/appstream2/latest/developerguide/custom-shared-folders-end-user.html): If your WorkSpaces Applications administrator has enabled this file storage option, after you sign in to a streaming session, your administrator will have a custom shared folder configured and named for you.
- [Regional Settings](https://docs.aws.amazon.com/appstream2/latest/developerguide/regional-settings-end-user.html): You can configure regional settings so that your WorkSpaces Applications Windows streaming sessions use settings that are specific to your location or language.


## [Extension SDK Developer Guide](https://docs.aws.amazon.com/appstream2/latest/developerguide/extension-sdk.html)

- [Prerequisites](https://docs.aws.amazon.com/appstream2/latest/developerguide/extension-sdk-prereq.html): Before you start working with the Amazon DCV Extension SDK, make sure that your WorkSpaces Applications client applications and your WorkSpaces Applications servers meet the following requirements.
- [Third-party vendor extensions](https://docs.aws.amazon.com/appstream2/latest/developerguide/extension-sdk-isv.html): AWS supports the Amazon DCV Extension SDK API within the WorkSpaces Applications host and client processes.
