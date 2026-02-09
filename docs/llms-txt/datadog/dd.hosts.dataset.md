# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/dd/dd.hosts.dataset.md

---
title: Hosts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Hosts
---

# Hosts

The Hosts table provides an inventory of hosts monitored by Datadog. It includes systems running the Datadog Agent and Cloud instances monitored through Datadog's metrics integrations. Each row represents a host and its associated attributes. The table includes columns for metadata tags, cloud provider details, resource type and specifications, and system information such as hostname, operating system, CPU, and memory.

```
dd.hosts
```

## Fields

| Title                           | ID                       | Type | Data Type     | Description                                                                                                                                                                 |
| ------------------------------- | ------------------------ | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Resource Tags                   | tags                     | core | hstore        | This field contains an array of tags, each represented as a key-value pair, used to categorize and provide metadata about the associated entity.                            |
| Cloud Provider                  | cloud_provider           | core | string        | Indicates the cloud service provider associated with the resource, such as AWS, GCP, or Azure.                                                                              |
| Resource Type                   | resource_type            | core | string        | Indicates the type of cloud resource, specifying the cloud provider and resource category.                                                                                  |
| Source Platforms                | sources                  | core | array<string> | Lists the platforms or environments from which data is collected, such as cloud providers or agents.                                                                        |
| Host Identifier                 | hostname                 | core | string        | Unique identifier for the host.                                                                                                                                             |
| Hostname Aliases                | hostname_aliases         | core | array<string> | Stores an array of alias names associated with a host, including instance IDs and internal network addresses.                                                               |
| IP Addresses                    | ip_addresses             | core | array<string> | The IP addresses assigned to the host. This includes both IPv4 and IPv6 addresses.                                                                                          |
| Instance Type                   | instance_type            | core | string        | Specifies the type of virtual machine instance                                                                                                                              |
| Operating System                | os                       | core | string        | Indicates the operating system running on the host                                                                                                                          |
| Operating System Version        | os_version               | core | string        | Indicates the version of the operating system installed on the host machine. This information is useful for compatibility and support purposes.                             |
| Memory Size                     | memory_mib               | core | float64       | Represents the amount of memory allocated or used, measured in mebibytes.                                                                                                   |
| Agent Version                   | agent_version            | core | string        | Indicates the version of the software agent running on the system, including release candidates and development builds.                                                     |
| Docker Version                  | docker_version           | core | string        | Indicates the version of Docker installed on the host, if applicable.                                                                                                       |
| CPU Specifications              | cpu                      | core | hstore        | Contains detailed specifications of the CPU, including core count, model, vendor, cache size, and architecture. This information is stored as a list of key-value pairs.    |
| Kernel Information              | kernel                   | core | hstore        | Stores detailed information about the operating system kernel, including the name, release version, and build details. The data is structured as a list of key-value pairs. |
| Modification Detected Timestamp | modification_detected_at | core | timestamp     | Indicates the exact time when a modification was detected in the system. This is useful for tracking changes and auditing purposes.                                         |
