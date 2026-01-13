# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.codeartifact_package.dataset.md

---
title: CodeArtifact Package
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CodeArtifact Package
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.codeartifact_package.dataset/index.html
---

# CodeArtifact Package

An AWS CodeArtifact Package represents a software package stored in a CodeArtifact repository. It contains metadata such as the package name, format, namespace, and available versions. This resource helps developers manage dependencies securely by storing, publishing, and sharing packages across teams and applications within AWS.

```
aws.codeartifact_package
```

## Fields

| Title                | ID   | Type   | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                            | Description |
| -------------------- | ---- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string |
| account_id           | core | string |
| format               | core | string | The format of the package.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| namespace            | core | string | The namespace of the package. The package component that specifies its namespace depends on its type. For example: The namespace of a Maven package version is its groupId. The namespace of an npm or Swift package version is its scope. The namespace of a generic package is its namespace. Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. |
| origin_configuration | core | json   | A PackageOriginConfiguration object that contains a PackageOriginRestrictions object that contains information about the upstream and publish package origin restrictions.                                                                                                                                                                                                                                                                           |
| package              | core | string | The name of the package.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| tags                 | core | hstore |
