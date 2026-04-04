# Source: https://docs.aws.amazon.com/res/archive/release-minus-1/ug/llms.txt

# Research and Engineering Studio User Guide

- [Architecture overview](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/architecture-overview.html)
- [Demo environment](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/create-demo-env.html)
- [Plan your deployment](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/plan-your-deployment.html)
- [Update the product](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/update-the-product.html)
- [Uninstall the product](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/uninstall-the-product.html)
- [Research and Engineering Studio support policy](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/support-policy.html)
- [Notices](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/notices.html)
- [Revisions](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/revisions.html)

## [Overview](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/overview.html)

- [Features and benefits](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/features-and-benefits.html): What are the features and benefits of Research and Engineering Studio
- [Concepts and definitions](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/concepts-and-definitions.html): What are the key concepts and the terminology specific to Research and Engineering Studio


## [Deploy the product](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/deploy-the-product.html)

- [Prerequisites](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/prerequisites.html): The prerequisites for setting up Research and Engineering Studio
- [Create external resources](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/create-external-resources.html): How to use a CloudFormation stack to create networking, storage, active directory, and domain certificates before deployment.
- [Step 1: Launch the product](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/launch-the-product.html): How to configure and deploy Research and Engineering Studio.
- [Step 2: Sign in for the first time](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/first-sign-in.html): How to sign in to your account and configure the workspace for other users.


## [Configuration guide](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/configuration-guide.html)

### [Identity management](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/manage-users.html)

Ways to manage user identities

- [Amazon Cognito identity setup](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/setting-up-cognito-users.html): How to set up users with Cognito identities
- [Active Directory Synchronization](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/active-directory-sync.html): How to set up user identities using Active Directory
- [Setting up SSO with IAM Identity Center](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/sso-idc.html): How to set up user identities using single sign-on (SSO)
- [Configuring your identity provider for SSO](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/configure-id-federation.html): How to integrate with your chosen SAML 2.0 identity provider.
- [Setting passwords for users](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/setting-user-passwords.html): How to set passwords for users
- [Creating subdomains](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/create-subdomains.html): How to set up subdomains to support the web and VDI portions of your portal when using a custom domain.
- [Create an ACM certificate](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/acm-certificate.html): How to configure a public SSL/TLS certificate provided by you or requested from AWS Certificate Manager (ACM) in order to use your own domain.
- [Amazon CloudWatch Logs](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/log-groups.html): CloudWatch log groups created during installation
- [Setting custom permission boundaries](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/permission-boundaries.html): How to set custom permission boundaries
- [Configure RES-ready AMIs](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/res-ready-ami.html): Use Research and Engineering Studio-ready Amazon Machine Images (AMIs), to pre-install dependencies for virtual desktop instances (VDIs) on your custom AMIs.
- [Set up custom domains after RES installation](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/setup-custom-domain-after-install.html)


## [Administrator guide](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/administrator-guide.html)

- [Secrets management](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/secrets-management.html): Research and Engineering Studio maintains secrets using AWS Secrets Manager and creates secrets automatically during environment creation.
- [Cost monitoring and control](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/cost-management.html): Create a budget for Research and Engineering Studio through AWS Cost Explorer to help manage costs.
- [Cost dashboard](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/cost-analysis-dashboard.html): Allows RES administrators to monitor project budgets and costs over time, filtered at the project level.

### [Session management](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/evdi.html)

Administrators can permit users to create and manage interactive sessions in their project environments.

- [Dashboard](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/dashboard.html): The Session Management Dashboard gives administrators a view into: Instance types, Session states, Base OS, Projects, Availability zones, and Software stacks
- [Sessions](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/sessions.html): From the Sessions page, you can filter and view session information or create a new session.
- [Software Stacks (AMIs)](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/software-stacks.html): The Software Stacks page lets you configure Amazon Machine Images (AMIs) or manage existing ones.
- [Debugging](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/debug.html): The debugging panel displays message traffic between the virtual desktops.
- [Desktop settings](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/desktop-settings.html): Use the Desktop Settings page to configure resources associated with virtual desktops.

### [Environment management](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/environment-management.html)

The Environment management section lets administrators create and manage isolated environments, including compute resources and storage.

- [Environment status](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/environment-status.html): The Environment Status page displays deployed software and hosts including software version and module names.
- [Environment settings](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/environment-settings.html): The Environment settings page displays product configuration details.
- [Users](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/users.html): All users synced from your active directory will appear on the Users page.
- [Groups](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/groups.html): All Groups synced from the active directory appear on the Groups page.

### [Projects](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/projects.html)

How to create a project and include a customized environment to meet specific requirements.

- [View projects](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/view-projects.html): How to view and modify your projects.
- [Create a project](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/create-project.html): How to create a project.
- [Edit a project](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/edit-project.html): How to edit a project
- [Disable a project](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/disable-project.html): How to disable a project.
- [Delete a project](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/delete-project.html): How to delete a project.
- [Add or remove tags from a project](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/tag-project.html): How to add or remove tags from a project.
- [View file systems associated with a project](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/view-project-file-systems.html): How to view file systems associated with a project.
- [Add a launch template](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/project-launch-template.html): How to add a launch template.

### [Permission policy](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/permission-profiles.html)

Administrators can create custom permission profiles that grant selected users additional permissions to manage projects they are part of.

