# Source: https://docs.aws.amazon.com/workspaces/latest/adminguide/llms.txt

# Amazon WorkSpaces Administration Guide

> Use Amazon WorkSpaces to provision virtual, cloud-based Microsoft Windows or Amazon Linux desktops that users can access from multiple devices or web browsers.

- [What is WorkSpaces?](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html)
- [Connect using a client application](https://docs.aws.amazon.com/workspaces/latest/adminguide/connect-client.html)
- [Quotas](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-limits.html)
- [WorkSpaces client end of life](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-eol.html)
- [Extension SDK Developer Guide](https://docs.aws.amazon.com/workspaces/latest/adminguide/extension-sdk.html)
- [Document history](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-document-history.html)

## [Bring Your Own Windows desktop licenses](https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html)

- [Videos on uploading and creating BYOL images](https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-videos.html): Learn with videos on uploading BYOL and creating BYOL images.
- [Link BYOL accounts in WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/link-byol-account.html): You can use BYOL linking to link accounts and share BYOL configurations.
- [Common error messages and their solutions](https://docs.aws.amazon.com/workspaces/latest/adminguide/windows-images-common-errors.html)
- [List of SysPrep error messages and error fixes](https://docs.aws.amazon.com/workspaces/latest/adminguide/images-errors-sysprep.html)


## [Use and manage WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/managing-wsp-personal.html)

- [WorkSpaces Personal options](https://docs.aws.amazon.com/workspaces/latest/adminguide/how-to-start.html): There are several methods to create a WorkSpace.
- [Create a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/create-workspaces-personal.html): Learn how to create a personal WorkSpace.

### [Networking protocols and access](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-networking.html)

Learn about the networking and security features for WorkSpaces.

- [VPC requirements](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-vpc.html): Learn how to create a virtual private cloud for use with Amazon WorkSpaces.
- [AWS Global Accelerator (AGA)](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-aga.html): Learn how to configure AWS Global Accelerator (AGA) for Amazon WorkSpaces.
- [Availability Zones for WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/azs-workspaces.html): Learn how to work with Availability Zones when setting up a virtual private cloud (VPC) for use with Amazon WorkSpaces.
- [IP address and port requirements](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html): Learn how to set up the IP addresses and ports required by WorkSpaces.
- [Network requirements](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-network-requirements.html): Learn how to verify that a client device meets the networking requirements for WorkSpaces.
- [Trusted devices](https://docs.aws.amazon.com/workspaces/latest/adminguide/trusted-devices.html): Learn how to restrict WorkSpaces access to trusted devices.

### [SAML 2.0 integration](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-saml.html)

Learn how to integrate WorkSpaces with SAML 2.0.

- [Set up SAML 2.0 for WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/setting-up-saml.html): Enable WorkSpaces client application registration and signing in to WorkSpaces for your users by using their SAML 2.0 identity provider (IdP) credentials and authentication methods by setting up identity federation using SAML 2.0.
- [Certificate-based authentication](https://docs.aws.amazon.com/workspaces/latest/adminguide/certificate-based-authentication.html): Learn how to use certificate-based authentication with WorkSpaces.
- [Microsoft Entra ID access](https://docs.aws.amazon.com/workspaces/latest/adminguide/access-entra-id.html): Learn how to access Microsoft Entra ID-joined WorkSpaces Personal.
- [Smart card authentication](https://docs.aws.amazon.com/workspaces/latest/adminguide/smart-cards.html): Learn how to enable smart card authentication for WorkSpaces.
- [Internet access](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-internet-access.html): Learn how to enable internet Access from your WorkSpaces.
- [Security groups](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-security-groups.html): Learn how to configure the security groups for your WorkSpaces.
- [IP access control groups](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-ip-access-control-groups.html): Learn how to configure IP access control groups for your WorkSpaces.
- [PCoIP zero client](https://docs.aws.amazon.com/workspaces/latest/adminguide/set-up-pcoip-zero-client.html): PCoIP zero clients are compatible only with WorkSpaces bundles that are using the PCoIP protocol.
- [Set up Android for Chromebook](https://docs.aws.amazon.com/workspaces/latest/adminguide/set-up-android-chromebook.html): Version 2.4.13 is the final release of the Amazon WorkSpaces Chromebook client application.
- [Configure web access](https://docs.aws.amazon.com/workspaces/latest/adminguide/web-access.html): Learn how to enable Web Access to your WorkSpaces.
- [Configure Amazon WorkSpaces Thin Client](https://docs.aws.amazon.com/workspaces/latest/adminguide/access-control-awstc.html): Learn how to enable Access Control to your Amazon WorkSpaces Thin Client.
- [Configure FIPS endpoint encryption](https://docs.aws.amazon.com/workspaces/latest/adminguide/fips-encryption.html): Learn how to set up Amazon WorkSpaces for FedRAMP authorization or compliance with the DoD SRG.
- [Enable SSH connections for Linux WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/connect-to-linux-workspaces-with-ssh.html): If you or your users want to connect to your Linux WorkSpaces by using the command line, you can enable SSH connections.
- [Required configuration and service components](https://docs.aws.amazon.com/workspaces/latest/adminguide/required-service-components.html): As a WorkSpace administrator, you must understand the following about required configuration and service components.

### [Manage directories for WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/manage-workspaces-directory.html)

Learn how to manage directories for your WorkSpaces.

- [Register an existing Directory Service directory](https://docs.aws.amazon.com/workspaces/latest/adminguide/register-deregister-directory.html): Learn how to register directories for your WorkSpaces.
- [Select an organizational unit](https://docs.aws.amazon.com/workspaces/latest/adminguide/select-ou.html)
- [Configure automatic public IP addresses](https://docs.aws.amazon.com/workspaces/latest/adminguide/automatic-assignment.html): After you enable automatic assignment of public IP addresses, each WorkSpace that you launch is assigned a public IP address from the Amazon-provided pool of public addresses.
- [Control device access](https://docs.aws.amazon.com/workspaces/latest/adminguide/control-device-access.html): You can specify the types of devices that have access to WorkSpaces based on the device platform.
- [Manage local administrator permissions](https://docs.aws.amazon.com/workspaces/latest/adminguide/local-admin-setting.html)
- [Update the AD Connector account (AD Connector)](https://docs.aws.amazon.com/workspaces/latest/adminguide/connect-account.html): You can update the AD Connector account that is used to read users and groups and join WorkSpaces machine accounts to your AD Connector directory.
- [Multi-factor authentication (AD Connector)](https://docs.aws.amazon.com/workspaces/latest/adminguide/connect-mfa.html): You can enable multi-factor authentication (MFA) for your AD Connector directory.

### [Create a directory](https://docs.aws.amazon.com/workspaces/latest/adminguide/launch-workspaces-tutorials.html)

Learn how to create a WorkSpaces Personal directory.

- [Identify the computer name](https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-directory-identify-computer.html): The Computer Name value shown for a WorkSpace in the Amazon WorkSpaces console varies, depending on which type of WorkSpace you've launched (Amazon Linux, Ubuntu, or Windows).
- [Create an AWS managed Microsoft AD directory](https://docs.aws.amazon.com/workspaces/latest/adminguide/launch-workspace-microsoft-ad.html): Learn how to create an AWS managed Microsoft AD directory.
- [Create a Simple AD directory](https://docs.aws.amazon.com/workspaces/latest/adminguide/launch-workspace-simple-ad.html): Learn how to create a Simple AD directory.
- [Create an AD Connector](https://docs.aws.amazon.com/workspaces/latest/adminguide/launch-workspace-ad-connector.html): Learn how to create an AD Connector.
- [Create a trust relationship](https://docs.aws.amazon.com/workspaces/latest/adminguide/launch-workspace-trusted-domain.html): Learn how to create a trust relationship between your AWS Managed Microsoft AD directory and your on-premises domain.
- [Create a dedicated Microsoft Entra ID directory](https://docs.aws.amazon.com/workspaces/latest/adminguide/launch-entra-id.html): Learn how to create a dedicated Microsoft Entra ID directory.
- [Create a dedicated Custom directory](https://docs.aws.amazon.com/workspaces/latest/adminguide/launch-custom.html): Learn how to create a dedicated Custom directory with WorkSpaces Personal.
- [Update DNS servers for WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/update-dns-server.html): Learn how to update the DNS servers for Amazon WorkSpaces.
- [Delete a directory](https://docs.aws.amazon.com/workspaces/latest/adminguide/delete-workspaces-directory.html): Learn how to delete directories for your WorkSpaces.
- [Set up Directory Administration](https://docs.aws.amazon.com/workspaces/latest/adminguide/directory_administration.html): Learn how to set up Active Directory Administration tools for your WorkSpaces.

### [Administer users](https://docs.aws.amazon.com/workspaces/latest/adminguide/administer-workspace-users.html)

Learn how to administer users in WorkSpaces Personal.

- [Manage users](https://docs.aws.amazon.com/workspaces/latest/adminguide/manage-workspaces-users.html): Learn how to manage WorkSpaces users using the WorkSpaces console.
- [Create multiple WorkSpaces for a user](https://docs.aws.amazon.com/workspaces/latest/adminguide/create-multiple-workspaces-for-user.html): Learn how to create multiple WorkSpaces for a user.
- [Customize how users log in to their WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/customize-workspaces-user-login.html): Learn how to customize how users log in to their WorkSpaces.
- [Enable self-service WorkSpaces management capabilities](https://docs.aws.amazon.com/workspaces/latest/adminguide/enable-user-self-service-workspace-management.html): Learn how to enable self-service management WorkSpace capabilities for your users.
- [Enable Amazon Connect audio optimization](https://docs.aws.amazon.com/workspaces/latest/adminguide/enable-amazon-connect-audio-optimization.html): Learn how to enable Amazon Connect audio optimization for your users.
- [Enable diagnostic log uploads](https://docs.aws.amazon.com/workspaces/latest/adminguide/enable-diagnostic-log-uploads.html): Learn how to enable diagnostic log uploads in WorkSpaces Personal.

### [Administer WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/administer-workspaces.html)

Learn how to launch, configure, and manage WorkSpaces for your users.

- [Manage Windows WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/group_policy.html): Learn how to use Group Policy Objects (GPOs) to manage your Windows WorkSpaces.
- [Manage your Amazon Linux 2 WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/manage_linux_workspace.html): Learn how to manage your Amazon Linux 2 WorkSpaces
- [Manage your Ubuntu WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/manage_ubuntu_workspace.html): Learn how to manage your Amazon Linux WorkSpaces
- [Manage your Rocky Linux WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/manage_rockylinux_workspace.html): Learn how to manage your Rocky Linux WorkSpaces
- [Manage your Red Hat Enterprise Linux WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/manage_rhel_workspace.html): Learn how to manage your Amazon Linux WorkSpaces
- [Optimize for real-time communication](https://docs.aws.amazon.com/workspaces/latest/adminguide/communication-optimization.html): Learn how to optimize your Amazon WorkSpaces for Real-Time Communication.
- [Manage the running mode](https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html): Learn how to manage the running mode of your WorkSpaces to switch between monthly and hourly billing.
- [Manage applications](https://docs.aws.amazon.com/workspaces/latest/adminguide/manage-applications.html): Learn how to Manage applications.
- [Modify a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-workspaces.html): Learn how to modify the configuration of a WorkSpace.
- [Customize branding](https://docs.aws.amazon.com/workspaces/latest/adminguide/customize-branding.html): Learn how to customize WorkSpace branding.
- [Tag resources](https://docs.aws.amazon.com/workspaces/latest/adminguide/tag-workspaces-resources.html): Learn how to manage the resources for your WorkSpaces using tags.
- [Maintenance](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspace-maintenance.html): Learn about maintenance in WorkSpaces Personal.
- [Encrypted WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/encrypt-workspaces.html): Learn how to encrypt your WorkSpaces.
- [Reboot a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/reboot-workspaces.html): Learn how to reboot (restart) your WorkSpaces.
- [Rebuild a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/rebuild-workspace.html): Learn how to rebuild your WorkSpaces.
- [Restore a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/restore-workspace.html): Learn how to restore WorkSpaces in WorkSpaces Personal.
- [Microsoft 365 BYOL](https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-microsoft365-licenses.html): Learn how to use Microsoft 365 Bring Your Own License (BYOL)
- [Upgrade Windows BYOL WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/upgrade-windows-10-byol-workspaces.html): Learn how to perform in-place Windows updates on your Windows Bring Your Own License (BYOL) WorkSpaces.
- [Migrate a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/migrate-workspaces.html): Learn how to migrate your WorkSpaces.
- [Delete a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/delete-workspaces.html): Learn how to delete your WorkSpaces.

### [Bundles and images](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-bundles.html)

Learn how to manage custom WorkSpaces bundles and images.

- [Bundle options](https://docs.aws.amazon.com/workspaces/latest/adminguide/bundle-options.html): Learn about WorkSpaces bundles
- [Create a custom image and bundle](https://docs.aws.amazon.com/workspaces/latest/adminguide/create-custom-bundle.html): Learn how to create a custom WorkSpaces image and bundle.
- [Update a custom bundle](https://docs.aws.amazon.com/workspaces/latest/adminguide/update-custom-bundle.html): Learn how to update a custom WorkSpaces bundle.
- [Copy a custom image](https://docs.aws.amazon.com/workspaces/latest/adminguide/copy-custom-image.html): You can copy a custom WorkSpaces image within or across AWS Regions.
- [Share or unshare a custom image](https://docs.aws.amazon.com/workspaces/latest/adminguide/share-custom-image.html): Learn how to share and unshare a custom WorkSpaces image with other accounts.
- [Delete a custom bundle or image](https://docs.aws.amazon.com/workspaces/latest/adminguide/delete_bundle.html): Learn how to delete a custom WorkSpaces bundle or image.

### [Monitor WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-monitoring.html)

Monitor your WorkSpaces using Amazon CloudWatch and Amazon CloudWatch Events.

- [Monitor with CloudWatch automatic dashboard](https://docs.aws.amazon.com/workspaces/latest/adminguide/cloudwatch-dashboard.html): You can monitor WorkSpaces using CloudWatch automatic dashboard, which collects raw data and processes it into readable, near real-time metrics.
- [Monitor using CloudWatch metrics](https://docs.aws.amazon.com/workspaces/latest/adminguide/cloudwatch-metrics.html): WorkSpaces and Amazon CloudWatch are integrated, so you can gather and analyze performance metrics.
- [Monitor using Amazon EventBridge](https://docs.aws.amazon.com/workspaces/latest/adminguide/cloudwatch-events.html): You can use events from Amazon WorkSpaces to view, search, download, archive, analyze, and respond to successful logins to your WorkSpaces.
- [Understanding AWS sign-in events for smart card users](https://docs.aws.amazon.com/workspaces/latest/adminguide/signin-events.html): AWS CloudTrail logs successful and unsuccessful sign-in events for smart card users.
- [Create custom CloudWatch dashboards](https://docs.aws.amazon.com/workspaces/latest/adminguide/cloudformation-templates.html): Learn how to create custom CloudFormation dashboard using templates.

### [Business continuity](https://docs.aws.amazon.com/workspaces/latest/adminguide/business-continuity.html)

Learn about business continuity features in Amazon WorkSpaces.

- [Cross-Region redirection](https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html): Learn how to use cross-Region redirection to provide alternative WorkSpaces to your users in the event of outages.
- [Multi-Region Resilience](https://docs.aws.amazon.com/workspaces/latest/adminguide/multi-region-resilience.html): Learn how to use Multi-Region Resilience to provide alternative WorkSpaces to your users in the event of outages.
- [Troubleshooting](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-troubleshooting.html): Troubleshooting WorkSpaces administration issues.
- [Release notes](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-release-notes.html): Version information for DCV.


## [Use and manage WorkSpaces Pools](https://docs.aws.amazon.com/workspaces/latest/adminguide/managing-wsp-pools.html)

- [Supported Regions and Availability Zones](https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-pools-regions.html): Learn about the AWS Regions for WorkSpaces Pools.

### [Manage directories](https://docs.aws.amazon.com/workspaces/latest/adminguide/manage-workspaces-pools-directory.html)

Learn how to manage directories for your WorkSpaces Pools.

### [Configure SAML 2.0 and create a pool directory](https://docs.aws.amazon.com/workspaces/latest/adminguide/create-directory-pools.html)

Learn how to create a WorkSpaces Pools directory.

- [Specify Active Directory details](https://docs.aws.amazon.com/workspaces/latest/adminguide/pools-service-account-details.html): In this topic, we show you how to specify your Active Directory (AD) details within the Create WorkSpaces Pool directory page of the WorkSpaces console.
- [Update directory details](https://docs.aws.amazon.com/workspaces/latest/adminguide/update-directory-pools-details.html): Learn how to update directory details for your WorkSpaces Pools.
- [Delete a WorkSpaces Pools directory](https://docs.aws.amazon.com/workspaces/latest/adminguide/delete-directory-pools.html): Complete the following procedures to delete a WorkSpaces Pools directory.

### [Networking and Access](https://docs.aws.amazon.com/workspaces/latest/adminguide/managing-network.html)

The following topics provide information about enabling users to connect to WorkSpaces Pools and enabling your WorkSpaces Pools to access network resources and the internet.

- [Internet Access](https://docs.aws.amazon.com/workspaces/latest/adminguide/internet-access.html): If your WorkSpaces in WorkSpaces Pools require internet access, you can enable it in several ways.

### [VPC Requirements](https://docs.aws.amazon.com/workspaces/latest/adminguide/appstream-vpc.html)

When you set up WorkSpaces Pools, you must specify the virtual private cloud (VPC) and at least one subnet in which to launch your WorkSpaces.

- [VPC Setup Recommendations](https://docs.aws.amazon.com/workspaces/latest/adminguide/vpc-setup-recommendations.html): When you create a WorkSpaces Pools, you specify the VPC and one or more subnets to use.

### [Configure a VPC with Private Subnets and a NAT Gateway](https://docs.aws.amazon.com/workspaces/latest/adminguide/managing-network-internet-NAT-gateway.html)

If you plan to provide your WorkSpaces in WorkSpaces Pools with access to the internet, we recommend that you configure a VPC with two private subnets for your WorkSpaces and a NAT gateway in a public subnet.

- [Create and Configure a New VPC](https://docs.aws.amazon.com/workspaces/latest/adminguide/create-configure-new-vpc-with-private-public-subnets-nat.html): This topic describes how to use the VPC wizard to create a VPC with a public subnet and one private subnet.
- [Add a NAT Gateway to an Existing VPC](https://docs.aws.amazon.com/workspaces/latest/adminguide/add-nat-gateway-existing-vpc.html): If you have already configured a VPC, complete the following steps to add a NAT gateway to your VPC.
- [Enable Internet Access for WorkSpaces Pools](https://docs.aws.amazon.com/workspaces/latest/adminguide/managing-network-manual-enable-internet-access.html): After your NAT gateway is available on a VPC, you can enable internet access for your WorkSpaces Pools.
- [Configure a VPC with a Public Subnet](https://docs.aws.amazon.com/workspaces/latest/adminguide/managing-network-default-internet-access.html): If you created your Amazon Web Services account after 2013-12-04, you have a default VPC in each AWS Region that includes default public subnets.
- [Use the Default VPC and Public Subnet](https://docs.aws.amazon.com/workspaces/latest/adminguide/default-vpc-with-public-subnet.html): Your Amazon Web Services account, if it was created after 2013-12-04, has a default VPC in each AWS Region.
- [Configure FIPS endpoint encryption](https://docs.aws.amazon.com/workspaces/latest/adminguide/fips-encryption-pools.html): Learn how to set up Amazon WorkSpaces for FedRAMP authorization or compliance with the DoD SRG.
- [Amazon S3 VPC Endpoints](https://docs.aws.amazon.com/workspaces/latest/adminguide/managing-network-vpce-iam-policy.html): When you enable Application Settings Persistence for a WorkSpaces Pool or Home folders for a WorkSpaces Pool directory, WorkSpaces uses the VPC you specify for your directory to provide access to Amazon Simple Storage Service (Amazon S3) buckets.
- [Connections to Your VPC](https://docs.aws.amazon.com/workspaces/latest/adminguide/pools-port-requirements.html): Learn how to set up the ports required for WorkSpaces Pools connections to your VPC

### [User connections](https://docs.aws.amazon.com/workspaces/latest/adminguide/user-connections-to-appstream2.html)

Learn about user connections to WorkSpaces Pools, including bandwidth recommendations, required ports and domains, and how to create and stream from interface VPC endpoints (interface endpoints).

- [Bandwidth Recommendations](https://docs.aws.amazon.com/workspaces/latest/adminguide/bandwidth-recommendations-user-connections.html): To optimize the performance of WorkSpaces Pools, make sure that your network bandwidth and latency can sustain your users' needs.
- [IP Address and Port Requirements](https://docs.aws.amazon.com/workspaces/latest/adminguide/pools-client-application-ports.html): WorkSpaces Pools users' devices require outbound access on port 443 (TCP) and port 4195 (UDP) when using the internet endpoints, and if you are using DNS servers for domain name resolution, port 53 (UDP).
- [Allowed Domains](https://docs.aws.amazon.com/workspaces/latest/adminguide/allowed-domains.html): For WorkSpaces Pools users to access WorkSpaces, you must allow various domains on the network from which users initiate access to the WorkSpaces.
- [Create a WorkSpaces Pool](https://docs.aws.amazon.com/workspaces/latest/adminguide/set-up-pools-create.html): Learn how to create a WorkSpaces Pool.

### [Administer WorkSpaces Pools](https://docs.aws.amazon.com/workspaces/latest/adminguide/managing-stacks-fleets.html)

Learn how to administer WorkSpaces Pools.

### [Running mode](https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode-pools.html)

Learn how WorkSpaces Pools run.

- [Modify the running mode](https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-running-mode-pool.html): Learn how to modify the running mode.
- [Bundles](https://docs.aws.amazon.com/workspaces/latest/adminguide/instance-types.html): Learn about WorkSpaces Pools bundles.
- [Modify a pool](https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-pool.html): After creating a WorkSpaces Pool, you can modify the following:
- [Delete a pool](https://docs.aws.amazon.com/workspaces/latest/adminguide/set-up-pools-finish.html): You can delete pools to free up resources and to avoid unintended charges to your account.
- [Auto Scaling for WorkSpaces Pools](https://docs.aws.amazon.com/workspaces/latest/adminguide/autoscaling.html): Use or disable scaling with WorkSpaces Pools

### [Using Active Directory](https://docs.aws.amazon.com/workspaces/latest/adminguide/active-directory.html)

Join your WorkSpaces Pools to your Active Directory domain.

- [Active Directory Domains](https://docs.aws.amazon.com/workspaces/latest/adminguide/active-directory-overview.html): Using Active Directory domains with WorkSpaces Pools requires an understanding of how they work together and the configuration tasks that you'll need to complete.
- [Before You Begin](https://docs.aws.amazon.com/workspaces/latest/adminguide/active-directory-prerequisites.html): Before you use Microsoft Active Directory domains with WorkSpaces Pools, be aware of the following requirements and considerations.

### [Certificate-Based Authentication](https://docs.aws.amazon.com/workspaces/latest/adminguide/pools-certificate-based-authentication.html)

You can use certificate-based authentication with WorkSpaces Pools joined to Microsoft Active Directory.

- [Prerequisites](https://docs.aws.amazon.com/workspaces/latest/adminguide/certificate-based-authentication-prereq.html): Complete the following steps before you use certificate-based authentication.
- [Enable Certificate-based Authentication](https://docs.aws.amazon.com/workspaces/latest/adminguide/certificate-based-authentication-enable.html): Complete the following steps to enable certificate-based authentication.
- [Manage Certificate-based Authentication](https://docs.aws.amazon.com/workspaces/latest/adminguide/certificate-based-authentication-manage.html): After you enable certificate-based authentication, review the following tasks.
- [Enable Cross-account PCA Sharing](https://docs.aws.amazon.com/workspaces/latest/adminguide/pca-sharing.html): Private CA (PCA) cross-account sharing offers the ability to grant permissions for other accounts to use a centralized CA.
- [Administration](https://docs.aws.amazon.com/workspaces/latest/adminguide/active-directory-admin.html): Setting up and using Active Directory with WorkSpaces Pools involves the following administrative tasks.
- [More Info](https://docs.aws.amazon.com/workspaces/latest/adminguide/active-directory-more-info.html): For more information related to this topic, see the following resources:

### [Bundles and images](https://docs.aws.amazon.com/workspaces/latest/adminguide/pools-images.html)

Learn how to administer WorkSpaces Pools.

- [Bundles options](https://docs.aws.amazon.com/workspaces/latest/adminguide/pools-custom-images-bundles.html): Learn about the bundle options for WorkSpaces Pools.
- [Create a custom image and bundle](https://docs.aws.amazon.com/workspaces/latest/adminguide/pools-images-custom-image.html): Learn how to create a custom image and bundle for WorkSpaces Pools.
- [Manage custom images and bundles](https://docs.aws.amazon.com/workspaces/latest/adminguide/pools-images-managing.html): Learn how to manage custom images and bundles for WorkSpaces Pools.
- [Use session scripts to manage experience](https://docs.aws.amazon.com/workspaces/latest/adminguide/pools-images-session-scripts.html): Learn how to use session scripts to manage the streaming experience for your users in WorkSpaces Pools.

### [Monitoring WorkSpaces Pools](https://docs.aws.amazon.com/workspaces/latest/adminguide/configure-monitoring-reporting.html)

Learn about monitoring WorkSpaces Pools.

- [WorkSpaces Pools metrics and dimensions](https://docs.aws.amazon.com/workspaces/latest/adminguide/monitoring-with-cloudwatch.html): Amazon WorkSpaces sends the following WorkSpaces Pools metrics and dimension information to Amazon CloudWatch.
- [Administer Persistent Storage](https://docs.aws.amazon.com/workspaces/latest/adminguide/persistent-storage.html): Learn how to enable persistent storage for WorkSpaces Pools.

### [Enable application settings persistence for your users](https://docs.aws.amazon.com/workspaces/latest/adminguide/app-settings-persistence.html)

Enable application settings persistence for WorkSpaces Pools users.

- [How application settings persistence works](https://docs.aws.amazon.com/workspaces/latest/adminguide/how-it-works-app-settings-persistence.html): Learn how application settings persistence works.
- [Enabling application settings persistence](https://docs.aws.amazon.com/workspaces/latest/adminguide/enabling-app-settings-persistence.html): Learn how to enable application settings persistence for your WorkSpaces Pools users.
- [Administer the VHDs for your users' application settings](https://docs.aws.amazon.com/workspaces/latest/adminguide/administer-app-settings-vhds.html): Learn how to administer the Virtual Hard Disks (VHD) files for your WorkSpaces Pools users' application settings.
- [Troubleshooting notification codes](https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-pools-troubleshooting.html): Learn about WorkSpaces Pools troubleshooting notification codes.


## [Security](https://docs.aws.amazon.com/workspaces/latest/adminguide/security.html)

- [Data protection](https://docs.aws.amazon.com/workspaces/latest/adminguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Amazon WorkSpaces.

### [Identity and access management](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-access-control.html)

Control which WorkSpaces resources can be viewed, created, and modified by IAM users.

- [AWS managed policies for WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/managed-policies.html): Learn about the managed policies for WorkSpaces.
- [Access to WorkSpaces and scripts on streaming instances](https://docs.aws.amazon.com/workspaces/latest/adminguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html): Applications and scripts that run on WorkSpaces streaming instances must include AWS credentials in their AWS API requests.
- [Amazon WorkSpaces Console operations permissions reference](https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-console-permissions-ref.html): Some Amazon WorkSpaces APIs can only be called through the AWS Management Console.
- [Compliance validation](https://docs.aws.amazon.com/workspaces/latest/adminguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/workspaces/latest/adminguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon WorkSpaces features for data resiliency.

### [Infrastructure Security](https://docs.aws.amazon.com/workspaces/latest/adminguide/infrastructure-security.html)

Learn how Amazon WorkSpaces isolates service traffic.

- [Network isolation](https://docs.aws.amazon.com/workspaces/latest/adminguide/network-isolation.html): A virtual private cloud (VPC) is a virtual network in your own logically isolated area in the AWS Cloud.
- [Isolation on physical hosts](https://docs.aws.amazon.com/workspaces/latest/adminguide/physical-isolation.html): Different WorkSpaces on the same physical host are isolated from each other through the hypervisor.
- [Credential Guard / Virtualization-Based Security (VBS)](https://docs.aws.amazon.com/workspaces/latest/adminguide/credential-guard-vbs.html): Windows WorkSpaces can utilize Credential Guard and Virtualization-Based Security (VBS) to provide hardware-based isolation and protect credentials within the operating system.
- [Authorization of corporate users](https://docs.aws.amazon.com/workspaces/latest/adminguide/authorization.html): With WorkSpaces, directories are managed through the Directory Service.
- [Create and Stream from Interface VPC Endpoints](https://docs.aws.amazon.com/workspaces/latest/adminguide/creating-streaming-vpc-endpoints.html): A virtual private cloud (VPC) is a virtual network in your own logically isolated area in the Amazon Web Services Cloud.
- [Make Amazon WorkSpaces API requests through a VPC interface endpoint](https://docs.aws.amazon.com/workspaces/latest/adminguide/interface-vpc-endpoint.html): Access Amazon WorkSpaces API endpoints through a VPC interface endpoint.
- [Create a VPC endpoint policy for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/api-private-link-policy.html): You can create a policy for Amazon VPC endpoints for Amazon WorkSpaces to specify the following:
- [Connect your private network to your VPC](https://docs.aws.amazon.com/workspaces/latest/adminguide/notebook-private-link-vpn.html): To call the Amazon WorkSpaces API through your VPC, you have to connect from an instance that is inside the VPC, or connect your private network to your VPC by using AWS Virtual Private Network (Site-to-Site VPN) or Direct Connect.
- [Update management](https://docs.aws.amazon.com/workspaces/latest/adminguide/update-management.html): We recommend that you regularly patch, update, and secure the operating system and applications on your WorkSpaces.
