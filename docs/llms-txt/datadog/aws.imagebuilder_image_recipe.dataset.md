# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.imagebuilder_image_recipe.dataset.md

---
title: EC2 Image Builder Image Recipe
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Image Builder Image Recipe
---

# EC2 Image Builder Image Recipe

An EC2 Image Builder Image Recipe in AWS defines the components, base image, and configuration details used to create a custom machine image. It acts as a blueprint that specifies how the image should be built, including software packages, updates, and settings. This recipe ensures consistency and repeatability when generating Amazon Machine Images (AMIs) or container images.

```
aws.imagebuilder_image_recipe
```

## Fields

| Title        | ID   | Type       | Data Type                                             | Description |
| ------------ | ---- | ---------- | ----------------------------------------------------- | ----------- |
| _key         | core | string     |
| account_id   | core | string     |
| image_recipe | core | json       | The image recipe object.                              |
| request_id   | core | string     | The request ID that uniquely identifies this request. |
| tags         | core | hstore_csv |
