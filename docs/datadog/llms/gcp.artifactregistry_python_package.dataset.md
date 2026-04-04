# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.artifactregistry_python_package.dataset.md

---
title: Artifact Registry Python Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Artifact Registry Python Package
---

# Artifact Registry Python Package

Artifact Registry Python Package in Google Cloud is a managed service for storing, managing, and securing Python packages. It allows teams to host private Python repositories, control access with IAM, and integrate seamlessly with CI/CD pipelines. This helps ensure consistent and secure package distribution across development environments.

```
gcp.artifactregistry_python_package
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                         | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. Time the package was created.                                                                                                                                                                                                                                                                                                                                                                                                        |
| datadog_display_name | core | string        |
| labels               | core | array<string> |
| name                 | core | string        | Required. registry_location, project_id, repository_name and python_package forms a unique package name:`projects//locations//repository//pythonPackages/`. For example, "projects/test-project/locations/us-west4/repositories/test-repo/pythonPackages/ python_package:1.0.0", where "us-west4" is the registry_location, "test-project" is the project_id, "test-repo" is the repository_name and python_package:1.0.0" is the python package. |
| organization_id      | core | string        |
| package_name         | core | string        | Package for the artifact.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. Time the package was updated.                                                                                                                                                                                                                                                                                                                                                                                                        |
| uri                  | core | string        | Required. URL to access the package. Example: us-west4-python.pkg.dev/test-project/test-repo/python_package/file-name-1.0.0.tar.gz                                                                                                                                                                                                                                                                                                                |
| version              | core | string        | Version of this package.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| zone_id              | core | string        |
