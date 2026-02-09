# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/oci/oci.network_security_list.dataset.md

---
title: Network Security List
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Network Security List
---

# Network Security List

A Network Security List in OCI is a virtual firewall that controls inbound and outbound traffic at the subnet level. It contains security rules that define allowed protocols, ports, and source or destination IP ranges. Security lists are stateful, meaning return traffic is automatically allowed. They provide a way to enforce network access policies for resources within a subnet.

```
oci.network_security_list
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                                                                                                                                             | Description |
| ---------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| cloud_account_id       | core | string     | The identifier of the related cloud account. The concept of an account might have different names in different cloud providers. AWS is calling it account, GCP calls it project and Azure uses the term subscription.                                                                 |
| cloud_account_name     | core | string     | The name of the account this resource belongs to.                                                                                                                                                                                                                                     |
| cloud_provider         | core | string     | The name of the cloud provider.                                                                                                                                                                                                                                                       |
| cloud_tags             | core | hstore     |
| compartment_id         | core | string     | The value to assign to the compartment_id property of this SecurityList.                                                                                                                                                                                                              |
| created_at             | core | timestamp  | Time when the resource has been created.                                                                                                                                                                                                                                              |
| egress_security_rules  | core | json       | The value to assign to the egress_security_rules property of this SecurityList.                                                                                                                                                                                                       |
| freeform_tags          | core | hstore     | The value to assign to the freeform_tags property of this SecurityList.                                                                                                                                                                                                               |
| id                     | core | string     | The value to assign to the id property of this SecurityList.                                                                                                                                                                                                                          |
| ingress_security_rules | core | json       | The value to assign to the ingress_security_rules property of this SecurityList.                                                                                                                                                                                                      |
| lifecycle_state        | core | string     | The value to assign to the lifecycle_state property of this SecurityList. Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'. Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'. |
| name                   | core | string     | The name of this resource.                                                                                                                                                                                                                                                            |
| region_id              | core | string     | The region this resource resides within.                                                                                                                                                                                                                                              |
| resource_type          | core | string     | The name of the resource type.                                                                                                                                                                                                                                                        |
| tags                   | core | hstore_csv |
| time_created           | core | timestamp  | The value to assign to the time_created property of this SecurityList.                                                                                                                                                                                                                |
| updated_at             | core | timestamp  | Time when the resource has been updated the last time.                                                                                                                                                                                                                                |
| vcn_id                 | core | string     | The value to assign to the vcn_id property of this SecurityList.                                                                                                                                                                                                                      |
| zone_id                | core | string     | The zone this resource resides within.                                                                                                                                                                                                                                                |
