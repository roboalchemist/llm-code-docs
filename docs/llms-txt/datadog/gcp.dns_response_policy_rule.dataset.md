# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dns_response_policy_rule.dataset.md

---
title: DNS Response Policy Rule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DNS Response Policy Rule
---

# DNS Response Policy Rule

A DNS Response Policy Rule in Google Cloud lets you define custom DNS behavior within a managed response policy. It allows administrators to control how DNS queries are resolved, such as blocking, redirecting, or modifying responses for specific domains. This helps enforce security, compliance, and internal naming policies across a network.

```
gcp.dns_response_policy_rule
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                       | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| behavior             | core | string        | Answer this query with a behavior rather than DNS data.                                                                                                                                                                                         |
| datadog_display_name | core | string        |
| dns_name             | core | string        | The DNS name (wildcard or exact) to apply this rule to. Must be unique within the Response Policy Rule.                                                                                                                                         |
| kind                 | core | string        |
| labels               | core | array<string> |
| local_data           | core | json          | Answer this query directly with DNS data. These ResourceRecordSets override any other DNS behavior for the matched name; in particular they override private zones, the public internet, and GCP internal DNS. No SOA nor NS types are allowed. |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| rule_name            | core | string        | An identifier for this rule. Must be unique with the ResponsePolicy.                                                                                                                                                                            |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
