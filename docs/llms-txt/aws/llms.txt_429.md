# Source: https://docs.aws.amazon.com/ground-station/latest/ug/llms.txt

# AWS Ground Station User Guide

> Provides a conceptual overview of AWS Ground Station and includes instructions for using the various features, and managing satellite operations.

- [What is AWS Ground Station?](https://docs.aws.amazon.com/ground-station/latest/ug/what-is.html)
- [AWS Ground Station digital twin](https://docs.aws.amazon.com/ground-station/latest/ug/digital-twin.html)
- [Quotas and limits](https://docs.aws.amazon.com/ground-station/latest/ug/quotas-and-limits.html)
- [Service terms](https://docs.aws.amazon.com/ground-station/latest/ug/service-terms.html)
- [Document History](https://docs.aws.amazon.com/ground-station/latest/ug/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/ground-station/latest/ug/glossary.html)

## [How AWS Ground Station works](https://docs.aws.amazon.com/ground-station/latest/ug/how-it-works.html)

### [Understand AWS Ground Station Core components](https://docs.aws.amazon.com/ground-station/latest/ug/how-it-works.core.html)

AWS Ground Station core components

- [Mission Profiles](https://docs.aws.amazon.com/ground-station/latest/ug/how-it-works-mission-profile.html): Describes mission profiles
- [Configs](https://docs.aws.amazon.com/ground-station/latest/ug/how-it-works.config.html): Describes configs
- [Dataflow endpoint groups](https://docs.aws.amazon.com/ground-station/latest/ug/how-it-works.dataflow-endpoint-group.html): Describes dataflow endpoint groups
- [AWS Ground Station Agent](https://docs.aws.amazon.com/ground-station/latest/ug/how-it-works.gs-agent.html): The AWS Ground Station Agent and how it works.


## [Get started](https://docs.aws.amazon.com/ground-station/latest/ug/getting-started.html)

- [Onboard satellite](https://docs.aws.amazon.com/ground-station/latest/ug/getting-started.step1.html): Getting started
- [Plan your dataflow communication paths](https://docs.aws.amazon.com/ground-station/latest/ug/getting-started.step2.html): Getting started
- [Plan your telemetry](https://docs.aws.amazon.com/ground-station/latest/ug/getting-started.step2b.html): Getting started with telemetry
- [Create configs](https://docs.aws.amazon.com/ground-station/latest/ug/getting-started.step3.html): Getting started
- [Create mission profile](https://docs.aws.amazon.com/ground-station/latest/ug/getting-started.step4.html): Getting started
- [Understand next steps](https://docs.aws.amazon.com/ground-station/latest/ug/getting-started.next-steps.html): Next steps


## [AWS Ground Station Locations](https://docs.aws.amazon.com/ground-station/latest/ug/aws-ground-station-antenna-locations.html)

- [AWS Ground Station site masks](https://docs.aws.amazon.com/ground-station/latest/ug/locations.site-masks.html): Each AWS Ground Station antenna location has associated site masks.
- [AWS Ground Station Site Capabilities](https://docs.aws.amazon.com/ground-station/latest/ug/locations.capabilities.html): To simplify your experience, AWS Ground Station determines a common set of capabilities for an antenna type and then deploys multiple antenna to a ground station location.


## [Understand how AWS Ground Station uses ephemerides](https://docs.aws.amazon.com/ground-station/latest/ug/ephemeris.html)

- [Default ephemeris data](https://docs.aws.amazon.com/ground-station/latest/ug/default-ephemeris-data.html): By default, AWS Ground Station uses publicly available data from Space-Track, and no action is required to supply AWS Ground Station with these default ephemerides.

### [Provide custom ephemeris data](https://docs.aws.amazon.com/ground-station/latest/ug/providing-custom-ephemeris-data.html)

- [Provide TLE ephemeris data](https://docs.aws.amazon.com/ground-station/latest/ug/providing-tle-ephemeris-data.html)
- [Provide OEM ephemeris data](https://docs.aws.amazon.com/ground-station/latest/ug/providing-oem-ephemeris-data.html)
- [Provide azimuth elevation ephemeris data](https://docs.aws.amazon.com/ground-station/latest/ug/providing-azimuth-elevation-ephemeris-data.html)
- [Reserve contacts with custom ephemeris](https://docs.aws.amazon.com/ground-station/latest/ug/reserving-contacts-with-custom-ephemeris.html)
- [Understand which ephemeris is used](https://docs.aws.amazon.com/ground-station/latest/ug/which-ephemeris-is-used.html): Ephemerides have a priority, expiration time, and enabled flag.
- [Get the current ephemeris for a satellite](https://docs.aws.amazon.com/ground-station/latest/ug/getting-current-ephemeris.html): The current ephemeris in use by AWS Ground Station for a specific satellite can be retrieved by calling the GetSatellite or ListSatellites actions.
- [Revert to default ephemeris data](https://docs.aws.amazon.com/ground-station/latest/ug/reverting-to-default-ephemeris-data.html): When you upload custom ephemeris data it will override the default ephemerides AWS Ground Station uses for that particular satellite.


## [Work with dataflows](https://docs.aws.amazon.com/ground-station/latest/ug/dataflows.html)

- [Using cross-region data delivery](https://docs.aws.amazon.com/ground-station/latest/ug/dataflows.cross-region-data-delivery.html): Using cross-region data delivery.
- [Set up and configure Amazon S3](https://docs.aws.amazon.com/ground-station/latest/ug/dataflows.s3-configuration.html): You can utilize a Amazon S3 bucket to receive your downlink signals using AWS Ground Station.
- [Set up and configure Amazon VPC](https://docs.aws.amazon.com/ground-station/latest/ug/dataflows.vpc-configuration.html): A full guide to set up a VPC is beyond the scope of this guide.
- [Set up and configure Amazon EC2](https://docs.aws.amazon.com/ground-station/latest/ug/dataflows.ec2-configuration.html): Properly configuring your Amazon EC2 instance is required for synchronous delivery of VITA-49 Signal/IP data or VITA-49 Extension data/IP to be delivered via the AWS Ground Station Agent or a dataflow endpoint.


## [Work with telemetry](https://docs.aws.amazon.com/ground-station/latest/ug/telemetry.html)

- [Set up telemetry](https://docs.aws.amazon.com/ground-station/latest/ug/telemetry.setup.html): Configure telemetry for your satellite contacts
- [Understand telemetry data](https://docs.aws.amazon.com/ground-station/latest/ug/telemetry.understanding-data.html): Learn about telemetry data format and types


## [Work with contacts](https://docs.aws.amazon.com/ground-station/latest/ug/contacts.html)

- [Understand contact lifecycle](https://docs.aws.amazon.com/ground-station/latest/ug/contacts.lifecycle.html): Understanding the contact lifecycle can help you to automate and troubleshoot various problems while using AWS Ground Station.
- [Understand contact billing](https://docs.aws.amazon.com/ground-station/latest/ug/contacts.billing.html): Understanding how billing works when utilizing the AWS Ground Station service


## [Monitoring](https://docs.aws.amazon.com/ground-station/latest/ug/monitoring.html)

- [Automate with Events](https://docs.aws.amazon.com/ground-station/latest/ug/monitoring.automating-events.html): Automate AWS Ground Station with other AWS services by using events.
- [Log API Calls with CloudTrail](https://docs.aws.amazon.com/ground-station/latest/ug/monitoring.cloudtrail.html): Learn about logging AWS Ground Station with AWS CloudTrail.
- [View metrics with Amazon CloudWatch](https://docs.aws.amazon.com/ground-station/latest/ug/monitoring.metrics.html): Gather and analyze metrics with Amazon CloudWatch


## [Security](https://docs.aws.amazon.com/ground-station/latest/ug/security.html)

### [Identity and Access Management](https://docs.aws.amazon.com/ground-station/latest/ug/security-iam.html)

How to authenticate requests and manage access to your AWS Ground Station resources.

- [How AWS Ground Station works with IAM](https://docs.aws.amazon.com/ground-station/latest/ug/security_iam_service-with-iam.html): Before you use IAM to manage access to AWS Ground Station, learn what IAM features are available to use with AWS Ground Station.
- [Identity-based policy examples](https://docs.aws.amazon.com/ground-station/latest/ug/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify AWS Ground Station resources.
- [Troubleshooting](https://docs.aws.amazon.com/ground-station/latest/ug/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS Ground Station and IAM.
- [AWS managed policies](https://docs.aws.amazon.com/ground-station/latest/ug/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS Ground Station and recent changes to those policies.
- [Use service-linked roles](https://docs.aws.amazon.com/ground-station/latest/ug/using-service-linked-roles.html): How to use service-linked roles to give Ground Station access to resources in your AWS account.

### [Data encryption at rest for AWS Ground Station](https://docs.aws.amazon.com/ground-station/latest/ug/security.encryption-at-rest.html)

AWS Ground Station provides encryption by default to protect your sensitive data at rest using AWS owned encryption keys.

- [Encryption at rest for TLE and OEM ephemeris data](https://docs.aws.amazon.com/ground-station/latest/ug/security.encryption-at-rest-tle-oem.html)
- [Encryption at rest for azimuth elevation ephemeris](https://docs.aws.amazon.com/ground-station/latest/ug/security.encryption-at-rest-azimuth-elevation.html)
- [Data encryption during transit for AWS Ground Station](https://docs.aws.amazon.com/ground-station/latest/ug/security.encryption-during-transit.html): AWS Ground Station provides encryption by default to protect your sensitive data during transit.


## [Example mission profile configurations](https://docs.aws.amazon.com/ground-station/latest/ug/examples.html)

- [Public broadcast satellite utilizing Amazon S3 data delivery](https://docs.aws.amazon.com/ground-station/latest/ug/examples.pbs-to-s3.html): This example builds off the analysis done in the section of the user guide.
- [Public broadcast satellite utilizing a dataflow endpoint (narrowband)](https://docs.aws.amazon.com/ground-station/latest/ug/examples.pbs-data-dataflow-endpoint.html): This example builds off the analysis done in the section of the user guide.
- [Public broadcast satellite utilizing a dataflow endpoint (demodulated and decoded)](https://docs.aws.amazon.com/ground-station/latest/ug/examples.pbs-dataflow-endpoint-demod-decode.html): This example builds off the analysis done in the section of the user guide.
- [Public broadcast satellite utilizing AWS Ground Station Agent (wideband)](https://docs.aws.amazon.com/ground-station/latest/ug/examples.pbs-agent.html): This example builds off the analysis done in the section of the user guide.


## [Troubleshooting](https://docs.aws.amazon.com/ground-station/latest/ug/troubleshooting.html)

- [Troubleshoot contacts that deliver data to Amazon EC2](https://docs.aws.amazon.com/ground-station/latest/ug/troubleshooting-contact.html): If you are unable to successfully complete an AWS Ground Station contact, you'll need to verify that your Amazon EC2 instance is running, verify that your dataflow endpoint application is running, and verify that your dataflow endpoint application's stream is configured properly.
- [Troubleshoot FAILED contacts](https://docs.aws.amazon.com/ground-station/latest/ug/troubleshooting-failed-contacts.html): Troubleshooting FAILED contacts
- [Troubleshoot FAILED_TO_SCHEDULE contacts](https://docs.aws.amazon.com/ground-station/latest/ug/troubleshooting-failed-to-schedule-contacts.html): Troubleshooting FAILED_TO_SCHEDULE contacts
- [Troubleshoot DataflowEndpointGroups not in a HEALTHY state](https://docs.aws.amazon.com/ground-station/latest/ug/troubleshooting-dfeg.html): This section lists the reasons a dataflow endpoint group may not be in a HEALTHY state as well as the appropriate corrective action to take.
- [Troubleshoot invalid ephemerides](https://docs.aws.amazon.com/ground-station/latest/ug/troubleshooting-invalid-ephemerides.html): When you upload ephemeris data to AWS Ground Station, it goes through an asynchronous validation workflow.
- [Troubleshoot contacts that received no data](https://docs.aws.amazon.com/ground-station/latest/ug/troubleshooting-no-data-received.html): Troubleshooting contacts that received no data
- [Troubleshoot telemetry](https://docs.aws.amazon.com/ground-station/latest/ug/troubleshooting-telemetry.html): Resolve common telemetry issues
