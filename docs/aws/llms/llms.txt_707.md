# Source: https://docs.aws.amazon.com/res/archive/release-minus-3/ug/llms.txt

# Research and Engineering Studio User Guide

- [Architecture overview](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/architecture-overview.html)
- [Demo environment](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/create-demo-env.html)
- [Plan your deployment](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/plan-your-deployment.html)
- [Update the product](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/update-the-product.html)
- [Uninstall the product](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/uninstall-the-product.html)
- [Notices](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/notices.html)
- [Revisions](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/revisions.html)

## [Overview](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/overview.html)

- [Features and benefits](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/features-and-benefits.html): Research and Engineering Studio on AWS provides the following features:
- [Concepts and definitions](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/concepts-and-definitions.html): This section describes key concepts and defines terminology specific to Research and Engineering Studio on AWS:


## [Deploy the product](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/deploy-the-product.html)

- [Prerequisites](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/prerequisites.html)
- [Create external resources](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/create-external-resources.html): This CloudFormation stack creates networking, storage, active directory, and domain certificates (if a PortalDomainName is provided).
- [Step 1: Launch the product](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/launch-the-product.html): Follow the step-by-step instructions in this section to configure and deploy the product into your account.
- [Step 2: Sign in for the first time](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/first-sign-in.html): Once the product stack has deployed in your account, you will receive an email with your credentials.


## [Configuration guide](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/configuration-guide.html)

### [Identity management](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/manage-users.html)

Research and Engineering Studio can use any SAML 2.0 compliant identity provider.

- [Amazon Cognito identity setup](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/setting-up-cognito-users.html): Research and Engineering Studio (RES) allows you to set up Amazon Cognito as a native user directory.
- [Active Directory Synchronization](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/active-directory-sync.html)
- [Setting up SSO with IAM Identity Center](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/sso-idc.html): If you do not already have an identity center connected to the managed Active Directory, start with .
- [Configuring your identity provider for SSO](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/configure-id-federation.html): Research and Engineering Studio integrates with any SAML 2.0 identity provider to authenticate user access to the RES portal.
- [Setting passwords for users](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/setting-user-passwords.html)
- [Creating subdomains](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/create-subdomains.html): If you are using a custom domain, you will need to set up subdomains to support the web and VDI portions of your portal.
- [Create an ACM certificate](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/acm-certificate.html): By default, RES hosts the web portal under an application load balancer using the domain amazonaws.com.
- [Amazon CloudWatch Logs](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/log-groups.html): Research and Engineering Studio creates the following log groups in CloudWatch during installation.
- [Setting custom permission boundaries](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/permission-boundaries.html): As of 2024.04, you can optionally modify roles created by RES by attaching custom permission boundaries.
- [Configure RES-ready AMIs](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/res-ready-ami.html): With RES-ready Amazon Machine Images (AMIs), you can pre-install RES dependencies for virtual desktop instances (VDIs) on your custom AMIs.


## [Administrator guide](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/administrator-guide.html)

- [Secrets management](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/secrets-management.html): Research and Engineering Studio maintains the following secrets using AWS Secrets Manager.
- [Cost monitoring and control](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/cost-management.html)
- [Cost dashboard](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/cost-analysis-dashboard.html): The cost analysis dashboard allows RES administrators to monitor project budgets and project costs over time from the RES portal.

### [Session management](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/evdi.html)

Session management provides a flexible and interactive environment for developing and testing sessions.

- [Dashboard](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/dashboard.html)
- [Sessions](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/sessions.html): Sessions displays all virtual desktops created within Research and Engineering Studio.
- [Software Stacks (AMIs)](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/software-stacks.html): From the Software Stacks page, you can configure Amazon Machine Images (AMIs) or manage existing ones.
- [Debugging](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/debug.html): The debugging panel displays message traffic associated with the virtual desktops.
- [Desktop settings](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/desktop-settings.html): You can use the Desktop Settings page to configure resources associated with virtual desktops.

### [Environment management](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/environment-management.html)

From the Environment management section of Research and Engineering Studio, administrative users can create and manage isolated environments for their research and engineering projects.

- [Environment status](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/environment-status.html): The Environment Status page displays the deployed software and hosts within the product.
- [Environment settings](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/environment-settings.html): The Environment settings page displays product configuration details, such as:
- [Users](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/users.html): All users synced from your active directory will appear on the Users page.
- [Groups](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/groups.html): All Groups synced from the active directory appear on the Groups page.

### [Projects](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/projects.html)

Projects form a boundary for virtual desktops, teams, and budgets.

- [View projects](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/view-projects.html)
- [Create a project](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/create-project.html)
- [Edit a project](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/edit-project.html)
- [Disable a project](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/disable-project.html): To disable a project:
- [Delete a project](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/delete-project.html): To delete a project:
- [Add or remove tags from a project](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/tag-project.html): Project tags will assign tags to all instances created under that project.
- [View file systems associated with a project](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/view-project-file-systems.html): When a project is selected, you can expand the File Systems pane at the bottom of the screen to view file systems associated with the project.
- [Add a launch template](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/project-launch-template.html): When creating or editing a project, you can add launch templates using the Advanced Options within the project configuration.

### [Permission policy](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/permission-profiles.html)

Research and Engineering Studio (RES) allows an administrative user to create custom permission profiles that grant selected users additional permissions to manage the project that they are part of.

- [Project management permissions](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/permission-profiles-permission-project-management.html)
- [VDI session management permissions](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/permission-profiles-permission-vdi-sessions.html)
- [Managing permission profiles](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/permission-profiles-permission-management.html): As a RES administrator, you can perform the following actions to manage permission profiles.
- [Default permissions profiles](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/permission-matrix.html): Every RES project comes with two default permission profiles that Global Administrators can configure. (In addition, Global Administrators can create and modify new permission profiles for a project.) The following table shows the allowed permissions for the default permission profiles- "Project Member" and "Project Owner".

