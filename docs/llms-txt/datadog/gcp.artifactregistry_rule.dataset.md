# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.artifactregistry_rule.dataset.md

---
title: Artifact Registry Rule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Artifact Registry Rule
---

# Artifact Registry Rule

Artifact Registry Rule in Google Cloud Platform defines policies and configurations for managing container images and language packages stored in Artifact Registry. It helps control access, versioning, and retention of artifacts, ensuring secure and efficient software delivery workflows.

```
gcp.artifactregistry_rule
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                 | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| action               | core | string        | The action this rule takes.                                                                                                               |
| ancestors            | core | array<string> |
| condition            | core | json          | Optional. A CEL expression for conditions that must be met in order for the rule to apply. If not provided, the rule matches all objects. |
| datadog_display_name | core | string        |
| labels               | core | array<string> |
| name                 | core | string        | The name of the rule, for example: `projects/p1/locations/us-central1/repositories/repo1/rules/rule1`.                                    |
| operation            | core | string        |
| organization_id      | core | string        |
| package_id           | core | string        | The package ID the rule applies to. If empty, this rule applies to all packages inside the repository.                                    |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
