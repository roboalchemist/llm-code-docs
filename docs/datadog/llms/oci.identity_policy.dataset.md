# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/oci/oci.identity_policy.dataset.md

---
title: Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Policy
---

# Policy

A Policy in Oracle Cloud Infrastructure (OCI) is a resource that defines permissions for groups of users to access specific cloud resources within a tenancy. Policies are written in a human-readable language and allow administrators to control access at the compartment or tenancy level. They provide fine-grained authorization by specifying who can access which resources and what actions they can perform, ensuring secure and organized management of cloud environments.

```
oci.identity_policy
```

## Fields

| Title              | ID   | Type          | Data Type                                                                                                                                                                                                                                                                      | Description |
| ------------------ | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key               | core | string        |
| cloud_account_id   | core | string        | The identifier of the related cloud account. The concept of an account might have different names in different cloud providers. AWS is calling it account, GCP calls it project and Azure uses the term subscription.                                                          |
| cloud_account_name | core | string        | The name of the account this resource belongs to.                                                                                                                                                                                                                              |
| cloud_provider     | core | string        | The name of the cloud provider.                                                                                                                                                                                                                                                |
| cloud_tags         | core | hstore        |
| compartment_id     | core | string        | The value to assign to the compartment_id property of this Policy.                                                                                                                                                                                                             |
| created_at         | core | timestamp     | Time when the resource has been created.                                                                                                                                                                                                                                       |
| description        | core | string        | The value to assign to the description property of this Policy.                                                                                                                                                                                                                |
| freeform_tags      | core | hstore        | The value to assign to the freeform_tags property of this Policy.                                                                                                                                                                                                              |
| id                 | core | string        | The value to assign to the id property of this Policy.                                                                                                                                                                                                                         |
| inactive_status    | core | int64         | The value to assign to the inactive_status property of this Policy.                                                                                                                                                                                                            |
| lifecycle_state    | core | string        | The value to assign to the lifecycle_state property of this Policy. Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'. Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'. |
| name               | core | string        | The value to assign to the name property of this Policy.                                                                                                                                                                                                                       |
| region_id          | core | string        | The region this resource resides within.                                                                                                                                                                                                                                       |
| resource_type      | core | string        | The name of the resource type.                                                                                                                                                                                                                                                 |
| statements         | core | array<string> | The value to assign to the statements property of this Policy.                                                                                                                                                                                                                 |
| tags               | core | hstore_csv    |
| time_created       | core | timestamp     | The value to assign to the time_created property of this Policy.                                                                                                                                                                                                               |
| updated_at         | core | timestamp     | Time when the resource has been updated the last time.                                                                                                                                                                                                                         |
| version_date       | core | timestamp     | The value to assign to the version_date property of this Policy.                                                                                                                                                                                                               |
| zone_id            | core | string        | The zone this resource resides within.                                                                                                                                                                                                                                         |
