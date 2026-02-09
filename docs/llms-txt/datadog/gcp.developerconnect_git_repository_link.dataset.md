# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.developerconnect_git_repository_link.dataset.md

---
title: Developer Connect Git Repository Link
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Developer Connect Git Repository
  Link
---

# Developer Connect Git Repository Link

Developer Connect Git Repository Link in Google Cloud is a resource that connects a Git repository from supported source control systems to Google Cloud Developer Connect. It enables seamless integration between your codebase and Google Cloud services, allowing automated builds, deployments, and continuous integration workflows. This link helps manage repository authentication, synchronization, and metadata to streamline development and delivery processes.

```
gcp.developerconnect_git_repository_link
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                           | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| annotations          | core | hstore        | Optional. Allows clients to store small amounts of arbitrary data.                                                                                                                                  |
| clone_uri            | core | string        | Required. Git Clone URI.                                                                                                                                                                            |
| create_time          | core | timestamp     | Output only. [Output only] Create timestamp                                                                                                                                                         |
| datadog_display_name | core | string        |
| delete_time          | core | timestamp     | Output only. [Output only] Delete timestamp                                                                                                                                                         |
| etag                 | core | string        | Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| git_proxy_uri        | core | string        | Output only. URI to access the linked repository through the Git Proxy. This field is only populated if the git proxy is enabled for the connection.                                                |
| labels               | core | array<string> | Optional. Labels as key value pairs                                                                                                                                                                 |
| name                 | core | string        | Identifier. Resource name of the repository, in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`.                                                                             |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| reconciling          | core | bool          | Output only. Set to true when the connection is being set up or updated in the background.                                                                                                          |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. A system-assigned unique identifier for the GitRepositoryLink.                                                                                                                         |
| update_time          | core | timestamp     | Output only. [Output only] Update timestamp                                                                                                                                                         |
| webhook_id           | core | string        | Output only. External ID of the webhook created for the repository.                                                                                                                                 |
| zone_id              | core | string        |
