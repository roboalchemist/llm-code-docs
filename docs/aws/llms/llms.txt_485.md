# Source: https://docs.aws.amazon.com/iot-wireless/latest/developerguide/llms.txt

# AWS IoT Wireless Developer Guide

- [What is AWS IoT Wireless?](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/what-is-iot-wireless.html)
- [Getting started](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/getting-started.html)
- [Using IPv6 with AWS IoT Wireless](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/wireless-ipv6-access.html)
- [AWS IoT Wireless API operations](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-wireless-api-reference.html)
- [AWS CloudFormation resources](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/creating-iotwireless-resources-cloudformation.html)
- [Tagging your wireless resources](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/tagging-iotwireless.html)

## [AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-lorawan.html)

- [What is AWS IoT Core for LoRaWAN?](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/what-is-iot-lorawan.html): Learn about the LoRaWAN technology, how AWS IoT Core for LoRaWAN works, and how to get started.

### [Connecting to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-getting-started.html)

Onboard your gateways and devices to AWS IoT Core for LoRaWAN and connect them to the cloud.

### [Onboard LoRaWAN gateways](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-onboard-gateways.html)

Learn how you can onboard LoRaWAN gateways to communicate with AWS IoT Core for LoRaWAN.

- [Select frequency band and add IAM role](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-rfregion-permissions.html): Select the frequency band to use and add the IAM role for CUPS to manage gateway credentials.
- [Add a LoRaWAN gateway](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-onboard-gateway-add.html): Learn how to add a LoRaWAN gateway to AWS IoT using the console and CLI.
- [Connect LoRaWAN gateway and check status](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-gateway-connection-status.html): Learn how to connect your LoRaWAN gateway to AWS IoT and verify the status.

### [Onboard LoRaWAN devices](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-onboard-end-devices.html)

Learn how you can onboard LoRaWAN devices to communicate with AWS IoT Core for LoRaWAN.

- [Add your LoRaWAN device](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-end-devices-add.html): Learn how to add your LoRaWAN gateways to communicate with AWS IoT Core for LoRaWAN.
- [Add LoRaWAN profiles](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-define-profiles.html): Learn how to add your LoRaWAN device and service profiles.
- [Add a LoRaWAN destination](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-create-destinations.html): Learn how to add a LoRaWAN destination for your devices.
- [Create rules for LoRaWAN messages](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-destination-rules.html): Learn how to add rules for LoRaWAN destinations.
- [Connect LoRaWAN device and check status](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-device-connection-status.html): Learn how to connect your LoRaWAN device and check the connection status.

### [Configuring position for LoRaWAN resources](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-configure-location.html)

Configure position information of LoRaWAN gateways and devices.

- [Configuring the position of LoRaWAN gateways](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-location-gateways.html): Configure static position information of LoRaWAN gateways.
- [Configuring position of LoRaWAN devices](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-location-devices.html): Configure position information of LoRaWAN devices and activate positioning.

### [Managing LoRaWAN gateways](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-manage-gateways.html)

Managing LoRaWAN gateways that have been onboarded to AWS IoT Core for LoRaWAN.

- [Configure gateway beaconing](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-gateway-beaconing.html): Configure beaconing for your LoRaWAN gateways to send to class B LoRaWAN devices.
- [Configure gateway subbands and filtering](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-subband-filter-configuration.html): Configure filtering, and sub-bands for your LoRaWAN gateways.
- [Choose participating gateways for downlink](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-gateway-participate.html): Choose the gateways that you want to participate for receiving the downlink data traffic.

### [Update gateway firmware using CUPS](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-update-firmware.html)

Update your LoRaWAN gateway firmware using the Configuration and Update Server (CUPS) service with AWS IoT Core for LoRaWAN.

