# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.greengrass_function_definition.dataset.md

---
title: Greengrass Function Definition
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Greengrass Function Definition
---

# Greengrass Function Definition

Greengrass Function Definition in AWS represents a collection of Lambda functions that can be deployed and run on Greengrass core devices. It defines the configuration and metadata for these functions, including versioning and deployment details, enabling edge devices to execute code locally while still integrating with AWS cloud services.

```
aws.greengrass_function_definition
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                        | Description |
| ---------------------- | ---- | ---------- | -------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| arn                    | core | string     | The ARN of the definition.                                                       |
| creation_timestamp     | core | string     | The time, in milliseconds since the epoch, when the definition was created.      |
| id                     | core | string     | The ID of the definition.                                                        |
| last_updated_timestamp | core | string     | The time, in milliseconds since the epoch, when the definition was last updated. |
| latest_version         | core | string     | The ID of the latest version associated with the definition.                     |
| latest_version_arn     | core | string     | The ARN of the latest version associated with the definition.                    |
| name                   | core | string     | The name of the definition.                                                      |
| tags                   | core | hstore_csv |
