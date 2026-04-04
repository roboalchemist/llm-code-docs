# Source: https://docs.aws.amazon.com/security-ir/latest/userguide/llms.txt

# AWS Security Incident Response User Guide 

> Describes key concepts for AWS Security Incident Response and provides instructions for how to configure and use AWS Security Incident Response features.

- [Concepts and Terminology](https://docs.aws.amazon.com/security-ir/latest/userguide/concepts-and-terminology.html)
- [Tagging AWS Security Incident Response resources](https://docs.aws.amazon.com/security-ir/latest/userguide/sir_tagging.html)
- [Service Quotas](https://docs.aws.amazon.com/security-ir/latest/userguide/service-quotas.html)
- [Document history](https://docs.aws.amazon.com/security-ir/latest/userguide/document-history-for-the-aws-security-incident-response-user-guide.html)

## [What is AWS Security Incident Response?](https://docs.aws.amazon.com/security-ir/latest/userguide/what-is.html)

- [Supported configurations](https://docs.aws.amazon.com/security-ir/latest/userguide/supported-configs.html): Describes AWS Security Incident Response supported configurations.
- [Feature Summary](https://docs.aws.amazon.com/security-ir/latest/userguide/feature-summary.html): Describes AWS Security Incident Response supported features.


## [Getting started](https://docs.aws.amazon.com/security-ir/latest/userguide/getting-started.html)

### [Onboarding Guide](https://docs.aws.amazon.com/security-ir/latest/userguide/onboarding-guide.html)

The AWS onboarding guide walks you through prerequisites and AWS Security Incident Response onboarding and containment actions.

- [Deploy and configure Security Incident Response](https://docs.aws.amazon.com/security-ir/latest/userguide/deploy-configure.html)

### [Authorize monitoring and containment actions](https://docs.aws.amazon.com/security-ir/latest/userguide/authorize-security-incident-response.html)

This page describes how to authorize Security Incident Response to perform automated monitoring and containment actions in your AWS environment.

- [Enable Proactive Response](https://docs.aws.amazon.com/security-ir/latest/userguide/enable-proactive-response.html): Proactive response enables Security Incident Response to monitor and investigate alerts generated from Amazon GuardDuty and AWS Security Hub CSPM integrations across your organization.
- [Define containment action preferences](https://docs.aws.amazon.com/security-ir/latest/userguide/define-containment-preferences.html): Containment actions enable Security Incident Response to execute rapid response measures during an active security incident, such as isolating compromised hosts or rotating credentials.
- [Post deployment of Security Incident Response](https://docs.aws.amazon.com/security-ir/latest/userguide/post-deploy.html): AWS integrates with your existing incident response framework instead of replacing it.
- [Update the Incident Response Team](https://docs.aws.amazon.com/security-ir/latest/userguide/update-security-incident-response.html)
- [AWS supported case](https://docs.aws.amazon.com/security-ir/latest/userguide/support-case.html): AWS Security Incident Response provides a subscription-based case management portal where your organization directly engages with our Security Incident Response engineers.
- [GuardDuty findings and suppression rules](https://docs.aws.amazon.com/security-ir/latest/userguide/guard-duty.html): AWS Security Incident Response proactively ingests, triages, and responds to all GuardDuty findings and Security Hub CSPM findings from CrowdStrike, FortinetCNAPP (Lacework), and Trend Micro.
- [Amazon EventBridge](https://docs.aws.amazon.com/security-ir/latest/userguide/amazon-eventbridge.html): Amazon EventBridge enables event-driven architecture for Security Incident Response, allowing case activity to trigger downstream services (SNS, Lambda, SQS, Step-Functions) or external tools (Jira, ServiceNow, Teams, Slack, PagerDuty).
- [Integrations and external tooling workflow](https://docs.aws.amazon.com/security-ir/latest/userguide/integrations-external-tooling.html): AWS solutions to integrate JIRA or ServiceNow with Security Incident Response
- [External tooling workflow](https://docs.aws.amazon.com/security-ir/latest/userguide/external-tooling.html): Security Incident Response integrates with external tools and partners in multiple ways:
- [Appendix A: Points of contact](https://docs.aws.amazon.com/security-ir/latest/userguide/appendix.html): Providing your metadata upfront to our Security Incident Response engineers, can help accelerate the profile creation time, improving the confidence in our triaging technology out of the gate.
- [RACI Matrix](https://docs.aws.amazon.com/security-ir/latest/userguide/raci-matrix.html): The following RACI matrix defines roles and responsibilities across the Security Incident Response implementation process.
- [Select a membership account](https://docs.aws.amazon.com/security-ir/latest/userguide/select-a-membership-account.html): A membership account is the AWS account used to configure account details, add and remove details for your incident response team, and where all active and historical security events can be created and managed.
- [Set up membership details](https://docs.aws.amazon.com/security-ir/latest/userguide/setup-membership-details.html)
- [Associate accounts with AWS Organizations](https://docs.aws.amazon.com/security-ir/latest/userguide/associate-accounts-with-aws-organizations.html): If you chose to associate your entire AWS Organizations during setup, your membership entitles coverage on all member accounts in the organization.

### [Set up proactive response and alert triaging workflows](https://docs.aws.amazon.com/security-ir/latest/userguide/setup-monitoring-and-investigation-workflows.html)

AWS Security Incident Response monitors and investigates threat alerts generated from Amazon GuardDuty and Security Hub CSPM integrations.

- [Understanding Automatic Archiving with Proactive Response](https://docs.aws.amazon.com/security-ir/latest/userguide/understanding-automatic-archiving.html): When you enable proactive response and alert triaging, AWS Security Incident Response automatically monitors and triages security findings from Amazon GuardDuty and Security Hub CSPM.


## [User tasks](https://docs.aws.amazon.com/security-ir/latest/userguide/task-based-content.html)

- [Dashboard](https://docs.aws.amazon.com/security-ir/latest/userguide/dashboard.html): On the AWS Security Incident Response console, the dashboard provides you with an overview of your incident response team, your proactive response status, and a four-week rolling count of cases.

### [Managing my Incident Response Team](https://docs.aws.amazon.com/security-ir/latest/userguide/managing-my-incident-response-team.html)

Your incident response teams contains stakeholders for the incident response process.

- [Communication Preferences](https://docs.aws.amazon.com/security-ir/latest/userguide/communication-preferences.html): Configure your communication preferences to control how you receive notifications and interact with the incident response system during security incidents.

### [Account association to AWS Organizations](https://docs.aws.amazon.com/security-ir/latest/userguide/managing-associated-accounts.html)

When you enable AWS Security Incident Response, you will be given the option of selecting your entire organization or specific organizational units (OUs).

### [Managing Your Membership Coverage](https://docs.aws.amazon.com/security-ir/latest/userguide/managing-membership-coverage.html)

You can change your membership coverage option at any time, including switching from organization-wide coverage to specific OUs.

- [Updating OU Associations](https://docs.aws.amazon.com/security-ir/latest/userguide/updating-ou-associations.html): To manage your membership coverage:
- [Important Considerations](https://docs.aws.amazon.com/security-ir/latest/userguide/important-considerations.html): Accounts directly under the root: When selecting specific OUs for your membership, accounts that are directly under the organization root (not part of any OU) will not be associated with your membership.

### [Monitoring and investigation](https://docs.aws.amazon.com/security-ir/latest/userguide/monitoring-and-investigation.html)

AWS Security Incident Response reviews and triages security alerts from Amazon GuardDuty and AWS Security Hub CSPM, then configures suppression rules based on your environment to prevent unnecessary alerts.

- [Prepare](https://docs.aws.amazon.com/security-ir/latest/userguide/prepare.html): The AWS Security Incident Response team investigates and partners with you throughout the security event response lifecycle.
- [Detect and Analyze](https://docs.aws.amazon.com/security-ir/latest/userguide/detect-and-analyze.html): Reporting an Event
- [AI Investigative Agent](https://docs.aws.amazon.com/security-ir/latest/userguide/ai-investigative-agent.html)

### [Contain](https://docs.aws.amazon.com/security-ir/latest/userguide/contain.html)

AWS Security Incident Response partners with you to contain events.

- [Containment Decision-Making](https://docs.aws.amazon.com/security-ir/latest/userguide/containment-decision-making.html): An essential part of containment is decision-making, such as whether to shut down a system, isolate a resource from the network, turn off access, or end sessions.

### [Supported Containment Actions](https://docs.aws.amazon.com/security-ir/latest/userguide/supported-containment-actions.html)

AWS Security Incident Response executes supported containment actions on your behalf to expedite response and reduce the time a threat actor has to potentially cause damage in your environment.

- [EC2 Containment](https://docs.aws.amazon.com/security-ir/latest/userguide/ec2-containment.html): The AWSSupport-ContainEC2Instance containment automation performs a reversible network containment of an EC2 instance, leaving the instance intact and running, but isolating it from any new network activity and preventing it from communicating with resources within and outside your VPC.
- [IAM Containment](https://docs.aws.amazon.com/security-ir/latest/userguide/iam-containment.html): The AWSSupport-ContainIAMPrincipal containment automation performs a reversible network containment of an IAM user or role, leaving the user or role in IAM, but isolating it from communicating with resources within your account.
- [S3 Containment](https://docs.aws.amazon.com/security-ir/latest/userguide/s3-containment.html): The AWSSupport-ContainS3Resource containment automation performs a reversible containment of a S3 bucket, leaving the objects in the bucket, and isolating the Amazon S3 bucket or object by modifying its access policies.
- [Developing Containment Strategies](https://docs.aws.amazon.com/security-ir/latest/userguide/developing-containment-strategies.html): AWS Security Incident Response encourages you to consider containment strategies for each major event type that fit within your risk appetite.

### [Staged Containment Approach](https://docs.aws.amazon.com/security-ir/latest/userguide/staged-containment-approach.html)

AWS Security Incident Response advises a staged approach to achieve efficient and effective containment, involving short-term and long-term strategies based on the resource type.

- [Containment Strategy](https://docs.aws.amazon.com/security-ir/latest/userguide/containment-strategy-questions.html): Can AWS Security Incident Response identify the scope of the security event?
- [System Backup](https://docs.aws.amazon.com/security-ir/latest/userguide/system-backup.html): Were backup copies of affected systems created for further analysis?
- [Eradicate](https://docs.aws.amazon.com/security-ir/latest/userguide/eradicate.html): During the eradication phase, it is important to identify and address all affected accounts, resources, and instances - such as by deleting malware, removing compromised user accounts, and mitigating any discovered vulnerabilities - to apply uniform remediation across the environment.
- [Recover](https://docs.aws.amazon.com/security-ir/latest/userguide/recover.html): AWS Security Incident Response provides you guidance to help restore systems to normal operation, confirm they are functioning properly, and remediate any vulnerabilities to prevent similar events in the future.

### [Post incident report](https://docs.aws.amazon.com/security-ir/latest/userguide/post-incident-report.html)

AWS Security Incident Response provides a summary of the event after the conclusion of security activities between your team and ours.

- [Case metrics](https://docs.aws.amazon.com/security-ir/latest/userguide/case-metrics.html)
- [Triaging metrics](https://docs.aws.amazon.com/security-ir/latest/userguide/triaging-metrics.html)

### [Cases](https://docs.aws.amazon.com/security-ir/latest/userguide/cases.html)

AWS Security Incident Response allows you to create two types of cases - AWS supported or self-managed cases.

### [Create an AWS supported case](https://docs.aws.amazon.com/security-ir/latest/userguide/create-an-aws-supported-case.html)

You can create an AWS supported case for AWS Security Incident Response through the Console, the API, or the AWS Command Line Interface.

- [When to contact AWS Security Incident Response](https://docs.aws.amazon.com/security-ir/latest/userguide/when-to-contact-security-ir.html): You can contact AWS Security Incident Response for various purposes depending on your needs.
- [Create a self-managed case](https://docs.aws.amazon.com/security-ir/latest/userguide/create-a-self-managed-case.html): You can create a self-managed for AWS Security Incident Response through the Console, API, or AWS Command Line Interface.

### [Working with AWS Security Incident Response engineers](https://docs.aws.amazon.com/security-ir/latest/userguide/working-with-aws-sir-engineers.html)

After you open a security incident case, the AWS Security Incident Response engineers begin working on your incident.

- [What to expect](https://docs.aws.amazon.com/security-ir/latest/userguide/what-to-expect-from-aws-sir-engineers.html): When you open an AWS supported case, a Security Incident Response engineer is assigned to your incident.
- [Investigation workflow](https://docs.aws.amazon.com/security-ir/latest/userguide/investigation-workflow.html): AWS Security Incident Response engineers follow a structured incident response process aligned with the NIST 800-61r2 framework.
- [Information Security Incident Response engineers may request](https://docs.aws.amazon.com/security-ir/latest/userguide/information-sir-engineers-may-request.html): To investigate your incident effectively, AWS Security Incident Response engineers may ask you to provide:
- [Communication best practices](https://docs.aws.amazon.com/security-ir/latest/userguide/communication-best-practices.html): Effective communication accelerates incident resolution.
- [Your role](https://docs.aws.amazon.com/security-ir/latest/userguide/your-role-during-investigation.html): While AWS Security Incident Response engineers lead the investigation, your participation is essential.
- [Case closure](https://docs.aws.amazon.com/security-ir/latest/userguide/case-closure.html): AWS Security Incident Response engineers close your case when:
- [Responding to an AWS generated case](https://docs.aws.amazon.com/security-ir/latest/userguide/responding-to-an-aws-generated-case.html): AWS Security Incident Response might create an outbound notification or case when you need to act on or be aware of something that potentially impacts your account or resources.

### [Managing Cases](https://docs.aws.amazon.com/security-ir/latest/userguide/managing-cases.html)

Contents

- [Changing the case status](https://docs.aws.amazon.com/security-ir/latest/userguide/changing-the-case-status.html): A case is in one of the following states:
- [Changing the resolver](https://docs.aws.amazon.com/security-ir/latest/userguide/changing-the-resolver.html): For self-managed cases, your incident response team can request help from AWS.
- [Action Items](https://docs.aws.amazon.com/security-ir/latest/userguide/action-items.html): An AWS Security Incident Response engineer working on the case may request actions from your internal team.
- [Edit a case](https://docs.aws.amazon.com/security-ir/latest/userguide/edit-a-case.html): Choose Edit to change the details of a case.
- [Communications](https://docs.aws.amazon.com/security-ir/latest/userguide/communications.html): AWS Security Incident Response engineers can add comments to document their activities when working on a case.
- [Permissions](https://docs.aws.amazon.com/security-ir/latest/userguide/sir-permissions.html): The permissions tab lists all individuals that will be notified for any change to the case.
- [Attachments](https://docs.aws.amazon.com/security-ir/latest/userguide/attachments.html): Your incident responders can add attachments to a case that help other incident responders with their investigation for self-managed cases.
- [Tags](https://docs.aws.amazon.com/security-ir/latest/userguide/tags.html): A tag is an optional label that you can assign to your cases to hold metadata about that resource.
- [Case activities](https://docs.aws.amazon.com/security-ir/latest/userguide/case-activities.html): Audit trailsÂ provide detailed chronological records of all case activities.
- [Closing a case](https://docs.aws.amazon.com/security-ir/latest/userguide/closing-a-case.html): For AWS supported cases, choose Close CaseÂ on the case details page to permanently close the case at any status.
- [Working with CloudFormation stacksets](https://docs.aws.amazon.com/security-ir/latest/userguide/working-with-stacksets.html)
- [Cancel Membership](https://docs.aws.amazon.com/security-ir/latest/userguide/cancel-membership.html): A role having the CancelMembership permission for AWS Security Incident Response can cancel the membership from the console, the API, or AWS Command Line Interface.


## [Using AWS CloudShell](https://docs.aws.amazon.com/security-ir/latest/userguide/using-aws-with-cloudshell.html)

- [Obtaining IAM permissions for AWS CloudShell](https://docs.aws.amazon.com/security-ir/latest/userguide/cloudshell-permissions.html): Using the access management resources provided by AWS Identity and Access Management, administrators can grant permissions to IAM users so they can access AWS CloudShell and use the environment's features.
- [Interacting with Security Incident Response using AWS CloudShell](https://docs.aws.amazon.com/security-ir/latest/userguide/cshell-examples.html): After you launch AWS CloudShell from the AWS Management Console, you can immediately start to interact with Security Incident Response using the command line interface.


## [CloudTrail logs](https://docs.aws.amazon.com/security-ir/latest/userguide/logging-using-cloudtrail.html)

- [Security Incident Response information in CloudTrail](https://docs.aws.amazon.com/security-ir/latest/userguide/service-name-info-in-cloudtrail.html): CloudTrail is enabled on your AWS account when you create the account.
- [Understanding Security Incident Response log file entries](https://docs.aws.amazon.com/security-ir/latest/userguide/understanding-service-name-entries.html): A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify.


## [Managing accounts with AWS Organizations](https://docs.aws.amazon.com/security-ir/latest/userguide/security-ir-organizations.html)

- [Considerations and recommendations](https://docs.aws.amazon.com/security-ir/latest/userguide/considerations_important.html)
- [Trusted access](https://docs.aws.amazon.com/security-ir/latest/userguide/using-orgs-trusted-access.html): Learn how to enable trusted access between AWS Organizations and AWS Account Management.
- [Permissions required to designate a delegated Security Incident Response administrator account](https://docs.aws.amazon.com/security-ir/latest/userguide/organizations_permissions.html): You can chose to set up your AWS Security Incident Response membership using delegated administrator for AWS Organizations.
- [Designating a delegated administrator AWS Security Incident Response](https://docs.aws.amazon.com/security-ir/latest/userguide/delegated-admin-designate.html): This section provides steps to designate a delegated administrator in the AWS Security Incident Response organization.
- [Managing membership with organizational units (OUs)](https://docs.aws.amazon.com/security-ir/latest/userguide/managing-membership-with-ou.html): AWS Security Incident Response supports membership coverage for individual organizational units (OUs).
- [Adding members to AWS Security Incident Response](https://docs.aws.amazon.com/security-ir/latest/userguide/add-member-accounts.html): There is a one to one relationship with AWS Organizations and your AWS Security Incident Response membership.
- [Removing members from AWS Security Incident Response](https://docs.aws.amazon.com/security-ir/latest/userguide/remove-member-account.html): To remove an account from your membership, you can remove a member account from your organization, move accounts out of your selected OUs, or remove OUs from your membership.


## [](https://docs.aws.amazon.com/security-ir/latest/userguide/eventbridge.html)

### [Managing events using EventBridge](https://docs.aws.amazon.com/security-ir/latest/userguide/eventbridge-integration-full.html)

Receive notifications when specific Security Incident Response events such as object creation or deletion occur in an Security Incident Response with EventBridge.

- [Events detail reference](https://docs.aws.amazon.com/security-ir/latest/userguide/events-detail-reference-full.html): All events from AWS services have a common set of fields containing metadata about the event, such as the AWS service that is the source of the event, the time the event was generated, the account and region in which the event took place, and others.
- [Case Events](https://docs.aws.amazon.com/security-ir/latest/userguide/case-events.html): Case Created by AWS Responder
- [Case Comment Events](https://docs.aws.amazon.com/security-ir/latest/userguide/case-comment-events.html): Case Comment Created by AWS Responder
- [Membership Events](https://docs.aws.amazon.com/security-ir/latest/userguide/case-membership-events.html): Membership Created
- [Using AWS Security Incident Response Events](https://docs.aws.amazon.com/security-ir/latest/userguide/using-events.html): You can create EventBridge rules to match these events and trigger automated actions.

### [Tutorial: Sending Amazon Simple Notification Service alerts for Membership Updated events](https://docs.aws.amazon.com/security-ir/latest/userguide/service_sns_tutorial.html)

In this tutorial, you configure an Amazon EventBridge event rule that only captures events where the your subscription enters a Membership Updated status.

- [Tutorial: Create and subscribe to an Amazon SNS topic](https://docs.aws.amazon.com/security-ir/latest/userguide/service_sns_create_topic.html): For this tutorial, you configure an Amazon SNS topic to serve as an event target for your new event rule.
- [Tutorial: Register an event rule](https://docs.aws.amazon.com/security-ir/latest/userguide/service_sns_reg_rule.html): Next, register an event rule that captures only Membership Updated events.
- [Tutorial: Test your rule](https://docs.aws.amazon.com/security-ir/latest/userguide/service_sns_test_rule.html): To test your rule, submit an update yo your AWS Security Incident Response membership.
- [Alternate rule: Security Incident Response Case Updates](https://docs.aws.amazon.com/security-ir/latest/userguide/service_case_updates_queue.html): To create an event rule that monitors for all case updates, repeat these tutorials with the following alterations:


## [Troubleshooting](https://docs.aws.amazon.com/security-ir/latest/userguide/troubleshooting.html)

- [Issues](https://docs.aws.amazon.com/security-ir/latest/userguide/issues.html): Not sending requests from the correct context.
- [Errors](https://docs.aws.amazon.com/security-ir/latest/userguide/errors.html): AccessDeniedException
- [Support](https://docs.aws.amazon.com/security-ir/latest/userguide/support.html): If you need additional assistance, contact Support Center for troubleshooting purposes.


## [Security](https://docs.aws.amazon.com/security-ir/latest/userguide/service-security.html)

### [Data Protection in AWS Security Incident Response](https://docs.aws.amazon.com/security-ir/latest/userguide/data-protection.html)

Contents

### [Data encryption](https://docs.aws.amazon.com/security-ir/latest/userguide/data-encryption.html)

Contents

- [Encryption at rest](https://docs.aws.amazon.com/security-ir/latest/userguide/encryption-at-rest.html): Data is encrypted at rest using transparent server-side encryption.
- [Encryption in transit](https://docs.aws.amazon.com/security-ir/latest/userguide/encryption-in-transit.html): Data gathered and accessed by AWS Security Incident Response is exclusively over a Transport Layer Security (TLS) protected channel.
- [Key management](https://docs.aws.amazon.com/security-ir/latest/userguide/key-management.html): AWS Security Incident Response implements integrations with AWS KMS to provide encryption at rest for case and attachment data.
- [Inter-network traffic privacy](https://docs.aws.amazon.com/security-ir/latest/userguide/inter-network-traffic-privacy.html)

### [Identity and Access Management](https://docs.aws.amazon.com/security-ir/latest/userguide/identity-and-access-management.html)

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator control access to AWS resources.

- [Authenticating with identities](https://docs.aws.amazon.com/security-ir/latest/userguide/authenticating-with-identities.html): Authentication is how you sign in to AWS using your identity credentials.

### [How AWS Security Incident Response Works with IAM](https://docs.aws.amazon.com/security-ir/latest/userguide/how-aws-security-incident-response-works-with-iam.html)

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources.

### [Identity-based policies for AWS Security Incident Response](https://docs.aws.amazon.com/security-ir/latest/userguide/identity-based-policies.html)

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role.

- [Identity-based policy examples](https://docs.aws.amazon.com/security-ir/latest/userguide/iam-examples.html): By default, users and roles don't have permission to create or modify AWS Security Incident Response resources.
- [Policy best practices](https://docs.aws.amazon.com/security-ir/latest/userguide/policy-best-practices.html): Identity-based policies determine whether someone can create, access, or delete AWS Security Incident Response resources in your account.
- [Using the AWS Security Incident Response console](https://docs.aws.amazon.com/security-ir/latest/userguide/using-the-amazon-aws-security-incident-response-console.html): To access https://console.aws.amazon.com/security-ir/, you must have a minimum set of permissions.
- [Allow users to view their own permissions](https://docs.aws.amazon.com/security-ir/latest/userguide/allow-users-to-view-their-own-permissions.html): This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user identity.
- [Resource-Based Policies](https://docs.aws.amazon.com/security-ir/latest/userguide/resource-based-policies.html): Resource-based policies within AWS Security Incident Response
- [Policy Actions](https://docs.aws.amazon.com/security-ir/latest/userguide/policy-actions.html): Policy actions for AWS Security Incident Response
- [Policy condition keys for AWS Security Incident Response](https://docs.aws.amazon.com/security-ir/latest/userguide/policy-condition-keys-for-aws-security-incident-response.html): Supports service-specific policy condition keys: No
- [Access control lists (ACLs) in AWS Security Incident Response](https://docs.aws.amazon.com/security-ir/latest/userguide/access-control-lists-acls-in-aws-security-incident-response.html): Supports ACLs: No
- [Troubleshooting AWS Security Incident Response identity and access](https://docs.aws.amazon.com/security-ir/latest/userguide/troubleshooting-aws-security-incident-response-identity-and-access.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS Security Incident Response and IAM.
- [Using service roles](https://docs.aws.amazon.com/security-ir/latest/userguide/using-service-roles.html): Supports service roles: No
- [Using service-linked roles](https://docs.aws.amazon.com/security-ir/latest/userguide/using-service-linked-roles.html): Service-linked roles for AWS Security Incident Response
- [AWS Managed Policies](https://docs.aws.amazon.com/security-ir/latest/userguide/aws-managed-policies.html): An AWS managed policy is a standalone policy that is created and administered by AWS.
- [Incident response](https://docs.aws.amazon.com/security-ir/latest/userguide/incident-response.html): Security and Compliance is a shared responsibility between AWS and the customer.
- [Compliance validation](https://docs.aws.amazon.com/security-ir/latest/userguide/compliance-validation.html): Third-party auditors assess the security and compliance of AWS services as part of multiple AWS compliance programs.
- [Logging and monitoring in AWS Security Incident Response](https://docs.aws.amazon.com/security-ir/latest/userguide/logging-and-monitoring-in-aws-security-incident-response.html): Monitoring is an important part of maintaining the reliability, availability, and performance of AWS Security Incident Response and your other AWS solutions.
- [Resilience](https://docs.aws.amazon.com/security-ir/latest/userguide/resilience.html): The AWS global infrastructure is built around AWS Regions and Availability Zones.
- [Infrastructure security](https://docs.aws.amazon.com/security-ir/latest/userguide/infrastructure-security.html): AWS Security Incident Response is protected by AWS global network security.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/security-ir/latest/userguide/configuration-and-vulnerability-analysis.html): You are responsible for managing the service containment roles and the associated CloudFormation stack sets.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/security-ir/latest/userguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.


## [AWS Security Incident Response Technical Guide](https://docs.aws.amazon.com/security-ir/latest/userguide/security-incident-response-guide.html)

- [Introduction](https://docs.aws.amazon.com/security-ir/latest/userguide/introduction.html): Security is the top priority at AWS.

### [Preparation](https://docs.aws.amazon.com/security-ir/latest/userguide/preparation.html)

Preparing for an incident is critical for timely and effective incident response.

### [People](https://docs.aws.amazon.com/security-ir/latest/userguide/people.html)

To respond to a security event, you need to identify the stakeholders who would support the response to a security event.

- [Define roles and responsibilities](https://docs.aws.amazon.com/security-ir/latest/userguide/define-roles-and-responsibilities.html): Handling security events requires cross-organizational discipline and an inclination for action.

### [Train incident response staff](https://docs.aws.amazon.com/security-ir/latest/userguide/train-incident-response-staff.html)

Training your incident response staff on the technologies their organization uses will be crucial for them to adequately respond to a security event.

- [Understand AWS Cloud technologies](https://docs.aws.amazon.com/security-ir/latest/userguide/understand-cloud-technologies.html): To reduce dependencies and decrease response time, ensure that your security teams and responders are educated about cloud services and have opportunities for hands-on practice with the specific cloud environment that your organization uses.
- [Understand your AWS environment](https://docs.aws.amazon.com/security-ir/latest/userguide/understand-your-environment.html): In addition to understanding AWS services, their use cases, and how they integrate with each other, itâs equally important to understand how your organizationâs AWS environment is actually architected and what operational processes are in place.
- [Understand AWS response teams and support](https://docs.aws.amazon.com/security-ir/latest/userguide/understand-response-teams-and-support.html)

### [Process](https://docs.aws.amazon.com/security-ir/latest/userguide/process.html)

Developing thorough and clearly defined incident response processes is key to a successful and scalable incident response program.

- [Develop and test an incident response plan](https://docs.aws.amazon.com/security-ir/latest/userguide/develop-and-test-incident-response-plan.html): The first document to develop for incident response is the incident response plan.
- [Document and centralize architecture diagrams](https://docs.aws.amazon.com/security-ir/latest/userguide/document-and-centralize-architecture-diagrams.html): To quickly and accurately respond to a security event, you need to understand how your systems and networks are architected.

### [Develop incident response playbooks](https://docs.aws.amazon.com/security-ir/latest/userguide/develop-incident-response-playbooks.html)

A key part of preparing your incident response processes is developing playbooks.

- [What to create playbooks for](https://docs.aws.amazon.com/security-ir/latest/userguide/what-to-create-playbooks-for.html): Playbooks should be created for incident scenarios such as:
- [What to include in playbooks](https://docs.aws.amazon.com/security-ir/latest/userguide/what-to-include-in-playbooks.html): Playbooks should contain technical steps for a security analyst to complete in order to adequately investigate and respond to a potential security incident.
- [Sample playbooks](https://docs.aws.amazon.com/security-ir/latest/userguide/sample-playbooks.html): A number of sample playbooks can be found in Appendix B in .

### [Run regular simulations](https://docs.aws.amazon.com/security-ir/latest/userguide/run-regular-simulations.html)

Organizations grow and evolve over time, as does the threat landscape.

- [Types of simulations](https://docs.aws.amazon.com/security-ir/latest/userguide/types-of-simulations.html): There are three main types of simulations:
- [Exercise lifecycle](https://docs.aws.amazon.com/security-ir/latest/userguide/exercise-lifecycle.html): Regardless of the type of simulation you choose, simulations generally follow these steps:

### [Technology](https://docs.aws.amazon.com/security-ir/latest/userguide/technology.html)

If you develop and implement the appropriate technologies before a security incident, your incident response staff will be able to investigate, understand the scope, and take action in a timely manner.

- [Develop AWS account structure](https://docs.aws.amazon.com/security-ir/latest/userguide/develop-account-structure.html): AWS Organizations helps centrally manage and govern an AWS environment as you grow and scale AWS resources.
- [Develop and implement a tagging strategy](https://docs.aws.amazon.com/security-ir/latest/userguide/develop-and-implement-tagging-strategy.html): Obtaining contextual information on the business use case and relevant internal stakeholders surrounding an AWS resource can be difficult.
- [Update AWS account contact information](https://docs.aws.amazon.com/security-ir/latest/userguide/update-account-contact-info.html): For each of your AWS accounts, itâs important to have accurate and up-to-date contact information so that the correct stakeholders receive important notifications from AWS on topics like security, billing, and operations.
- [Prepare access to AWS accounts](https://docs.aws.amazon.com/security-ir/latest/userguide/prepare-access-to-accounts.html): During an incident, your incident response teams must have access to the environments and resources involved in the incident.
- [Understand the threat landscape](https://docs.aws.amazon.com/security-ir/latest/userguide/understand-threat-landscape.html)

### [Select and set up logs for analysis and alerting](https://docs.aws.amazon.com/security-ir/latest/userguide/select-and-set-up-logs-for-analysis-alerting.html)

During a security investigation, you need to be able to review relevant logs to record and understand the full scope and timeline of the incident.

- [Select and enable log sources](https://docs.aws.amazon.com/security-ir/latest/userguide/select-and-enable-log-sources.html): Ahead of a security investigation, you need to capture relevant logs to retroactively reconstruct activity in an AWS account.
- [Select log storage](https://docs.aws.amazon.com/security-ir/latest/userguide/select-log-storage.html): The choice of log storage is generally related to which querying tool you use, retention capabilities, familiarity, and cost.
- [Identify appropriate log retention](https://docs.aws.amazon.com/security-ir/latest/userguide/identify-appropriate-log-retention.html): When you use an S3 bucket or CloudWatch log group to store logs, you must establish adequate lifecycles for each log source to optimize storage and retrieval costs.
- [Select and implement querying mechanisms for logs](https://docs.aws.amazon.com/security-ir/latest/userguide/select-and-implement-querying-mechanisms.html): In AWS, the main services you can use to query logs are CloudWatch Logs Insights for data stored in CloudWatch log groups, and Amazon Athena and Amazon OpenSearch Service for data stored in Amazon S3.
- [Use logs for alerting](https://docs.aws.amazon.com/security-ir/latest/userguide/use-logs-for-alerting.html): AWS natively provides alerting through security services, such as Amazon GuardDuty, AWS Security Hub CSPM, and AWS Config.

### [Develop forensics capabilities](https://docs.aws.amazon.com/security-ir/latest/userguide/develop-forensics-capabilities.html)

Ahead of a security incident, consider developing forensics capabilities to support security event investigations.

- [Forensics on AWS](https://docs.aws.amazon.com/security-ir/latest/userguide/forensics.html): Concepts from traditional on-premises forensics apply to AWS.
- [Capture backups and snapshots](https://docs.aws.amazon.com/security-ir/latest/userguide/capture-backups-and-snapshots.html): Setting up backups of key systems and databases are critical for recovering from a security incident and for forensics purposes.
- [Automation of forensics on AWS](https://docs.aws.amazon.com/security-ir/latest/userguide/automate-forensics.html): During a security event, your incident response team must be able to collect and analyze evidence quickly while maintaining accuracy for the time period surrounding the event.
- [Summary of preparation items](https://docs.aws.amazon.com/security-ir/latest/userguide/preparation-summary.html): Thorough preparation for responding to security events is critical for timely and effective incident response.

### [Operations](https://docs.aws.amazon.com/security-ir/latest/userguide/operations.html)

Operations is the core of performing incident response.

### [Detection](https://docs.aws.amazon.com/security-ir/latest/userguide/detection.html)

An alert is the main component of the detection phase.

- [Alert sources](https://docs.aws.amazon.com/security-ir/latest/userguide/alert-sources.html): You should consider using the following sources to define alerts:
- [Detection as part of security control engineering](https://docs.aws.amazon.com/security-ir/latest/userguide/detection-as-security-control-engineering.html): Detection mechanisms are an integral part of security control development.
- [Detective control implementations](https://docs.aws.amazon.com/security-ir/latest/userguide/detective-control-implementations.html): It is important to understand how detective controls are implemented because they help determine how the alert will be used for the particular event.
- [People-based detection](https://docs.aws.amazon.com/security-ir/latest/userguide/people-based-detection.html): Up to this point, we have discussed technology-based detection.
- [Summary](https://docs.aws.amazon.com/security-ir/latest/userguide/detection-summary.html): With detection, itâs important to have a mix of rule-based and behavioral driven alerting.

### [Analysis](https://docs.aws.amazon.com/security-ir/latest/userguide/analysis.html)

Logs, query capabilities, and threat intelligence are a few of the supporting components required by the analysis phase.

- [Validate, scope, and assess impact of alert](https://docs.aws.amazon.com/security-ir/latest/userguide/validate-scope-assess-alert-impact.html): During the analysis phase, comprehensive log analysis is performed with the goal to validate alerts, define scope, and assess the impact of the possible compromise.
- [Enrich security logs and findings](https://docs.aws.amazon.com/security-ir/latest/userguide/enrich-security-logs-and-findings.html)

### [Collect and analyze forensic evidence](https://docs.aws.amazon.com/security-ir/latest/userguide/collect-analyze-forensic-evidence.html)

Forensics, as mentioned in the section of this document, is the process of collecting and analyzing artifacts during incident response.

- [Collect relevant artifacts](https://docs.aws.amazon.com/security-ir/latest/userguide/collect-relevant-artifacts.html): With these characteristics in mind, and based on the relevant alerts and assessment of impact and scope, you will need to collect the data that will be relevant to further investigation and analysis.
- [Develop narratives](https://docs.aws.amazon.com/security-ir/latest/userguide/develop-narratives.html): During analysis and investigation, document the actions taken, analysis performed, and information identified, to be used by the subsequent phases and ultimately a final report.

### [Containment](https://docs.aws.amazon.com/security-ir/latest/userguide/containment.html)

One definition of containment, as it relates to incident response, is the process or implementation of a strategy during the handling of a security event that acts to minimize the scope of the security event and contain the effects of unauthorized usage within the environment.

- [Source containment](https://docs.aws.amazon.com/security-ir/latest/userguide/source-containment.html): Source containment is the use and application of filtering or routing within an environment to prevent access to resources from a specific source IP address or network range.
- [Technique and access containment](https://docs.aws.amazon.com/security-ir/latest/userguide/technique-access-containment.html): Prevent unauthorized use of a resource by limiting the functions and IAM principals with access to the resource.
- [Destination containment](https://docs.aws.amazon.com/security-ir/latest/userguide/destination-containment.html): Destination containment is the application of filtering or routing within an environment to prevent access to a targeted host or resource.
- [Summary](https://docs.aws.amazon.com/security-ir/latest/userguide/containment-summary.html): Containment is one step of the incident response process and can be manual or automated.
- [Eradication](https://docs.aws.amazon.com/security-ir/latest/userguide/eradication.html): Eradication, in relation to security incident response, is the removal of suspicious or unauthorized resources in efforts to return the account to a known safe state.
- [Recovery](https://docs.aws.amazon.com/security-ir/latest/userguide/recovery.html): Recovery is the process of restoring systems to a known safe state, validating that backups are safe or unaffected by the incident prior to restoration, testing to verify that the systems are working properly post-restoration, and addressing vulnerabilities associated with the security event.
- [Conclusion](https://docs.aws.amazon.com/security-ir/latest/userguide/operations-conclusion.html): Each operations phase has unique goals, techniques, methodologies, and strategies.

### [Post-incident activity](https://docs.aws.amazon.com/security-ir/latest/userguide/post-incident-activity.html)

The threat landscape is constantly changing and it is important to be equally dynamic in your organizationâs ability to effectively protect your environments.

- [Establish a framework for learning from incidents](https://docs.aws.amazon.com/security-ir/latest/userguide/establish-framework-for-learning.html): Implementing a lessons learned framework and methodology will not only help to improve incident response capabilities, but also help to prevent the incident from recurring.

### [Establish metrics for success](https://docs.aws.amazon.com/security-ir/latest/userguide/establish-metrics-for-success.html)

Metrics are necessary to effectively measure, assess, and improve your incident response capabilities.

- [Mean time to detect](https://docs.aws.amazon.com/security-ir/latest/userguide/mean-time-to-detect.html): Mean time to detect is the average time it takes to discover a possible security incident.
- [Mean time to acknowledge](https://docs.aws.amazon.com/security-ir/latest/userguide/mean-time-to-acknowledge.html): Mean time to acknowledge is the average time it takes to acknowledge and prioritize a possible security incident.
- [Mean time to respond](https://docs.aws.amazon.com/security-ir/latest/userguide/mean-time-to-respond.html): Mean time to respond is the average time it takes to begin the initial response to a possible security incident.
- [Mean time to contain](https://docs.aws.amazon.com/security-ir/latest/userguide/mean-time-to-contain.html): Mean time to contain is the average time it takes to contain a possible security incident.
- [Mean time to recover](https://docs.aws.amazon.com/security-ir/latest/userguide/mean-time-to-recover.html): Mean time to recover is the average time it takes to fully return so safe operations from a possible security incident.
- [Attacker dwell time](https://docs.aws.amazon.com/security-ir/latest/userguide/attacker-dwell-time.html): Attacker dwell time is the average time that an unauthorized user has access to a systems or environment.
- [Metrics summary](https://docs.aws.amazon.com/security-ir/latest/userguide/metrics-summary.html): Establishing and tracking metrics for incident response allows you to effectively measure, assess, and improve your incident response capabilities.
- [Use indicators of compromise](https://docs.aws.amazon.com/security-ir/latest/userguide/use-indicators-of-compromise.html): An indicator of compromise (IOC) is an artifact observed in or on a network, system, or environment that can (with a high level of confidence) identify malicious activity or a security incident.
- [Continuous education and training](https://docs.aws.amazon.com/security-ir/latest/userguide/continuous-education-and-training.html): Education and training are both evolving and continual efforts that should be purposefully pursued and maintained.
- [Conclusion](https://docs.aws.amazon.com/security-ir/latest/userguide/conclusion.html): Conclusion
- [Contributors](https://docs.aws.amazon.com/security-ir/latest/userguide/contributors.html): Contributors

### [Appendix A: Cloud capability definitions](https://docs.aws.amazon.com/security-ir/latest/userguide/appendix-a-cloud-capability-definitions.html)

AWS offers over 200 cloud services and thousands of features.

- [Logging and events](https://docs.aws.amazon.com/security-ir/latest/userguide/logging-and-events.html): AWS CloudTrail â AWS CloudTrail service enabling governance, compliance, operational auditing, and risk auditing of AWS accounts.
- [Visibility and alerting](https://docs.aws.amazon.com/security-ir/latest/userguide/visibility-and-alerting.html): AWS Security Incident Response â AWS Security Incident Response is a comprehensive service that helps organizations handle security events throughout their lifecycle by combining automated capabilities with expert human support.
- [Automation](https://docs.aws.amazon.com/security-ir/latest/userguide/automation-1.html): AWS Lambda â AWS Lambda is a serverless compute service that runs your code in response to events, and automatically manages the underlying compute resources for you.
- [Secure storage](https://docs.aws.amazon.com/security-ir/latest/userguide/secure-storage.html): Amazon Simple Storage Service â Amazon S3 is object storage built to store and retrieve any amount of data from anywhere.
- [Future and Custom Security Capabilities](https://docs.aws.amazon.com/security-ir/latest/userguide/custom.html): The aforementioned services and features are not an exhaustive list.
- [Appendix B: AWS incident response resources](https://docs.aws.amazon.com/security-ir/latest/userguide/appendix-b-incident-response-resources.html): AWS publishes resources to assist customers with developing incident response capabilities.
- [Notices](https://docs.aws.amazon.com/security-ir/latest/userguide/notices.html): Notices
