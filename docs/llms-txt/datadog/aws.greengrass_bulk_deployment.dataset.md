# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.greengrass_bulk_deployment.dataset.md

---
title: Greengrass Bulk Deployment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Greengrass Bulk Deployment
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.greengrass_bulk_deployment.dataset/index.html
---

# Greengrass Bulk Deployment

This table represents the greengrass_bulk_deployment resource from Amazon Web Services.

```
aws.greengrass_bulk_deployment
```

## Fields

| Title                   | ID   | Type   | Data Type                                                           | Description |
| ----------------------- | ---- | ------ | ------------------------------------------------------------------- | ----------- |
| _key                    | core | string |
| account_id              | core | string |
| bulk_deployment_metrics | core | json   | Relevant metrics on input records processed during bulk deployment. |
| bulk_deployment_status  | core | string | The status of the bulk deployment.                                  |
| created_at              | core | string | The time, in ISO format, when the deployment was created.           |
| error_details           | core | json   | Error details                                                       |
| error_message           | core | string | Error message                                                       |
| tags                    | core | hstore |
