# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/dd/dd.agent_hosts.dataset.md

---
title: Agent Hosts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Agent Hosts
---

# Agent Hosts

The Agent Hosts table provides information about hosts where Datadog Agents are installed and actively collecting data. Each row represents a host monitored by a Datadog Agent and includes metadata about the agent version, cloud provider infrastructure, hostname detection, and resource tags. This table enables you to track agent deployments across your infrastructure, monitor agent version compliance, correlate agent data with cloud integration data, and maintain visibility into which hosts are reporting to Datadog.

```
dd.agent_hosts
```

## Fields

| Title                        | ID                           | Type | Data Type | Description                                                                                                      |
| ---------------------------- | ---------------------------- | ---- | --------- | ---------------------------------------------------------------------------------------------------------------- |
| Agent Version                | agent_version                | core | string    | The version of the Datadog Agent running on the host.                                                            |
| Cloud Provider               | cloud_provider               | core | string    | Indicates the cloud service provider associated with the host, such as AWS, GCP, or Azure.                       |
| Cloud Provider Resource Type | cloud_provider_resource_type | core | string    | Specifies the type of cloud resource, indicating the cloud provider and specific resource category.              |
| Hostname                     | hostname                     | core | string    | The hostname of the host running the Datadog Agent.                                                              |
| Resource Tags                | tags                         | core | hstore    | This field contains tags represented as key-value pairs, used to categorize and provide metadata about the host. |
