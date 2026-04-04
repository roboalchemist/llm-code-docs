# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.cloudbuild_github_enterprise_config.dataset.md

---
title: GitHubEnterpriseConfig
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > GitHubEnterpriseConfig
---

# GitHubEnterpriseConfig

GitHubEnterpriseConfig in Google Cloud represents the configuration settings that connect a Google Cloud project or service with a GitHub Enterprise instance. It manages authentication, repository linking, and integration details to enable secure and automated interactions between GitHub Enterprise and Google Cloud services such as Cloud Build or Cloud Source Repositories.

```
gcp.cloudbuild_github_enterprise_config
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| app_id               | core | int64         | Required. The GitHub app id of the Cloud Build app on the GitHub Enterprise server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| create_time          | core | timestamp     | Output only. Time when the installation was associated with the project.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| datadog_display_name | core | string        |
| gcp_display_name     | core | string        | Optional. Name to display for this config.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| host_url             | core | string        | The URL of the github enterprise host the configuration is for.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| labels               | core | array<string> |
| name                 | core | string        | The full resource name for the GitHubEnterpriseConfig For example: "projects/{$project_id}/locations/{$location_id}/githubEnterpriseConfigs/{$config_id}"                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| organization_id      | core | string        |
| parent               | core | string        |
| peered_network       | core | string        | Optional. The network to be used when reaching out to the GitHub Enterprise server. The VPC network must be enabled for private service connection. This should be set if the GitHub Enterprise server is hosted on-premises and not reachable by public internet. If this field is left empty, no network peering will occur and calls to the GitHub Enterprise server will be made over the public internet. Must be in the format `projects/{project}/global/networks/{network}`, where {project} is a project number or id and {network} is the name of a VPC network in the project. |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| secrets              | core | json          | Optional. Names of secrets in Secret Manager.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ssl_ca               | core | string        | Optional. SSL certificate to use for requests to GitHub Enterprise.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
