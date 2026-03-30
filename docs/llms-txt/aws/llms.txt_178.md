# Source: https://docs.aws.amazon.com/chime-sdk/latest/ag/llms.txt

# Amazon Chime SDK Administration Guide

> Use the Amazon Chime SDK to add real-time voice, video, and messaging powered by machine learning into your applications.

- [What is the Amazon Chime SDK?](https://docs.aws.amazon.com/chime-sdk/latest/ag/what-is-chime-sdk.html)
- [Prerequisites](https://docs.aws.amazon.com/chime-sdk/latest/ag/prereqs.html)
- [Getting started](https://docs.aws.amazon.com/chime-sdk/latest/ag/getting-started.html)
- [Managing global settings](https://docs.aws.amazon.com/chime-sdk/latest/ag/manage-global.html)
- [Network configuration and bandwidth requirements](https://docs.aws.amazon.com/chime-sdk/latest/ag/network-config.html)
- [Administrative support](https://docs.aws.amazon.com/chime-sdk/latest/ag/chime-getting-admin-support.html)
- [Document history](https://docs.aws.amazon.com/chime-sdk/latest/ag/doc-history.html)

## [Security](https://docs.aws.amazon.com/chime-sdk/latest/ag/security.html)

- [Identity and access management](https://docs.aws.amazon.com/chime-sdk/latest/ag/security-iam.html): Learn how to authenticate requests and manage access your Amazon Chime SDK resources.
- [How the Amazon Chime SDK works with IAM](https://docs.aws.amazon.com/chime-sdk/latest/ag/security_iam_service-with-iam.html): Learn how Amazon Chime SDK works with IAM policies to manage user access.

### [Using encryption with voice analytics](https://docs.aws.amazon.com/chime-sdk/latest/ag/analytics-encryption.html)

Learn how to use encryption to help safeguard your Amazon Chime SDK voice analytics data.

- [Understanding encryption at rest](https://docs.aws.amazon.com/chime-sdk/latest/ag/how-encrypted.html): How Amazon Chime SDK voice analytics encrypts data at rest.
- [Understanding how voice analytics uses grants](https://docs.aws.amazon.com/chime-sdk/latest/ag/how-use-grants.html): Abstract here
- [Key policy for voice analytics](https://docs.aws.amazon.com/chime-sdk/latest/ag/key-policy.html): Abstract here
- [Using encryption context](https://docs.aws.amazon.com/chime-sdk/latest/ag/encryption-context.html): Abstract here
- [Monitoring encryption keys](https://docs.aws.amazon.com/chime-sdk/latest/ag/monitor-keys.html): How to use AWS KMS to track Amazon Chime SDK Voice Connector requests in CloudTrail or CloudWatch logs.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/chime-sdk/latest/ag/confused-deputy.html): Learn how to create a trust policy that helps reduce confused deputy security issues.

### [Identity-based policy examples](https://docs.aws.amazon.com/chime-sdk/latest/ag/security_iam_id-based-policy-examples.html)

JSON examples of identity-based security policies for the Amazon Chime SDK.

- [Policy best practices](https://docs.aws.amazon.com/chime-sdk/latest/ag/security_iam_service-with-iam-policy-best-practices.html): The best practices for using IAM policies in the Amazon Chime SDK.
- [AWS managed Amazon Chime SDK policy](https://docs.aws.amazon.com/chime-sdk/latest/ag/security_iam_id-based-policy-examples-chime-sdk.html): How to use the AWS managed AmazonChimeVoiceConnectorServiceLinkedRolePolicy and grant users acess to Amazon Chime SDK actions.
- [AWS managed policy: AmazonChimeVoiceConnectorServiceLinkedRolePolicy](https://docs.aws.amazon.com/chime-sdk/latest/ag/cvc-linked-role-policy.html): How to use the AWS managed policy: AmazonChimeVoiceConnectorServiceLinkedRolePolicy and enable Amazon Chime SDK Voice Connector's to stream media.
- [AWS managed policy: AmazonChimeSDKMediaPipelinesServiceLinkedRolePolicy](https://docs.aws.amazon.com/chime-sdk/latest/ag/media-pipeline-service-linked-role-policy.html): How to use the AWS managed policy: AmazonChimeSDKMediaPipelinesServiceLinkedRolePolicy and grant Amazon Kinesis Video and Amazon Chime SDK media pipelines access to Amazon Chime SDK meetings.
- [Policy updates](https://docs.aws.amazon.com/chime-sdk/latest/ag/security-iam-awsmanpol-updates.html): A list of the new and updated AWS managed policies for use with the Amazon Chime SDK.
- [Troubleshooting](https://docs.aws.amazon.com/chime-sdk/latest/ag/security_iam_troubleshoot.html): Steps for troubleshooting IAM policies in the Amazon Chime SDK.

### [Using service-linked roles](https://docs.aws.amazon.com/chime-sdk/latest/ag/using-service-linked-roles.html)

How to use service-linked roles to give Amazon Chime SDK access to resources in your AWS account.

- [Using the Amazon Chime SDK Voice Connector service linked role policy](https://docs.aws.amazon.com/chime-sdk/latest/ag/using-service-linked-roles-stream.html): How to use the Amazon Chime SDK Voice Connector service linked role policy to stream media to Kinesis, and synthesize speech with Amazon Polly.
- [Using roles with live transcription](https://docs.aws.amazon.com/chime-sdk/latest/ag/using-service-linked-roles-transcription.html): Learn how to create the service-linked role needed to use Amazon Chime SDK live transcription.
- [Using roles with media pipelines](https://docs.aws.amazon.com/chime-sdk/latest/ag/using-service-linked-roles-media-pipeline.html): How to use service-linked roles to give the Amazon Chime SDK access to resources in your AWS account.
- [Using the AmazonChimeSDKEvents service-linked role](https://docs.aws.amazon.com/chime-sdk/latest/ag/analytics-service-role.html): How to use the >AmazonChimeSDKEvents service-linked role.

### [Logging and monitoring](https://docs.aws.amazon.com/chime-sdk/latest/ag/monitoring-overview.html)

Monitor the Amazon Chime SDK to maintain reliability, availability, and performance.

- [Monitoring with CloudWatch](https://docs.aws.amazon.com/chime-sdk/latest/ag/monitoring-cloudwatch.html): Learn how to use CloudWatch to collect near real-time metrics for the Amazon Chime SDK.
- [Automating with EventBridge](https://docs.aws.amazon.com/chime-sdk/latest/ag/automating-chime-with-cloudwatch-events.html): Automate the Amazon Chime SDK with other AWS services by using EventBridge.
- [Using AWS CloudTrail to log API calls](https://docs.aws.amazon.com/chime-sdk/latest/ag/cloudtrail.html): Use AWS CloudTrail to log Amazon Chime SDK API calls.
- [Compliance validation](https://docs.aws.amazon.com/chime-sdk/latest/ag/compliance.html): Learn what AWS services are in scope for a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/chime-sdk/latest/ag/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Chime SDK features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/chime-sdk/latest/ag/infrastructure-security.html): Learn how the Amazon Chime SDK isolates service traffic and provides automatic updates.


## [Managing phone numbers](https://docs.aws.amazon.com/chime-sdk/latest/ag/phone-numbers.html)

- [Provisioning phone numbers](https://docs.aws.amazon.com/chime-sdk/latest/ag/provision-phone.html): Learn how to provision new phone numbers for your Amazon Chime SDK phone number inventory.

### [Requesting international phone numbers](https://docs.aws.amazon.com/chime-sdk/latest/ag/request-intl-numbers.html)

Learn how to request international phone numbers for your Amazon Chime SDK phone inventory.

- [Outbound calling restrictions](https://docs.aws.amazon.com/chime-sdk/latest/ag/outbound-call-restrictions.html): Learn the restrictions placed on outbound calls.

### [Country requirements for phone numbers](https://docs.aws.amazon.com/chime-sdk/latest/ag/phone-country-reqs.html)

Learn the requirements for ordering and porting phone numbers in a number of countries.

- [Australia](https://docs.aws.amazon.com/chime-sdk/latest/ag/order-port-australia.html): Learn how to order and port Australian phone numbers for use with the Amazon Chime SDK.
- [Austria](https://docs.aws.amazon.com/chime-sdk/latest/ag/order-port-austria.html): Learn how to order and port Austrian phone numbers for use with the Amazon Chime SDK.
- [Canada](https://docs.aws.amazon.com/chime-sdk/latest/ag/order-port-canada.html): Learn how to order and port Canadian phone numbers for use with the Amazon Chime SDK.
- [Denmark](https://docs.aws.amazon.com/chime-sdk/latest/ag/order-port-denmark.html): Learn how to order and port Danish phone numbers for use with the Amazon Chime SDK.
- [Finland](https://docs.aws.amazon.com/chime-sdk/latest/ag/order-port-finland.html): Learn how to order and port Finnish phone numbers for use with the Amazon Chime SDK.
- [Germany](https://docs.aws.amazon.com/chime-sdk/latest/ag/order-port-germany.html): Learn how to order and port German phone numbers for use with the Amazon Chime SDK.
- [Ireland](https://docs.aws.amazon.com/chime-sdk/latest/ag/order-port-ireland.html): Learn how to order and port Irish phone numbers for use with the Amazon Chime SDK.
- [Italy](https://docs.aws.amazon.com/chime-sdk/latest/ag/order-port-italy.html): Learn how to order and port Italian phone numbers for use with the Amazon Chime SDK.
- [New Zealand](https://docs.aws.amazon.com/chime-sdk/latest/ag/order-port-nz.html): Learn how to order and port New Zealand phone numbers for use with the Amazon Chime SDK.
- [Nigeria](https://docs.aws.amazon.com/chime-sdk/latest/ag/order-port-nigeria.html): Learn how to order Nigerian phone numbers for use with the Amazon Chime SDK.
- [Puerto Rico](https://docs.aws.amazon.com/chime-sdk/latest/ag/order-port-pr.html): Learn how to order and port Puerto Rican phone numbers for use with the Amazon Chime SDK.
- [South Korea](https://docs.aws.amazon.com/chime-sdk/latest/ag/order-port-s-korea.html): Learn how to order South Korean phone numbers for use with the Amazon Chime SDK.
- [Sweden](https://docs.aws.amazon.com/chime-sdk/latest/ag/order-port-sweden.html): Learn how to order and port Swedish phone numbers for use with the Amazon Chime SDK.
- [Switzerland](https://docs.aws.amazon.com/chime-sdk/latest/ag/order-port-switzerland.html): Learn how to order and port Swiss phone numbers for use with the Amazon Chime SDK.
- [United Kingdom](https://docs.aws.amazon.com/chime-sdk/latest/ag/order-port-uk.html): Learn how to order and port UK phone numbers for use with the Amazon Chime SDK.
- [Porting existing phone numbers](https://docs.aws.amazon.com/chime-sdk/latest/ag/porting.html): Learn how to port existing phone numbers for use with the Amazon Chime SDK.

### [Managing phone number inventory](https://docs.aws.amazon.com/chime-sdk/latest/ag/phone-inventory.html)

Learn how to manage your Amazon Chime phone number inventory.

- [Assigning phone numbers to Voice Connectors](https://docs.aws.amazon.com/chime-sdk/latest/ag/assign-to-cvc.html): How to assign a phone number to an Amazon Chime SDK Voice Connector or Voice Connector group.
- [Reassigning Voice Connector numbers](https://docs.aws.amazon.com/chime-sdk/latest/ag/reassign-vc-numbers.html): How to reassign a phone number assigned to an Amazon Chime SDK Voice Connector.
- [Unassigning Voice Connector phone numbers](https://docs.aws.amazon.com/chime-sdk/latest/ag/unassign-numbers.html): How to unassign a phone number from an Amazon Chime SDK Voice Connector or SIP media application.
- [Reassigning phone numbers](https://docs.aws.amazon.com/chime-sdk/latest/ag/reassign-numbers.html): How to reassign phone numbers that are currently assigned to an Amazon Chime SDK Voice Connector or Voice Connector group.
- [Assigning phone numbers to SIP media applications](https://docs.aws.amazon.com/chime-sdk/latest/ag/assign-sip-app.html): How to assign phone numbers to Amazon Chime SDK SIP media applications.
- [Viewing phone number details](https://docs.aws.amazon.com/chime-sdk/latest/ag/view-number-details.html): How to view phone number details in your Amazon Chime SDK number inventory.
- [Changing a phone number's product type](https://docs.aws.amazon.com/chime-sdk/latest/ag/change-product-type.html): How to change the product type of your Amazon Chime SDK phone numbers.
- [Changing a phone number's assignment type](https://docs.aws.amazon.com/chime-sdk/latest/ag/change-assignment-type.html): How to change the assignment type of your Amazon Chime SDK phone numbers.
- [Setting outbound calling names](https://docs.aws.amazon.com/chime-sdk/latest/ag/calling-name.html): How to enter and update outbound calling names in your Amazon Chime SDK phone number inventory.
- [Deleting phone numbers](https://docs.aws.amazon.com/chime-sdk/latest/ag/delete-phone.html): Learn how to delete phone numbers from your the Amazon Chime SDK phone number inventory.
- [Restoring deleted phone numbers](https://docs.aws.amazon.com/chime-sdk/latest/ag/restore-phone.html): Learn how to restore deleted phone numbers in your Amazon Chime SDK phone number inventory.
- [Optimize your outbound calling reputation](https://docs.aws.amazon.com/chime-sdk/latest/ag/optimize-outbound-calling.html): Our recommendations for steps you can take to get a higher call answer rate.
- [STIR/SHAKEN for Amazon Chime SDK](https://docs.aws.amazon.com/chime-sdk/latest/ag/stir-shaken.html): Learn about STIR/SHAKEN for Amazon Chime SDK.


## [Managing Voice Connectors](https://docs.aws.amazon.com/chime-sdk/latest/ag/voice-connectors.html)

- [Creating Voice Connectors](https://docs.aws.amazon.com/chime-sdk/latest/ag/create-voicecon.html): Learn how to create an Amazon Chime SDK Voice Connector.
- [Using tags with Voice Connectors](https://docs.aws.amazon.com/chime-sdk/latest/ag/use-tags-voice-con.html): Learn how to use tagsâkey-value pairs that you defineâwith your Amazon Chime SDK Voice Connectors.
- [Editing Voice Connector settings](https://docs.aws.amazon.com/chime-sdk/latest/ag/edit-voicecon.html): Learn how to edit Amazon Chime SDK Voice Connector settings to allow outbound or inbound calls.
- [Assigning and unassigning phone numbers](https://docs.aws.amazon.com/chime-sdk/latest/ag/assign-voicecon.html): Learn how to assign and unassign phone numbers to an Amazon Chime SDK Voice Connector.
- [Deleting Voice Connectors](https://docs.aws.amazon.com/chime-sdk/latest/ag/delete-voicecon.html): Learn how to delete an Amazon Chime SDK Voice Connector.
- [Configuring Voice Connectors to use call analytics](https://docs.aws.amazon.com/chime-sdk/latest/ag/configure-voicecon.html): Learn how to configure Amazon Chime SDK Voice Connectors to use Amazon Chime SDK call analytics.
- [Managing Voice Connector groups](https://docs.aws.amazon.com/chime-sdk/latest/ag/voice-connector-groups.html): Learn how to create and manage Amazon Chime SDK Voice Connector groups.

### [Streaming media to Kinesis](https://docs.aws.amazon.com/chime-sdk/latest/ag/start-kinesis-vc.html)

Learn how to stream Amazon Chime SDK Voice Connector media to Kinesis.

- [Using Amazon Chime SDK voice analytics with Voice Connectors](https://docs.aws.amazon.com/chime-sdk/latest/ag/use-ca-with-vc.html): Learn how to use Amazon Chime SDK voice analytics with your Voice Connectors.
- [Using Voice Connector configuration guides](https://docs.aws.amazon.com/chime-sdk/latest/ag/config-guides.html): Learn how to configure Amazon Chime SDK Voice Connectors for use with private branch exchanges, session border controllers, and call centers.


## [Managing call analytics](https://docs.aws.amazon.com/chime-sdk/latest/ag/ag-call-analytics.html)

- [Creating call analytics configurations](https://docs.aws.amazon.com/chime-sdk/latest/ag/create-ca-config.html): Create Amazon Chime SDK call analytics configurations, the first step in using call analytics.
- [Using call analytics configurations](https://docs.aws.amazon.com/chime-sdk/latest/ag/use-ca-config.html): Learn how to use an Amazon Chime SDK call analytics configuration by associating it with an Amazon Chime SDK Voice Connector.
- [Updating call analytics configurations](https://docs.aws.amazon.com/chime-sdk/latest/ag/update-ca-config.html): Learn how to update Amazon Chime SDK call analytics configurations.
- [Deleting call analytics configurations](https://docs.aws.amazon.com/chime-sdk/latest/ag/delete-ca-config.html): Learn how to delete an Amazon Chime SDK call analytics configuration.
- [Enabling voice analytics](https://docs.aws.amazon.com/chime-sdk/latest/ag/enable-voice-analytics.html): Learn how to enable Amazon Chime SDK PSTN voice analytics by configuring Amazon Chime SDK Voice Connectors, and creating notification targets and voice profile domains.

### [Managing voice profile domains](https://docs.aws.amazon.com/chime-sdk/latest/ag/manage-voice-profile-domains.html)

Learn how to create and manage voice profile domains, collections of voice profiles generated by Amazon Chime SDK speaker search.

- [Creating voice profile domains](https://docs.aws.amazon.com/chime-sdk/latest/ag/create-vp-domain.html): Learn how to create voice profile domains and enable speaker search in Amazon Chime SDK meetings.
- [Editing voice profile domains](https://docs.aws.amazon.com/chime-sdk/latest/ag/edit-vp-domain.html): Learn how to use the Amazon Chime SDK console to edit voice profile domains.
- [Deleting voice profile domains](https://docs.aws.amazon.com/chime-sdk/latest/ag/delete-vp-domain.html): Learn how to use the Amazon Chime SDK console to delete voice profile domains.
- [Using tags with voice profile domains](https://docs.aws.amazon.com/chime-sdk/latest/ag/vp-domain-tags.html): Learn how to use tags with Amazon Chime SDK voice profile domains.
- [Understanding the voice analytics consent notice](https://docs.aws.amazon.com/chime-sdk/latest/ag/va-consent-notice.html): Background information about the consent notice that you see when you create a voice profile domain or enable Amazon Chime SDK voice analytics.


## [Setting up emergency calling](https://docs.aws.amazon.com/chime-sdk/latest/ag/set-up-emergency-calls.html)

- [Validating addresses for emergency calls](https://docs.aws.amazon.com/chime-sdk/latest/ag/validate-emergency-addresses.html): You use the Amazon Chime SDK console to validate the addresses used in emergency calls.
- [Setting up third-party emergency routing numbers](https://docs.aws.amazon.com/chime-sdk/latest/ag/chime-voice-connector-emergency-calling.html): Learn how to set up emergency third-part emergency routing numbers for use with Amazon Chime SDK Voice Connectors.
- [Using PIDF-LO in emergency calls](https://docs.aws.amazon.com/chime-sdk/latest/ag/use-pidf-lo.html): Learn how to use PIDF-LO objects in emergency calls.


## [Managing SIP media applications](https://docs.aws.amazon.com/chime-sdk/latest/ag/manage-sip-applications.html)

- [Understanding SIP applications and rules](https://docs.aws.amazon.com/chime-sdk/latest/ag/understand-sip-data-models.html): An overview of Amazon Chime SDK SIP rules, Amazon Chime SDK SIP media applications, and how they invoke AWS Lambda functions.

### [Using SIP media applications](https://docs.aws.amazon.com/chime-sdk/latest/ag/use-sip-apps.html)

Learn how to use SIP media applications, managed object that pass values from a SIP rule to a target AWS Lambda function.

- [Creating a SIP media application](https://docs.aws.amazon.com/chime-sdk/latest/ag/create-sip-app.html): Learn how to create Amazon Chime SDK SIP media applications and enable calling for Request URI hostnames, Amazon Chime SDK Voice Connector groups, and more.
- [Using tags with SIP media applications](https://docs.aws.amazon.com/chime-sdk/latest/ag/use-tags-sip-apps.html): Learn how to use tagsâkey-value pairs that you defineâwith your Amazon Chime SDK SIP media applications.
- [Viewing a SIP media application](https://docs.aws.amazon.com/chime-sdk/latest/ag/view-sip-app.html): Learn how to view the details of an Amazon Chime SDK SIP media application.
- [Updating a SIP media application](https://docs.aws.amazon.com/chime-sdk/latest/ag/update-sip-app.html): Learn how to update an Amazon Chime SDK SIP media application.
- [Deleting a SIP media application](https://docs.aws.amazon.com/chime-sdk/latest/ag/delete-sip-app.html): Learn how to delete an Amazon Chime SDK SIP media application.


## [Managing SIP rules](https://docs.aws.amazon.com/chime-sdk/latest/ag/use-sip-rules.html)

- [Creating a SIP rule](https://docs.aws.amazon.com/chime-sdk/latest/ag/create-sip-rule.html): The steps for creating Session Initiation Protocol (SIP) rules.
- [Viewing a SIP rule](https://docs.aws.amazon.com/chime-sdk/latest/ag/view-a-rule.html): The steps for viewing a SIP rule.
- [Updating a SIP rule](https://docs.aws.amazon.com/chime-sdk/latest/ag/update-sip-rule.html): How to update a SIP rule.
- [Enabling a SIP rule](https://docs.aws.amazon.com/chime-sdk/latest/ag/enable-sip-rule.html): How to enable a SIP rule.
- [Disabling a SIP rule](https://docs.aws.amazon.com/chime-sdk/latest/ag/disable-sip-rule.html): How to disable a SIP rule.
- [Deleting a SIP rule](https://docs.aws.amazon.com/chime-sdk/latest/ag/delete-sip-rule.html): Learn how to delete an Amazon Chime SDK SIP rule.
