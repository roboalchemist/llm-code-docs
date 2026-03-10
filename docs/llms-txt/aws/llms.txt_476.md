# Source: https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/llms.txt

# AWS IoT FleetWise Developer Guide

- [Get started](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-getting-started.html)
- [Ingest data](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/data-ingestion.html)
- [Configure network agnostic data collection](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/network-agnostic-data-collection.html)
- [AWS CLI and SDKs](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/sdk-cli.html)
- [Document history](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/doc-history.html)

## [What is AWS IoT FleetWise?](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/what-is-iotfleetwise.html)

- [Key concepts](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/how-iotfleetwise-works.html): Learn about the key components of AWS IoT FleetWise and how the service works.
- [Supported AWS Regions](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html): For a list of AWS Regions that support AWS IoT FleetWise, see AWS IoT FleetWise endpoints and quotas.


## [Set up AWS IoT FleetWise](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/setting-up.html)

- [Configure your settings](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/configure-settings.html): Learn how to configure settings for AWS IoT FleetWise.
- [Using IPv6 with AWS IoT FleetWise](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-ipv6-access.html): Using IPv6 and IPv4 to make requests to AWS IoT FleetWise endpoints.


## [Model vehicles](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/vehicle-modeling.html)

### [Signal catalogs](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/signal-catalogs.html)

Learn about how to create and manage signal catalogs, and how to add signals to signal catalogs.

- [Configure signals](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/define-signal.html): Learn how to configure branches, attributes, sensors, and actuators.
- [Create a signal catalog](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/create-signal-catalog.html): Create a signal catalog in the AWS CLI.
- [Import a signal catalog](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/import-signal.html): Import a signal catalog in the AWS IoT FleetWise console or API.
- [Update a signal catalog](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/update-signal-catalog.html): Update a signal catalog in the AWS CLI.
- [Delete a signal catalog](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/delete-signal-catalog.html): Delete a signal catalog in the AWS CLI.
- [Get signal catalog information](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/get-signal-catalog-information.html): Learn how to get signal catalog information.

### [Vehicle models](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/vehicle-models.html)

Learn about how to create and manage vehicle models.

- [Create a vehicle model](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/create-vehicle-model.html): Learn how to create a vehicle model.
- [Update a vehicle model](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/update-vehicle-model-cli.html): Update a vehicle model in the AWS CLI.
- [Delete a vehicle model](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/delete-vehicle-model.html): Delete a vehicle model in the AWS IoT FleetWise console or the AWS CLI.
- [Get vehicle model information](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/get-vehicle-model-information.html): Get information about a vehicle model in the AWS CLI.

### [Decoder manifests](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/decoder-manifests.html)

Learn how to create and manage decoder manifests in AWS IoT FleetWise.

- [Configure interfaces and signals](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/configure-network-interfaces-decoder-signals.html): Learn how to configure network interfaces and signal decoders.
- [Create a decoder manifest](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/create-decoder-manifest.html): Learn how to create a decoder manifest.
- [Update a decoder manifest](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/update-decoder-manifest.html): Learn how to update a decoder manifest in the AWS CLI.
- [Delete a decoder manifest](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/delete-decoder-manifest.html): Learn how to delete a decoder manifest in the AWS IoT FleetWise console or the AWS CLI.
- [Get decoder manifest information](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/get-decoder-manifest-information.html): Learn how to get information about a decoder manifest in the AWS CLI.


## [Manage vehicles](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/vehicles.html)

- [Provision vehicles](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/provision-vehicles.html): Learn about how vehicles created in AWS IoT FleetWise integrate with AWS IoT Core.
- [Reserved topics](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/reserved-topics.html): Topics reserved for use by AWS IoT FleetWise.
- [Create a vehicle](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/create-vehicle.html): Create a vehicle in AWS IoT FleetWise.
- [Create multiple vehicles](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/create-vehicles-cli.html): Learn how to create multiple vehicles at one time in AWS IoT FleetWise.
- [Update a vehicle](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/update-vehicle-cli.html): Update a vehicle in the AWS CLI.
- [Update multiple vehicles](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/update-vehicles-cli.html): Update multiple vehicles in the AWS CLI.
- [Delete a vehicle](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/delete-vehicle.html): You can delete a vehicle in the AWS IoT FleetWise console or AWS CLI.
- [Get vehicle information](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/get-vehicle-information-cli.html): Get information about a vehicle in the AWS CLI.


