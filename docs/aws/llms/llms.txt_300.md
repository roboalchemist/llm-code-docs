# Source: https://docs.aws.amazon.com/directoryservice/latest/admin-guide/llms.txt

# AWS Directory Service Administration Guide

> AWS Directory Service is a directory as a service that provides the capabilities of an enterprise directory with the accessibility and security of the AWS cloud.

- [What is AWS Directory Service?](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html)
- [Service level agreement](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/sla.html)
- [Region availability](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/regions.html)
- [Browser compatibility](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/compatibility.html)
- [Document history](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/document_history.html)

## [AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html)

### [AWS Managed Microsoft AD (Hybrid Edition)](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/aws-hybrid-directory.html)

Learn how AWS hybrid directory connects your self-managed (on-premises) Active Directory with Directory Service to provide seamless identity management across environments.

- [Hybrid directory prerequisites](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/create_hybrid_directory_prereqs.html): Learn how to extend your self-managed AD
- [Creating a hybrid directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/hybrid_directory_create.html): Learn more about creating a hybrid directory and how to extend your self-managed AD
- [Viewing and editing a hybrid directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/hybrid_directory_view_and_edit.html): View and edit your hybrid directory in the Directory Service console.
- [Deleting a hybrid directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/hybrid_directory_delete.html): Learn more about deleting your hybrid directory in the AWS Management Console.

### [Directory assessments](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/hybrid_directory_assessment.html)

You can create, view, and delete directory assessments for your hybrid directory in the AWS Management Console.

- [Creating directory assessments](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/create_directory_assessment.html): You can create a directory assessment to verify your self-managed Active Directory environment meets hybrid directory requirements.
- [Viewing directory assessments](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/viewing_hybrid_dir_assessment.html): You can view directory assessment results to review test outcomes and identify configuration issues.
- [Deleting directory assessments](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/deleting_hybrid_dir_assessment.html): You can delete customer-created directory assessments that are no longer needed.

### [Troubleshooting](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/hybrid_directory_troubleshooting.html)

Learn how to troubleshoot hybrid directory and directory assessment problems.

- [Directory Status Errors](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/hybrid_directory_status_errors.html): Learn how to troubleshoot hybrid directory status errors
- [Directory Assessment Error Messages](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/da-error-msgs.html): Learn more about the directory assessment error messages, what they mean and how to resolve them.
- [Assessment Test error messages](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/assessment_test_error-msgs.html): Error messages that indicate blocking issues during hybrid directory assessment tests.
- [Assessment Test warning messages](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/assessment_test_warning-msgs.html): Warning messages that may occur during assessment tests.

### [Getting started](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started.html)

Learn about the prerequisites for AWS Managed Microsoft AD and how to create a AWS Managed Microsoft AD Active Directory.

- [What gets created with your AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started_what_gets_created.html): Learn about the security groups, inbound, and outbound rules that are created along with your AWS Managed Microsoft AD.
- [Administrator account and group permissions](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started_admin_account.html): Learn about the permissions granted to the AWS Managed Microsoft AD administrator account and group, AWS Domain Administrator, and enterprise privileged accounts.

### [Key concepts and best practices](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_key_concepts_best_practices.html)

Learn more about AWS Managed Microsoft AD key concepts and best practices.

- [Key concepts](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_key_concepts.html): Learn more about how AWS Managed Microsoft AD works.
- [Best practices](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_best_practices.html): Follow best practices to avoid problems and get the most out of AWS Managed Microsoft AD.

### [Use cases](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_use_cases.html)

Use AWS Managed Microsoft AD for various business use cases.

- [Use Case 1: Sign in to AWS applications and services with Active Directory credentials](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/usecase1.html): Learn more about how you can use AWS Managed Microsoft AD to sign in to AWS applications and services.
- [Use Case 2: Manage Amazon EC2 instances](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/usecase2.html): Learn more about how you can use AWS Managed Microsoft AD to manage Amazon EC2.
- [Use Case 3: Provide directory services to your Active Directory-aware workloads](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/usecase3.html): Learn more about how you can use AWS Managed Microsoft AD to provide directory services to your Active Directory-aware workloads.
- [Use Case 4: AWS IAM Identity Center to Office 365 and other cloud applications](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/usecase4.html): Learn more about how you can use AWS Managed Microsoft AD to provide AWS IAM Identity Center services for cloud applications.
- [Use Case 5: Extend your on-premises Active Directory to the AWS Cloud](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/usecase5.html): Learn more about how you can use AWS Managed Microsoft AD to extend your on-premises Active Directory to the AWS Cloud.
- [Use Case 6: Share your directory to seamlessly join Amazon EC2 instances to a domain across AWS accounts](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/usecase6.html): Learn more about how you can use AWS Managed Microsoft AD to share your directory to seamlessly joined Amazon EC2 instances to a domain across AWS accounts.

