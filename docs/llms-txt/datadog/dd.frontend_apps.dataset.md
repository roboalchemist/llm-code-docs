# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/dd/dd.frontend_apps.dataset.md

---
title: Frontend Apps
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Frontend Apps
---

# Frontend Apps

This table contains frontend applications, which are user-facing web, mobile, or desktop clients. Populated by [RUM](https://docs.datadoghq.com/real_user_monitoring/) or the [Software Catalog](https://docs.datadoghq.com/internal_developer_portal/software_catalog/).

```
dd.frontend_apps
```

## Fields

| Title                  | ID                     | Type | Data Type     | Description                                                                                                                                                                            |
| ---------------------- | ---------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                   | name                   | core | string        | The unique name assigned to the frontend, used for identification and categorization. It's meant to be both human-recognizable and machines to use it as a reference.                  |
| Display Name           | display_name           | core | string        | The preferred display name of entity, often used if the name field is overly technical or not descriptive.                                                                             |
| Description            | description            | core | string        | Provides detailed information about the function or purpose of the frontend.                                                                                                           |
| Tags                   | tags                   | core | hstore        | This field contains an array of tags, each represented as a key-value pair, used to categorize and provide metadata about the associated entity.                                       |
| Owner                  | owner                  | core | string        | Represents the handle for the team that owns the frontend.                                                                                                                             |
| Languages              | languages              | core | array<string> | The list of programming languages that the frontend is written in. Each element in the array represents a language used or supported.                                                  |
| Lifecycle              | lifecycle              | core | string        | Indicates the current stage of the frontend or product as defined by the owner, such as 'production', 'development', or 'stable'.                                                      |
| Tier                   | tier                   | core | string        | Indicates the classification or level of frontend as defined by the owner, which may affect priority or access. Common values include different tier levels such as Tier1, Tier2, etc. |
| Type                   | type                   | core | string        | Indicates the category or classification of the resource, such as web or mobile.                                                                                                       |
| Definition API Version | definition_api_version | core | string        | The version of the definition used to register the entity, often in the form of a YAML file in a repository.                                                                           |
| Pagerduty Service ID   | pagerduty_service_id   | core | string        | The PagerDuty service ID associated with this frontend app for incident management.                                                                                                    |
