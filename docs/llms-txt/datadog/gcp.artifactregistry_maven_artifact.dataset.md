# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.artifactregistry_maven_artifact.dataset.md

---
title: Artifact Registry Maven Artifact
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Artifact Registry Maven Artifact
---

# Artifact Registry Maven Artifact

Artifact Registry Maven Artifact in Google Cloud is a resource that stores and manages Maven packages within Artifact Registry repositories. It allows developers to organize, version, and distribute Java artifacts securely and efficiently. This resource supports integration with build tools and CI/CD pipelines, enabling automated dependency management and artifact publishing.

```
gcp.artifactregistry_maven_artifact
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                        | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| artifact_id          | core | string        | Artifact ID for the artifact.                                                                                                                                                                                                                                                                                                                                                                                    |
| create_time          | core | timestamp     | Output only. Time the artifact was created.                                                                                                                                                                                                                                                                                                                                                                      |
| datadog_display_name | core | string        |
| group_id             | core | string        | Group ID for the artifact. Example: com.google.guava                                                                                                                                                                                                                                                                                                                                                             |
| labels               | core | array<string> |
| name                 | core | string        | Required. registry_location, project_id, repository_name and maven_artifact forms a unique artifact For example, "projects/test-project/locations/us-west4/repositories/test-repo/mavenArtifacts/ com.google.guava:guava:31.0-jre", where "us-west4" is the registry_location, "test-project" is the project_id, "test-repo" is the repository_name and "com.google.guava:guava:31.0-jre" is the maven artifact. |
| organization_id      | core | string        |
| parent               | core | string        |
| pom_uri              | core | string        | Required. URL to access the pom file of the artifact. Example: us-west4-maven.pkg.dev/test-project/test-repo/com/google/guava/guava/31.0/guava-31.0.pom                                                                                                                                                                                                                                                          |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. Time the artifact was updated.                                                                                                                                                                                                                                                                                                                                                                      |
| version              | core | string        | Version of this artifact.                                                                                                                                                                                                                                                                                                                                                                                        |
| zone_id              | core | string        |
