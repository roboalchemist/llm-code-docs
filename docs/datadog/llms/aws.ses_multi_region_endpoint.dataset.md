# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ses_multi_region_endpoint.dataset.md

---
title: SES Multi Region Endpoint
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SES Multi Region Endpoint
---

# SES Multi Region Endpoint

This table represents the SES Multi Region Endpoint resource from Amazon Web Services.

```
aws.ses_multi_region_endpoint
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                        | Description |
| ---------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| created_timestamp      | core | timestamp  | The time stamp of when the multi-region endpoint (global-endpoint) was created.                                                                                                                                                                                                                                                                                  |
| endpoint_id            | core | string     | The ID of the multi-region endpoint (global-endpoint).                                                                                                                                                                                                                                                                                                           |
| endpoint_name          | core | string     | The name of the multi-region endpoint (global-endpoint).                                                                                                                                                                                                                                                                                                         |
| last_updated_timestamp | core | timestamp  | The time stamp of when the multi-region endpoint (global-endpoint) was last updated.                                                                                                                                                                                                                                                                             |
| routes                 | core | json       | Contains routes information for the multi-region endpoint (global-endpoint).                                                                                                                                                                                                                                                                                     |
| status                 | core | string     | The status of the multi-region endpoint (global-endpoint). <ul> <li> <code>CREATING</code> â The resource is being provisioned. </li> <li> <code>READY</code> â The resource is ready to use. </li> <li> <code>FAILED</code> â The resource failed to be provisioned. </li> <li> <code>DELETING</code> â The resource is being deleted as requested. </li> </ul> |
| tags                   | core | hstore_csv |
