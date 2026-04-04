# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.panorama_application_instance.dataset.md

---
title: Panorama Application Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Panorama Application Instance
---

# Panorama Application Instance

An AWS Panorama Application Instance represents a deployed computer vision application running on a Panorama Appliance. It allows you to run machine learning models at the edge, process video streams locally, and generate insights without sending data to the cloud. This resource provides details about the application's status, health, and configuration.

```
aws.panorama_application_instance
```

## Fields

| Title                               | ID   | Type       | Data Type                                                       | Description |
| ----------------------------------- | ---- | ---------- | --------------------------------------------------------------- | ----------- |
| _key                                | core | string     |
| account_id                          | core | string     |
| application_instance_id             | core | string     | The application instance's ID.                                  |
| application_instance_id_to_replace  | core | string     | The ID of the application instance that this instance replaced. |
| arn                                 | core | string     | The application instance's ARN.                                 |
| created_time                        | core | timestamp  | When the application instance was created.                      |
| default_runtime_context_device      | core | string     | The device's ID.                                                |
| default_runtime_context_device_name | core | string     | The device's bane.                                              |
| description                         | core | string     | The application instance's description.                         |
| health_status                       | core | string     | The application instance's health status.                       |
| last_updated_time                   | core | timestamp  | The application instance was updated.                           |
| name                                | core | string     | The application instance's name.                                |
| runtime_context_states              | core | json       | The application instance's state.                               |
| runtime_role_arn                    | core | string     | The application instance's runtime role ARN.                    |
| status                              | core | string     | The application instance's status.                              |
| status_description                  | core | string     | The application instance's status description.                  |
| tags                                | core | hstore_csv |
