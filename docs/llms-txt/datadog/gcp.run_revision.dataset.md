# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.run_revision.dataset.md

---
title: Cloud Run Revision
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud Run Revision
---

# Cloud Run Revision

A Cloud Run Revision in Google Cloud represents an immutable version of a deployed service. Each time you deploy new code or configuration, a new revision is created. Revisions capture the exact container image, environment variables, and settings used at deployment, allowing you to roll back or split traffic between versions.

```
gcp.run_revision
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                   | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| api_version          | core | string        | The API version for this call such as "serving.knative.dev/v1".                             |
| datadog_display_name | core | string        |
| gcp_status           | core | json          | Status communicates the observed state of the Revision (from the controller).               |
| kind                 | core | string        | The kind of this resource, in this case "Revision".                                         |
| labels               | core | array<string> |
| metadata             | core | json          | Metadata associated with this Revision, including name, namespace, labels, and annotations. |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| spec                 | core | json          | Spec holds the desired state of the Revision (from the client).                             |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
