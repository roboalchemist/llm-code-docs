# Source: https://docs.aws.amazon.com/network-firewall/latest/developerguide/llms.txt

# AWS Network Firewall Developer Guide

> Describes how to use AWS Network Firewall, the Amazon Virtual Private Cloud firewall service.

- [What is Network Firewall?](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)
- [Setting up](https://docs.aws.amazon.com/network-firewall/latest/developerguide/setting-up.html)
- [Getting started with Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/getting-started.html)
- [Sharing Network Firewall resources](https://docs.aws.amazon.com/network-firewall/latest/developerguide/sharing.html)
- [Resource tagging](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tagging.html)
- [Quotas](https://docs.aws.amazon.com/network-firewall/latest/developerguide/quotas.html)
- [Resources](https://docs.aws.amazon.com/network-firewall/latest/developerguide/resources.html)
- [Document history](https://docs.aws.amazon.com/network-firewall/latest/developerguide/document-history.html)

## [How Network Firewall works](https://docs.aws.amazon.com/network-firewall/latest/developerguide/how-it-works.html)

- [Firewall components](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-components.html): Learn about Network Firewall firewall components.
- [High-level steps for implementation](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-high-level-steps.html): Learn the high-level steps to add a firewall to your VPC.

### [Firewall behavior](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-behavior.html)

Learn about the Network Firewall stateless and stateful rules engines and the steps in packet filtering.

- [Stateless and stateful rules engines](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-rules-engines.html): Learn about the Network Firewall stateless and stateful rules engines.
- [How Network Firewall filters network traffic](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-policy-processing.html): Learn about the process that Network Firewall and the rules engines follow to filter network traffic in your VPC.
- [Route table configurations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/route-tables.html): Use Amazon VPC routing to modify your route table configurations to send network traffic through your Network Firewall firewall endpoints.
- [Avoiding asymmetric routing with AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/asymmetric-routing.html): Understand how to avoid asymmetric routing within Network Firewall workflows

### [Architecture and routing examples](https://docs.aws.amazon.com/network-firewall/latest/developerguide/architectures.html)

See common architectures for Network Firewall with route table examples.

- [Single zone internet gateway](https://docs.aws.amazon.com/network-firewall/latest/developerguide/arch-single-zone-igw.html): See a simple VPC configuration using an internet gateway and Network Firewall.
- [Multi zone internet gateway](https://docs.aws.amazon.com/network-firewall/latest/developerguide/arch-two-zone-igw.html): See a simple multi-zone VPC configuration using an internet gateway and Network Firewall.
- [Internet gateway and NAT gateway](https://docs.aws.amazon.com/network-firewall/latest/developerguide/arch-igw-ngw.html): See a NAT gateway and internet gateway configuration with Network Firewall.


## [Configuring your VPC](https://docs.aws.amazon.com/network-firewall/latest/developerguide/vpc-config.html)

- [VPC subnets](https://docs.aws.amazon.com/network-firewall/latest/developerguide/vpc-config-subnets.html): When you associate a firewall to your VPC, you must provide a subnet for each Availability Zone where you want to place a firewall endpoint to filter traffic.
- [VPC route tables](https://docs.aws.amazon.com/network-firewall/latest/developerguide/vpc-config-route-tables.html): After you create your firewall, you reroute your VPC network traffic through the firewall endpoints so they can start filtering traffic.
- [Transit gateway attachments](https://docs.aws.amazon.com/network-firewall/latest/developerguide/vpc-config-tgw-multi-az.html): This section applies to the use of Network Firewall with a transit gateway in multiple Availability Zones where the firewall endpoints might reside in different Availability Zones than the subnets whose traffic they're filtering.


## [Firewalls and firewall endpoints](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewalls.html)

- [Considerations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-and-firewall-endpoints-considerations.html): Before you create, update, or delete a firewall and its endpoints in AWS Network Firewall, review these considerations.
- [Firewall settings](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-settings.html): See the configuration settings for a Network Firewall firewall.
- [Firewall and VPC endpoint association owner capabilities](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-owners-and-vpc-endpoint-association-owners.html): Compare the capabilities and responsibilities of firewall owners versus VPC endpoint association owners.

### [Managing a firewall and firewall endpoints](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-managing.html)

Create, update, and delete your AWS Network Firewall firewall and its endpoints.

- [Creating a firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/creating-firewall.html): Create a firewall
- [Creating a VPC endpoint association](https://docs.aws.amazon.com/network-firewall/latest/developerguide/creating-vpc-endpoint-association.html): Create a VPC endpoint association to establish additional firewall endpoints for a firewall that you own or that has been shared with you.
- [Updating a AWS Network Firewall firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-updating.html): Update your firewall.
- [Deleting a firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/deleting-firewall.html): Delete a firewall that you own.
- [Deleting a VPC endpoint association](https://docs.aws.amazon.com/network-firewall/latest/developerguide/deleting-vpc-endpoint-association.html): Delete a VPC endpoint association from a firewall.

### [Transit gateway-attached firewalls](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tgw-firewall.html)

The AWS Network Firewall integration with AWS Transit Gateway lets you create and centrally manage firewall protective coverage without needing to provision multiple firewall endpoints.

- [Considerations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tgw-firewall-considerations.html): Before you create or use a transit gateway-attached firewall, consider the following points.
- [Create a transit gateway-attached firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/create-tgw-firewall.html): Create a transit gateway-attached firewall from a transit gateway that has been shared with your account through AWS RAM.
- [Working with transit gateway-attached firewalls](https://docs.aws.amazon.com/network-firewall/latest/developerguide/working-with-tgw-firewalls.html): After you accept a shared transit gateway attachment, the firewall you create appears in the Firewalls page of the Network Firewall console with one of the following statuses, depending on what state it is in:

### [Flow operations in your firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-flow-operations.html)

Learn how to use flow operations to flush or capture traffic monitored in your firewall's state table for enhanced network security management.

- [Capturing firewall flows](https://docs.aws.amazon.com/network-firewall/latest/developerguide/flow-operations-capture.html): With flow capture operations in Network Firewall, you can view information about active traffic flows that are tracked in your firewall's state table.
- [Flushing traffic flows](https://docs.aws.amazon.com/network-firewall/latest/developerguide/flow-operations-flush.html): Flow flush operations give you greater control over how your firewall rules are applied to network traffic.
- [Viewing flow operations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/flow-operations-view.html): You can view the history of operations in your firewall and monitor the progress of ongoing operations.
- [Troubleshooting firewall endpoint failures](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-troubleshooting-endpoint-failures.html): Use the status messages to troubleshoot endpoint failures for both firewall endpoints and VPC endpoint associations.


## [Firewall policies](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-policies.html)

- [Firewall policy settings](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-policy-settings.html): See the configuration settings for a Network Firewall firewall policy.
- [Stream exception policy options](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stream-exception-policy.html): Use a firewall policy stream exception policy to determine how Network Firewall handles traffic when a network connection breaks midstream.

### [Managing your firewall policy](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-policy-managing.html)

Create, update, and delete your firewall policy.

- [Creating a firewall policy](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-policy-creating.html): Create your firewall policy.
- [Updating a firewall policy](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-policy-updating.html): Update your firewall policy.
- [Deleting a firewall policy](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-policy-deleting.html): Delete your firewall policy.


## [Managing your rule groups](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups.html)

- [Common rule group settings](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-group-settings.html): See the configuration settings for a Network Firewall rule group.

### [Stateful rule options](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateful-rule-group-options.html)

Understand your options for providing Suricata compatible rules to AWS Network Firewall.

- [Standard stateful rule groups](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateful-rule-groups-basic.html): Use a stateful rule group with basic header rules to inspect for packet flows that match simple network traffic inspection criteria.
- [Suricata compatible rule strings](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateful-rule-groups-suricata.html): Provide your Suricata compatible rules as strings or as a file that contains strings.
- [Stateful domain list rule groups](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateful-rule-groups-domain-names.html): Use a stateful rule group with domain list to inspect for packets that match domain name specifications.
- [IP set references](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups-ip-set-references.html): You can use an IP set reference with Suricata compatible rule strings and with standard Network Firewall stateful rule groups.
- [Geographic IP filtering](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups-geo-ip-filtering.html): You can use Geographic IP filtering with Suricata compatible rule strings and with standard Network Firewall stateful rule groups.
- [URL and Domain Category Filtering](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-groups-url-filtering.html): URL and Domain Category filtering enables you to filter network traffic based on predefined content categories.

### [Working with stateful rule groups](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateful-rule-groups-ips.html)

Use a stateful rule group with Suricata compatible intrusion prevention system (IPS) rules to inspect traffic flows.

- [Creating a stateful rule group](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-group-stateful-creating.html): Create a stateful rule group.
- [Updating a stateful rule group](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-group-stateful-updating.html): Update a stateful rule group.
- [Deleting a stateful rule group](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-group-stateful-deleting.html): Delete a stateful rule group.
- [Managing evaluation order for stateful rules](https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html): You can configure and manage the evaluation order of the rules in your Suricata compatible stateful rule groups.
- [Limitations and caveats](https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-limitations-caveats.html): AWS Network Firewall stateful rules are Suricata compatible.
- [Best practices](https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-best-practices.html): A stateful rule group is a rule group that uses Suricata compatible intrusion prevention system (IPS) specifications.
- [Rule examples](https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-examples.html): This section lists examples of Suricata compatible rules that could be used with AWS Network Firewall.

### [Working with stateless rule groups](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateless-rule-groups-standard.html)

Use a stateless rule to inspect each network packet in isolation, without considering context such as traffic direction or other packets in the same traffic flow.

- [Creating a stateless rule group](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-group-stateless-creating.html): Create a stateless rule group.
- [Updating a stateless rule group](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-group-updating.html): Update a rule group.
- [Deleting a stateless rule group](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-group-deleting.html): Delete a rule group.
- [Analyzing stateless rule groups](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateless-rule-group-analyzer.html): The stateless rule group analyzer identifies the rules that might adversely effect your firewall's functionality.
- [Defining rule actions](https://docs.aws.amazon.com/network-firewall/latest/developerguide/rule-action.html): Use a rule action setting to specify what to do with a packet when it matches the criteria that's defined in the rule.
- [Setting rule group capacity](https://docs.aws.amazon.com/network-firewall/latest/developerguide/nwfw-rule-group-capacity.html): The rule group capacity indicates how much operating capacity to reserve in the firewall policy for the rule group.


## [Using managed rule groups](https://docs.aws.amazon.com/network-firewall/latest/developerguide/nwfw-managed-rule-groups.html)

### [Active threat defense managed rule groups](https://docs.aws.amazon.com/network-firewall/latest/developerguide/aws-managed-rule-groups-atd.html)

Learn how to implement the active threat defense in your AWS Network Firewall policies.

### [Understanding active threat defense indicators](https://docs.aws.amazon.com/network-firewall/latest/developerguide/atd-indicators.html)

Learn about the different types of indicators that active threat defense managed rule groups use to protect your resources.

- [Working with indicators in Amazon GuardDuty](https://docs.aws.amazon.com/network-firewall/latest/developerguide/nwfw-atd-guardduty-use-case.html): Learn how active threat defense managed rule group complements Amazon GuardDuty threat detection.
- [Deep threat inspection for active threat defense managed rule groups](https://docs.aws.amazon.com/network-firewall/latest/developerguide/atd-deep-threat-inspection.html): Learn about deep threat inspection capability for active threat defense managed rule groups.
- [Domain and IP managed rule groups](https://docs.aws.amazon.com/network-firewall/latest/developerguide/aws-managed-rule-groups-domain-list.html): AWS domain and IP managed rule groups for Network Firewall

### [Threat signature managed rule groups](https://docs.aws.amazon.com/network-firewall/latest/developerguide/aws-managed-rule-groups-threat-signature.html)

AWS threat signature rule groups for Network Firewall

- [Copying threat signature rules](https://docs.aws.amazon.com/network-firewall/latest/developerguide/copying-managed-threat-signature-rules.html): Network Firewall provides full visibility into the threat signature rule content of its AWS managed rules.
- [Notifications for threat signature rule group updates](https://docs.aws.amazon.com/network-firewall/latest/developerguide/using-managed-rule-groups-sns.html): You can subscribe to Amazon Simple Notification Service (Amazon SNS) notifications for updates to a managed threat signature rule group, such as updates made for urgent security updates.
- [Using AWS Marketplace rule groups](https://docs.aws.amazon.com/network-firewall/latest/developerguide/aws-marketplace-rule-groups.html): Learn how to use AWS Marketplace rule groups with AWS Network Firewall to integrate managed security rules from AWS Partners.

### [Working with managed rule groups](https://docs.aws.amazon.com/network-firewall/latest/developerguide/nwfw-using-managed-rule-groups-console.html)

Through the console, you access managed rule group information when you add and edit rules in your firewall policies.

- [Adding managed rule groups](https://docs.aws.amazon.com/network-firewall/latest/developerguide/nwfw-using-managed-rule-groups-add-to-policy.html): Learn how to add one or more managed rule groups to your Network Firewall firewall policy.
- [Viewing managed rule groups](https://docs.aws.amazon.com/network-firewall/latest/developerguide/nwfw-using-managed-rule-groups-list.html): You can view the managed rule groups that are available for your use in your Network Firewall policy.
- [Troubleshooting](https://docs.aws.amazon.com/network-firewall/latest/developerguide/nwfw-using-managed-rule-groups-mitigating-false-positive.html): As a best practice, before using a rule group in production, with logging enabled, run the managed rule group in alert mode if you're using an intrusion detection system (IDS), or in drop mode if you use an intrusion prevention system (IPS) in a non-production environment.
- [Considerations and disclaimers](https://docs.aws.amazon.com/network-firewall/latest/developerguide/aws-managed-rule-groups-disclaimer.html): Considerations regarding the use of AWS managed rule groups in AWS Network Firewall.


## [Tagged resource groups](https://docs.aws.amazon.com/network-firewall/latest/developerguide/resource-groups.html)

- [Resource group settings](https://docs.aws.amazon.com/network-firewall/latest/developerguide/resource-group-settings.html): See the configuration settings for a tag-based Network Firewall resource group.
- [Creating a resource group](https://docs.aws.amazon.com/network-firewall/latest/developerguide/resource-group-creating.html): Create your resource group.
- [Updating a resource group](https://docs.aws.amazon.com/network-firewall/latest/developerguide/resource-group-updating.html): Update your resource group.
- [Deleting a resource group](https://docs.aws.amazon.com/network-firewall/latest/developerguide/resource-group-deleting.html): Delete your resource group.


## [TLS inspection configurations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection-configurations.html)

- [Considerations when working with TLS inspection configurations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection-considerations.html): Considerations when working with TLS inspection configurations
- [Logging for TLS inspection in AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection-logging.html): Logging for TLS inspection
- [Using SSL/TLS certificates with TLS inspection configurations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection-certificate-requirements.html): Requirements for using SSL/TLS certificates for TLS inspection configurations.
- [TLS inspection configuration settings](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection-settings.html): See the configuration settings for a Network Firewall TLS inspection configuration.
- [Session holding with TLS inspection](https://docs.aws.amazon.com/network-firewall/latest/developerguide/session-holding-tls.html): Configure session holding to enhance security for TLS inspection by controlling when connection establishment packets reach destination servers.

### [Managing your TLS inspection configuration](https://docs.aws.amazon.com/network-firewall/latest/developerguide/managing-tls-configuration.html)

This section describes how to create, update, and delete a TLS inspection configuration in Network Firewall.

- [Creating a TLS inspection configuration](https://docs.aws.amazon.com/network-firewall/latest/developerguide/creating-tls-configuration.html): Create a TLS inspection configuration.
- [Updating a TLS inspection configuration](https://docs.aws.amazon.com/network-firewall/latest/developerguide/updating-tls-configuration.html): Update a TLS inspection configuration
- [Deleting a TLS inspection configuration](https://docs.aws.amazon.com/network-firewall/latest/developerguide/deleting-tls-configuration.html): Delete a TLS inspection configuration


## [Security in your use of the Network Firewall service](https://docs.aws.amazon.com/network-firewall/latest/developerguide/security.html)

### [Data protection](https://docs.aws.amazon.com/network-firewall/latest/developerguide/data-protection.html)

Protect your data when you use Network Firewall.

- [Encryption at rest](https://docs.aws.amazon.com/network-firewall/latest/developerguide/kms-encryption-at-rest.html): By default, AWS Network Firewall provides encryption for your data at rest using AWS owned keys to protect sensitive customer data.

### [Identity and Access Management](https://docs.aws.amazon.com/network-firewall/latest/developerguide/security-iam.html)

How to authenticate requests and manage access to your Network Firewall resources.

- [How AWS Network Firewall works with IAM](https://docs.aws.amazon.com/network-firewall/latest/developerguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Network Firewall, learn what IAM features are available to use with Network Firewall.
- [Identity-based policy examples](https://docs.aws.amazon.com/network-firewall/latest/developerguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Network Firewall resources.
- [Resource-based policy examples](https://docs.aws.amazon.com/network-firewall/latest/developerguide/security_iam_resource-based-policy-examples.html): The Network Firewall service supports only one type of resource-based policy called a resource policy, which is attached to a shared firewall policy or rule group.
- [AWS managed policies](https://docs.aws.amazon.com/network-firewall/latest/developerguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Network Firewall and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/network-firewall/latest/developerguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Network Firewall and IAM.
- [Using service-linked roles](https://docs.aws.amazon.com/network-firewall/latest/developerguide/using-service-linked-roles.html): Use service-linked roles to give Network Firewall access to resources in your AWS account.
- [AWS logging and monitoring tools](https://docs.aws.amazon.com/network-firewall/latest/developerguide/incident-response.html): Use AWS tools for monitoring and responding to incidents.
- [Compliance validation and security best practices for Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/network-firewall/latest/developerguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy as well as any specific Network Firewall features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/network-firewall/latest/developerguide/infrastructure-security.html): Learn how AWS Network Firewall isolates service traffic.
- [VPC endpoints](https://docs.aws.amazon.com/network-firewall/latest/developerguide/vpc-interface-endpoints.html): You can create a private connection between your VPC and AWS Network Firewall.


## [Logging and monitoring](https://docs.aws.amazon.com/network-firewall/latest/developerguide/logging-monitoring.html)

- [Managing AWS Network Firewall events using Amazon EventBridge](https://docs.aws.amazon.com/network-firewall/latest/developerguide/eventbridge-events.html): Receive notifications when firewall state changes occur in AWS Network Firewall.

### [Logging network traffic](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-logging.html)

Log alert, flow, and TLS logs from the Network Firewall stateful inspection engine.

- [Contents of a Network Firewall log](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-logging-contents.html): Understand the contents of the firewall logs.
- [Timing of log delivery](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-logging-timing.html): Understand how logs are delivered.
- [Permissions to configure logging](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-logging-permissions.html): Understand the general permissions required to configure firewall logs.
- [Pricing for logging](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-logging-pricing.html): Understand the pricing considerations for using firewall logs.

### [Firewall logging destinations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-logging-destinations.html)

Configure a logging destination to receive Network Firewall logs and configure the permissions that are required to log to the destination from Network Firewall.

- [Amazon S3](https://docs.aws.amazon.com/network-firewall/latest/developerguide/logging-s3.html): Configure firewall logging to Amazon S3.
- [CloudWatch Logs](https://docs.aws.amazon.com/network-firewall/latest/developerguide/logging-cw-logs.html): Configure firewall logging to Amazon CloudWatch Logs.
- [Firehose](https://docs.aws.amazon.com/network-firewall/latest/developerguide/logging-kinesis.html): Configure firewall logging to Amazon Data Firehose.
- [Logging with server-side encryption and customer-provided keys](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-logging-encrypt-kms.html): Configure permissions to your SSE-KMS KMS keys to allow Network Firewall logging.
- [Updating a firewall's logging configuration](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-update-logging-configuration.html): Update your firewall's logging configuration in AWS Network Firewall.
- [Logging calls to the API with AWS CloudTrail](https://docs.aws.amazon.com/network-firewall/latest/developerguide/logging-using-cloudtrail.html): Learn about how Network Firewall API calls are logged with AWS CloudTrail and about how to view the logs.
- [Metrics in CloudWatch](https://docs.aws.amazon.com/network-firewall/latest/developerguide/monitoring-cloudwatch.html): Learn about CloudWatch metrics for Network Firewall.

### [Monitoring and reporting in Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/nwfw-monitoring-reporting.html)

Network Firewall provides monitoring and reporting capabilities to help you analyze your network traffic and maintain security compliance from within the Network Firewall console.

### [Firewall monitoring in the console](https://docs.aws.amazon.com/network-firewall/latest/developerguide/nwfw-detailed-monitoring.html)

Learn how to use detailed monitoring to analyze your network traffic patterns and security metrics in real time.

- [Working with the dashboard](https://docs.aws.amazon.com/network-firewall/latest/developerguide/nwfw-using-dashboard.html): The firewall monitoring dashboard provides multiple options for viewing key metrics about your firewall.
- [Flow and alert log metrics](https://docs.aws.amazon.com/network-firewall/latest/developerguide/nwfw-detailed-monitoring-metrics.html): The firewall monitoring dashboard provides multiple options for viewing key metrics about your firewall.
- [Reporting network traffic](https://docs.aws.amazon.com/network-firewall/latest/developerguide/reporting.html): Learn about reporting capabilities that exist for Network Firewall.


## [Troubleshooting](https://docs.aws.amazon.com/network-firewall/latest/developerguide/troubleshooting.html)

- [General issues](https://docs.aws.amazon.com/network-firewall/latest/developerguide/troubleshooting-general-issues.html): Use the information here to help you diagnose and fix common issues when you work with Network Firewall.
- [Logging](https://docs.aws.amazon.com/network-firewall/latest/developerguide/troubleshooting-logging.html): Use the information here to help you diagnose common issues that you might encounter when working with logging in Network Firewall.
- [Rules](https://docs.aws.amazon.com/network-firewall/latest/developerguide/troubleshooting-rules.html): Use the information here to help you diagnose common issues that you might encounter when working with rules in Network Firewall.
- [TLS inspection](https://docs.aws.amazon.com/network-firewall/latest/developerguide/troubleshooting-tls-inspection.html): Use the information here to help you diagnose common issues that you might encounter when working with TLS inspection in Network Firewall.


## [Network Firewall Proxy Guide](https://docs.aws.amazon.com/network-firewall/latest/developerguide/network-firewall-proxy-developer-guide.html)

- [How does Network Firewall Proxy work?](https://docs.aws.amazon.com/network-firewall/latest/developerguide/how-does-network-firewall-proxy-work.html): Learn about the core components and traffic flow management of Network Firewall Proxy, including proxy configurations, rule groups, filtering rules, and the multi-phase traffic inspection process.
- [Architecture overview](https://docs.aws.amazon.com/network-firewall/latest/developerguide/proxy-architecture-overview.html): This section provides a high-level view of simple architectures that you can configure with AWS Network Firewall Proxy.
- [Pre-requisites](https://docs.aws.amazon.com/network-firewall/latest/developerguide/proxy-pre-requisites.html): Prerequisites and setup requirements for NFW proxy implementation including related services, IAM permissions, proxy endpoints, trust setup, and proxy variables configuration.
- [Getting started with Network Firewall Proxy](https://docs.aws.amazon.com/network-firewall/latest/developerguide/getting-started-with-network-firewall-proxy.html): AWS Network Firewall Proxy provides network traffic filtering and protection for your applications hosted in Amazon VPCs and on-premises environment.
- [Managing Your Rules](https://docs.aws.amazon.com/network-firewall/latest/developerguide/managing-your-proxy-rules.html): Learn how to manage proxy rules, including rule structure, operations, priority, and evaluation order for effective traffic filtering and control.
- [Managing Your Rule Groups](https://docs.aws.amazon.com/network-firewall/latest/developerguide/managing-proxy-rule-groups.html): Learn how to create, modify, and manage rule groups in VPC Proxy for organizing and managing collections of access control rules.
- [Managing Your Proxy Configuration](https://docs.aws.amazon.com/network-firewall/latest/developerguide/managing-proxy-configuration.html): Proxy configurations use rule groups and other settings to define the traffic filtering behavior for a Proxy.
- [Logging and Monitoring](https://docs.aws.amazon.com/network-firewall/latest/developerguide/proxy-logging-and-monitoring.html): Learn how to configure logging for network traffic and monitor proxy activity with detailed log information.
- [Security in your use of the AWS Network Firewall service](https://docs.aws.amazon.com/network-firewall/latest/developerguide/proxy-security.html): Security considerations and best practices for AWS Network Firewall service configuration and deployment.
- [Limits of the proxy service for the public preview in US East (Ohio) region only](https://docs.aws.amazon.com/network-firewall/latest/developerguide/limits-of-the-proxy-service.html): Service resource limits and network protocol restrictions for the Network Firewall proxy service public preview.


## [Using the Network Firewall REST API](https://docs.aws.amazon.com/network-firewall/latest/developerguide/api-using.html)

- [Making HTTPS requests to Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/api-making-requests.html): Create proper HTTPS requests to access the Network Firewall REST API.
- [HTTP responses](https://docs.aws.amazon.com/network-firewall/latest/developerguide/api-making-requests-response.html): Handle HTTPS responses to your Network Firewall REST API requests.
- [Authenticating requests](https://docs.aws.amazon.com/network-firewall/latest/developerguide/authenticating-requests.html): Sign your Network Firewall REST API requests to authenticate them.
