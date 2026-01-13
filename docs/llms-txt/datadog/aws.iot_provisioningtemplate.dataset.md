# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iot_provisioningtemplate.dataset.md

---
title: Iot Provisioningtemplate
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Iot Provisioningtemplate
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iot_provisioningtemplate.dataset/index.html
---

# Iot Provisioningtemplate

This table represents the iot_provisioningtemplate resource from Amazon Web Services.

```
aws.iot_provisioningtemplate
```

## Fields

| Title                 | ID   | Type      | Data Type                                                                                                                                                                                                                                                                                                                                                                            | Description |
| --------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                  | core | string    |
| account_id            | core | string    |
| creation_date         | core | timestamp | The date when the provisioning template was created.                                                                                                                                                                                                                                                                                                                                 |
| default_version_id    | core | int64     | The default fleet template version ID.                                                                                                                                                                                                                                                                                                                                               |
| description           | core | string    | The description of the provisioning template.                                                                                                                                                                                                                                                                                                                                        |
| enabled               | core | bool      | True if the provisioning template is enabled, otherwise false.                                                                                                                                                                                                                                                                                                                       |
| last_modified_date    | core | timestamp | The date when the provisioning template was last modified.                                                                                                                                                                                                                                                                                                                           |
| pre_provisioning_hook | core | json      | Gets information about a pre-provisioned hook.                                                                                                                                                                                                                                                                                                                                       |
| provisioning_role_arn | core | string    | The ARN of the role associated with the provisioning template. This IoT role grants permission to provision a device.                                                                                                                                                                                                                                                                |
| tags                  | core | hstore    |
| template_arn          | core | string    | The ARN of the provisioning template.                                                                                                                                                                                                                                                                                                                                                |
| template_body         | core | string    | The JSON formatted contents of the provisioning template.                                                                                                                                                                                                                                                                                                                            |
| template_name         | core | string    | The name of the provisioning template.                                                                                                                                                                                                                                                                                                                                               |
| type                  | core | string    | The type you define in a provisioning template. You can create a template with only one type. You can't change the template type after its creation. The default value is <code>FLEET_PROVISIONING</code>. For more information about provisioning template, see: <a href="https://docs.aws.amazon.com/iot/latest/developerguide/provision-template.html">Provisioning template</a>. |