### [Environment boundaries](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/permission-profiles-environment-boundaries.html)

Environment boundaries allow Research and Engineering Studio (RES) administrators to configure permissions that will take effect globally for all users.

- [Configuring File browser access](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/configuring-file-browser-access.html): RES Administrators can toggle Access data on or off under File browser permissions.
- [Configuring SSH access](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/configuring-ssh-access.html): Administrators can enable or disable SSH for the RES environment from the Environment boundaries section.
- [Configuring Desktop Permissions](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/configuring-desktop-permissions.html): Administrators can toggle Desktop permissions on or off to globally manage the VDI functionality of all session owners.
- [Desktop sharing profiles](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/permission-profiles-desktop-sharing-profiles.html): Administrators can create new profiles and customize them.

### [File Systems](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/file-system.html)

- [Onboard a file system](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/onboard-file-system.html)

### [Snapshot management](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/snapshots.html)

Snapshot management simplifies the process of saving and migrating data between environments, ensuring consistency and accuracy.

- [Create a snapshot](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/create-snapshot.html): Before you can create a snapshot, you must provide an Amazon S3 bucket with the necessary permissions.
- [Apply a snapshot](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/apply-snapshot.html): Once you have created a snapshot of an environment, you can apply that snapshot to a new environment to migrate data.

### [Amazon S3 buckets](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/S3-buckets.html)

Research and Engineering Studio (RES) supports mounting Amazon S3 buckets to Linux Virtual Desktop Infrastructure (VDI) instances.

- [Amazon S3 bucket prerequisites for isolated VPC deployments](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/S3-buckets-prereqs.html): If you're deploying Research and Engineering Studio in an isolated VPC, follow these steps to update the lambda configuration parameters after you deploy RES in your AWS account.
- [Add an Amazon S3 bucket](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/S3-buckets-add.html)
- [Edit an Amazon S3 bucket](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/S3-buckets-edit.html)
- [Remove an Amazon S3 bucket](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/S3-buckets-remove.html)
- [Data Isolation](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/S3-buckets-data-isolation.html): When you add an S3 bucket to RES, you have options to isolate the data within the bucket to specific projects and users.
- [Cross account bucket access](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/S3-buckets-cross-account-access.html): RES has the ability to mount buckets from other AWS accounts, provided these buckets have the right permissions.
- [Preventing data exfiltration in a private VPC](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/S3-buckets-preventing-exfiltration.html): To prevent users from exfiltrating data from secure S3 buckets into their own S3 buckets in their account, you can attach a VPC endpoint to secure your private VPC.
- [Troubleshooting](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/S3-buckets-troubleshooting.html): How to check if a bucket fails to mount on a VDI
- [Enabling CloudTrail](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/S3-buckets-enabling-cloudtrail.html): To enable CloudTrail in your account using the CloudTrail console, follow the instructions provided in Creating a trail with the CloudTrail console in the AWS CloudTrail User Guide.


## [Use the product](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/use-the-product.html)

- [SSH access](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/ssh-access.html): To use SSH to access the bastion host:

### [Virtual desktops](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/virtual-desktops.html)

The virtual desktop interface (VDI) module allows users create and manage Windows or Linux virtual desktops on AWS.

- [Launch a new desktop](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/launch-desktop.html)
- [Access your desktop](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/access-desktop.html): To access a virtual desktop, choose the card for the desktop and connect using either the web or a DCV client.
- [Control your desktop state](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/control-desktop-state.html): To control your desktop's state:
- [Modify a virtual desktop](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/modify-virtual-desktop.html): You can update the hardware of your virtual desktop or change the session name.
- [Retrieve session information](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/retrieve-session-information.html)

### [Schedule virtual desktops](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/schedule-virtual-desktops.html)

By default, virtual desktops are scheduled to automatically stop on Saturdays and Sundays.

- [Setting individual desktop schedules](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/schedule-individual-desktops.html)
- [Setting default schedules](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/setting-default-schedules.html): The default schedule can be updated in DynamoDB :
- [VDI autostop](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/virtual-desktops-autostop.html): Administrators can configure settings to allow idle VDIs to be Stopped or Terminated.

### [Shared desktops](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/shared-desktops.html)

On Shared Desktops, you can see the desktops that have been shared with you.

- [Share a desktop](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/desktop-sharing.html)
- [Access a shared desktop](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/access-shared-desktop.html): From Shared Desktops, you can view the desktops shared with you and connect to an instance.

### [File browser](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/file-browser.html)

File browser allows you to access the global shared EFS filesystem through the web portal.

- [Upload file(s)](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/upload-file.html)
- [Delete file(s)](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/delete-file.html)
- [Manage favorites](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/manage-favorites.html): To pin important files and folders, you can add them to Favorites.
- [Edit files](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/edit-files.html): You can edit the content of text-based files within the web portal.
- [Transfer files](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/transfer-files.html): Use File Transfer to use external file transfer applications to transfer files.


## [Troubleshooting](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/troubleshooting.html)

- [General Debugging and Monitoring](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/res-troubleshooting-general.html): This section contains information about where information can be found within RES.
- [Issue RunBooks](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/res-troubleshooting-issue-runbooks.html): The following section contains issues that may occur, how to detect them, and suggestions on how to resolve the issue.
- [Known Issues](https://docs.aws.amazon.com/res/archive/release-minus-3/ug/res-troubleshooting-known-issues.html)
