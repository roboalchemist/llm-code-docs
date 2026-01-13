# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.imagebuilder_container_recipe.dataset.md

---
title: EC2 Image Builder Container Recipe
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Image Builder Container Recipe
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.imagebuilder_container_recipe.dataset/index.html
---

# EC2 Image Builder Container Recipe

EC2 Image Builder Container Recipe is an AWS resource that defines the components, base image, and configuration used to build and customize container images. It provides a blueprint for creating reproducible, secure, and version-controlled container images that can be deployed across environments.

```
aws.imagebuilder_container_recipe
```

## Fields

| Title            | ID   | Type   | Data Type                                             | Description |
| ---------------- | ---- | ------ | ----------------------------------------------------- | ----------- |
| _key             | core | string |
| account_id       | core | string |
| container_recipe | core | json   | The container recipe object that is returned.         |
| request_id       | core | string | The request ID that uniquely identifies this request. |
| tags             | core | hstore |