## [Manage fleets](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleets.html)

- [Create a fleet](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/create-fleet-cli.html): Learn how to use the CreateFleet API to create a fleet in AWS IoT FleetWise
- [Associate a vehicle with a fleet](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/associate-vehicle-cli.html): Learn how to associate a vehicle with a fleet in AWS IoT FleetWise.
- [Disassociate a vehicle from a fleet](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/disassociate-vehicle-cli.html): Learn how to disassociate a vehicle from a fleet in AWS IoT FleetWise.
- [Update a fleet](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/update-fleet-cli.html): Learn how to update a fleet in AWS IoT FleetWise.
- [Delete a fleet](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/delete-fleet-cli.html): Learn how to delete an AWS IoT FleetWise fleet.
- [Get fleet information](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/get-fleet-information-cli.html): Learn how to get information about an AWS IoT FleetWise fleet.


## [Manage data with campaigns](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/campaigns.html)

### [Create a campaign](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/create-campaign.html)

Learn how campaigns give Edge Agent for AWS IoT FleetWise software instructions on how to select, collect, and transfer data to the cloud.

- [Logical expressions for AWS IoT FleetWise campaigns](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/logical-expression.html): Learn how to write a logical expression for campaigns.
- [Update a campaign](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/update-campaign-cli.html): Update a campaign in the AWS CLI.
- [Delete a campaign](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/delete-campaign.html): Delete a campaign in the AWS IoT FleetWise console or the AWS CLI.
- [Get campaign information](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/get-campaign-information-cli.html): Get information about a campaign in the AWS CLI.

### [Store and forward](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/store-and-forward.html)

- [Create data partitions](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/create-campaign-data-partitions.html)
- [Upload campaign data](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/update-campaign-cli-data-partitions.html)
- [Upload data using AWS IoT Jobs](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/update-campaign-cli-data-partitions-jobs.html)

### [Collect diagnostic trouble code data](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/diagnostic-trouble-codes.html)

Learn how to collect diagnostic trouble code data using AWS IoT FleetWise.

- [Diagnostic trouble code keywords](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/dtc-keywords.html)
- [Create a data collection campaign for diagnostic trouble codes](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/dtc-data-collection.html): Learn how to create a data collection campaign for diagnostic trouble codes.
- [Diagnostic trouble code use cases](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/dtc-use-cases.html)
- [Visualize vehicle data](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/process-visualize-data.html): Use MQTT, Amazon Timestream or Amazon S3 to process AWS IoT FleetWise data.


## [Commands](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/remote-commands.html)

- [Commands concepts](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/remote-command-concepts-states.html)
- [Vehicles and commands](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/remote-command-vehicles.html)
- [Create and manage commands](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/create-manage-remote-command-cli.html): Create and manage a command using the AWS CLI.
- [Start and monitor command executions](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/send-monitor-remote-command-cli.html): Send a command using the AWS CLI and monitor the command run status.
- [Example: Using commands](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/remote-command-tutorial.html)
- [Command usage scenarios](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/remote-command-use-cases.html): Use cases and best practices for commands.


## [Last known state](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/last-known-state.html)

- [Create a state template](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/state-templates.html): State templates provide a mechanism for vehicle owners to track the state of their vehicles.
- [Update a state template](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/update-state-template.html): Update a state template in the AWS CLI.
- [Delete a state template](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/delete-state-template.html): Delete a state template in the AWS CLI.
- [Get state template information](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/get-state-template.html): Get information about state templates in the AWS CLI.

### [State template operations](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/state-template-api-operations.html)

