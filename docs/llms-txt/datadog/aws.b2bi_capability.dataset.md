# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.b2bi_capability.dataset.md

---
title: B2B Data Interchange Capability
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > B2B Data Interchange Capability
---

# B2B Data Interchange Capability

B2B Data Interchange Capability in AWS B2BI enables secure and reliable exchange of business documents between trading partners. It supports standards-based protocols and provides tools to configure, monitor, and manage data flows, helping organizations automate partner integrations and streamline supply chain operations.

```
aws.b2bi_capability
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                                                                      | Description |
| ---------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| capability_arn         | core | string     | Returns an Amazon Resource Name (ARN) for a specific Amazon Web Services resource, such as a capability, partnership, profile, or transformer.                                                                 |
| capability_id          | core | string     | Returns a system-assigned unique identifier for the capability.                                                                                                                                                |
| configuration          | core | json       | Returns a structure that contains the details for a capability.                                                                                                                                                |
| created_at             | core | timestamp  | Returns a timestamp for creation date and time of the capability.                                                                                                                                              |
| instructions_documents | core | json       | Returns one or more locations in Amazon S3, each specifying an EDI document that can be used with this capability. Each item contains the name of the bucket and the key, to identify the document's location. |
| modified_at            | core | timestamp  | Returns a timestamp for last time the capability was modified.                                                                                                                                                 |
| name                   | core | string     | Returns the name of the capability, used to identify it.                                                                                                                                                       |
| tags                   | core | hstore_csv |
| type                   | core | string     | Returns the type of the capability. Currently, only edi is supported.                                                                                                                                          |
