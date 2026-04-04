# Source: https://docs.aws.amazon.com/iot-mi/latest/devguide/llms.txt

# Managed integrations for AWS IoT Device Management Developer Guide

- [What is managed integrations for AWS IoT Device Management](https://docs.aws.amazon.com/iot-mi/latest/devguide/what-is-managedintegrations.html)
- [Set up managed integrations](https://docs.aws.amazon.com/iot-mi/latest/devguide/setting-up.html)
- [Get started](https://docs.aws.amazon.com/iot-mi/latest/devguide/getting-started.html)
- [Device provisioning](https://docs.aws.amazon.com/iot-mi/latest/devguide/device-provisioning.html)
- [Manage device lifecycle and profiles](https://docs.aws.amazon.com/iot-mi/latest/devguide/device-and-device-profile-lifecycle-management.html)
- [Device commands and events](https://docs.aws.amazon.com/iot-mi/latest/devguide/device-commands-events.html)
- [Managed integrations notifications](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-notifications.html)
- [Document history](https://docs.aws.amazon.com/iot-mi/latest/devguide/doc-history.html)

## [Data models](https://docs.aws.amazon.com/iot-mi/latest/devguide/data-model.html)

- [Managed integrations data model](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-data-model.html): Understand the Managed integrations data model that enables unified device control and management across multiple vendors and protocols.
- [AWS implementation of the Matter data model](https://docs.aws.amazon.com/iot-mi/latest/devguide/matter-data-model.html): Understand how AWS implements the Matter data model to provide interoperability across different smart home devices and protocols.

### [Data model schemas](https://docs.aws.amazon.com/iot-mi/latest/devguide/data-model-schemas.html)

Learn about the capability and type definition schemas in managed integrations

- [Schema for capability definitions](https://docs.aws.amazon.com/iot-mi/latest/devguide/schema-for-capability-definitions.html): Learn about the schema elements for capability definitions in managed integrations
- [Schema for type definitions](https://docs.aws.amazon.com/iot-mi/latest/devguide/schema-for-type-definitions.html): Learn about the schema elements for type definitions in managed integrations
- [Building and using type definitions in capability schema documents](https://docs.aws.amazon.com/iot-mi/latest/devguide/type-definitions.html): Learn about type definitions in managed integrations schemas.


## [Tag resources](https://docs.aws.amazon.com/iot-mi/latest/devguide/tagging-iot.html)

- [Tag with IAM policies](https://docs.aws.amazon.com/iot-mi/latest/devguide/tagging-iot-iam.html): You can apply tag-based resource-level permissions in the IAM policies you use for managed integrations API actions.


## [Cloud-to-Cloud (C2C) connectors](https://docs.aws.amazon.com/iot-mi/latest/devguide/concepts-c2c-connector.html)

### [Build a C2C (Cloud-to-Cloud) connector](https://docs.aws.amazon.com/iot-mi/latest/devguide/concepts-building-connector.html)

Learn how to create a C2C connector for managed integrations for AWS IoT Device Management.

### [Authorization](https://docs.aws.amazon.com/iot-mi/latest/devguide/concepts-authorization.html)

Learn about the authorization requirements for C2C connectors, including OAuth 2.0 and General Authorization options.

### [OAuth 2.0 requirements for account linking](https://docs.aws.amazon.com/iot-mi/latest/devguide/concepts-account-linking.html)

Learn how to implement OAuth 2.0 authorization for C2C Connectors in managed integrations, enabling secure account linking and device access for third-party integrations.

- [Account linking roles](https://docs.aws.amazon.com/iot-mi/latest/devguide/roles-account-linking.html): Learn about the four key roles in OAuth 2.0 account linking for managed integrations for AWS IoT Device Management: authorization server, resource owner, resource server, and client.
- [Account linking workflow](https://docs.aws.amazon.com/iot-mi/latest/devguide/account-linking-flow.html): Learn how managed integrations for AWS IoT Device Management obtains access tokens to interact with third-party devices through your C2C connector, including the OAuth 2.0 flow and account linking process.
- [General/Custom Authorization requirements for connector developers](https://docs.aws.amazon.com/iot-mi/latest/devguide/concepts-general-authorization-dev.html): Learn how to implement General Authorization in your C2C connector to support device access using credentials stored in AWS Secrets Manager.

### [Implement C2C connector interface operations](https://docs.aws.amazon.com/iot-mi/latest/devguide/connector-operations-overview.html)

Learn about the four essential operations that AWS Lambda must implement to function as a connector for managed integrations for AWS IoT Device Management, including user activation, device discovery, command sending, and user deactivation.

- [Implement the AWS.ActivateUser operation](https://docs.aws.amazon.com/iot-mi/latest/devguide/activate-user-op.html): Learn how to implement the AWS.ActivateUser operation for managed integrations for AWS IoT Device Management to retrieve user identifiers and process activation requests.
- [Implement the AWS.DiscoverDevices operation](https://docs.aws.amazon.com/iot-mi/latest/devguide/discover-devices-op.html): Learn how to implement device discovery in managed integrations for AWS IoT Device Management, enabling customers to align physical devices with digital representations through an asynchronous process using connectors.
- [Implement the AWS.SendCommand operation](https://docs.aws.amazon.com/iot-mi/latest/devguide/send-command-op.html): Learn how to implement the AWS.SendCommand operation in your Cloud-to-Cloud connector to enable command execution on third-party cloud devices.
- [Send device events with the SendConnectorEvent API](https://docs.aws.amazon.com/iot-mi/latest/devguide/send-connector-events.html)
- [Implement the AWS.DeactivateUser operation](https://docs.aws.amazon.com/iot-mi/latest/devguide/deactive-user-op.html)
- [Invoke your C2C connector](https://docs.aws.amazon.com/iot-mi/latest/devguide/allow-iot-smart-home.html): AWS Lambda allows for resource-based policies to authorize who can invoke a Lambda.
- [Add permissions to your IAM Role](https://docs.aws.amazon.com/iot-mi/latest/devguide/adding-permissions-to-iam-role.html): All managed integrations APIs require AWS sigV4 authentication to invoke.
- [Manually test your C2C connector](https://docs.aws.amazon.com/iot-mi/latest/devguide/manually-testing-connector.html): Learn how to manually test your C2C connector end-to-end by simulating customer and end user interactions.

### [Use a C2C (Cloud-to-Cloud) connector](https://docs.aws.amazon.com/iot-mi/latest/devguide/use-c2c-create-cloud-connector.html)

A C2C connector manages the translation of request and response messages, and enables communication between managed integrations and a third-party vendor cloud.

- [General/Custom Authorization requirements](https://docs.aws.amazon.com/iot-mi/latest/devguide/concepts-general-authorization.html): Learn how to implement General/Custom Authorization for C2C Connectors in managed integrations, enabling device control using pre-shared keys or tokens stored in AWS Secrets Manager.


## [Hub SDK](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-v2.html)

- [Device onboarding](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-v2-device-onboarding.html): Learn about Managed integrations Hub SDK components and flows for IoT device onboarding, including core provisioner functions, and protocol-specific plugins.
- [Device control](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-v2-control.html): Explore managed integrations Hub SDK components for IoT device control, including Edge Agent functions, Common Data Model Bridge operations, and protocol-specific plugin handling.

### [Install and validate the managed integrations Hub SDK](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-v2-cookbook-deployment.html)

Deploy and validate the managed integrations Hub SDK on your devices using either AWS IoT Greengrass or manual installation methods.

- [Install the SDK using AWS IoT Greengrass](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-v2-cookbook-deployment-gg.html): Set up the managed integrations Hub SDK components for Zigbee and Z-Wave devices using AWS IoT Greengrass deployment and configuration.
- [Deploy the Hub SDK with a script](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-v2-cookbook-deployment-nogg.html): Install and validate the managed integrations Hub SDK components using manual script deployment for your IoT devices.
- [Deploy Hub SDK with systemd](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-v2-cookbook-deployment-hub-deployment-scripts.html): Scripts for deploying and setting up services on a Linux-based hub device.

### [Onboard your hubs](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-v2-cookbook-usinghub.html)

Learn how to onboard IoT hub devices to managed integrations by configuring certificates and device settings for secure communication.

- [Setup for onboarding](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-v2-cookbook-hubsetup.html): Configure your hub devices for onboarding by creating managed things, setting up directories, and managing certificates for fleet provisioning.

### [Onboard devices and operate them in hub](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-v2-cookbook-onboard-to-hub.html)

Learn how to configure your devices for onboarding using simple setup, user guided setup, or WiFi Simple Setup options.

- [Simple setup to onboard and operate devices](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-v2-cookbook-ss.html): Learn how to configure your devices for onboarding using the simple setup option.
- [User guided setup to onboard and operate devices](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-v2-cookbook-ugs.html): Learn how to configure your devices for onboarding using the user guided setup option.
- [Capability rediscovery](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-v2-onboarding-capability-rediscovery.html): Learn how to update device capabilities when end device or hub capabilities have changed.

### [WiFi Simple Setup to onboard and operate devices](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-v2-cookbook-wss.html)

Learn how to configure your devices for onboarding using the WiFi Simple Setup option.

- [Configure provisioners for WiFi Simple Setup](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-v2-cookbook-wss-provisioner-config.html): Configure hub devices to function as provisioners that share WiFi credentials with new devices during WiFi Simple Setup.
- [Configure provisionees for WiFi Simple Setup](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-v2-cookbook-wss-provisionee-config.html): Prepare WiFi devices to receive credentials automatically from provisioners during WiFi Simple Setup.
- [Custom certificate handler](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-v2-cookbook-certhandler.html): Create a custom certificate handler to manage device credentials securely in your own storage implementation.
- [Custom protocol plugin](https://docs.aws.amazon.com/iot-mi/latest/devguide/custom-protocol-plugin.html): Integrate your proprietary IoT protocols with managed integrations for AWS IoT Device Management.
- [Matter Plugin](https://docs.aws.amazon.com/iot-mi/latest/devguide/matter-plugin.html): Learn how to use the Matter Plugin reference implementation to control Matter devices both locally and remotely through Managed integrations.

### [Hub SDK client](https://docs.aws.amazon.com/iot-mi/latest/devguide/hub-sdk-client.html)

Understand the Hub SDK client architecture and APIs for integrating IoT hubs with Managed integrations.

### [Hub SDK client API](https://docs.aws.amazon.com/iot-mi/latest/devguide/hub-sdk-client-api-reference.html)

Use the Hub SDK client to interact with managed integrations Device SDK.

- [Client initialization](https://docs.aws.amazon.com/iot-mi/latest/devguide/client-initialization.html): To start using the DeviceSDKClient, initialize it with a client ID.
- [Provision task subscription](https://docs.aws.amazon.com/iot-mi/latest/devguide/provision-task-subscription.html): Use these methods to subscribe to provision-related tasks from the managed integrations components.
- [Provision task publication](https://docs.aws.amazon.com/iot-mi/latest/devguide/provision-task-publication.html): Use these methods to publish provision-related requests to the managed integrations components.
- [Control task subscription](https://docs.aws.amazon.com/iot-mi/latest/devguide/control-task-subscription.html): Use these methods to subscribe to control-related tasks from the managed integrations components.
- [Control task publication](https://docs.aws.amazon.com/iot-mi/latest/devguide/control-task-publication.html): Use these methods to publish control-related requests to the managed integrations components.
- [Logging features](https://docs.aws.amazon.com/iot-mi/latest/devguide/logging-features.html): Use logging methods to implement managed integrations logging features in your application.
- [Other APIs](https://docs.aws.amazon.com/iot-mi/latest/devguide/other-apis.html)
- [Hub control](https://docs.aws.amazon.com/iot-mi/latest/devguide/hub-control.html): Learn how to set up hub control for the managed integrations Hub SDK.
- [Enable CloudWatch Logs](https://docs.aws.amazon.com/iot-mi/latest/devguide/hub-log.html): Learn how to configure and manage Hub SDK log settings.
- [Supported Zigbee and Z-Wave device types](https://docs.aws.amazon.com/iot-mi/latest/devguide/supported-devices.html): Learn about which Zigbee and Z-Wave device types are supported by Managed integrations.

### [Run managed integrations on Raspberry Pi](https://docs.aws.amazon.com/iot-mi/latest/devguide/supported-raspberry.html)

Build unified control experiences for AWS IoT devices across multiple protocols and connectivity types using managed integrations.

- [Managed integrations Hub SDK image on Raspberry Pi](https://docs.aws.amazon.com/iot-mi/latest/devguide/raspberrypi-device-hub-sdk.html): Deploy the Managed integrations Hub SDK on a Raspberry Pi 5 device.
- [Managed integrations Hub SDK Docker container on Raspberry Pi](https://docs.aws.amazon.com/iot-mi/latest/devguide/raspberrypi-container-docker-sdk.html): Deploy the Managed integrations docker container Hub SDK on a Raspberry Pi 5 device.
- [Managed integrations demo application](https://docs.aws.amazon.com/iot-mi/latest/devguide/supported-raspberry-demo-app.html): Deploy a comprehensive React-based demo application that showcases Managed Integrations capabilities.
- [Offboard managed integrations hub](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-hub-offboard.html): Offboard the hub for managed integrations Hub SDK.

### [Protocol-specific middleware](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-middleware.html)

Learn about protocol-specific middleware components that enable Managed integrations to communicate with devices using different protocols like Zigbee and Z-Wave.

### [Middleware code organization](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-middleware-code.html)

This section contains information about the location of the code for each component inside the IotManagedIntegrationsDeviceSDK-Middleware repository.

- [Zigbee middleware code organization](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-middleware-zigbee.html): The following shows the Zigbee reference middleware code organization.
- [Z-Wave middleware code organization](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-middleware-zwave.html): The following shows the Z-wave reference middleware code organization.
- [Integrate middleware with SDK](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-integration-middleware.html): The middleware integration on the new hub is discussed in the following sections.


## [End device SDK](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-devices.html)

- [What is the End device SDK?](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-device-whatis.html): Learn how the End device SDK integrates AWS IoT devices with managed integrations through secure cloud connectivity.
- [Architecture and components](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-device-architecture.html): Review the End device SDK architecture and how components interact with low level C-Functions.
- [Provisionee](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-device-provisionee.html): Implement secure device provisioning through fleet provisioning by claim using the managed integrations Provisionee component.

### [OTA updates](https://docs.aws.amazon.com/iot-mi/latest/devguide/ota-updates.html)

Learn how to implement over-the-air (OTA) updates for your IoT devices using Managed integrations.

- [Prerequisites](https://docs.aws.amazon.com/iot-mi/latest/devguide/ota-updates-prerequisites-configuration.html): Set up the necessary prerequisites for implementing over-the-air updates, including Amazon S3 access configuration.
- [Implement Over-the-Air(OTA) tasks](https://docs.aws.amazon.com/iot-mi/latest/devguide/ota-task-types-implementation.html): Learn about the different types of OTA tasks you can create and how to implement them for your device updates.
- [OTA task configurations setup](https://docs.aws.amazon.com/iot-mi/latest/devguide/ota-task-configuration-implementation.html): Learn how to create and apply advanced configurations for OTA tasks, including rollout rates, abort conditions, and timeouts.
- [Apply configuration settings to OTA tasks](https://docs.aws.amazon.com/iot-mi/latest/devguide/apply-ota-task-configuration.html): Learn how to apply configuration settings to OTA tasks and add scheduling parameters.
- [Monitor OTA notifications](https://docs.aws.amazon.com/iot-mi/latest/devguide/ota-update-notification-methods.html): Learn about different methods for monitoring the status of OTA updates across your devices.
- [Process job documents](https://docs.aws.amazon.com/iot-mi/latest/devguide/process-job-documents-implementation.html): Learn how to process job documents on your device when an OTA update is available.
- [Implement OTA agent](https://docs.aws.amazon.com/iot-mi/latest/devguide/implement-ota-agent.html): Learn how to implement an OTA agent on your device to process job documents, download updates, and perform installation operations.

### [Data model code generator](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-device-codegen.html)

Generate C code data model handlers from .matter files to process device-cloud data exchanges.

- [Environment setup](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-codegen-env.html): Configure your development environment to use the code generator for managed integrations.
- [Generate code for devices](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-codegen-generate.html): Create device-specific C code using the managed integrations code generation tools.
- [Low level C-Function APIs](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-device-api.html): Implement device-cloud interactions using low level C-Function APIs provided by the SDK.
- [Service-device interactions](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-device-interactions.html): Understand how managed integrations devices handle remote commands and unsolicited events.

### [Get started with End device SDK](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-device-onboarding.html)

Integrate the End device SDK into your device firmware by configuring build environments, network settings, and implementing hardware functions.

- [Port the End device SDK](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-device-porting-guide.html): Port the End device SDK to your platform and implement the required platform-specific functionalities.
- [Technical reference](https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-device-appendix.html)


## [Security](https://docs.aws.amazon.com/iot-mi/latest/devguide/security.html)

- [Data protection](https://docs.aws.amazon.com/iot-mi/latest/devguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in managed integrations.

### [Identity and access management](https://docs.aws.amazon.com/iot-mi/latest/devguide/security-iam.html)

How to authenticate requests and manage access for your managed integrations resources.

- [AWS managed policies](https://docs.aws.amazon.com/iot-mi/latest/devguide/security-iam-awsmanpol.html): Learn about AWS managed policies for managed integrations and recent changes to those policies.
- [How managed integrations works with IAM](https://docs.aws.amazon.com/iot-mi/latest/devguide/security_iam_service-with-iam.html): Learn how managed integrations integrates with AWS Identity and Access Management (IAM) and how to create policies to control access to managed integrations resources.
- [Identity-based policy examples](https://docs.aws.amazon.com/iot-mi/latest/devguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify managed integrations resources.
- [Troubleshooting](https://docs.aws.amazon.com/iot-mi/latest/devguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with managed integrations and IAM.
- [Using service-linked roles](https://docs.aws.amazon.com/iot-mi/latest/devguide/using-service-linked-roles.html): How to use service-linked roles to give managed integrations access to resources in your AWS account.
- [Use AWS Secrets Manager for data protection for C2C workflows](https://docs.aws.amazon.com/iot-mi/latest/devguide/secrets-manager.html): Use AWS Secrets Manager to protect your data when using open authorization (OAuth) with managed integrations for AWS IoT Device Management.
- [Compliance validation](https://docs.aws.amazon.com/iot-mi/latest/devguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.

### [Use managed integrations with interface VPC endpoints](https://docs.aws.amazon.com/iot-mi/latest/devguide/interface-vpc-endpoints.html)

You can connect and use managed integrations with Amazon VPC endpoints

- [VPC endpoint considerations](https://docs.aws.amazon.com/iot-mi/latest/devguide/vpc-endpoints-considerations.html): Important considerations when setting up interface VPC endpoints for AWS IoT Managed integrations.
- [Creating VPC endpoints](https://docs.aws.amazon.com/iot-mi/latest/devguide/vpc-endpoints-creating.html): Steps to create a VPC endpoint for the AWS IoT Managed integrations service.
- [Testing VPC endpoints](https://docs.aws.amazon.com/iot-mi/latest/devguide/vpc-endpoints-testing.html): Steps to test the connection to AWS IoT Managed integrations through your Amazon VPC endpoint.
- [Access control](https://docs.aws.amazon.com/iot-mi/latest/devguide/vpc-endpoints-access-control.html): How to control access to AWS IoT Managed integrations through VPC endpoints using endpoint policies.
- [Pricing](https://docs.aws.amazon.com/iot-mi/latest/devguide/vpc-endpoints-pricing.html): Pricing information for using interface VPC endpoints with AWS IoT Managed integrations.
- [Limitations](https://docs.aws.amazon.com/iot-mi/latest/devguide/vpc-endpoints-limitations.html): Limitations of VPC endpoints for AWS IoT Managed integrations.
- [Connect to managed integrations for AWS IoT Device Management FIPS endpoints](https://docs.aws.amazon.com/iot-mi/latest/devguide/FIPS-endpoints.html): Learn how to manually test your C2C connector end-to-end by simulating customer and end user interactions.


## [Monitoring](https://docs.aws.amazon.com/iot-mi/latest/devguide/monitoring-overview.html)

- [CloudTrail logs](https://docs.aws.amazon.com/iot-mi/latest/devguide/logging-using-cloudtrail.html): Learn about logging Managed integrations with AWS CloudTrail.
