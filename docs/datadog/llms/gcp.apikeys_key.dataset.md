# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.apikeys_key.dataset.md

---
title: API Key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > API Key
---

# API Key

An API Key in Google Cloud is a simple encrypted string used to authenticate applications calling Google Cloud APIs. It identifies the calling project and helps control access to services without requiring user credentials. API Keys can be restricted by service, IP address, or application to enhance security.

```
gcp.apikeys_key
```

## Fields

| Title                 | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                        | Description |
| --------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                  | core | string        |
| ancestors             | core | array<string> |
| annotations           | core | hstore        | Annotations is an unstructured key-value map stored with a policy that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects.                                                                             |
| create_time           | core | timestamp     | Output only. A timestamp identifying the time this key was originally created.                                                                                                                                                                                                                   |
| datadog_display_name  | core | string        |
| delete_time           | core | timestamp     | Output only. A timestamp when this key was deleted. If the resource is not deleted, this must be empty.                                                                                                                                                                                          |
| etag                  | core | string        | Output only. A checksum computed by the server based on the current value of the Key resource. This may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. See https://google.aip.dev/154.                                                    |
| gcp_display_name      | core | string        | Human-readable display name of this key that you can modify. The maximum length is 63 characters.                                                                                                                                                                                                |
| key_string            | core | string        | Output only. An encrypted and signed value held by this key. This field can be accessed only through the `GetKeyString` method.                                                                                                                                                                  |
| labels                | core | array<string> |
| name                  | core | string        | Output only. The resource name of the key. The `name` has the form: `projects//locations/global/keys/`. For example: `projects/123456867718/locations/global/keys/b7ff1f9f-8275-410a-94dd-3855ee9b5dd2` NOTE: Key is a global resource; hence the only supported value for location is `global`. |
| organization_id       | core | string        |
| parent                | core | string        |
| project_id            | core | string        |
| project_number        | core | string        |
| region_id             | core | string        |
| resource_name         | core | string        |
| restrictions          | core | json          | Key restrictions.                                                                                                                                                                                                                                                                                |
| service_account_email | core | string        | Optional. The email address of [the service account](https://cloud.google.com/iam/docs/service-accounts) the key is bound to.                                                                                                                                                                    |
| tags                  | core | hstore_csv    |
| uid                   | core | string        | Output only. Unique id in UUID4 format.                                                                                                                                                                                                                                                          |
| update_time           | core | timestamp     | Output only. A timestamp identifying the time this key was last updated.                                                                                                                                                                                                                         |
| zone_id               | core | string        |
