# Source: https://docs.aws.amazon.com/pinpoint/latest/developerguide/llms.txt

# Amazon Pinpoint Developer Guide

> This is the official Amazon Web Services (AWS) developer documentation for Amazon Pinpoint. This documentation shows you how to integrate the features of Amazon Pinpoint into your apps. It also includes information about interacting with Amazon Pinpoint programmatically by using the Amazon Pinpoint REST API. Amazon Pinpoint is a customer engagement service that you can use to engage with your customers. When you use Amazon Pinpoint, you create segments that define targeted groups of customers. Next, you create campaigns that target your segments. Campaigns contain content that Amazon Pinpoint delivers to your customers using their preferred channels (such as email, SMS, or push notifications). Finally, Amazon Pinpoint provides engagement metrics that help you to track the success of your campaigns, as well as usage metrics that help you understand how customers use your apps. This documentation is offered here as a free Kindle book. You can also read it online or in PDF format at https://aws.amazon.com/documentation/pinpoint/.

- [What is Amazon Pinpoint?](https://docs.aws.amazon.com/pinpoint/latest/developerguide/welcome.html)
- [Use the SMS and Voice API](https://docs.aws.amazon.com/pinpoint/latest/developerguide/sms-voice-v2.html)
- [Phone number validation](https://docs.aws.amazon.com/pinpoint/latest/developerguide/validate-phone-numbers.html)
- [Delete Amazon Pinpoint project data](https://docs.aws.amazon.com/pinpoint/latest/developerguide/deleting-data.html)
- [Quotas](https://docs.aws.amazon.com/pinpoint/latest/developerguide/quotas.html)
- [Document history](https://docs.aws.amazon.com/pinpoint/latest/developerguide/doc-history.html)

## [Use endpoints to define your audience](https://docs.aws.amazon.com/pinpoint/latest/developerguide/audience-define.html)

- [Add endpoints](https://docs.aws.amazon.com/pinpoint/latest/developerguide/audience-define-endpoints.html): Before you send messages with Amazon Pinpoint, define one or more endpoints for each member of your audience.
- [Associate users with endpoints](https://docs.aws.amazon.com/pinpoint/latest/developerguide/audience-define-user.html): Add information about your users to your Amazon Pinpoint endpoints.
- [Add a batch of endpoints](https://docs.aws.amazon.com/pinpoint/latest/developerguide/audience-define-endpoints-batch.html): Add multiple endpoints to your Amazon Pinpoint project by submitting them in batches.
- [Import endpoints](https://docs.aws.amazon.com/pinpoint/latest/developerguide/audience-define-import.html): Quickly add many endpoints to your Amazon Pinpoint project by importing them.
- [Export endpoints from Amazon Pinpoint to Amazon S3 buckets](https://docs.aws.amazon.com/pinpoint/latest/developerguide/audience-define-export.html): Get all of the audience data in your Amazon Pinpoint project by exporting your endpoints to Amazon S3 buckets.
- [Look up endpoints in an Amazon Pinpoint project](https://docs.aws.amazon.com/pinpoint/latest/developerguide/audience-define-lookup.html): Look up the details for any endpoint in your Amazon Pinpoint project.
- [List endpoint IDs](https://docs.aws.amazon.com/pinpoint/latest/developerguide/audience-define-list-ids.html): Get a list of your endpoint IDs if you need to update or delete all of the endpoints in your Amazon Pinpoint project.
- [Manage endpoint maximum](https://docs.aws.amazon.com/pinpoint/latest/developerguide/audience-define-auto-inactive.html): Amazon Pinpoint has a maximum of 15 endpoints per audience member.
- [Delete endpoints](https://docs.aws.amazon.com/pinpoint/latest/developerguide/audience-define-remove.html): When you no longer want to message an endpoint, delete it from your Amazon Pinpoint project.


## [Create or import segments](https://docs.aws.amazon.com/pinpoint/latest/developerguide/segments.html)

- [Build segments](https://docs.aws.amazon.com/pinpoint/latest/developerguide/segments-dimensional.html): Build an Amazon Pinpoint user segment programmatically.
- [Import segments](https://docs.aws.amazon.com/pinpoint/latest/developerguide/segments-importing.html): Import an Amazon Pinpoint user segment programmatically.
- [Customize segments](https://docs.aws.amazon.com/pinpoint/latest/developerguide/segments-dynamic.html): Use an AWS Lambda function to tailor how an Amazon Pinpoint campaign engages your target audience.


## [Create Amazon Pinpoint campaigns programmatically](https://docs.aws.amazon.com/pinpoint/latest/developerguide/campaigns.html)

- [Create a campaign with the SDK for Java](https://docs.aws.amazon.com/pinpoint/latest/developerguide/campaigns-standard.html): A standard campaign sends a custom push notification to a specified segment according to a schedule that you define.
- [Create an A/B test campaign](https://docs.aws.amazon.com/pinpoint/latest/developerguide/campaigns-abtest.html): An A/B test campaign behaves like a standard campaign, but enables you to define different treatments for the campaign message or schedule.


## [Manage tags](https://docs.aws.amazon.com/pinpoint/latest/developerguide/tagging-resources.html)

- [Use tags in IAM policies](https://docs.aws.amazon.com/pinpoint/latest/developerguide/tags-iam.html): After you start implementing tags, you can apply tag-based, resource-level permissions to AWS Identity and Access Management (IAM) policies and API operations.
- [Add tags to resources](https://docs.aws.amazon.com/pinpoint/latest/developerguide/tags-add.html): The following examples show how to add a tag to an Amazon Pinpoint resource by using the AWS CLI and the Amazon Pinpoint REST API.
- [Display tags for resources](https://docs.aws.amazon.com/pinpoint/latest/developerguide/tags-display.html): The following examples show how to use the AWS CLI and the Amazon Pinpoint REST API to display a list of all the tags (keys and values) that are associated with an Amazon Pinpoint resource.
- [Update or overwrite tags](https://docs.aws.amazon.com/pinpoint/latest/developerguide/tags-update.html): There are several ways to update (overwrite) a tag for an Amazon Pinpoint resource.
- [Remove tags from resources](https://docs.aws.amazon.com/pinpoint/latest/developerguide/tags-remove.html): The following examples show how to remove a tag (both the key and value) from an Amazon Pinpoint resource by using the AWS CLI and the Amazon Pinpoint REST API.


## [Integrate with your application](https://docs.aws.amazon.com/pinpoint/latest/developerguide/integrate.html)

- [Working with AWS SDKs](https://docs.aws.amazon.com/pinpoint/latest/developerguide/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.
- [Connect your frontend application using Amplify](https://docs.aws.amazon.com/pinpoint/latest/developerguide/integrate-sdk.html): Add Amazon Pinpoint features to your application by using the AWS Mobile SDKs for Android or iOS, or by using the AWS Amplify JavaScript library.
- [Register endpoints in your app](https://docs.aws.amazon.com/pinpoint/latest/developerguide/integrate-endpoints.html): Register Amazon Pinpoint endpoints by using the AWS Mobile SDKs or the AWS Amplify JavaScript library.
- [Report events in your app](https://docs.aws.amazon.com/pinpoint/latest/developerguide/integrate-events.html): Report events to Amazon Pinpoint by using the AWS Mobile SDKs for iOS and Android.


## [Send transactional messages from your app](https://docs.aws.amazon.com/pinpoint/latest/developerguide/send-messages.html)

### [Send transactional emails](https://docs.aws.amazon.com/pinpoint/latest/developerguide/send-messages-email.html)

Send transactional email messages by using an AWS SDK or the Amazon Pinpoint SMTP interface.

- [Send email using the API](https://docs.aws.amazon.com/pinpoint/latest/developerguide/send-messages-sdk.html): Use the Amazon Pinpoint API to send an email.
- [Add email unsubscribe headers](https://docs.aws.amazon.com/pinpoint/latest/developerguide/send-messages-email-cli.html): Send an email message with unsubscribe headers by using the AWS CLI.
- [Send SMS messages](https://docs.aws.amazon.com/pinpoint/latest/developerguide/send-messages-sms.html): Send transactional SMS messages by using an AWS SDK or the Amazon Pinpoint SMTP interface.
- [Send voice messages](https://docs.aws.amazon.com/pinpoint/latest/developerguide/send-messages-voice.html): Send voice messages by using an AWS SDK.


## [Generate one-time passwords](https://docs.aws.amazon.com/pinpoint/latest/developerguide/send-validate-otp.html)

- [Validate OTP messages](https://docs.aws.amazon.com/pinpoint/latest/developerguide/send-validate-otp-validating.html): After you send a one-time-password, your application can call the Amazon Pinpoint API to verify it.
- [OTP code examples in Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/developerguide/send-validate-otp-examples.html): This section contains code examples that show how to use the SDK for Python (Boto3) to send and verify OTP codes.


## [Customize in-app messages](https://docs.aws.amazon.com/pinpoint/latest/developerguide/channels-inapp.html)

- [Retrieve in-app messages for an endpoint](https://docs.aws.amazon.com/pinpoint/latest/developerguide/channels-inapp-retrieving.html): Your applications can call the GetInAppMessages API to retrieve all of the in-app messages that a given endpoint is entitled to.
- [GetInAppMessages API response JSON example](https://docs.aws.amazon.com/pinpoint/latest/developerguide/channels-inapp-response.html): When you call the GetInAppMessages API operation, it returns a list of messages that the specified endpoint is entitled to.


## [Create a custom channel](https://docs.aws.amazon.com/pinpoint/latest/developerguide/channels-custom.html)

- [Assign a Lambda function or webhook to an individual campaign](https://docs.aws.amazon.com/pinpoint/latest/developerguide/channels-custom-create.html): To assign a Lambda function or webhook to an individual campaign, use the Amazon Pinpoint API to create or update a Campaign object.

### [Create and configure a Lambda function for a Amazon Pinpoint campaign](https://docs.aws.amazon.com/pinpoint/latest/developerguide/channels-custom-lambda-create.html)

This section provides an overview of the steps to create a Lambda function that sends messages over a custom channel.

- [Lambda function response format for Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/developerguide/channels-custom-lambda-response-format.html): If you want to use the journey multivariate or yes/no split to determine the endpoint path after a custom channel activity you must structure your Lambda function response into a format that Amazon Pinpoint can understand, and then send endpoints down the correct path.
- [Grant permission to invoke the function](https://docs.aws.amazon.com/pinpoint/latest/developerguide/channels-custom-lambda-trust-policy-assign.html): You can use the AWS Command Line Interface (AWS CLI) to add permissions to the Lambda function policy assigned to your Lambda function.


## [Stream app event data](https://docs.aws.amazon.com/pinpoint/latest/developerguide/event-streams.html)

- [Set up event data streaming](https://docs.aws.amazon.com/pinpoint/latest/developerguide/event-streams-setup.html): Set up Amazon Pinpoint to stream event data through Amazon Kinesis or an Amazon Data Firehose.
- [App event data stream from Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/developerguide/event-streams-data-app.html): View your app events using Amazon Pinpoint.
- [Campaign event data stream from Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/developerguide/event-streams-data-campaign.html): If you use Amazon Pinpoint to send campaigns through a channel, Amazon Pinpoint can stream event data about those campaigns.
- [Journey event data from Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/developerguide/event-streams-data-journey.html): When you publish a journey, Amazon Pinpoint can stream event data for email, SMS, push, and custom messages that you send from the journey.
- [Email event data stream from Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/developerguide/event-streams-data-email.html): If you use Amazon Pinpoint to send emails, Amazon Pinpoint can stream event data about those emails.
- [SMS event data stream from Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/developerguide/event-streams-data-sms.html): If the SMS channel is enabled for a project, Amazon Pinpoint can stream event data about SMS message deliveries for the project.
- [Delete an event stream](https://docs.aws.amazon.com/pinpoint/latest/developerguide/event-streams-disable.html): If you assign a Kinesis stream to an application, you can disable event streaming for that application.


## [Query analytics data](https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics.html)

- [IAM policies](https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-permissions.html): Manage programmatic access to Amazon Pinpoint analytics data by adding API actions to IAM policies for roles or users in your AWS account.

### [Standard metrics for projects, campaigns, and journeys](https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html)

Use the Amazon Pinpoint API to query analytics data for standard metrics that apply to Amazon Pinpoint projects, campaigns, and journeys.

- [Application metrics for campaigns](https://docs.aws.amazon.com/pinpoint/latest/developerguide/application-metrics-campaigns.html): The following table lists and describes standard application metrics that you can query to assess the performance of all the campaigns that are associated with an Amazon Pinpoint project.
- [Application metrics for email](https://docs.aws.amazon.com/pinpoint/latest/developerguide/application-metrics-txn-email.html): The following table lists and describes standard application metrics that you can query to monitor trends for all the transactional email messages that are associated with an Amazon Pinpoint project.
- [Application metrics for SMS](https://docs.aws.amazon.com/pinpoint/latest/developerguide/application-metrics-txn-sms.html): The following table lists and describes standard application metrics that you can query to monitor trends for all the transactional SMS messages that are associated with an Amazon Pinpoint project.
- [Campaign metrics](https://docs.aws.amazon.com/pinpoint/latest/developerguide/campaign-metrics.html): The following table lists and describes standard campaign metrics that you can query to assess the performance of an individual campaign.
- [Journey engagement metrics](https://docs.aws.amazon.com/pinpoint/latest/developerguide/journey-metrics-engagement-email.html): The following table lists and describes standard journey engagement metrics that you can query to monitor trends for all the email messages that were sent by an Amazon Pinpoint journey.
- [Journey execution metrics](https://docs.aws.amazon.com/pinpoint/latest/developerguide/journey-metrics-execution.html): The following table lists and describes standard execution metrics that you can query to assess the status of participants in an Amazon Pinpoint journey.
- [Journey activity execution metrics](https://docs.aws.amazon.com/pinpoint/latest/developerguide/journey-metrics-activity-execution.html): The following table lists and describes standard execution metrics that you can query to assess the status of participants in each type of individual activity for an Amazon Pinpoint journey.
- [Journey and campaign execution metrics](https://docs.aws.amazon.com/pinpoint/latest/developerguide/journey-run-metrics-activity-execution.html): You can query standard execution metrics to assess the status of participants in each type of individual activity for an Amazon Pinpoint journey or campaign.

### [Query campaign data](https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-query-campaigns.html)

Use the Amazon Pinpoint API to query analytics data for one or more campaigns.

- [Query data for one campaign](https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-query-campaigns-single.html): To query the data for one campaign, you use the Campaign Metrics API and specify values for the following required parameters:
- [Query data for multiple campaigns](https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-query-campaigns-multiple.html): There are two ways to query the data for multiple campaigns.

### [Query transactional messaging data](https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-query-txn-messaging.html)

Use the Amazon Pinpoint API to query analytics data for transactional messages that are associated with an Amazon Pinpoint project.

- [Query data for transactional email](https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-query-txn-messaging-email.html): To query the data for transactional email messages that were sent for a project, you use the Application Metrics API and specify values for the following required parameters:
- [Query data for transactional SMS](https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-query-txn-messaging-sms.html): To query the data for transactional SMS messages that were sent for a project, you use the Application Metrics API and specify values for the following required parameters:
- [Use JSON query results](https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-query-results.html): Understand the structure of query results that the Amazon Pinpoint API provides in response to a query for Amazon Pinpoint analytics data.


## [Log API calls with CloudTrail](https://docs.aws.amazon.com/pinpoint/latest/developerguide/logging-using-cloudtrail.html)

- [API actions in CloudTrail log files](https://docs.aws.amazon.com/pinpoint/latest/developerguide/pinpoint-cloudtrail-actions.html): The Amazon Pinpoint API supports logging the following actions as events in CloudTrail log files:
- [Email API actions in CloudTrail log files](https://docs.aws.amazon.com/pinpoint/latest/developerguide/pinpoint-email-cloudtrail-actions.html): The Amazon Pinpoint Email API supports logging the following actions as events in CloudTrail log files:
- [Supported SMS and voice API v1 actions in CloudTrail log files](https://docs.aws.amazon.com/pinpoint/latest/developerguide/pinpoint-sms-voice-cloudtrail-actions.html): The Amazon Pinpoint SMS and Voice version 1 API supports logging the following actions as events in CloudTrail log files:
- [CloudTrail log entry examples](https://docs.aws.amazon.com/pinpoint/latest/developerguide/understanding-pinpoint-entries.html): A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify.


## [Use a recommender model](https://docs.aws.amazon.com/pinpoint/latest/developerguide/ml-models-rm-lambda.html)

- [Add recommendations to messages](https://docs.aws.amazon.com/pinpoint/latest/developerguide/ml-models-rm-lambda-overview.html): To use a recommender model with Amazon Pinpoint, you start by creating an Amazon Personalize solution and deploying that solution as an Amazon Personalize campaign.
- [Invoke a Lambda function for a recommender model](https://docs.aws.amazon.com/pinpoint/latest/developerguide/ml-models-rm-lambda-create-function.html): To learn how to create a Lambda function, see Getting Started in the AWS Lambda Developer Guide.
- [Assign a policy to process recommendation data](https://docs.aws.amazon.com/pinpoint/latest/developerguide/ml-models-rm-lambda-trust-policy.html): Before you can use your Lambda function to process recommendation data, you must authorize Amazon Pinpoint to invoke the function.


## [Code examples](https://docs.aws.amazon.com/pinpoint/latest/developerguide/service_code_examples.html)

### [Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/developerguide/service_code_examples_pinpoint.html)

Code examples that show how to use Amazon Pinpoint with an AWS SDK.

### [Basics](https://docs.aws.amazon.com/pinpoint/latest/developerguide/service_code_examples_pinpoint_basics.html)

The following code examples show how to use the basics of Amazon Pinpoint with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/pinpoint/latest/developerguide/service_code_examples_pinpoint_actions.html)

The following code examples show how to use Amazon Pinpoint with AWS SDKs.

- [CreateApp](https://docs.aws.amazon.com/pinpoint/latest/developerguide/pinpoint_example_pinpoint_CreateApp_section.html): Use CreateApp with an AWS SDK or CLI
- [CreateCampaign](https://docs.aws.amazon.com/pinpoint/latest/developerguide/pinpoint_example_pinpoint_CreateCampaign_section.html): Use CreateCampaign with an AWS SDK
- [CreateExportJob](https://docs.aws.amazon.com/pinpoint/latest/developerguide/pinpoint_example_pinpoint_CreateExportJob_section.html): Use CreateExportJob with an AWS SDK
- [CreateImportJob](https://docs.aws.amazon.com/pinpoint/latest/developerguide/pinpoint_example_pinpoint_CreateImportJob_section.html): Use CreateImportJob with an AWS SDK
- [CreateSegment](https://docs.aws.amazon.com/pinpoint/latest/developerguide/pinpoint_example_pinpoint_CreateSegment_section.html): Use CreateSegment with an AWS SDK
- [DeleteApp](https://docs.aws.amazon.com/pinpoint/latest/developerguide/pinpoint_example_pinpoint_DeleteApp_section.html): Use DeleteApp with an AWS SDK or CLI
- [DeleteEndpoint](https://docs.aws.amazon.com/pinpoint/latest/developerguide/pinpoint_example_pinpoint_DeleteEndpoint_section.html): Use DeleteEndpoint with an AWS SDK
- [GetEndpoint](https://docs.aws.amazon.com/pinpoint/latest/developerguide/pinpoint_example_pinpoint_GetEndpoint_section.html): Use GetEndpoint with an AWS SDK or CLI
- [GetSegments](https://docs.aws.amazon.com/pinpoint/latest/developerguide/pinpoint_example_pinpoint_GetSegments_section.html): Use GetSegments with an AWS SDK
- [GetSmsChannel](https://docs.aws.amazon.com/pinpoint/latest/developerguide/pinpoint_example_pinpoint_GetSmsChannel_section.html): Use GetSmsChannel with an AWS SDK or CLI
- [GetUserEndpoints](https://docs.aws.amazon.com/pinpoint/latest/developerguide/pinpoint_example_pinpoint_GetUserEndpoints_section.html): Use GetUserEndpoints with an AWS SDK
- [SendMessages](https://docs.aws.amazon.com/pinpoint/latest/developerguide/pinpoint_example_pinpoint_SendMessages_section.html): Use SendMessages with an AWS SDK or CLI
- [UpdateEndpoint](https://docs.aws.amazon.com/pinpoint/latest/developerguide/pinpoint_example_pinpoint_UpdateEndpoint_section.html): Use UpdateEndpoint with an AWS SDK

### [Amazon Pinpoint SMS and Voice API](https://docs.aws.amazon.com/pinpoint/latest/developerguide/service_code_examples_pinpoint-sms-voice.html)

Code examples that show how to use Amazon Pinpoint SMS and Voice API with an AWS SDK.

### [Basics](https://docs.aws.amazon.com/pinpoint/latest/developerguide/service_code_examples_pinpoint-sms-voice_basics.html)

The following code examples show how to use the basics of Amazon Pinpoint SMS and Voice API with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/pinpoint/latest/developerguide/service_code_examples_pinpoint-sms-voice_actions.html)

The following code examples show how to use Amazon Pinpoint SMS and Voice API with AWS SDKs.

- [CreateConfigurationSet](https://docs.aws.amazon.com/pinpoint/latest/developerguide/pinpoint-sms-voice_example_pinpoint-sms-voice_CreateConfigurationSet_section.html): Use CreateConfigurationSet with an AWS SDK
- [CreateConfigurationSetEventDestination](https://docs.aws.amazon.com/pinpoint/latest/developerguide/pinpoint-sms-voice_example_pinpoint-sms-voice_CreateConfigurationSetEventDestination_section.html): Use CreateConfigurationSetEventDestination with an AWS SDK
- [DeleteConfigurationSet](https://docs.aws.amazon.com/pinpoint/latest/developerguide/pinpoint-sms-voice_example_pinpoint-sms-voice_DeleteConfigurationSet_section.html): Use DeleteConfigurationSet with an AWS SDK
- [DeleteConfigurationSetEventDestination](https://docs.aws.amazon.com/pinpoint/latest/developerguide/pinpoint-sms-voice_example_pinpoint-sms-voice_DeleteConfigurationSetEventDestination_section.html): Use DeleteConfigurationSetEventDestination with an AWS SDK
- [GetConfigurationSetEventDestinations](https://docs.aws.amazon.com/pinpoint/latest/developerguide/pinpoint-sms-voice_example_pinpoint-sms-voice_GetConfigurationSetEventDestinations_section.html): Use GetConfigurationSetEventDestinations with an AWS SDK
- [ListConfigurationSets](https://docs.aws.amazon.com/pinpoint/latest/developerguide/pinpoint-sms-voice_example_pinpoint-sms-voice_ListConfigurationSets_section.html): Use ListConfigurationSets with an AWS SDK
- [SendVoiceMessage](https://docs.aws.amazon.com/pinpoint/latest/developerguide/pinpoint-sms-voice_example_pinpoint-sms-voice_SendVoiceMessage_section.html): Use SendVoiceMessage with an AWS SDK
- [UpdateConfigurationSetEventDestination](https://docs.aws.amazon.com/pinpoint/latest/developerguide/pinpoint-sms-voice_example_pinpoint-sms-voice_UpdateConfigurationSetEventDestination_section.html): Use UpdateConfigurationSetEventDestination with an AWS SDK


## [Security](https://docs.aws.amazon.com/pinpoint/latest/developerguide/security.html)

### [Data protection](https://docs.aws.amazon.com/pinpoint/latest/developerguide/security-data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Pinpoint.

- [Data encryption](https://docs.aws.amazon.com/pinpoint/latest/developerguide/security-data-protection-encryption.html): Learn how Amazon Pinpoint secures your data in transit and at rest.
- [Internetwork traffic privacy](https://docs.aws.amazon.com/pinpoint/latest/developerguide/security-data-protection-internetwork-traffic.html): Describes how you can secure connections between Amazon Pinpoint and other locations.
- [Creating an interface VPC endpoint for Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/developerguide/security-vpc-endpoints.html): You can establish a private connection between your virtual private cloud (VPC) and an endpoint in Amazon Pinpoint by creating an interface VPC endpoint.

### [Identity and access management](https://docs.aws.amazon.com/pinpoint/latest/developerguide/security-iam.html)

Learn how to authenticate requests and manage access for your Amazon Pinpoint resources.

- [How Amazon Pinpoint works with IAM](https://docs.aws.amazon.com/pinpoint/latest/developerguide/security_iam_service-with-iam.html): To use Amazon Pinpoint, users in your AWS account require permissions that allow them to view analytics data, create projects, define user segments, deploy campaigns, and more.
- [Amazon Pinpoint policy actions](https://docs.aws.amazon.com/pinpoint/latest/developerguide/permissions-actions.html): Manage Amazon Pinpoint access by adding actions to IAM policies for users and resources in your AWS account.
- [Identity-based policy examples](https://docs.aws.amazon.com/pinpoint/latest/developerguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon Pinpoint resources.

### [IAM roles for common tasks](https://docs.aws.amazon.com/pinpoint/latest/developerguide/security_iam_roles-common.html)

An IAM role is an AWS Identity and Access Management (IAM) identity that you can create in your AWS account and grant specific permissions.

- [Importing endpoints or segments](https://docs.aws.amazon.com/pinpoint/latest/developerguide/permissions-import-segment.html): Create an IAM role that enables you to import user segment definitions into Amazon Pinpoint.
- [Exporting endpoints or segments](https://docs.aws.amazon.com/pinpoint/latest/developerguide/permissions-export-endpoints.html): Create an IAM role that enables you to export Amazon Pinpoint segment information to Amazon Simple Storage Service (Amazon S3).
- [Retrieving recommendations](https://docs.aws.amazon.com/pinpoint/latest/developerguide/permissions-get-recommendations.html): Create an IAM role that enables Amazon Pinpoint to retrieve recommendation data from an Amazon Personalize campaign.
- [Streaming events to Kinesis](https://docs.aws.amazon.com/pinpoint/latest/developerguide/permissions-streams.html): Create an IAM role that enables Amazon Pinpoint to automatically send event data to Amazon Kinesis.
- [Sending email with Amazon SES](https://docs.aws.amazon.com/pinpoint/latest/developerguide/permissions-ses.html): Create an IAM role that sets up Amazon Pinpoint to automatically send email through Amazon SES.
- [Troubleshooting](https://docs.aws.amazon.com/pinpoint/latest/developerguide/security_iam_troubleshoot.html): Use the following information to diagnose and fix common issues that you might encounter when working with Amazon Pinpoint and IAM.
- [Logging and monitoring](https://docs.aws.amazon.com/pinpoint/latest/developerguide/security-incident-response.html): Learn about tools for monitoring Amazon Pinpoint resources and responding to incidents.
- [Compliance validation](https://docs.aws.amazon.com/pinpoint/latest/developerguide/security-compliance-validation.html): Learn what AWS services are in scope for a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/pinpoint/latest/developerguide/security-disaster-recovery-resiliency.html): Learn how the AWS architecture supports data redundancy, and learn about specific Amazon Pinpoint features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/pinpoint/latest/developerguide/security-infrastructure-security.html): Learn how Amazon Pinpoint isolates service traffic.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/pinpoint/latest/developerguide/security-vulnerability-analysis-management.html): Learn about customer responsibilities for hardening, updating, and patching Amazon Pinpoint.
- [Security best practices](https://docs.aws.amazon.com/pinpoint/latest/developerguide/security-best-practices.html): Amazon Pinpoint; provides a number of security features to consider as you develop and implement your own security policies.