### [Maintain your directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_maintain.html)

Learn how to maintain day-to-day administrative tasks for your AWS Managed Microsoft AD.

- [Viewing directory information](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_view_directory_info.html): Learn how to view details about your AWS Managed Microsoft AD directory.
- [Restoring your directory with snapshots](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_snapshots.html): Learn more about daily and manual snapshots for your AWS Managed Microsoft AD Active Directory.
- [Deploying additional domain controllers](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_deploy_additional_dcs.html): Learn how to improve redundancy, resilience, and availability by deploying additional domain controllers for your AWS Managed Microsoft AD.
- [Upgrading your AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_upgrade_edition.html): Learn how to upgrade your Standard edition of AWS Managed Microsoft AD to Enterprise edition and about the limitations that occur with an upgrade.
- [Updating directory network type](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_update-directory-type.html): Update an Directory Service directory's network type from IPv4 to Dual-stack (IPv4 and IPv6) to provide a larger address space.
- [Adding alternate UPN suffixes](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_upn_suffixes.html): Learn how to add an alternative user principal name (UPN) for your AWS Managed Microsoft AD.
- [Renaming your directory's site name](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_rename_site.html): Learn how to rename your AWS Managed Microsoft AD directory' site name.
- [Deleting your AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_delete.html): Learn how to delete a AWS Managed Microsoft AD.

### [Secure your directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_security.html)

Learn more about how you can secure your AWS Managed Microsoft AD.

### [Understanding password policies](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_password_policies.html)

Learn more about the password and account lockout policies for your AWS Managed Microsoft AD users and groups.

- [Assigning password policies to your users](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/assignpasswordpolicies.html): Learn how to assign password policies to your AWS Managed Microsoft AD users
- [Delegating who can manage your password policies](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/delegatepasswordpolicies.html): Learn how to delegate permissions to manage your AWS Managed Microsoft AD password policy.
- [Enabling multi-factor authentication](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_mfa.html): You can enable multi-factor authentication (MFA) for your AWS Managed Microsoft AD directory to increase security when your users specify their AD credentials to access Supported Amazon Enterprise applications.

### [Enable Secure LDAP or LDAPS](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_ldap.html)

For greater security, enable LDAP over Secure Sockets Layer (SSL)/Transport Layer Security (TLS) in AWS Directory Service.

- [Enabling server-side LDAPS](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_ldap_server_side.html): Use server-side Lightweight Directory Access Protocol Secure Sockets Layer (SSL)/Transport Layer Security (TLS) (LDAPS) to encrypt all communications between your LDAP-enabled applications and AWS Managed Microsoft AD directory.
- [Enabling client-side LDAPS](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_ldap_client_side.html): Use client-side Lightweight Directory Access Protocol Secure Sockets Layer (SSL)/Transport Layer Security (TLS) (LDAPS) to encrypt all communications between your self-managed Microsoft Active Directory (AD) and your AWS enterprise applications.
- [Manage compliance for your directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_compliance.html): Understand how AWS Managed Microsoft AD can be configured for full PCI and HIPAA compliance.
- [Enhancing network security](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_network_security.html): Learn how to secure your AWS Managed Microsoft AD network by modifying the AWS Security Group.
- [Editing directory security settings](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_directory_settings.html): Learn how you can edit AWS Managed Microsoft AD directory security settings and resolve failed settings update.
- [Enable Public Key Cryptography for Initial Authentication (PKINIT)](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_map_altsecurityidentity.html): Learn how to enable the AltSecurityIdentity attribute on your Active Directory object to enable secure certificate-based authentication with AWS Managed Microsoft AD.
- [Set up AWS Private CA Connector for AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_pca_connector.html): Learn how to set up AWS Private Certificate Authority for your AWS Managed Microsoft AD

### [Monitor your directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_monitor.html)

Learn more about tasks to monitor your AWS Managed Microsoft AD.

- [Understanding your directory status](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_directory_status.html): Learn more about what your AWS Managed Microsoft AD directory status means.
- [Enabling directory status notifications with Amazon SNS](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_enable_notifications.html): Learn how to configure Amazon SNS for AWS Managed Microsoft AD Active Directory.
- [Understanding your directory logs](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_directory_logs.html): Learn more about the security logs for your AWS Managed Microsoft AD.
- [Enabling Amazon CloudWatch log forwarding](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_enable_log_forwarding.html): Learn how to use Amazon CloudWatch Logs to monitor your AWS Managed Microsoft AD.
- [Using CloudWatch to monitor your directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_monitor_dc_performance.html): Learn how you can use Amazon CloudWatch to monitor your AWS Managed Microsoft AD domain controllers performance.
- [Disabling Amazon CloudWatch log forwarding](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_disable_log_forwarding_with_console.html): You can disable CloudWatch Logs log forwarding for your AWS Managed Microsoft AD in the AWS Management Console.
- [Monitoring DNS Server with Microsoft Event Viewer](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_dns_event_viewer.html): Using Microsoft Event Viewer to troubleshoot DNS in AWS Managed Microsoft AD.

### [Access to AWS applications and services](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_manage_apps_services.html)

Learn how to grant access AWS applications and services from your AWS Managed Microsoft AD.

- [Application compatibility](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_app_compatibility.html): Learn more about which applications are AWS Managed Microsoft AD compatible.
- [Enabling access to AWS applications and services](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_enable_apps_services.html): Enable other AWS applications and services for access to your AWS Managed Microsoft AD directory.
- [Enabling access to the AWS Management Console](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_management_console_access.html): Manage AWS Management Console access for members of your AWS Managed Microsoft AD directory.
- [Creating an access URL](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_create_access_url.html): Learn how to create an access URL for your AWS Managed Microsoft AD
- [Enabling single sign-on](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_single_sign_on.html): Learn how to enable single sign-on access to your AWS Managed Microsoft AD directory users to access Amazon WorkDocs.

### [Granting access to AWS resources](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_manage_roles.html)

Creating and configuring IAM roles for your AWS Managed Microsoft AD users and groups.

- [Creating a new role](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/create_role.html): Learn how to create an IAM for your AWS Managed Microsoft AD users and groups
- [Editing the trust relationship for an existing role](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/edit_trust.html): Learn how to edit the trust relationship for an AWS Managed Microsoft AD IAM role
- [Assigning users or groups to an existing role](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/assign_role.html): Learn how to assign AWS Managed Microsoft AD users and groups to an existing IAM role.
- [Viewing users and groups assigned to a role](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/view_role_details.html): Learn how to view the AWS Managed Microsoft AD users and groups assigned to an IAM role in your AWS Managed Microsoft AD.
- [Removing a user or group from a role](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/remove_role_users.html): Learn how to remove an AWS Managed Microsoft AD user or group from an IAM role
- [Using AWS managed policies](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_managed_policies.html): Directory Service provides the following AWS managed policies to give your users and groups access to AWS services and resources, such as access to the Amazon EC2 console.

### [Configure Multi-Region replication](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_configure_multi_region_replication.html)

Learn more about AWS Managed Microsoft AD's multi-Region replication feature and how it works.

- [Global vs Regional features](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/multi-region-global-region-features.html): Learn more about the differences between global and regional features when using multi-Region replication for AWS Managed Microsoft AD.
- [Primary vs additional Regions](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/multi-region-global-primary-additional.html): Learn more about the differences between primary and additional regions when using multi-Region replication for AWS Managed Microsoft AD
- [Adding a replicated Region](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/multi-region-add-region.html): Learn how to add a replicated Region to your AWS Managed Microsoft AD.
- [Deleting a replicated Region](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/multi-region-delete-region.html): Learn how to delete a replicated Region for your AWS Managed Microsoft AD

### [Share your directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_directory_sharing.html)

Learn how to extend the reach of your AWS Managed Microsoft AD directory across AWS account boundaries.

### [Tutorial: Share your AWS Managed Microsoft AD directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_tutorial_directory_sharing.html)

Learn how to share your AWS Managed Microsoft AD directory.

- [Step 1: Set up your networking environment](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/step1_setup_networking.html): You will need to establish an Amazon VPC peering connection to share your AWS Managed Microsoft AD directory (directory account owner) with another AWS account (directory consumer account).
- [Step 2: Share your directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/step2_share_directory.html): Use the following procedures to begin the directory sharing workflow from within the directory owner account.
- [Step 3: Accept shared directory invite - Optional](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/step3_accept_invite.html): If you chose the Share this directory with other AWS accounts (handshake method) option in the previous procedure, you should use this procedure to finish the shared directory workflow.
- [Step 4: Test seamlessly joining an EC2 instance for Windows Server to a domain](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/step4_test_ec2_access.html): You can use either of the following two methods to test seamlessly joining an EC2 instance to a domain.
- [Unsharing your directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_directory_sharing_unshare.html): Learn how to unshare a shared AWS Managed Microsoft AD.
- [Migrating Active Directory users to AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_migrate_users.html): Learn how to migrate Active Directory users to AWS Managed Microsoft AD

### [Connect your existing Active Directory infrastructure](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_connect_existing_infrastructure.html)

Learn how to configure trust relationships between AWS Managed Microsoft AD and your existing Active Directory infrastructure.

- [Creating a trust relationship](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_setup_trust.html): Learn how to create a trust relationship between your AWS Managed Microsoft AD and self-managed Active Directory.
- [Adding IP routes](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_adding_routes.html): Learn how to add required IP routes when using public IP addresses with AWS Managed Microsoft AD

### [Tutorial: Create a trust relationship between your AWS Managed Microsoft AD and your self-managed Active Directory domain](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_tutorial_setup_trust.html)

Learn how to set up a trust relationship with AWS Managed Microsoft AD and your self-managed Active Directory domain.

- [Prerequisites](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/before_you_start.html): This tutorial assumes you already have the following:
- [Step 1: Prepare your self-managed AD Domain](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_tutorial_setup_trust_prepare_onprem.html): Prepare your self-managed domain for a trust relationship with AWS Managed Microsoft AD.
- [Step 2: Prepare your AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_tutorial_setup_trust_prepare_mad.html): Prepare your AWS Managed Microsoft AD for the trust relationship.
- [Step 3: Create the trust relationship](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_tutorial_setup_trust_create.html): Create the trust relationship between your AWS Managed Microsoft AD and your self-managed domain.

### [Tutorial: Create a trust relationship between AWS Managed Microsoft AD domains](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_tutorial_setup_trust_between_2_managed_ad_domains.html)

Follow this step-by-step guide to set up a trust relationship with AWS Managed Microsoft AD.

- [Step 1: Prepare your AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_tutorial_setup_trust_prepare_mad_between_2_managed_ad_domains.html): Prepare your AWS Managed Microsoft AD for the trust relationship.
- [Step 2: Create the trust relationship with another AWS Managed Microsoft AD domain](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_tutorial_setup_trust_create_between_2_managed_ad_domains.html): Create the trust relationship between two AWS Managed Microsoft AD domains.

### [Extend your directory schema](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_schema_extensions.html)

Learn when and how to extend an AWS Managed Microsoft AD schema.

### [Tutorial: Extending your AWS Managed Microsoft AD schema](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_tutorial_extend_schema.html)

Learn how to extend the schema for your AWS Directory Service for Microsoft Active Directory

- [Step 1: Create your LDIF file](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/create.html): Create a LDIF (Lightweight Directory Interchange Format) script file to define the new attributes and any classes that the attributes should be added to.
- [Step 2: Import your LDIF file](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/import.html): Use the Directory Service console to import the LDIF file to your AWS Managed Microsoft AD environment.
- [Step 3: Verify if the schema extension was successful](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/verify.html): Use an EC2 instance to verify that the new extensions appear in the Active Directory Schema Snap-in.
- [Add a value to the new attribute - Optional](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/addvalue.html): Optional step for adding a value to the new attribute.
- [Related resources](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/additional.html): Consult Microsoft resources for working with Active Directory schema and schema extensions.

### [Ways to join an instance to your directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_join_instance.html)

Learn how you can join an Amazon EC2 instance to your AWS Managed Microsoft AD Active Directory domain.

- [Launching a directory administration instance](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/console_instance.html): How to launch a directory administrator EC2 instance in the AWS Management Console with AWS Systems Manager.
- [Joining a Windows instance](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/launching_instance.html): Learn how to join an Amazon EC2 Windows instance to your AWS Managed Microsoft AD.

### [Joining a Linux instance](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/joining_linux_instance.html)

Learn how you can join an Amazon EC2 Linux instance to an AWS Managed Microsoft AD Active Directory

- [Seamlessly joining a Linux instance](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/seamlessly_join_linux_instance.html): Learn how to seamlessly join an Amazon EC2 Linux instance to your AWS Managed Microsoft AD Active Directory.
- [Seamlessly joining a Linux instance to a shared Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/seamlessly_join_linux_to_shared_MAD.html): Learn how to seamlessly join an Amazon EC2 Linux instance to a shared AWS Managed Microsoft AD.
- [Manually joining a Linux instance](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/join_linux_instance.html): Learn how to manually join a Amazon EC2 Linux instance to your AWS Managed Microsoft AD Active Directory after the instance was launched.
- [Manually joining a Linux instance using Winbind](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/join_linux_instance_winbind.html): Learn how to manually join an Amazon EC2 Linux instance to your AWS Managed Microsoft AD Active Directory using Winbind
- [Joining a Mac instance](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/join_mac_instance.html): Learn about the prerequisites for joining an Amazon EC2 Mac instance to your AWS Managed Microsoft AD and how you can join an Amazon EC2 Mac instance to a AWS Managed Microsoft AD Active Directory.
- [Delegating directory join privileges](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_join_privileges.html): Learn how to delegate directory join privileges for AWS Managed Microsoft AD.
- [Creating or changing a DHCP options set](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/dhcp_options_set.html): Learn how to create or change your DHCP options set for your AWS Managed Microsoft AD

### [User and group management](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_manage_users_groups.html)

Learn how to create and manage users and groups in AWS Managed Microsoft AD.

### [Manage users and group with the console, CLI, or PowerShell](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_manage_users_groups_procedures.html)

Learn how to create and manage users and groups in AWS Managed Microsoft AD.

- [Enabling or disabling AWS Directory Service Data](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_users_groups_mgmt_enable_disable.html): Learn about how to enable or disable the AWS Managed Microsoft AD user and group management with AWS Directory Service Data using the AWS Management Console, AWS CLI, or AWS Tools for PowerShell.
- [Creating a user](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_create_user.html): Use the Directory Service Data to create a new user account in AWS Managed Microsoft AD with the AWS Management Console, AWS CLI or AWS Tools for PowerShell.
- [Viewing and updating a user](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_view_update_user.html): Use the AWS Management Console, AWS Directory Service Data CLI, or AWS Tools for PowerShell to view an AWS Managed Microsoft AD user's details.
- [Deleting a user](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_delete_user.html): Use the AWS Management Console or AWS Directory Service Data CLI to delete an AWS Managed Microsoft AD user's account.
- [Disabling a user](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_disable_user.html): Use the AWS Management Console or AWS Directory Service Data CLI to disable an AWS Managed Microsoft AD user's account.
- [Resetting and enabling a user's password](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_reset_user_pswd.html): Learn about how to reset an AWS Managed Microsoft AD user's password to enable their account in the AWS Management Console, AWS CLI, or AWS Tools for PowerShell.
- [Creating a group](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_create_group.html): Learn about how to create an AWS Managed Microsoft AD group in the AWS Management Console or AWS CLI.
- [Viewing and updating a group](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_view_update_group.html): Learn about how to view an AWS Managed Microsoft AD group's details in the AWS Management Console, AWS CLI, or AWS Tools for PowerShell.
- [Deleting a group](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_delete_group.html): Learn about how to delete an AWS Managed Microsoft AD group in the AWS Management Console, AWS CLI, or AWS Tools for PowerShell.
- [Adding and removing members to groups and groups to groups](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_add_remove_user_group.html): Learn how to add an AWS Managed Microsoft AD member to a group and remove a member from a group in the AWS Management Console, AWS CLI, or AWS Tools for PowerShell.
- [Copying a group memberships in the console](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/copy_group_membership.html): Learn about how to copy AWS Managed Microsoft AD groups memberships from one user into another user in the AWS Management Console.

### [Manage users and groups with an Amazon EC2 instance](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_manage_users_groups_ec2.html)

Learn about how to manage users and groups with an Amazon EC2 instance.

- [Installing AD Administration Tools](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_install_ad_tools.html): Learn about the prerequisites for Active Directory Administration Tools and how to install the Active Directory Administration Tools.
- [Creating a user](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_manage_users_groups_create_user.html): Learn how to create an AWS Managed Microsoft AD user with the Active Directory Administration Tools and Windows PowerShell.
- [Delete a user's account with an Amazon EC2 instance](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_manage_users_groups_delete_user.html): Learn about how to delete a user's account
- [Resetting a user password](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_manage_users_groups_reset_password.html): Learn how to reset an AWS Managed Microsoft AD Active Directory user's password with the AWS Management Console, AWS CLI, and PowerShell.
- [Creating a group](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_manage_users_groups_create_group.html): Learn how to create an AWS Managed Microsoft AD group with the Active Directory Administration Tools and Windows PowerShell.
- [Adding a user to a group](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_manage_users_groups_add_user_to_group.html): Learn how to create an AWS Managed Microsoft AD group with the eActive Directory Administration Tools and Windows PowerShell.

### [Directory Service Data](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started_directory_service_data.html)

Learn about AWS Directory Service Data.

- [AWS Directory Service Data attributes](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html): Use Directory Service Data attributes to manage users and groups in the console and AWS Command Line Interface.
- [Group type and group scope](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_group_type_and_scope.html): Learn about AWS Managed Microsoft AD group type and group scope.
- [Connecting to Microsoft Entra Connect Sync](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_connect_ms_entra_sync.html): Learn how to connect your AWS Managed Microsoft AD to Microsoft Entra Connect Sync.

### [AWS Managed Microsoft AD test lab tutorials](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_tutorial_test_lab.html)

Learn more about the steps for the AWS Managed Microsoft AD test lab tutorial where you create a AWS Managed Microsoft AD along with the necessary networking resources like a Amazon VPC, security group, and Amazon EC2 Windows instance.

### [Tutorial: Set up your base AWS Managed Microsoft AD test lab](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_tutorial_test_lab_base.html)

Set up your base test lab for AWS Managed Microsoft AD by creating an Amazon EC2 key pair, two Amazon VPCs, and two security groups.

- [Prerequisites](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/microsoftadbaseprereq.html): Check the prerequisites before you use the AWS CLI or AWS Tools for Windows PowerShell to create your AWS Managed Microsoft AD test lab in Directory Service.
- [Step 1: Set up your AWS environment for AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/microsoftadbasestep1.html): Create Amazon EC2 key pairs, Amazon VPC, and security groups, for your AWS Managed Microsoft AD test environment.
- [Step 2: Create your AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/microsoftadbasestep2.html): Create your AWS Managed Microsoft AD Active Directory as part of the AWS Managed Microsoft AD test lab tutorial.
- [Step 3: Deploy an EC2 instance to manage your AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/microsoftadbasestep3.html): Launch an Amazon EC2 instance to manage your AWS Managed Microsoft AD Active Directory.
- [Step 4: Verify that the base test lab is operational](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/microsoftadbasestep4.html): Verify that your AWS Managed Microsoft AD Active Directory was successfully launched.

### [Tutorial: Create a trust from AWS Managed Microsoft AD to a self-managed AD install on EC2](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_tutorial_test_lab_trust.html)

Set up a trust from AWS Directory Service for Microsoft Active Directory to a new Active Directory forest that you create in Amazon EC2.

- [Step 1: Set up your environment for trusts](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/microsoftadtruststep1.html): Set up your Amazon EC2 environment, deploy your new forest, and prepare your VPC for trusts with AWS.
- [Step 2: Create the trusts](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/microsoftadtruststep2.html): Create two separate forest trusts, one from the Active Directory domain on your EC2 instance and the other from your AWS Managed Microsoft AD in AWS.
- [Step 3: Verify the trust](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/microsoftadtruststep3.html): Test whether the trusts were set up successfully between AWS and Active Directory on Amazon EC2.
- [Quotas](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_limits.html): AWS Managed Microsoft AD has default quotas for resources.

### [Troubleshooting](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_troubleshooting.html)

Learn how to troubleshoot AWS Managed Microsoft AD administration problems.

- [Amazon EC2 Linux instance domain join errors](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_troubleshooting_join_linux.html): Learn how to troubleshoot error messages related to domain joining Amazon EC2 Linux instances with AWS Directory Service for Microsoft Active Directory.
- [Low available storage space](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_troubleshooting_low_storage_space.html): Learn how to troubleshoot AWS Managed Microsoft AD impaired state due to low available storage space.
- [Schema extension errors](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_troubleshooting_schema.html): Learn to troubleshoot error messages related to schema extensions in AWS Directory Service for Microsoft Active Directory.
- [Trust creation status reasons](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_troubleshooting_trusts.html): Consult these status message explanations when AWS Managed Microsoft AD trust creation fails.


## [AD Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_ad_connector.html)

### [Getting started](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_getting_started.html)

Learn more about AD Connector and how it works with your existing Active Directory.

- [What gets created with your AD Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/create_details_ad_connector.html): Learn more about the resources that are created along with your AD Connector.
- [Best practices](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_best_practices.html): Follow best practices to avoid problems and get the most out of AD Connector.

### [Maintain your directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_maintain.html)

Learn how to maintain day-to-day administrative tasks for your AD Connector.

- [Viewing directory information](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_view_directory_info.html): View details about your AD Connector directory.
- [Updating directory network type](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_update-directory-type.html): Update an Directory Service directory's network type from IPv4 to Dual-stack (IPv4 and IPv6) to provide a larger address space.
- [Updating the DNS address for your AD Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_update_dns.html): Learn how to update the DNS addresses that your AD Connector is pointing to in the AWS Management Console.
- [Deleting your AD Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_delete.html): Learn how to delete a AD Connector.

### [Secure your directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_security.html)

Learn more about how you can secure your AD Connector.

- [Enabling multi-factor authentication](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_mfa.html): Learn how to enable MFA for your AD Connector

### [Enabling client-side LDAPS](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_ldap_client_side.html)

Use LDAPS to encrypt all communications between your self-managed Microsoft Active Directory (AD) and your AWS enterprise applications.

- [Managing client-side LDAPS](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/manage-ldap-client-side.html): Learn how to manage client-side LDAPS for your AD Connector.

### [Enabling mTLS authentication](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_clientauth.html)

For greater security, enable mTLS authentication support for smart cards in AWS Directory Service AD Connector.

- [Managing smart card authentication settings](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/manage-clientauth.html): Learn how to manage your AD Connector smart card authentication settings.
- [Updating your AD Connector service account credentials](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_update_creds.html): Learn how to update your AD Connector service account credentials in the AWS Management Console
- [Set up AWS Private CA Connector for AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_pca_connector.html): Learn how to issue and manage certificates for your AD domain-joined users, groups, and machines using AWS Private Certificate Authority with AD Connector.

### [Monitor your directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_monitor.html)

Ways to monitor your AD Connector

- [Understanding your directory status](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_directory_status.html): Learn more about what your AD Connector directory status means.
- [Enabling directory status notifications with Amazon SNS](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_enable_notifications.html): Learn how to configure Amazon SNS for AD Connector.

### [Access to AWS applications and services](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_manage_apps_services.html)

Learn more about the AWS applications and services that can work with AD Connector and how to grant access to them.

- [Application compatibility](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_app_compatibility.html): Learn which applications are compatible with AD Connector.
- [Enabling access to AWS applications and services from AD Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_enable_apps_services.html): Enable other applications and services for access to your AD Connector.
- [Ways to join an Amazon EC2 instance to your Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_join_instance.html): Learn how to launch an Amazon EC2 instance and join it to your Active Directory domain that is connected to AD Connector.
- [Quotas](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_limits.html): AD Connector has default quotas for resources.
- [Troubleshooting](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_troubleshooting.html): Troubleshoot AD Connector like connectivity issue when creating an AD Connector, connecting to an on-premises Active Directory, can't update the Active Directory service account, errors with smart cards, and deleting an AD Connector.


## [Simple AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_simple_ad.html)

### [Getting started](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_getting_started.html)

Learn about the prerequisites for Simple AD and how to create a Simple AD Active Directory.

- [What gets created with your Simple AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_what_gets_created.html): Learn more about what gets created with Simple AD
- [Best practices](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_best_practices.html): Follow best practices to avoid problems and get the most out of Simple AD.

### [Maintain your directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_maintain.html)

Learn how to maintain day-to-day administrative tasks for your Simple AD;.

- [Viewing directory information](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_view_directory_info.html): View details about your Simple AD directory.
- [Updating directory network type](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_update-directory-type.html): Update an Directory Service directory's network type from IPv4 to Dual-stack (IPv4 and IPv6) to provide a larger address space.
- [Configuring DNS servers](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_dns.html): Learn how to configure your DNS servers to work correctly with Simple AD.
- [Restoring your directory with snapshot](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_snapshots.html): Learn more about daily and manual snapshots for your Simple AD Active Directory.
- [Deleting your Simple AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_delete.html): Learn how to delete a Simple AD.
- [Secure your directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_security.html): Learn how you can secure your Simple AD directory.

### [Monitor your directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_monitor.html)

Learn more about tasks to monitor your Simple AD.

- [Understanding your directory status](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_directory_status.html): Learn more about the different types of Simple AD directory status
- [Enabling directory status notifications with Amazon Simple Notification Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_enable_notifications.html): Learn how to configure Amazon SNS for Simple AD Active Directory.

### [Access to AWS applications and services](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_manage_apps_services.html)

Enable other applications and services for access to your Simple AD directory.

- [Application compatibility](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_app_compatibility.html): Learn which applications are compatible with Simple AD.
- [Enabling access to AWS applications and services](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_enable_apps_services.html): Enable other AWS applications and services for access to your Simple AD directory.
- [Enabling access to the AWS Management Console](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_management_console_access.html): Manage console access for members of your Directory Service directory.
- [Creating an access URL](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_create_access_url.html): Learn how to create an access URL for your Simple AD
- [Enabling single sign-on](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_single_sign_on.html): Learn how to enable single sign-on access to your Simple AD directory users to access Amazon WorkDocs.

### [Ways to join an instance to your directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_join_instance.html)

Learn how to launch an Amazon EC2 instance, then join it to your Simple AD Active Directory.

- [Joining a Windows instance](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_launching_instance.html): Learn how to join an Amazon EC2 Windows instance to Simple AD

### [Join Linux instance](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_linux_domain_join.html)

Learn more about domain joining an Amazon EC2 Linux to a Simple AD

- [Seamlessly join Linux instance](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_seamlessly_join_linux_instance.html): Learn how to seamlessly join an Amazon EC2 Linux instance to your Simple AD Active Directory.
- [Manually join a Linux instance](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_join_linux_instance.html): Learn how to manually join a Amazon EC2 Linux instance to your Simple AD Active Directory after the instance was launched.
- [Delegating directory join privileges](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_directory_join_privileges.html): Learn how to delegate directory join privileges for Simple AD.
- [Creating a DHCP options set](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_dhcp_options_set.html): Learn how to create or change your DHCP options set for your Simple AD

### [Users and groups management](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_manage_users_groups.html)

Create and manage users and groups in Simple AD.

- [Installing AD Administration Tools](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_install_ad_tools.html): Learn about the prerequisites for Active Directory Administration Tools and how to install the Active Directory Administration Tools on an Amazon EC2 Windows Server instance.
- [Creating a user](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_manage_users_groups_create_user.html): Learn how to create a Simple AD user with Active Directory Administration Tools.
- [Deleting a user](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_manage_users_groups_delete_user.html): Learn how to delete a Simple AD user with Active Directory Administration Tools.
- [Resetting a user password](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_manage_users_groups_reset_password.html): Learn how to reset a Simple AD Active Directory user's password with the AWS Management Console, and AWS CLI.
- [Creating a group](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_manage_users_groups_create_group.html): Learn how to create a Simple AD group with Active Directory User and Computer tools
- [Adding a user to a group](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_manage_users_groups_add_user_to_group.html): Learn how to add a Simple AD user to a group
- [Quotas](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_limits.html): Simple AD has default quotas for resources.

### [Troubleshooting](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_troubleshooting.html)

Troubleshoot Simple AD administration problems.

- [Troubleshooting directory status messages](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_troubleshooting_reasons.html): Learn more about directory status messages in Simple AD and how to troubleshoot them.


## [Security](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/security.html)

### [Identity and access management](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/iam_auth_access.html)

Create permissions that specify which actions a user or group in your AWS account can perform and on which Directory Service resources.

- [Overview of managing access](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/IAM_Auth_Access_Overview.html): Every AWS resource is owned by an AWS account.
- [AWS managed policies](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/security-iam-awsmanpol.html): Learn about AWS managed policies for Directory Service and recent changes to those policies.
- [Using identity-based policies (IAM policies)](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/IAM_Auth_Access_IdentityBased.html): This topic provides examples of identity-based policies in which an account administrator can attach permissions policies to IAM identities (users, groups, and roles).
- [Directory Service API permissions reference](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html): When you are setting up and writing permissions policies that you can attach to an IAM identity (identity-based policies), you can use the table as a reference.
- [Directory Service Data condition keys](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/iam_dsdata-condition-keys.html): Describes condition keys in AWS Directory Service Data to add granularity to your user and group level access.
- [Authorization for AWS applications and services using Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_manage_apps_services_authorization.html): Authorizes and deauthorizes other applications and services access to your Directory Service directory.
- [Using service-linked roles](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/using-service-linked-roles.html): How to use service-linked roles to give Directory Service access to resources in your AWS account.

### [Logging and monitoring](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/incident-response.html)

Monitor Directory Service by using AWS CloudTrail and Amazon CloudWatch.

- [AWS Directory Service logs](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/logging-using-cloudtrail-ads.html): Learn about logging AWS Directory Service with AWS CloudTrail.
- [AWS Directory Service Data logs](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/logging-using-cloudtrail.html): Learn about logging AWS Directory Service Data with AWS CloudTrail.
- [Compliance validation](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Directory Service features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/infrastructure-security.html): Learn how AWS Directory Service isolates service traffic.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [AWS PrivateLink](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/vpc-interface-endpoints.html): Learn about how you can use an AWS PrivateLink to create a private connection between your VPC and Directory Service/Directory Service Data.
