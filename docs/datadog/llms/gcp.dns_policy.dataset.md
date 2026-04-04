# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dns_policy.dataset.md

---
title: DNS Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DNS Policy
---

# DNS Policy

A DNS Policy in Google Cloud lets you manage and control DNS behavior for your Virtual Private Cloud networks. It allows configuration of features such as inbound and outbound forwarding, logging, and DNS peering. With DNS policies, you can customize how name resolution works within your network, apply security controls, and integrate with on-premises DNS systems.

```
gcp.dns_policy
```

## Fields

| Title                          | ID   | Type          | Data Type                                                                                                                                                                                                                            | Description |
| ------------------------------ | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                           | core | string        |
| alternative_name_server_config | core | json          | Sets an alternative name server for the associated networks. When specified, all DNS queries are forwarded to a name server that you choose. Names such as .internal are not available when an alternative name server is specified. |
| ancestors                      | core | array<string> |
| datadog_display_name           | core | string        |
| description                    | core | string        | A mutable string of at most 1024 characters associated with this resource for the user's convenience. Has no effect on the policy's function.                                                                                        |
| enable_inbound_forwarding      | core | bool          | Allows networks bound to this policy to receive DNS queries sent by VMs or applications over VPN connections. When enabled, a virtual IP address is allocated from each of the subnetworks that are bound to this policy.            |
| enable_logging                 | core | bool          | Controls whether logging is enabled for the networks bound to this policy. Defaults to no logging if not set.                                                                                                                        |
| id                             | core | string        | Unique identifier for the resource; defined by the server (output only).                                                                                                                                                             |
| kind                           | core | string        |
| labels                         | core | array<string> |
| name                           | core | string        | User-assigned name for this policy.                                                                                                                                                                                                  |
| networks                       | core | json          | List of network names specifying networks to which this policy is applied.                                                                                                                                                           |
| organization_id                | core | string        |
| parent                         | core | string        |
| project_id                     | core | string        |
| project_number                 | core | string        |
| region_id                      | core | string        |
| resource_name                  | core | string        |
| tags                           | core | hstore_csv    |
| zone_id                        | core | string        |
