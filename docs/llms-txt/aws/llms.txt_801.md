# Source: https://docs.aws.amazon.com/social-messaging/latest/userguide/llms.txt

# AWS End User Messaging Social User Guide

> AWS End User Messaging Social is a messaging service that enables application developers to incorporate WhatsApp into their existing omnichannel workflows. With AWS End User Messaging Social, you have access to the rich messaging capabilities on WhatsApp to create branded, interactive content with images, video, and interactive buttons. This allows you to expand your reach and engagement by connecting with customers on the platform they already use.

- [What is AWS End User Messaging Social?](https://docs.aws.amazon.com/social-messaging/latest/userguide/what-is-service.html)
- [Setting up AWS End User Messaging Social](https://docs.aws.amazon.com/social-messaging/latest/userguide/setting-up.html)
- [Getting started](https://docs.aws.amazon.com/social-messaging/latest/userguide/getting-started-whatsapp.html)
- [Message types](https://docs.aws.amazon.com/social-messaging/latest/userguide/message-types.html)
- [Best practices](https://docs.aws.amazon.com/social-messaging/latest/userguide/whatsapp-best-practices.html)
- [AWS PrivateLink](https://docs.aws.amazon.com/social-messaging/latest/userguide/vpc-interface-endpoints.html)
- [Quotas](https://docs.aws.amazon.com/social-messaging/latest/userguide/quotas.html)
- [Document history](https://docs.aws.amazon.com/social-messaging/latest/userguide/doc-history.html)

## [WhatsApp Business Account (WABA)](https://docs.aws.amazon.com/social-messaging/latest/userguide/managing-whatsapp-waba.html)

- [View a WABA](https://docs.aws.amazon.com/social-messaging/latest/userguide/managing-waba_steps.html): You can view the WABA associated with your AWS account.
- [Add a WABA](https://docs.aws.amazon.com/social-messaging/latest/userguide/managing-waba-add_steps.html): Add a new WABA to your account if you already have a WhatsApp Business Profile.
- [WhatsApp business account types](https://docs.aws.amazon.com/social-messaging/latest/userguide/whatsapp-business-account.html): Your WhatsApp business account determines how you appear to your customers.


## [Phone numbers](https://docs.aws.amazon.com/social-messaging/latest/userguide/whatsapp-managing-phone-numbers.html)

- [Phone number considerations](https://docs.aws.amazon.com/social-messaging/latest/userguide/managing-phone-numbers_body.html): When you link a phone number with your WhatsApp Business Account (WABA), you should consider the following:
- [Add a phone number](https://docs.aws.amazon.com/social-messaging/latest/userguide/managing-phone-numbers-add.html): Learn how to add a WhatsApp phone number to a new or existing WhatsApp Business Account (WABA)
- [View a phone number's status](https://docs.aws.amazon.com/social-messaging/latest/userguide/managing-phone-numbers-status.html): Learn how to check your WhatsApp phone number's status to be able to send messages in AWS End User Messaging Social.
- [View a phone number's ID](https://docs.aws.amazon.com/social-messaging/latest/userguide/managing-phone-numbers-id.html): Learn how to find your phone number's ID to use when sending a message in AWS End User Messaging Social.
- [Increase messaging conversation limits](https://docs.aws.amazon.com/social-messaging/latest/userguide/increase-message-limit.html): Learn how to increase your message sending limit in WhatsApp.
- [Increase message throughput](https://docs.aws.amazon.com/social-messaging/latest/userguide/increase-message-throughput.html): Learn how to increase your messages per second sending rate in WhatsApp.
- [Understanding phone number quality rating](https://docs.aws.amazon.com/social-messaging/latest/userguide/understanding-phone-number-quality-rating.html): Learn how WhatsApp rates the quality of your phone number and how the status impacts your ability to send WhatsApp messages.


## [Message templates](https://docs.aws.amazon.com/social-messaging/latest/userguide/managing-templates.html)

- [Manage templates in the AWS Console](https://docs.aws.amazon.com/social-messaging/latest/userguide/managing-templates-console-detailed.html): Comprehensive guide for creating, editing, and managing WhatsApp message templates in the AWS End User Messaging Social console.
- [Create templates with CreateWhatsAppMessageTemplate](https://docs.aws.amazon.com/social-messaging/latest/userguide/create-message-templates-api.html): You can create customized WhatsApp message templates using the API.
- [Template pacing](https://docs.aws.amazon.com/social-messaging/latest/userguide/managing-templates-pacings.html): Template pacing is a method to allow early customers to rate and give feedback on your template.
- [Get feedback on a templates lowered status](https://docs.aws.amazon.com/social-messaging/latest/userguide/managing-templates-retreive-status.html): Learn how to get feeback from Meta on why your template's status was lowered.
- [Template status and quality rating](https://docs.aws.amazon.com/social-messaging/latest/userguide/managing-templates_status.html): Meta uses the status and quality rating of a template to determine how many messages you can send using the template.
- [Reasons why a template is rejected](https://docs.aws.amazon.com/social-messaging/latest/userguide/managing-templates_rejection.html): Learn about some of the common reasons why Meta rejects a template.


## [Message and event destinations](https://docs.aws.amazon.com/social-messaging/latest/userguide/managing-event-destinations.html)

- [Add an event destination](https://docs.aws.amazon.com/social-messaging/latest/userguide/managing-event-destinations-add.html): Learn about adding a message and event destinations for AWS End User Messaging Social.
- [Message and event format](https://docs.aws.amazon.com/social-messaging/latest/userguide/managing-event-destination-dlrs.html): Learn about AWS End User Messaging Social and WhatsApp event format.
- [Message status](https://docs.aws.amazon.com/social-messaging/latest/userguide/managing-event-destinations-status.html): Learn about the different message statuses that are returned from WhatsApp.


## [Uploading media files](https://docs.aws.amazon.com/social-messaging/latest/userguide/managing-media-files-s3.html)

- [Supported media file types](https://docs.aws.amazon.com/social-messaging/latest/userguide/supported-media-types.html): Learn about the media file types and sizes that can be sent with WhatsApp.


## [Sending messages](https://docs.aws.amazon.com/social-messaging/latest/userguide/whatsapp-send-message.html)

- [Send a template message](https://docs.aws.amazon.com/social-messaging/latest/userguide/send-message-text.html): An example of how to use the AWS CLI to send a template message in AWS End User Messaging Social.
- [Sending a media message](https://docs.aws.amazon.com/social-messaging/latest/userguide/send-message-media.html): An example of how to use the AWS CLI to send a media message in AWS End User Messaging Social.


## [Responding to a received message](https://docs.aws.amazon.com/social-messaging/latest/userguide/whatsapp-receive-message.html)

- [Change a message's status to read](https://docs.aws.amazon.com/social-messaging/latest/userguide/receive-message-status.html): An example of how to use the AWS CLI to change a message's status to read in AWS End User Messaging Social.
- [Respond with a reaction](https://docs.aws.amazon.com/social-messaging/latest/userguide/receive-message-emoji.html): An example of how to use the AWS CLI to respond to a message with a reaction in AWS End User Messaging Social.
- [Download a media file to Amazon S3 from WhatsApp](https://docs.aws.amazon.com/social-messaging/latest/userguide/receive-message-image.html): Learn how to download a media file from WhatsApp to an Amazon S3 bucket.
- [Example of responding to a message](https://docs.aws.amazon.com/social-messaging/latest/userguide/example-response.html): Learn how to respond to a message with a read receipt and reaction using example data.


## [Understanding your bill](https://docs.aws.amazon.com/social-messaging/latest/userguide/billing.html)

- [Charged per conversation (Deprecated)](https://docs.aws.amazon.com/social-messaging/latest/userguide/charged-per-conversation.html)


## [Monitoring](https://docs.aws.amazon.com/social-messaging/latest/userguide/monitoring-overview.html)

- [Monitoring with CloudWatch](https://docs.aws.amazon.com/social-messaging/latest/userguide/monitoring-cloudwatch.html): Learn how to monitor WhatsApp sending using CloudWatch.
- [CloudTrail logs](https://docs.aws.amazon.com/social-messaging/latest/userguide/logging-using-cloudtrail.html): Learn about logging AWS End User Messaging Social with AWS CloudTrail.
- [Monitoring with EventBridge](https://docs.aws.amazon.com/social-messaging/latest/userguide/monitor-event-bridge.html): Learn about using EventBridge to monitor AWS End User Messaging Social events.


## [Security](https://docs.aws.amazon.com/social-messaging/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/social-messaging/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS End User Messaging Social.

### [Identity and access management](https://docs.aws.amazon.com/social-messaging/latest/userguide/security-iam.html)

How to authenticate requests and manage access your AWS End User Messaging Social resources.

- [How AWS End User Messaging Social works with IAM](https://docs.aws.amazon.com/social-messaging/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to AWS End User Messaging Social, learn what IAM features are available to use with AWS End User Messaging Social.
- [Identity-based policy examples](https://docs.aws.amazon.com/social-messaging/latest/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify AWS End User Messaging Social resources.
- [AWS managed policies](https://docs.aws.amazon.com/social-messaging/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS End User Messaging Social and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/social-messaging/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS End User Messaging Social and IAM.
- [Compliance validation](https://docs.aws.amazon.com/social-messaging/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/social-messaging/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS End User Messaging Social features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/social-messaging/latest/userguide/infrastructure-security.html): Learn how AWS End User Messaging Social isolates service traffic.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/social-messaging/latest/userguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Security best practices](https://docs.aws.amazon.com/social-messaging/latest/userguide/security-best-practices.html): AWS End User Messaging Social security best practices.
- [Using service-linked roles](https://docs.aws.amazon.com/social-messaging/latest/userguide/using-service-linked-roles.html): How to use service-linked roles to give AWS End User Messaging Social access to resources in your AWS account.
