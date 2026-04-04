# Source: https://docs.aws.amazon.com/ses/latest/dg/llms.txt

# Amazon Simple Email Service Developer Guide

> Create a highly-scalable and flexible email sending and receiving platform using Amazon SES. This Developer Guide provides information and procedures for configuring your Amazon SES account to send and receive email.

- [Tenants - NEW](https://docs.aws.amazon.com/ses/latest/dg/tenants.html)
- [Global endpoints](https://docs.aws.amazon.com/ses/latest/dg/global-endpoints.html)
- [Monitoring using EventBridge](https://docs.aws.amazon.com/ses/latest/dg/monitoring-eventbridge.html)
- [Quick Find Index](https://docs.aws.amazon.com/ses/latest/dg/quick-find.html)

## [What is Amazon SES?](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html)

- [Regions](https://docs.aws.amazon.com/ses/latest/dg/regions.html): Provides information about Regions and endpoints in Amazon SES.
- [Quotas](https://docs.aws.amazon.com/ses/latest/dg/quotas.html): Lists and describes the quotas that apply to Amazon SES resources and operations.
- [Types of credentials](https://docs.aws.amazon.com/ses/latest/dg/send-email-concepts-credentials.html): Describes the different types of security credentials you might need when you use Amazon SES.

### [How Amazon SES works](https://docs.aws.amazon.com/ses/latest/dg/send-email-concepts-process.html)

Describes what happens when you send an email with Amazon SES, and the various outcomes that can occur after the email is sent.

- [Email format](https://docs.aws.amazon.com/ses/latest/dg/send-email-concepts-email-format.html): Describes the format of email messages and the information you need to provide to Amazon SES to construct an email.
- [Understanding deliverability](https://docs.aws.amazon.com/ses/latest/dg/send-email-concepts-deliverability.html): Describes the email deliverability concepts that you should be familiar with when you use Amazon SES.

### [Email best practices](https://docs.aws.amazon.com/ses/latest/dg/best-practices.html)

Best practices for Amazon Simple Email Service email sending, including guidance for message content, recipient list quality, and your email sending infrastructure.

- [Success metrics](https://docs.aws.amazon.com/ses/latest/dg/success-metrics.html): Success metrics for Amazon SES email programs.
- [Maintaining a positive sender reputation](https://docs.aws.amazon.com/ses/latest/dg/tips-and-best-practices.html): Maintaining a positive sender reputation in Amazon SES.
- [Working with AWS SDKs](https://docs.aws.amazon.com/ses/latest/dg/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.


## [Getting started](https://docs.aws.amazon.com/ses/latest/dg/getting-started.html)

- [Setting up](https://docs.aws.amazon.com/ses/latest/dg/setting-up.html): Learn how to prepare to use Amazon SES.
- [Migrating to Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/send-email-getting-started-migrate.html): Provides information about moving your email-sending solution to Amazon SES from one that's hosted on-premises or on Amazon EC2.
- [Request production access](https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html): Request production access by moving your account out of the Amazon SES sandbox and raise your sending quotas.


## [Sending limits](https://docs.aws.amazon.com/ses/latest/dg/manage-sending-quotas.html)

- [Increasing your sending quotas](https://docs.aws.amazon.com/ses/latest/dg/manage-sending-quotas-request-increase.html): Describes how to increase the sending quotas for your Amazon SES account.
- [Monitoring your sending quotas](https://docs.aws.amazon.com/ses/latest/dg/manage-sending-quotas-monitor.html): Monitor your sending quotas by using the Amazon SES console or the Amazon SES API.
- [Sending quota errors](https://docs.aws.amazon.com/ses/latest/dg/manage-sending-quotas-errors.html): Describes the errors you might encounter if you reach the sending quotas for your Amazon SES account.


## [Set up email sending](https://docs.aws.amazon.com/ses/latest/dg/send-email.html)

### [Using the SMTP interface](https://docs.aws.amazon.com/ses/latest/dg/send-email-smtp.html)

Send email through Amazon SES by using the SMTP interface.

- [Obtaining SMTP credentials](https://docs.aws.amazon.com/ses/latest/dg/smtp-credentials.html): Get your Amazon SES SMTP user name and password so you can access the Amazon SES SMTP interface.
- [Connecting to an SMTP endpoint](https://docs.aws.amazon.com/ses/latest/dg/smtp-connect.html): Lists the Amazon SES SMTP endpoints for the regions in which Amazon SES is available.
- [Using software packages to send email](https://docs.aws.amazon.com/ses/latest/dg/send-email-smtp-software-package.html): Configure commercial and open source SMTP-enabled software packages to send email through Amazon SES.
- [Sending emails programmatically](https://docs.aws.amazon.com/ses/latest/dg/send-using-smtp-programmatically.html): Send email through the Amazon SES SMTP interface using an SMTP-enabled compatible programming language.

### [Integrating with your existing email server](https://docs.aws.amazon.com/ses/latest/dg/send-email-smtp-existing-server.html)

Integrate your existing email server to use the Amazon SES SMTP endpoint to send all of your outgoing email.

- [Integrating with Postfix](https://docs.aws.amazon.com/ses/latest/dg/postfix.html): Configure Postfix to send email through Amazon SES.
- [Integrating with Sendmail](https://docs.aws.amazon.com/ses/latest/dg/send-email-sendmail.html): Configure Sendmail to send email through Amazon SES.
- [Integrating with Microsoft Windows Server IIS SMTP](https://docs.aws.amazon.com/ses/latest/dg/send-email-windows-server.html): Configure Windows Server to send email through Amazon SES.
- [Testing your connection to the Amazon SES SMTP interface](https://docs.aws.amazon.com/ses/latest/dg/send-email-smtp-client-command-line.html): Use common command line utilities to test your connection to the Amazon SES SMTP interface.

### [Using the API](https://docs.aws.amazon.com/ses/latest/dg/send-email-api.html)

Use the Amazon SES API to send email through Amazon SES using HTTPS.

- [Sending formatted email](https://docs.aws.amazon.com/ses/latest/dg/send-email-formatted.html): Send a formatted email by calling the Amazon SES API through an application.
- [Sending raw email](https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html): Use the Amazon SES raw email interface to send highly customized messages such as messages that contain attachments.

### [Using templates to send email](https://docs.aws.amazon.com/ses/latest/dg/send-personalized-email-api.html)

Use the Amazon SES CreateTemplate and SendBulkEmail operations to send personalized messages.

- [Advanced email personalization](https://docs.aws.amazon.com/ses/latest/dg/send-personalized-email-advanced.html): Use Handlebars helpers to create advanced email templates.
- [Managing email templates](https://docs.aws.amazon.com/ses/latest/dg/send-personalized-email-manage-templates.html): Contains information about managing Amazon SES email templates.

### [Sending email using an AWS SDK](https://docs.aws.amazon.com/ses/latest/dg/send-an-email-using-sdk-programmatically.html)

Send an email through Amazon SES using an AWS SDK to call the Amazon SES API.

- [Creating a shared credentials file](https://docs.aws.amazon.com/ses/latest/dg/create-shared-credentials-file.html): Create a shared credentials file, which is used in the SDK examples for .NET, Java, PHP, Python, and Ruby.
- [Content encodings](https://docs.aws.amazon.com/ses/latest/dg/content-encodings.html): The following is provided for reference.
- [Supported security protocols](https://docs.aws.amazon.com/ses/latest/dg/security-protocols.html): Explains the security protocols that Amazon SES supports.
- [Supported header fields](https://docs.aws.amazon.com/ses/latest/dg/header-fields.html): Describes the header fields that Amazon SES accepts.
- [Email attachments](https://docs.aws.amazon.com/ses/latest/dg/attachments.html): Learn how to work with email attachments when sending emails through Amazon Simple Email Service (Amazon SES)


## [Email receiving](https://docs.aws.amazon.com/ses/latest/dg/receiving-email.html)

- [Email receiving concepts & use cases](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-concepts.html): Overview of Amazon SES email receiving concepts.

### [Setting up email receiving](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-setting-up.html)

Overview of how to set up Amazon SES email receiving.

- [Verifying your domain](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-verification.html): Explains why you need to verify your domain when you receive emails using Amazon SES.
- [Publishing an MX record](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-mx-record.html): Provides information about adding a DNS record to your domain's DNS configuration that enables Amazon SES to receive email sent to your domain.
- [Giving permission](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-permissions.html): Explains the permissions that you need to put in place when you receive emails using Amazon SES.

### [Email receiving console walkthroughs](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-walkthroughs.html)

Introduction to Amazon SES email receiving walkthroughs.

### [Creating receipt rules](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html)

Describes how to set up receipt rules using the Amazon SES console.

### [Action options](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action.html)

Explains how to set up actions within receipt rules for Amazon SES email receiving.

- [Add header](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-add-header.html): Explains how to set up the Add Header action for Amazon SES email receiving.
- [Return bounce response](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-bounce.html): Explains how to set up the Bounce action for Amazon SES email receiving.

### [Invoke Lambda function](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-lambda.html)

Explains how to set up the Lambda action for Amazon SES email receiving.

- [Sample incoming email event](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-lambda-event.html): Includes a sample event that Amazon SES sends to Lambda when an incoming email is received.
- [Use case examples](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-lambda-example-use-cases.html): Provides example use cases for using a Lambda function for Amazon SES email receiving.
- [Lambda function examples](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-lambda-example-functions.html): Provides example Lambda functions that you can use with Amazon SES email receiving
- [Deliver to S3 bucket](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-s3.html): Explains how to set up the S3 action for Amazon SES email receiving.

### [Publish to Amazon SNS topic](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-sns.html)

Explains how to set up the SNS action for Amazon SES email receiving.

- [Notification contents](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-notifications-contents.html): Describes Amazon SES email-receiving notification contents.
- [Notification examples](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-notifications-examples.html): Provides examples of Amazon SES email-receiving notifications.
- [Stop rule set](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-stop.html): Explains how to set up the Stop action for Amazon SES email receiving.
- [Integrate with Amazon WorkMail](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-workmail.html): Explains how to set up the WorkMail action for Amazon SES email receiving.
- [Create IP filters](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-ip-filtering-console-walkthrough.html): Describes how to set up IP address filters using the Amazon SES console.
- [Email receiving metrics](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-metrics.html): Explains how to view your email-receiving metrics.


## [Verified identities](https://docs.aws.amazon.com/ses/latest/dg/verify-addresses-and-domains.html)

- [Creating & verifying identities](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html): Create an identity at the domain level or can create email address identities.

### [Managing identities](https://docs.aws.amazon.com/ses/latest/dg/managing-identities.html)

View a list of identities, edit an identity, or delete an identity.

- [View identities using the console](https://docs.aws.amazon.com/ses/latest/dg/view-verified-domains.html): View the identities you have verified with Amazon SES.
- [Delete an identity using the console](https://docs.aws.amazon.com/ses/latest/dg/remove-verified-domain.html): Remove an identity you have verified with Amazon SES.
- [Edit an identity using the console](https://docs.aws.amazon.com/ses/latest/dg/edit-verified-domain.html): Edit an identity you have verified with Amazon SES.
- [Edit an identity to use a default configuration set using the SES API](https://docs.aws.amazon.com/ses/latest/dg/managing-configuration-sets-default-adding.html): You can use the PutEmailIdentityConfigurationSetAttributes operation to add or remove a default configuration set from an existing email identity.
- [Retrieve the default configuration set used by the identity using the SES API](https://docs.aws.amazon.com/ses/latest/dg/managing-configuration-sets-default-returning.html): You can use the GetEmailIdentity operation to return the default configuration set for an email identity, if applicable.
- [Override the current default configuration set used by the identity using the SES API](https://docs.aws.amazon.com/ses/latest/dg/managing-configuration-sets-default-overriding.html): You can use the SendEmail operation to send email with a different configuration set.

### [Configuring identities](https://docs.aws.amazon.com/ses/latest/dg/configure-identities.html)

Describes two authentication mechanisms ISPs use and provides instructions for how to use these standards with Amazon SES.

### [Email authentication methods](https://docs.aws.amazon.com/ses/latest/dg/email-authentication-methods.html)

Describes the authentication methods.

### [Authenticating Email with DKIM](https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim.html)

Walks through how to authenticate email with DomainKeys Identified Mail (DKIM) in Amazon SES.

- [Easy DKIM](https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-easy.html): Configure Easy DKIM settings and enable or disable automatic DKIM signing for your email messages using the Amazon SES console.
- [Deterministic Easy DKIM (DEED)](https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-deed.html): Learn how to use Deterministic Easy DKIM (DEED) with Amazon SES for consistent DKIM signing across multiple AWS Regions.
- [BYODKIM - Bring Your Own DKIM](https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-bring-your-own.html): Configure Amazon SES to perform DKIM authentication using a public-private key pair that you specify.
- [Managing Easy DKIM & BYODKIM](https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-easy-managing.html): You can manage the DKIM settings for your identities authenticated with either Easy DKIM or BYODKIM by using the web-based Amazon SES console, or by using the Amazon SES API.
- [Manual DKIM signing](https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-manual.html): Manually sign your email messages using a DKIM signature and send them using Amazon SES.
- [Authenticating Email with SPF](https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-spf.html): Provides information about authenticating email by using Sender Policy Framework.
- [Using a custom MAIL FROM domain](https://docs.aws.amazon.com/ses/latest/dg/mail-from.html): Configure a custom MAIL FROM domain for Amazon SES.
- [Authenticating Email with DMARC](https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dmarc.html): Describes how to authenticate email with DMARC with Amazon SES.
- [Using BIMI in SES](https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-bimi.html): Describes how to configure BIMI in Amazon SES.

### [Setting up event notifications](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity-using-notifications.html)

Monitor Amazon SES sending by using notifications.

- [Receive notifications through email](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity-using-notifications-email.html): Receive notifications about bounces and complaints for emails that you send through Amazon SES.

### [Receive notifications using Amazon SNS](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity-using-notifications-sns.html)

Receive Amazon SNS feedback notifications about bounces and complaints for emails that you send through Amazon SES.

- [Configuring Amazon SNS notifications](https://docs.aws.amazon.com/ses/latest/dg/configure-sns-notifications.html): Configure Amazon SNS notifications for Amazon SES on a per-verified-identity basis.
- [Notification contents](https://docs.aws.amazon.com/ses/latest/dg/notification-contents.html): Describes the content of Amazon SES notifications that are published to Amazon SNS in JavaScript Object Notation (JSON) format.
- [Notification examples](https://docs.aws.amazon.com/ses/latest/dg/notification-examples.html): Amazon SNS notification examples for Amazon SES.

### [Using identity authorization](https://docs.aws.amazon.com/ses/latest/dg/identity-authorization-policies.html)

Provides detailed information about Amazon SES authorization policies.

- [Policy anatomy](https://docs.aws.amazon.com/ses/latest/dg/policy-anatomy.html): The structure, elements, and requirements of a policy.

### [Creating an identity authorization policy](https://docs.aws.amazon.com/ses/latest/dg/identity-authorization-policies-creating.html)

Provides detailed information about Amazon SES authorization policies.

- [Using the policy generator](https://docs.aws.amazon.com/ses/latest/dg/using-policy-generator.html): Create a policy using the policy generator.
- [Creating a custom policy](https://docs.aws.amazon.com/ses/latest/dg/creating-custom-policy.html): Create a custom policy and attach it to an identity.
- [Identity policy examples](https://docs.aws.amazon.com/ses/latest/dg/identity-authorization-policy-examples.html): Provides examples of Amazon SES sending authorization policies.
- [Managing your policies](https://docs.aws.amazon.com/ses/latest/dg/managing-policies.html): View, list, edit, delete or remove a policy.

### [Using sending authorization](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html)

Describes how to use Amazon SES sending authorization.

- [Overview of sending authorization](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-overview.html): Provides an overview of Amazon SES sending authorization.

### [Identity owner tasks](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-identity-owner-tasks.html)

Describes the tasks required for an identity owner to enable another sender to send on their behalf.

- [Verifying an identity](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-identity-owner-tasks-verification.html): Describes why the identity owner must verify the identity to use for Amazon SES sending authorization.
- [Setting up notifications](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-identity-owner-tasks-notifications.html): Describes how an identity owner can set up notifications for an identity they're using for Amazon SES sending authorization.
- [Getting information from the delegate sender](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-identity-owner-tasks-information.html): Describes the information that the identity owner needs to get from the identity owner for Amazon SES sending authorization.
- [Creating a sending authorization policy](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-identity-owner-tasks-policy.html): Describes how an identity owner can create an Amazon SES sending authorization policy.
- [Sending policy examples](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-policy-examples.html): Provides examples of Amazon SES sending authorization policies.
- [Providing the delegate sender with the identity information](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-identity-owner-tasks-identity.html): Describes how an identity owner can find the ARN of an identity they are using for Amazon SES sending authorization.

### [Delegate sender tasks](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-delegate-sender-tasks.html)

Describes the tasks required for a delegate sender to send on behalf of another Amazon SES sender.

- [Providing information to the identity owner](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-delegate-sender-tasks-information.html): Describes the information that the delegate sender needs to provide the identity owner for Amazon SES sending authorization.
- [Using delegate sender notifications](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-delegate-sender-tasks-notifications.html): Describes how the delegate sender can set up notifications when using Amazon SES sending authorization.
- [Sending emails for the identity owner](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-delegate-sender-tasks-email.html): Describes how the delegate sender can send email for the identity owner when using Amazon SES sending authorization.
- [Sending test emails with the simulator](https://docs.aws.amazon.com/ses/latest/dg/send-an-email-from-console.html): Send an email to yourself from the Amazon SES console for the easiest way to experiment with sending emails using Amazon SES.


## [Configuration sets](https://docs.aws.amazon.com/ses/latest/dg/using-configuration-sets.html)

- [Create configuration sets](https://docs.aws.amazon.com/ses/latest/dg/creating-configuration-sets.html): Create configuration sets with SES.

### [Manage configuration sets](https://docs.aws.amazon.com/ses/latest/dg/managing-configuration-sets.html)

Manage configuration sets with Amazon SES.

- [Create event destinations](https://docs.aws.amazon.com/ses/latest/dg/event-destinations-manage.html): Creating event destinations with Amazon SES.
- [Assign IP pools](https://docs.aws.amazon.com/ses/latest/dg/managing-ip-pools.html): Manage IP pools with Amazon SES.
- [Configure custom open and click domains](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html): Includes procedures for configuring a subdomain to handle open and click tracking link redirects.
- [Specify configuration sets in email](https://docs.aws.amazon.com/ses/latest/dg/using-configuration-sets-in-email.html): Provides procedures and information for specifying a configuration set when sending email using Amazon SES.
- [View and export reputation metrics](https://docs.aws.amazon.com/ses/latest/dg/configuration-sets-export-metrics.html): Includes procedures for exporting reputation metrics (such as bounce or complaint rates) for configuration sets to Amazon CloudWatch.


## [Dedicated IP addresses](https://docs.aws.amazon.com/ses/latest/dg/dedicated-ip.html)

### [Standard](https://docs.aws.amazon.com/ses/latest/dg/manual-dedicated-ips.html)

Describes how to manually set up dedicated IP addresses with Amazon SES.

- [Request & relinquish](https://docs.aws.amazon.com/ses/latest/dg/dedicated-ip-case.html): Describes how to request and release Dedicated IP addresses Standard with Amazon SES.
- [Warming up](https://docs.aws.amazon.com/ses/latest/dg/dedicated-ip-warming.html): Describes how to warm up standard dedicated IP addresses with Amazon SES.
- [Creating pools](https://docs.aws.amazon.com/ses/latest/dg/dedicated-ip-pools.html): Describes how to create dedicated IP pools.
- [Dedicated IP addresses (managed)](https://docs.aws.amazon.com/ses/latest/dg/managed-dedicated-sending.html): Describes how to use dedicated IP addresses (managed) for dedicated IP addresses with Amazon SES.
- [Bring your own IP addresses](https://docs.aws.amazon.com/ses/latest/dg/dedicated-ip-byo.html): Includes information about using your own IP addresses to send email through Amazon SES.


## [Virtual Deliverability Manager](https://docs.aws.amazon.com/ses/latest/dg/vdm.html)

- [Getting started](https://docs.aws.amazon.com/ses/latest/dg/vdm-get-started.html): Describes how to get started with Virtual Deliverability Manager and Virtual Deliverability Manager account settings in Amazon SES.
- [Dashboard](https://docs.aws.amazon.com/ses/latest/dg/vdm-dashboard.html): Describes how to use Dashboard in Virtual Deliverability Manager in Amazon SES.
- [Advisor](https://docs.aws.amazon.com/ses/latest/dg/vdm-advisor.html): Describes how to use Advisor in Virtual Deliverability Manager in Amazon SES.
- [Settings](https://docs.aws.amazon.com/ses/latest/dg/vdm-settings.html): Describes how to edit Virtual Deliverability Manager account settings in Amazon SES.


## [Email Validation](https://docs.aws.amazon.com/ses/latest/dg/email-validation.html)

- [Email Validation API](https://docs.aws.amazon.com/ses/latest/dg/email-validation-api.html): Describes how to use the Email Validation API in Amazon SES.
- [Auto Validation](https://docs.aws.amazon.com/ses/latest/dg/email-validation-auto.html): Describes how to use Auto Validation in Amazon SES.
- [Email Validation Dashboard](https://docs.aws.amazon.com/ses/latest/dg/email-validation-dashboard.html): Describes how to use the Email Validation Dashboard in Amazon SES.


## [Mail Manager](https://docs.aws.amazon.com/ses/latest/dg/eb.html)

- [Getting started](https://docs.aws.amazon.com/ses/latest/dg/eb-getting-started.html): Describes getting started with Mail Manager in Amazon SES.
- [Ingress endpoints](https://docs.aws.amazon.com/ses/latest/dg/eb-ingress.html): Describes how to use ingress endpoint in Mail Manager in Amazon SES.
- [Traffic policies & policy statements](https://docs.aws.amazon.com/ses/latest/dg/eb-filters.html): Describes how to use traffic policies and policy statements in Mail Manager in Amazon SES.
- [Rule sets & rules](https://docs.aws.amazon.com/ses/latest/dg/eb-rules.html): Describes how to use rules sets and rules in Mail Manager in Amazon SES.
- [SMTP relay](https://docs.aws.amazon.com/ses/latest/dg/eb-relay.html): Describes how to use SMTP relay in Mail Manager in Amazon SES.
- [Address Lists](https://docs.aws.amazon.com/ses/latest/dg/eb-addlist.html): Learn how to create, manage, and use recipient lists in Amazon SES to filter and process email messages.
- [Email archiving](https://docs.aws.amazon.com/ses/latest/dg/eb-archiving.html): Describes how to use archiving in Mail Manager in Amazon SES.
- [Email Add Ons](https://docs.aws.amazon.com/ses/latest/dg/eb-addons.html): Describes how to use Email Add Ons in Mail Manager in Amazon SES.
- [Permission policies](https://docs.aws.amazon.com/ses/latest/dg/eb-policies.html): Describes the required permission policies for Mail Manager in Amazon SES.
- [Logging](https://docs.aws.amazon.com/ses/latest/dg/eb-logging.html): Learn about Mail Manager logging and how to configure and interpret logs.


## [Lists and subscriptions](https://docs.aws.amazon.com/ses/latest/dg/lists-and-subscriptions.html)

- [Global suppression list](https://docs.aws.amazon.com/ses/latest/dg/sending-email-global-suppression-list.html): Provides information about the Amazon SES global suppression list, and includes information about removing addresses from it.
- [Using the account-level suppression list](https://docs.aws.amazon.com/ses/latest/dg/sending-email-suppression-list.html): Provides information about using the account-level suppression list to prevent sending email to addresses that produced bounces or complaints.
- [Using configuration set-level suppression](https://docs.aws.amazon.com/ses/latest/dg/sending-email-suppression-list-config-level.html): Provides information about using the configuration set-level suppression list to prevent sending email to addresses that produced bounces or complaints while overriding the account-level suppression list.
- [Using list management](https://docs.aws.amazon.com/ses/latest/dg/sending-email-list-management.html): Provides information about creating and managing contact lists.
- [Using subscription management](https://docs.aws.amazon.com/ses/latest/dg/sending-email-subscription-management.html): Provides information about configuring Amazon SES to add an email footer unsubscribe link and/or a list-unsubscribe header to enable end users to unsubscribe from a list or from all customer emails.


## [Monitoring sending activity](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html)

- [Monitoring using the console](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity-console.html): Monitor by using the Amazon SES console.
- [Monitor using the API](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity-api.html): The Amazon SES API provides the GetSendStatistics operation, which returns information about your service usage.

### [Monitor email sending using event publishing](https://docs.aws.amazon.com/ses/latest/dg/monitor-using-event-publishing.html)

Monitor by using Amazon SES event publishing.

### [Setting up event publishing](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-using-event-publishing-setup.html)

Set up event publishing with Amazon SES

- [Step 1: Create a configuration set](https://docs.aws.amazon.com/ses/latest/dg/event-publishing-create-configuration-set.html): Create a configuration set for Amazon SES event publishing.

### [Step 2: Add event destination](https://docs.aws.amazon.com/ses/latest/dg/event-publishing-add-event-destination.html)

Add an event destination to a configuration set for event publishing.

- [Set up a CloudWatch destination](https://docs.aws.amazon.com/ses/latest/dg/event-publishing-add-event-destination-cloudwatch.html): Setting up a CloudWatch event destination to use with Amazon SES event publishing
- [Set Up a Data Firehose destination](https://docs.aws.amazon.com/ses/latest/dg/event-publishing-add-event-destination-firehose.html): Setting up a Firehose event destination to use with Amazon SES event publishing
- [Set up an EventBridge destination](https://docs.aws.amazon.com/ses/latest/dg/event-publishing-add-event-destination-eventbridge.html): Set up an Amazon EventBridge event destination to use with Amazon SES event publishing.
- [Set up an Amazon Pinpoint destination](https://docs.aws.amazon.com/ses/latest/dg/event-publishing-add-event-destination-pinpoint.html): Set up an Amazon Pinpoint event destination to use with Amazon SES event publishing.
- [Set up an Amazon SNS destination](https://docs.aws.amazon.com/ses/latest/dg/event-publishing-add-event-destination-sns.html): Set up an Amazon SNS event destination to use with Amazon SES event publishing.
- [Step 3: Specify your configuration set when sending](https://docs.aws.amazon.com/ses/latest/dg/event-publishing-send-email.html): Specify a configuration set that uses your event destination when you send email using Amazon SES.

### [Working with event data](https://docs.aws.amazon.com/ses/latest/dg/working-with-event-data.html)

Contains information about retrieving and interpreting Amazon SES event publishing data.

- [Retrieving event data from CloudWatch](https://docs.aws.amazon.com/ses/latest/dg/event-publishing-retrieving-cloudwatch.html): Retrieving Amazon SES event data from Amazon CloudWatch.

### [Retrieving event data from Firehose](https://docs.aws.amazon.com/ses/latest/dg/event-publishing-retrieving-firehose.html)

Retrieving Amazon SES event data from Amazon Data Firehose.

- [Event record contents](https://docs.aws.amazon.com/ses/latest/dg/event-publishing-retrieving-firehose-contents.html): Information about the event data that Amazon SES publishes to Firehose.
- [Event record examples](https://docs.aws.amazon.com/ses/latest/dg/event-publishing-retrieving-firehose-examples.html): Retrieving event data from Amazon Data Firehose with Amazon SES

### [Interpreting event data from Amazon SNS](https://docs.aws.amazon.com/ses/latest/dg/event-publishing-retrieving-sns.html)

Information about interpreting the Amazon SES event publishing data provided by Amazon Simple Notification Service.

- [Event record contents](https://docs.aws.amazon.com/ses/latest/dg/event-publishing-retrieving-sns-contents.html): Information about retrieving Amazon SES event data in Amazon SNS.
- [Event record examples](https://docs.aws.amazon.com/ses/latest/dg/event-publishing-retrieving-sns-examples.html): This section provides examples of the types of email sending event records that Amazon SES publishes to Amazon SNS.


## [Monitoring sender reputation](https://docs.aws.amazon.com/ses/latest/dg/monitor-sender-reputation.html)

- [Using reputation metrics](https://docs.aws.amazon.com/ses/latest/dg/reputation-dashboard-dg.html): The reputation metrics console page contains the same information that the Amazon SES team sees when determining the health of individual accounts.
- [Reputation metrics messages](https://docs.aws.amazon.com/ses/latest/dg/reputationdashboardmessages.html): Additional information about messages that users might encounter when using the Amazon SES Reputation metrics console page.
- [Creating alarms using CloudWatch](https://docs.aws.amazon.com/ses/latest/dg/reputationdashboard-cloudwatch-alarm.html): Procedures for creating an alarm in CloudWatch that notifies you when your account's reputation metrics reach certain levels.
- [SNDS metrics for dedicated IPs](https://docs.aws.amazon.com/ses/latest/dg/snds-metrics-dedicated-ips.html): Describes how to view SNDS metrics for dedicated IP addresses.

### [Automatically pausing email sending](https://docs.aws.amazon.com/ses/latest/dg/monitoring-sender-reputation-pausing.html)

Includes information about protecting your sender reputation by automatically pausing Amazon SES email sending when reputation metrics exceed certain thresholds.

- [For your entire account](https://docs.aws.amazon.com/ses/latest/dg/monitoring-sender-reputation-pausing-account.html): The procedures in this section explain the steps to set up Amazon SES, Amazon SNS, Amazon CloudWatch, and AWS Lambda to automatically pause email sending for your Amazon SES account in a single AWS Region.
- [For a configuration set](https://docs.aws.amazon.com/ses/latest/dg/monitoring-sender-reputation-pausing-configuration-set.html): You can configure Amazon SES to export reputation metrics that are specific to emails that are sent using a specific configuration set to Amazon CloudWatch.


## [Code examples](https://docs.aws.amazon.com/ses/latest/dg/service_code_examples.html)

### [Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/service_code_examples_ses.html)

Code examples that show how to use Amazon SES with an AWS SDK.

### [Basics](https://docs.aws.amazon.com/ses/latest/dg/service_code_examples_ses_basics.html)

The following code examples show how to use the basics of Amazon SES with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/ses/latest/dg/service_code_examples_ses_actions.html)

The following code examples show how to use Amazon SES with AWS SDKs.

- [CreateReceiptFilter](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_CreateReceiptFilter_section.html): Use CreateReceiptFilter with an AWS SDK
- [CreateReceiptRule](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_CreateReceiptRule_section.html): Use CreateReceiptRule with an AWS SDK
- [CreateReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_CreateReceiptRuleSet_section.html): Use CreateReceiptRuleSet with an AWS SDK
- [CreateTemplate](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_CreateTemplate_section.html): Use CreateTemplate with an AWS SDK
- [DeleteIdentity](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_DeleteIdentity_section.html): Use DeleteIdentity with an AWS SDK or CLI
- [DeleteReceiptFilter](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_DeleteReceiptFilter_section.html): Use DeleteReceiptFilter with an AWS SDK
- [DeleteReceiptRule](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_DeleteReceiptRule_section.html): Use DeleteReceiptRule with an AWS SDK
- [DeleteReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_DeleteReceiptRuleSet_section.html): Use DeleteReceiptRuleSet with an AWS SDK
- [DeleteTemplate](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_DeleteTemplate_section.html): Use DeleteTemplate with an AWS SDK
- [DescribeReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_DescribeReceiptRuleSet_section.html): Use DescribeReceiptRuleSet with an AWS SDK
- [GetIdentityVerificationAttributes](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_GetIdentityVerificationAttributes_section.html): Use GetIdentityVerificationAttributes with an AWS SDK or CLI
- [GetSendQuota](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_GetSendQuota_section.html): Use GetSendQuota with an AWS SDK or CLI
- [GetSendStatistics](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_GetSendStatistics_section.html): Use GetSendStatistics with a CLI
- [GetTemplate](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_GetTemplate_section.html): Use GetTemplate with an AWS SDK
- [ListIdentities](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_ListIdentities_section.html): Use ListIdentities with an AWS SDK or CLI
- [ListReceiptFilters](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_ListReceiptFilters_section.html): Use ListReceiptFilters with an AWS SDK
- [ListTemplates](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_ListTemplates_section.html): Use ListTemplates with an AWS SDK
- [SendBulkTemplatedEmail](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_SendBulkTemplatedEmail_section.html): Use SendBulkTemplatedEmail with an AWS SDK
- [SendEmail](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_SendEmail_section.html): Use SendEmail with an AWS SDK or CLI
- [SendRawEmail](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_SendRawEmail_section.html): Use SendRawEmail with an AWS SDK or CLI
- [SendTemplatedEmail](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_SendTemplatedEmail_section.html): Use SendTemplatedEmail with an AWS SDK
- [UpdateTemplate](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_UpdateTemplate_section.html): Use UpdateTemplate with an AWS SDK
- [VerifyDomainIdentity](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_VerifyDomainIdentity_section.html): Use VerifyDomainIdentity with an AWS SDK or CLI
- [VerifyEmailIdentity](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_VerifyEmailIdentity_section.html): Use VerifyEmailIdentity with an AWS SDK or CLI

### [Scenarios](https://docs.aws.amazon.com/ses/latest/dg/service_code_examples_ses_scenarios.html)

The following code examples show how to use Amazon SES with AWS SDKs.

- [Build an Amazon Transcribe streaming app](https://docs.aws.amazon.com/ses/latest/dg/ses_example_cross_TranscriptionStreamingApp_section.html): Build an Amazon Transcribe streaming app
- [Copy email and domain identities across Regions](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_Scenario_ReplicateIdentities_section.html): Copy Amazon SES email and domain identities from one AWS Region to another using an AWS SDK
- [Create a web application to track DynamoDB data](https://docs.aws.amazon.com/ses/latest/dg/ses_example_cross_DynamoDBDataTracker_section.html): Create a web application to track DynamoDB data
- [Create a web application to track Amazon Redshift data](https://docs.aws.amazon.com/ses/latest/dg/ses_example_cross_RedshiftDataTracker_section.html): Create an Amazon Redshift item tracker
- [Create an Aurora Serverless work item tracker](https://docs.aws.amazon.com/ses/latest/dg/ses_example_cross_RDSDataTracker_section.html): Create an Aurora Serverless work item tracker
- [Detect PPE in images](https://docs.aws.amazon.com/ses/latest/dg/ses_example_cross_RekognitionPhotoAnalyzerPPE_section.html): Detect PPE in images with Amazon Rekognition using an AWS SDK
- [Detect objects in images](https://docs.aws.amazon.com/ses/latest/dg/ses_example_cross_RekognitionPhotoAnalyzer_section.html): Detect objects in images with Amazon Rekognition using an AWS SDK
- [Detect people and objects in a video](https://docs.aws.amazon.com/ses/latest/dg/ses_example_cross_RekognitionVideoDetection_section.html): Detect people and objects in a video with Amazon Rekognition using an AWS SDK
- [Generate credentials to connect to an SMTP endpoint](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_Scenario_GenerateSmtpCredentials_section.html): Generate credentials to connect to an Amazon SES SMTP endpoint
- [Use Step Functions to invoke Lambda functions](https://docs.aws.amazon.com/ses/latest/dg/ses_example_cross_ServerlessWorkflows_section.html): Use Step Functions to invoke Lambda functions
- [Verify an email identity and send messages](https://docs.aws.amazon.com/ses/latest/dg/ses_example_ses_Scenario_SendEmail_section.html): Verify an email identity and send messages with Amazon SES using an AWS SDK

### [Amazon SES API v2](https://docs.aws.amazon.com/ses/latest/dg/service_code_examples_sesv2.html)

Code examples that show how to use Amazon SES API v2 with an AWS SDK.

### [Basics](https://docs.aws.amazon.com/ses/latest/dg/service_code_examples_sesv2_basics.html)

The following code examples show how to use the basics of Amazon SES API v2 with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/ses/latest/dg/service_code_examples_sesv2_actions.html)

The following code examples show how to use Amazon SES API v2 with AWS SDKs.

- [CreateContact](https://docs.aws.amazon.com/ses/latest/dg/sesv2_example_sesv2_CreateContact_section.html): Use CreateContact with an AWS SDK
- [CreateContactList](https://docs.aws.amazon.com/ses/latest/dg/sesv2_example_sesv2_CreateContactList_section.html): Use CreateContactList with an AWS SDK
- [CreateEmailIdentity](https://docs.aws.amazon.com/ses/latest/dg/sesv2_example_sesv2_CreateEmailIdentity_section.html): Use CreateEmailIdentity with an AWS SDK
- [CreateEmailTemplate](https://docs.aws.amazon.com/ses/latest/dg/sesv2_example_sesv2_CreateEmailTemplate_section.html): Use CreateEmailTemplate with an AWS SDK
- [DeleteContactList](https://docs.aws.amazon.com/ses/latest/dg/sesv2_example_sesv2_DeleteContactList_section.html): Use DeleteContactList with an AWS SDK
- [DeleteEmailIdentity](https://docs.aws.amazon.com/ses/latest/dg/sesv2_example_sesv2_DeleteEmailIdentity_section.html): Use DeleteEmailIdentity with an AWS SDK
- [DeleteEmailTemplate](https://docs.aws.amazon.com/ses/latest/dg/sesv2_example_sesv2_DeleteEmailTemplate_section.html): Use DeleteEmailTemplate with an AWS SDK
- [GetEmailIdentity](https://docs.aws.amazon.com/ses/latest/dg/sesv2_example_sesv2_GetEmailIdentity_section.html): Use GetEmailIdentity with an AWS SDK
- [ListContactLists](https://docs.aws.amazon.com/ses/latest/dg/sesv2_example_sesv2_ListContactLists_section.html): Use ListContactLists with an AWS SDK
- [ListContacts](https://docs.aws.amazon.com/ses/latest/dg/sesv2_example_sesv2_ListContacts_section.html): Use ListContacts with an AWS SDK
- [SendEmail](https://docs.aws.amazon.com/ses/latest/dg/sesv2_example_sesv2_SendEmail_section.html): Use SendEmail with an AWS SDK

### [Scenarios](https://docs.aws.amazon.com/ses/latest/dg/service_code_examples_sesv2_scenarios.html)

The following code examples show how to use Amazon SES API v2 with AWS SDKs.

- [Newsletter scenario](https://docs.aws.amazon.com/ses/latest/dg/sesv2_example_sesv2_NewsletterWorkflow_section.html): A complete Amazon SES API v2 Newsletter scenario using an AWS SDK


## [Security](https://docs.aws.amazon.com/ses/latest/dg/security.html)

### [Data protection](https://docs.aws.amazon.com/ses/latest/dg/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Simple Email Service.

- [Data at rest encryption](https://docs.aws.amazon.com/ses/latest/dg/encryption-rest.html): By default, Amazon SES encrypts all data at rest.
- [Deleting personal data](https://docs.aws.amazon.com/ses/latest/dg/deleting-personal-data.html): Permanently delete various types of personal data that's stored in Amazon SES.

### [Identity and access management](https://docs.aws.amazon.com/ses/latest/dg/control-user-access.html)

Control user access and specify which Amazon SES API actions a user can perform on resources by using IAM.

- [AWS managed policies](https://docs.aws.amazon.com/ses/latest/dg/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon Simple Email Service and recent changes to those policies.
- [Using service-linked roles](https://docs.aws.amazon.com/ses/latest/dg/using-service-linked-roles.html): How to use service-linked roles to give Amazon SES access to resources in your AWS account.

### [Logging and monitoring](https://docs.aws.amazon.com/ses/latest/dg/security-monitoring-overview.html)

Monitor Amazon SES to maintain reliability, availability, and performance.

- [Logging API calls](https://docs.aws.amazon.com/ses/latest/dg/logging-using-cloudtrail.html): Amazon SES is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in SES.
- [Compliance validation](https://docs.aws.amazon.com/ses/latest/dg/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/ses/latest/dg/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Simple Email Service features for data resiliency.
- [Infrastructure security in SES](https://docs.aws.amazon.com/ses/latest/dg/infrastructure-security.html): Learn how Amazon Simple Email Service isolates service traffic.
- [VPC endpoints](https://docs.aws.amazon.com/ses/latest/dg/send-email-set-up-vpc-endpoints.html): Use Amazon VPC to interact with Amazon SES through a virtual network in an isolated area of the AWS Cloud.


## [Troubleshooting](https://docs.aws.amazon.com/ses/latest/dg/troubleshoot.html)

- [General issues](https://docs.aws.amazon.com/ses/latest/dg/troubleshoot-general.html): Troubleshoot common delivery problems when the email you send through Amazon SES does not arrive.
- [Verification problems](https://docs.aws.amazon.com/ses/latest/dg/troubleshoot-verification.html): Troubleshoot common problems that may arise when you verify an email address or domain with Amazon SES.
- [DKIM problems](https://docs.aws.amazon.com/ses/latest/dg/troubleshoot-dkim.html): Troubleshoot common problems when you use DKIM with Amazon SES.
- [Delivery problems](https://docs.aws.amazon.com/ses/latest/dg/troubleshoot-delivery.html): Troubleshoot common delivery problems when the email you send through Amazon SES does not arrive.
- [Problems with received emails](https://docs.aws.amazon.com/ses/latest/dg/troubleshoot-receiving.html): Troubleshoot common problems with emails received from Amazon SES.
- [Notification problems](https://docs.aws.amazon.com/ses/latest/dg/troubleshoot-notifications.html): Troubleshoot common problems with Amazon SES notifications.
- [Email sending errors](https://docs.aws.amazon.com/ses/latest/dg/troubleshoot-error-messages.html): Troubleshoot types of email sending-specific errors that you might encounter when you send an email through Amazon SES.
- [Increasing throughput](https://docs.aws.amazon.com/ses/latest/dg/troubleshoot-throughput-problems.html): Increase your throughput using Amazon SES with these recommendations.
- [SMTP issues](https://docs.aws.amazon.com/ses/latest/dg/troubleshoot-smtp.html): Troubleshoot common problems sending email through the Amazon SES Simple Mail Transfer Protocol (SMTP) interface.


## [FAQs](https://docs.aws.amazon.com/ses/latest/dg/faqs.html)

- [Managed DIPS FAQs](https://docs.aws.amazon.com/ses/latest/dg/faqs-managed-dips.html): Answers to the most common questions related to the dedicated IP addresses (managed).
- [Sending review process FAQs](https://docs.aws.amazon.com/ses/latest/dg/faqs-enforcement.html): Includes information about the process that we use when there are issues with an Amazon SES account.
- [DNS Blackhole List (DNSBL) FAQs](https://docs.aws.amazon.com/ses/latest/dg/faqs-dnsbls.html): Learn how DNS Blackhole Lists (DNSBLs) can impact the delivery of your email, as well as what to do when your IP address is added to one of these types of lists.
- [Email metrics FAQs](https://docs.aws.amazon.com/ses/latest/dg/faqs-metrics.html): Answers to several of the most common questions related to the email metrics that Amazon SES collects for your emails.
