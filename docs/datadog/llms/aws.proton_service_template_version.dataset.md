# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.proton_service_template_version.dataset.md

---
title: Proton Service Template Version
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Proton Service Template Version
---

# Proton Service Template Version

Proton Service Template Version in AWS Proton represents a specific version of a service template that defines the infrastructure and resources needed to deploy and manage services. It allows platform teams to create standardized, reusable templates for service deployments, while application teams can use these versions to consistently provision and update their services.

```
aws.proton_service_template_version
```

## Fields

| Title                            | ID   | Type          | Data Type                                                                                                                                                                                                                                      | Description |
| -------------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                             | core | string        |
| account_id                       | core | string        |
| arn                              | core | string        | The Amazon Resource Name (ARN) of the version of a service template.                                                                                                                                                                           |
| compatible_environment_templates | core | json          | An array of compatible environment template names for the major version of a service template.                                                                                                                                                 |
| created_at                       | core | timestamp     | The time when the version of a service template was created.                                                                                                                                                                                   |
| description                      | core | string        | A description of the version of a service template.                                                                                                                                                                                            |
| last_modified_at                 | core | timestamp     | The time when the version of a service template was last modified.                                                                                                                                                                             |
| major_version                    | core | string        | The latest major version that's associated with the version of a service template.                                                                                                                                                             |
| minor_version                    | core | string        | The minor version of a service template.                                                                                                                                                                                                       |
| recommended_minor_version        | core | string        | The recommended minor version of the service template.                                                                                                                                                                                         |
| schema                           | core | string        | The schema of the version of a service template.                                                                                                                                                                                               |
| status                           | core | string        | The service template version status.                                                                                                                                                                                                           |
| status_message                   | core | string        | A service template version status message.                                                                                                                                                                                                     |
| supported_component_sources      | core | array<string> | An array of supported component sources. Components with supported sources can be attached to service instances based on this service template version. For more information about components, see Proton components in the Proton User Guide. |
| tags                             | core | hstore_csv    |
| template_name                    | core | string        | The name of the version of a service template.                                                                                                                                                                                                 |
