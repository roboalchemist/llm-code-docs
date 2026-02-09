# Source: https://docs.datadoghq.com/security/default_rules/def-000-9yy.md

---
title: VPC Flow Logs should be enabled for all VPC subnets
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > VPC Flow Logs should be enabled for all
  VPC subnets
---

# VPC Flow Logs should be enabled for all VPC subnets
 
## Description{% #description %}

Flow Logs is a feature that enables users to capture information about the IP traffic going to and from network interfaces in an organization's VPC subnets. Once a flow log is created, the user can view and retrieve its data in Stackdriver Logging. It is recommended that Flow Logs is enabled for every business-critical VPC subnet.

### Default value{% #default-value %}

By default Flow Logs is set to `Off` when a new VPC network subnet is created.

## Rationale{% #rationale %}

VPC networks and subnetworks that are not reserved for internal HTTP(S) load balancing provide logically isolated and secure network partitions from which GCP resources can be launched. When Flow Logs are enabled for a subnet, VMs within that subnet start reporting on all Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) flows. Each VM samples the TCP and UDP flows it sees, inbound and outbound, whether the flow is to or from another VM, a host in the on-premise datacenter, a Google service, or a host on the Internet. If two GCP VMs are communicating, and both are in subnets that have VPC Flow Logs enabled, both VMs report the flows.

Flow Logs supports the following use cases:

- Network monitoring
- Understanding network usage and optimizing network traffic expenses
- Network forensics
- Real-time security analysis

Flow Logs provides visibility into network traffic for each VM inside the subnet and can be used to detect anomalous traffic or provide insight on security workflows. The Flow Logs must be configured such that all network traffic is logged. The interval of logging is granular enough to provide detailed information on the connections, where no logs are filtered and metadata to facilitate investigations are included.

- Note: Subnets reserved for use by internal HTTP(S) load balancers do not support VPC Flow Logs.

### Impact{% #impact %}

Standard pricing for Stackdriver Logging, BigQuery, or Cloud Pub/Sub applies. VPC Flow Logs generation will be charged when it's generally available, as described in this reference: [https://cloud.google.com/vpc/](https://cloud.google.com/vpc/)

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to the VPC network GCP Console page by visiting: [https://console.cloud.google.com/networking/networks/list](https://console.cloud.google.com/networking/networks/list)
1. Click the name of a **subnet** to display the subnet details page.
1. Click **EDIT** .
1. Set Flow Logs to **On**.
1. Expand the **Configure Logs** section.
1. Set **Aggregation Interval** to `5 SEC`.
1. Check the box for **Include metadata**.
1. Set **Sample rate** to `100`.
1. Click **Save**.

- Note: You can only configure a log filter from the command line.

### From the command line{% #from-the-command-line %}

To enable VPC Flow Logs for a network subnet, run the following command:

```
gcloud compute networks subnets update [SUBNET_NAME] --region [REGION] --
enable-flow-logs --logging-aggregation-interval=interval-5-sec --logging-
flow-sampling=1 --logging-metadata=include-all
```

## References{% #references %}

1. [https://cloud.google.com/vpc/docs/using-flow-logs#enabling_vpc_flow_logging](https://cloud.google.com/vpc/docs/using-flow-logs#enabling_vpc_flow_logging)
1. [https://cloud.google.com/vpc/](https://cloud.google.com/vpc/)
