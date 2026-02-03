# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dns_managed_zone.dataset.md

---
title: Cloud DNS Managed Zone
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud DNS Managed Zone
---

# Cloud DNS Managed Zone

A Cloud DNS Managed Zone in Google Cloud is a container for DNS records that define how domain names are resolved. It allows you to manage public or private DNS zones, configure record sets, and control name resolution for your applications and services. This resource provides scalable, reliable, and low-latency DNS management integrated with other Google Cloud services.

```
gcp.dns_managed_zone
```

## Fields

| Title                     | ID   | Type          | Data Type                                                                                                                                                                                                                                                     | Description |
| ------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string        |
| ancestors                 | core | array<string> |
| cloud_logging_config      | core | json          |
| creation_time             | core | timestamp     | The time that this resource was created on the server. This is in RFC3339 text format. Output only.                                                                                                                                                           |
| datadog_display_name      | core | string        |
| description               | core | string        | A mutable string of at most 1024 characters associated with this resource for the user's convenience. Has no effect on the managed zone's function.                                                                                                           |
| dns_name                  | core | string        | The DNS name of this managed zone, for instance "example.com.".                                                                                                                                                                                               |
| dnssec_config             | core | json          | DNSSEC configuration.                                                                                                                                                                                                                                         |
| forwarding_config         | core | json          | The presence for this field indicates that outbound forwarding is enabled for this zone. The value of this field contains the set of destinations to forward to.                                                                                              |
| id                        | core | string        | Unique identifier for the resource; defined by the server (output only)                                                                                                                                                                                       |
| kind                      | core | string        |
| labels                    | core | array<string> | User labels.                                                                                                                                                                                                                                                  |
| name                      | core | string        | User assigned name for this resource. Must be unique within the project. The name must be 1-63 characters long, must begin with a letter, end with a letter or digit, and only contain lowercase letters, digits or dashes.                                   |
| name_server_set           | core | string        | Optionally specifies the NameServerSet for this ManagedZone. A NameServerSet is a set of DNS name servers that all host the same ManagedZones. Most users leave this field unset. If you need to use this field, contact your account team.                   |
| name_servers              | core | array<string> | Delegate your managed_zone to these virtual name servers; defined by the server (output only)                                                                                                                                                                 |
| organization_id           | core | string        |
| parent                    | core | string        |
| peering_config            | core | json          | The presence of this field indicates that DNS Peering is enabled for this zone. The value of this field contains the network to peer with.                                                                                                                    |
| private_visibility_config | core | json          | For privately visible zones, the set of Virtual Private Cloud resources that the zone is visible from.                                                                                                                                                        |
| project_id                | core | string        |
| project_number            | core | string        |
| region_id                 | core | string        |
| resource_name             | core | string        |
| reverse_lookup_config     | core | json          | The presence of this field indicates that this is a managed reverse lookup zone and Cloud DNS resolves reverse lookup queries using automatically configured records for VPC resources. This only applies to networks listed under private_visibility_config. |
| service_directory_config  | core | json          | This field links to the associated service directory namespace. Do not set this field for public zones or forwarding zones.                                                                                                                                   |
| tags                      | core | hstore_csv    |
| visibility                | core | string        | The zone's visibility: public zones are exposed to the Internet, while private zones are visible only to Virtual Private Cloud resources.                                                                                                                     |
| zone_id                   | core | string        |
