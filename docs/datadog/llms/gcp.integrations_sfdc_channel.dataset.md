# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.integrations_sfdc_channel.dataset.md

---
title: Salesforce Channel Connection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Salesforce Channel Connection
---

# Salesforce Channel Connection

Salesforce Channel Connection in Google Cloud is a resource that enables integration between Google Cloud services and Salesforce through Eventarc. It allows events from Salesforce to be received and processed by Google Cloud applications, enabling event-driven workflows across both platforms. This connection simplifies building automated processes that respond to Salesforce events in real time.

```
gcp.integrations_sfdc_channel
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                          | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| channel_topic        | core | string        | Required. The Channel topic defined by salesforce once an channel is opened                                                                                                                                        |
| create_time          | core | timestamp     | Output only. Time when the channel is created                                                                                                                                                                      |
| datadog_display_name | core | string        |
| delete_time          | core | timestamp     | Output only. Time when the channel was deleted. Empty if not deleted.                                                                                                                                              |
| description          | core | string        | Optional. The description for this channel                                                                                                                                                                         |
| gcp_display_name     | core | string        | Optional. Client level unique name/alias to easily reference a channel.                                                                                                                                            |
| is_active            | core | bool          | Output only. Indicated if a channel has any active integrations referencing it. Set to false when the channel is created, and set to true if there is any integration published with the channel configured in it. |
| labels               | core | array<string> |
| last_replay_id       | core | string        | Output only. Last sfdc messsage replay id for channel                                                                                                                                                              |
| name                 | core | string        | Resource name of the SFDC channel projects/{project}/locations/{location}/sfdcInstances/{sfdc_instance}/sfdcChannels/{sfdc_channel}.                                                                               |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. Time when the channel was last updated                                                                                                                                                                |
| zone_id              | core | string        |
