# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/dd/dd.apis.dataset.md

---
title: APIs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > APIs
---

# APIs

This table contains APIs, which are interfaces exposed by services for internal or external communication. Populated by [APM](https://docs.datadoghq.com/tracing/) or the [Software Catalog](https://docs.datadoghq.com/internal_developer_portal/software_catalog/).

```
dd.apis
```

## Fields

| Title                  | ID                     | Type | Data Type     | Description                                                                                                                                                                       |
| ---------------------- | ---------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                   | name                   | core | string        | The unique name assigned to the API, used for identification and categorization. It's meant to be both human-recognizable and machines to use it as a reference.                  |
| Display Name           | display_name           | core | string        | The preferred display name of entity, often used if the name field is overly technical or not descriptive.                                                                        |
| Description            | description            | core | string        | Provides detailed information about the function or purpose of the API.                                                                                                           |
| Tags                   | tags                   | core | hstore        | This field contains an array of tags, each represented as a key-value pair, used to categorize and provide metadata about the associated entity.                                  |
| Owner                  | owner                  | core | string        | Represents the handle for the team that owns the API.                                                                                                                             |
| Lifecycle              | lifecycle              | core | string        | Indicates the current stage of the API or product as defined by the owner, such as 'production', 'development', or 'stable'.                                                      |
| Tier                   | tier                   | core | string        | Indicates the classification or level of API as defined by the owner, which may affect priority or access. Common values include different tier levels such as Tier1, Tier2, etc. |
| Languages              | languages              | core | array<string> | The list of programming languages that the API is written in. Each element in the array represents a language used or supported.                                                  |
| Type                   | type                   | core | string        | Indicates the type of API specification, such as OpenAPI or AsyncAPI, used to define the service interface.                                                                       |
| Definition API Version | definition_api_version | core | string        | The version of the definition used to register the entity, often in the form of a YAML file in a repository.                                                                      |
| Pagerduty Service ID   | pagerduty_service_id   | core | string        | The PagerDuty service ID associated with this API for incident management.                                                                                                        |
| Interface File Ref     | interface_file_ref     | core | string        | Stores the URL link to the interface file, which provides the specification details for the API catalog.                                                                          |
| Interface Definition   | interface_definition   | core | string        | The definition of the API. This is OpenAPI for type:openapi. Other formats are not supported yet.                                                                                 |
