# Source: https://docs.aws.amazon.com/workmail/latest/adminguide/llms.txt

# Amazon WorkMail Administrator Guide

> Amazon WorkMail is a managed email and calendaring service that offers strong security controls and support for existing desktop and mobile clients.

- [What is Amazon WorkMail?](https://docs.aws.amazon.com/workmail/latest/adminguide/what_is.html)
- [Prerequisites](https://docs.aws.amazon.com/workmail/latest/adminguide/prereqs.html)
- [Exporting mailbox content](https://docs.aws.amazon.com/workmail/latest/adminguide/mail-export.html)
- [Using email journaling with Amazon WorkMail](https://docs.aws.amazon.com/workmail/latest/adminguide/journaling_overview.html)
- [Document history](https://docs.aws.amazon.com/workmail/latest/adminguide/DocumentHistory.html)

## [Security](https://docs.aws.amazon.com/workmail/latest/adminguide/security.html)

- [Data protection](https://docs.aws.amazon.com/workmail/latest/adminguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Amazon WorkMail.

### [Identity and access management](https://docs.aws.amazon.com/workmail/latest/adminguide/security-iam.html)

How to authenticate requests and manage access to your Amazon WorkMail resources.

- [How Amazon WorkMail works with IAM](https://docs.aws.amazon.com/workmail/latest/adminguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon WorkMail, you should understand what IAM features are available to use with Amazon WorkMail.
- [Identity-based policy examples](https://docs.aws.amazon.com/workmail/latest/adminguide/security_iam_id-based-policy-examples.html): By default, IAM users and roles don't have permission to create or modify Amazon WorkMail resources.
- [Troubleshooting](https://docs.aws.amazon.com/workmail/latest/adminguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon WorkMail and IAM.
- [AWS managed policies](https://docs.aws.amazon.com/workmail/latest/adminguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon WorkMail and recent changes to those policies.
- [Using service-linked roles](https://docs.aws.amazon.com/workmail/latest/adminguide/using-service-linked-roles.html): How to use service-linked roles to give Amazon WorkMail access to resources in your AWS account.

### [Logging and monitoring](https://docs.aws.amazon.com/workmail/latest/adminguide/monitoring-overview.html)

Monitor Amazon WorkMail to maintain reliability, availability, and performance.

- [Monitoring with CloudWatch metrics](https://docs.aws.amazon.com/workmail/latest/adminguide/monitoring-workmail-cloudwatch.html): You can monitor Amazon WorkMail using CloudWatch, which collects raw data and processes it into readable, near real-time metrics.
- [Monitoring Amazon WorkMail email event logs](https://docs.aws.amazon.com/workmail/latest/adminguide/cw-events.html): When you turn on email event logging for your Amazon WorkMail organization, Amazon WorkMail logs email events with CloudWatch.
- [Monitoring Amazon WorkMail audit logs](https://docs.aws.amazon.com/workmail/latest/adminguide/monitoring-audit-logging.html): You can use audit logs to monitor access to your Amazon WorkMail Organizationâs mailboxes.
- [Using CloudWatch Insights with Amazon WorkMail](https://docs.aws.amazon.com/workmail/latest/adminguide/cw-insights.html): If you turned on email event logging in the Amazon WorkMail console or enabled audit logs delivery to CloudWatch Logs, you can use Amazon CloudWatch Logs Insights to query your event logs.
- [Logging Amazon WorkMail API calls with AWS CloudTrail](https://docs.aws.amazon.com/workmail/latest/adminguide/logging-using-cloudtrail.html): Learn about integrating Amazon WorkMail with AWS CloudTrail.
- [Enabling email event logging](https://docs.aws.amazon.com/workmail/latest/adminguide/tracking.html): Learn how to track messages using IAM service-linked roles and CloudWatch Logs.
- [Enabling audit logging](https://docs.aws.amazon.com/workmail/latest/adminguide/audit-logging.html): Learn how to track audit logs using IAM service-linked roles and CloudWatch Logs.
- [Compliance validation](https://docs.aws.amazon.com/workmail/latest/adminguide/compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/workmail/latest/adminguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon WorkMail features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/workmail/latest/adminguide/infrastructure-security.html): Learn how Amazon WorkMail isolates service traffic.


## [Getting started](https://docs.aws.amazon.com/workmail/latest/adminguide/getting_started.html)

- [Getting started with Amazon WorkMail](https://docs.aws.amazon.com/workmail/latest/adminguide/howto-start.html): Learn how to create an Amazon WorkMail site.
- [Migrating to Amazon WorkMail](https://docs.aws.amazon.com/workmail/latest/adminguide/migration_overview.html): You can migrate existing mailboxes to Amazon WorkMail from a number of sources, including Microsoft Exchange and G Suite Basic.
- [Interoperability between Amazon WorkMail and Microsoft Exchange](https://docs.aws.amazon.com/workmail/latest/adminguide/interoperability.html): Amazon WorkMail users can share calendar information with Microsoft Exchange users who are in the process of migrating to Amazon WorkMail.

### [Configure availability settings on Amazon WorkMail](https://docs.aws.amazon.com/workmail/latest/adminguide/enable_interop_wm.html)

Configure availability settings on Amazon WorkMail to enable querying external systems, offering calendaring functionality, and to get calendar free/busy information.

- [Building a CAP Lambda function](https://docs.aws.amazon.com/workmail/latest/adminguide/building_cap.html): Custom Availability Providers (CAPs) are configured with a JSON-based request and response protocol that is written in a well defined JSON schema.
- [Configure availability settings in Microsoft Exchange](https://docs.aws.amazon.com/workmail/latest/adminguide/enable_interop_ms.html): Learn how to configure Microsoft Exchange server to redirect free/busy calendar information to Amazon WorkMail.
- [Enable email routing between Microsoft Exchange and Amazon WorkMail users](https://docs.aws.amazon.com/workmail/latest/adminguide/setup-msexchange.html): Learn how to enable email routing between Microsoft Exchange and Amazon WorkMail users.
- [Disabling interoperability mode and decommissioning your mail server](https://docs.aws.amazon.com/workmail/latest/adminguide/disable_interop.html): Learn how to disable interoperability between Amazon WorkMail and Microsoft Exchange Server.
- [Troubleshooting](https://docs.aws.amazon.com/workmail/latest/adminguide/troubleshooting_interop.html): Steps for troubleshooting the most common Amazon WorkMail interoperability and migration problems.
- [Amazon WorkMail quotas](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail_limits.html): Amazon WorkMail can be used by both enterprise customers and small business owners.


## [Working with organizations](https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html)

- [Creating an organization](https://docs.aws.amazon.com/workmail/latest/adminguide/add_new_organization.html): Create an organization to get started with Amazon WorkMail.
- [Deleting an organization](https://docs.aws.amazon.com/workmail/latest/adminguide/delete_organization.html): Learn how to delete an Amazon WorkMail organization.
- [Finding an email address](https://docs.aws.amazon.com/workmail/latest/adminguide/find-emails.html): Learn how to find email addresses in the Amazon WorkMail console.

### [Working with organization settings](https://docs.aws.amazon.com/workmail/latest/adminguide/org-settings.html)

Learn the settings for migration, journaling, interoperability, SMTP gateways, email policies, and DMARC in the Amazon Chime console.

- [Enabling mailbox migration](https://docs.aws.amazon.com/workmail/latest/adminguide/migration-settings.html): You enable mailbox migration when you want to transfer mailboxes from a source, such as Microsoft Exchange or G Suite Basic, to Amazon WorkMail.
- [Enabling journaling](https://docs.aws.amazon.com/workmail/latest/adminguide/journaling.html): You enable journaling to record your email communication.
- [Enabling interoperability](https://docs.aws.amazon.com/workmail/latest/adminguide/enable-interop.html): Interoperability allows you to migrate from Microsoft Exchange and to use Amazon WorkMail as a subset of your corporate mailboxes.
- [Enabling SMTP gateways](https://docs.aws.amazon.com/workmail/latest/adminguide/smtp-gateway.html): Learn how to enable and configure SMTP gateways for use with outbound email flow rules.

### [Managing email flows](https://docs.aws.amazon.com/workmail/latest/adminguide/email-flows.html)

Learn how to set up email flow rules for managing inbound and outbound emails.

- [Creating email flow rules](https://docs.aws.amazon.com/workmail/latest/adminguide/create-email-rules.html): Learn how to create an email flow rule in Amazon WorkMail.
- [Editing email flow rules](https://docs.aws.amazon.com/workmail/latest/adminguide/edit-rules.html): Learn how to edit email flow rules in the Amazon WorkMail console.

### [Configuring AWS Lambda for Amazon WorkMail](https://docs.aws.amazon.com/workmail/latest/adminguide/lambda.html)

Learn how to configure the Run Lambda action for use with email flow rules and AWS Lambda functions.

- [Retrieving message content with AWS Lambda](https://docs.aws.amazon.com/workmail/latest/adminguide/lambda-content.html): Learn how to use AWS Lambda functions to retrieve email message content in Amazon WorkMail.
- [Updating message content with AWS Lambda](https://docs.aws.amazon.com/workmail/latest/adminguide/update-with-lambda.html): Learn how to use AWS Lambda to update in-transit email messages in Amazon WorkMail.
- [Managing access to the Amazon WorkMail Message Flow API](https://docs.aws.amazon.com/workmail/latest/adminguide/lambda-content-access.html): Learn how to use IAM policies to manage access to the Amazon WorkMail Message Flow API.
- [Testing an email flow rule](https://docs.aws.amazon.com/workmail/latest/adminguide/test-email-flow-rule.html): Learn how to test your email flow rules in Amazon WorkMail.
- [Removing an email flow rule](https://docs.aws.amazon.com/workmail/latest/adminguide/remove-email-flow-rule.html): Learn how to remove and email flow rule in Amazon WorkMail.
- [Enforcing DMARC policies on incoming email](https://docs.aws.amazon.com/workmail/latest/adminguide/inbound-dmarc.html): Learn how to enforce Domain-based Message Authentication, Reporting and Conformance (DMARC) policies on incoming email.
- [Tagging an organization](https://docs.aws.amazon.com/workmail/latest/adminguide/org-tag.html): Learn how to use tagging in your Amazon WorkMail organizations.
- [Working with access control rules](https://docs.aws.amazon.com/workmail/latest/adminguide/access-rules.html): Learn how to use access control rules to grant user access to Amazon WorkMail.
- [Setting mailbox retention policies](https://docs.aws.amazon.com/workmail/latest/adminguide/mailbox-retention-policy.html): Learn how to set retention policies for your Amazon WorkMail messages and other items.


## [Working with domains](https://docs.aws.amazon.com/workmail/latest/adminguide/domains_overview.html)

- [Adding a domain](https://docs.aws.amazon.com/workmail/latest/adminguide/add_domain.html): Add a domain to an Amazon WorkMail organization.
- [Removing a domain](https://docs.aws.amazon.com/workmail/latest/adminguide/remove_domain.html): Remove domains in Amazon WorkMail.
- [Choosing the default domain](https://docs.aws.amazon.com/workmail/latest/adminguide/default_domain.html): Choose a default domain for users and groups in Amazon WorkMail.
- [Verifying domains](https://docs.aws.amazon.com/workmail/latest/adminguide/domain_verification.html): Learn to verify domains by adding TXT and MX records to your DNS service in the Amazon WorkMail console.
- [Enabling AutoDiscover to configure endpoints](https://docs.aws.amazon.com/workmail/latest/adminguide/autodiscover.html): Use AutoDiscover to configure endpoints in Amazon WorkMail.
- [Editing domain identity policies](https://docs.aws.amazon.com/workmail/latest/adminguide/editing_domains.html): Learn to edit domain identity policies that specify permissions for email actions.
- [Authenticating email with SPF](https://docs.aws.amazon.com/workmail/latest/adminguide/authenticate_domain.html): Learn to authenticate email with SPF.
- [Configuring a custom MAIL FROM domain](https://docs.aws.amazon.com/workmail/latest/adminguide/custom-mail-from-domain.html): Learn how to configure a custom MAIL FROM domain in Amazon WorkMail.


## [Working with users](https://docs.aws.amazon.com/workmail/latest/adminguide/users_overview.html)

- [Viewing a list of users](https://docs.aws.amazon.com/workmail/latest/adminguide/display_users.html): Learn how to view users that can be used by Amazon WorkMail.
- [Adding a user](https://docs.aws.amazon.com/workmail/latest/adminguide/add_user.html): Add a user in your Amazon WorkMail organization.
- [Enabling users](https://docs.aws.amazon.com/workmail/latest/adminguide/enable_user.html): Learn how to enable an Amazon WorkDocs or Amazon WorkSpaces user for Amazon WorkMail.
- [Managing user aliases](https://docs.aws.amazon.com/workmail/latest/adminguide/managing_users.html): Learn how to manage the details of an Amazon WorkMail user, such as adding or removing a user from an email alias.
- [Disabling users](https://docs.aws.amazon.com/workmail/latest/adminguide/disable-users.html): You can disable any user in an organization at any time.
- [Editing user details](https://docs.aws.amazon.com/workmail/latest/adminguide/edit_user.html): Learn how to modify user details in Amazon WorkMail.
- [Resetting user password](https://docs.aws.amazon.com/workmail/latest/adminguide/reset_password.html): Learn how to reset user passwords in Amazon WorkMail.
- [Troubleshooting Amazon WorkMail password policies](https://docs.aws.amazon.com/workmail/latest/adminguide/password-policies.html): If resetting the password is unsuccessful, verify that the new password meets the password policy requirements.
- [Working with notifications](https://docs.aws.amazon.com/workmail/latest/adminguide/notifications.html): Learn how to set up push notifications in Amazon WorkMail.
- [Enabling signed or encrypted email](https://docs.aws.amazon.com/workmail/latest/adminguide/enable_encryption.html): Learn how to enable users to send signed or encrypted email.


## [Working with groups](https://docs.aws.amazon.com/workmail/latest/adminguide/groups_overview.html)

- [Viewing a list of groups](https://docs.aws.amazon.com/workmail/latest/adminguide/display_groups.html): Learn how to view groups that can be used by Amazon WorkMail.
- [Adding a group](https://docs.aws.amazon.com/workmail/latest/adminguide/add_new_group.html): Learn how to add groups in Amazon WorkMail.
- [Enabling groups](https://docs.aws.amazon.com/workmail/latest/adminguide/enable_existing_group.html): Learn how to enable groups as security groups or distribution lists in Amazon WorkMail.
- [Adding members to a group](https://docs.aws.amazon.com/workmail/latest/adminguide/add-group-users.html): Add members (users and groups) to an Amazon WorkMail group.
- [Editing group details](https://docs.aws.amazon.com/workmail/latest/adminguide/edit-group-users.html): Edit an Amazon WorkMail group.
- [Removing members from a group](https://docs.aws.amazon.com/workmail/latest/adminguide/remove-group-users.html): Remove members from an Amazon WorkMail group.
- [Managing group aliases](https://docs.aws.amazon.com/workmail/latest/adminguide/managing_groups.html): Learn how to manage the details of an Amazon WorkMail group, such as adding or removing an email alias from the group.
- [Disabling groups](https://docs.aws.amazon.com/workmail/latest/adminguide/disable-group.html): Learn how to disable Amazon WorkMail groups when you no longer need them.
- [Deleting a group](https://docs.aws.amazon.com/workmail/latest/adminguide/delete-group.html): Learn how to delete an Amazon WorkMail group.


## [Working with resources](https://docs.aws.amazon.com/workmail/latest/adminguide/resources_overview.html)

- [Viewing a list of resources](https://docs.aws.amazon.com/workmail/latest/adminguide/display_resource.html): Learn how to view resources that can be used by Amazon WorkMail.
- [Adding a resource](https://docs.aws.amazon.com/workmail/latest/adminguide/create_resource.html): Learn how to add a new resource that can be reserved using Amazon WorkMail.
- [Editing resource details](https://docs.aws.amazon.com/workmail/latest/adminguide/edit_resource.html): Learn how to edit the details of an Amazon WorkMail resource, such as name, resource type, email address, and hide the resource from the global address list.
- [Managing resource aliases](https://docs.aws.amazon.com/workmail/latest/adminguide/managing_resource.html): Learn how to manage the details of an Amazon WorkMail resource, such as adding or removing an email alias from the resource.
- [Enabling a resource](https://docs.aws.amazon.com/workmail/latest/adminguide/enable-resource.html): Learn how to enable an Amazon WorkMail resource.
- [Disabling a resource](https://docs.aws.amazon.com/workmail/latest/adminguide/disable-resource.html): Learn how to disable an Amazon WorkMail resource.
- [Deleting a resource](https://docs.aws.amazon.com/workmail/latest/adminguide/remove_resource.html): Learn how to delete unnecessary resources from Amazon WorkMail.


## [Working with IAM Identity Center](https://docs.aws.amazon.com/workmail/latest/adminguide/identity_center_overview.html)

- [Enabling IAM Identity Center in Amazon WorkMail](https://docs.aws.amazon.com/workmail/latest/adminguide/enabling_identity_center.html): Learn how to enable IAM Identity Center in Amazon WorkMail.
- [Assigning IAM Identity Center users and groups to Amazon WorkMail application](https://docs.aws.amazon.com/workmail/latest/adminguide/assigning_usersandgroups.html): Learn how to assign IAM Identity Center users and groups in Amazon WorkMail.
- [Associating Amazon WorkMail users with IAM Identity Center users](https://docs.aws.amazon.com/workmail/latest/adminguide/connecting_wmusers.html): Learn how to associate Amazon WorkMailusers with IAM Identity Center users
- [Authentication mode](https://docs.aws.amazon.com/workmail/latest/adminguide/authenticate_mode.html): Learn how to authenticate in Amazon WorkMail.
- [Configuring personal access tokens](https://docs.aws.amazon.com/workmail/latest/adminguide/personal_access-token.html): Learn how to view enable IAM Identity Center in Amazon WorkMail.
- [Disabling IAM Identity Center](https://docs.aws.amazon.com/workmail/latest/adminguide/disabling_sso.html): Learn how to disable IAM Identity Center in Amazon WorkMail.


## [Working with mobile devices](https://docs.aws.amazon.com/workmail/latest/adminguide/work-with-mobile-devices.html)

- [Editing your organization's mobile device policy](https://docs.aws.amazon.com/workmail/latest/adminguide/edit_mobile_policy.html): Learn how to edit organizational mobile device policies in Amazon WorkMail.
- [Managing mobile devices](https://docs.aws.amazon.com/workmail/latest/adminguide/manage-devices.html): How to keep the mobile devices connected to your Amazon WorkMail organization safer.
- [Managing mobile device access rules](https://docs.aws.amazon.com/workmail/latest/adminguide/manage-mobile-access.html): Learn how to create and manage access rules for mobile devices in Amazon WorkMail.
- [Managing mobile device access overrides](https://docs.aws.amazon.com/workmail/latest/adminguide/mobile-overrides.html): Learn how to manage access overrides for mobile devices connected to Amazon WorkMail.
- [Integrating with mobile device management solutions](https://docs.aws.amazon.com/workmail/latest/adminguide/mdm-integration.html): Learn how to integrate Amazon WorkMail with third-party mobile device management solutions.


## [Working with mailbox permissions](https://docs.aws.amazon.com/workmail/latest/adminguide/mail_perms_overview.html)

- [About mailbox and folder permissions](https://docs.aws.amazon.com/workmail/latest/adminguide/mail_vs_folder.html): The concepts that you need to understand in order to effectively set and manage mailbox permissions in Amazon WorkMail.
- [Managing mailbox permissions for users](https://docs.aws.amazon.com/workmail/latest/adminguide/enable_mail_perms.html): Learn how to grant users permissions to other mailboxes in Amazon WorkMail.
- [Managing mailbox permissions for groups](https://docs.aws.amazon.com/workmail/latest/adminguide/manage_group_perms.html): Learn how to give Amazon WorkMail groups permission to access other users' mailboxes.


## [Programmatic access to mailboxes](https://docs.aws.amazon.com/workmail/latest/adminguide/mail_perms_programmatic.html)

- [Managing impersonation roles](https://docs.aws.amazon.com/workmail/latest/adminguide/managing-impersonation-roles.html): Learn how to manage an impersonation role.
- [Using impersonation roles](https://docs.aws.amazon.com/workmail/latest/adminguide/using-impersonation-roles.html): Learn how to use impersonation roles in Amazon WorkMail.


## [Troubleshooting](https://docs.aws.amazon.com/workmail/latest/adminguide/troubleshooting.html)

- [Viewing email headers](https://docs.aws.amazon.com/workmail/latest/adminguide/email-headers.html): Learn how to view email headers, information that can help you troubleshoot user email issues.
- [Mail routing](https://docs.aws.amazon.com/workmail/latest/adminguide/mail-routing.html): Learn how to troubleshoot mail routing issues.
