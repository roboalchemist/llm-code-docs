# Source: https://docs.aws.amazon.com/systems-manager/latest/userguide/llms.txt

# AWS Systems Manager User Guide

> AWS Systems Manager (formerly Amazon EC2 Systems Manager) is a unified interface that allows you to centralize operational data and automate tasks across your AWS resources. Systems Manager shortens the time to detect and resolve operational problems in your infrastructure. Systems Manager gives you a complete view of your infrastructure performance and configuration, simplifies resource and application management, and allows you to operate and manage your infrastructure at scale.

- [AWS Systems ManagerÂ Change Manager availability change](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-availability-change.html)
- [Related information](https://docs.aws.amazon.com/systems-manager/latest/userguide/related-information.html)
- [Document history](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-release-history.html)
- [Document conventions](https://docs.aws.amazon.com/systems-manager/latest/userguide/docconventions.html)

## [What is AWS Systems Manager?](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)

- [Supported operating systems and machine types](https://docs.aws.amazon.com/systems-manager/latest/userguide/operating-systems-and-machine-types.html): Learn about the operating systems and machine types that are supported by AWS Systems Manager.
- [What is the unified console?](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-unified-console.html): Learn about the unified Systems Manager console.


## [Setting up managed nodes for AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-nodes.html)

### [Managing EC2 instances with Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-ec2.html)

Learn how to set up Systems Manager to configure and manage the EC2 instances in your account.

- [Configure instance permissions required for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-permissions.html): Learn how to configure Amazon EC2 instance permissions for Systems Manager using the Default Host Management Configuration, or an IAM instance profile.
- [Improve the security of EC2 instances by using VPC endpoints for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-create-vpc.html): Discover how to improve the security posture of your managed instances by configuring Systems Manager to use an interface VPC endpoint in Amazon VPC.

### [Managing nodes in hybrid and multicloud environments with Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-hybrid-multicloud.html)

Learn how to set up Systems Manager to configure and manage non-EC2 machines for use in a hybrid and multicloud environment.

- [Create the IAM service role required for Systems Manager in hybrid and multicloud environments](https://docs.aws.amazon.com/systems-manager/latest/userguide/hybrid-multicloud-service-role.html): Learn how to grant AssumeRole trust to the Systems Manager service so that it can communicate with non-EC2 machines in hybrid and multicloud environments.
- [Create a hybrid activation to register nodes with Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/hybrid-activation-managed-nodes.html): Learn how to create a managed-node activation to provide secure access to the Systems Manager service from your managed nodes.
- [Install SSM Agent on hybrid Linux nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/hybrid-multicloud-ssm-agent-install-linux.html): Learn how to install SSM Agent on non-EC2 Linux machines in a hybrid and multicloud environment.
- [Install SSM Agent on hybrid Windows Server nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/hybrid-multicloud-ssm-agent-install-windows.html): Learn how to install SSM Agent on non-EC2 Windows Server machines in a hybrid and multicloud environment.
- [Managing edge devices with Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-edge-devices.html): Learn how to set up AWS Systems Manager to configure and manage edge devices.
- [Creating an AWS Organizations delegated administrator for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setting_up_delegated_admin.html): Learn how to set up a delegated administrator for Systems Manager.


## [Setting up AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-console.html)

- [Setting up Systems Manager console access](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-console-access.html): Permissions and policy setup steps that are required to grant Systems Manager console access.
- [Setting up Systems Manager unified console for an organization](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-organizations.html): Learn how to set up the Systems Manager unified console experience from the AWS Management Console with just a few clicks.
- [Setting up Systems Manager unified console for a single account and Region](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-single-account-region.html): Discover how to set up the Systems Manager unified console experience for a single AWS account and AWS Region.
- [Disabling the Systems Manager unified console](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-disable-integrated-console.html): Learn how to disable the unified console experience and return to the classic Systems Manager console interface.


## [Performing node management tasks](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-node-tasks.html)

### [Reviewing node insights](https://docs.aws.amazon.com/systems-manager/latest/userguide/review-node-insights.html)

Learn how to review the overall status of managed nodes and unmanaged Amazon Elastic Compute Cloud (Amazon EC2) instances in your organization or account.

- [Adding or removing widgets](https://docs.aws.amazon.com/systems-manager/latest/userguide/review-node-insights-add-and-remove-widgets.html): Learn how to customize the layout of the Systems Manager Review node insights page by adding and removing widgets.
- [Rearranging widgets](https://docs.aws.amazon.com/systems-manager/latest/userguide/review-node-insights-rearrange-widgets.html): Learn how to customize layout in the Systems Manager Review node insights page by dragging and dropping widgets.

### [Exploring nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/view-aggregated-node-details.html)

Learn how review aggregated details about managed nodes in your organization or account Systems Manager.

### [Exploring nodes using console filters](https://docs.aws.amazon.com/systems-manager/latest/userguide/view-aggregated-node-details-console.html)

Learn how to view lists of managed nodes in your account or organziation organized according to the filter views in Systems Manager.

- [Choosing a filter view for managed node summaries](https://docs.aws.amazon.com/systems-manager/latest/userguide/explore-nodes-filter-view.html): Learn how to view aggregated data about managed nodes in your organization or account according to specific filter selections.

### [Exploring nodes using text prompts in Amazon Q](https://docs.aws.amazon.com/systems-manager/latest/userguide/view-aggregated-node-details-Q.html)

Learn how to view information about managed nodes and instances in Systems Manager by entering natural language prompts in Amazon Q.

- [Learning to craft effective prompts to ask Amazon Q about your fleet](https://docs.aws.amazon.com/systems-manager/latest/userguide/view-aggregated-node-details-Q-prompts.html): Learn how to create questions for Amazon Q that will yield the most accurate and complete results about servers in your fleet.
- [Exploring managed nodes using Amazon Q](https://docs.aws.amazon.com/systems-manager/latest/userguide/explore-managed-nodes-using-Q.html): Learn how to ask Amazon Q questions about managed nodes and instances in your Systems Manager fleet.
- [Viewing individual node details and taking action on a node](https://docs.aws.amazon.com/systems-manager/latest/userguide/node-detail-actions.html): Learn how to view details about a managed node in Systems Manager and perform a variety of actions on the node from the node details page.

### [Downloading or exporting a managed node report](https://docs.aws.amazon.com/systems-manager/latest/userguide/explore-nodes-download-report.html)

Learn how to download a filtered or unfiltered list of nodes managed by Systems Manager in your AWS organization or account.

- [Creating a custom service role to export diagnosis reports to S3](https://docs.aws.amazon.com/systems-manager/latest/userguide/create-s3-export-role.html): Learn how to create a custom service role for exporting managed node reports from Systems Manager to Amazon S3.
- [Managing node report content and appearance](https://docs.aws.amazon.com/systems-manager/latest/userguide/explore-nodes-manage-report-display.html): Learn how to customize reports about managed nodes in your AWS organization or account by showing or hiding available columns for the report and configuring console display options.

### [Just-in-time node access using Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access.html)

Improve security by providing temporary, time-bound access to nodes only when needed, eliminating the need for long-standing permissions.

### [Setting up just-in-time access with Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access-setting-up.html)

Learn how to configure just-in-time access to provide temporary, secure access to managed nodes.

### [Create approval policies for your nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access-approval-policies.html)

Learn how to define approval policies to control access requests for managed nodes.

- [Create manual approval policies for just-in-time node access](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access-create-manual-policies.html): Learn how to set up manual approval workflows for just-in-time node access requests.
- [Statement structure and built-in operators for auto-approval and deny-access policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/auto-approval-deny-access-policy-statement-structure.html): Learn about the structure and schema of just-in-time node access auto-approval and deny-access policies, as well as the built-in operators for statements.
- [Create an auto-approval policy for just-in-time node access](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access-create-auto-approval-policies.html): Learn how to configure automatic approval rules for just-in-time node access based on conditions.
- [Create a deny-access policy for just-in-time node access](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access-create-deny-access-policies.html): Learn how to create policies that automatically deny specific just-in-time access requests.
- [Create approval policies for just-in-time node access with Amazon Q](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access-create-approval-policies-q-ide-cli.html): Learn how to configure approval policies using Amazon Q for just-in-time node access management.
- [Update just-in-time node access session preferences](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access-session-preferences.html): Learn how to modify session settings and preferences for just-in-time node access.
- [Configure notifications for just-in-time access requests](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access-notifications.html): Learn how to set up notifications to alert administrators about just-in-time access requests.
- [Recording RDP connections](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access-rdp-recording.html): Learn how to enable and configure recording of RDP connections for audit and compliance purposes.
- [Modifying targets](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access-modify-targets.html): Learn how to update and modify target configurations for just-in-time access policies.
- [Changing identity providers](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access-change-identity-provider.html): Learn how to switch or update identity providers for just-in-time access authentication.
- [Start a just-in-time node access session](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access-start-session.html): Learn how to initiate a just-in-time access session to connect to managed nodes.

### [Managing just-in-time access requests](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access-manage-requests.html)

Learn how to review, approve, and manage pending just-in-time access requests.

- [Approving and denying just-in-time node access requests](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access-approve-deny-requests.html): Learn how to process just-in-time access requests by approving or denying them.
- [Moving to just-in-time node access from Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access-moving-from-session-manager.html): Learn how to migrate from Session Manager to just-in-time node access for improved security.
- [Disabling just-in-time access with Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access-disable.html): Learn how to turn off just-in-time access functionality in your Systems Manager environment.
- [FAQ](https://docs.aws.amazon.com/systems-manager/latest/userguide/just-in-time-node-access-faq.html): Discover answers to common questions about just-in-time node access.

### [Diagnosing and remediating](https://docs.aws.amazon.com/systems-manager/latest/userguide/diagnose-and-remediate.html)

Learn how to identify problems across your fleet in a single diagnosis operation, and then attempt remediation on all affected accounts in a single Automation operation.

- [Diagnosing and remediating failed deployments](https://docs.aws.amazon.com/systems-manager/latest/userguide/remediating-deployment-issues.html): Learn how to identify and resolve deployment failures using Systems Manager diagnostic tools and remediation strategies.
- [Diagnosing and remediating drifted configurations](https://docs.aws.amazon.com/systems-manager/latest/userguide/remediating-configuration-drift.html): Learn how to use the unified Systems Manager console to diagnose and remediate certain types of drifted configurations in your AWS environment.

### [Diagnosing and remediating unmanaged Amazon EC2 instances](https://docs.aws.amazon.com/systems-manager/latest/userguide/remediating-unmanaged-instances.html)

Learn how now use the unified Systems Manager console to identify which EC2 instances in your account aren't currently managed by Systems Manager, identify any issues that are preventing Systems Manager from managing the instances, and perform automatic or manual remediations.

- [Categories of diagnosable unmanaged EC2 instance issues](https://docs.aws.amazon.com/systems-manager/latest/userguide/diagnosing-ec2-category-types.html): Learn about the types of issuesânetwork, security group, and DNSâthat can prevent Systems Manager from taking over management of your EC2 instances.
- [Running a diagnosis and optional remediation for unmanaged EC2 instances](https://docs.aws.amazon.com/systems-manager/latest/userguide/running-diagnosis-execution-ec2.html): Learn how to diagnose the network-related and VPC-related issues that might be preventing Systems Manager from managing your EC2 instances.
- [Scheduling a recurring scan for unmanaged EC2 instances](https://docs.aws.amazon.com/systems-manager/latest/userguide/schedule-recurring-ec2-diagnosis.html): Learn how to configure Systems Manager to scan for unmanaged EC2 instances in your account or organization on a regular schedule.
- [Remediation impact types of runbook actions](https://docs.aws.amazon.com/systems-manager/latest/userguide/remediation-impact-type.html): Learn about the three types of impacts Systems Manager can report on as the result of an execution preview operation.
- [Viewing execution history details for remediations](https://docs.aws.amazon.com/systems-manager/latest/userguide/diagnose-and-remediate-execution-history.html): Learn how to view a history of all in-progress and completed remediation operations made using the Diagnose and remediate feature in Systems Manager.and

### [Adjusting Systems Manager settings](https://docs.aws.amazon.com/systems-manager/latest/userguide/settings-overview.html)

Change settings for AWS Systems Manager.

### [Working with Amazon S3 buckets and bucket policies for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-diagnosis-metadata-bucket.html)

Learn about the Amazon S3 bucket created during the unified Systems Manager console onboarding process.

- [Changing to an AWS KMS customer managed key to encrypt S3 resources](https://docs.aws.amazon.com/systems-manager/latest/userguide/remediate-s3-bucket-encryption.html): Learn how to user your own customer managed key (CMK) as an alternative to Amazon S3 managed keys for storing results of Systems Manager remediation operations.
- [S3 bucket policies for the unified Systems Manager console](https://docs.aws.amazon.com/systems-manager/latest/userguide/remediate-s3-bucket-policies.html): Review the bucket policies that are created when an organization or single account onboard to the unified Systems Manager console.


## [Using AWS Systems Manager tools](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-tools.html)

- [Perform a node task with Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-launch-managed-instance.html): Learn how to launch an Amazon EC2 instance managed by Systems Manager, and use various Systems Manager tools.

### [Node tools](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-instances-and-nodes.html)

Manage Amazon Elastic Compute Cloud (Amazon EC2) instances and other machine types in a hybrid and multicloud environment, as well as other types of AWS resources, using Systems Manager.

### [Compliance](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-compliance.html)

Scan your fleet of managed nodes for patch compliance and configuration inconsistencies.

- [Getting started with Compliance](https://docs.aws.amazon.com/systems-manager/latest/userguide/compliance-prerequisites.html): Complete these tasks to get started with Compliance.
- [Configuring permissions for Compliance](https://docs.aws.amazon.com/systems-manager/latest/userguide/compliance-permissions.html): Learn how to set up the required permissions and roles to use Systems Manager Compliance effectively.
- [Creating a resource data sync for Compliance](https://docs.aws.amazon.com/systems-manager/latest/userguide/compliance-datasync-create.html): Send compliance data from managed nodes to an S3 bucket and then use services like Athena and Quick to query and analyze it.
- [Learn details about Compliance](https://docs.aws.amazon.com/systems-manager/latest/userguide/compliance-about.html): View Systems Manager compliance data about the status of Patch Manager patching, State Manager associations, and custom compliance types.
- [Deleting a resource data sync for Compliance](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-compliance-delete-RDS.html): Delete an AWS Systems Manager Compliance resource data sync
- [Remediating compliance issues using EventBridge](https://docs.aws.amazon.com/systems-manager/latest/userguide/compliance-fixing.html): Configure Amazon EventBridge to respond to Compliance events.
- [Assign custom compliance metadata using the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/compliance-custom-metadata-cli.html): Use the PutComplianceItems API operation to assign custom compliance metadata to a resource or to a managed node.

### [Distributor](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html)

Learn how to create, manage, and deploy software packages on managed nodes using Distributor, a tool in AWS Systems Manager.

- [Setting up Distributor](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor-getting-started.html): Discover how to set up Distributor by completing prerequisites, creating an IAM instance profile with Distributor permissions, controlling access to packages, and creating an Amazon S3 bucket.

### [Working with Distributor packages](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor-working-with.html)

Learn how to create package manifests, and create, deploy, and manage packages in Distributor, a tool in AWS Systems Manager.

- [View packages](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor-view-packages.html): Discover how to view packages in Distributor, a tool in AWS Systems Manager, that are available for installation using your preferred command line tool.
- [Create a package](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor-working-with-packages-create.html): Learn how to create a package in Distributor, a tool in AWS Systems Manager, using the simple or advanced package creation workflow.
- [Edit package permissions](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor-working-with-packages-ep.html): Learn how to edit a Distributor package's permissions in the AWS Systems Manager console in order to add other AWS accounts to a package's permissions.
- [Edit package tags](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor-working-with-packages-tags.html): Learn how how edit a Distributor package's tags in the AWS Systems Manager console to help you group and filter packages by criteria that are relevant to your organization.
- [Add a package version](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor-working-with-packages-version.html): Learn how to add package versions to replace installable files attached to the current version in Distributor, a tool in AWS Systems Manager, and to add installable files, or delete files.
- [Install or update packages](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor-working-with-packages-deploy.html): Learn how to deploy packages to managed nodes by using Distributor, a tool in AWS Systems Manager.
- [Uninstall a package](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor-working-with-packages-uninstall.html): Learn how to uninstall Distributor packages from your AWS Systems Manager managed nodes by using Run Command from the AWS Management Console or the AWS CLI.
- [Delete a package](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor-working-with-packages-dpkg.html): Learn how to delete a package and all its versions from Distributor, a tool in AWS Systems Manager.
- [Auditing and logging Distributor activity](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor-logging-auditing.html): Learn how to audit and log activity in Distributor, a tool in AWS Systems Manager.
- [Troubleshooting Distributor](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor-troubleshooting.html): Discover how to troubleshoot issues in Distributor, a tool in AWS Systems Manager.

### [Fleet Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager.html)

Remotely manage, view status, and troubleshoot AWS or on-premises managed nodes using Fleet Manager, a tool in AWS Systems Manager.

### [Setting up Fleet Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setting-up-fleet-manager.html)

Learn how to complete the setup steps for Fleet Manager, a tool in AWS Systems Manager, to monitor and manage your managed nodes.

- [Controlling access to Fleet Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/configuring-fleet-manager-permissions.html): Learn how to create an IAM policy that provides access to all features in Fleet Manager, a tool in AWS Systems Manager, and to modify your policy to grant access to the features you choose.

### [Working with managed nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-managed-nodes.html)

Discover how to configure EC2 instances; AWS IoT Greengrass core devices; and on-premises servers, edge devices, and VMs in a hybrid and multicloud environment as managed nodes in Fleet Manager, a tool in AWS Systems Manager.

### [Configuring instance tiers](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-configure-instance-tiers.html)

Learn how to differentiate in Fleet Manager, a tool in AWS Systems Manager, between standard-instances tier and advanced-instances tier for managed nodes in a hybrid and multicloud environment.

- [Turning on the advanced-instances tier](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-enable-advanced-instances-tier.html): Learn now to configure your hybrid and multicloud environment in Fleet Manager, a tool in AWS Systems Manager, to use the advanced-instances tier using the Systems Manager console, AWS CLI, or Tools for Windows PowerShell.
- [Reverting from the advanced-instances tier to the standard-instances tier](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-revert-to-standard-tier.html): Learn how to change managed nodes running in the advanced-instances tier back to the standard-instances tier in Fleet Manager, a tool in AWS Systems Manager.
- [Resetting passwords on managed nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-reset-password.html): Learn how to reset the password for any user on a managed node in Fleet Manager, a tool in AWS Systems Manager.
- [Deregistering managed nodes in a hybrid and multicloud environment](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-deregister-hybrid-nodes.html): Learn how to deregister non-EC2 machines in Fleet Manager, a tool in AWS Systems Manager, that you no longer want to manage using Systems Manager.

### [Working with OS file systems](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-file-system-management.html)

Learn how to work with the file system on a managed node using Fleet Manager, a tool in AWS Systems Manager.

- [Viewing the OS file system](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-viewing-file-system.html): Learn how to view the file system on a managed node using Fleet Manager, a tool in AWS Systems Manager.
- [Previewing OS files](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-preview-os-files.html): Learn how to preview text files on an OS Fleet Manager, a tool in AWS Systems Manager.
- [Tailing OS file](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-tailing-os-files.html): Learn how to tail a file on a managed node using Fleet Manager, a tool in AWS Systems Manager.
- [Copying, cutting, and pasting OS files or directories](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-move-files-or-directories.html): Learn how to copy, cut, and paste files on a managed node using Fleet Manager, a tool in AWS Systems Manager.
- [Renaming OS files and directories](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-renaming-files-and-directories.html): Learn how to rename files and directories on a managed node using Fleet Manager, a tool in AWS Systems Manager.
- [Deleting OS files and directories](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-deleting-files-and-directories.html): Learn how to delete files and directories on a managed node using Fleet Manager, a tool in AWS Systems Manager.
- [Creating OS directories](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-creating-directories.html): Learn how to create directories on a managed node using Fleet Manager, a tool in AWS Systems Manager.
- [Cutting, copying, and pasting OS directories](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-managing-directories.html): Learn how to cut, copy, and paste directories on a managed node using Fleet Manager, a tool in AWS Systems Manager.
- [Monitoring performance](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-monitoring-node-performance.html): Learn how to view managed node performance data using Fleet Manager, a tool in AWS Systems Manager.

### [Working with processes](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-manage-processes.html)

Discover how to work with processes running on your managed nodes using Fleet Manager, a tool in AWS Systems Manager.

- [Viewing details about OS processes](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-view-process-details.html): Learn how to view details about OS processes using Fleet Manager, a tool in AWS Systems Manager.
- [Starting an OS process on a managed node](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-start-process.html): Learn how to start a process on a managed node using Fleet Manager, a tool in AWS Systems Manager.
- [Terminating an OS process](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-terminate-process.html): Learn how to terminate a process on a managed node using Fleet Manager, a tool in AWS Systems Manager.
- [Viewing logs](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-view-node-logs.html): Learn how to view log data stored on your managed nodes using Fleet Manager, a tool in AWS Systems Manager.

### [Managing OS user accounts and groups](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-manage-os-user-accounts.html)

Discover how to manage operating system user accounts and groups on managed nodes using Fleet Manager, a tool in AWS Systems Manager.

- [Creating an OS user or group using Fleet Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/manage-os-user-accounts-create.html): Discover how to create user accounts and groups on managed nodes using Fleet Manager, a tool in AWS Systems Manager.
- [Updating user or group membership using Fleet Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/manage-os-user-accounts-update.html): Discover how to update user accounts and groups on managed nodes using Fleet Manager, a tool in AWS Systems Manager.
- [Deleting an OS user or group using Fleet Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/manage-os-user-accounts-delete.html): Discover how to delete user accounts and groups on managed nodes using Fleet Manager, a tool in AWS Systems Manager.
- [Managing the Windows registry](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-manage-windows-registry.html): Learn how to manage the Windows registry on managed nodes using Fleet Manager, a tool in AWS Systems Manager.
- [Managing EC2 instances automatically with Default Host Management Configuration](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-default-host-management-configuration.html): Learn how to use Default Host Management Configuration to automatically track Amazon EC2 instances using Fleet Manager, how to use Run Command on remote instances, and how to securely connect to the instances using Session Manager.
- [Connecting to a managed instance using Remote Desktop](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-remote-desktop-connections.html): Learn how to connect to Windows Server managed Amazon EC2 instances over RDP using Fleet Manager, a tool in AWS Systems Manager.
- [Managing Amazon EBS volumes](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-manage-amazon-ebs-volumes.html): Learn how to manage EBS volumes on Amazon EC2 managed instances using Fleet Manager, a tool in AWS Systems Manager.
- [Accessing the Red Hat Knowledge base portal](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-red-hat-knowledge-base-access.html): Learn how to access the Red Hat Knowledge base portal through Fleet Manager, a tool in AWS Systems Manager.

### [Troubleshooting managed node availability](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-troubleshooting-managed-nodes.html)

Learn how to diagnose why a managed node that you have confirmed is running isn't included in your lists of managed nodes in Systems Manager.

- [Troubleshooting managed node availability using ssm-cli](https://docs.aws.amazon.com/systems-manager/latest/userguide/troubleshooting-managed-nodes-using-ssm-cli.html): Use the ssm-cli to diagnose why a machine that you have confirmed is running isn't included in your lists of managed nodes in Systems Manager.
- [Hybrid Activations](https://docs.aws.amazon.com/systems-manager/latest/userguide/activations.html): Configure and manage non-EC2 nodes for hybrid and multicloud environments by using Systems Manager hybrid activations.

### [Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html)

Collect metadata about the operating system and applications running on your managed nodes using Systems Manager Inventory.

### [Learn more about Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-about.html)

Specify the type of metadata to collect, the nodes from where to collect the metadata, and a schedule for metadata collection.

- [Metadata collected by Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-schema.html): View the complete list of metadata collected by each Inventory plugin.
- [Working with file and Windows registry inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-file-and-registry.html): Search and inventory files on Windows Server, Linux, and macOS operating systems.

### [Setting up Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory-setting-up.html)

Information about how to set up AWS Systems Manager Inventory.

- [Creating a resource data sync for Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-create-resource-data-sync.html): Set up and configure resource data sync for Systems Manager Inventory.
- [Using EventBridge to monitor Inventory events](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory-setting-up-eventbridge.html): Monitor Systems Manager Inventory events using Amazon EventBridge.
- [Configuring inventory collection](https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-collection.html): Configure inventory collection on one or more managed nodes by using the Systems Manager console.
- [Querying inventory data from multiple Regions and accounts](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory-query.html): Query inventory data from multiple AWS Regions and AWS accounts by integrating AWS Systems Manager Inventory with Amazon Athena.
- [Querying an inventory collection by using filters](https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-query-filters.html): Use the filter tools in AWS Systems Manager to query a list of managed nodes that meet certain criteria.
- [Aggregating inventory data](https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-aggregate.html): View aggregated counts of AWS Systems Manager Inventory data by using the AWS CLI.
- [Working with custom inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-custom.html): Assign any metadata you want to your nodes by creating AWS Systems Manager Inventory custom inventory.
- [Viewing inventory history and change tracking](https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-history.html): View AWS Systems Manager Inventory history and change tracking for all of your managed nodes by using AWS Config.
- [Stopping data collection and deleting inventory data](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory-delete.html): Stop AWS Systems Manager Inventory data collection and delete data.
- [Assigning custom inventory metadata to a managed node](https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-custom-metadata.html): Use the AWS Systems Manager PutInventory API operation to assign custom inventory metadata to a managed node.
- [Using the AWS CLI to configure inventory data collection](https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-collection-cli.html): Configure AWS Systems Manager Inventory to collect metadata from your managed nodes.
- [Walkthrough: Using resource data sync to aggregate inventory data](https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-resource-data-sync.html): Create a resource data sync configuration to automatically port inventory data from all of your managed nodes to a central Amazon S3 bucket.
- [Troubleshooting Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/syman-inventory-troubleshooting.html): Troubleshoot common errors or problems with AWS Systems Manager Inventory.

### [Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html)

Discover how to use Patch Manager, a tool in AWS Systems Manager, to automate the process of patching managed nodes with both security-related updates and other types of updates for operating systems and applications.

- [Patch policy configurations in Quick Setup](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-policies.html): Learn about Quick Setup patch policies for Patch Manager, both tools in AWS Systems Manager, which provide extensive, centralized control over your patching operations across multiple AWS accounts and Regions.
- [Patch Manager prerequisites](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-prerequisites.html): Learn how to ensure that your environment meets the prerequisites for Patch Manager, a tool in AWS Systems Manager.

### [How Patch Manager operations work](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-patching-operations.html)

Learn how Patch Manager, a tool in AWS Systems Manager, determines which patches to install and how it installs them on each supported operating system.

- [How package release dates and update dates are calculated](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-release-dates.html): Learn how package release dates are calculated for Amazon Linux 2 and Amazon Linux 2023 Amazon EC2 instances in Patch Manager, a tool in AWS Systems Manager, and how these dates can affect Patch Manager auto-approval operations.
- [How security patches are selected](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-selecting-patches.html): Learn how to install a smaller set of patches focused on operating system security-related updates on managed nodes in Patch Manager, a tool in AWS Systems Manager.
- [How to specify an alternative patch source repository (Linux)](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-alternative-source-repository.html): Learn how to install patches that aren't related to security or that are in a different source repository than the default one configured on a managed node in Patch Manager, a tool in AWS Systems Manager.
- [How patches are installed](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-installing-patches.html): Learn how to install patches on different types of operating systems using Patch Manager, a tool in AWS Systems Manager.
- [How patch baseline rules work on Linux-based systems](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-linux-rules.html): Discover how to use native package managers to install patches approved by the a patch baseline in Patch Manager, a tool in AWS Systems Manager, for different Linux distributions.
- [Patching operation differences between Linux and Windows Server](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-windows-and-linux-differences.html): Learn the important differences between Linux and Windows Server patching in Patch Manager, a tool in AWS Systems Manager.

### [SSM Command documents for patching managed nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-ssm-documents.html)

Use SSM documents with Patch Manager, a tool in AWS Systems Manager, to keep your managed nodes patched with the latest security-related updates.

- [AWS-RunPatchBaseline](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-aws-runpatchbaseline.html): Learn how to perform patching operations on managed nodes for both security-related and other types of updates in Patch Manager, a tool in AWS Systems Manager.
- [AWS-RunPatchBaselineAssociation](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-aws-runpatchbaselineassociation.html): Discover how to perform patching operations on instances for security-related and other types of updates in Patch Manager, a tool in AWS Systems Manager, and to apply patches for both operating systems and applications.
- [AWS-RunPatchBaselineWithHooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-aws-runpatchbaselinewithhooks.html): Discover how to perform patching operations on managed nodes for both security-related and other types of updates using optional hooks in Patch Manager, a tool in AWS Systems Manager.
- [Sample scenario for using the InstallOverrideList parameter](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-override-lists.html): Discover to to override the patches specified by the current default patch baseline in Patch Manager, a tool in AWS Systems Manager.
- [Using the BaselineOverride parameter](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-baselineoverride-parameter.html): Discover how to define patching preferences at runtime using the patch baseline override in Patch Manager, a tool in AWS Systems Manager.

### [Patch baselines](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-patch-baselines.html)

Learn how to patch managed nodes on a schedule and patch managed nodes on demand in Patch Manager, a tool in AWS Systems Manager.

- [Predefined and custom patch baselines](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-predefined-and-custom-patch-baselines.html): Learn how to define which patches are installed on your managed nodes by Patch Manager, a tool in AWS Systems Manager, and to create rules to specify that certain types of updates should be automatically approved.
- [Package name formats for approved and rejected patch lists](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html): Learn how to add specific formats of package names to approved and rejected patch lists in Patch Manager, a tool in AWS Systems Manager, depending on the type of operating system you're patching.
- [Patch groups](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-patch-groups.html): Learn how to use a patch group in Patch Manager, a tool in AWS Systems Manager, to associate managed nodes with a specific patch baseline to help with various deployment tasks.
- [Patching applications released by Microsoft on Windows Server](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-patching-windows-applications.html): Learn how to update applications released by Microsoft on Windows Server using Patch Manager, a tool in AWS Systems Manager.

### [Using Kernel Live Patching on Amazon Linux 2 managed nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-kernel-live-patching.html)

Discover how to use Patch Manager, a tool in AWS Systems Manager, to apply security vulnerability and critical bug patches to a running Linux kernel without reboots or disruptions to running applications.

- [Turning on Kernel Live Patching](https://docs.aws.amazon.com/systems-manager/latest/userguide/enable-klp.html): Learn how to turn on Kernel Live Patching using Run Command, a tool in AWS Systems Manager.
- [Applying kernel live patches](https://docs.aws.amazon.com/systems-manager/latest/userguide/install-klp.html): Learn how to apply kernel live patches using Run Command, a tool in AWS Systems Manager.
- [Turning off Kernel Live Patching](https://docs.aws.amazon.com/systems-manager/latest/userguide/disable-klp.html): Learn how to turn off Kernel Live Patching using Run Command, a tool in AWS Systems Manager.

### [Working with Patch Manager resources and compliance using the console](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-console.html)

Learn how to ensure that you have completed the required tasks to use Patch Manager, a tool in AWS Systems Manager.

- [Creating a patch policy](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-create-a-patch-policy.html): Learn how to create a patch policy in Patch Manager, a tool in AWS Systems Manager, to automate patching of applications and nodes in your AWS account or organization.
- [Viewing patch Dashboard summaries](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-view-dashboard-summaries.html): Learn how to view patch summary data on the Dashnoard in Patch Manager, a tool in AWS Systems Manager.

### [Patch compliance reports](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-compliance-reports.html)

Learn how to view and use patch compliance reports in Patch Manager, a tool in AWS Systems Manager.

- [Viewing patch compliance results](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-view-compliance-results.html): Learn how to view compliance information about patching operations in Patch Manager, a tool in AWS Systems Manager, that use the AWS-RunPatchBaseline document on your managed nodes.
- [Generating .csv patch compliance reports](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-store-compliance-results-in-s3.html): Learn how to generate and save Patch Manager patch compliance reports in .csv format to an Amazon S3 bucket.

### [Remediating noncompliant managed nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-noncompliant-nodes.html)

Learn how to identify managed nodes that are out of patch compliance in Patch Manager, a tool in AWS Systems Manager, and bring them into compliance.

- [Identifying noncompliant managed nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-find-noncompliant-nodes.html): Learn how to identify noncompliant managed nodes by running an SSM document for Patch Manager, a tool in AWS Systems Manager.
- [Patch compliance state values](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-compliance-states.html): Learn how to identify why a managed node might be out of patch compliance by using the state or status of each individual patch in Patch Manager, a tool in AWS Systems Manager.
- [Patching noncompliant managed nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-compliance-remediation.html): Learn how to make managed nodes comply with the patch rules that apply to them by using the same tools and processes used to check nodes for patch compliance in Patch Manager, a tool in AWS Systems Manager.
- [Identifying the execution that created patch compliance data](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-compliance-data-overwrites.html): Learn how to identify which execution created patch compliance data and avoid unintended overwrites of patch compliance data in Patch Manager, a tool in AWS Systems Manager.
- [Patching managed nodes on demand](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-patch-now-on-demand.html): Learn how to run on-demand patching operations from the Systems Manager console by using the Patch now option in Patch Manager, a tool in AWS Systems Manager.

### [Patch baselines](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-create-a-patch-baseline.html)

Discover how to use patch baselines in Patch Manager, a tool in AWS Systems Manager, to define which patches are approved for installation on your managed nodes.

- [Viewing AWS predefined patch baselines](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-view-predefined-patch-baselines.html): Learn how to use a predefined patch baseline for each operating system supported by Patch Manager, a tool in AWS Systems Manager.

### [Custom patch baselines](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-manage-patch-baselines.html)

Discover how to create, update, and delete your own custom patch baselines in Patch Manager, a tool in AWS Systems Manager.

- [Creating a custom patch baseline for Linux](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-create-a-patch-baseline-for-linux.html): Learn how to create a custom patch baseline for Linux managed nodes in Patch Manager, a tool in AWS Systems Manager.
- [Creating a custom patch baseline for macOS](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-create-a-patch-baseline-for-macos.html): Learn how to create a custom patch baseline for macOS managed nodes in Patch Manager, a tool in AWS Systems Manager.
- [Creating a custom patch baseline for Windows Server](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-create-a-patch-baseline-for-windows.html): Learn how to create a custom patch baseline for Windows Server managed nodes in Patch Manager, a tool in AWS Systems Manager.
- [Updating or deleting a custom patch baseline](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-update-or-delete-a-patch-baseline.html): Learn how to update or delete a custom patch baseline that you have created in Patch Manager, a tool in AWS Systems Manager, and to update its name or description, approval and exception rules, and tags.
- [Setting an existing patch baseline as the default](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-default-patch-baseline.html): Learn how to set a baseline as the default for the associated operating system type upon creation in Patch Manager, a tool in AWS Systems Manager, or set an existing patch baseline as the default for an OS type.
- [Viewing available patches](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-view-available-patches.html): Learn how to view all available patches for a specified operating system in Patch Manager and, optionally, a specific operating system version.
- [Creating and managing patch groups](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-tag-a-patch-group.html): Learn how to organize your patching efforts by adding managed nodes to patch groups by using tags in Patch Manager, a tool in AWS Systems Manager.
- [Integrating Patch Manager with AWS Security Hub CSPM](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-security-hub-integration.html): Learn how to use the integration support between Patch Manager, a tool in AWS Systems Manager, Security Hub CSPM.
- [Working with Patch Manager resources using theÂ AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-cli-commands.html): Learn how to perform configuration tasks for Patch Manager, a tool in AWS Systems Manager, using the AWS CLI.

### [Patch Manager tutorials](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-tutorials.html)

Discover how to use Patch Manager, a tool in AWS Systems Manager, in a variety of patching scenarios.

- [Tutorial: Patching a server in an IPv6 only environment](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-server-patching-iPv6-tutorial.html): Discover how to patch a server in an IPv6-only environment using Systems Manager Patch Manager.
- [Tutorial: Create a patch baseline for installing Windows Service Packs using the console](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-windows-service-pack-patch-baseline-tutorial.html): Discover how to specify that all, some, or only one type of supported patch is installed when you create a custom patch baseline in Patch Manager, a tool in AWS Systems Manager.
- [Tutorial: Update application dependencies, patch a managed node, and perform an application-specific health check using the console](https://docs.aws.amazon.com/systems-manager/latest/userguide/aws-runpatchbaselinewithhooks-tutorial.html): Discover how to use Patch Manager, a tool in AWS Systems Manager, and the SSM document AWS-RunPatchBaselineWithHooks to update application dependencies, patch a managed node, and perform an application-specific health check.
- [Tutorial: Patch a server environment using the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-patch-servers-using-the-aws-cli.html): Discover how to patch a server environment by using Patch Manager, a tool in AWS Systems Manager, with a custom patch baseline, patch groups, and a maintenance window.
- [Troubleshooting Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-troubleshooting.html): Discover troubleshooting tips for Patch Manager, a tool in AWS Systems Manager.

### [Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html)

Remotely manage the configuration of your EC2 instances, edge devices, and on-premises servers and VMs by using Systems Manager Run Command.

- [Setting up Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command-setting-up.html): Configure an IAM policy for users who run commands.

### [Running commands on managed nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/running-commands.html)

Learn how to run commands on managed nodes using Systems Manager Run Command.

- [Running commands from the console](https://docs.aws.amazon.com/systems-manager/latest/userguide/running-commands-console.html): Use Run Command from the AWS Management Console to configure managed nodes without having to log into them.
- [Running commands using a specific document version](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command-version.html): Use the document version parameter to specify which version of a Systems Manager document to use when a command runs.
- [Run commands at scale](https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html): Run commands at scale using targets and rate controls.
- [Canceling a command](https://docs.aws.amazon.com/systems-manager/latest/userguide/cancel-run-command.html): Attempt to cancel a command as long as the service shows that it's in either a Pending or Executing state.

### [Using exit codes in commands](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command-handle-exit-status.html)

Manage how commands are handled by using exit codes.

- [Handling reboots when running commands](https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-reboot.html): Learn how to handle reboots when running commands using Systems Manager Run Command.
- [Understanding command statuses](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html): Monitor run command statuses about the different states a command experiences during processing and for each managed node that processed the command.

### [Run Command walkthroughs](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command-walkthroughs.html)

Run commands with Run Command by using either the AWS CLI or the Tools for Windows PowerShell.

- [Updating software using Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command-tutorial-update-software.html): Run commands with Run Command by using either the AWS CLI or the Tools for Windows PowerShell.
- [Use the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/walkthrough-cli.html): Use the AWS CLI to view information about commands and command parameters, how to run commands, and how to view the status of those commands.
- [Use the Tools for Windows PowerShell](https://docs.aws.amazon.com/systems-manager/latest/userguide/walkthrough-powershell.html): Use the Tools for Windows PowerShell to view information about commands and command parameters, run commands, and view the status of those commands.
- [Troubleshooting Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/troubleshooting-remote-commands.html): Troubleshoot problems with Run Command.

### [Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)

Manage your nodes using a secure one-click browser-based interactive shell or the AWS CLI without having to open inbound ports.

### [Setting up Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started.html)

Set up Session Manager to connect to the managed nodes in your account.

- [Step 1: Complete Session Manager prerequisites](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-prerequisites.html): Ensure your environment meets the requirements for using Session Manager.

### [Step 2: Verify or add instance permissions for Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started-instance-profile.html)

Verify or add the permissions required for you to connect to your instances using Session Manager.

- [Add Session Manager permissions to an existing IAM role](https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-add-permissions-to-existing-profile.html): Embed Session Manager permissions in an existing IAM role that doesn't rely on the default policy for instance permissions.
- [Create a custom IAM role for Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-create-iam-instance-profile.html): Create a custom IAM role that provides permissions for only Session Manager actions on your instances.

### [Step 3: Control session access to managed nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started-restrict-access.html)

Use IAM policies to control which managed nodes specific users or groups can connect to and what Session Manager API operations they can perform on them.

- [Start a default shell session](https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-default-session-document.html): Learn how to configure IAM policies to specify default session documents for shell sessions.
- [Start a session with a document](https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-specify-session-document.html): Learn how to use IAM policies to control which session documents users can access.
- [Sample IAM policies for Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-restrict-access-quickstart.html): Create IAM policies that provide the most commonly needed permissions for Session Manager access using samples.
- [Additional sample IAM policies for Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-restrict-access-examples.html): Create a custom IAM policy for any Session Manager user access scenarios you want to support.

### [Step 4: Configure session preferences](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started-configure-preferences.html)

Configure IAM user permissions for Session Manager.

- [Grant or deny a user permissions to update Session Manager preferences](https://docs.aws.amazon.com/systems-manager/latest/userguide/preference-setting-permissions.html): Grant the necessary permissions for users to access and update SSM documents containing account preferences for sessions.
- [Specify an idle session timeout value](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-preferences-timeout.html): Specify the amount of time a user can be inactive before a session ends.
- [Specify maximum session duration](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-preferences-max-timeout.html): Specify the maximum duration of a session before it ends.
- [Allow configurable shell profiles](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-preferences-shell-config.html): Allow configurable shell profiles to customize preferences within sessions.
- [Turn on Run As support for Linux and macOS managed nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-preferences-run-as.html): Launch sessions using the credentials of an operating system user account instead of using the credentials of a system-generated ssm-user account.
- [Turn on KMS key encryption of session data (console)](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-preferences-enable-encryption.html): Use AWS KMS to create and manage keys.
- [Create a Session Manager preferences document (command line)](https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-create-preferences-cli.html): Create preferences to encrypt your session data and specify options for logging it in an Amazon S3 bucket or CloudWatch Logs log group.
- [Update Session Manager preferences (command line)](https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-configure-preferences-cli.html): Make changes to the Session Manager preferences for your account in the selected AWS Region.
- [Step 5: (Optional) Restrict access to commands in a session](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-restrict-command-access.html): Create a custom Session type SSM document to restrict the commands a user can run in a Session Manager session.
- [Step 6: (Optional) Use AWS PrivateLink to set up a VPC endpoint for Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started-privatelink.html): Improve the security posture of your managed nodes by configuring Systems Manager to use an interface VPC endpoint.
- [Step 7: (Optional) Turn on or turn off ssm-user account administrative permissions](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started-ssm-user-permissions.html): Manage the permissions of the default operating system user when a Session Manager session is started, ssm-user.
- [Step 8: (Optional) Allow and control permissions for SSH connections through Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started-enable-ssh-connections.html): Allow users in your AWS account to use the AWS CLI to establish SSH connections to managed nodes using Session Manager.

### [Working with Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with.html)

Use the Systems Manager console, Amazon EC2 console, or AWS CLI to start sessions that connect you to your managed nodes.

### [Install the Session Manager plugin for the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html)

Install the Session Manager plugin on your system to use the AWS CLI to start and end sessions that connect to your managed nodes.

- [Version history](https://docs.aws.amazon.com/systems-manager/latest/userguide/plugin-version-history.html): Learn about the latest version and release history of the Session Manager plugin.
- [Install on Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/install-plugin-windows.html): Learn how to install the Session Manager plugin on Windows Server systems.
- [Install on macOS](https://docs.aws.amazon.com/systems-manager/latest/userguide/install-plugin-macos-overview.html): Learn how to install the Session Manager plugin on macOS systems.

### [Install the Session Manager plugin on Linux](https://docs.aws.amazon.com/systems-manager/latest/userguide/install-plugin-linux-overview.html)

Learn how to install the Session Manager plugin on Linux distributions.

- [Verify the signature of the Session Manager plugin](https://docs.aws.amazon.com/systems-manager/latest/userguide/install-plugin-linux-verify-signature.html): Learn how to verify the digital signature of the Session Manager plugin for security.
- [Install on Amazon Linux 2, AL2023, and RHEL distros](https://docs.aws.amazon.com/systems-manager/latest/userguide/install-plugin-linux.html): Learn how to install the Session Manager plugin on Linux systems.
- [Install on Debian Server and Ubuntu Server](https://docs.aws.amazon.com/systems-manager/latest/userguide/install-plugin-debian-and-ubuntu.html): Learn how to install the Session Manager plugin on Debian Server and Ubuntu Server systems.
- [Verify the Session Manager plugin installation](https://docs.aws.amazon.com/systems-manager/latest/userguide/install-plugin-verify.html): Learn how to confirm that the Session Manager plugin is properly installed and configured.
- [Session Manager plugin on GitHub](https://docs.aws.amazon.com/systems-manager/latest/userguide/plugin-github.html): Discover how to access the Session Manager plugin source code and documentation on GitHub.
- [(Optional) Turn on Session Manager plugin logging](https://docs.aws.amazon.com/systems-manager/latest/userguide/install-plugin-configure-logs.html): Learn how to enable logging for the Session Manager plugin to track session activity.
- [Start a session](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-sessions-start.html): Use the Systems Manager console, Amazon EC2 console, AWS CLI, or SSH to start a session.
- [End a session](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-sessions-end.html): Use the Systems Manager console or the AWS CLI to end a session that you started in your account.
- [View session history](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-view-history.html): Use the Systems Manager console or the AWS CLI to view information about sessions in your account.
- [Logging session activity](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-auditing.html): Log session API calls in your AWS account using AWS CloudTrail.

### [Enabling and disabling session logging](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-logging.html)

Enable or disable session logging in your AWS account.

- [Streaming session data using Amazon CloudWatch Logs (console)](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-logging-cwl-streaming.html): Learn how to stream session data to Amazon CloudWatch Logs for real-time monitoring.
- [Logging session data using Amazon S3 (console)](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-logging-s3.html): Store session log data in a specified Amazon S3 bucket for debugging and troubleshooting purposes.
- [Logging session data using Amazon CloudWatch Logs (console)](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-logging-cloudwatch-logs.html): Learn how to configure session logging to Amazon CloudWatch Logs for audit purposes.
- [Configuring session logging to disk](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-logging-disk.html): Learn how to set up local disk logging for session data.
- [Adjusting how long the Session Manager temporary log file is stored on disk](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-logging-disk-retention.html): Learn how to configure retention settings for temporary session log files.
- [Disabling Session Manager logging in CloudWatch Logs and Amazon S3](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-enable-and-disable-logging.html): Learn how to turn off session logging to CloudWatch Logs and Amazon S3 services.
- [Session document schema](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-schema.html): Learn about the different schema elements of a Session document.
- [Troubleshooting Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-troubleshooting.html): Troubleshoot problems with Session Manager.

### [State Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state.html)

State Manager, a tool in AWS Systems Manager, helps prevent configuration drift.

- [Understanding how State Manager works](https://docs.aws.amazon.com/systems-manager/latest/userguide/state-manager-about.html): Learn how to use Systems Manager State Manager to automate the process of keeping your managed nodes in a hybrid and multicloud infrastructure in a state that you define.

### [Working with associations](https://docs.aws.amazon.com/systems-manager/latest/userguide/state-manager-associations.html)

Learn how to work with State Manager associations.

- [Understanding targets and rate controls](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state-manager-targets-and-rate-controls.html): Learn how to deploy a State Manager association to dozens or hundreds of nodes while controlling the number of nodes that run the association at the scheduled time.
- [Creating associations](https://docs.aws.amazon.com/systems-manager/latest/userguide/state-manager-associations-creating.html): Create a State Manager association by using the Systems Manager console, the AWS CLI, or Tools for Windows PowerShell.
- [Editing an association](https://docs.aws.amazon.com/systems-manager/latest/userguide/state-manager-associations-edit.html): Edit a State Manager association by using the AWS CLI, console, and Tools for Windows PowerShell to specify a new name, schedule, severity level, or targets.
- [Deleting associations](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state-manager-delete-association.html): Delete a Systems Manager State Manager association.
- [Running Auto Scaling groups with associations](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state-manager-asg.html): Learn the best practices for creating State Manager associations to run Auto Scaling groups.
- [Viewing association histories](https://docs.aws.amazon.com/systems-manager/latest/userguide/state-manager-associations-history.html): View association histories to see the status, detailed status, results, last execution time, and more information about a State Manager association.
- [Working with associations using IAM](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state-manager-iam.html): Best practices for working with associations using IAM.
- [Creating associations that run MOF files](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state-manager-using-mof-file.html): Run MOF files to enforce a desired state on Windows Server managed nodes with State Manager by using the AWS-ApplyDSCMofs SSM document.
- [Creating associations that run Ansible playbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state-manager-ansible.html): Create State Manager associations that run Ansible playbooks by using the AWS-ApplyAnsiblePlaybooks SSM document.
- [Creating associations that run Chef recipes](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state-manager-chef.html): Create State Manager associations that run Chef recipes using the AWS-ApplyChefRecipes SSM document.
- [Walkthrough: Automatically update SSM Agent with the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/state-manager-update-ssm-agent-cli.html): Create a State Manager association with the AWS CLI that automatically updates the SSM Agent according to a schedule that you specify.
- [Walkthrough: Automatically update PV drivers on EC2 instances for Windows Server](https://docs.aws.amazon.com/systems-manager/latest/userguide/state-manager-update-pv-drivers.html): Configure a State Manager association to automatically download and install new AWS PV drivers when the drivers become available.

### [Change management tools](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-actions-and-change.html)

Make changes to your AWS resources using Systems Manager tools.

### [Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)

Simplify common maintenance and deployment of Amazon EC2 instances and other AWS resources with Systems Manager Automation.

### [Setting up Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-setup.html)

Verify user access to Systems Manager Automation and configure roles so the service can perform actions on your resources.

- [Create service roles for Automation by using CloudFormation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-setup-cloudformation.html): Create a service role for Automation from an CloudFormation template.
- [Create the service roles for Automation using the console](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-setup-iam.html): Create a service role for Systems Manager Automation using IAM.
- [Setting up identity based policies examples](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-setup-identity-based-policies.html): Learn how to grant IAM users and roles permission for AWS Systems Manager Automation service.
- [Allowing Automation to adapt to your concurrency needs](https://docs.aws.amazon.com/systems-manager/latest/userguide/adaptive-concurrency.html): Allow Automation to adjust your concurrent automation quota automatically to scale.
- [Configuring automatic retry for throttled operations](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-throttling-retry.html): Configure automatic retry behavior for automation steps that encounter throttling exceptions.
- [Implement change controls for Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-change-calendar-integration.html): Integrate Automation with Change Calendar to prevent unapproved changes during the time periods you specify.
- [Run an automated operation powered by Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/running-simple-automations.html): Run an automation using AWS Systems Manager Automation with the AWS Management Console or your preferred command line tool.
- [Rerunning automation executions](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-rerun-executions.html): Rerun automation executions with identical or modified parameters to streamline repeated tasks.
- [Run an automation that requires approvals](https://docs.aws.amazon.com/systems-manager/latest/userguide/running-automations-require-approvals.html): Run an automation with approvals by using the AWS CLI and console.

### [Run automated operations at scale](https://docs.aws.amazon.com/systems-manager/latest/userguide/running-automations-scale.html)

Run automations at scale using using targets and rate controls.

- [Mapping targets for an automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/running-automations-map-targets.html): Define which resources are targeted by an automation.
- [Control automations at scale](https://docs.aws.amazon.com/systems-manager/latest/userguide/running-automations-scale-controls.html): Use rate controls to manage the deployment of an automation across a fleet of AWS resources.
- [Running automations in multiple AWS Regions and accounts](https://docs.aws.amazon.com/systems-manager/latest/userguide/running-automations-multiple-accounts-regions.html): Run automations in multiple Regions and accounts or OUs to reduce the time required to administer AWS resources and enhance security.
- [Run automations based on EventBridge events](https://docs.aws.amazon.com/systems-manager/latest/userguide/running-automations-event-bridge.html): Run automations on a schedule, or when a specific AWS system event occurs by using a runbook as the target of an EventBridge event.
- [Run an automation step by step](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing-manually.html): Run an automation by using the manual execution mode from the AWS CLI or console.
- [Scheduling automations with State Manager associations](https://docs.aws.amazon.com/systems-manager/latest/userguide/scheduling-automations-state-manager-associations.html): Target different types of AWS resources by creating a State Manager association that uses a runbook.
- [Schedule automations with maintenance windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/scheduling-automations-maintenance-windows.html): Run automations during scheduled maintenance periods by configuring a runbook as a registered task for a maintenance window.

### [Automation actions reference](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-actions.html)

Automation actions determine the input, behavior, and output of each step in an Automation runbook.

- [aws:approve â Pause an automation for manual approval](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-approve.html): Temporarily pause running an Automation until designated principals either approve or reject the action.
- [aws:assertAwsResourceProperty â Assert an AWS resource state or event state](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-assertAwsResourceProperty.html): Assert a specific resource state or event state for a specific Automation step.
- [aws:branch â Run conditional automation steps](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-branch.html): Create a dynamic automation that evaluates different choices in a step and jumps to a different step based on the results of that evaluation.
- [aws:changeInstanceState â Change or assert instance state](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-changestate.html): Change or assert the state of the instance.
- [aws:copyImage â Copy or encrypt an Amazon Machine Image](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-copyimage.html): Copy an AMI from any AWS Region into the current Region.
- [aws:createImage â Create an Amazon Machine Image](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-create.html): Create an AMI from an instance that is either running, stopping, or stopped.
- [aws:createStack â Create an CloudFormation stack](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-createstack.html): Create an CloudFormation stack from a template.
- [aws:createTags â Create tags for AWS resources](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-createtag.html): Create tags for Amazon EC2 instances or Systems Manager managed instances.
- [aws:deleteImage â Delete an Amazon Machine Image](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-delete.html): Delete the specified image and all related snapshots.
- [aws:deleteStack â Delete an CloudFormation stack](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-deletestack.html): Delete an CloudFormation stack.
- [aws:executeAutomation â Run another automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-executeAutomation.html): Remove the need to duplicate steps across similar runbooks by calling a secondary runbook and running a secondary automation.
- [aws:executeAwsApi â Call and run AWS API operations](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-executeAwsApi.html): Call and run AWS API operations.
- [aws:executeScript â Run a script](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-executeScript.html): Run a Python or PowerShell script by using a specified runtime and handler.
- [aws:executeStateMachine â Run an AWS Step Functions state machine](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-executeStateMachine.html): Run an AWS Step Functions state machine.
- [aws:invokeWebhook â Invoke an Automation webhook integration](https://docs.aws.amazon.com/systems-manager/latest/userguide/invoke-webhook.html): Invoke a specified Automation webhook integration.
- [aws:invokeLambdaFunction â Invoke an AWS Lambda function](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-lamb.html): Invoke a specified Lambda function.
- [aws:loop â Iterate over steps in an automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-loop.html): Iterate over steps in an automation.
- [aws:pause â Pause an automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-pause.html): Pause running an automation.
- [aws:runCommand â Run a command on a managed instance](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-runcommand.html): Run the specified commands.
- [aws:runInstances â Launch an Amazon EC2 instance](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-runinstance.html): Launch a new Amazon EC2 instance.
- [aws:sleep â Delay an automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-sleep.html): Delay an Automation from running for a specified amount of time.
- [aws:updateVariable â Updates a value for a runbook variable](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-update-variable.html): Update a value for a runbook variable.
- [aws:waitForAwsResourceProperty â Wait on an AWS resource property](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-waitForAwsResourceProperty.html): Allow your automation to wait for a specific resource state or event state before continuing the automation.
- [Automation system variables](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-variables.html): Learn about the variables used by Systems Manager Automation runbooks.

### [Creating your own runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html)

Learn about the actions Systems Manager Automation can perform on your managed instances and other AWS resources when using runbooks.

### [Visual design experience for Automation runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-visual-designer.html)

Learn about the visual design experience for Systems Manager Automation.

- [Interface overview](https://docs.aws.amazon.com/systems-manager/latest/userguide/visual-designer-interface-overview.html): Visual design experience interface overview
- [Using the visual design experience](https://docs.aws.amazon.com/systems-manager/latest/userguide/visual-designer-use.html): Learn how to use the visual design experience for Automation.
- [Configure inputs and outputs](https://docs.aws.amazon.com/systems-manager/latest/userguide/visual-designer-action-inputs-outputs.html): Use the visual design experience to configure inputs and outputs for automation actions.
- [Error handling with the visual design experience](https://docs.aws.amazon.com/systems-manager/latest/userguide/visual-designer-error-handling.html): Configure error handling using the visual design experience.
- [Tutorial: Create a runbook using the visual design experience](https://docs.aws.amazon.com/systems-manager/latest/userguide/visual-designer-tutorial.html): Create a runbook using the visual design experience.

### [Authoring Automation runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-authoring-runbooks.html)

Learn how to author Systems Manager Automation runbooks.

- [Example 1: Creating parent-child runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-authoring-runbooks-parent-child-example.html): Learn how to create parent-child runbook relationships to organize and manage complex automation workflows.
- [Example 2: Scripted runbook](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-authoring-runbooks-scripted-example.html): Learn how to build scripted runbooks to automate tasks using custom scripts and programming logic.

### [Additional runbook examples](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-document-examples.html)

Review runbook examples that demonstrate how you can automate common deployment, troubleshooting, and maintenance tasks using automation actions.

- [Deploy VPC architecture and Microsoft Active Directory domain controllers](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-document-architecture-deployment-example.html): Automate deployments to increase efficiency, reduce the potential for human error, and standardize common tasks.
- [Restore a root volume from the latest snapshot](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-document-instance-recovery-example.html): Retrieve details from the root volume of an instance, retrieve the latest snapshot for the root volume, and continue the automation if a snapshot is found.
- [Create an AMI and cross-Region copy](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-document-backup-maintenance-example.html): Create an AMI, confirm its availability, and copy it to the destination AWS Region by using Automation actions.
- [Creating input parameters that populate AWS resources](https://docs.aws.amazon.com/systems-manager/latest/userguide/populating-input-parameters.html): Create input parameters in your runbook content that populate your AWS resources in the AWS Management Console.
- [Using Document Builder to create runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-document-builder.html): Learn how to use the Document Builder tool provided by Systems Manager Automation to create your own custom runbooks.
- [Using scripts in runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-document-script-considerations.html): Learn how Systems Manager Automation allows you to run scripts directly from runbooks without creating a separate compute environment.
- [Using conditional statements in runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-branch-condition.html): Create automations that jump to different steps after evaluating different choices or that dynamically respond to changes when a step completes.
- [Using action outputs as inputs](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-outputs-inputs.html): Learn how to use outputs from automation actions as values for inputs in later actions in your runbooks.
- [Creating webhook integrations for Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/creating-webhook-integrations.html): Create integrations to use webhooks in Automation runbooks.
- [Handling timeouts in runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-handling-timeouts.html): Specify the execution timeout value for an action and change how an action timing out affects the automation and overall run status.
- [Automation Runbook Reference](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents-reference.html): Learn about the predefined runbooks maintained by AWS, Support, and AWS Config.

### [Tutorials](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-tutorials.html)

Learn how to use Automation runbooks to address common use cases.

### [Updating AMIs](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-tutorial-update-ami.html)

Update AMIs to include the latest patches.

- [Update a Linux AMI](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-tutorial-update-patch-linux-ami.html): Use the AWS-UpdateLinuxAmi runbook to update a Linux AMI to include the latest patches of specific packages.
- [Update a Windows ServerÂ AMI](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-tutorial-update-patch-windows-ami.html): Automate image maintenance tasks on your Amazon Windows AMI without authoring the runbook in JSON or YAML.
- [Update a golden AMI using Automation, AWS Lambda, and Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-tutorial-update-patch-golden-ami.html): Automatically apply operating system patches to a Windows AMI that is already considered to be the most up-to-date AMI.
- [Updating AMIs using Automation and Jenkins](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-tutorial-update-patch-ami-jenkins-integration.html): Learn how to pre-install applications into AMIs using Automation and Jenkins software in a CI/CD pipeline.
- [Updating AMIs for Auto Scaling groups](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-tutorial-update-patch-windows-ami-autoscaling.html): Automate updates for AMIs to include the latest patches, and create a launch template for an Auto Scaling group that uses the udpated AMI.

### [Using AWS Support self-service runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-tutorial-support-runbooks.html)

Use runbooks created by AWS Support to help you troubleshoot common issues with your AWS resources.

- [Run the EC2Rescue tool on unreachable instances](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-ec2rescue.html): Troubleshoot problems on EC2 instances for Linux and Windows manually or automatically using Automation and the AWSSupport-ExecuteEC2Rescue runbook.
- [Reset passwords and SSH keys on EC2 instances](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-ec2reset.html): Use the AWSSupport-ResetAccess runbook to re-enable local Administrator passwords and to generate new SSH keys.
- [Passing data to Automation using input transformers](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-tutorial-eventbridge-input-transformers.html): Use the input transformer feature of Amazon EventBridge to extract the instance-id of an EC2 instance from an instance state change event.
- [Learn about statuses returned by Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-statuses.html): Automation reports detailed status information about an automation action or step when you run an automation and for the overall automation.
- [Troubleshooting Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-troubleshooting.html): Troubleshoot problems with the Automation service and resolve issues based on Automation error messages.

### [Change Calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar.html)

Control changes to your Systems Manager infrastructure by specifying periods of time during which you want to limit or prevent code changes to resources.

- [Setting up Change Calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar-prereqs.html): Install command line tools and set up permissions to get state information about calendars and create, update, or delete a Change Calendar entry.

### [Working with Change Calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar-working.html)

Add, manage, or delete Change Calendar entries.

- [Creating a change calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-calendar-create.html): Create a Systems Manager document that uses the text format to create a Change Calendar entry.

### [Creating and managing events in Change Calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-calendar-events.html)

Create and manage events for a calendar in Systems Manager Change Calendar using the Systems Manager console.

- [Create an event](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-calendar-create-event.html): Add an event to a Change Calendar to specify a period of time during which the default action of the calendar entry is suspended.
- [Update an event](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-calendar-update-event.html): Update a Change Calendar event using the Systems Manager console.
- [Delete an event](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-calendar-delete-event.html): Delete a Change Calendar event using the Systems Manager console.

### [Importing and managing events from third-party calendars](https://docs.aws.amazon.com/systems-manager/latest/userguide/third-party-events.html)

Use the Import calendar feature to add events from a third-party calendar provider to your calendar in Systems Manager Change Calendar.

- [Importing events from third-party calendar providers](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-calendar-import.html): Import a calendar file with its events that you have exported from a third-party calendar application.
- [Updating all events from a third-party calendar provider](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-calendar-import-add-remove.html): Update all events from third-party calendar applications in Change Calendar.
- [Deleting all events imported from a third-party calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-calendar-delete-ics.html): Remove all events imported from third-party calendar applications.
- [Updating a change calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-calendar-update.html): Update a change calendar using the Systems Manager console to edit the document that you created when you created the entry.
- [Sharing a change calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-calendar-share.html): Share a change calendar with other AWS accounts by using the Systems Manager console.
- [Deleting a change calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-calendar-delete.html): Delete a change calendar by using the Systems Manager console.
- [Getting the state of a change calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-calendar-getstate.html): Use the Systems ManagerGetCalendarState API operation to get the overall state of the calendar or the state of the calendar at a specific time.
- [Adding Change Calendar dependencies to Automation runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar-automations.html): Make Automation actions adhere to Change Calendar by using the aws:assertAwsResourceProperty action in an Automation runbook.
- [Troubleshooting Change Calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-calendar-troubleshooting.html): Troubleshoot problems with Change Calendar, a tool in AWS Systems Manager.

### [Change Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager.html)

Request, approve, implement, and report on operational changes to your application configuration and infrastructure using Change Manager.

### [Setting up Change Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-setting-up.html)

Set up Change Manager to manage changes for an entire organization.

- [Setting up Change Manager for an organization (management account)](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-organization-setup.html): Set up Change Manager for use with an organization that is defined in Organizations.

### [Configuring Change Manager options and best practices](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-account-setup.html)

Perform these tasks the first time you access Change Manager whether you're using it across an organization or in a single AWS account.

- [Configuring Amazon SNS topics for Change Manager notifications](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-sns-setup.html): Configure Change Manager to send notifications to an Amazon SNS topic for events related to change requests and change templates.
- [Configuring roles and permissions for Change Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-permissions.html): Create a service role for Systems Manager Change Manager using IAM.
- [Controlling access to auto-approval runbook workflows](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-auto-approval-access.html): Use a condition in an IAM policy to prevent a user, group or IAM role from running auto-approval runbook workflows.

### [Working with Change Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/working-with-change-manager.html)

Perform change-related tasks in Change Manager for which users across your organization or in a single AWS account have been granted the necessary permissions.

### [Working with change templates](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-templates.html)

Use a change template in Change Manager to define things such as required approvals, available runbooks, and notification options for change requests.

- [Try out the AWS managed Hello World change template](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-templates-aws-managed.html): Use a sample change template to test the review and approval process after you have finished setting up Change Manager.

### [Creating change templates](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-templates-create.html)

Create change templates using the Change Manager Builder, Editor, or command line tools.

### [About approvals in your change templates](https://docs.aws.amazon.com/systems-manager/latest/userguide/cm-approvals-templates.html)

Learn how Change Manager supports both per-line approvals and per-level approvals.

- [Change Manager approval type examples](https://docs.aws.amazon.com/systems-manager/latest/userguide/approval-type-samples.html): View samples of approval types in Change Manager
- [Creating change templates using Builder](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-templates-custom-builder.html): Configure the runbook workflow defined in a Change Manager change template without using JSON or YAML syntax by using the Builder for change templates.
- [Creating change templates using Editor](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-templates-custom-editor.html): Configure a change template in Change Manager by entering JSON or YAML instead of using the console controls.
- [Creating change templates using command line tools](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-templates-tools.html): Use command line tools to create change templates for Change Manager.
- [Reviewing and approving or rejecting change templates](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-templates-review.html): Review and approve or reject a change template in Change Manager when you are notified that a new change template is awaiting your review.
- [Deleting change templates](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-templates-delete.html): Learn how to delete change templates in Systems Manager Change Manager.

### [Working with change requests](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-requests.html)

Run an Automation runbook that updates one or more resources in your AWS or on-premises environments using a Change Manager change request.

- [Creating change requests](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-requests-create.html): Create a Change Manager change request by using the console or AWS CLI.
- [Reviewing and approving or rejecting change requests](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-requests-review.html): Use the Systems Manager console to review and approve or reject a change request in Change Manager.
- [Reviewing change request details, tasks, and timelines (console)](https://docs.aws.amazon.com/systems-manager/latest/userguide/reviewing-changes.html): View information about a change request in Change Manager, including requests for which changes have been processed, in the Change Manager dashboard.
- [Viewing aggregated counts of change requests (command line)](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-requests-review-aggregate-command-line.html): View aggregated counts of change requests in Change Manager by using the GetOpsSummary API operation.
- [Auditing and logging Change Manager activity](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-auditing.html): Audit Change Manager activity by using AWS CloudTrail and Amazon CloudWatch alarms.
- [Troubleshooting Change Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-troubleshooting.html): Troubleshoot problems with Change Manager, a tool in AWS Systems Manager.

### [Documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents.html)

Define the actions that Systems Manager performs on your managed instances using SSM documents.

### [Document components](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-components.html)

Learn about the components that make up SSM documents.

- [Schemas, features, and examples](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-schemas-features.html): SSM documents use different schema versions for different document types.
- [Data elements and parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-syntax-data-elements-parameters.html): Learn about the data elements used for SSM documents.
- [Command document plugin reference](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-command-ssm-plugin-reference.html): Choose what actions are performed on managed instances by specifying plugins in Command type SSM documents.
- [Creating SSM document content](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-creating-content.html): Create a custom SSM document to perform actions on your AWS resources.

### [Working with documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-using.html)

Learn about how to create, delete, compare, and work with SSM documents.

- [Compare SSM document versions](https://docs.aws.amazon.com/systems-manager/latest/userguide/comparing-versions.html): Compare the differences between different versions of SSM documents using the console.
- [Create an SSM document](https://docs.aws.amazon.com/systems-manager/latest/userguide/create-ssm-console.html): Create a custom SSM document using the console.
- [Deleting custom SSM documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/deleting-documents.html): Delete a custom SSM document using the console.
- [Running documents from remote locations](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-running-remote-github-s3.html): Run SSM documents from remote locations by using Run Command in the Systems Manager console.
- [Sharing SSM documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-ssm-sharing.html): Share SSM documents privately or publicly with accounts in the same AWS Region by modifying the document permissions.
- [Searching for SSM documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-documents-searching.html): Favorite and search for SSM documents using the console or the command line.
- [Troubleshooting parameter handling issues](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-troubleshooting.html): Common issues and solutions when working with SSM document parameters and environment variable interpolation.

### [Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows.html)

Define a schedule for performing potentially disruptive actions on your nodes and other AWS resources using Systems Manager Maintenance Windows.

### [Setting up](https://docs.aws.amazon.com/systems-manager/latest/userguide/setting-up-maintenance-windows.html)

Grant the necessary permissions for users in your account to create and schedule maintenance window tasks using Systems Manager Maintenance Windows.

- [Control access using the console](https://docs.aws.amazon.com/systems-manager/latest/userguide/configuring-maintenance-window-permissions-console.html): Learn how to use the Systems Manager console to create the required roles and permissions for maintenance windows.
- [Control access using the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/configuring-maintenance-window-permissions-cli.html): Learn how to use the AWS CLI to create the required roles and permissions for Maintenance Windows, a tool in AWS Systems Manager.

### [Create and manage maintenance windows using the console](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-working.html)

Learn how to create, configure, update, delete, and manage the targets and tasks of maintenance windows using the Systems Manager console.

- [Create a maintenance window](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-create-mw.html): Learn how to create a maintenance window in AWS Systems Manager and specify its basic options.
- [Assign targets to a maintenance window](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-assign-targets.html): Learn how to specify which resources a maintenance window performs actions on in Maintenance Windows, a tool in AWS Systems Manager.
- [Assign tasks to a maintenance window](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-assign-tasks.html): Learn how to add actions to perform on a resource when a maintenance window runs in Maintenance Windows, a tool in AWS Systems Manager.
- [Disable or enable a maintenance window](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-disable.html): Learn how to disable or enable a maintenance window in Maintenance Windows, a tool in AWS Systems Manager.
- [Update or delete maintenance window resources](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-update.html): Learn how to update or delete a maintenance window or its targets and tasks in Maintenance Windows, a tool in AWS Systems Manager.

### [Tutorials](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-tutorials.html)

Learn how to use Maintenance Windows, a tool in AWS Systems Manager, by completing tutorials.

### [Create and manage maintenance windows using the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-window-tutorial-cli.html)

Learn how to use the AWS CLI to create and configure, view information about, update, and delete a maintenance window.

### [Create and configure a maintenance window using the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-cli-tutorials-create.html)

Learn how to use the AWS CLI to create and configure a maintenance window, its targets, and its tasks.

- [Step 1: Create the maintenance window using the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-create-mw.html): Learn how to create a maintenance window in Systems Manager and specify its basic options using the AWS CLI.

### [Step 2: Register a target node with the maintenance window using the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-targets.html)

Learn how to register a target with a new maintenance window in Systems Manager, and to specify which node to update when the maintenance window runs.

- [Examples: Register targets with a maintenance window](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-targets-examples.html): Learn how to register one or more nodes as targets in Maintenance Windows, a tool in AWS Systems Manager.

### [Step 3: Register a task with the maintenance window using the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-tasks.html)

Learn how to register a Run Command-type task for a maintenance window that runs the df command on an EC2 instance for Linux.

- [Examples: Register tasks with a maintenance window](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-register-tasks-examples.html): Learn how to register Run Command tasks, Automation workflows, Lambda functions, and Step Functions tasks with a maintenance window by viewing examples.
- [Parameter options for the register-task-with-maintenance-windows command](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-task-options.html): Learn how to configure a maintenance window task in Systems Manager according to your needs using the register-task-with-maintenance-window command.
- [View information about a maintenance windows using the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-cli-tutorials-describe.html): Learn how to view information about your maintenance windows, tasks, executions, and invocations in Systems Manager.
- [View information about tasks and task executions using the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-task-info.html): Learn how to use the AWS CLI to view details about your completed maintenance window tasks in Systems Manager.
- [Update a maintenance window using the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-cli-tutorials-update.html): Learn how to update a maintenance window in Systems Manager and update different maintenance window task types by using the AWS CLI.
- [Delete a maintenance window using the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-delete-mw.html): Learn how to delete a Systems Manager maintenance window that was created in a tutorial.

### [Create a maintenance window for patching using the console](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-window-tutorial-patching.html)

Learn how to create a maintenance window in Systems Manager to patch your managed nodes.

- [Patching schedules using maintenance windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-scheduletasks.html): Discover how to apply patches to your node by using a maintenance window in AWS Systems Manager after you configure a patch baseline and a patch group.
- [Using pseudo parameters when registering maintenance window tasks](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-window-tasks-pseudo-parameters.html): Learn how to use input parameters in the console or the --task-invocation-parameters option to specify the parameters that are unique to each maintenance window task type in Systems Manager.
- [Maintenance window scheduling and active period options](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-schedule-options.html): Discover how to determine how often a Systems Manager maintenance window runs by using a cron and rate expression.
- [Registering maintenance window tasks without targets](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html): Learn about the types of maintenance window tasks in Systems Manager for which you don't need to specify targets.
- [Troubleshooting maintenance windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/troubleshooting-maintenance-windows.html): Learn how to troubleshoot problems with maintenance windows in AWS Systems Manager.

### [Quick Setup](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-quick-setup.html)

Learn how to use Quick Setup, a tool in AWS Systems Manager, to quickly configure frequently used Amazon Web Services services and features with recommended best practices.

- [Getting started with Quick Setup](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-getting-started.html): Learn how to get started with Quick Setup, a tool in AWS Systems Manager, using the required AWS Identity and Access Management permissions and roles.
- [Configure Assume Role](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-assume-role.html): Configure the Systems Manager Assume Role for Automation Quick Setup

### [Using a delegated administrator for Quick Setup](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-delegated-administrator.html)

Learn how to register a delegated administrator for Quick Setup.

- [Register a delegated administrator for Quick Setup](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-register-delegated-administrator.html): Learn the step-by-step process for registering a delegated administrator account for Systems Manager Quick Setup through the AWS Management Console.
- [Deregister a delegated administrator for Quick Setup](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-deregister-delegated-administrator.html): Learn how to remove a delegated administrator account from Quick Setup management.
- [Learn Quick Setup terminology and details](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-using.html): Learn about the types of information used by configuration managers in Quick Setup, a tool in AWS Systems Manager.
- [Using the Quick Setup API to manage configurations and deployments](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-api.html): Discover how to create and manage Quick Setup configurations and deployments using the public Quick Setup API provided with the AWS CLI or your preferred AWS SDK.

### [Supported Quick Setup configuration types](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-config-types.html)

Learn about the types of configurations supported by Quick Setup, a tool in AWS Systems Manager.

- [Set up Amazon EC2 host management](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-host-management.html): Learn how to quickly configure security roles and Systems Manager tools on your Amazon EC2 instances by using Quick Setup.
- [Set up the Default Host Management Configuration for an organization](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-default-host-management-configuration.html): Learn how to use Quick Setup, a tool in AWS Systems Manager, to configure checks for updates to SSM Agent for all EC2 instances in all your organization's accounts and Regions.
- [Create an AWS ConfigÂ configuration recorder](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-config.html): Learn how to use Quick Setup, a tool in AWS Systems Manager, to quickly create a configuration recorder powered by AWS Config to detect changes in your resource configurations and capture the changes as configuration items.
- [Deploy AWS Config conformance pack](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-cpack.html): Learn how to use Quick Setup, a tool in AWS Systems Manager, to quickly deploy conformance packs from AWS Config to your resources.
- [Configure patching for instances in an organization using patch policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-patch-manager.html): Learn how to use Quick Setup, a tool in AWS Systems Manager, to automate patching of EC2 instances and other managed nodes in your AWS account or organization.
- [Set up DevOpsÂ Guru](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-devops.html): Learn how to use Quick Setup, a tool in AWS Systems Manager, to quickly configure DevOpsÂ Guru options.
- [Deploy Distributor packages](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-distributor.html): Learn how to use Quick Setup to quickly deploy Distributor packages to nodes in your organization.
- [Stop and start EC2 instances automatically on a schedule](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-scheduler.html): Learn how to use Quick Setup, a tool in AWS Systems Manager, to schedule the starting and stopping of your Amazon EC2 instances.
- [Configure AWS Resource Explorer](https://docs.aws.amazon.com/systems-manager/latest/userguide/Resource-explorer-quick-setup.html): Learn how to use Quick Setup, a tool in AWS Systems Manager, to create and configure indexes for all AWS Regions at the AWS account or AWS organization level.
- [Troubleshooting Quick Setup results](https://docs.aws.amazon.com/systems-manager/latest/userguide/quick-setup-results-troubleshooting.html): Learn how to troubleshoot issues with Quick Setup, a tool in AWS Systems Manager.

### [Application tools](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-application-management.html)

Manage your applications running in AWS by using the Application tools suite of capabilities.

- [AWS AppConfig](https://docs.aws.amazon.com/systems-manager/latest/userguide/appconfig.html): AWS AppConfig feature flags and dynamic configurations help software builders quickly and securely adjust application behavior in production environments without full code deployments.

### [Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager.html)

Investigate and remediate issues with your AWS resources in the context of your applications and clusters by using Application Manager.

- [Setting up related services](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager-getting-started-related-services.html): View AWS resources and operations information about your AWS resources in Application Manager.
- [Configuring permissions for Systems Manager Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager-getting-started-permissions.html): Use all features of Application Manager if your IAM user, group, or role has access to certain API operations.
- [Adding applications and container clusters to Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager-getting-started-adding-applications.html): Operate a logical group of AWS resources as a unit.

### [Working with applications](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager-working-applications.html)

Work with Systems Manager Application Manager applications, and view operations information about your AWS resources.

- [Application overview in Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager-working-viewing-overview.html): View a summary of Amazon CloudWatch alarms, OpsItems, and runbook history from the Overview tab.
- [Managing your application EC2 instances](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager-working-instances.html): Learn how to use Application Manager to organize and manage Amazon EC2 instances by application.
- [Viewing resources associated with your application](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager-working-viewing-resources.html): View the AWS resources in your application from the Resources tab.
- [Managing your application compliance](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager-working-viewing-resource-compliance.html): View AWS Config resources and configuration rule compliance information from the Compliance tab.
- [Using CloudWatch Application Insights to monitor an application](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager-working-viewing-monitors.html): View the Amazon CloudWatch alarm status for resources in an application from the Monitoring tab.
- [Viewing OpsItems for an application](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager-working-viewing-OpsItems.html): View OpsItems for resources in the selected application using the OpsItems tab.
- [Managing your application logs](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager-viewing-logs.html): View a list of log groups from Amazon CloudWatch Logs using the Logs tab.
- [Use Automation runbooks to remediate application issues](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager-working-runbooks.html): Remediate issues with AWS resources from Application Manager by using Systems Manager Automation runbooks.
- [Tag resources in Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager-working-tags.html): Add or delete tags on your AWS resources by using Application Manager.

### [Working with CloudFormation templates and stacks](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager-working-stacks.html)

Create, edit, and delete AWS CloudFormation templates and stacks by using Systems Manager Application Manager.

- [Using Application Manager to manage CloudFormation templates](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager-working-templates-overview.html): View, create, and edit AWS CloudFormation templates in the Systems Manager Application Manager template library.
- [Using Application Manager to manage CloudFormation stacks](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager-working-stacks-overview.html): Create and edit CloudFormation stacks by using AWS Systems Manager Application Manager.

### [Working with clusters](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager-working-clusters.html)

Work with clusters in Systems Manager Application Manager to view operations information about your AWS resources.

- [Working with Amazon ECS in Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager-working-ECS.html): View the health of your Amazon ECS cluster infrastructure and a component runtime of the compute, networking, and storage resources in a cluster.
- [Working with Amazon EKS in Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager-working-EKS.html): View the health of your Amazon EKS cluster infrastructure and a component runtime of the compute, networking, and storage resources in a cluster.
- [Working with runbooks for clusters](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager-working-runbooks-clusters.html): Remediate issues with AWS resources from Application Manager by using Systems Manager Automation runbooks.

### [Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)

Learn how Parameter Store, a tool in AWS Systems Manager, provides secure, hierarchical storage for configuration data management and secrets management.

### [Setting up Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-setting-up.html)

Learn how to set up notifications or invoke actions based on events in Parameter Store, a tool in AWS Systems Manager, to restrict access to parameters using IAM policies, manage parameter tiers, or increase Parameter Store throughput.

- [Restricting access to Parameter Store parameters using IAM policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-access.html): Learn how to restrict access to parameters in Parameter Store, a tool in AWS Systems Manager, by using IAM policies.
- [Managing parameter tiers](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html): Learn how to configure parameters in Patch Manager, a tool in AWS Systems Manager, to use the standard-parameter tier or the advanced-parameter tier.
- [Increasing or resetting Parameter Store throughput](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-throughput.html): Learn how to increase the TPS quota in Parameter Store, a tool in AWS Systems Manager, so you can operate at higher volumes, or reset the quota to defaults.
- [Setting up notifications or triggering actions based on Parameter Store events](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-cwe.html): Learn how to use EventBridge and Amazon SNS to notify you about changes to parameters in Parameter Store, a tool in AWS Systems Manager.

### [Working with Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-working-with.html)

Discover how to create, search for, and label parameters; to assign parameter policies; to work with parameter versions; and to search for public parameters in Parameter Store; and to and work with parameters using Run Command.

### [Creating parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-su-create.html)

Learn about the valid values for parameter names before you create a parameter in Parameter Store, a tool in AWS Systems Manager.

- [Creating a parameter using the console](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-create-console.html): Learn how to create a Parameter Store parameter by using the AWS Systems Manager console.
- [Creating a parameter using the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/param-create-cli.html): Learn how to create String, StringList, and SecureString parameter types in Parameter Store, a tool in AWS Systems Manager, by using the AWS CLI.
- [Creating a parameter using Tools for Windows PowerShell](https://docs.aws.amazon.com/systems-manager/latest/userguide/param-create-ps.html): Learn how to create String, StringList, and SecureString parameter types in Parameter Store, a tool inf AWS Systems Manager, by using Tools for Windows PowerShell.
- [Searching for parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-search.html): Dsicover how to filter through your parameters stored in Parameter Store, a tool in AWS Systems Manager, by using specific search criteria.
- [Assigning parameter policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html): Learn how to manage your parameters by assigning an Expiration, ExpirationNotification, or NoChangeNotification policy to a parameter in Parameter Store, a tool in AWS Systems Manager.
- [Working with parameter hierarchies](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-hierarchies.html): Discover how to organize and manage parameters in Parameter Store, a tool in AWS Systems Manager, by using parameter hierarchies.
- [Preventing access to Parameter Store API operations](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policy-conditions.html): Learn how to prevent users and roles in your organization from running specified API actions in Parameter Store, a tool in AWS Systems Manager.
- [Working with parameter labels](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-labels.html): Discover how to manage different versions of a parameter in Parameter Store, a tool in AWS Systems Manager, with parameter labels.
- [Working with parameter versions](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-versions.html): Learn how to create and reference parameter versions in for use in API commands and SSM documents in Parameter Store, a tool in AWS Systems Manager.
- [Working with shared parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-shared-parameters.html): Learn how to working with shared parameters in Parameter Store, a tool in AWS Systems Manager.
- [Working with parameters using Run Command commands](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-param-runcommand.html): Learn how to run parameters in Parameter Store, a tool in AWS Systems Manager, by using either Run Command on the Systems Manager console or the AWS CLI.
- [Using native parameter support for Amazon Machine Image IDs](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-ec2-aliases.html): Learn how to use parameters in Parameter Store, a tool in AWS Systems Manager, with data type aws:ec2:image in your templates, commands, and scripts.
- [Deleting parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/deleting-parameters.html): Learn how to delete a parameter in Parameter Store, a tool in AWS Systems Manager.

### [Working with public parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-public-parameters.html)

Learn how to work with information published by some AWS services as public parameters in Parameter Store, a tool in AWS Systems Manager.

- [Discovering public parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-finding-public-parameters.html): Learn how to search for public parameters in Parameter Store, a tool in AWS Systems Manager, using the Parameter Store console or the AWS CLI
- [Calling AMI public parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-public-parameters-ami.html): Learn how to call AMI public parameters in Parameter Store, a tool in AWS Systems Manager, for Amazon Linux 2, Amazon Linux 2023, macOS, and Windows Server.
- [Calling the ECS optimized AMI public parameter](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-public-parameters-ecs.html): Discover how to view the name of the latest Amazon ECS optimized AMIs in Parameter Store, a tool in AWS Systems Manager.
- [Calling the EKS optimized AMI public parameter](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-public-parameters-eks.html): Discover how to view the name of the latest Amazon EKS optimized AMI in Parameter Store, a tool in AWS Systems Manager.
- [Calling public parameters for AWS services, Regions, endpoints, and Zones](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-public-parameters-global-infrastructure.html): Discover how to call public parameters for AWS services, Regions, endpoints, and zones in Parameter Store, a tool in AWS Systems Manager.

### [Parameter Store walkthroughs](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-walk.html)

Learn how to use Parameter Store, a tool in AWS Systems Manager, with other Systems Manager tools and AWS services.

- [Creating a SecureString parameter and joining a node to a Domain (PowerShell)](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-param-securestring-walkthrough.html): Learn how to join a Windows Server managed node to a domain using Parameter Store SecureString parameters and Run Command.
- [Auditing and logging Parameter Store activity](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-logging-auditing.html): Learn how to use CloudTrail logs to capture API calls from the AWS CLI and the Systems Manager console and SDK.
- [Troubleshooting Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-troubleshooting.html): Learn how to troubleshoot problems with AWS Systems Manager Parameter StoreParameter Store, a tool in AWS Systems Manager.

### [Operations tools](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-ops-center.html)

Operations tools are a suite of capabilities that help you manage your AWS resources.

- [Incident Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/incident-manager.html): Learn about Incident Manager, a tool in AWS Systems Manager.

### [Explorer](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer.html)

View an aggregated display of OpsData about your AWS resources for your AWS accounts and across Regions.

### [Getting started](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-setup.html)

Use Integrated Setup to get started with Systems Manager Explorer and OpsCenter.

- [Setting up related services for Explorer](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-setup-related-services.html): Set up and configure other AWS services and Systems Manager tools before you use Integrated Setup.
- [Configuring roles and permissions](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-setup-permissions.html): Configure permission for Systems Manager OpsCenter and Explorer.
- [Understanding default EventBridge rules created by Integrated Setup](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-setup-default-rules.html): Work with the default rules configured by Integrated Setup.

### [Configuring a delegated administrator for Explorer](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-setup-delegated-administrator.html)

Configure a delegated administrator for Explorer to improve your security.

- [Configure an Explorer delegated administrator](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-setup-delegated-administrator-configure.html): Learn how to configure a delegated administrator account to manage Explorer across multiple AWS accounts in your organization.
- [Deregister an Explorer delegated administrator](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-setup-delegated-administrator-deregister.html): Learn how to remove a delegated administrator account from managing Explorer in your organization.

### [Setting up Systems Manager Explorer to display data from multiple accounts and Regions](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-resource-data-sync.html)

Create a resource data sync to aggregate OpsData and OpsItems from other AWS accounts and AWS Regions.

- [Understanding resource data syncs for Explorer](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-resource-data-sync-understanding.html): Learn about creating a resource data sync to aggregate OpsData and OpsItems from other AWS accounts and AWS Regions.
- [Understanding multiple account and Region resource data syncs](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-resource-data-sync-multiple-accounts-and-regions.html): Learn about how resource data syncs aggregate operational data across multiple AWS accounts and AWS Regions.
- [Creating a resource data sync](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-resource-data-sync-configuring-multi.html): Learn how to create a resource data sync to aggregate Explorer data from multiple AWS Regions and accounts.

### [Using Explorer](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-using.html)

Customize Explorer by changing the widget layout and data displayed in the dashboard.

- [Editing EventBridge rules created for Explorer](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-using-editing-default-rules.html): Edit the default rules for creating OpsItems in Systems Manager Explorer.
- [Editing data sources](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-using-editing-data-sources.html): Choose what sources AWS Systems Manager Explorer displays data from.
- [Customizing the Explorer display](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-using-filters.html): Customize widget layout and the OpsData and OpsItems displayed in AWS Systems Manager Explorer by using a drag-and-drop capability and filters.
- [Receiving Security Hub CSPM findings](https://docs.aws.amazon.com/systems-manager/latest/userguide/explorer-securityhub-integration.html): Learn how to use the AWS Systems Manager Explorer integration with AWS Security Hub CSPM to receive findings from Security Hub CSPM.
- [Deleting a resource data sync](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-using-resource-data-sync-delete.html): Aggregate OpsData and OpsItems from other accounts and Regions by creating a resource data sync.
- [Exporting OpsData](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-exporting-OpsData.html): Export up to 5,000 OpsData items as a .csv file to an Amazon S3 bucket.
- [Troubleshooting](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-troubleshooting.html): Troubleshoot common problems with AWS Systems Manager Explorer.

### [OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html)

View, investigate, and resolve operational work items (OpsItems) related to AWS resources to reduce the mean time to resolution for issues impacting those resources.

### [Set up OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-setup.html)

Use Integrated Setup to get started with Explorer and OpsCenter.

### [Setting up for multiple accounts](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-setting-up-cross-account.html)

Learn how to configure OpsCenter to manage OpsItems across multiple AWS accounts.

- [Configure using Quick Setup](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-quick-setup-cross-account.html): Learn how to use Quick Setup to set up cross-account OpsItems management in OpsCenter.
- [Manually setting up for multiple accounts](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-getting-started-multiple-accounts.html): Learn how to manually configure OpsCenter for cross-account OpsItems management.
- [Set up Amazon SNS](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-getting-started-sns.html): Learn how to set up Amazon SNS to send notifications about OpsItems activity.
- [Integrate OpsCenter with other AWS services](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-applications-that-integrate.html): Learn how to connect OpsCenter with other AWS services for enhanced functionality.

### [Create OpsItems](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-create-OpsItems.html)

Learn how to create OpsItems manually and programmatically by configuring CloudWatch alarms and EventBridge events.

- [Configure EventBridge rules](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-automatically-create-OpsItems-2.html): Learn how to configure Systems Manager OpsItems as the target of an EventBridge event and update an existing EventBridge event rule.

### [Configure CloudWatch alarms](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.html)

Configure CloudWatch to automatically create an OpsItem in Systems Manager OpsCenter when an alarm enters the ALARM state.

- [Configuring alarms (console)](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-creating-or-editing-existing-alarm-console.html): Learn how to set up CloudWatch alarms to automatically create OpsItems in OpsCenter.
- [Configuring alarms (programmatically)](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-configuring-an-existing-alarm-programmatically.html): Learn how to modify existing CloudWatch alarms to generate OpsItems programmatically.

### [Create OpsItems manually](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-manually-create-OpsItems.html)

Learn how to manually create OpsItems in OpsCenterby using the AWS Systems Manager console, AWS CLI, or AWS Tools for Windows PowerShell.

- [Creating OpsItems (console)](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-creating-OpsItems-console.html): Learn how to manually create OpsItems from the AWS Systems Manager console.
- [Creating OpsItems (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-creating-OpsItems-CLI.html): Learn how to manually create OpsItems using the AWS Command Line Interface.
- [Creating OpsItems (PowerShell)](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-creating-OpsItems-Powershell.html): Learn how to manually create OpsItems using AWS Tools for Windows PowerShell.

### [Manage OpsItems](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems.html)

Learn how to configure the options available in an OpsItem.

- [Viewing details](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems-viewing-details.html): Learn how to access and review detailed information about an OpsItem.
- [Editing an OpsItem](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems-editing-details.html): Learn how to modify and update existing OpsItems in OpsCenter.
- [Adding related resources](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems-adding-related-resources.html): Learn how to associate related AWS resources with an OpsItem.
- [Adding related OpsItems](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems-adding-related-OpsItems.html): Learn how to link related OpsItems together for better organization.
- [Adding operational data](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems-adding-operational-data.html): Learn how to include additional operational data in an OpsItem.
- [Creating an incident](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems-create-an-incident.html): Learn how to generate an incident from an existing OpsItem.
- [Managing duplicate OpsItems](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-deduplication.html): Get information about how to reduce duplicate number of OpsItems that are created by OpsCenter.
- [Analyzing insights](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-operational-insights.html): Learn how to enable or disable operational insights, view operational insights, and use insights to reduce duplicate OpsItems.
- [Viewing OpsCenter logs and reports](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-logging-auditing.html): Learn about how AWS CloudTrail audits and logs OpsCenter activity, and the information that is available in summary reports for OpsCenter.
- [Delete OpsItems](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-delete-OpsItems.html): Learn how to remove OpsItems from OpsCenter when they are no longer needed.
- [Remediate OpsItem issues](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-remediating.html): Learn how to remediate issues with AWS resources identified in your OpsItems using Systems Manager Automation.
- [Viewing OpsCenter summary reports](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-reports.html): View the OpsCenter summary page.
- [Troubleshooting issues with OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-troubleshooting.html): Learn how to resolve common problems and issues with OpsCenter.
- [CloudWatch Dashboards](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-cloudwatch-dashboards.html): Learn how to monitor your resources in a single view, and to create customized views of the metrics and alarms for your AWS resources with CloudWatch dashboards.


## [Working with SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html)

- [Learn technical details about the SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent-technical-details.html): Learn about technical details and requirements to help you implement and use SSM Agent in your Systems Manager operations.
- [Find AMIs with the SSM Agent preinstalled](https://docs.aws.amazon.com/systems-manager/latest/userguide/ami-preinstalled-agent.html): SSM Agent is preinstalled on some AMIs provided by AWS.

### [Working with SSM Agent on EC2 instances for Linux](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent-linux.html)

Install, configure, or uninstall SSM Agent for Linux operating systems.

- [Verifying the signature of SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/verify-agent-signature.html): Use a public key to verify that the SSM Agent package is original and unmodified.

### [Manually installing and uninstalling SSM Agent on EC2 instances for Linux](https://docs.aws.amazon.com/systems-manager/latest/userguide/manually-install-ssm-agent-linux.html)

Manually install or uninstall SSM Agent on an Amazon EC2 Linux operating system.

- [AlmaLinux](https://docs.aws.amazon.com/systems-manager/latest/userguide/agent-install-alma.html): Connect to a AlmaLinux instance and install SSM Agent on each instance that will run commands using Systems Manager.
- [Amazon Linux 2 and Amazon Linux 2023](https://docs.aws.amazon.com/systems-manager/latest/userguide/agent-install-al2.html): Connect to an Amazon Linux 2 or Amazon Linux 2023 instance and install SSM Agent on each instance that will run commands using Systems Manager.
- [CentOS Stream](https://docs.aws.amazon.com/systems-manager/latest/userguide/agent-install-centos-stream.html): Connect to a CentOS Stream instance and install SSM Agent on each instance that will run commands using Systems Manager.
- [Debian Server](https://docs.aws.amazon.com/systems-manager/latest/userguide/agent-install-deb.html): Connect to a Debian Server instance and install SSM Agent on each instance that will run commands using Systems Manager.
- [Oracle Linux](https://docs.aws.amazon.com/systems-manager/latest/userguide/agent-install-oracle.html): Connect to an Oracle Linux instance and install SSM Agent on each instance that will run commands using Systems Manager.

### [RHEL](https://docs.aws.amazon.com/systems-manager/latest/userguide/agent-install-rhel.html)

Connect to a Red Hat Enterprise Linux instance and install SSM Agent on each instance that will run commands using Systems Manager.

- [Versions 8.x, 9.x, and 10.x](https://docs.aws.amazon.com/systems-manager/latest/userguide/agent-install-rhel-8-9.html): Install SSM Agent on RHEL 8.x, 9.x, and 10.x
- [Version 7.x](https://docs.aws.amazon.com/systems-manager/latest/userguide/agent-install-rhel-7.html): Install SSM Agent on RHEL 7.x
- [Rocky Linux](https://docs.aws.amazon.com/systems-manager/latest/userguide/agent-install-rocky.html): Connect to a Rocky Linux instance and install SSM Agent on each instance that will run commands using Systems Manager.
- [SUSE Linux Enterprise Server](https://docs.aws.amazon.com/systems-manager/latest/userguide/agent-install-sles.html): Connect to an SUSE Linux Enterprise Server (SLES) instance and install the SSM Agent on each instance that will run commands using Systems Manager.

### [Ubuntu Server](https://docs.aws.amazon.com/systems-manager/latest/userguide/agent-install-ubuntu.html)

Connect to an Ubuntu Server instance and install SSM Agent on each instance that will run commands using Systems Manager.

- [Versions 16.04 LTS 64-bit (Snap), 18.04, 20.04, 22.04 LTS, 23.10, 24.04 LTS, 24.0, and 25.04](https://docs.aws.amazon.com/systems-manager/latest/userguide/agent-install-ubuntu-64-snap.html): Install SSM Agent on Ubuntu Server 16.04 LTS 64-bit (Snap), 18.04, 20.04, 22.04 LTS, 23.10, 24.04 LTS, 24.0, and 25.04
- [Versions 16.04 and 14.04 64-bit (deb)](https://docs.aws.amazon.com/systems-manager/latest/userguide/agent-install-ubuntu-64-deb.html): Install SSM Agent on Ubuntu Server 16.0464-bit (deb)
- [Versions 16.04 and 14.04 32-bit](https://docs.aws.amazon.com/systems-manager/latest/userguide/agent-install-ubuntu-32.html): Install SSM Agent on Ubuntu Server 16.04 32-bit
- [Determining the correct SSM Agent version to install on 64-bit Ubuntu Server 16.04 instances](https://docs.aws.amazon.com/systems-manager/latest/userguide/agent-install-ubuntu-about-v16.html): Learn how to determine which SSM Agent version to install on Ubuntu Server 16.04 64-bit Amazon EC2 instances
- [Configuring SSM Agent to use a proxy on Linux nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/configure-proxy-ssm-agent.html): Configuring SSM Agent to communicate through an HTTP proxy by creating an override configuration file in either upstart or systemd environments.

### [Working with SSM Agent on EC2 instances for macOS](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent-macos.html)

Install, configure, or uninstall SSM Agent for macOS.

### [Manually installing and uninstalling SSM Agent on EC2 instances for macOS](https://docs.aws.amazon.com/systems-manager/latest/userguide/manually-install-ssm-agent-macos.html)

Connect to an macOS instance and install SSM Agent on each instance that will run commands using Systems Manager.

- [Uninstall SSM Agent from macOS instances](https://docs.aws.amazon.com/systems-manager/latest/userguide/uninstall-ssm-agent-macos.html): Uninstall SSM Agent from an EC2 instance for macOS by using an AWS managed script.

### [Working with SSM Agent on EC2 instances for Windows Server](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent-windows.html)

Download and install the latest version of SSM Agent to each of your EC2 instances or non-EC2 machines that are configured for Systems Manager.

- [Manually installing and uninstalling SSM Agent on EC2 instances for Windows Server](https://docs.aws.amazon.com/systems-manager/latest/userguide/manually-install-ssm-agent-windows.html): Manually install or uninstall SSM Agent on EC2 instances for Windows Server.
- [Configure SSM Agent to use a proxy for Windows Server instances](https://docs.aws.amazon.com/systems-manager/latest/userguide/configure-proxy-ssm-agent-windows.html): Configure SSM Agent to use a proxy for Windows Server instances created on or after November 2016 that don't use the Nano installation option.
- [Checking SSM Agent status and starting the agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent-status-and-restart.html): Check whether SSM Agent is running on each supported operating system, and use the correct command to start the agent if it isn't running.
- [Checking the SSM Agent version number](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent-get-version.html): Check the currently installed SSM Agent version on your managed nodes.
- [Viewing SSM Agent logs](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent-logs.html): View log files about commands, scheduled actions, errors, and health status by manually connecting to a managed node or by automatically sending logs to CloudWatch Logs.
- [Restricting access to root-level commands through SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent-restrict-root-level-commands.html): Elevate your security posture by restricting access to commands using IAM.
- [Automating updates to SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent-automatic-updates.html): Automate the process of updating SSM Agent so you can use its new capabilities or benefit from its updated capabilities.
- [Subscribing to SSM Agent notifications](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent-subscribe-notifications.html): Get notifications when new versions of SSM Agent are released by using Amazon SNS.
- [Troubleshooting SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/troubleshooting-ssm-agent.html): View SSM Agent log files and troubleshoot the agent.


## [Security](https://docs.aws.amazon.com/systems-manager/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/systems-manager/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Systems Manager.
- [Data perimeters](https://docs.aws.amazon.com/systems-manager/latest/userguide/data-perimeters.html): Learn about AWS service-owned resources that Systems Manager accesses and how to configure data perimeter policies.

### [Identity and access management](https://docs.aws.amazon.com/systems-manager/latest/userguide/security-iam.html)

Learn how to authenticate requests and manage access to your Systems Manager resources.

- [How AWS Systems Manager works with IAM](https://docs.aws.amazon.com/systems-manager/latest/userguide/security_iam_service-with-iam.html): Discover what IAM features are available to use with Systems Manager.

### [Identity-based policy examples](https://docs.aws.amazon.com/systems-manager/latest/userguide/security_iam_id-based-policy-examples.html)

Learn how to grant IAM users and roles permission to create or modify Systems Manager resources and perform tasks using the AWS CLI, or API, or console.

- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/systems-manager/latest/userguide/cross-service-confused-deputy-prevention.html): Learn how to avoid the confused deputy problem in AWS Systems Manager.
- [AWS managed policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Systems Manager and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/systems-manager/latest/userguide/security_iam_troubleshoot.html): Learn how to fix common issues that you might encounter when working with Systems Manager and IAM.

### [Using service-linked roles](https://docs.aws.amazon.com/systems-manager/latest/userguide/using-service-linked-roles.html)

Discover how to use service-linked roles to give Systems Manager access to resources in your AWS account.

- [Inventory and Explorer data role](https://docs.aws.amazon.com/systems-manager/latest/userguide/using-service-linked-roles-service-action-1.html): Learn how to use service-linked roles to give permissions to Inventory and Explorer that are required to call other AWS services on your behalf.
- [OpsCenter and Explorer account discovery role](https://docs.aws.amazon.com/systems-manager/latest/userguide/using-service-linked-roles-service-action-2.html): Learn how to use the OpsCenter and Explorer account discovery role for OpsCenter and Explorer to call other AWS services on your behalf.
- [OpsData and OpsItems creation role](https://docs.aws.amazon.com/systems-manager/latest/userguide/using-service-linked-roles-service-action-3.html): Learn how to use the service-linked role AWSServiceRoleForSystemsManagerOpsDataSync to give Systems Manager access to resources in your AWS account.
- [Operational insights creation role](https://docs.aws.amazon.com/systems-manager/latest/userguide/using-service-linked-roles-service-action-4.html): Learn how to use the service-linked role AWSServiceRoleForAmazonSSM_OpsInsights so that OpsCenter operational insights can create and update OpsItems on your behalf.
- [Quick Setup deployment health-check role](https://docs.aws.amazon.com/systems-manager/latest/userguide/using-service-linked-roles-service-action-5.html): Learn how to use the service-linked role AWSServiceRoleForSSMQuickSetup to enable Quick Setup to check the health of deployed configurations and remediate instances that have drifted from the original configuration.
- [Export OpsData service role](https://docs.aws.amazon.com/systems-manager/latest/userguide/using-service-linked-roles-service-action-6.html): Learn how to use the AmazonSSMExplorerExportRole service-linked role so that Systems Manager Explorer can export operations data to an Amazon S3 bucket on your behalf.
- [Just-in-time node access service role](https://docs.aws.amazon.com/systems-manager/latest/userguide/using-service-linked-roles-service-action-8.html): Learn how to use the service-linked role AWSServiceRoleForSystemsManagerJustInTimeAccess to give Systems Manager access to resources in your AWS account.
- [Just-in-time node access request notifications service role](https://docs.aws.amazon.com/systems-manager/latest/userguide/using-service-linked-roles-service-action-9.html): Learn how to use the service-linked role AWSServiceRoleForSystemsManagerNotifications to give Systems Manager access to resources in your AWS account.
- [Logging and monitoring](https://docs.aws.amazon.com/systems-manager/latest/userguide/logging-and-monitoring.html): Discover how to monitor resources and respond to incidents with different Systems Manager tools.
- [Compliance validation](https://docs.aws.amazon.com/systems-manager/latest/userguide/compliance-validation.html): Learn about AWS Systems Manager compliance with third-party assurance programs.
- [Resilience](https://docs.aws.amazon.com/systems-manager/latest/userguide/disaster-recovery-resiliency.html): Learn about AWS Regions, which provide multiple physically separated and isolated Availability Zones (AZs).
- [Infrastructure security](https://docs.aws.amazon.com/systems-manager/latest/userguide/infrastructure-security.html): Learn about Systems Manager protection by AWS global network security procedures.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/systems-manager/latest/userguide/vulnerability-analysis-and-management.html): Discover information about how AWS handles basic security tasks such as firewall configuration and disaster recovery.
- [Security best practices](https://docs.aws.amazon.com/systems-manager/latest/userguide/security-best-practices.html): Learn how to use recommended best practices for security features as you develop and implement your own security policies for Systems Manager.


## [Code examples](https://docs.aws.amazon.com/systems-manager/latest/userguide/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/systems-manager/latest/userguide/service_code_examples_basics.html)

The following code examples show how to use the basics of Systems Manager with AWS SDKs.

- [Hello Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_Hello_section.html): Hello Systems Manager
- [Learn the basics](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_Scenario_section.html): Learn the basics of Systems Manager with an AWS SDK

### [Actions](https://docs.aws.amazon.com/systems-manager/latest/userguide/service_code_examples_actions.html)

The following code examples show how to use Systems Manager with AWS SDKs.

- [AddTagsToResource](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_AddTagsToResource_section.html): Use AddTagsToResource with a CLI
- [CancelCommand](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_CancelCommand_section.html): Use CancelCommand with a CLI
- [CreateActivation](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_CreateActivation_section.html): Use CreateActivation with a CLI
- [CreateAssociation](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_CreateAssociation_section.html): Use CreateAssociation with a CLI
- [CreateAssociationBatch](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_CreateAssociationBatch_section.html): Use CreateAssociationBatch with a CLI
- [CreateDocument](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_CreateDocument_section.html): Use CreateDocument with an AWS SDK or CLI
- [CreateMaintenanceWindow](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_CreateMaintenanceWindow_section.html): Use CreateMaintenanceWindow with an AWS SDK or CLI
- [CreateOpsItem](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_CreateOpsItem_section.html): Use CreateOpsItem with an AWS SDK or CLI
- [CreatePatchBaseline](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_CreatePatchBaseline_section.html): Use CreatePatchBaseline with a CLI
- [DeleteActivation](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DeleteActivation_section.html): Use DeleteActivation with a CLI
- [DeleteAssociation](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DeleteAssociation_section.html): Use DeleteAssociation with a CLI
- [DeleteDocument](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DeleteDocument_section.html): Use DeleteDocument with an AWS SDK or CLI
- [DeleteMaintenanceWindow](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DeleteMaintenanceWindow_section.html): Use DeleteMaintenanceWindow with an AWS SDK or CLI
- [DeleteOpsItem](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DeleteOpsItem_section.html): Use DeleteOpsItem with an AWS SDK
- [DeleteParameter](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DeleteParameter_section.html): Use DeleteParameter with a CLI
- [DeletePatchBaseline](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DeletePatchBaseline_section.html): Use DeletePatchBaseline with a CLI
- [DeregisterManagedInstance](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DeregisterManagedInstance_section.html): Use DeregisterManagedInstance with a CLI
- [DeregisterPatchBaselineForPatchGroup](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DeregisterPatchBaselineForPatchGroup_section.html): Use DeregisterPatchBaselineForPatchGroup with a CLI
- [DeregisterTargetFromMaintenanceWindow](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DeregisterTargetFromMaintenanceWindow_section.html): Use DeregisterTargetFromMaintenanceWindow with a CLI
- [DeregisterTaskFromMaintenanceWindow](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DeregisterTaskFromMaintenanceWindow_section.html): Use DeregisterTaskFromMaintenanceWindow with a CLI
- [DescribeActivations](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribeActivations_section.html): Use DescribeActivations with a CLI
- [DescribeAssociation](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribeAssociation_section.html): Use DescribeAssociation with a CLI
- [DescribeAssociationExecutionTargets](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribeAssociationExecutionTargets_section.html): Use DescribeAssociationExecutionTargets with a CLI
- [DescribeAssociationExecutions](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribeAssociationExecutions_section.html): Use DescribeAssociationExecutions with a CLI
- [DescribeAutomationExecutions](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribeAutomationExecutions_section.html): Use DescribeAutomationExecutions with a CLI
- [DescribeAutomationStepExecutions](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribeAutomationStepExecutions_section.html): Use DescribeAutomationStepExecutions with a CLI
- [DescribeAvailablePatches](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribeAvailablePatches_section.html): Use DescribeAvailablePatches with a CLI
- [DescribeDocument](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribeDocument_section.html): Use DescribeDocument with an AWS SDK or CLI
- [DescribeDocumentPermission](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribeDocumentPermission_section.html): Use DescribeDocumentPermission with a CLI
- [DescribeEffectiveInstanceAssociations](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribeEffectiveInstanceAssociations_section.html): Use DescribeEffectiveInstanceAssociations with a CLI
- [DescribeEffectivePatchesForPatchBaseline](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribeEffectivePatchesForPatchBaseline_section.html): Use DescribeEffectivePatchesForPatchBaseline with a CLI
- [DescribeInstanceAssociationsStatus](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribeInstanceAssociationsStatus_section.html): Use DescribeInstanceAssociationsStatus with a CLI
- [DescribeInstanceInformation](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribeInstanceInformation_section.html): Use DescribeInstanceInformation with a CLI
- [DescribeInstancePatchStates](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribeInstancePatchStates_section.html): Use DescribeInstancePatchStates with a CLI
- [DescribeInstancePatchStatesForPatchGroup](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribeInstancePatchStatesForPatchGroup_section.html): Use DescribeInstancePatchStatesForPatchGroup with a CLI
- [DescribeInstancePatches](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribeInstancePatches_section.html): Use DescribeInstancePatches with a CLI
- [DescribeMaintenanceWindowExecutionTaskInvocations](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribeMaintenanceWindowExecutionTaskInvocations_section.html): Use DescribeMaintenanceWindowExecutionTaskInvocations with a CLI
- [DescribeMaintenanceWindowExecutionTasks](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribeMaintenanceWindowExecutionTasks_section.html): Use DescribeMaintenanceWindowExecutionTasks with a CLI
- [DescribeMaintenanceWindowExecutions](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribeMaintenanceWindowExecutions_section.html): Use DescribeMaintenanceWindowExecutions with a CLI
- [DescribeMaintenanceWindowTargets](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribeMaintenanceWindowTargets_section.html): Use DescribeMaintenanceWindowTargets with a CLI
- [DescribeMaintenanceWindowTasks](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribeMaintenanceWindowTasks_section.html): Use DescribeMaintenanceWindowTasks with a CLI
- [DescribeMaintenanceWindows](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribeMaintenanceWindows_section.html): Use DescribeMaintenanceWindows with a CLI
- [DescribeOpsItems](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribeOpsItems_section.html): Use DescribeOpsItems with an AWS SDK or CLI
- [DescribeParameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribeParameters_section.html): Use DescribeParameters with an AWS SDK or CLI
- [DescribePatchBaselines](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribePatchBaselines_section.html): Use DescribePatchBaselines with a CLI
- [DescribePatchGroupState](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribePatchGroupState_section.html): Use DescribePatchGroupState with a CLI
- [DescribePatchGroups](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_DescribePatchGroups_section.html): Use DescribePatchGroups with a CLI
- [GetAutomationExecution](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_GetAutomationExecution_section.html): Use GetAutomationExecution with a CLI
- [GetCommandInvocation](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_GetCommandInvocation_section.html): Use GetCommandInvocation with a CLI
- [GetConnectionStatus](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_GetConnectionStatus_section.html): Use GetConnectionStatus with a CLI
- [GetDefaultPatchBaseline](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_GetDefaultPatchBaseline_section.html): Use GetDefaultPatchBaseline with a CLI
- [GetDeployablePatchSnapshotForInstance](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_GetDeployablePatchSnapshotForInstance_section.html): Use GetDeployablePatchSnapshotForInstance with a CLI
- [GetDocument](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_GetDocument_section.html): Use GetDocument with a CLI
- [GetInventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_GetInventory_section.html): Use GetInventory with a CLI
- [GetInventorySchema](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_GetInventorySchema_section.html): Use GetInventorySchema with a CLI
- [GetMaintenanceWindow](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_GetMaintenanceWindow_section.html): Use GetMaintenanceWindow with a CLI
- [GetMaintenanceWindowExecution](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_GetMaintenanceWindowExecution_section.html): Use GetMaintenanceWindowExecution with a CLI
- [GetMaintenanceWindowExecutionTask](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_GetMaintenanceWindowExecutionTask_section.html): Use GetMaintenanceWindowExecutionTask with a CLI
- [GetParameter](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_GetParameter_section.html): Use GetParameter with an AWS SDK or CLI
- [GetParameterHistory](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_GetParameterHistory_section.html): Use GetParameterHistory with a CLI
- [GetParameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_GetParameters_section.html): Use GetParameters with a CLI
- [GetPatchBaseline](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_GetPatchBaseline_section.html): Use GetPatchBaseline with a CLI
- [GetPatchBaselineForPatchGroup](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_GetPatchBaselineForPatchGroup_section.html): Use GetPatchBaselineForPatchGroup with a CLI
- [ListAssociationVersions](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_ListAssociationVersions_section.html): Use ListAssociationVersions with a CLI
- [ListAssociations](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_ListAssociations_section.html): Use ListAssociations with a CLI
- [ListCommandInvocations](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_ListCommandInvocations_section.html): Use ListCommandInvocations with an AWS SDK or CLI
- [ListCommands](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_ListCommands_section.html): Use ListCommands with a CLI
- [ListComplianceItems](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_ListComplianceItems_section.html): Use ListComplianceItems with a CLI
- [ListComplianceSummaries](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_ListComplianceSummaries_section.html): Use ListComplianceSummaries with a CLI
- [ListDocumentVersions](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_ListDocumentVersions_section.html): Use ListDocumentVersions with a CLI
- [ListDocuments](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_ListDocuments_section.html): Use ListDocuments with a CLI
- [ListInventoryEntries](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_ListInventoryEntries_section.html): Use ListInventoryEntries with a CLI
- [ListResourceComplianceSummaries](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_ListResourceComplianceSummaries_section.html): Use ListResourceComplianceSummaries with a CLI
- [ListTagsForResource](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_ListTagsForResource_section.html): Use ListTagsForResource with a CLI
- [ModifyDocumentPermission](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_ModifyDocumentPermission_section.html): Use ModifyDocumentPermission with a CLI
- [PutComplianceItems](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_PutComplianceItems_section.html): Use PutComplianceItems with a CLI
- [PutInventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_PutInventory_section.html): Use PutInventory with a CLI
- [PutParameter](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_PutParameter_section.html): Use PutParameter with an AWS SDK or CLI
- [RegisterDefaultPatchBaseline](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_RegisterDefaultPatchBaseline_section.html): Use RegisterDefaultPatchBaseline with a CLI
- [RegisterPatchBaselineForPatchGroup](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_RegisterPatchBaselineForPatchGroup_section.html): Use RegisterPatchBaselineForPatchGroup with a CLI
- [RegisterTargetWithMaintenanceWindow](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_RegisterTargetWithMaintenanceWindow_section.html): Use RegisterTargetWithMaintenanceWindow with a CLI
- [RegisterTaskWithMaintenanceWindow](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_RegisterTaskWithMaintenanceWindow_section.html): Use RegisterTaskWithMaintenanceWindow with a CLI
- [RemoveTagsFromResource](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_RemoveTagsFromResource_section.html): Use RemoveTagsFromResource with a CLI
- [SendCommand](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_SendCommand_section.html): Use SendCommand with an AWS SDK or CLI
- [StartAutomationExecution](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_StartAutomationExecution_section.html): Use StartAutomationExecution with a CLI
- [StartSession](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_StartSession_section.html): Use StartSession with a CLI
- [StopAutomationExecution](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_StopAutomationExecution_section.html): Use StopAutomationExecution with a CLI
- [UpdateAssociation](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_UpdateAssociation_section.html): Use UpdateAssociation with a CLI
- [UpdateAssociationStatus](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_UpdateAssociationStatus_section.html): Use UpdateAssociationStatus with a CLI
- [UpdateDocument](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_UpdateDocument_section.html): Use UpdateDocument with a CLI
- [UpdateDocumentDefaultVersion](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_UpdateDocumentDefaultVersion_section.html): Use UpdateDocumentDefaultVersion with a CLI
- [UpdateMaintenanceWindow](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_UpdateMaintenanceWindow_section.html): Use UpdateMaintenanceWindow with an AWS SDK or CLI
- [UpdateManagedInstanceRole](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_UpdateManagedInstanceRole_section.html): Use UpdateManagedInstanceRole with a CLI
- [UpdateOpsItem](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_UpdateOpsItem_section.html): Use UpdateOpsItem with an AWS SDK or CLI
- [UpdatePatchBaseline](https://docs.aws.amazon.com/systems-manager/latest/userguide/example_ssm_UpdatePatchBaseline_section.html): Use UpdatePatchBaseline with a CLI


## [Logging and monitoring](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring.html)

- [Sending node logs to unified CloudWatch Logs (CloudWatch agent)](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-cloudwatch-agent.html): Learn how to configure and use the CloudWatch agent to collect metrics and logs from your nodes in addition to those supplied by SSM Agent.
- [Sending SSM Agent logs to CloudWatch Logs](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-ssm-agent.html): Learn how to configure SSM Agent to send logs to CloudWatch.
- [Monitoring your change request events](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-change-request-events.html): Learn how to monitor change request event activity in Systems Manager using AWS CloudTrail Lake.
- [Monitoring your automations](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-automation-metrics.html): Learn how to monitor Automation usage in Systems Manager with CloudWatch.
- [Monitoring Run Command metrics using Amazon CloudWatch](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-cloudwatch-metrics.html): Learn how to set alarms based on metrics about the status of Run Command commands using CloudWatch.
- [Logging AWS Systems Manager API calls with AWS CloudTrail](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-cloudtrail-logs.html): Learn how to log Systems Manager API calls with CloudTrail to provide a record of actions taken by a user, a role, or an AWS service in Systems Manager.
- [Logging Automation action output with CloudWatch Logs](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-logging.html): Discover how to log the output from your Systems Manager executeScript Automation actions in Amazon CloudWatch Logs.
- [Configuring Amazon CloudWatch Logs for Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-rc-setting-up-cwlogs.html): Discover how to specify the command output location when you send a command using Run Command, a tool in AWS Systems Manager.

### [Monitoring with Amazon EventBridge](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-eventbridge-events.html)

Learn how to monitor events in AWS Systems Manager by using EventBridge.

- [Configuring EventBridge for Systems Manager events](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-systems-manager-events.html): Learn how to use EventBridge to perform a target event in Systems Manager when statuses changes, state changes, or other conditions occur.
- [Amazon EventBridge event examples for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-systems-manager-event-examples.html): Learn about supported EventBridge events for Systems Manager by viewing JSON format examples.
- [Sample scenarios: Systems Manager targets in Amazon EventBridge rules](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-systems-manager-targets.html): Learn about situations where you might want to add a supported Systems Manager target to an EventBridge rule by reviewing sample scenarios.

### [Monitoring Systems Manager status changes using Amazon SNS notifications](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-sns-notifications.html)

Discover how to receive email notifications from Amazon SNS when a command sent with Run Command or Maintenance Windows changes status.

- [Example Amazon SNS notifications for AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-sns-examples.html): Learn how to configure Amazon SNS to send notifications about the status of commands sent by using Run Command or Maintenance Windows, tools in AWS Systems Manager.
- [Use Run Command to send a command that returns status notifications](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-sns-rc-send.html): Learn how to use the AWS CLI or Systems Manager console to send a command through Run Command that is configured to return status notifications.
- [Use a maintenance window to send a command that returns status notifications](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-sns-mw-register.html): Learn how to register a Run Command task with your maintenance window to return status notifications by using the Systems Manager console or the AWS CLI.


## [Product and service integrations](https://docs.aws.amazon.com/systems-manager/latest/userguide/integrations.html)

### [Integration with AWS services](https://docs.aws.amazon.com/systems-manager/latest/userguide/integrations-aws.html)

Learn how to use Command and Automation-type SSM documents to integrate Systems Manager with AWS services.

- [Running scripts from Amazon S3](https://docs.aws.amazon.com/systems-manager/latest/userguide/integration-s3.html): Discover how to download and run scripts from Amazon S3âincluding Ansible Playbooks, Python, Ruby, Shell, and PowerShellâfor Run Command operations.
- [Referencing AWS Secrets Manager secrets from Parameter Store parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/integration-ps-secretsmanager.html): Learn how to retrieve Secrets Manager secrets when using other AWS services that already support references to Parameter Store parameters.
- [AWS KMS encryption for Parameter Store SecureString parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/secure-string-parameter-kms-encryption.html): Learn how AWS Systems ManagerÂ Parameter Store uses AWS KMS to encrypt the values of Parameter Store SecureString parameters.

### [Use AWS Secrets Manager secrets in Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/systems-manager/latest/userguide/integrate_eks.html)

Learn about different approaches to integrate AWS Systems Manager parameters with Amazon EKS and when to use each method.

- [Install ASCP for Amazon EKS](https://docs.aws.amazon.com/systems-manager/latest/userguide/ascp-eks-installation.html): Learn how to install and configure AWS Secrets and Configuration Provider for Amazon Elastic Kubernetes Service to use with parameters in AWS Systems Manager.
- [Integrate ASCP with Pod Identity for Amazon EKS](https://docs.aws.amazon.com/systems-manager/latest/userguide/ascp-pod-identity-integration.html): Learn how to retrieve parameters from Parameter Store to use in your Amazon EKS Pods using Pod Identity.
- [Integrate ASCP with IRSA for Amazon EKS](https://docs.aws.amazon.com/systems-manager/latest/userguide/integrating_ascp_irsa.html): Learn how to retrieve parameters from Parameter Store to use in your Amazon EKS Pods.
- [ASCP examples](https://docs.aws.amazon.com/systems-manager/latest/userguide/ascp-examples.html): Use these code examples to help you integrate ASCP with your Amazon EKS clusters.
- [Using Parameter Store parameters in AWS Lambda functions](https://docs.aws.amazon.com/systems-manager/latest/userguide/ps-integration-lambda-extensions.html): Learn how to use the AWS Parameters and Secrets Lambda Extension with Parameter Store.

### [Integration with other products and services](https://docs.aws.amazon.com/systems-manager/latest/userguide/integrations-partners.html)

Learn about Systems Manager integrations with other products and services, including Ansible, Chef, GitHub, and Jenkins.

### [Running scripts from GitHub](https://docs.aws.amazon.com/systems-manager/latest/userguide/integration-remote-scripts.html)

Learn how to use the AWS-RunRemoteScript pre-defined SSM document to download scripts from GitHub for Run Command operations.

- [Run Ansible Playbooks from GitHub](https://docs.aws.amazon.com/systems-manager/latest/userguide/integration-github-ansible.html): Learn how to run Ansible Playbooks from GitHub in Run Command by using either the Systems Manager console or the AWS CLI.
- [Run Python scripts from GitHub](https://docs.aws.amazon.com/systems-manager/latest/userguide/integration-github-python.html): Learn how to run Python scripts from GitHub for Run Command by using either the Systems Manager console or the AWS CLI.
- [Using Chef InSpec profiles with Systems Manager Compliance](https://docs.aws.amazon.com/systems-manager/latest/userguide/integration-chef-inspec.html): Discover how to create a human-readable profile of a security, compliance, or policy requirement and use Systems Manager to run compliance scans.
- [Integrating with ServiceNow](https://docs.aws.amazon.com/systems-manager/latest/userguide/integrations-partners-servicenow.html): Learn how to integrate ServiceNow with Systems Manager.


## [AWS Systems Manager reference](https://docs.aws.amazon.com/systems-manager/latest/userguide/reference.html)

- [Working with AWS SDKs](https://docs.aws.amazon.com/systems-manager/latest/userguide/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.
- [Amazon S3 buckets for patching operations](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-operations-s3-buckets.html): Learn how to identify the appropriate Amazon S3 buckets to provide access to for patching operations in your AWS Regions.
- [EventBridge event patterns and types for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/reference-eventbridge-events.html): Learn about the Systems Manager events that you can include in EventBridge rules.
- [Cron and rate expressions](https://docs.aws.amazon.com/systems-manager/latest/userguide/reference-cron-and-rate-expressions.html): Discover how to specify a schedule for when to run maintenance windows or associations as a time-based entry (cron) or a frequency-based entry (rate).
- [ec2messages, ssmmessages, and other API operations](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-messageAPIs.html): Learn about special API operations used by Systems Manager internal operations.
- [Date and time string formats for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-datetime-strings.html): Learn how to create approved or custom formatted date and time strings to use with Systems Manager API operations.


## [Use cases and best practices](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-best-practices.html)

- [Deleting Systems Manager resources and artifacts](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-best-practices-delete-resources.html): Learn how to delete resources and artifacts created by AWS Systems Manager.
- [Choosing between State Manager and Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/state-manager-vs-maintenance-windows.html): Learn how to choose between State Manager and Maintenance Windows to perform updates on your managed nodes based on best practice recommendations.
