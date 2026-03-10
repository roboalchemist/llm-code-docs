# Source: https://docs.aws.amazon.com/pinpoint/latest/archguide/llms.txt

# Amazon Pinpoint Resilient Architecture Guide

> The Amazon Pinpoint Resilient Architecture Guide contains information, best practices, and example architectures related to building a resilient, multi-region architecture with Amazon Pinpoint. It is intended for System Administrators, Solutions Architects, IT professionals, and engineering teams. For information about using the features Amazon Pinpoint by using the AWS Management Console, see the Amazon Pinpoint User Guide. For information related to integrating Amazon Pinpoint with web and mobile applications, see the Amazon Pinpoint Developer Guide. For reference content related to the Amazon Pinpoint API, see the Amazon Pinpoint API Reference. Amazon Pinpoint is a customer engagement service that you can use to engage with your customers. When you use Amazon Pinpoint, you create segments that define targeted groups of customers. Next, you create campaigns that target your segments. Campaigns contain content that Amazon Pinpoint delivers to your customers using their preferred channels (such as email, SMS, or push notifications). Finally, Amazon Pinpoint provides engagement metrics that help you to track the success of your campaigns, as well as usage metrics that help you understand how customers use your apps.

- [Welcome](https://docs.aws.amazon.com/pinpoint/latest/archguide/welcome.html)
- [Resilient architecture overview](https://docs.aws.amazon.com/pinpoint/latest/archguide/overview.html)
- [Best practices](https://docs.aws.amazon.com/pinpoint/latest/archguide/bestpractices.html)
- [Channel considerations](https://docs.aws.amazon.com/pinpoint/latest/archguide/channels.html)
- [Reference architectures](https://docs.aws.amazon.com/pinpoint/latest/archguide/architectures.html)
- [Document history](https://docs.aws.amazon.com/pinpoint/latest/archguide/doc-history.html)

## [Synchronizing customer data](https://docs.aws.amazon.com/pinpoint/latest/archguide/customerdata.html)

- [Endpoints](https://docs.aws.amazon.com/pinpoint/latest/archguide/customerdata-endpoints.html): Example architectures for replicating and synchronizing Amazon Pinpoint endpoints across AWS Regions.
- [Events](https://docs.aws.amazon.com/pinpoint/latest/archguide/customerdata-events.html): Example architectures for replicating and synchronizing Amazon Pinpoint message events across AWS Regions.


## [Security](https://docs.aws.amazon.com/pinpoint/latest/archguide/security.html)

### [Data protection](https://docs.aws.amazon.com/pinpoint/latest/archguide/security-data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Pinpoint.

- [Data encryption](https://docs.aws.amazon.com/pinpoint/latest/archguide/security-data-protection-encryption.html): Learn how Amazon Pinpoint secures your data in transit and at rest.
- [Internetwork traffic privacy](https://docs.aws.amazon.com/pinpoint/latest/archguide/security-data-protection-internetwork-traffic.html): The following section describes how you can establish secure and private connections between Amazon Pinpoint and other locations.

### [Identity and access management](https://docs.aws.amazon.com/pinpoint/latest/archguide/security-iam.html)

Learn how to authenticate requests and manage access for your Amazon Pinpoint resources.

- [How Amazon Pinpoint works with IAM](https://docs.aws.amazon.com/pinpoint/latest/archguide/security_iam_service-with-iam.html): Learn how Amazon Pinpoint works with IAM, an AWS service that helps an administrator securely control access to AWS resources.
- [Amazon Pinpoint policy actions](https://docs.aws.amazon.com/pinpoint/latest/archguide/permissions-actions.html): Manage Amazon Pinpoint access by adding actions to IAM policies for users and resources in your AWS account.
- [Identity-based policy examples](https://docs.aws.amazon.com/pinpoint/latest/archguide/security_iam_id-based-policy-examples.html): This section provides Amazon Pinpoint identity-based policy examples and best practices as well as how to use the console.

### [IAM roles for common tasks](https://docs.aws.amazon.com/pinpoint/latest/archguide/security_iam_roles-common.html)

Learn about the IAM roles for common Amazon Pinpoint tasks.

- [Importing endpoints or segments](https://docs.aws.amazon.com/pinpoint/latest/archguide/permissions-import-segment.html): Create an IAM role that you can use to import user segment definitions into Amazon Pinpoint.
- [Exporting endpoints or segments](https://docs.aws.amazon.com/pinpoint/latest/archguide/permissions-export-endpoints.html): Create an IAM role that you can use to export Amazon Pinpoint segment information to Amazon Simple Storage Service.
- [Retrieving recommendations](https://docs.aws.amazon.com/pinpoint/latest/archguide/permissions-get-recommendations.html): Create an IAM role that enables Amazon Pinpoint to retrieve recommendation data from an Amazon Personalize campaign.
- [Streaming events to Kinesis](https://docs.aws.amazon.com/pinpoint/latest/archguide/permissions-streams.html): Create an IAM role that enables Amazon Pinpoint to send event data to Amazon Kinesis automatically.
- [Streaming email events to Firehose](https://docs.aws.amazon.com/pinpoint/latest/archguide/permissions-stream-email-events-kinesis.html): Create an IAM role that enables the Amazon Pinpoint Email API to send email-sending automatically, delivery, and response data to Firehose.
- [Troubleshooting](https://docs.aws.amazon.com/pinpoint/latest/archguide/security_iam_troubleshoot.html): Learn how to troubleshoot common errors when working with IAM and Amazon Pinpoint.
- [Security event logging and monitoring](https://docs.aws.amazon.com/pinpoint/latest/archguide/security-incident-response.html): Learn about tools for monitoring Amazon Pinpoint resources and responding to incidents.
- [Compliance validation](https://docs.aws.amazon.com/pinpoint/latest/archguide/security-compliance-validation.html): Learn about which AWS services are in scope for a specific compliance program.
- [Infrastructure security](https://docs.aws.amazon.com/pinpoint/latest/archguide/security-infrastructure-security.html): Learn how Amazon Pinpoint isolates service traffic.
- [Security best practices](https://docs.aws.amazon.com/pinpoint/latest/archguide/security-best-practices.html): Amazon Pinpoint provides a number of security features for you to consider as you develop and implement your own security policies.
