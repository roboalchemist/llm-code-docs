# Source: https://docs.aws.amazon.com/greengrass/v1/developerguide/llms.txt

# AWS IoT Greengrass Developer Guide, Version 1

- [AWS IoT Greengrass V1 maintenance policy](https://docs.aws.amazon.com/greengrass/v1/developerguide/maintenance-policy.html)
- [OTA updates of AWS IoT Greengrass Core software](https://docs.aws.amazon.com/greengrass/v1/developerguide/core-ota-update.html)
- [Greengrass Discovery RESTful API](https://docs.aws.amazon.com/greengrass/v1/developerguide/gg-discover-api.html)
- [Tagging your Greengrass resources](https://docs.aws.amazon.com/greengrass/v1/developerguide/tagging.html)
- [CloudFormation support for AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v1/developerguide/cloudformation-support.html)
- [Troubleshooting](https://docs.aws.amazon.com/greengrass/v1/developerguide/gg-troubleshooting.html)
- [Document history](https://docs.aws.amazon.com/greengrass/v1/developerguide/doc-history.html)

## [What is AWS IoT Greengrass?](https://docs.aws.amazon.com/greengrass/v1/developerguide/what-is-gg.html)

- [Install the AWS IoT Greengrass Core software](https://docs.aws.amazon.com/greengrass/v1/developerguide/install-ggc.html): Learn about the different ways that you can install the AWS IoT Greengrass Core software.
- [Configure the AWS IoT Greengrass core](https://docs.aws.amazon.com/greengrass/v1/developerguide/gg-core.html): Learn how to configure the AWS IoT Greengrass core.


## [Getting started with AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v1/developerguide/gg-gs.html)

- [Quick start: Greengrass device setup](https://docs.aws.amazon.com/greengrass/v1/developerguide/quick-start.html): Get started using AWS IoT Greengrass by running the Greengrass device setup script.

### [Module 1: Environment setup for Greengrass](https://docs.aws.amazon.com/greengrass/v1/developerguide/module1.html)

This module shows you how to get an out-of-the-box Raspberry Pi, Amazon EC2 instance, or other device ready to be used by AWS IoT Greengrass as your AWS IoT Greengrass core device.

- [Setting up a Raspberry Pi](https://docs.aws.amazon.com/greengrass/v1/developerguide/setup-filter.rpi.html): Follow the steps in this topic to set up a Raspberry Pi to use as an AWS IoT Greengrass core.
- [Setting up an Amazon EC2 instance](https://docs.aws.amazon.com/greengrass/v1/developerguide/setup-filter.ec2.html): Follow the steps in this topic to set up an Amazon EC2 instance to use as your AWS IoT Greengrass core.
- [Setting up other devices](https://docs.aws.amazon.com/greengrass/v1/developerguide/setup-filter.other.html): Follow the steps in this topic to set up a device (other than a Raspberry Pi) to use as your AWS IoT Greengrass core.

### [Module 2: Installing the AWS IoT Greengrass Core software](https://docs.aws.amazon.com/greengrass/v1/developerguide/module2.html)

This module of the Getting Started tutorial shows you how to download, configure, and start the AWS IoT Greengrass Core software on your core device.

- [Provision an AWS IoT thing to use as a Greengrass core](https://docs.aws.amazon.com/greengrass/v1/developerguide/provision-core.html): AWS IoT Greengrass cores are AWS IoT things.
- [Create an Greengrass group](https://docs.aws.amazon.com/greengrass/v1/developerguide/create-group.html): Create an AWS IoT Greengrass group to manage and deploy configurations for your Greengrass core.
- [Install and run AWS IoT Greengrass on the core device](https://docs.aws.amazon.com/greengrass/v1/developerguide/start-greengrass.html): Configure and install the AWS IoT Greengrass Core software on your device to connect it to AWS.

### [Module 3 (part 1): Lambda functions on AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v1/developerguide/module3-I.html)

This module shows you how to create and deploy a Lambda function that sends MQTT messages from your AWS IoT Greengrass core device.

- [Create and package a Lambda function](https://docs.aws.amazon.com/greengrass/v1/developerguide/create-lambda.html): The example Python Lambda function in this module uses the AWS IoT Greengrass Core SDK for Python to publish MQTT messages.
- [Configure the Lambda function for AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v1/developerguide/config-lambda.html): You are now ready to configure your Lambda function for AWS IoT Greengrass.
- [Deploy cloud configurations to a core device](https://docs.aws.amazon.com/greengrass/v1/developerguide/configs-core.html)
- [Verify the Lambda function is running on the core device](https://docs.aws.amazon.com/greengrass/v1/developerguide/lambda-check.html)

### [Module 3 (part 2): Lambda functions on AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v1/developerguide/module3-II.html)

This module explores the differences between on-demand and long-lived Lambda functions running on the AWS IoT Greengrass core.

- [Create and package the Lambda function](https://docs.aws.amazon.com/greengrass/v1/developerguide/package.html): In this step, you:
- [Configure long-lived Lambda functions for AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v1/developerguide/long-lived.html): You are now ready to configure your Lambda function for AWS IoT Greengrass.
- [Test long-lived Lambda functions](https://docs.aws.amazon.com/greengrass/v1/developerguide/long-testing.html): A long-lived Lambda function starts automatically when the AWS IoT Greengrass core starts and runs in a single container (or sandbox).
- [Test on-demand Lambda functions](https://docs.aws.amazon.com/greengrass/v1/developerguide/on-demand.html): An on-demand Lambda function is similar in functionality to a cloud-based AWS Lambda function.

### [Module 4: Interacting with client devices in an AWS IoT Greengrass group](https://docs.aws.amazon.com/greengrass/v1/developerguide/module4.html)

This module shows you how local IoT devices, called client devices or devices, can connect to and communicate with an AWS IoT Greengrass core device.

- [Create client devices in an AWS IoT Greengrass group](https://docs.aws.amazon.com/greengrass/v1/developerguide/device-group.html): In this step, you add two client devices to your Greengrass group.
- [Configure subscriptions](https://docs.aws.amazon.com/greengrass/v1/developerguide/config-subs.html): In this step, you enable the HelloWorld_Publisher client device to send MQTT messages to the HelloWorld_Subscriber client device.
- [Install the AWS IoT Device SDK for Python](https://docs.aws.amazon.com/greengrass/v1/developerguide/IoT-SDK.html): Learn how to install the AWS IoT Device SDK for Python for Module 4 of the Getting Started tutorial.
- [Test communications](https://docs.aws.amazon.com/greengrass/v1/developerguide/test-comms.html)

### [Module 5: Interacting with device shadows](https://docs.aws.amazon.com/greengrass/v1/developerguide/module5.html)

This advanced module shows you how client devices can interact with AWS IoT device shadows in an AWS IoT Greengrass group.

- [Configure devices and subscriptions](https://docs.aws.amazon.com/greengrass/v1/developerguide/config-dev-subs.html): Shadows can be synced to AWS IoT when the AWS IoT Greengrass core is connected to the internet.
- [Download required files](https://docs.aws.amazon.com/greengrass/v1/developerguide/file-download.html)
- [Test communications (device syncs disabled)](https://docs.aws.amazon.com/greengrass/v1/developerguide/comms-disabled.html)
- [Test communications (device syncs enabled)](https://docs.aws.amazon.com/greengrass/v1/developerguide/comms-enabled.html): For this test, you configure the GG_TrafficLight device shadow to sync to AWS IoT.

### [Module 6: Accessing other AWS services](https://docs.aws.amazon.com/greengrass/v1/developerguide/module6.html)

This advanced module shows you how AWS IoT Greengrass cores can interact with other AWS services in the cloud.

- [Configure the group role](https://docs.aws.amazon.com/greengrass/v1/developerguide/config-iam-roles.html): The group role is an IAM role that you create and attach to your Greengrass group.
- [Create and configure the Lambda function](https://docs.aws.amazon.com/greengrass/v1/developerguide/create-config-lambda.html): In this step, you create a Lambda function that tracks the number of cars that pass the traffic light.
- [Configure subscriptions](https://docs.aws.amazon.com/greengrass/v1/developerguide/config_subs.html): In this step, you create a subscription that enables the GG_TrafficLight shadow to send updated state information to the GG_Car_Aggregator Lambda function.
- [Test communications](https://docs.aws.amazon.com/greengrass/v1/developerguide/comms-test.html)
- [Module 7: Simulating hardware security integration](https://docs.aws.amazon.com/greengrass/v1/developerguide/console-mod7.html): Walk through steps to configure hardware security on an AWS IoT Greengrass core using a simulated, software-only implementation.


## [Deploy AWS IoT Greengrass groups](https://docs.aws.amazon.com/greengrass/v1/developerguide/deployments.html)

- [Get deployment notifications](https://docs.aws.amazon.com/greengrass/v1/developerguide/deployment-notifications.html): Learn how to use Amazon EventBridge to create a rule for AWS IoT Greengrass deployment state changes.
- [Reset deployments](https://docs.aws.amazon.com/greengrass/v1/developerguide/reset-deployments-scenario.html): This feature is available for AWS IoT Greengrass Core v1.1 and later.
- [Create bulk deployments](https://docs.aws.amazon.com/greengrass/v1/developerguide/bulk-deploy-cli.html): Describes how to use the AWS CLI to create and monitor a group bulk deployment in AWS IoT Greengrass.


## [Run local Lambda functions](https://docs.aws.amazon.com/greengrass/v1/developerguide/lambda-functions.html)

- [Controlling Greengrass Lambda function execution](https://docs.aws.amazon.com/greengrass/v1/developerguide/lambda-group-config.html): Learn about running Lambda functions on the AWS IoT Greengrass core.
- [Run AWS IoT Greengrass in a Docker container](https://docs.aws.amazon.com/greengrass/v1/developerguide/run-gg-in-docker-container.html): Learn how to pull an AWS IoT Greengrass container image from Amazon ECR and run Greengrass in a Docker container.


## [Access local resources](https://docs.aws.amazon.com/greengrass/v1/developerguide/access-local-resources.html)

- [Using the CLI](https://docs.aws.amazon.com/greengrass/v1/developerguide/lra-cli.html): Learn how to use the AWS CLI to add a local resource to an AWS IoT Greengrass group and configure access to the local resource for Lambda functions.
- [Using the console](https://docs.aws.amazon.com/greengrass/v1/developerguide/lra-console.html): Use the AWS Management Console to add a local resource to an AWS IoT Greengrass group and configure access to the local resource for Lambda functions.


## [Perform machine learning inference](https://docs.aws.amazon.com/greengrass/v1/developerguide/ml-inference.html)

- [Access machine learning resources](https://docs.aws.amazon.com/greengrass/v1/developerguide/access-ml-resources.html): Learn how Lambda functions can access machine learning resources.
- [How to configure machine learning inference](https://docs.aws.amazon.com/greengrass/v1/developerguide/ml-console.html): Use the AWS Management Console to configure an AWS IoT Greengrass group to run machine learning (ML) inference locally on a core device.
- [How to configure optimized machine learning inference](https://docs.aws.amazon.com/greengrass/v1/developerguide/ml-dlc-console.html): Learn how to use the AWS Management Console to configure an AWS IoT Greengrass group to run machine learning (ML) inference locally on a core device.


## [Manage data streams](https://docs.aws.amazon.com/greengrass/v1/developerguide/stream-manager.html)

- [Configure stream manager](https://docs.aws.amazon.com/greengrass/v1/developerguide/configure-stream-manager.html): On the AWS IoT Greengrass core, stream manager can store, process, and export IoT device data.

### [Use StreamManagerClient to work with streams](https://docs.aws.amazon.com/greengrass/v1/developerguide/work-with-streams.html)

User-defined Lambda functions running on the AWS IoT Greengrass core can use the StreamManagerClient object in the AWS IoT Greengrass Core SDK to create streams in stream manager and then interact with the streams.

- [Export configurations for supported AWS Cloud destinations](https://docs.aws.amazon.com/greengrass/v1/developerguide/stream-export-configurations.html): Learn how to configure the ExportDefinition object in the AWS IoT Greengrass Core SDK to automatically export data streams to the AWS Cloud.
- [Export data streams (console)](https://docs.aws.amazon.com/greengrass/v1/developerguide/stream-manager-console.html): Use the AWS IoT console to configure an AWS IoT Greengrass group and enable stream manager.
- [Export data streams (CLI)](https://docs.aws.amazon.com/greengrass/v1/developerguide/stream-manager-cli.html): Learn how to use the AWS CLI to configure an AWS IoT Greengrass group with stream manager enabled.


## [Deploy secrets to the core](https://docs.aws.amazon.com/greengrass/v1/developerguide/secrets.html)

- [Work with secret resources](https://docs.aws.amazon.com/greengrass/v1/developerguide/secrets-using.html): Learn how to create, manage, and use secrets in AWS IoT Greengrass.
- [How to create a secret resource (console)](https://docs.aws.amazon.com/greengrass/v1/developerguide/secrets-console.html): Learn how to use the AWS Management Console to create a secret resource and attach it to a Lambda function.


## [Integrate with services and protocols using connectors](https://docs.aws.amazon.com/greengrass/v1/developerguide/connectors.html)

### [AWS-provided Greengrass connectors](https://docs.aws.amazon.com/greengrass/v1/developerguide/connectors-list.html)

Describes connectors that are provided by AWS and their requirements.

- [CloudWatch Metrics](https://docs.aws.amazon.com/greengrass/v1/developerguide/cloudwatch-metrics-connector.html): Learn how to use the CloudWatch Metrics connector.
- [Device Defender](https://docs.aws.amazon.com/greengrass/v1/developerguide/device-defender-connector.html): The Device Defender connector notifies administrators of changes in the state of a Greengrass core device.
- [Docker application deployment](https://docs.aws.amazon.com/greengrass/v1/developerguide/docker-app-connector.html): Learn how to use the Greengrass Docker application deployment connector.
- [IoT Analytics](https://docs.aws.amazon.com/greengrass/v1/developerguide/iot-analytics-connector.html): Learn how to use the IoT Analytics connector to collect data from devices and sensors and send the data to AWS IoT Analytics.
- [IoT Ethernet IP Protocol Adapter](https://docs.aws.amazon.com/greengrass/v1/developerguide/ethernet-ip-connector.html): The IoT Ethernet IP Protocol Adapter connector collects data from local devices using the Ethernet/IP protocol.
- [IoT SiteWise](https://docs.aws.amazon.com/greengrass/v1/developerguide/iot-sitewise-connector.html): Learn how to use the IoT SiteWise connector.
- [Kinesis Firehose](https://docs.aws.amazon.com/greengrass/v1/developerguide/kinesis-firehose-connector.html): The Kinesis Firehose connector publishes data through an Amazon Data Firehose delivery stream to destinations such as Amazon S3, Amazon Redshift, or Amazon OpenSearch Service.
- [ML Feedback](https://docs.aws.amazon.com/greengrass/v1/developerguide/ml-feedback-connector.html): Learn how to use the ML Feedback connector to upload model input to the cloud and publish model output to an MQTT topic.
- [ML Image Classification](https://docs.aws.amazon.com/greengrass/v1/developerguide/image-classification-connector.html): Learn how to use the ML Image Classification connector.
- [ML Object Detection](https://docs.aws.amazon.com/greengrass/v1/developerguide/obj-detection-connector.html): Learn how to use the ML Object Detection connector.
- [Modbus-RTU Protocol Adapter](https://docs.aws.amazon.com/greengrass/v1/developerguide/modbus-protocol-adapter-connector.html): The Modbus-RTU Protocol Adapter connector polls information from Modbus RTU devices that are in the AWS IoT Greengrass group.
- [Modbus-TCP Protocol Adapter](https://docs.aws.amazon.com/greengrass/v1/developerguide/modbus-tcp-connector.html): The Modbus-TCP Protocol Adapter connector collects data from local devices through the ModbusTCP protocol and publishes it to the selected StreamManager streams.
- [Raspberry Pi GPIO](https://docs.aws.amazon.com/greengrass/v1/developerguide/raspberrypi-gpio-connector.html): Learn how to use the Raspberry Pi GPIO connector.
- [Serial Stream](https://docs.aws.amazon.com/greengrass/v1/developerguide/serial-stream-connector.html): Learn how to use the Serial Stream connector.
- [ServiceNow MetricBase Integration](https://docs.aws.amazon.com/greengrass/v1/developerguide/servicenow-connector.html): Learn how to use the ServiceNow MetricBase Integration connector.
- [SNS](https://docs.aws.amazon.com/greengrass/v1/developerguide/sns-connector.html): Learn how to use the SNS connector.
- [Splunk Integration](https://docs.aws.amazon.com/greengrass/v1/developerguide/splunk-connector.html): Learn how to use the Splunk Integration connector.
- [Twilio Notifications](https://docs.aws.amazon.com/greengrass/v1/developerguide/twilio-notifications-connector.html): Learn how to use the Twilio Notifications connector.
- [Get started with connectors (console)](https://docs.aws.amazon.com/greengrass/v1/developerguide/connectors-console.html): Learn how to use the AWS IoT console to configure and deploy a connector.
- [Get started with connectors (CLI)](https://docs.aws.amazon.com/greengrass/v1/developerguide/connectors-cli.html): Learn how to use the AWS CLI to configure and deploy a connector.


## [Security](https://docs.aws.amazon.com/greengrass/v1/developerguide/security.html)

- [Overview of AWS IoT Greengrass security](https://docs.aws.amazon.com/greengrass/v1/developerguide/gg-sec.html): Learn about the AWS IoT Greengrass security model.

### [Data protection](https://docs.aws.amazon.com/greengrass/v1/developerguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in AWS IoT Greengrass.

### [Data encryption](https://docs.aws.amazon.com/greengrass/v1/developerguide/data-encryption.html)

Learn how the AWS shared responsibility model applies to data encryption in AWS IoT Greengrass.

- [Encryption in transit](https://docs.aws.amazon.com/greengrass/v1/developerguide/encryption-in-transit.html): Learn how the AWS shared responsibility model applies to encryption in transit in AWS IoT Greengrass.
- [Encryption at rest](https://docs.aws.amazon.com/greengrass/v1/developerguide/encryption-at-rest.html): Learn how the AWS shared responsibility model applies to encryption at rest in AWS IoT Greengrass.
- [Key management](https://docs.aws.amazon.com/greengrass/v1/developerguide/key-management.html): Learn how the AWS shared responsibility model applies to key management in AWS IoT Greengrass.
- [Hardware security integration](https://docs.aws.amazon.com/greengrass/v1/developerguide/hardware-security.html): Learn how to configure hardware security for AWS IoT Greengrass.
- [Device authentication and authorization](https://docs.aws.amazon.com/greengrass/v1/developerguide/device-auth.html): Learn how Greengrass core devices use X.509 certificates and AWS IoT policies to securely connect to AWS IoT Core and AWS IoT Greengrass.

### [Identity and access management](https://docs.aws.amazon.com/greengrass/v1/developerguide/security-iam.html)

How to authenticate requests and manage access your AWS IoT Greengrass resources.

- [How AWS IoT Greengrass works with IAM](https://docs.aws.amazon.com/greengrass/v1/developerguide/security_iam_service-with-iam.html): Learn which IAM features that AWS IoT Greengrass supports.
- [Greengrass service role](https://docs.aws.amazon.com/greengrass/v1/developerguide/service-role.html): Learn how to manage the required Greengrass service role.
- [Greengrass group role](https://docs.aws.amazon.com/greengrass/v1/developerguide/group-role.html): Learn how to create and configure the group role used by Greengrass Lambda functions and connectors.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/greengrass/v1/developerguide/cross-service-confused-deputy-prevention.html): Prevent cross-service impersonation because of confused deputy issues.
- [Identity-based policy examples](https://docs.aws.amazon.com/greengrass/v1/developerguide/security_iam_id-based-policy-examples.html): See example identity-based policies that you can use with AWS IoT Greengrass.
- [Troubleshooting identity and access issues](https://docs.aws.amazon.com/greengrass/v1/developerguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS IoT Greengrass and IAM.
- [Compliance validation](https://docs.aws.amazon.com/greengrass/v1/developerguide/compliance-validation.html): Learn which AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/greengrass/v1/developerguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS IoT Greengrass features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/greengrass/v1/developerguide/infrastructure-security.html): Learn how AWS IoT Greengrass isolates service traffic.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/greengrass/v1/developerguide/vulnerability-analysis-and-management.html): Learn how the AWS shared responsibility model applies to vulnerability analysis and management in AWS IoT Greengrass.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/greengrass/v1/developerguide/vpc-interface-endpoints.html): Use an interface VPC endpoint to create a private connection between your VPC and AWS IoT Greengrass V1 without requiring internet access, use of a NAT device, a VPN connection, or an Direct Connect connection.
- [Security best practices](https://docs.aws.amazon.com/greengrass/v1/developerguide/security-best-practices.html): Learn about security best practices for AWS IoT Greengrass.


## [Logging and monitoring](https://docs.aws.amazon.com/greengrass/v1/developerguide/logging-and-monitoring.html)

- [Monitoring with AWS IoT Greengrass logs](https://docs.aws.amazon.com/greengrass/v1/developerguide/greengrass-logs-overview.html): Use AWS IoT Greengrass logs to monitor your application.
- [Logging AWS IoT Greengrass API calls with AWS CloudTrail](https://docs.aws.amazon.com/greengrass/v1/developerguide/logging-using-cloudtrail.html): Learn about logging AWS IoT Greengrass with AWS CloudTrail.
- [Gathering system health telemetry data](https://docs.aws.amazon.com/greengrass/v1/developerguide/telemetry.html): Learn about the system health telemetry on the AWS IoT Greengrass core, how to configure telemetry settings, and how to subscribe to receive telemetry data.
- [Calling the local health check API](https://docs.aws.amazon.com/greengrass/v1/developerguide/health-check.html): Learn how to use the health check API to get a snapshot of the state of worker processes started by AWS IoT Greengrass.


## [Using AWS IoT Device Tester for AWS IoT Greengrass V1](https://docs.aws.amazon.com/greengrass/v1/developerguide/device-tester-for-greengrass-ug.html)

- [Supported versions of AWS IoT Device Tester for AWS IoT Greengrass V1](https://docs.aws.amazon.com/greengrass/v1/developerguide/dev-test-versions.html): Lists supported versions of AWS IoT Device Tester for AWS IoT Greengrass V1.

### [Use IDT to run the AWS IoT Greengrass qualification suite](https://docs.aws.amazon.com/greengrass/v1/developerguide/idt-gg-qualification.html)

Describes how to use AWS IoT Device Tester (IDT) to ensure your Linux device is compatible with AWS IoT Greengrass and can communicate with the AWS IoT Cloud.

- [Prerequisites](https://docs.aws.amazon.com/greengrass/v1/developerguide/dev-tst-prereqs.html): Learn how to configure your AWS account to grant permissions required by AWS IoT Device Tester for AWS IoT Greengrass.

### [Configure your device to run IDT tests](https://docs.aws.amazon.com/greengrass/v1/developerguide/device-config-setup.html)

Learn how to configure your device to run IDT tests for AWS IoT Greengrass device qualification.

- [Optional: Configuring your Docker container](https://docs.aws.amazon.com/greengrass/v1/developerguide/docker-config-setup.html): Learn how to configure your AWS IoT Greengrass Docker container to run IDT tests for device qualification.
- [Optional: Configuring your device for ML qualification](https://docs.aws.amazon.com/greengrass/v1/developerguide/idt-ml-qualification.html): Learn how to configure your AWS IoT Greengrass core device to run IDT tests for machine learning (ML) qualification.
- [Configure IDT settings](https://docs.aws.amazon.com/greengrass/v1/developerguide/set-config.html): Describes the settings configuration that is required to run the AWS IoT Greengrass qualification suite.
- [Run the AWS IoT Greengrass qualification suite](https://docs.aws.amazon.com/greengrass/v1/developerguide/run-tests.html): Learn how to run IDT tests for device qualification.
- [Understanding results and logs](https://docs.aws.amazon.com/greengrass/v1/developerguide/results-logs.html): Learn how to view and interpret IDT tests for device qualification.

### [Use IDT to develop and run your own test suites](https://docs.aws.amazon.com/greengrass/v1/developerguide/idt-custom-tests.html)

Describes how to use AWS IoT Device Tester (IDT) to develop custom test suites for device validation.

- [Tutorial: Build and run the sample IDT test suite](https://docs.aws.amazon.com/greengrass/v1/developerguide/build-sample-suite.html): Learn how to build and run the sample test suite that is included in the AWS IoT Device Tester (IDT) download.
- [Tutorial: Develop a simple IDT test suite](https://docs.aws.amazon.com/greengrass/v1/developerguide/create-custom-tests.html): Learn how to use the test suite environment of IDT for AWS IoT Greengrass to develop a simple test suite.
- [Create IDT test suite configuration files](https://docs.aws.amazon.com/greengrass/v1/developerguide/idt-json-config.html): This section describes the formats in which you create JSON configuration files that you include when you write a custom test suite.
- [Configure the IDT state machine](https://docs.aws.amazon.com/greengrass/v1/developerguide/idt-state-machine.html): Describes the AWS IoT Device Tester state machine that determines the flow of your test suite.
- [Create IDT test case executables](https://docs.aws.amazon.com/greengrass/v1/developerguide/test-executables.html): Describe how to write a test case executable and understand how the test case executable interacts with IDT.
- [Use the IDT context](https://docs.aws.amazon.com/greengrass/v1/developerguide/idt-context.html): Describes the IDT context and how to use it to access data during test execution.
- [Configure settings for test runners](https://docs.aws.amazon.com/greengrass/v1/developerguide/set-config-custom.html): Describes the configuration information that test runners must provide to configure IDT and run custom test suites.
- [Debug and run custom test suites](https://docs.aws.amazon.com/greengrass/v1/developerguide/run-tests-custom.html): Describes how to run IDT in debug mode and lists the CLI commands that you can use to run a custom test suite.
- [Review IDT test results and logs](https://docs.aws.amazon.com/greengrass/v1/developerguide/idt-review-results-logs.html): View and interpret test results and logs generated by AWS IoT Device Tester (IDT).
- [IDT usage metrics](https://docs.aws.amazon.com/greengrass/v1/developerguide/idt-usage-metrics.html): Learn how to submit IDT usage metrics to AWS.
- [IDT for AWS IoT Greengrass troubleshooting](https://docs.aws.amazon.com/greengrass/v1/developerguide/idt-troubleshooting.html): Find troubleshooting information for IDT for AWS IoT Greengrass.
- [Support policy for AWS IoT Device Tester for AWS IoT Greengrass V1](https://docs.aws.amazon.com/greengrass/v1/developerguide/idt-support-policy.html): Describes the support policy for AWS IoT Device Tester for AWS IoT Greengrass V1.
