# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.eventarc_trigger.dataset.md

---
title: Eventarc Trigger
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Eventarc Trigger
---

# Eventarc Trigger

Eventarc Trigger in Google Cloud is a resource that allows you to route events from various sources to Cloud Run, Workflows, or other event-driven services. It enables building loosely coupled, event-driven architectures by automatically delivering events based on defined filters and conditions.

```
gcp.eventarc_trigger
```

## Fields

| Title                   | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                         | Description |
| ----------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string        |
| ancestors               | core | array<string> |
| channel                 | core | string        | Optional. The name of the channel associated with the trigger in `projects/{project}/locations/{location}/channels/{channel}` format. You must provide a channel to receive events from Eventarc SaaS partners.                                                                                                                                                                                                   |
| create_time             | core | timestamp     | Output only. The creation time.                                                                                                                                                                                                                                                                                                                                                                                   |
| datadog_display_name    | core | string        |
| destination             | core | json          | Required. Destination specifies where the events should be sent to.                                                                                                                                                                                                                                                                                                                                               |
| etag                    | core | string        | Output only. This checksum is computed by the server based on the value of other fields, and might be sent only on create requests to ensure that the client has an up-to-date value before proceeding.                                                                                                                                                                                                           |
| event_data_content_type | core | string        | Optional. EventDataContentType specifies the type of payload in MIME format that is expected from the CloudEvent data field. This is set to `application/json` if the value is not defined.                                                                                                                                                                                                                       |
| event_filters           | core | json          | Required. Unordered list. The list of filters that applies to event attributes. Only events that match all the provided filters are sent to the destination.                                                                                                                                                                                                                                                      |
| labels                  | core | array<string> | Optional. User labels attached to the triggers that can be used to group resources.                                                                                                                                                                                                                                                                                                                               |
| name                    | core | string        | Required. The resource name of the trigger. Must be unique within the location of the project and must be in `projects/{project}/locations/{location}/triggers/{trigger}` format.                                                                                                                                                                                                                                 |
| organization_id         | core | string        |
| parent                  | core | string        |
| project_id              | core | string        |
| project_number          | core | string        |
| region_id               | core | string        |
| resource_name           | core | string        |
| satisfies_pzs           | core | bool          | Output only. Whether or not this Trigger satisfies the requirements of physical zone separation                                                                                                                                                                                                                                                                                                                   |
| service_account         | core | string        | Optional. The IAM service account email associated with the trigger. The service account represents the identity of the trigger. The `iam.serviceAccounts.actAs` permission must be granted on the service account to allow a principal to impersonate the service account. For more information, see the [Roles and permissions](/eventarc/docs/all-roles-permissions) page specific to the trigger destination. |
| tags                    | core | hstore_csv    |
| transport               | core | json          | Optional. To deliver messages, Eventarc might use other Google Cloud products as a transport intermediary. This field contains a reference to that transport intermediary. This information can be used for debugging purposes.                                                                                                                                                                                   |
| uid                     | core | string        | Output only. Server-assigned unique identifier for the trigger. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted.                                                                                                                                                                                                                                                     |
| update_time             | core | timestamp     | Output only. The last-modified time.                                                                                                                                                                                                                                                                                                                                                                              |
| zone_id                 | core | string        |