- [(Optional) Generate update file and signature](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-script-fwupdate-sigkey.html): An example for generating the firmware update file and signature for the Raspberry Pi RAKWireless gateway.
- [Upload file to S3 and add IAM role](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-upload-firmware-s3bucket.html): Steps to upload firmware file to Amazon S3 and add IAM role if you're using the AWS CLI.
- [Schedule and run firmware update](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-schedule-firmware-update.html): Schedule and run firmware update for wireless gateway by creating a task definition.

### [Managing LoRaWAN devices](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-manage-end-devices.html)

Manage your LoRaWAN devices efficiently at scale using AWS IoT Core for LoRaWAN.

- [Performing ADR for LoRaWAN devices](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-lorawan-adr.html): Optimize data rates for your LoRaWAN devices with AWS IoT Core for LoRaWAN.
- [View LoRaWAN uplink message format](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-uplink-metadata-format.html): How to view and manage the uplink messages that are sent from your LoRaWAN devices to the cloud.
- [Queue LoRaWAN downlink messages](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-downlink-queue.html): How to queue and send downlink messages from the cloud to your LoRaWAN devices.

### [Managing traffic from public LoRaWAN networks](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-lorawan-roaming.html)

How to connect your devices to public LoRaWAN networks and manage traffic without using private gateways.

- [How LoRaWAN public network support works](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-roaming-works.html): LoRaWAN public network concepts and how an AWS IoT Core for LoRaWAN public network works.
- [How to use LoRaWAN public network](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-roaming-use.html): How to connect your devices to the public LoRaWAN network using the AWS IoT console and the CLI.

### [FUOTA and LoRaWAN multicast groups](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-multicast-fuota.html)

Learn how to perform FUOTA to update the firmware of LoRaWAN devices and multicast groups.

- [Prepare for multicast and FUOTA](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-prepare-devices-multicast.html): Prepare your devices and update profiles to join multicast groups and perform FUOTA updates.

### [Create multicast groups](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-multicast-groups.html)

Create a multicast group to send a downlink payload to multiple devices.

- [Create multicast groups and add devices](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-create-multicast-groups.html): Create a multicast group and add devices to the group.
- [Choose gateways for multicast downlink](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-multicast-choose-gateways.html): A multicast group that consists of multiple devices can have the devices associated with multiple gateways.
- [Monitor and troubleshoot multicast groups](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-multicast-status.html): Monitor and troubleshoot the status of your multicast group and devices in the group.
- [Schedule multicast downlink message](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-multicast-schedule-downlink.html): Schedule a downlink message to send to devices in your multicast group.

### [FUOTA for LoRaWAN](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-mc-fuota-overview.html)

Use FUOTA to update the firmware of a group of LoRaWAN devices.

- [FUOTA process overview](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-fuota-mc-process.html): How FUOTA works to update the firmware of a group of LoRaWAN devices.
- [Create FUOTA task](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-fuota-create-task.html): Create FUOTA task and provide the firmware image for the update.
- [Add devices and schedule FUOTA](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-fuota-add-devices.html): Add devices and multicast groups to a FUOTA task and schedule a FUOTA session to update firmware.
- [Monitor and troubleshoot FUOTA task](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-fuota-status.html): Monitor and troubleshoot the status of your FUOTA task and devices in the task.

### [Monitoring with network analyzer](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/network-analyzer-overview.html)

Monitor your LoRaWAN resources in real time using network analyzer.

- [Add IAM role for network analyzer](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/network-analyzer-iam.html): Add the IAM role that grants you permission to update and get a network analyzer configuration.

### [Create a configuration and add resources](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/network-analyzer-create-resources.html)

Create a network analyzer configuration and add resources to be monitored to the configuration.

- [Create a network analyzer configuration](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/network-analyzer-create.html): Create a network analyzer configuration to monitor resources.
- [Add resources and update configuration](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/network-analyzer-resources.html): Add LoRaWAN resources to be monitored to network analyzer configuration and update configuration.

### [Stream trace messages with WebSockets](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/network-analyzer-api.html)

Use network analyzer to stream trace messages in real time with AWS IoT Core for LoRaWAN.

