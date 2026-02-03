# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.discoveryengine_engine.dataset.md

---
title: Discovery Engine Engine
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Discovery Engine Engine
---

# Discovery Engine Engine

Discovery Engine Engine is a Google Cloud resource that provides the core configuration for Discovery Engine, a service used to build and manage search and recommendation systems. It defines the engine's type, data sources, and operational settings, enabling developers to deliver personalized and relevant search or recommendation experiences across websites and applications.

```
gcp.discoveryengine_engine
```

## Fields

| Title                              | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                | Description |
| ---------------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                               | core | string        |
| ancestors                          | core | array<string> |
| chat_engine_config                 | core | json          | Configurations for the Chat Engine. Only applicable if solution_type is SOLUTION_TYPE_CHAT.                                                                                                                                                                                                                                                                                                                                              |
| chat_engine_metadata               | core | json          | Output only. Additional information of the Chat Engine. Only applicable if solution_type is SOLUTION_TYPE_CHAT.                                                                                                                                                                                                                                                                                                                          |
| common_config                      | core | json          | Common config spec that specifies the metadata of the engine.                                                                                                                                                                                                                                                                                                                                                                            |
| create_time                        | core | timestamp     | Output only. Timestamp the Recommendation Engine was created at.                                                                                                                                                                                                                                                                                                                                                                         |
| data_store_ids                     | core | array<string> | Optional. The data stores associated with this engine. For SOLUTION_TYPE_SEARCH and SOLUTION_TYPE_RECOMMENDATION type of engines, they can only associate with at most one data store. If solution_type is SOLUTION_TYPE_CHAT, multiple DataStores in the same Collection can be associated here. Note that when used in CreateEngineRequest, one DataStore id must be provided as the system will use it for necessary initializations. |
| datadog_display_name               | core | string        |
| disable_analytics                  | core | bool          | Optional. Whether to disable analytics for searches performed on this engine.                                                                                                                                                                                                                                                                                                                                                            |
| gcp_display_name                   | core | string        | Required. The display name of the engine. Should be human readable. UTF-8 encoded string with limit of 1024 characters.                                                                                                                                                                                                                                                                                                                  |
| industry_vertical                  | core | string        | Optional. The industry vertical that the engine registers. The restriction of the Engine industry vertical is based on DataStore: Vertical on Engine has to match vertical of the DataStore linked to the engine.                                                                                                                                                                                                                        |
| labels                             | core | array<string> |
| media_recommendation_engine_config | core | json          | Configurations for the Media Engine. Only applicable on the data stores with solution_type SOLUTION_TYPE_RECOMMENDATION and IndustryVertical.MEDIA vertical.                                                                                                                                                                                                                                                                             |
| name                               | core | string        | Immutable. Identifier. The fully qualified resource name of the engine. This field must be a UTF-8 encoded string with a length limit of 1024 characters. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}` engine should be 1-63 characters, and valid characters are /a-z0-9*/. Otherwise, an INVALID_ARGUMENT error is returned.                                                            |
| organization_id                    | core | string        |
| parent                             | core | string        |
| project_id                         | core | string        |
| project_number                     | core | string        |
| region_id                          | core | string        |
| resource_name                      | core | string        |
| search_engine_config               | core | json          | Configurations for the Search Engine. Only applicable if solution_type is SOLUTION_TYPE_SEARCH.                                                                                                                                                                                                                                                                                                                                          |
| solution_type                      | core | string        | Required. The solutions of the engine.                                                                                                                                                                                                                                                                                                                                                                                                   |
| tags                               | core | hstore_csv    |
| update_time                        | core | timestamp     | Output only. Timestamp the Recommendation Engine was last updated.                                                                                                                                                                                                                                                                                                                                                                       |
| zone_id                            | core | string        |