- [Activate and deactivate state data collection](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/start-stop-data-ingestion.html): How to activate or deactivate data ingestion with a state template using the AWS CLI.
- [Fetch a vehicle state snapshot](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/on-demand-operations.html): The operations that are available for retrieving a vehicle state snapshot.
- [Process last known state vehicle data using MQTT messaging](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/process-last-known-state-vehicle-data.html)


## [Troubleshooting](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/troubleshooting.html)

- [Decoder manifest issues](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/troubleshoot-decoder-manifest.html): Learn how to troubleshoot decoder manifest issues in AWS IoT FleetWise.
- [Edge agent issues](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/trouebleshoot-edge-agent.html): Learn how to troubleshoot issues with Edge Agent for AWS IoT FleetWise software.
- [Store and forward issues](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/troubleshooting-campaign.html)


## [Security](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/security.html)

### [Data protection](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in AWS IoT FleetWise.

### [Data encryption in AWS IoT FleetWise](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/data-encryption.html)

Learn how the AWS shared responsibility model applies to data encryption in AWS IoT FleetWise.

- [Encryption at rest in AWS IoT FleetWise](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/encryption-at-rest.html): Learn how the AWS shared responsibility model applies to encryption at rest in AWS IoT FleetWise.
- [Key management in AWS IoT FleetWise](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/key-management.html): Learn how the AWS shared responsibility model applies to key management in AWS IoT FleetWise.
- [Controlling access](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/controlling-access.html): Control access to and from your AWS IoT FleetWise resources by using IAM.

### [Identity and Access Management](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/security-iam.html)

How to authenticate requests and manage access your AWS IoT FleetWise resources.

### [How AWS IoT FleetWise works with IAM](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/security_iam_service-with-iam.html)

Learn how AWS IoT FleetWise works with IAM.

- [Using service-linked roles](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/using-service-linked-roles.html): How to use service-linked roles to give AWS IoT FleetWise access to resources in your AWS account.
- [Identity-based policy examples](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/security_iam_id-based-policy-examples.html): Learn about identity-based policy examples in AWS IoT FleetWise.
- [Troubleshooting](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/security_iam_troubleshoot.html): Learn about troubleshooting identity and access issues in AWS IoT FleetWise.
- [API permissions reference](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/api-permissions-reference.html): Learn about the AWS IoT FleetWise actions and the AWS resources for which you can grant permissions.
- [Managed policy updates](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/managed-policy-updates.html): View details about updates to AWS managed policies for AWS IoT FleetWise since this service began tracking these changes.
- [Compliance validation](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS IoT FleetWise features for data resiliency.

### [Infrastructure security](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/infrastructure-security.html)

Learn how AWS IoT FleetWise isolates service traffic.

- [Connecting to AWS IoT FleetWise through an interface VPC endpoint](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/interface-vpc-endpoint.html): Access AWS IoT FleetWise by using an interface VPC endpoint.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/vulnerability-analysis-and-management.html): Learn how the AWS shared responsibility model applies to vulnerability analysis and management in AWS IoT FleetWise.
- [Security best practices](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/security-best-practices.html): Learn about security best practices for AWS IoT FleetWise.


## [Monitoring AWS IoT FleetWise](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/monitoring-overview.html)

- [Monitoring with CloudWatch](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/monitoring-cloudwatch.html): Learn how to monitor AWS IoT FleetWise with CloudWatch.

### [Monitor with CloudWatch Logs](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/monitoring-cloudwatch-logs.html)

Learn about monitoring AWS IoT FleetWise with Amazon CloudWatch Logs.

- [Configuring logging](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/logging-cw.html): Configure AWS IoT FleetWise logging to CloudWatch.

### [CloudTrail logs](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/logging-using-cloudtrail.html)

Learn about logging AWS IoT FleetWise with AWS CloudTrail.

- [Understand log file entries](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/understanding-iotfleetwise-entries.html): Learn how to understand AWS IoT FleetWise log file entries.
