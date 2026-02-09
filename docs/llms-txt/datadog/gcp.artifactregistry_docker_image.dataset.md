# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.artifactregistry_docker_image.dataset.md

---
title: Artifact Registry Docker Image
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Artifact Registry Docker Image
---

# Artifact Registry Docker Image

Artifact Registry Docker Image in Google Cloud is a managed service for storing, managing, and securing container images. It provides a central repository for Docker images, enabling teams to build, version, and deploy applications efficiently. Integrated with Google Cloud services, it supports fine-grained access control, vulnerability scanning, and regional replication for performance and compliance.

```
gcp.artifactregistry_docker_image
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| build_time           | core | timestamp     | The time this image was built. This field is returned as the 'metadata.buildTime' field in the Version resource. The build time is returned to the client as an RFC 3339 string, which can be easily used with the JavaScript Date constructor.                                                                                                                                                                                                                                                                                                            |
| datadog_display_name | core | string        |
| image_size_bytes     | core | int64         | Calculated size of the image. This field is returned as the 'metadata.imageSizeBytes' field in the Version resource.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| labels               | core | array<string> |
| media_type           | core | string        | Media type of this image, e.g. "application/vnd.docker.distribution.manifest.v2+json". This field is returned as the 'metadata.mediaType' field in the Version resource.                                                                                                                                                                                                                                                                                                                                                                                   |
| name                 | core | string        | Required. registry_location, project_id, repository_name and image id forms a unique image name:`projects//locations//repositories//dockerImages/`. For example, "projects/test-project/locations/us-west4/repositories/test-repo/dockerImages/ nginx@sha256:e9954c1fc875017be1c3e36eca16be2d9e9bccc4bf072163515467d6a823c7cf", where "us-west4" is the registry_location, "test-project" is the project_id, "test-repo" is the repository_name and "nginx@sha256:e9954c1fc875017be1c3e36eca16be2d9e9bccc4bf072163515467d6a823c7cf" is the image's digest. |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The time when the docker image was last updated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| upload_time          | core | timestamp     | Time the image was uploaded.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| uri                  | core | string        | Required. URL to access the image. Example: us-west4-docker.pkg.dev/test-project/test-repo/nginx@sha256:e9954c1fc875017be1c3e36eca16be2d9e9bccc4bf072163515467d6a823c7cf                                                                                                                                                                                                                                                                                                                                                                                   |
| zone_id              | core | string        |
