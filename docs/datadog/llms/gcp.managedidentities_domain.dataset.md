# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.managedidentities_domain.dataset.md

---
title: Managed Microsoft AD Domain
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Managed Microsoft AD Domain
---

# Managed Microsoft AD Domain

Managed Microsoft AD Domain on Google Cloud is a fully managed service that provides highly available, secure, and scalable Active Directory domains. It allows organizations to run Microsoft Active Directory workloads in the cloud without the overhead of managing domain controllers, replication, or patching. This service integrates with on-premises AD environments, enabling hybrid identity and access management.

```
gcp.managedidentities_domain
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                     | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| admin                | core | string        | Optional. The name of delegated administrator account used to perform Active Directory operations. If not specified, `setupadmin` will be used.                                                                                                                                                                                               |
| ancestors            | core | array<string> |
| audit_logs_enabled   | core | bool          | Optional. Configuration for audit logs. True if audit logs are enabled, else false. Default is audit logs disabled.                                                                                                                                                                                                                           |
| authorized_networks  | core | array<string> | Optional. The full names of the Google Compute Engine [networks](/compute/docs/networks-and-firewalls#networks) the domain instance is connected to. Networks can be added using UpdateDomain. The domain is only available on networks listed in `authorized_networks`. If CIDR subnets overlap between networks, domain creation will fail. |
| create_time          | core | timestamp     | Output only. The time the instance was created.                                                                                                                                                                                                                                                                                               |
| datadog_display_name | core | string        |
| fqdn                 | core | string        | Output only. The fully-qualified domain name of the exposed domain used by clients to connect to the service. Similar to what would be chosen for an Active Directory set up on an internal network.                                                                                                                                          |
| labels               | core | array<string> | Optional. Resource labels that can contain user-provided metadata.                                                                                                                                                                                                                                                                            |
| locations            | core | array<string> | Required. Locations where domain needs to be provisioned. The locations can be specified according to https://cloud.google.com/compute/docs/regions-zones, such as `us-west1` or `us-east4`. Each domain supports up to 4 locations, separated by commas. Each location will use a /26 block.                                                 |
| name                 | core | string        | Required. The unique name of the domain using the form: `projects/{project_id}/locations/global/domains/{domain_name}`.                                                                                                                                                                                                                       |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| reserved_ip_range    | core | string        | Required. The CIDR range of internal addresses that are reserved for this domain. Reserved networks must be /24 or larger. Ranges must be unique and non-overlapping with existing subnets in [Domain].[authorized_networks].                                                                                                                 |
| resource_name        | core | string        |
| state                | core | string        | Output only. The current state of this domain.                                                                                                                                                                                                                                                                                                |
| status_message       | core | string        | Output only. Additional information about the current status of this domain, if available.                                                                                                                                                                                                                                                    |
| tags                 | core | hstore_csv    |
| trusts               | core | json          | Output only. The current trusts associated with the domain.                                                                                                                                                                                                                                                                                   |
| update_time          | core | timestamp     | Output only. The last update time.                                                                                                                                                                                                                                                                                                            |
| zone_id              | core | string        |
