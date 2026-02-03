# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.integrations_sfdc_instance.dataset.md

---
title: Salesforce Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Salesforce Instance
---

# Salesforce Instance

This table represents the Salesforce Instance resource from Google Cloud Platform.

```
gcp.integrations_sfdc_instance
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                   | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| auth_config_id       | core | array<string> | A list of AuthConfigs that can be tried to open the channel to SFDC                                                         |
| create_time          | core | timestamp     | Output only. Time when the instance is created                                                                              |
| datadog_display_name | core | string        |
| delete_time          | core | timestamp     | Output only. Time when the instance was deleted. Empty if not deleted.                                                      |
| description          | core | string        | Optional. A description of the sfdc instance.                                                                               |
| gcp_display_name     | core | string        | Optional. User selected unique name/alias to easily reference an instance.                                                  |
| labels               | core | array<string> |
| name                 | core | string        | Resource name of the SFDC instance projects/{project}/locations/{location}/sfdcInstances/{sfdcInstance}.                    |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| service_authority    | core | string        | Optional. URL used for API calls after authentication (the login authority is configured within the referenced AuthConfig). |
| sfdc_org_id          | core | string        | The SFDC Org Id. This is defined in salesforce.                                                                             |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. Time when the instance was last updated                                                                        |
| zone_id              | core | string        |