- [Generate a presigned request](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/network-analyzer-generate-request.html): Learn from pseudocode on how to use the network analyzer API to generate a presigned request.
- [Sample presigned request Python code](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/network-analyzer-request-sample.html): Use Python coding to generate a presigned request to use the network analyzer API.
- [WebSocket messages and status codes](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/network-analyzer-messages-status.html): Learn about the different WebSocket messages and status codes when using network analyzer.
- [Monitor trace messages in real time](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/network-analyzer-logs.html): Activate trace messaging and view network analyzer trace messages in real time for your resources.
- [Debug your multicast groups and FUOTA tasks using network analyzer](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-network-analyzer-fuota.html): Activate trace messaging and troubleshoot multicast groups and FUOTA tasks with network analyzer.
- [AWS IoT Core for LoRaWAN metrics](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-lorawan-metrics.html): Use AWS IoT Core for LoRaWAN metrics to monitor health of your LoRaWAN resources.

### [LoRaWAN VPC endpoints](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/vpc-interface-endpoints.html)

Use interface VPC endpoint to create a private connection between your VPC and AWS IoT Core for LoRaWAN.

- [Onboard control plane endpoint](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-onboard-control-endpoint.html): Use AWS IoT Core for LoRaWAN to onboard control plane API endpoints with AWS PrivateLink.

### [Onboard data plane endpoints](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/onboard-lns-cups-endpoints.html)

Use AWS IoT Core for LoRaWAN to onboard data plane API endpoints with AWS PrivateLink.

- [Create VPC endpoints and hosted zone](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/create-vpc-lns-cups.html): Use AWS IoT Core for LoRaWAN to create VPC endpoint and private hosted zone for AWS PrivateLink.
- [Use VPN to connect LoRa gateways](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/lorawan-vpc-vpn-connection.html): Use VPN to connect LoRa gateways with AWS PrivateLink.


## [AWS IoT Core for Amazon Sidewalk](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-sidewalk.html)

- [What is AWS IoT Core for Amazon Sidewalk?](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/what-is-iot-sidewalk.html): Learn about the LoRaWAN technology, how AWS IoT Core for LoRaWAN works, and how to get started.
- [Get started using AWS IoT Core for Amazon Sidewalk](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/sidewalk-getting-started.html): Get started with AWS IoT Core for Amazon Sidewalk to onboard your Sidewalk devices and manage them at scale.

### [Connecting to AWS IoT Core for Amazon Sidewalk](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-sidewalk-onboard.html)

Onboard your devices to AWS IoT Core for Amazon Sidewalk and connect them to the cloud.

### [Add your Sidewalk device](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-sidewalk-create-device.html)

Learn how to add your Sidewalk devices to communicate with AWS IoT Core for Amazon Sidewalk.

- [Add your device profile and Sidewalk end device](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-sidewalk-add-device.html): This section shows how you can create a device profile.
- [Obtain device JSON files for provisioning](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/sidewalk-json-get.html): After you've added your Sidewalk device to AWS IoT Core for Amazon Sidewalk, download the JSON file that contains the information required to provision your end device.

### [Add a destination for Sidewalk device](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-sidewalk-qsg-destination.html)

Learn how to add a Sidewalk destination for your devices.

- [Create a destination for your Sidewalk device](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-sidewalk-destination-create.html): You can add a destination to your account for AWS IoT Core for Amazon Sidewalk either from the using the Destinations hub or using the CreateDestination.
- [Create an IAM role and IoT rule for your destination](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/sidewalk-destination-rule-role.html): Learn how to add rules for Sidewalk destinations.
- [Connect your Sidewalk device](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-sidewalk-connect-uplink-metadata.html): Learn how to add a Sidewalk device and check the connection status.

### [Bulk provisioning Sidewalk devices](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/sidewalk-bulk-provisioning.html)

Provision Sidewalk devices in bulk with AWS IoT Core for Amazon Sidewalk.

