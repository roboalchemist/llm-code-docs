# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.proton_environment_template_version.dataset.md

---
title: Proton Environment Template Version
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Proton Environment Template Version
---

# Proton Environment Template Version

Proton Environment Template Version in AWS Proton represents a specific version of an environment template that defines the infrastructure and resources for deploying and managing environments. It allows platform teams to create standardized, reusable templates with version control, ensuring consistency and governance across deployments. Each version can be reviewed, updated, and promoted to provide controlled evolution of environment definitions.

```
aws.proton_environment_template_version
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                               | Description |
| ------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| arn                       | core | string     | The Amazon Resource Name (ARN) of the version of an environment template.               |
| created_at                | core | timestamp  | The time when the version of an environment template was created.                       |
| description               | core | string     | A description of the minor version of an environment template.                          |
| last_modified_at          | core | timestamp  | The time when the version of an environment template was last modified.                 |
| major_version             | core | string     | The latest major version that's associated with the version of an environment template. |
| minor_version             | core | string     | The minor version of an environment template.                                           |
| recommended_minor_version | core | string     | The recommended minor version of the environment template.                              |
| schema                    | core | string     | The schema of the version of an environment template.                                   |
| status                    | core | string     | The status of the version of an environment template.                                   |
| status_message            | core | string     | The status message of the version of an environment template.                           |
| tags                      | core | hstore_csv |
| template_name             | core | string     | The name of the version of an environment template.                                     |
