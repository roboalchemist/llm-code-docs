# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.artifactregistry_npm_package.dataset.md

---
title: Artifact Registry NPM Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Artifact Registry NPM Package
---

# Artifact Registry NPM Package

Artifact Registry NPM Package in Google Cloud is a managed service for storing, managing, and securing Node.js packages. It allows teams to host private NPM repositories, control access with IAM, and integrate seamlessly with CI/CD pipelines. This helps ensure consistent package management and improved security across development environments.

```
gcp.artifactregistry_npm_package
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                           | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. Time the package was created.                                                                                                                                                                                                                                                                                                                          |
| datadog_display_name | core | string        |
| labels               | core | array<string> |
| name                 | core | string        | Required. registry_location, project_id, repository_name and npm_package forms a unique package For example, "projects/test-project/locations/us-west4/repositories/test-repo/npmPackages/ npm_test:1.0.0", where "us-west4" is the registry_location, "test-project" is the project_id, "test-repo" is the repository_name and npm_test:1.0.0" is the npm package. |
| organization_id      | core | string        |
| package_name         | core | string        | Package for the artifact.                                                                                                                                                                                                                                                                                                                                           |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. Time the package was updated.                                                                                                                                                                                                                                                                                                                          |
| version              | core | string        | Version of this package.                                                                                                                                                                                                                                                                                                                                            |
| zone_id              | core | string        |
