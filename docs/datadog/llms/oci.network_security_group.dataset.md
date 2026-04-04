# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/oci/oci.network_security_group.dataset.md

---
title: Network Security Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Network Security Group
---

# Network Security Group

A Network Security Group (NSG) in OCI is a virtual firewall that lets you define and enforce security rules for a set of cloud resources. It provides fine-grained control over both inbound and outbound traffic at the virtual network interface level, independent of the subnet's security rules. NSGs make it easier to apply consistent security policies across multiple resources without changing subnet configurations.

```
oci.network_security_group
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                     | Description |
| ------------------ | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| cloud_account_id   | core | string     | The identifier of the related cloud account. The concept of an account might have different names in different cloud providers. AWS is calling it account, GCP calls it project and Azure uses the term subscription.                                                                         |
| cloud_account_name | core | string     | The name of the account this resource belongs to.                                                                                                                                                                                                                                             |
| cloud_provider     | core | string     | The name of the cloud provider.                                                                                                                                                                                                                                                               |
| cloud_tags         | core | hstore     |
| compartment_id     | core | string     | The value to assign to the compartment_id property of this NetworkSecurityGroup.                                                                                                                                                                                                              |
| created_at         | core | timestamp  | Time when the resource has been created.                                                                                                                                                                                                                                                      |
| freeform_tags      | core | hstore     | The value to assign to the freeform_tags property of this NetworkSecurityGroup.                                                                                                                                                                                                               |
| id                 | core | string     | The value to assign to the id property of this NetworkSecurityGroup.                                                                                                                                                                                                                          |
| lifecycle_state    | core | string     | The value to assign to the lifecycle_state property of this NetworkSecurityGroup. Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'. Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'. |
| name               | core | string     | The name of this resource.                                                                                                                                                                                                                                                                    |
| region_id          | core | string     | The region this resource resides within.                                                                                                                                                                                                                                                      |
| resource_type      | core | string     | The name of the resource type.                                                                                                                                                                                                                                                                |
| security_rules     | core | json       |
| tags               | core | hstore_csv |
| time_created       | core | timestamp  | The value to assign to the time_created property of this NetworkSecurityGroup.                                                                                                                                                                                                                |
| updated_at         | core | timestamp  | Time when the resource has been updated the last time.                                                                                                                                                                                                                                        |
| vcn_id             | core | string     | The value to assign to the vcn_id property of this NetworkSecurityGroup.                                                                                                                                                                                                                      |
| zone_id            | core | string     | The zone this resource resides within.                                                                                                                                                                                                                                                        |