- [Project management permissions](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/permission-profiles-permission-project-management.html): Lets non-admin users add and remove users or groups from a project, and set permission profiles access levels for all users and groups.
- [VDI session management permissions](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/permission-profiles-permission-vdi-sessions.html): Controls user permissions to launch their own VDI session from the My Virtual Desktops page.
- [Managing permission profiles](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/permission-profiles-permission-management.html): Administrators can create, edit, delete, list and view permission profiles.
- [Default permissions profiles](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/permission-matrix.html): Administrators have two default permission profiles they can configure, and they can create and modify new ones.

### [Environment boundaries](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/permission-profiles-environment-boundaries.html)

Environment boundaries let administrators configure global file browser, SSH, Desktop, and Desktop advanced settings permissions.

- [Configuring File browser access](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/configuring-file-browser-access.html): File browser permissions lets administrators toggle Access data on or off so users can upload or download data attached to their global file system.
- [Configuring SSH access](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/configuring-ssh-access.html): Administrators can enable or disable SSH from the Environment boundaries section.
- [Configuring Desktop Permissions](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/configuring-desktop-permissions.html): Administrators can manage the VDI functionality of session owners, and create Desktop sharing profiles that determine which actions users with whom a desktop is shared can perform.
- [Desktop sharing profiles](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/permission-profiles-desktop-sharing-profiles.html): Administrators can create and customize new profiles that are used when sharing a session with others.

### [File Systems](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/file-system.html)

The File Systems page lets you search for and select a file system, then add, remove, onboard, or view details of the file system.

- [Onboard a file system](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/onboard-file-system.html): The File Systems page lets you onboard a file system.

### [Snapshot management](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/snapshots.html)

Snapshot management saves and migrates data between environments.

- [Create a snapshot](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/create-snapshot.html): Create a snapshot
- [Apply a snapshot](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/apply-snapshot.html): Apply a snapshot

### [Amazon S3 buckets](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/S3-buckets.html)

Using S3 buckets

- [Amazon S3 bucket prerequisites for isolated VPC deployments](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/S3-buckets-prereqs.html): How to set S3 bucket prerequisites for isolated VPC deployments
- [Add an Amazon S3 bucket](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/S3-buckets-add.html): How to add an S3 bucket
- [Edit an Amazon S3 bucket](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/S3-buckets-edit.html): How to edit an S3 bucket
- [Remove an Amazon S3 bucket](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/S3-buckets-remove.html): How to remove an S3 bucket
- [Data Isolation](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/S3-buckets-data-isolation.html): When you add an S3 bucket you have options to isolate the data within the bucket to specific projects and users.
- [Cross account bucket access](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/S3-buckets-cross-account-access.html): How to set up cross account S3 bucket access
- [Preventing data exfiltration in a private VPC](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/S3-buckets-preventing-exfiltration.html): How to prevent users from exfiltrating data from secure S3 buckets into their own S3 buckets in their account.
- [Troubleshooting](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/S3-buckets-troubleshooting.html): How to troubleshoot issues with S3 buckets
- [Enabling CloudTrail](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/S3-buckets-enabling-cloudtrail.html): How to enable CloudTrail logging


## [Use the product](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/use-the-product.html)

- [SSH access](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/ssh-access.html): How to use SSH to access the bastion host

### [Virtual desktops](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/virtual-desktops.html)

Use the virtual desktop interface (VDI) module to create and manage Windows or Linux virtual desktops

- [Launch a new desktop](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/launch-desktop.html): How to launch a new virtual desktop
- [Access your desktop](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/access-desktop.html): How to access a virtual desktop
- [Control your desktop state](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/control-desktop-state.html): How to control a virtual desktop's state
- [Modify a virtual desktop](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/modify-virtual-desktop.html): How to modify a virtual desktop
- [Retrieve session information](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/retrieve-session-information.html): How to retrieve session information for a virtual desktop

### [Schedule virtual desktops](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/schedule-virtual-desktops.html)

How to set schedules for virtual desktops

- [Setting individual desktop schedules](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/schedule-individual-desktops.html): How to set individual schedules for virtual desktops
- [Setting default schedules](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/setting-default-schedules.html): How to set default schedules for virtual desktops across the entire environment
- [VDI autostop](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/virtual-desktops-autostop.html): How to set up autostop for virtual desktops

### [Shared desktops](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/shared-desktops.html)

How to use shared desktops

- [Share a desktop](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/desktop-sharing.html): How to share a desktop
- [Access a shared desktop](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/access-shared-desktop.html): How to connect to a shared desktop

### [File browser](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/file-browser.html)

How to use File browser to access the global shared EFS filesystem through the web portal.

- [Upload file(s)](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/upload-file.html): How to use File browser to upload files to the global shared EFS filesystem through the web portal.
- [Delete file(s)](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/delete-file.html): How to use File browser to delete files from the global shared EFS filesystem through the web portal.
- [Manage favorites](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/manage-favorites.html): How to use File browser to manage favorite files in the global shared EFS filesystem through the web portal.
- [Edit files](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/edit-files.html): How to use File browser to edit files in the global shared EFS filesystem through the web portal.
- [Transfer files](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/transfer-files.html): How to use external file transfer applications with the File browser for the global shared EFS filesystem.


## [Troubleshooting](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/troubleshooting.html)

- [General Debugging and Monitoring](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/res-troubleshooting-general.html): Information to help with debugging and monitoring.
- [Issue RunBooks](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/res-troubleshooting-issue-runbooks.html): How to troubleshoot known issues.
- [Known Issues](https://docs.aws.amazon.com/res/archive/release-minus-1/ug/res-troubleshooting-known-issues.html): How to troubleshoot known issues.
