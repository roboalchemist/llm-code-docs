# Source: https://docs.aws.amazon.com/iotevents/latest/developerguide/llms.txt

# AWS IoT Events Developer Guide

> Describes how to use the service to monitor your equipment or device fleets for failures or changes in operation, and to trigger actions when such events occur.

- [What is AWS IoT Events?](https://docs.aws.amazon.com/iotevents/latest/developerguide/what-is-iotevents.html)
- [Best practices](https://docs.aws.amazon.com/iotevents/latest/developerguide/best-practices.html)
- [Quotas](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-quotas.html)
- [Tagging](https://docs.aws.amazon.com/iotevents/latest/developerguide/tagging-iotevents.html)
- [Commands](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commands.html)
- [Document history](https://docs.aws.amazon.com/iotevents/latest/developerguide/doc-history.html)

## [AWS IoT Events end of support](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-end-of-support.html)

- [Detector models](https://docs.aws.amazon.com/iotevents/latest/developerguide/eos-procedure-detector-models.html): This section describes alternative solutions that deliver similar detector model functionality as you migrate away from AWS IoT Events.
- [Alarms](https://docs.aws.amazon.com/iotevents/latest/developerguide/eos-procedure-alarms.html): This section describes alternative solutions that deliver similar alarm functionality as you migrate away from AWS IoT Events.


## [Setting up](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-start.html)

### [Setting up permissions for AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-permissions.html)

Configuring permissions and access control for AWS IoT Events resources and operations.

- [Action permissions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-permissions-event-actions.html): Setting IAM permissions for AWS IoT Events event actions like Amazon SNS and Lambda.
- [Securing input data](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-permissions-input-data.html): Configuring AWS IoT Events access for input data for use in a detector model.
- [Amazon CloudWatch logging role policy](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-permissions-cloudwatch.html): Setting IAM policies to allow AWS IoT Events access to CloudWatch.
- [Amazon SNS messaging role policy](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-permissions-sns.html): Configuring AWS IoT Events to publish notifications to Amazon SNS topics with IAM policies.


## [Getting started](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-getting-started.html)

- [Prerequisites](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-getting-started-prereqs.html): The prerequisites and steps required before getting started with AWS IoT Events.

### [Create an input](https://docs.aws.amazon.com/iotevents/latest/developerguide/create-input-overview.html)

This section describes how to create an AWS IoT Events input.

- [Create an input within the Detector Model](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-detector-input.html): Configuration details for the different input types supported in AWS IoT Events detectors.
- [Create a detector model](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-detector-model.html): In this section, you define an AWS IoT Events detector model, which is a model of your equipment or process, using states.
- [Test the detector model](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-iot-rules-engine.html): This topic shows you how to create an AWS IoT rule in the AWS IoT console that forwards messages as inputs to your AWS IoT Events detector.


## [Tutorials](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-tutorials.html)

- [Using AWS IoT Events to monitor your IoT devices](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-how-to-use.html): How to use AWS IoT Events to detect events from IoT devices and take actions.

### [Simple step-by-step example](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-simple-example.html)

Use the AWS IoT Events APIs using AWS CLI commands to create a detector that models two states of an engine: a normal state and an over-pressure condition.

- [Create an input to capture device data](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-create-input.html): How to create input in AWS IoT Events to ingest data from IoT devices.
- [Create a detector model to represent device states](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-create-detector.html): How to create a detector model in AWS IoT Events to analyze input data and detect events.
- [Send messages as inputs to a detector](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-batch-put-messages.html): How to ingest batch data into AWS IoT Events using the BatchPutMessage API.
- [Detector model restrictions and limitations](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-restrictions-detector-model.html): Restrictions and limits when creating AWS IoT Events detector models.

### [A commented example: HVAC temperature control](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commented-example.html)

This demo showcases a temperature control model with remote thermostats, anomaly detection, emergency overrides, and adjustable settings for efficient monitoring.

- [Input definitions for detector models](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commented-example-inputs.html): Defining inputs in AWS IoT Events detector models to ingest and process IoT device data.
- [Create a detector model definition](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commented-example-detector-model.html): Building an example detector model in AWS IoT Events.
- [Use BatchUpdateDetector](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commented-example-batch-update-detector.html): Using batch operations to update the AWS IoT Events detector model.
- [Use BatchPutMessage for inputs](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commented-example-input-usage-examples.html): Example use cases for AWS IoT Events inputs like timers, asset properties, and IoT messages.
- [Ingest MQTT messages](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commented-example-ingest-mqtt.html): Ingesting MQTT messages from IoT devices into AWS IoT Events.
- [Generate Amazon SNS messages](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commented-example-generated-sns.html): Using the AWS IoT Events detector instance to generate Amazon SNS messages.
- [Configure the DescribeDetector API](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commented-example-describe-detector.html): AWS IoT Events detector configurations using the DescribeDetector API.
- [Use the AWS IoT Core rules engine](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commented-examples-iot-rules-examples.html): This page contains a few example uses of the AWS IoT Core rule engine for AWS IoT Events.


## [Supported actions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-supported-actions.html)

- [Use built-in actions](https://docs.aws.amazon.com/iotevents/latest/developerguide/built-in-actions.html): Use AWS IoT Events built-in actions to use a timer or set a variable.
- [Work with other AWS services](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-other-aws-services.html): You can configure the action payload when AWS IoT Events works with other AWS services.


## [Expressions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html)

- [Usage](https://docs.aws.amazon.com/iotevents/latest/developerguide/expression-usage.html): Guidelines and examples for using expressions in AWS IoT Events to filter, transform, and process event data.


## [Detector model examples](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-examples.html)

### [HVAC temperature control](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-examples-hvac.html)

An overview of the AWS IoT Events HVAC system example covering inputs, detectors, models, and actions.

- [Input definitions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-examples-hvac-inputs.html): Configuring AWS IoT Events inputs for the HVAC system example.
- [Detector model definition](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-examples-hvac-detector-model.html): Using AWS IoT Events detectors in HVAC system example to identify states based on input data.
- [BatchPutMessage examples](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-examples-hvac-input-usage-examples.html): Using AWS IoT Events inputs in HVAC system example for temperature and operational data.
- [BatchUpdateDetector example](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-examples-hvac-batch-update-detector.html): Batch updating AWS IoT Events HVAC detectors using the CLI.
- [AWS IoT Core rules engine](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-examples-hvac-iot-rules-examples.html): Configuring the AWS IoT Core rules engine for AWS IoT Events using an HVAC example.
- [Cranes](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-examples-cranes.html): An AWS IoT Events example application for monitoring cranes and detecting unsafe operating conditions.
- [Send commands](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-examples-cranes-commands.html): Sending commands in response to detected conditions in the AWS IoT Events crane monitoring example application.
- [Detector models](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-examples-cranes-detector-models.html): Detector models in the AWS IoT Events crane monitoring example application.
- [Inputs](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-examples-cranes-inputs.html): Configuring inputs in the AWS IoT Events crane monitoring example application.
- [Messages](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-examples-cranes-messages.html): Sending alarm and operational messages in the AWS IoT Events crane monitoring example application.
- [Example: Event detection with sensors](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-examples-edwsaa.html): An example showing how a detector model can be used with sensors.
- [Device HeartBeat](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-examples-dhb.html): An example showing how a detector model can be used to monitor device connections using device HeartBeat.
- [ISA alarm](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-examples-bisaa.html): An example showing how a detector model can be used to monitor device connections.
- [Simple alarm](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-examples-bsa.html): An example showing how a detector model can be used to create simple alarms.


## [Monitoring with alarms](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-alarms.html)

- [Creating an alarm model](https://docs.aws.amazon.com/iotevents/latest/developerguide/create-alarm-model.html): This section shows you how to create an AWS IoT Events alarm model.
- [Responding to alarms](https://docs.aws.amazon.com/iotevents/latest/developerguide/respond-to-alarms.html): How to respond to AWS IoT Events alarms using the AWS IoT Events console or the AWS IoT Events API reference.

### [Managing alarm notifications](https://docs.aws.amazon.com/iotevents/latest/developerguide/lambda-support.html)

Using Lambda functions to manage AWS IoT Events alarm notifications.

### [Creating a Lambda function](https://docs.aws.amazon.com/iotevents/latest/developerguide/alarms-create-lambda.html)

AWS IoT Events provides a Lambda function that enables alarms to send and receive email and SMS notifications.

- [Deploy a Lambda function for AWS IoT Events using CloudFormation](https://docs.aws.amazon.com/iotevents/latest/developerguide/alarms-create-lambda-cfn.html): Use CloudFormation to create a Lambda function to process AWS IoT Events alarms.
- [Creating a custom Lambda function](https://docs.aws.amazon.com/iotevents/latest/developerguide/alarms-create-custom-lambda.html): Create a custom Lambda function in Node.js to process AWS IoT Events alarms.
- [Using the Lambda function](https://docs.aws.amazon.com/iotevents/latest/developerguide/use-alarm-notifications.html): How to use the Lambda function provided by AWS IoT Events for managing alarm notifications.
- [Manage alarm recipients](https://docs.aws.amazon.com/iotevents/latest/developerguide/sso-authorization-recipients.html): Using IAM Identity Center to manage access of alarms recipients in AWS IoT Events


## [Security](https://docs.aws.amazon.com/iotevents/latest/developerguide/security.html)

### [Identity and access management](https://docs.aws.amazon.com/iotevents/latest/developerguide/security-iam.html)

How to authenticate requests and manage access to your AWS IoT Events resources.

- [Authenticating with identities](https://docs.aws.amazon.com/iotevents/latest/developerguide/security_iam_authentication.html): Authenticating identities using IAM with AWS IoT Events.
- [Managing access using policies](https://docs.aws.amazon.com/iotevents/latest/developerguide/security_iam_access-manage.html): Managing access to AWS IoT Events using IAM identity-based policies.

### [Identity-based policy examples](https://docs.aws.amazon.com/iotevents/latest/developerguide/security_iam_id-based-policy-examples.html)

Example IAM identity-based policies for AWS IoT Events access control.

- [Policy best practices](https://docs.aws.amazon.com/iotevents/latest/developerguide/security_iam_service-with-iam-policy-best-practices.html): Best practices for IAM policies with AWS IoT Events.
- [Using the console](https://docs.aws.amazon.com/iotevents/latest/developerguide/security_iam_id-based-policy-examples-console.html): Example IAM identity-based policies using the AWS Management Console with AWS IoT Events.
- [Allow users to view their own permissions](https://docs.aws.amazon.com/iotevents/latest/developerguide/security_iam_id-based-policy-examples-view-own-permissions.html): Example IAM policy to view your own permissions in AWS IoT Events.
- [Access one input](https://docs.aws.amazon.com/iotevents/latest/developerguide/security_iam_id-based-policy-examples-access-one-input.html): Example IAM policy to access one AWS IoT Events input.
- [Viewing inputs based on tags](https://docs.aws.amazon.com/iotevents/latest/developerguide/security_iam_id-based-policy-examples-view-input-tags.html): Example IAM policy to view tags for an AWS IoT Events input.

### [Cross-service confused deputy prevention for AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/cross-service-confused-deputy-prevention.html)

Guidance on using IAM roles and policies to prevent confused deputy security issues when integrating AWS IoT Events with other AWS services.

- [Example: Secure access to a detector model](https://docs.aws.amazon.com/iotevents/latest/developerguide/accessing-a-detector-model.html): How to grant access to a detector model in AWS IoT Events.
- [Example: Secure access to an AWS IoT Events alarm model](https://docs.aws.amazon.com/iotevents/latest/developerguide/accessing-an-alarm-model.html): How to grant a particular role access to an alarm model in AWS IoT Events.
- [Example: Access a resource in a specified region](https://docs.aws.amazon.com/iotevents/latest/developerguide/accessing-resource-in-specified-region.html): Accessing AWS IoT Events resources across regions programmatically.
- [Example: Configure logging options;](https://docs.aws.amazon.com/iotevents/latest/developerguide/logging-options.html): Configure logging options for AWS IoT Events by allowing access your AWS IoT Events resources.
- [Troubleshooting](https://docs.aws.amazon.com/iotevents/latest/developerguide/security_iam_troubleshoot.html): Troubleshooting IAM identity-based policies for AWS IoT Events.

### [Monitoring](https://docs.aws.amazon.com/iotevents/latest/developerguide/monitoring_overview.html)

Lists the items to monitor to maintain the reliability, availability, and performance of AWS IoT Events.

- [Available tools to monitor AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/monitoring_automated_manual.html): An overview of the available automated and manual configuration tools used to monitor AWS IoT Events.
- [Monitoring AWS IoT Events with Amazon CloudWatch](https://docs.aws.amazon.com/iotevents/latest/developerguide/monitoring-cloudwatch.html): Monitoring AWS IoT Events with CloudWatch metrics and logs.

### [Logging AWS IoT Events API calls with AWS CloudTrail](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-using-cloudtrail.html)

Using CloudTrail to monitor AWS IoT Events API calls.

- [Understanding AWS IoT Events log file entries](https://docs.aws.amazon.com/iotevents/latest/developerguide/understanding-aws-iotevents-entries.html): Understanding AWS IoT Events log entries in CloudTrail.
- [Compliance validation](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-compliance.html): Compliance guidelines and information for using AWS IoT Events to ensure security, governance, and regulatory requirements.
- [Resilience](https://docs.aws.amazon.com/iotevents/latest/developerguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS IoT Events features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/iotevents/latest/developerguide/infrastructure-security.html): Learn how AWS IoT Events isolates service traffic.


## [Troubleshooting](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-troubleshooting.html)

- [Common AWS IoT Events issues and solutions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-error-messages.html): Reference for error messages in AWS IoT Events to help troubleshoot issues.

### [Troubleshooting a detector model](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-analyze-api.html)

AWS IoT Events can analyze your detector model and generate analysis results that you can use to troubleshoot your detector model.

- [Diagnostic information](https://docs.aws.amazon.com/iotevents/latest/developerguide/analyze-diagnostic-information.html): Learn about detector model and analysis results in AWS IoT Events so that you can troubleshoot errors with your detector model.
- [Analyze a detector model (Console)](https://docs.aws.amazon.com/iotevents/latest/developerguide/analyze-api-console.html): Use the AWS Management Console to analyze AWS IoT Events APIs.
- [Analyze a detector model (AWS CLI)](https://docs.aws.amazon.com/iotevents/latest/developerguide/analyze-api-api.html): Use the AWS IoT Events API to analyze a detector model to gain valuable insights.
