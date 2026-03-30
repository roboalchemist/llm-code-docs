# Source: https://docs.aws.amazon.com/iot/latest/developerguide/llms.txt

# AWS IoT Core Developer Guide

> AWS IoT provides secure, bi-directional communication between Internet-connected devices such as sensors, actuators, embedded micro-controllers, or smart appliances and the AWS Cloud. This enables you to collect telemetry data from multiple devices, and store and analyze the data. You can also create applications that enable your users to control these devices from their phones or tablets.

- [AWS IoT Device SDKs, Mobile SDKs, and AWS IoT Device Client](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sdks.html)
- [AWS IoT quotas](https://docs.aws.amazon.com/iot/latest/developerguide/limits-iot.html)
- [AWS IoT Core pricing](https://docs.aws.amazon.com/iot/latest/developerguide/iot-price.html)

## [What is AWS IoT?](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html)

- [What AWS IoT can do](https://docs.aws.amazon.com/iot/latest/developerguide/aws-iot-solutions.html): This topic describes some of the solutions that you might need that AWS IoT supports.
- [How AWS IoT works](https://docs.aws.amazon.com/iot/latest/developerguide/aws-iot-how-it-works.html): AWS IoT provides cloud services and device support that you can use to implement IoT solutions.
- [Learn more about AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/aws-iot-learn-more.html): This topic helps you get familiar with the world of AWS IoT.
- [What's new in the AWS IoT console](https://docs.aws.amazon.com/iot/latest/developerguide/whats-new-in-console.html): Describes the state of the AWS IoT console UI update.
- [Working with AWS SDKs](https://docs.aws.amazon.com/iot/latest/developerguide/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.


## [Get started tutorials](https://docs.aws.amazon.com/iot/latest/developerguide/iot-gs.html)

- [Set up AWS account](https://docs.aws.amazon.com/iot/latest/developerguide/setting-up.html): Before you use AWS IoT Core for the first time, complete the following tasks:
- [Interactive tutorial](https://docs.aws.amazon.com/iot/latest/developerguide/interactive-demo.html): The interactive tutorial shows the components of a simple IoT solution built on AWS IoT.

### [Quick connect tutorial](https://docs.aws.amazon.com/iot/latest/developerguide/iot-quick-start.html)

In this tutorial, you'll create your first thing object, connect a device to it, and watch it send MQTT messages.

- [Test connectivity](https://docs.aws.amazon.com/iot/latest/developerguide/iot-quick-start-test-connection.html): This topic describes how to test a device's connection with your account's device data endpoint, the endpoint that your IoT devices use to connect to AWS IoT.

### [Advanced connect tutorial](https://docs.aws.amazon.com/iot/latest/developerguide/iot-gs-first-thing.html)

In this tutorial, you'll install the software and create the AWS IoT resources necessary to connect a device to AWS IoT Core so that it can send and receive MQTT messages with AWS IoT Core.

- [Create AWS IoT resources](https://docs.aws.amazon.com/iot/latest/developerguide/create-iot-resources.html): In this tutorial, you'll create the AWS IoT resources that a device requires to connect to AWS IoT Core and exchange messages.

### [Configure your device](https://docs.aws.amazon.com/iot/latest/developerguide/configure-device.html)

This section describes how to configure your device to connect to AWS IoT Core.

- [Create a virtual device with Amazon EC2](https://docs.aws.amazon.com/iot/latest/developerguide/creating-a-virtual-thing.html): In this tutorial, you'll create an Amazon EC2 instance to serve as your virtual device in the cloud.
- [Use your Windows or Linux PC or Mac as an AWS IoT device](https://docs.aws.amazon.com/iot/latest/developerguide/using-laptop-as-device.html): In this tutorial, you'll configure a personal computer for use with AWS IoT.
- [Connect a Raspberry Pi or other device](https://docs.aws.amazon.com/iot/latest/developerguide/connecting-to-existing-device.html): In this section, we'll configure a Raspberry Pi for use with AWS IoT.
- [Troubleshoot problems with the sample application](https://docs.aws.amazon.com/iot/latest/developerguide/gs-device-troubleshoot.html): If you encounter an error when you try to run the sample app, here are some things to check.
- [View MQTT messages with the AWS IoT MQTT client](https://docs.aws.amazon.com/iot/latest/developerguide/view-mqtt-messages.html): This section describes how to use the AWS IoT MQTT test client in the AWS IoT console to watch the MQTT messages sent and received by AWS IoT.


## [AWS IoT tutorials](https://docs.aws.amazon.com/iot/latest/developerguide/iot-tutorials.html)

### [Building demos with the AWS IoT Device Client](https://docs.aws.amazon.com/iot/latest/developerguide/iot-tutorials-dc-intro.html)

The tutorials in this learning path walk you through the steps to develop demonstration software by using the AWS IoT Device Client.

### [Preparing to use IoT Device Client](https://docs.aws.amazon.com/iot/latest/developerguide/iot-dc-prepare-device.html)

Prepare your IoT devices to use the AWS IoT Device Client and run the demos.

- [Install and update operation system](https://docs.aws.amazon.com/iot/latest/developerguide/iot-dc-prepare-device-sys.html): Install the OS software and start the IoT device with the updated software.
- [Install and verify required software](https://docs.aws.amazon.com/iot/latest/developerguide/iot-dc-prepare-device-sw.html): The procedures in this section continue from the previous section to bring your Raspberry Pi's operating system up to date and install the software on the Raspberry Pi that will be used in the next section to build and install the AWS IoT Device Client.
- [Test IoT device and install certificates](https://docs.aws.amazon.com/iot/latest/developerguide/iot-dc-prepare-device-test.html): Test connectivity of your IoT device with the internet and download and install the Amazon Root CA certificates.

### [Installing and configuring IoT device client](https://docs.aws.amazon.com/iot/latest/developerguide/iot-dc-install-dc.html)

Installing and configuring the AWS IoT Device Client and run the demos.

- [Download and save IoT Device Client](https://docs.aws.amazon.com/iot/latest/developerguide/iot-dc-install-download.html): Download and build the AWS IoT Device Client for running the demos.
- [Provision your Raspberry Pi](https://docs.aws.amazon.com/iot/latest/developerguide/iot-dc-install-provision.html): Install microSD card and provision your Raspberry Pi in AWS IoT Core.
- [Configure Device Client and test connectivity](https://docs.aws.amazon.com/iot/latest/developerguide/iot-dc-install-configure.html): Create the config file and test connectivity with the IoT Device Client.

### [Communicate with Device client using MQTT](https://docs.aws.amazon.com/iot/latest/developerguide/iot-dc-testconn.html)

Establish MQTT message communication and subcribe to and publish MQTT messages with IoT Device Client.

- [Prepare Raspberry Pi for MQTT](https://docs.aws.amazon.com/iot/latest/developerguide/iot-dc-testconn-provision.html): Create certificates and provision your Rasperry Pi device for MQTT communication.
- [Publish messages with IoT Device Client](https://docs.aws.amazon.com/iot/latest/developerguide/iot-dc-testconn-publish.html): Learn how the AWS IoT Device Client can send default and custom MQTT messages.
- [Subscribe to messages with IoT Device Client](https://docs.aws.amazon.com/iot/latest/developerguide/iot-dc-testconn-subscribe.html): Learn how the AWS IoT Device Client can send default and custom MQTT messages.

### [Run IoT jobs with the Device Client](https://docs.aws.amazon.com/iot/latest/developerguide/iot-dc-runjobs.html)

Tutorial demo that demonstrates how to perform remote actions or IoT jobs with the Device Client.

- [Prepare Raspberry Pi for jobs](https://docs.aws.amazon.com/iot/latest/developerguide/iot-dc-runjobs-prepare.html): Tutorial demo that shows how to provision your Raspberry Pi and configure Device Client for jobs.
- [Create and run IoT job](https://docs.aws.amazon.com/iot/latest/developerguide/iot-dc-runjobs-prepare-define.html): AWS IoT Device Client tutorial to create the job document and run the IoT job on a single device.
- [Cleaning up](https://docs.aws.amazon.com/iot/latest/developerguide/iot-dc-cleanup.html): The procedures in this tutorial walk you through removing the files and resources you created while completing the tutorials in this learning path.

### [Building solutions with the AWS IoT Device SDKs](https://docs.aws.amazon.com/iot/latest/developerguide/iot-tutorials-sdk-intro.html)

The tutorials in this section help walk you through the steps to develop an IoT solution that can be deployed to a production environment using AWS IoT.

### [Connecting a device to AWS IoT Core by using the AWS IoT Device SDK](https://docs.aws.amazon.com/iot/latest/developerguide/sdk-tutorials.html)

Learn how to use the AWS IoT Device SDK to connect a device to AWS IoT Core.

- [Using the AWS IoT Device SDK for Embedded C](https://docs.aws.amazon.com/iot/latest/developerguide/iot-embedded-c-sdk.html): Learn about how to install and use the AWS IoT Device SDK for Embedded C.

### [Creating AWS IoT rules to route device data to other services](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules-tutorial.html)

Learn how to use AWS IoT rules to process messages from your things.

- [Republishing an MQTT message](https://docs.aws.amazon.com/iot/latest/developerguide/iot-repub-rule.html): This tutorial demonstrates how to create an AWS IoT rule that publishes an MQTT message when a specified MQTT message is received.
- [Sending an Amazon SNS notification](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sns-rule.html): This tutorial demonstrates how to create an AWS IoT rule that sends MQTT message data to an Amazon SNS topic so that it can be sent as an SMS text message.
- [Storing device data in a DynamoDB table](https://docs.aws.amazon.com/iot/latest/developerguide/iot-ddb-rule.html): This tutorial demonstrates how to create an AWS IoT rule that sends message data to a DynamoDB table.
- [Formatting a notification by using an AWS Lambda function](https://docs.aws.amazon.com/iot/latest/developerguide/iot-lambda-rule.html): This tutorial demonstrates how to send MQTT message data to an AWS Lambda action for formatting and sending to another AWS service.

### [Retaining device state while the device is offline with Device Shadows](https://docs.aws.amazon.com/iot/latest/developerguide/iot-shadows-tutorial.html)

Learn how to use AWS IoT Device Shadow to store and update state information of a thing.

- [Preparing your Raspberry Pi to run the shadow application](https://docs.aws.amazon.com/iot/latest/developerguide/create-resources-shadow.html): This tutorial demonstrates how to set up and configure a Raspberry Pi device and create the AWS IoT resources that a device requires to connect and exchange MQTT messages.
- [Provisioning your device in AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/shadow-provision-cloud.html): This section creates the AWS IoT Core resources that your tutorial will use.
- [Installing the Device SDK and running the sample application for Device Shadows](https://docs.aws.amazon.com/iot/latest/developerguide/lightbulb-shadow-application.html): This section shows how you can install the required software and the AWS IoT Device SDK for Python and run the shadow.py sample application to edit the Shadow document and control the shadow's state.
- [Interacting with Device Shadow using the sample app and the MQTT test client](https://docs.aws.amazon.com/iot/latest/developerguide/interact-lights-device-shadows.html): To interact with the shadow.py sample app, enter a value in the terminal for the desired value.
- [Creating a custom authorizer for AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/custom-auth-tutorial.html): This tutorial demonstrates the steps to create, validate, and use Custom Authentication by using the AWS CLI.

### [Monitoring soil moisture with AWS IoT and Raspberry Pi](https://docs.aws.amazon.com/iot/latest/developerguide/iot-moisture-tutorial.html)

This tutorial shows you how to use a Raspberry Pi, a moisture sensor, and AWS IoT to monitor the soil moisture level for a house plant or garden.

### [Setting up AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/iot-moisture-setup.html)

To complete this tutorial, you need to create the following resources.

- [Step 1: Create the AWS IoT policy](https://docs.aws.amazon.com/iot/latest/developerguide/iot-moisture-policy.html): Create an AWS IoT policy that allows your Raspberry Pi to connect and send messages to AWS IoT.
- [Step 2: Create the AWS IoT thing, certificate, and private key](https://docs.aws.amazon.com/iot/latest/developerguide/iot-moisture-create-thing.html): Create a thing in the AWS IoT registry to represent your Raspberry Pi.
- [Step 3: Create an Amazon SNS topic and subscription](https://docs.aws.amazon.com/iot/latest/developerguide/iot-moisture-create-sns-topic.html): Create an Amazon SNS topic and subscription.
- [Step 4: Create an AWS IoT rule to send an email](https://docs.aws.amazon.com/iot/latest/developerguide/iot-moisture-create-rule.html): An AWS IoT rule defines a query and one or more actions to take when a message is received from a device.
- [Setting up your Raspberry Pi and moisture sensor](https://docs.aws.amazon.com/iot/latest/developerguide/iot-moisture-raspi-setup.html)


## [Connect to AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/connect-to-iot.html)

- [Connect to AWS IoT Core service endpoints](https://docs.aws.amazon.com/iot/latest/developerguide/iot-connect-service.html): You can access the features of the AWS IoT CoreÂ -Â controlÂ plane by using the AWS CLI, the AWS SDK for your preferred language, or by calling the REST API directly.

### [Connect devices to AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/iot-connect-devices.html)

Devices connect to AWS IoT and other services through AWS IoT Core.

### [Device communication protocols](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html)

Use the AWS IoT MQTT protocol to publish and subscribe to messages and the HTTPS protocol to publish messages.

- [MQTT](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html): Use the AWS IoT MQTT messaging protocol for your devices.
- [HTTPS publish](https://docs.aws.amazon.com/iot/latest/developerguide/http.html): Learn how AWS IoT clients can publish messages by making requests to the REST API using HTTPS.

### [MQTT topics](https://docs.aws.amazon.com/iot/latest/developerguide/topics.html)

Learn how AWS IoT clients can identify messages that they publish by using topics.

- [MQTT message payload](https://docs.aws.amazon.com/iot/latest/developerguide/topicdata.html): The message payload that is sent in your MQTT messages isn't specified by AWS IoT, unless it's for one of the .
- [Reserved topics](https://docs.aws.amazon.com/iot/latest/developerguide/reserved-topics.html): Learn about the reserved topics for AWS IoT that you can't use to publish or subscribe.

### [Domain configurations](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-configurable.html)

Learn about configurable endpoints (domain configurations) and how they relate to custom domains for AWS IoT Core.

- [What is a domain configuration?](https://docs.aws.amazon.com/iot/latest/developerguide/iot-domain-configuration-what-is.html): In AWS IoT Core, a domain configuration refers to the setup and configuration of a domain (either AWS managed domain or customer managed domain) for your AWS IoT Core data endpoints.
- [Creating and configuring AWS managed domains](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-configurable-aws.html): Create and configure AWS managed domains for devices connecting to AWS IoT Core.
- [Creating and configuring customer managed domains](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-configurable-custom.html): Create and configure custom domains for AWS IoT Core.
- [Managing domain configurations](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-managing.html): Manage domain configurations in AWS IoT Core
- [Configuring TLS settings in domain configurations](https://docs.aws.amazon.com/iot/latest/developerguide/iot-endpoints-tls-config.html): AWS IoT Core provides predefined security polices for you to customize your Transport Layer Security (TLS) settings for TLS 1.2 and TLS 1.3 in domain configurations.
- [Server certificate configuration for OCSP stapling](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-cert-config.html): Use the AWS IoT Core server OCSP stapling.
- [Connect to AWS IoT FIPS endpoints](https://docs.aws.amazon.com/iot/latest/developerguide/iot-connect-fips.html): AWS IoT provides endpoints that support the Federal Information Processing Standard (FIPS) 140-2.


## [Manage devices](https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html)

### [Registry](https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html)

You use the AWS IoT console, AWS IoT API, or the AWS CLI to interact with the registry.

- [Create a thing](https://docs.aws.amazon.com/iot/latest/developerguide/create-thing.html): The following command shows how to use the AWS IoT CreateThing command from the CLI to create a thing.
- [List things](https://docs.aws.amazon.com/iot/latest/developerguide/list-things.html): You can use the ListThings command to list all things in your account:
- [Describe things](https://docs.aws.amazon.com/iot/latest/developerguide/search-things.html): You can use the DescribeThing command to display more detailed information about a thing:
- [Update a thing](https://docs.aws.amazon.com/iot/latest/developerguide/update-thing.html): You can use the UpdateThing command to update a thing.
- [Delete a thing](https://docs.aws.amazon.com/iot/latest/developerguide/delete-thing.html): You can use the DeleteThing command to delete a thing:
- [Attach a principal to a thing](https://docs.aws.amazon.com/iot/latest/developerguide/attach-thing-principal.html): A physical device can use a principal to communicate with AWS IoT.
- [List things associated with a principal](https://docs.aws.amazon.com/iot/latest/developerguide/list-principal-things.html): To list the things associated with the specified principal, run the list-principal-things command.
- [List principals associated with a thing](https://docs.aws.amazon.com/iot/latest/developerguide/list-thing-principals.html): To list the principals associated with the specified thing, run the list-thing-principals command.
- [List things associated with a principal V2](https://docs.aws.amazon.com/iot/latest/developerguide/list-principal-things-v2.html): To list the things associated with the specified certificate, along with the attachment type, run the list-principal-things-v2 command.
- [List principals associated with a thing V2](https://docs.aws.amazon.com/iot/latest/developerguide/list-thing-principals-v2.html): To list the certificates associated with the specified thing, along with the attachment type, run the list-thing-principals-V2 command.
- [Detach a principal from a thing](https://docs.aws.amazon.com/iot/latest/developerguide/detach-thing-principal.html): You can use the DetachThingPrincipal command to detach a certificate from a thing:

### [Thing types](https://docs.aws.amazon.com/iot/latest/developerguide/thing-types.html)

Thing types allow you to store description and configuration information that is common to all things associated with the same thing type.

- [Create a thing type](https://docs.aws.amazon.com/iot/latest/developerguide/create-thing-type.html): You can use the CreateThingType command to create a thing type:
- [List thing types](https://docs.aws.amazon.com/iot/latest/developerguide/list-thing-types.html): You can use the ListThingTypes command to list thing types:
- [Describe a thing type](https://docs.aws.amazon.com/iot/latest/developerguide/describe-thing-type.html): You can use the DescribeThingType command to get information about a thing type:
- [Associate a thing type with a thing](https://docs.aws.amazon.com/iot/latest/developerguide/associate-thing-type.html): You can use the CreateThing command to specify a thing type when you create a thing:
- [Update a thing type](https://docs.aws.amazon.com/iot/latest/developerguide/update-thing-type.html): You can use the UpdateThingType command to update a thing type when you create a thing:
- [Deprecate a thing type](https://docs.aws.amazon.com/iot/latest/developerguide/deprecate-thing-type.html): Thing types are immutable.
- [Delete a thing type](https://docs.aws.amazon.com/iot/latest/developerguide/delete-thing-types.html): You can delete thing types only after they have been deprecated.
- [Static thing groups](https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html): Static thing groups allow you to manage several things at once by categorizing them into groups.
- [Dynamic thing groups](https://docs.aws.amazon.com/iot/latest/developerguide/dynamic-thing-groups.html): Dynamic thing groups are created from specific search queries in the registry.
- [Associate thing to connection](https://docs.aws.amazon.com/iot/latest/developerguide/exclusive-thing.html): Learn about the AWS IoT Core feature that lets you associate an AWS IoT thing with an MQTT client ID exclusively.
- [Add propagating attributes](https://docs.aws.amazon.com/iot/latest/developerguide/thing-types-propagating-attributes.html): In AWS IoT Core, you can enrich MQTT messages from devices by adding propagating attributes, which are contextual metadata from thing attributes or connection details.


## [Tag resources](https://docs.aws.amazon.com/iot/latest/developerguide/tagging-iot.html)

- [Tag with IAM policies](https://docs.aws.amazon.com/iot/latest/developerguide/tagging-iot-iam.html): You can apply tag-based resource-level permissions in the IAM policies you use for AWS IoT API actions.
- [Billing groups](https://docs.aws.amazon.com/iot/latest/developerguide/tagging-iot-billing-groups.html): AWS IoT doesn't allow you to directly apply tags to individual things, but it does allow you to place things in billing groups and to apply tags to these.


## [Security](https://docs.aws.amazon.com/iot/latest/developerguide/security.html)

- [Security in AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/iot-security.html): Each connected device or client must have a credential to interact with AWS IoT.

### [Authentication](https://docs.aws.amazon.com/iot/latest/developerguide/authentication.html)

Authentication is a mechanism where you verify the identity of a client or a server.

- [Server authentication](https://docs.aws.amazon.com/iot/latest/developerguide/server-authentication.html): Learn how to authenticate the server with an X.509 certificate when you connect to AWS IoT Core.

### [Client authentication](https://docs.aws.amazon.com/iot/latest/developerguide/client-authentication.html)

AWS IoT supports three types of identity principals for device or client authentication:

### [X.509 client certificates](https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html)

X.509 certificates provide AWS IoT with the ability to authenticate client and device connections.

- [Create AWS IoT client certificates](https://docs.aws.amazon.com/iot/latest/developerguide/device-certs-create.html): AWS IoT provides client certificates that are signed by the Amazon Root certificate authority (CA).

### [Create your own client certificates](https://docs.aws.amazon.com/iot/latest/developerguide/device-certs-your-own.html)

AWS IoT supports client certificates signed by any root or intermediate certificate authorities (CA).

- [Manage your CA certificates](https://docs.aws.amazon.com/iot/latest/developerguide/manage-your-CA-certs.html): This section describes common tasks for managing your own certificate authority (CA) certificates.
- [Create a client certificate using your CA certificate](https://docs.aws.amazon.com/iot/latest/developerguide/create-device-cert.html): You can use your own certificate authority (CA) to create client certificates.

### [Register a client certificate](https://docs.aws.amazon.com/iot/latest/developerguide/register-device-cert.html)

Client certificates must be registered with AWS IoT to enable communications between the client and AWS IoT.

- [Register a client certificate manually](https://docs.aws.amazon.com/iot/latest/developerguide/manual-cert-registration.html): You can register a client certificate manually by using the AWS IoT console and AWS CLI.
- [Register a client certificate when the client connects to AWS IoT just-in-time registration (JITR)](https://docs.aws.amazon.com/iot/latest/developerguide/auto-register-device-cert.html): You can configure a CA certificate to enable client certificates it has signed to register with AWS IoT automatically the first time the client connects to AWS IoT.

### [Manage client certificates](https://docs.aws.amazon.com/iot/latest/developerguide/manage-device-cert.html)

AWS IoT provides capabilities for you to manage client certificates.

- [Activate or deactivate a client certificate](https://docs.aws.amazon.com/iot/latest/developerguide/activate-or-deactivate-device-cert.html): AWS IoT verifies that a client certificate is active when it authenticates a connection.
- [Attach a thing or policy to a client certificate](https://docs.aws.amazon.com/iot/latest/developerguide/attach-to-cert.html): When you create and register a certificate separate from an AWS IoT thing, it will not have any policies that authorize any AWS IoT operations, nor will it be associated with any AWS IoT thing object.
- [Revoke a client certificate](https://docs.aws.amazon.com/iot/latest/developerguide/revoke-ca-cert.html): If you detect suspicious activity on a registered client certificate, you can revoke it so that it can't be used again.
- [Transfer a certificate to another account](https://docs.aws.amazon.com/iot/latest/developerguide/transfer-cert.html): X.509 certificates that belong to one AWS account can be transferred to another AWS account.
- [Custom client certificate validation](https://docs.aws.amazon.com/iot/latest/developerguide/customize-client-auth.html): AWS IoT Core supports custom client certificate validation for X.509 client certificates, which enhances client authentication management.
- [IAM users, groups, and roles](https://docs.aws.amazon.com/iot/latest/developerguide/iam-users-groups-roles.html): IAM users, groups, and roles are the standard mechanisms for managing identity and authentication in AWS.
- [Amazon Cognito identities](https://docs.aws.amazon.com/iot/latest/developerguide/cognito-identities.html): Amazon Cognito Identity enables you to create temporary, limited privilege AWS credentials for use in mobile and web applications.

### [Custom authentication and authorization](https://docs.aws.amazon.com/iot/latest/developerguide/custom-authentication.html)

Describes the AWS IoT Core custom authentication feature and how to use it.

- [Understanding the custom authentication workflow](https://docs.aws.amazon.com/iot/latest/developerguide/custom-authorizer.html): Custom authentication enables you to define how to authenticate and authorize clients by using authorizer resources.Â  Each authorizer contains a reference to a customer-managed Lambda function, an optional public key for validating device credentials, and additional configuration information.Â The following diagram illustrates the authorization workflow for custom authentication in AWS IoT Core.

### [Creating and managing custom authorizers (CLI)](https://docs.aws.amazon.com/iot/latest/developerguide/config-custom-auth.html)

AWS IoT Core implements custom authentication and authorization schemes by using custom authorizers.

- [Defining your Lambda function](https://docs.aws.amazon.com/iot/latest/developerguide/custom-auth-lambda.html): When AWS IoT Core invokes your authorizer, it triggers the associated Lambda associated with the authorizer with an event that contains the following JSON object.
- [Creating an authorizer](https://docs.aws.amazon.com/iot/latest/developerguide/custom-auth-create-authorizer.html): You can create an authorizer by using the CreateAuthorizer API.Â The following example describes the command.
- [Authorizing AWS IoT to invoke your Lambda function](https://docs.aws.amazon.com/iot/latest/developerguide/custom-auth-authorize.html): In this section, you'll grant the permission of the custom authorizer resource that you just created to run the Lambda function.
- [Testing your authorizers](https://docs.aws.amazon.com/iot/latest/developerguide/custom-auth-testing.html): You can use the TestInvokeAuthorizer API to test the invocation and return values of your authorizer.Â This API enables you to specify protocol metadata and test the signature validation in your authorizer.
- [Managing custom authorizers](https://docs.aws.amazon.com/iot/latest/developerguide/custom-auth-manage.html): You can manage your authorizers by using the following APIs.
- [Custom authentication with X.509 client certificates](https://docs.aws.amazon.com/iot/latest/developerguide/custom-auth-509cert.html): When connecting devices to AWS IoT Core, you have multiple authentication types available.
- [Connecting to AWS IoT Core by using custom authentication](https://docs.aws.amazon.com/iot/latest/developerguide/custom-auth.html): Devices can connect to AWS IoT Core by using custom authentication with any protocol that AWS IoT Core supports for device messaging.
- [Troubleshooting your authorizers](https://docs.aws.amazon.com/iot/latest/developerguide/custom-auth-troubleshooting.html): This topic walks through common issues that can cause problems in custom authentication workflows and steps for resolving them.

### [Authorization](https://docs.aws.amazon.com/iot/latest/developerguide/iot-authorization.html)

Authorization is the process of granting permissions to an authenticated identity.

### [AWS IoT Core policies](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html)

AWS IoT Core policies are JSON documents.

- [AWS IoT Core policy actions](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policy-actions.html): The following policy actions are defined by AWS IoT Core:
- [AWS IoT Core action resources](https://docs.aws.amazon.com/iot/latest/developerguide/iot-action-resources.html): To specify a resource for an AWS IoT Core policy action, use the Amazon Resource Name (ARN) of the resource.

### [AWS IoT Core policy variables](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policy-variables.html)

AWS IoT Core defines policy variables that can be used in AWS IoT Core policies in the Resource or Condition block.

- [Basic AWS IoT Core policy variables](https://docs.aws.amazon.com/iot/latest/developerguide/basic-policy-variables.html): AWS IoT Core defines the following basic policy variables:
- [Thing policy variables](https://docs.aws.amazon.com/iot/latest/developerguide/thing-policy-variables.html): Thing policy variables allow you to write AWS IoT Core policies that grant or deny permissions based on thing properties like thing names, thing types, and thing attribute values.

### [X.509 Certificate AWS IoT Core policy variables](https://docs.aws.amazon.com/iot/latest/developerguide/cert-policy-variables.html)

X.509 certificate policy variables assist with writing AWS IoT Core policies.

- [Using X.509 certificate policy variables](https://docs.aws.amazon.com/iot/latest/developerguide/use-policy-variables.html): This topic provides details of how to use certificate policy variables.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/iot/latest/developerguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.

### [AWS IoT Core policy examples](https://docs.aws.amazon.com/iot/latest/developerguide/example-iot-policies.html)

See the following example AWS IoT Core policies to allow or deny specific actions.

- [Connect policy examples](https://docs.aws.amazon.com/iot/latest/developerguide/connect-policy.html): The following policy denies permission to client IDs client1 and client2 to connect to AWS IoT Core, while allowing devices to connect using a client ID.
- [Publish/Subscribe policy examples](https://docs.aws.amazon.com/iot/latest/developerguide/pub-sub-policy.html): The policy you use depends on how you're connecting to AWS IoT Core.
- [Connect and publish policy examples](https://docs.aws.amazon.com/iot/latest/developerguide/connect-and-pub.html): For devices registered as things in the AWS IoT Core registry, the following policy grants permission to connect to AWS IoT Core with a client ID that matches the thing name and restricts the device to publishing on a client-ID or thing name-specific MQTT topic.
- [Retained message policy examples](https://docs.aws.amazon.com/iot/latest/developerguide/retained-message-policy-examples.html): Using retained messages requires specific policies.
- [Certificate policy examples](https://docs.aws.amazon.com/iot/latest/developerguide/certificate-policy-examples.html): For devices registered in AWS IoT Core registry, the following policy grants permission to connect to AWS IoT Core with a client ID that matches a thing name, and to publish to a topic whose name is equal to the certificateId of the certificate the device used to authenticate itself:
- [Thing policy examples](https://docs.aws.amazon.com/iot/latest/developerguide/thing-policy-examples.html): The following policy allows a device to connect if the certificate used to authenticate with AWS IoT Core is attached to the thing for which the policy is being evaluated:
- [Basic job policy example](https://docs.aws.amazon.com/iot/latest/developerguide/basic-jobs-example.html): This sample shows the policy statments required for a job target that's a single device to receive a job request and communicate job execution status with AWS IoT.
- [Authorization with Amazon Cognito identities](https://docs.aws.amazon.com/iot/latest/developerguide/cog-iot-policies.html): There are two types of Amazon Cognito identities: unauthenticated and authenticated.
- [Authorizing direct calls to AWS services using AWS IoT Core credential provider](https://docs.aws.amazon.com/iot/latest/developerguide/authorizing-direct-aws.html): Devices can use X.509 certificates to connect to AWS IoT Core using TLS mutual authentication protocols.
- [Cross account access with IAM](https://docs.aws.amazon.com/iot/latest/developerguide/cross-account-access.html): AWS IoT Core allows you to enable a principal to publish or subscribe to a topic that is defined in an AWS account not owned by the principal.

### [Data protection](https://docs.aws.amazon.com/iot/latest/developerguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in AWS IoT.

- [Transport security in AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/transport-security.html): TLS (Transport Layer Security) is a cryptographic protocol that is designed for secure communication over a computer network.

### [Data encryption](https://docs.aws.amazon.com/iot/latest/developerguide/data-encryption.html)

Learn how AWS IoT uses data encryption to keep your data safe.

- [Data encryption at rest in AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/encryption-at-rest.html): Learn how AWS IoT Core encrypts data at rest.

### [Identity and access management](https://docs.aws.amazon.com/iot/latest/developerguide/security-iam.html)

How to authenticate requests and manage access to your AWS IoT resources.

- [How AWS IoT works with IAM](https://docs.aws.amazon.com/iot/latest/developerguide/security_iam_service-with-iam.html): Before you use IAM to manage access to AWS IoT, you should understand which IAM features are available to use with AWS IoT.
- [Identity-based policy examples](https://docs.aws.amazon.com/iot/latest/developerguide/security_iam_id-based-policy-examples.html): By default, IAM users and roles don't have permission to create or modify AWS IoT resources.
- [AWS managed policies](https://docs.aws.amazon.com/iot/latest/developerguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS IoT and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/iot/latest/developerguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS IoT and IAM.
- [Logging and Monitoring](https://docs.aws.amazon.com/iot/latest/developerguide/security-logging.html): Monitoring is an important part of maintaining the reliability, availability, and performance of AWS IoT and your AWS solutions.
- [Compliance validation](https://docs.aws.amazon.com/iot/latest/developerguide/compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/iot/latest/developerguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS IoT Core features for data resiliency.

### [Using AWS IoT Core with VPC endpoints](https://docs.aws.amazon.com/iot/latest/developerguide/IoTCore-VPC.html)

You can connect and use AWS IoT Core with Amazon VPC endpoints.

- [Using AWS IoT Device Management with VPC endpoints](https://docs.aws.amazon.com/iot/latest/developerguide/IoTCore-ST-VPC.html): You can connect and use AWS IoT Device Management secure tunneling with Amazon VPC endpoints.
- [Infrastructure security](https://docs.aws.amazon.com/iot/latest/developerguide/infrastructure-security.html): Learn how AWS IoT isolates service traffic.
- [Security monitoring](https://docs.aws.amazon.com/iot/latest/developerguide/security-monitoring.html): Use AWS IoT Core to monitor for vulnerabilities with your production fleets or devices.
- [Security best practices](https://docs.aws.amazon.com/iot/latest/developerguide/security-best-practices.html): This section contains information about security best practices for AWS IoT Core.


## [Monitor AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/monitoring_overview.html)

- [Configure AWS IoT logging](https://docs.aws.amazon.com/iot/latest/developerguide/configure-logging.html): Configure AWS tools to monitor AWS IoT.

### [Monitor AWS IoT alarms and metrics using Amazon CloudWatch](https://docs.aws.amazon.com/iot/latest/developerguide/monitoring-cloudwatch.html)

You can monitor AWS IoT using CloudWatch, which collects and processes raw data from AWS IoT into readable, near real-time metrics.

- [Create CloudWatch alarms](https://docs.aws.amazon.com/iot/latest/developerguide/creating_alarms.html): You can create a CloudWatch alarm that sends an Amazon SNS message when the alarm changes state.
- [Metrics and dimensions](https://docs.aws.amazon.com/iot/latest/developerguide/metrics_dimensions.html): When you interact with AWS IoT, the service sends metrics and dimensions to CloudWatch every minute.

### [Monitor AWS IoT using CloudWatch Logs](https://docs.aws.amazon.com/iot/latest/developerguide/cloud-watch-logs.html)

When AWS IoT logging is enabled, AWS IoT sends progress events about each message as it passes from your devices through the message broker and rules engine.

- [CloudWatch Logs AWS IoT log entries](https://docs.aws.amazon.com/iot/latest/developerguide/cwl-format.html): Each component of AWS IoT generates its own log entries.

### [Upload device-side logs to Amazon CloudWatch](https://docs.aws.amazon.com/iot/latest/developerguide/upload-device-logs-to-cloudwatch.html)

Use the AWS IoT CloudWatch Logs rule action to upload device-side logs to Amazon CloudWatch.

- [Uploading device-side logs by using AWS IoT rules](https://docs.aws.amazon.com/iot/latest/developerguide/uploading-logs-rules-action-procedure.html): Complete the following procedure to upload device-side logs to Amazon CloudWatch using the AWS IoT CloudWatch Logs rule action.
- [Log AWS IoT API calls](https://docs.aws.amazon.com/iot/latest/developerguide/iot-using-cloudtrail.html): AWS IoT is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in AWS IoT.


## [Rules](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html)

- [Grant access](https://docs.aws.amazon.com/iot/latest/developerguide/iot-create-role.html): Create an IAM role to grant AWS IoT access to your AWS resources.
- [Pass role permissions](https://docs.aws.amazon.com/iot/latest/developerguide/pass-role.html): To grant permission to access resources, pass an IAM role to the AWS IoT rules engine.
- [Create a rule](https://docs.aws.amazon.com/iot/latest/developerguide/iot-create-rule.html): Create an AWS IoT rule so that you can route data from your connected things.
- [Manage a rule](https://docs.aws.amazon.com/iot/latest/developerguide/iot-managae-rule.html): Manage an AWS IoT rule that you created.

### [AWS IoT rule actions](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rule-actions.html)

Use AWS IoT rules actions to specify what to do when a rule is invoked.

### [Apache Kafka](https://docs.aws.amazon.com/iot/latest/developerguide/apache-kafka-rule-action.html)

Use the Apache Kafka rule action to send messages from your devices directly to your Amazon Managed Streaming for Apache Kafka (Amazon MSK), Apache Kafka clusters managed by third-party providers such as Confluent Cloud, or self-managed Apache Kafka clusters for data analysis and visualization.

- [Apache Kafka Virtual Private Cloud (VPC) destinations](https://docs.aws.amazon.com/iot/latest/developerguide/kafka-vpc-destination.html): The rule action sends data to an Apache Kafka cluster in an Amazon Virtual Private Cloud (Amazon VPC).
- [CloudWatch alarms](https://docs.aws.amazon.com/iot/latest/developerguide/cloudwatch-alarms-rule-action.html): Use the CloudWatch alarms rule action to change the state of an Amazon CloudWatch alarm from AWS IoT.
- [CloudWatch Logs](https://docs.aws.amazon.com/iot/latest/developerguide/cloudwatch-logs-rule-action.html): Use the CloudWatch Logs rule action to send an MQTT message from AWS IoT to Amazon CloudWatch Logs.
- [CloudWatch metrics](https://docs.aws.amazon.com/iot/latest/developerguide/cloudwatch-metrics-rule-action.html): Use the CloudWatch metrics rule action to capture an Amazon CloudWatch metric from AWS IoT.
- [DynamoDB](https://docs.aws.amazon.com/iot/latest/developerguide/dynamodb-rule-action.html): Use the DynamoDB rule action to write an MQTT message from AWS IoT to an Amazon DynamoDB table.
- [DynamoDBv2](https://docs.aws.amazon.com/iot/latest/developerguide/dynamodb-v2-rule-action.html): Use the DynamoDBv2 rule action to write an MQTT message from AWS IoT into multiple columns of an Amazon DynamoDB table.
- [Elasticsearch](https://docs.aws.amazon.com/iot/latest/developerguide/elasticsearch-rule-action.html): Use the Elasticsearch action to send an MQTT message from AWS IoT to an Amazon OpenSearch Service domain.

### [HTTP](https://docs.aws.amazon.com/iot/latest/developerguide/https-rule-action.html)

Use the HTTP rule action to send an MQTT message from AWS IoT to your web application or service at an HTTPS endpoint.

- [Batching HTTP action messages](https://docs.aws.amazon.com/iot/latest/developerguide/http_batching.html): Learn how to use batching to send multiple HTTP action messages from AWS IoT Core Rules Engine in a single request.
- [HTTP action destinations](https://docs.aws.amazon.com/iot/latest/developerguide/http-action-destination.html): Use HTTP action destinations to specify where the AWS IoT rules engine can route data.
- [AWS IoT Events](https://docs.aws.amazon.com/iot/latest/developerguide/iotevents-rule-action.html): Use the AWS IoT Events rule action to send an MQTT message from AWS IoT to an AWS IoT Events input.
- [AWS IoT SiteWise](https://docs.aws.amazon.com/iot/latest/developerguide/iotsitewise-rule-action.html): Use the AWS IoT SiteWise rule action to send an MQTT message from AWS IoT to asset properties in AWS IoT SiteWise.
- [Firehose](https://docs.aws.amazon.com/iot/latest/developerguide/kinesis-firehose-rule-action.html): Use the Firehose action to send an MQTT message from AWS IoT to an Amazon Data Firehose stream.
- [Kinesis Data Streams](https://docs.aws.amazon.com/iot/latest/developerguide/kinesis-rule-action.html): Use the Kinesis Data Streams rule action to send an MQTT message from AWS IoT to an Amazon Kinesis Data Streams stream.
- [Lambda](https://docs.aws.amazon.com/iot/latest/developerguide/lambda-rule-action.html): Use the Lambda rule action to send an MQTT message from AWS IoT to an AWS Lambda function.
- [Location](https://docs.aws.amazon.com/iot/latest/developerguide/location-rule-action.html): The Amazon Location rule action routes your geographical location data to Amazon Location Service.
- [OpenSearch](https://docs.aws.amazon.com/iot/latest/developerguide/opensearch-rule-action.html): Use the OpenSearch action to send an MQTT message from AWS IoT to an Amazon OpenSearch Service domain.
- [Republish](https://docs.aws.amazon.com/iot/latest/developerguide/republish-rule-action.html): Use the republish action to republish an MQTT message from AWS IoT to another MQTT topic.
- [S3](https://docs.aws.amazon.com/iot/latest/developerguide/s3-rule-action.html): Use the S3 action to send an MQTT message from AWS IoT to an Amazon Simple Storage Service bucket.
- [Salesforce IoT](https://docs.aws.amazon.com/iot/latest/developerguide/salesforce-iot-rule-action.html): Use the Salesforce rule action to send an MQTT message from AWS IoT to a Salesforce IoT input stream.
- [SNS](https://docs.aws.amazon.com/iot/latest/developerguide/sns-rule-action.html): Use the SNS rule action to send an MQTT message from AWS IoT as an Amazon Simple Notification Service push notification.
- [SQS](https://docs.aws.amazon.com/iot/latest/developerguide/sqs-rule-action.html): Use the SQS rule action to send an MQTT message from AWS IoT to an Amazon Simple Queue Service queue.
- [Step Functions](https://docs.aws.amazon.com/iot/latest/developerguide/stepfunctions-rule-action.html): Use the Step Functions rule action to start an AWS Step Functions state machine.
- [Timestream](https://docs.aws.amazon.com/iot/latest/developerguide/timestream-rule-action.html): Use the Timestream rule action to write attributes of an MQTT message from AWS IoT into an Amazon Timestream database table.
- [Access cross-account resources](https://docs.aws.amazon.com/iot/latest/developerguide/accessing-cross-account-resources-using-rules.html): Learn how to configure AWS IoT rules to activate cross-account access to AWS resources.
- [Error handling (error action)](https://docs.aws.amazon.com/iot/latest/developerguide/rule-error-handling.html): Learn how to handle errors that occur while working with your AWS IoT rules.
- [Basic Ingest](https://docs.aws.amazon.com/iot/latest/developerguide/iot-basic-ingest.html): Learn how to use Basic Ingest to send data to an AWS IoT rule without incurring messaging costs.

### [AWS IoT SQL reference](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-reference.html)

See the following SQL reference for creating your AWS IoT rules.

- [SELECT clause](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-select.html): Use the SELECT cause to extract information from incoming MQTT messages in AWS IoT.
- [FROM clause](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-from.html): Use the FROM clause to subscribe your AWS IoT rule to a topic or topic filter.
- [SET clause](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-set.html): Use the SET clause to define variables that can be reused throughout your AWS IoT SQL statement.
- [WHERE clause](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-where.html): Use the WHERE clause to determine if actions specified by your AWS IoT rule are carried out.
- [Data types](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-data-types.html): See the following data types that AWS IoT rules support.
- [Operators](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-operators.html): You can use the following operators when you create your AWS IoT rules.
- [Functions](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-functions.html): Use the following functions to create your SQL expressions for AWS IoT rules.
- [Literals](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-literals.html): Specify literal objects in your AWS IoT SQL rule to pass information.
- [Case statements](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-case.html): Use case statements for your AWS IoT rules for branching execution.
- [JSON extensions](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-json.html): Use JSON extensions for your rules in AWS IoT.
- [Substitution templates](https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html): Use a substitution template to augment the JSON data returned when a rule triggers and AWS IoT performs an action.
- [Nested object queries](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-nested-queries.html): You can use intra-object queries to retrieve data within arrays and inner objects for AWS IoT.
- [Binary payloads](https://docs.aws.amazon.com/iot/latest/developerguide/binary-payloads.html): Use binary payloads to handle data for AWS IoT messages.
- [SQL versions](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rule-sql-version.html): Use the following SQL versions for using AWS IoT rule engine.


## [Shadows](https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-shadows.html)

- [Using shadows in devices](https://docs.aws.amazon.com/iot/latest/developerguide/device-shadow-comms-device.html): This section describes device communications with shadows using MQTT messages, the preferred method for devices to communicate with the AWS IoT Device Shadow service.
- [Using shadows in apps and services](https://docs.aws.amazon.com/iot/latest/developerguide/device-shadow-comms-app.html): This section describes how an app or service interacts with the AWS IoT Device Shadow service.
- [Simulating Device Shadow service communications](https://docs.aws.amazon.com/iot/latest/developerguide/using-device-shadows.html): Demonstrates how devices and apps use the Device Shadow service to retrieve and update state data.
- [Interacting with shadows](https://docs.aws.amazon.com/iot/latest/developerguide/device-shadow-data-flow.html): This topic describes the messages associated with each of the three methods that AWS IoT provides for working with shadows.
- [Device Shadow REST API](https://docs.aws.amazon.com/iot/latest/developerguide/device-shadow-rest-api.html): Describes the REST API for working with the Device Shadow service in AWS IoT.
- [Device Shadow MQTT topics](https://docs.aws.amazon.com/iot/latest/developerguide/device-shadow-mqtt.html): Describes the publish/subscribe messages used with MQTT to interact with the Device Shadow service in AWS IoT.
- [Device Shadow service documents](https://docs.aws.amazon.com/iot/latest/developerguide/device-shadow-document.html): Describes the state documents used by the Device Shadow service in AWS IoT.
- [Device Shadow error messages](https://docs.aws.amazon.com/iot/latest/developerguide/device-shadow-error-messages.html): Describes the error messages provided by the Device Shadow service in AWS IoT.


## [Software Package Catalog](https://docs.aws.amazon.com/iot/latest/developerguide/software-package-catalog.html)

- [Preparing to use Software Package Catalog](https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html): The following section provides an overview of the package version lifecycle and information for using AWS IoT Device Management Software Package Catalog.
- [Preparing security](https://docs.aws.amazon.com/iot/latest/developerguide/preparing-security.html): This section discusses the main security requirements for AWS IoT Device Management Software Package Catalog.
- [Preparing fleet indexing](https://docs.aws.amazon.com/iot/latest/developerguide/preparing-fleet-indexing.html): With AWS IoT fleet indexing, you can search and aggregate data by using the reserved named shadow ($package).
- [Preparing AWS IoT Jobs](https://docs.aws.amazon.com/iot/latest/developerguide/preparing-jobs-for-service-package-catalog.html): AWS IoT Device Management Software Package Catalog extends AWS IoT Jobs through substitution parameters, and integration with AWS IoT fleet indexing, dynamic thing groups, and the AWS IoT thingâs reserved named shadow.

### [Getting started](https://docs.aws.amazon.com/iot/latest/developerguide/getting-started-with-software-package-catalog.html)

You can build and maintain the AWS IoT Device Management Software Package Catalog through the AWS Management Console, AWS IoT Core API operations, and AWS Command Line Interface (AWS CLI).

- [Creating a package and version](https://docs.aws.amazon.com/iot/latest/developerguide/creating-package-and-version.html): You can use the following steps to create a package and an initial version thing through the AWS Management Console.
- [Deploying a package version](https://docs.aws.amazon.com/iot/latest/developerguide/deploying-package-version.html): You can use the following steps to deploy a package version through the AWS Management Console.
- [Associating a package version](https://docs.aws.amazon.com/iot/latest/developerguide/associating-package-version.html): After you install software on your device, you can associate a package version to an AWS IoT thingâs reserved named shadow.


## [Jobs](https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs.html)

- [What is a remote operation?](https://docs.aws.amazon.com/iot/latest/developerguide/jobs-what-is-remote-operation.html)

### [What is AWS IoT Jobs?](https://docs.aws.amazon.com/iot/latest/developerguide/jobs-what-is.html)

Use AWS IoT Jobs to define a set of remote operations that can be sent to and run on one or more devices connected to AWS IoT.

- [Jobs key concepts](https://docs.aws.amazon.com/iot/latest/developerguide/key-concepts-jobs.html): The following concepts provide details about AWS IoT Jobs and how to create and deploy jobs to run remote operations on your devices.
- [Jobs and job execution states](https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs-lifecycle.html): The following sections describe the lifecycle of an AWS IoT job and the lifecycle of a job execution.

### [Managing jobs](https://docs.aws.amazon.com/iot/latest/developerguide/create-manage-jobs.html)

Use jobs to notify devices of a software or firmware update.

- [Create and manage jobs using the console](https://docs.aws.amazon.com/iot/latest/developerguide/manage-job-console.html): This section describes how you can create and manage jobs from the AWS IoT console.
- [Create and manage jobs using the CLI](https://docs.aws.amazon.com/iot/latest/developerguide/manage-job-cli.html): This section describes how to create and manage jobs.

### [Job templates](https://docs.aws.amazon.com/iot/latest/developerguide/job-templates.html)

Use job templates to preconfigure jobs that you can deploy to multiple sets of target devices.

### [Use AWS managed templates](https://docs.aws.amazon.com/iot/latest/developerguide/job-templates-managed.html)

Use AWS managed templates to create AWS IoT Jobs to perform common remote operations.

- [Create a job from AWS managed templates using the console](https://docs.aws.amazon.com/iot/latest/developerguide/job-template-manage-console-create.html): Use the AWS Management Console to get information about AWS managed templates and create a job by using these templates.
- [Create a job from AWS managed templates using the CLI](https://docs.aws.amazon.com/iot/latest/developerguide/job-template-manage-cli-create.html): Use the AWS CLI to get information about AWS managed templates and create a job by using these templates.

### [Create custom job templates](https://docs.aws.amazon.com/iot/latest/developerguide/job-templates-create.html)

You can create job templates by using the AWS CLI and the AWS IoT console.

- [Create custom job templates using the console](https://docs.aws.amazon.com/iot/latest/developerguide/job-templates-console.html): This topic explains how to create, delete, and view details about job templates by using the AWS IoT console.
- [Create custom job templates using the CLI](https://docs.aws.amazon.com/iot/latest/developerguide/job-templates-cli.html): This topic explains how to create, delete, and retrieve details about job templates by using the AWS CLI.

### [Job configurations](https://docs.aws.amazon.com/iot/latest/developerguide/jobs-configurations.html)

You can have the following additional configurations for each job that you deploy to the specified targets.

- [How job configurations work](https://docs.aws.amazon.com/iot/latest/developerguide/jobs-configurations-details.html): You use the rollout and abort configurations when you're deploying a job, and the timeout and retry configurations for job execution.

### [Specify additional configurations](https://docs.aws.amazon.com/iot/latest/developerguide/jobs-configurations-specify.html)

When you create a job or job template, you can specify these additional configurations.

- [Specify job configurations by using the console](https://docs.aws.amazon.com/iot/latest/developerguide/job-configurations-console.html): You can add the different configurations for your job by using the AWS IoT console.
- [Specify job configurations using the API](https://docs.aws.amazon.com/iot/latest/developerguide/job-configurations-api.html): You can use the CreateJob or the CreateJobTemplate API to specify the different job configurations.

### [Devices and jobs](https://docs.aws.amazon.com/iot/latest/developerguide/jobs-devices.html)

Devices can communicate with AWS IoT Jobs using MQTT, HTTP Signature Version 4, or HTTP TLS.

- [Device workflow](https://docs.aws.amazon.com/iot/latest/developerguide/jobs-workflow-device-online.html): A device can handle jobs that it runs using either of the following ways.
- [Jobs workflow](https://docs.aws.amazon.com/iot/latest/developerguide/jobs-workflow-jobs-online.html): The following shows the different steps in the jobs workflow from starting a new job to reporting the completion status of a job execution.
- [Jobs notifications](https://docs.aws.amazon.com/iot/latest/developerguide/jobs-comm-notifications.html): The AWS IoT Jobs service publishes MQTT messages to reserved topics when jobs are pending or when the first job execution in the list changes.

### [AWS IoT jobs API operations](https://docs.aws.amazon.com/iot/latest/developerguide/jobs-api.html)

AWS IoT Jobs API can be used for either of the following categories:

- [Jobs management and control API and data types](https://docs.aws.amazon.com/iot/latest/developerguide/jobs-management-control-api.html): The following commands are available for Job management and control in the CLI and over the HTTPS protocol.

### [Jobs device MQTT and HTTPS API operations and data types](https://docs.aws.amazon.com/iot/latest/developerguide/jobs-mqtt-https-api.html)

The following commands are available over the MQTT and HTTPS protocols.

- [Jobs device MQTT API operations](https://docs.aws.amazon.com/iot/latest/developerguide/jobs-mqtt-api.html)
- [Jobs device HTTP API](https://docs.aws.amazon.com/iot/latest/developerguide/jobs-http-device-api.html): Devices can communicate with AWS IoT Jobs using HTTP Signature Version 4 on port 443.

### [Securing users and devices for Jobs](https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs-security.html)

Secure users, devices, and Cloud Services to interact securely with AWS IoT Jobs.

- [Authorizing Jobs users and cloud services](https://docs.aws.amazon.com/iot/latest/developerguide/iam-policy-users-jobs.html): To authorize your users and cloud services, you must use IAM policies on both the control plane and data plane.
- [Authorizing devices to use jobs](https://docs.aws.amazon.com/iot/latest/developerguide/iot-data-plane-jobs.html): To authorize your devices to interact securely with AWS IoT Jobs on the data plane, you must use AWS IoT Core policies.
- [AWS IoT Jobs limits](https://docs.aws.amazon.com/iot/latest/developerguide/job-limits.html): AWS IoT Jobs has Service quotas, or limits, that correspond to the maximum number of service resources or operations for your AWS account.


## [Commands](https://docs.aws.amazon.com/iot/latest/developerguide/iot-remote-command.html)

- [Quick start](https://docs.aws.amazon.com/iot/latest/developerguide/iot-commands-quickstart.html): Complete these steps to send your first command:
- [Commands concepts and status](https://docs.aws.amazon.com/iot/latest/developerguide/iot-remote-command-concepts.html): Use AWS IoT Commands to send instructions from the cloud to connected devices.
- [Commands workflow](https://docs.aws.amazon.com/iot/latest/developerguide/iot-remote-command-workflow.html): This workflow shows how devices interact with AWS IoT Device Management Commands.
- [Create and manage commands](https://docs.aws.amazon.com/iot/latest/developerguide/iot-remote-command-create-manage.html): Use AWS IoT Device Management Commands to configure reusable remote actions or send immediate instructions to devices.
- [Start and monitor command executions](https://docs.aws.amazon.com/iot/latest/developerguide/iot-remote-command-execution-start-monitor.html): After creating a Command, start an Execution on the target device.
- [Deprecate a command resource](https://docs.aws.amazon.com/iot/latest/developerguide/iot-remote-command-deprecate.html): Deprecate commands to indicate they are outdated and should not be used.


## [Secure tunneling](https://docs.aws.amazon.com/iot/latest/developerguide/secure-tunneling.html)

### [What is secure tunneling?](https://docs.aws.amazon.com/iot/latest/developerguide/secure-tunneling-what-is.html)

Use secure tunneling to access devices that are deployed behind port-restricted firewalls at remote sites.

- [Secure tunneling concepts](https://docs.aws.amazon.com/iot/latest/developerguide/secure-tunneling-concepts.html): The following terms are used by secure tunneling when establishing communication with remote devices.
- [How secure tunneling works](https://docs.aws.amazon.com/iot/latest/developerguide/how-secure-tunneling-works.html): The following shows how secure tunneling establishes a connection between your source and destination device.
- [Secure tunnel lifecycle](https://docs.aws.amazon.com/iot/latest/developerguide/tunnel-lifecycle.html): Tunnels can have the status OPEN or CLOSED.

### [Secure tunneling tutorials](https://docs.aws.amazon.com/iot/latest/developerguide/secure-tunneling-tutorial.html)

AWS IoT secure tunneling tutorials that show how to use secure tunneling in AWS IoT.

### [Open a tunnel and start SSH session to remote device](https://docs.aws.amazon.com/iot/latest/developerguide/secure-tunneling-tutorial-open-tunnel.html)

AWS IoT secure tunneling tutorial that shows how to open a tunnel and start an SSH session.

- [Open a tunnel and use browser-based SSH to access remote device](https://docs.aws.amazon.com/iot/latest/developerguide/tunneling-tutorial-quick-setup.html): You can use the quick setup or the manual setup method for creating a tunnel.
- [Open a tunnel using manual setup and connect to remote device](https://docs.aws.amazon.com/iot/latest/developerguide/tunneling-tutorial-manual-setup.html): When you open a tunnel, you can choose the quick setup or the manual setup method for opening a tunnel into the remote device.
- [Open a tunnel for remote device and use browser-based SSH](https://docs.aws.amazon.com/iot/latest/developerguide/tunneling-tutorial-existing-tunnel.html): From the AWS IoT console, you can create a tunnel either from the Tunnels hub or from the details page of an IoT thing that you created.

### [Local proxy](https://docs.aws.amazon.com/iot/latest/developerguide/local-proxy.html)

The local proxy transmits data sent by the application running on the source device by using secure tunneling over a WebSocket secure connection.

- [How to use the local proxy](https://docs.aws.amazon.com/iot/latest/developerguide/how-use-local-proxy.html): You can run the local proxy on the source and destination devices to transmit data to the secure tunneling endpoints.
- [Configure local proxy for devices that use web proxy](https://docs.aws.amazon.com/iot/latest/developerguide/configure-local-proxy-web-proxy.html): You can use local proxy on AWS IoT devices to communicate with AWS IoT secure tunneling APIs.

### [Multiplexing and simultaneous TCP connections](https://docs.aws.amazon.com/iot/latest/developerguide/multiplexing.html)

You can use multiple data streams per tunnel by using the secure tunneling multiplexing feature.

- [Multiplexing multiple data streams](https://docs.aws.amazon.com/iot/latest/developerguide/multiplexing-multiple-streams.html): You can use the multiplexing feature for devices that use multiple connections or ports.
- [Using simultaneous TCP connections](https://docs.aws.amazon.com/iot/latest/developerguide/multiplexing-simultaneous-tcp.html): AWS IoT secure tunneling supports more than one TCP connection simultaneously for each data stream.
- [Configuring a remote device and using IoT agent](https://docs.aws.amazon.com/iot/latest/developerguide/configure-remote-device.html): The IoT agent is used to receive the MQTT message that includes the client access token and start a local proxy on the remote device.
- [Controlling access to tunnels](https://docs.aws.amazon.com/iot/latest/developerguide/tunnel-access.html): Secure tunneling provides service-specific actions, resources, and condition context keys for use in IAM permissions policies.
- [Resolving secure tunneling connectivity issues](https://docs.aws.amazon.com/iot/latest/developerguide/iot-secure-tunneling-troubleshooting.html): When you use AWS IoT secure tunneling, you might run into connectivity issues even if the tunnel is open.


## [Device provisioning](https://docs.aws.amazon.com/iot/latest/developerguide/iot-provision.html)

- [Provisioning devices that don't have device certificates using fleet provisioning](https://docs.aws.amazon.com/iot/latest/developerguide/provision-wo-cert.html): By using AWS IoT fleet provisioning, AWS IoT can generate and securely deliver device certificates and private keys to your devices when they connect to AWS IoT for the first time.

### [Provisioning devices that have device certificates](https://docs.aws.amazon.com/iot/latest/developerguide/provision-w-cert.html)

AWS IoT provides three ways to provision devices when they already have a device certificate (and associated private key) on them:

- [Single thing provisioning](https://docs.aws.amazon.com/iot/latest/developerguide/single-thing-provisioning.html): To provision a thing, use the RegisterThing API or the register-thing CLI command.
- [Just-in-time provisioning](https://docs.aws.amazon.com/iot/latest/developerguide/jit-provisioning.html): You can use just-in-time provisioning (JITP) to provision your devices when they first attempt to connect to AWS IoT.
- [Bulk registration](https://docs.aws.amazon.com/iot/latest/developerguide/bulk-provisioning.html): You can use the start-thing-registration-task command to register things in bulk.
- [Provisioning templates](https://docs.aws.amazon.com/iot/latest/developerguide/provision-template.html): A provisioning template is a JSON document that uses parameters to describe the resources your device must use to interact with AWS IoT.
- [Pre-provisioning hooks](https://docs.aws.amazon.com/iot/latest/developerguide/pre-provisioning-hook.html): AWS recommends using pre-provisioning hook functions when creating provisioning templates to allow more control of which and how many devices your account onboards.
- [Self-managed certificate signing using AWS IoT Core certificate provider](https://docs.aws.amazon.com/iot/latest/developerguide/provisioning-cert-provider.html): You can create an AWS IoT Core certificate provider to sign certificate signing requests (CSRs) in AWS IoT fleet provisioning.
- [Creating IAM policies and roles for a user installing a device](https://docs.aws.amazon.com/iot/latest/developerguide/provision-create-role.html)
- [Device provisioning MQTT API](https://docs.aws.amazon.com/iot/latest/developerguide/fleet-provision-api.html)


## [Fleet indexing](https://docs.aws.amazon.com/iot/latest/developerguide/iot-indexing.html)

### [Managing fleet indexing](https://docs.aws.amazon.com/iot/latest/developerguide/managing-fleet-index.html)

Fleet indexing manages two types of indexes for you: thing indexing and thing group indexing.

- [Manage thing indexing](https://docs.aws.amazon.com/iot/latest/developerguide/managing-index.html): The index created for all of your things is AWS_Things.
- [Manage thing group indexing](https://docs.aws.amazon.com/iot/latest/developerguide/thinggroup-index.html): AWS_ThingGroups is the index that contains all of your thing groups.
- [Device connectivity status](https://docs.aws.amazon.com/iot/latest/developerguide/device-connectivity-status.html): AWS IoT Fleet Indexing supports individual device connectivity querying, allowing you to efficiently retrieve connectivity status and related metadata for specific devices.
- [Querying for aggregate data](https://docs.aws.amazon.com/iot/latest/developerguide/index-aggregate.html): AWS IoT provides four APIs (GetStatistics, GetCardinality, GetPercentiles, and GetBucketsAggregation) that allow you to search your device fleet for aggregate data.
- [Query syntax](https://docs.aws.amazon.com/iot/latest/developerguide/query-syntax.html): In fleet indexing, you use a query syntax to specify queries.
- [Example thing queries](https://docs.aws.amazon.com/iot/latest/developerguide/example-queries.html): Specify queries in a query string using a query syntax.
- [Example thing group queries](https://docs.aws.amazon.com/iot/latest/developerguide/example-thinggroup-queries.html): Queries are specified in a query string using a query syntax and passed to the SearchIndex API.

### [Indexing location data](https://docs.aws.amazon.com/iot/latest/developerguide/location-indexing-geoquery.html)

You can use AWS IoT fleet indexing to index your devices' last sent location data and search for devices using geoqueries.

- [Getting started tutorial](https://docs.aws.amazon.com/iot/latest/developerguide/location-indexing-tutorial.html): This tutorial demonstrates how to use fleet indexing to index your location data.

### [Fleet metrics](https://docs.aws.amazon.com/iot/latest/developerguide/iot-fleet-metrics.html)

Create fleet metrics in AWS IoT Core so that you can monitor your fleet status more effectively.

- [Getting started tutorial](https://docs.aws.amazon.com/iot/latest/developerguide/fleet-metrics-get-started.html): In this tutorial, you create a fleet metric to monitor your sensors' temperatures to detect potential anomalies.
- [Managing fleet metrics](https://docs.aws.amazon.com/iot/latest/developerguide/managing-fleet-metrics.html): This topic shows how to use the AWS IoT console and AWS CLI to manage your fleet metrics.


## [MQTT-based file delivery](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt-based-file-delivery.html)

- [What is a stream?](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt-based-file-delivery-what-is.html): In AWS IoT, a stream is a publicly addressable resource that is an abstraction for a list of files that can be transferred to an IoT device.
- [Manage a stream](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt-based-file-delivery-managing.html): AWS IoT provides AWS SDK and AWS CLI commands that you can use to manage a stream in the AWS Cloud.
- [Use AWS IoT MQTT-based file delivery in devices](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt-based-file-delivery-in-devices.html): To initiate the data transfer process, a device must receive an initial data set, which includes a stream ID at minimum.
- [An example use case in FreeRTOS OTA](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt-based-file-delivery-example.html): The FreeRTOS OTA (over-the-air) agent uses AWS IoT MQTT-based file delivery to transfer FreeRTOS firmware images to FreeRTOS devices.


## [Device Advisor](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor.html)

- [Setting up](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-setting-up.html): Before you use Device Advisor for the first time, complete the following tasks:
- [Getting started with Device Advisor in the console](https://docs.aws.amazon.com/iot/latest/developerguide/da-console-guide.html): This tutorial helps you get started with AWS IoT Core Device Advisor on the console.
- [Device Advisor workflow](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-workflow.html): This tutorial explains how to create a custom test suite and run tests against the device you want to test in the console.
- [Device Advisor detailed console workflow](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-console-tutorial.html): In this tutorial, you'll create a custom test suite and run tests against the device you want to test in the console.
- [Long duration tests console workflow](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-long-duration-console-tutorial.html): This tutorial helps you get started with the Long duration tests on Device Advisor using the console.
- [Device Advisor VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-vpc-endpoint.html): You can establish a private connection between your VPC and the AWS IoT Core Device Advisor test endpoint (data plane) by creating an interface VPC endpoint.

### [Device Advisor test cases](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-tests.html)

Device Advisor provides prebuilt tests in six categories.

- [TLS](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-tests-tls.html): Use these tests to determine if the transport layer security protocol (TLS) between your devices and AWS IoT is secure.
- [MQTT](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-tests-mqtt.html)
- [Shadow](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-tests-shadow.html): Use these tests to verify your devices under test use AWS IoT Device Shadow service correctly.
- [Job Execution](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-tests-job-execution.html)
- [Permissions and policies](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-tests-permissions-policies.html): You can use the following tests to determine if the policies attached to your devicesâ certificates follow standard best practices.
- [Long duration tests](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-tests-long-duration.html): Long duration tests is a new test suite that monitors a device's behavior when it operates over longer periods of time.


## [Device Location](https://docs.aws.amazon.com/iot/latest/developerguide/device-location.html)

- [Resolving location of IoT devices](https://docs.aws.amazon.com/iot/latest/developerguide/device-location-resolve-solvers.html): Use AWS IoT Core Device Location to decode the measurement data from your devices, and resolve the device location using third-party solvers.
- [Resolving device location using MQTT topics](https://docs.aws.amazon.com/iot/latest/developerguide/device-location-reserved-topics.html): You can use reserved MQTT topics to get the latest location information for your devices with the AWS IoT Core Device Location feature.
- [Location solvers and device payload](https://docs.aws.amazon.com/iot/latest/developerguide/device-location-solvers-payload.html): Location solvers are algorithms that can be used to resolve the location of your IoT devices.


## [Event messages](https://docs.aws.amazon.com/iot/latest/developerguide/iot-events.html)

- [Registry events](https://docs.aws.amazon.com/iot/latest/developerguide/registry-events.html): The registry can publish event messages when things, thing types, and thing groups are created, updated, or deleted.
- [Jobs events](https://docs.aws.amazon.com/iot/latest/developerguide/events-jobs.html): The AWS IoT Jobs service publishes to reserved topics on the MQTT protocol when jobs are pending, completed, or canceled, and when a device reports success or failure when running a job.
- [Lifecycle events](https://docs.aws.amazon.com/iot/latest/developerguide/life-cycle-events.html): See the following lifecycle events that AWS IoT publishes.


## [Troubleshooting](https://docs.aws.amazon.com/iot/latest/developerguide/iot_troubleshooting.html)

### [AWS IoT Core troubleshooting guide](https://docs.aws.amazon.com/iot/latest/developerguide/iot-core-troubleshooting.html)

- [Diagnosing connectivity issues](https://docs.aws.amazon.com/iot/latest/developerguide/diagnosing-connectivity-issues.html)
- [Diagnosing rules issues](https://docs.aws.amazon.com/iot/latest/developerguide/diagnosing-rules.html)
- [Diagnosing problems with shadows](https://docs.aws.amazon.com/iot/latest/developerguide/diagnosing-shadows.html)
- [Diagnosing Salesforce action issues](https://docs.aws.amazon.com/iot/latest/developerguide/diagnosing-salesforce.html)
- [Diagnosing Stream Limits](https://docs.aws.amazon.com/iot/latest/developerguide/diagnosing-stream-limits.html): Troubleshooting "Stream limit exceeded for your AWS account"
- [Troubleshooting device fleet disconnects](https://docs.aws.amazon.com/iot/latest/developerguide/ota-troubleshooting-fleet-disconnects.html)

### [AWS IoT Device Management troubleshooting guide](https://docs.aws.amazon.com/iot/latest/developerguide/device-management-troubleshooting.html)

- [AWS IoT Jobs Troubleshooting](https://docs.aws.amazon.com/iot/latest/developerguide/jobs-troubleshooting.html): This is the troubleshooting section for AWS IoT Jobs.
- [Fleet Indexing Troubleshooting](https://docs.aws.amazon.com/iot/latest/developerguide/fleet-indexing-troubleshooting.html)
- [AWS IoT Device Management Software Package Catalog Troubleshooting](https://docs.aws.amazon.com/iot/latest/developerguide/software-package-catalog-troubleshooting.html): This is the troubleshooting section for AWS IoT Device Management Software Package Catalog.
- [AWS IoT Device Advisor troubleshooting guide](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-troubleshooting.html)
- [AWS IoT errors](https://docs.aws.amazon.com/iot/latest/developerguide/iot-errors.html)


## [Code examples](https://docs.aws.amazon.com/iot/latest/developerguide/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/iot/latest/developerguide/service_code_examples_basics.html)

The following code examples show how to use the basics of AWS IoT with AWS SDKs.

- [Hello AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/example_iot_Hello_section.html): Hello AWS IoT
- [Learn the basics](https://docs.aws.amazon.com/iot/latest/developerguide/example_iot_Scenario_section.html): Learn the basics of AWS IoT with an AWS SDK

### [Actions](https://docs.aws.amazon.com/iot/latest/developerguide/service_code_examples_actions.html)

The following code examples show how to use AWS IoT with AWS SDKs.

- [AttachThingPrincipal](https://docs.aws.amazon.com/iot/latest/developerguide/example_iot_AttachThingPrincipal_section.html): Use AttachThingPrincipal with an AWS SDK or CLI
- [CreateKeysAndCertificate](https://docs.aws.amazon.com/iot/latest/developerguide/example_iot_CreateKeysAndCertificate_section.html): Use CreateKeysAndCertificate with an AWS SDK or CLI
- [CreateThing](https://docs.aws.amazon.com/iot/latest/developerguide/example_iot_CreateThing_section.html): Use CreateThing with an AWS SDK or CLI
- [CreateTopicRule](https://docs.aws.amazon.com/iot/latest/developerguide/example_iot_CreateTopicRule_section.html): Use CreateTopicRule with an AWS SDK or CLI
- [DeleteCertificate](https://docs.aws.amazon.com/iot/latest/developerguide/example_iot_DeleteCertificate_section.html): Use DeleteCertificate with an AWS SDK or CLI
- [DeleteThing](https://docs.aws.amazon.com/iot/latest/developerguide/example_iot_DeleteThing_section.html): Use DeleteThing with an AWS SDK or CLI
- [DeleteTopicRule](https://docs.aws.amazon.com/iot/latest/developerguide/example_iot_DeleteTopicRule_section.html): Use DeleteTopicRule with an AWS SDK or CLI
- [DescribeEndpoint](https://docs.aws.amazon.com/iot/latest/developerguide/example_iot_DescribeEndpoint_section.html): Use DescribeEndpoint with an AWS SDK or CLI
- [DescribeThing](https://docs.aws.amazon.com/iot/latest/developerguide/example_iot_DescribeThing_section.html): Use DescribeThing with an AWS SDK or CLI
- [DetachThingPrincipal](https://docs.aws.amazon.com/iot/latest/developerguide/example_iot_DetachThingPrincipal_section.html): Use DetachThingPrincipal with an AWS SDK or CLI
- [ListCertificates](https://docs.aws.amazon.com/iot/latest/developerguide/example_iot_ListCertificates_section.html): Use ListCertificates with an AWS SDK or CLI
- [ListThings](https://docs.aws.amazon.com/iot/latest/developerguide/example_iot_ListThings_section.html): Use ListThings with an AWS SDK or CLI
- [SearchIndex](https://docs.aws.amazon.com/iot/latest/developerguide/example_iot_SearchIndex_section.html): Use SearchIndex with an AWS SDK or CLI
- [UpdateIndexingConfiguration](https://docs.aws.amazon.com/iot/latest/developerguide/example_iot_UpdateIndexingConfiguration_section.html): Use UpdateIndexingConfiguration with an AWS SDK or CLI
- [UpdateThing](https://docs.aws.amazon.com/iot/latest/developerguide/example_iot_UpdateThing_section.html): Use UpdateThing with an AWS SDK or CLI
