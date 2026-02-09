# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.imagebuilder_public_image_recipe.dataset.md

---
title: EC2 Image Builder Public Image Recipe
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > EC2 Image Builder Public Image
  Recipe
---

# EC2 Image Builder Public Image Recipe

An EC2 Image Builder Public Image Recipe in AWS defines the configuration for building Amazon Machine Images (AMIs). It specifies the base image, software components, and settings used to create a reusable and versioned image. Public image recipes are shared by AWS or other publishers, allowing you to use pre-defined, tested configurations as a starting point for your own custom images.

```
aws.imagebuilder_public_image_recipe
```

## Fields

| Title        | ID   | Type       | Data Type                                             | Description |
| ------------ | ---- | ---------- | ----------------------------------------------------- | ----------- |
| _key         | core | string     |
| account_id   | core | string     |
| image_recipe | core | json       | The image recipe object.                              |
| request_id   | core | string     | The request ID that uniquely identifies this request. |
| tags         | core | hstore_csv |
