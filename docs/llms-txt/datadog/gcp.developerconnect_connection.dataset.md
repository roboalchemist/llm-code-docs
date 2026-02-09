# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.developerconnect_connection.dataset.md

---
title: Developer Connect Connection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Developer Connect Connection
---

# Developer Connect Connection

Developer Connect Connection in Google Cloud is a resource that establishes a secure link between Google Cloud and external code repositories or developer tools. It enables integration with source control systems such as GitHub or Bitbucket, allowing Google Cloud services to access, build, and deploy code directly from these repositories.

```
gcp.developerconnect_connection
```

## Fields

| Title                        | ID   | Type          | Data Type                                                                                                                                                                                           | Description |
| ---------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string        |
| ancestors                    | core | array<string> |
| annotations                  | core | hstore        | Optional. Allows clients to store small amounts of arbitrary data.                                                                                                                                  |
| bitbucket_cloud_config       | core | json          | Configuration for connections to an instance of Bitbucket Clouds.                                                                                                                                   |
| bitbucket_data_center_config | core | json          | Configuration for connections to an instance of Bitbucket Data Center.                                                                                                                              |
| create_time                  | core | timestamp     | Output only. [Output only] Create timestamp                                                                                                                                                         |
| crypto_key_config            | core | json          | Optional. The crypto key configuration. This field is used by the Customer-Managed Encryption Keys (CMEK) feature.                                                                                  |
| datadog_display_name         | core | string        |
| delete_time                  | core | timestamp     | Output only. [Output only] Delete timestamp                                                                                                                                                         |
| disabled                     | core | bool          | Optional. If disabled is set to true, functionality is disabled for this connection. Repository based API methods and webhooks processing for repositories in this connection will be disabled.     |
| etag                         | core | string        | Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| git_proxy_config             | core | json          | Optional. Configuration for the git proxy feature. Enabling the git proxy allows clients to perform git operations on the repositories linked in the connection.                                    |
| github_config                | core | json          | Configuration for connections to github.com.                                                                                                                                                        |
| github_enterprise_config     | core | json          | Configuration for connections to an instance of GitHub Enterprise.                                                                                                                                  |
| gitlab_config                | core | json          | Configuration for connections to gitlab.com.                                                                                                                                                        |
| gitlab_enterprise_config     | core | json          | Configuration for connections to an instance of GitLab Enterprise.                                                                                                                                  |
| installation_state           | core | json          | Output only. Installation state of the Connection.                                                                                                                                                  |
| labels                       | core | array<string> | Optional. Labels as key value pairs                                                                                                                                                                 |
| name                         | core | string        | Identifier. The resource name of the connection, in the format `projects/{project}/locations/{location}/connections/{connection_id}`.                                                               |
| organization_id              | core | string        |
| parent                       | core | string        |
| project_id                   | core | string        |
| project_number               | core | string        |
| reconciling                  | core | bool          | Output only. Set to true when the connection is being set up or updated in the background.                                                                                                          |
| region_id                    | core | string        |
| resource_name                | core | string        |
| tags                         | core | hstore_csv    |
| uid                          | core | string        | Output only. A system-assigned unique identifier for the Connection.                                                                                                                                |
| update_time                  | core | timestamp     | Output only. [Output only] Update timestamp                                                                                                                                                         |
| zone_id                      | core | string        |