- [Amazon Sidewalk bulk provisioning workflow](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/sidewalk-bulk-provisioning-workflow.html): Process overview for provisioning Sidewalk devices in bulk with AWS IoT Core for Amazon Sidewalk.
- [Creating device profiles with factory support](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/sidewalk-provision-profile.html): Creating factory-supported device profiles for bulk provisioning Amazon Sidewalk devices.

### [Provisioning Sidewalk devices using import tasks](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/sidewalk-provision-bulk-import.html)

Use import tasks with AWS IoT Core for Amazon Sidewalk to provision Amazon Sidewalk devices in bulk.

- [Provision Sidewalk devices in bulk](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/sidewalk-bulk-provision-how.html): Provision Amazon Sidewalk devices in bulk using import tasks.
- [View import task and device onboarding status](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/sidewalk-bulk-provision-status.html): View status of import task and devices in the task.


## [Security](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/security.html)

### [Data protection](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in AWS IoT Wireless.

- [LoRaWAN data and transport security](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-lorawan-security.html): AWS IoT Core for LoRaWAN uses the following methods to secure the data and communication between LoRaWAN devices, gateways, and AWS IoT Core for LoRaWAN:

### [Identity and access management](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/security-iam.html)

How to authenticate requests and manage access your AWS IoT Wireless resources.

- [How AWS IoT Wireless works with IAM](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/security_iam_service-with-iam.html): Before you use IAM to manage access to AWS IoT Wireless, you should understand what IAM features are available to use with AWS IoT Wireless.
- [Identity-based policy examples](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/security_iam_id-based-policy-examples.html): By default, IAM users and roles don't have permission to create or modify AWS IoT Wireless resources.
- [AWS managed policies](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS IoT Wireless and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS IoT Wireless and IAM.
- [Infrastructure security and compliance validation](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/security-compliance-resiliency.html): Learn about the compliance scope, and how to prepare for disaster recovery, data resiliency, and isolation of network traffic.


## [Monitoring](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/monitoring-cloudwatch.html)

### [Configure logging](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/configure-logging.html)

Configure logging for AWS IoT Wireless to monitor resources.

- [Create logging role and policy](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/create-logging-role-policy.html): Create logging role and policy for configuring logging and monitoring AWS IoT Wireless resources.
- [Configure resource logging](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/configure-resource-logging.html): Create resource logging using the AWS IoT Wireless API to start monitoring resources.

### [Monitor using CloudWatch Logs](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/cloud-watch-logs.html)

How to monitor your AWS IoT Wireless resources using Amazon CloudWatch Logs and view log entries.

- [View log entries for wireless resources](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/cwl-format.html): How to monitor your AWS IoT Wireless resources using Amazon CloudWatch Logs and view log entries.
- [Use CloudWatch Insights to filter logs](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/cwl-insights.html): While you can use CloudWatch Logs to create filter expressions, we recommend that you use CloudWatch insights to more effectively create and use filter expressions depending on your application.


## [Event notifications](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-wireless-events.html)

- [Enable events for wireless resources](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-wireless-control-events.html): Enable events for AWS IoT Wireless resources to receive notifications.

### [Event notifications for wireless resources](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-wireless-events-notifications.html)

Receive event notifications for AWS IoT Wireless resources.

- [LoRaWAN join events](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-lorawan-join-events.html): Receive event notifications for LoRaWAN join events.
- [LoRaWAN gateway connection status events](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-lorawan-gateway-events.html): Receive event notifications for gateway connection status events.
- [Sidewalk device registration state events](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-sidewalk-device-events.html): Receive event notifications for device registation state events.
- [Sidewalk proximity events](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-sidewalk-proximity-events.html): Receive event notifications for Sidewalk proximity events.
- [Sidewalk message delivery status events](https://docs.aws.amazon.com/iot-wireless/latest/developerguide/iot-sidewalk-message-delivery-events.html): Receive event notifications for Sidewalk message delivery events.
