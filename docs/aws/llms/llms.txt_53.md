# Source: https://docs.aws.amazon.com/Monitron/latest/user-guide/llms.txt

# Amazon Monitron User Guide

> Provides detailed information and instructions for getting started, working with, and managing Amazon Monitron.

- [What is Amazon Monitron?](https://docs.aws.amazon.com/Monitron/latest/user-guide/what-is-monitron.html)
- [Monitoring costs](https://docs.aws.amazon.com/Monitron/latest/user-guide/monitoring-costs.html)
- [App settings](https://docs.aws.amazon.com/Monitron/latest/user-guide/monitron-settings.html)
- [Troubleshooting](https://docs.aws.amazon.com/Monitron/latest/user-guide/troubleshooting.html)
- [Available devices](https://docs.aws.amazon.com/Monitron/latest/user-guide/hardware.html)
- [Quotas](https://docs.aws.amazon.com/Monitron/latest/user-guide/quotas.html)
- [Data Management and Privacy](https://docs.aws.amazon.com/Monitron/latest/user-guide/data-management-and-privacy.html)
- [Document history](https://docs.aws.amazon.com/Monitron/latest/user-guide/doc-history.html)

## [How Amazon Monitron works](https://docs.aws.amazon.com/Monitron/latest/user-guide/how-monitron-works.html)

- [Amazon Monitron workflow](https://docs.aws.amazon.com/Monitron/latest/user-guide/deployed-workflow.html): Learn how Amazon Monitron captures temperature and vibration data from your equipment to detect and report abnormalities.
- [Amazon Monitron concepts](https://docs.aws.amazon.com/Monitron/latest/user-guide/monitron-terminology.html): Learn key Amazon Monitron concepts and terminology.
- [Amazon Monitron components](https://docs.aws.amazon.com/Monitron/latest/user-guide/monitron-components.html): Amazon Monitron includes purpose-built sensors to capture vibration and temperature data, as well as gateways to automatically transfer data to the AWS Cloud.
- [Amazon Monitron alerts](https://docs.aws.amazon.com/Monitron/latest/user-guide/how-it-works-alerts.html): To track equipment health, the Amazon Monitron mobile app displays an icon for each asset, so you can see its condition at a glance.


## [Getting started](https://docs.aws.amazon.com/Monitron/latest/user-guide/gsg-getting-started.html)

### [Setting up a project](https://docs.aws.amazon.com/Monitron/latest/user-guide/step-1.html)

Your organization's IT manager will use these steps to learn how to set up a project for monitoring factory floor equipment with Amazon Monitron.

- [Step 1: Create an account](https://docs.aws.amazon.com/Monitron/latest/user-guide/ags-signup.html)
- [Step 2: Create a project](https://docs.aws.amazon.com/Monitron/latest/user-guide/gsg-projects.html): Now that you've signed in to the AWS Management Console, you can use the Amazon Monitron console to create your project.
- [Step 3: Create admin users](https://docs.aws.amazon.com/Monitron/latest/user-guide/ags-project-admin.html): Give access to one or more people in your organization (such as reliability managers) as admin users.
- [Step 4: (optional) Add Amazon Monitron users to your project](https://docs.aws.amazon.com/Monitron/latest/user-guide/gsg-sso.html): In addition to admin users, you can also add users who lack admin permissions.
- [Step 5: Invite users to your project](https://docs.aws.amazon.com/Monitron/latest/user-guide/gsg-invite.html): Invite the users you've added to your Amazon Monitron project.

### [Adding assets and installing devices](https://docs.aws.amazon.com/Monitron/latest/user-guide/step-2.html)

Install and set up gateways, sensors, and assets in Amazon Monitron.

- [Step 1: Add a Gateway](https://docs.aws.amazon.com/Monitron/latest/user-guide/gs-adding-gateway.html): In Amazon Monitron, sensors collect data from machines and pass it to gateways, which transmit the data to the AWS Cloud and thus to Amazon Monitron for analysis.
- [Step 2: Adding Assets](https://docs.aws.amazon.com/Monitron/latest/user-guide/gsg-assets.html): Learn how to add assets (machines) to a gateway to monitor temperature and vibration in Amazon Monitron.
- [Step 3: Attach Sensors](https://docs.aws.amazon.com/Monitron/latest/user-guide/gsg-sensors.html): Learn how to install sensors on your factory assets to monitor vibration and temperature with Amazon Monitron.
- [Step 4: Pairing Sensors to an Asset](https://docs.aws.amazon.com/Monitron/latest/user-guide/gs-adding-sensors.html): Each sensor that you pair to an asset has a designated position and is set to monitor a specific part of the asset.

### [Understanding warnings and alerts](https://docs.aws.amazon.com/Monitron/latest/user-guide/step-3.html)

Learn how factory technicians monitor machine conditions with Amazon Monitron.

- [Step 1: Understanding asset health](https://docs.aws.amazon.com/Monitron/latest/user-guide/gsg-asset-list.html): To monitor assets using the Amazon Monitron mobile app, start with the Assets list.
- [Step 2: Viewing asset conditions](https://docs.aws.amazon.com/Monitron/latest/user-guide/gsg-monitoring.html): Viewing assets is more than simply understanding the icons that show the asset and position health status.
- [Step 3: Viewing and acknowledging a machine abnormality](https://docs.aws.amazon.com/Monitron/latest/user-guide/gsg-acknowledging.html): The longer Amazon Monitron monitors a position, the more it fine-tunes its baseline and increases its accuracy.
- [Step 4: Resolving a machine abnormality](https://docs.aws.amazon.com/Monitron/latest/user-guide/gs-resolving-anomalies.html): Resolving an abnormality returns the sensor to healthy status and provides information about the issue to Amazon Monitron so it can better determine when a failure might occur in the future.
- [Step 5: Muting and unmuting alerts](https://docs.aws.amazon.com/Monitron/latest/user-guide/gs-muting-alerts.html): You can choose to mute and unmute alerts (alarms and warnings) for a position.


## [Projects](https://docs.aws.amazon.com/Monitron/latest/user-guide/projects-chapter.html)

- [Creating a project](https://docs.aws.amazon.com/Monitron/latest/user-guide/mp-creating-project.html): Learn how to create a project in Amazon Monitron.
- [Using tags with your project](https://docs.aws.amazon.com/Monitron/latest/user-guide/tagging.html): Learn how to use tags to organize your Amazon Monitron project.
- [Updating a project](https://docs.aws.amazon.com/Monitron/latest/user-guide/mp-updating-project.html): Learn how to update an Amazon Monitron project.
- [Switching between projects](https://docs.aws.amazon.com/Monitron/latest/user-guide/monitron-switch-projects.html): Learn how to switch between an Amazon Monitron project.
- [Deleting a project](https://docs.aws.amazon.com/Monitron/latest/user-guide/mp-delete-project.html): Learn how to delete an Amazon Monitron project.
- [Additional project tasks](https://docs.aws.amazon.com/Monitron/latest/user-guide/mp-project-tasks.html): Two common project-related tasks that you might frequently encounter are listing all of your projects and retrieving the details on one specific project.


## [Sites](https://docs.aws.amazon.com/Monitron/latest/user-guide/site-management-chapterSM.html)

- [Organizing a project into sites](https://docs.aws.amazon.com/Monitron/latest/user-guide/site-organization.html): You can organize a project into sites based on your business needs.
- [Controlling access to projects and sites](https://docs.aws.amazon.com/Monitron/latest/user-guide/site-permissions.html): To give a user access to all of the resources in a project, including those in all of the project's sites, you add the user to the project.
- [Creating a site](https://docs.aws.amazon.com/Monitron/latest/user-guide/SM-creating-site.html): Create a site to use with Amazon Monitron using the mobile or web app.
- [Changing a site name](https://docs.aws.amazon.com/Monitron/latest/user-guide/SM-editing-site.html): Change the name of a site in Amazon Monitron using the mobile or web app.
- [Deleting a site](https://docs.aws.amazon.com/Monitron/latest/user-guide/SM-deleting-site.html): Delete a site in Amazon Monitron using the web or mobile app.
- [Navigating between projects and sites in the mobile app](https://docs.aws.amazon.com/Monitron/latest/user-guide/SM-working-project-and-site.html): Switch between projects and sites in Amazon Monitron.


## [Gateways](https://docs.aws.amazon.com/Monitron/latest/user-guide/gateways.html)

### [Ethernet gateways](https://docs.aws.amazon.com/Monitron/latest/user-guide/setting-up-ethernet-gateways.html)

The Amazon Monitron Ethernet Gateway comes equipped with an RJ-45 socket, so you can connect it to your Ethernet network using a Cat 5e or Cat 6 Ethernet cable.

- [Reading the LED lights on an Ethernet gateway](https://docs.aws.amazon.com/Monitron/latest/user-guide/reading-LED-lights-ethernet.html): The LED lights on the top of your Amazon Monitron Ethernet Gateway indicate the status of the gateway.
- [Placing and installing an Ethernet gateway](https://docs.aws.amazon.com/Monitron/latest/user-guide/installing-gateway-ethernet.html): Unlike sensors, an Ethernet gateway doesn't need to be attached to the machines that are being monitored.
- [Commissioning an Ethernet gateway](https://docs.aws.amazon.com/Monitron/latest/user-guide/adding-gateway-ethernet.html): When your gateway is mounted in your factory, you will need access to the Amazon Monitron mobile app to commission it.
- [Troubleshooting Ethernet gateway detection](https://docs.aws.amazon.com/Monitron/latest/user-guide/troubleshooting-gateway-detection-ethernet.html): When you add a gateway to your project or site, as soon as you choose Add Gateway, the Amazon Monitron mobile app starts scanning for the gateway.
- [](https://docs.aws.amazon.com/Monitron/latest/user-guide/troubleshooting-Bluetooth-pairing-ethernet.html): You may find yourself attempting to pair your iOS mobile device with a gateway that it has already paired with.
- [Resetting the Ethernet gateway to factory settings](https://docs.aws.amazon.com/Monitron/latest/user-guide/commissioning-button-ethernet.html): If you re-use a gateway that was deleted from Amazon Monitron, use the commissioning button to reset the gateway to factory settings.
- [Viewing the list of gateways](https://docs.aws.amazon.com/Monitron/latest/user-guide/ethernet-gateway-list.html): This page describes how to list your gateways in the Amazon Monitron app.
- [Viewing Ethernet gateway details](https://docs.aws.amazon.com/Monitron/latest/user-guide/viewing-gateway-details-ethernet.html): You can view gateway details on your mobile or web app.
- [Editing Ethernet gateway name](https://docs.aws.amazon.com/Monitron/latest/user-guide/editing-gateway-ethernet.html): You can change the display name for your Ethernet gateway to find it faster.
- [Deleting an Ethernet gateway](https://docs.aws.amazon.com/Monitron/latest/user-guide/deleting-gateway-ethernet.html): Sensors need a gateway to relay their data to the AWS Cloud.
- [Retrieving MAC address details](https://docs.aws.amazon.com/Monitron/latest/user-guide/mac-address-ethernet-gateway.html): To retrieve your Amazon Monitron gateway's Media Access Control (MAC) address, you can scan the QR code on the gateway device with your mobile phone.

### [Wi-Fi gateways](https://docs.aws.amazon.com/Monitron/latest/user-guide/setting-up-Wi-Fi-gateways.html)

This topic explains how to install your Wi-Fi gateway.

- [Reading the LED lights on a Wi-Fi gateway](https://docs.aws.amazon.com/Monitron/latest/user-guide/LED.html): Learn how to interpret the LED light sequences on an Amazon Monitron gateway.
- [Placing and installing a Wi-Fi gateway](https://docs.aws.amazon.com/Monitron/latest/user-guide/installing-gateway.html): Unlike sensors, a Wi-Fi gateway doesn't need to be attached to the machines that are being monitored.
- [Commissioning a Wi-Fi gateway](https://docs.aws.amazon.com/Monitron/latest/user-guide/adding-gateway-Wi-Fi.html): When your gateway is mounted in your factory, you will need access to the Amazon Monitron mobile app to commission it.
- [Troubleshooting Wi-Fi gateway detection](https://docs.aws.amazon.com/Monitron/latest/user-guide/gateway-failure-Wi-Fi.html): If the Amazon Monitron mobile app doesn't detect your gateway, use these steps to troubleshoot.
- [Troubleshooting Bluetooth pairing](https://docs.aws.amazon.com/Monitron/latest/user-guide/troubleshooting-Bluetooth-pairing-wireless.html): You may find yourself attempting to pair your iOS mobile device with a gateway that it has already been paired with.
- [Resetting the Wi-Fi gateway to factory settings](https://docs.aws.amazon.com/Monitron/latest/user-guide/commissioning-button-Wi-Fi.html): If you reuse a gateway that was deleted from Amazon Monitron, you use the commissioning button to reset the gateway to factory settings.
- [Viewing the list of gateways](https://docs.aws.amazon.com/Monitron/latest/user-guide/wi-fi-gateway-list.html): This page describes how to list your Wi-Fi gateaways in the web or mobile app.
- [Viewing Wi-Fi gateway details](https://docs.aws.amazon.com/Monitron/latest/user-guide/viewing-gateway-details-wifi.html): You can view gateway details on your mobile or web app.
- [Editing Wi-Fi gateway name](https://docs.aws.amazon.com/Monitron/latest/user-guide/editing-gateway-wifi.html): You can change the display name for your Wi-Fi gateway to find it faster.
- [Deleting a Wi-Fi gateway](https://docs.aws.amazon.com/Monitron/latest/user-guide/deleting-gateway-Wi-Fi.html): Sensors need a gateway to relay their data to the AWS Cloud.
- [Retrieving MAC address details](https://docs.aws.amazon.com/Monitron/latest/user-guide/mac-address-wifi-gateway.html): To retrieve your Amazon Monitron gateway's Media Access Control (MAC) address, you can scan the QR code on the gateway device with your mobile phone.


## [Assets](https://docs.aws.amazon.com/Monitron/latest/user-guide/assets-chapter.html)

- [Creating asset classes](https://docs.aws.amazon.com/Monitron/latest/user-guide/custom-asset-class.html): Amazon Monitron offers four default machine classes based on ISO 20816 Standards.
- [Managing assets](https://docs.aws.amazon.com/Monitron/latest/user-guide/as-assets.html): View, list, and manage your Amazon Monitron assets.
- [Viewing the list of assets](https://docs.aws.amazon.com/Monitron/latest/user-guide/asset-list.html)
- [Adding an asset](https://docs.aws.amazon.com/Monitron/latest/user-guide/as-add-assets.html): Add an asset to use with Amazon Monitron.
- [Changing an asset name](https://docs.aws.amazon.com/Monitron/latest/user-guide/as-edit-assets.html): Change the name of an asset that you use with Amazon Monitron.
- [Moving an asset](https://docs.aws.amazon.com/Monitron/latest/user-guide/moving-assets.html): Assets in a project can be grouped under various sites.
- [Deleting an asset](https://docs.aws.amazon.com/Monitron/latest/user-guide/as-delete-assets.html): Deleting an asset removes all associated sensors and their positions, in addition to any historical data associated with them.


## [Sensors](https://docs.aws.amazon.com/Monitron/latest/user-guide/as-sensor-positions1.html)

- [Positioning a sensor](https://docs.aws.amazon.com/Monitron/latest/user-guide/as-where-sensors.html): To detect abnormalities in machine components, mount sensors in all locations where temperature and vibrations can be measured effectively.
- [Mounting a sensor](https://docs.aws.amazon.com/Monitron/latest/user-guide/as-how-sensors.html): Mount a sensor with Amazon Monitron using the proper adhesive.
- [Adding a sensor position](https://docs.aws.amazon.com/Monitron/latest/user-guide/adding-position.html): Adding an asset position in Amazon Monitron.
- [Pairing a sensor to an asset](https://docs.aws.amazon.com/Monitron/latest/user-guide/as-add-sensors.html): Pair a sensor to an asset with Amazon Monitron.
- [Renaming a sensor position](https://docs.aws.amazon.com/Monitron/latest/user-guide/as-edit-sensorposition.html): Change the name of a sensor position with Amazon Monitron.
- [Editing machine class](https://docs.aws.amazon.com/Monitron/latest/user-guide/edit-sensor-position.html): Edit the name and machine class of a Amazon Monitron sensor.
- [Deleting a sensor](https://docs.aws.amazon.com/Monitron/latest/user-guide/as-delete-sensor.html): Delete a sensor with Amazon Monitron.
- [Deleting a sensor position](https://docs.aws.amazon.com/Monitron/latest/user-guide/as-delete-sensorposition.html): Deleting a sensor position removes that data collection point from the asset.
- [Understanding sensor details](https://docs.aws.amazon.com/Monitron/latest/user-guide/as-view-sensor-details.html): Get information about a sensor in Amazon Monitron, including the sensor ID, sensor status, the date the sensor was last commissioned, the date the sensor was last measured, the last gateway the sensor was connected to, the current signal strength of the last gateway the sensor was connected to, and the sensor type.
- [Identifying sensor position](https://docs.aws.amazon.com/Monitron/latest/user-guide/identify-sensor-position.html): Use the mobile app to find sensors in the factory or shop floor without searching through your asset list.
- [Ex-rated sensors](https://docs.aws.amazon.com/Monitron/latest/user-guide/ex-rated-sensors.html)


## [Measurements and machine abnormalities](https://docs.aws.amazon.com/Monitron/latest/user-guide/anom-monitoring-chapter.html)

- [Choosing your measurement viewing platform](https://docs.aws.amazon.com/Monitron/latest/user-guide/platform-chapter.html): Learn about the difference between the Amazon Monitron mobile app and the Amazon Monitron web app.
- [Viewing sensor measurements](https://docs.aws.amazon.com/Monitron/latest/user-guide/view-sensor-measurement.html): You can choose to view your sensor measurement data in two chart formats: scatter plot and line plot.
- [Understanding sensor measurements](https://docs.aws.amazon.com/Monitron/latest/user-guide/anom-sensor-measure.html): When a sensor is initially paired to an asset, Amazon Monitron will learn from the vibration and temperature data collected from the equipment, establishing a baseline to determine what is "normal" for that asset.
- [Understanding asset status](https://docs.aws.amazon.com/Monitron/latest/user-guide/anom-monitor-assets.html): When a sensor detects a machine abnormality, the status of the asset changes.
- [Acknowledging a machine abnormality](https://docs.aws.amazon.com/Monitron/latest/user-guide/anom-acknowledge-anom.html): After receiving a notification, the admin user or technician must acknowledge it.
- [Resolving an abnormality](https://docs.aws.amazon.com/Monitron/latest/user-guide/anom-resolve-anom.html): After an abnormality has occurred and been acknowledged, it must be addressed.
- [Taking a one-time measurement](https://docs.aws.amazon.com/Monitron/latest/user-guide/anom-take-measure.html): In addition to viewing the measurements that a sensor normally makes, you can take a one-time measurement with a sensor at any time.


## [Managing users](https://docs.aws.amazon.com/Monitron/latest/user-guide/user-management.html)

### [Managing admin users](https://docs.aws.amazon.com/Monitron/latest/user-guide/user-management-chapter.html)

Learn how to add and remove admin users to your Amazon Monitron projects.

- [User directory setup](https://docs.aws.amazon.com/Monitron/latest/user-guide/mu-adding-user.html): Learn how to set up the Amazon Monitron user directory.
- [Adding users as an admin](https://docs.aws.amazon.com/Monitron/latest/user-guide/adding-users-as-admin.html): Learn how to add users as an Amazon Monitron admin user.
- [Managing users as an admin user](https://docs.aws.amazon.com/Monitron/latest/user-guide/viewing-users-as-admin.html): Viewing user details Amazon Monitron admin user.
- [Removing an admin user](https://docs.aws.amazon.com/Monitron/latest/user-guide/mu-remove-project-admin.html): Learn how to remove an Amazon Monitron admin user.
- [Sending an email invitation](https://docs.aws.amazon.com/Monitron/latest/user-guide/resending-email.html): When you add a user to an Amazon Monitron project or site, you send them an email and invite them to download and log in to the Amazon Monitron mobile or web app.

### [Managing non-admin users](https://docs.aws.amazon.com/Monitron/latest/user-guide/non-admin-user-management-chapter.html)

Learn how to add and remove non-admin users to your Amazon Monitron projects.

- [Displaying a list of users](https://docs.aws.amazon.com/Monitron/latest/user-guide/display-user-list.html): As an admin, you can use the list of users to manage users in the Amazon Monitron app.
- [Adding a user](https://docs.aws.amazon.com/Monitron/latest/user-guide/adding-user.html): When you add a new user, the role you choose determines the permissions that user has.
- [Changing a user role](https://docs.aws.amazon.com/Monitron/latest/user-guide/editing-user-role.html): You can change a user's role, but not a user's name.
- [Removing a user](https://docs.aws.amazon.com/Monitron/latest/user-guide/deleting-user.html): Removing a user removes their permissions to access the site or project.


## [Networking](https://docs.aws.amazon.com/Monitron/latest/user-guide/networking-chapter.html)

- [Networking with your mobile device](https://docs.aws.amazon.com/Monitron/latest/user-guide/network-mobile.html): From a networking perspective, the process of provisioning sensors or gateways goes like this.
- [Securing your network](https://docs.aws.amazon.com/Monitron/latest/user-guide/network-secure.html): In order to allow your Amazon Monitron gateways to send data back to AWS, you should allow the following with regard to your local network traffic:


## [Accessing your data](https://docs.aws.amazon.com/Monitron/latest/user-guide/access-data.html)

### [Exporting your data to Amazon S3](https://docs.aws.amazon.com/Monitron/latest/user-guide/data-download-monitron.html)

Download your Amazon Monitron sensor data for use in another application

- [Prerequisites](https://docs.aws.amazon.com/Monitron/latest/user-guide/exporting-data-procedure.html): To successfully export your Amazon Monitron data, the following prerequisites must be met.
- [Exporting your data with CloudFormation (recommended option)](https://docs.aws.amazon.com/Monitron/latest/user-guide/onetime-download-cflink.html)
- [Exporting your data with the console](https://docs.aws.amazon.com/Monitron/latest/user-guide/onetime-download-console.html)
- [Exporting your data with CloudShell](https://docs.aws.amazon.com/Monitron/latest/user-guide/export-shell.html)

### [Exporting your data with Kinesis v1](https://docs.aws.amazon.com/Monitron/latest/user-guide/monitron-kinesis-export.html)

Export your Amazon Monitron with Kinesis

- [Monitoring with Amazon CloudWatch Logs](https://docs.aws.amazon.com/Monitron/latest/user-guide/data-export-cloudwatch-logs.html): You can monitor Amazon Monitron live data export using Amazon CloudWatch Logs.
- [Storing exported data in Amazon S3](https://docs.aws.amazon.com/Monitron/latest/user-guide/kinesis-store-S3.html)
- [Processing data with Lambda](https://docs.aws.amazon.com/Monitron/latest/user-guide/data-export-lambda.html)
- [Understanding the v1 data export schema](https://docs.aws.amazon.com/Monitron/latest/user-guide/data-export-schema.html)

### [Exporting your data with Kinesis v2](https://docs.aws.amazon.com/Monitron/latest/user-guide/monitron-kinesis-export-v2.html)

Export your Amazon Monitron with Kinesis

- [Monitoring with Amazon CloudWatch Logs](https://docs.aws.amazon.com/Monitron/latest/user-guide/data-export-cloudwatch-logs-v2.html): You can monitor Amazon Monitron live data export using Amazon CloudWatch Logs.
- [Storing exported data in Amazon S3](https://docs.aws.amazon.com/Monitron/latest/user-guide/kinesis-store-S3-v2.html): If you want to store your exported data in Amazon S3, use the following procedure.
- [Processing data with Lambda](https://docs.aws.amazon.com/Monitron/latest/user-guide/data-export-lambda-v2.html)
- [Understanding the v2 data export schema](https://docs.aws.amazon.com/Monitron/latest/user-guide/data-export-schema-v2.html): Each measurement data, its corresponding inference result, gateway connect/disconnect, and sensor connect/disconnect events are exported as one Kinesis data stream record in JSON format.
- [Migration from Kinesis v1 to v2](https://docs.aws.amazon.com/Monitron/latest/user-guide/migration-from-v1-to-v2.html): If you are currently using the v1 data schema, you may already be sending data to Amazon S3, or further processing the data stream payload with Lambda.


## [Logging actions with AWS CloudTrail](https://docs.aws.amazon.com/Monitron/latest/user-guide/logging-using-cloudtrail.html)

- [Amazon Monitron information in CloudTrail](https://docs.aws.amazon.com/Monitron/latest/user-guide/service-name-info-in-cloudtrail.html): CloudTrail is enabled for your AWS users when you create your account.
- [Example: Amazon Monitron log file entries](https://docs.aws.amazon.com/Monitron/latest/user-guide/understanding-service-name-entries.html): A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify.


## [Security](https://docs.aws.amazon.com/Monitron/latest/user-guide/security.html)

### [Data Protection](https://docs.aws.amazon.com/Monitron/latest/user-guide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Monitron.

- [Data at rest](https://docs.aws.amazon.com/Monitron/latest/user-guide/data-at-rest.html): Your data is encrypted at rest in the cloud using one of two types of keys through AWS Key Management Service (AWS KMS).
- [Data in transit](https://docs.aws.amazon.com/Monitron/latest/user-guide/data-in-transit.html): Amazon Monitron uses TLS (Transport Layer Security) to encrypt data that is transferred between your sensors and Amazon Monitron.
- [AWS KMS and Data Encryption](https://docs.aws.amazon.com/Monitron/latest/user-guide/kms-data-encrypt.html): Amazon Monitron encrypts your data and project information using one of two types of keys through AWS Key Management Service (AWS KMS).

### [Identity and Access Management](https://docs.aws.amazon.com/Monitron/latest/user-guide/security-iam.html)

Learn how to authenticate requests and manage access to your Amazon Monitron resources.

- [Audience](https://docs.aws.amazon.com/Monitron/latest/user-guide/security_iam_audience.html): How you use AWS Identity and Access Management (IAM) differs based on your role:

### [Authenticating with Identities](https://docs.aws.amazon.com/Monitron/latest/user-guide/security_iam_authentication.html)

Authentication is how you sign in to AWS using your identity credentials.

- [AWS account root user](https://docs.aws.amazon.com/Monitron/latest/user-guide/security_iam_authentication-rootuser.html): When you create an AWS account, you begin with one sign-in identity called the AWS account root user that has complete access to all AWS services and resources.
- [IAM users and Groups](https://docs.aws.amazon.com/Monitron/latest/user-guide/security_iam_authentication-iamuser.html): An IAM user is an identity with specific permissions for a single person or application.
- [IAM Roles](https://docs.aws.amazon.com/Monitron/latest/user-guide/security_iam_authentication-iamrole.html): An IAM role is an identity with specific permissions that provides temporary credentials.

### [Managing Access Using Policies](https://docs.aws.amazon.com/Monitron/latest/user-guide/security_iam_access-manage.html)

You control access in AWS by creating policies and attaching them to AWS identities or resources.

- [Identity-Based Policies](https://docs.aws.amazon.com/Monitron/latest/user-guide/security_iam_access-manage-id-based-policies.html): Identity-based policies are JSON permissions policy documents that you attach to an identity (user, group, or role).
- [Other Policy Types](https://docs.aws.amazon.com/Monitron/latest/user-guide/security_iam_access-manage-other-policies.html): AWS supports additional policy types that can set the maximum permissions granted by more common policy types:
- [Multiple Policy Types](https://docs.aws.amazon.com/Monitron/latest/user-guide/security_iam_access-manage-multiple-policies.html): When multiple types of policies apply to a request, the resulting permissions are more complicated to understand.
- [How Amazon Monitron Works with IAM](https://docs.aws.amazon.com/Monitron/latest/user-guide/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon Monitron, you should understand what IAM features are available to use with Amazon Monitron.

### [Using service-linked roles](https://docs.aws.amazon.com/Monitron/latest/user-guide/using-service-linked-roles.html)

How to use service-linked roles to give Amazon Monitron access to resources in your AWS account.

- [Service-linked role permissions for Amazon Monitron](https://docs.aws.amazon.com/Monitron/latest/user-guide/slr-permissions.html): Amazon Monitron uses the service-linked role named AWSServiceRoleForMonitron[_{SUFFIX}] â Amazon Monitron uses AWSServiceRoleForMonitron to access other AWS services, including Cloudwatch Logs, Kinesis Data Streams, KMS keys, and SSO.
- [Creating a service-linked role for Amazon Monitron](https://docs.aws.amazon.com/Monitron/latest/user-guide/create-slr.html): You don't need to manually create a service-linked role.
- [Editing a service-linked role for Amazon Monitron](https://docs.aws.amazon.com/Monitron/latest/user-guide/edit-slr.html): Amazon Monitron does not allow you to edit the AWSServiceRoleForMonitron[_{SUFFIX}] service-linked role.
- [Deleting a service-linked role for Amazon Monitron](https://docs.aws.amazon.com/Monitron/latest/user-guide/delete-slr.html): You don't need to manually delete the AWSServiceRoleForMonitron[_{SUFFIX}] role.
- [Supported regions for Amazon Monitron service-linked roles](https://docs.aws.amazon.com/Monitron/latest/user-guide/slr-regions.html): Amazon Monitron supports using service-linked roles in all of the regions where the service is available.
- [AWS managed policies for Amazon Monitron](https://docs.aws.amazon.com/Monitron/latest/user-guide/monitron-managed-policies.html): You can attach AmazonMonitronFullAccess to your IAM entities.
- [Amazon Monitron updates to AWS managed policies](https://docs.aws.amazon.com/Monitron/latest/user-guide/managed-policy-updates.html): View details about updates to AWS managed policies for Amazon Monitron since this service began tracking these changes.
- [Logging and Monitoring](https://docs.aws.amazon.com/Monitron/latest/user-guide/monitron-logging.html): Monitoring is an important part of maintaining the reliability, availability, and performance of your Amazon Monitron applications.
- [Compliance Validation](https://docs.aws.amazon.com/Monitron/latest/user-guide/monitron-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Infrastructure Security](https://docs.aws.amazon.com/Monitron/latest/user-guide/infrastructure-security.html): Learn how Amazon Monitron isolates service traffic.
- [Security Best Practices for Amazon Monitron](https://docs.aws.amazon.com/Monitron/latest/user-guide/security-best-practices.html): Security Best Practices for Amazon Monitron
