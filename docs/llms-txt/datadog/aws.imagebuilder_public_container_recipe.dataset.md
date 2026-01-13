# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.imagebuilder_public_container_recipe.dataset.md

---
title: Image Builder Public Container Recipe
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Image Builder Public Container
  Recipe
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.imagebuilder_public_container_recipe.dataset/index.html
---

# Image Builder Public Container Recipe

An Image Builder Public Container Recipe in AWS defines the configuration for building container images using EC2 Image Builder. It specifies details such as the base image, components, and settings required to produce a container image. Public container recipes are shared by AWS or other users, allowing you to reuse and customize them for your own container image pipelines.

```
aws.imagebuilder_public_container_recipe
```

## Fields

| Title            | ID   | Type   | Data Type                                             | Description |
| ---------------- | ---- | ------ | ----------------------------------------------------- | ----------- |
| _key             | core | string |
| account_id       | core | string |
| container_recipe | core | json   | The container recipe object that is returned.         |
| request_id       | core | string | The request ID that uniquely identifies this request. |
| tags             | core | hstore |
