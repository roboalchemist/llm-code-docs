# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.appconfig_configurationprofile.dataset.md

---
title: Appconfig Configurationprofile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Appconfig Configurationprofile
---

# Appconfig Configurationprofile

This table represents the appconfig_configurationprofile resource from Amazon Web Services.

```
aws.appconfig_configurationprofile
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description |
| ------------------ | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| application_id     | core | string     | The application ID.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| description        | core | string     | The configuration profile description.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| id                 | core | string     | The configuration profile ID.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| kms_key_arn        | core | string     | The Amazon Resource Name of the Key Management Service key to encrypt new configuration data versions in the AppConfig hosted configuration store. This attribute is only used for <code>hosted</code> configuration types. To encrypt data managed in other configuration stores, see the documentation for how to specify an KMS key for that particular service.                                                                                              |
| kms_key_identifier | core | string     | The Key Management Service key identifier (key ID, key alias, or key ARN) provided when the resource was created or updated.                                                                                                                                                                                                                                                                                                                                     |
| location_uri       | core | string     | The URI location of the configuration.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| name               | core | string     | The name of the configuration profile.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| retrieval_role_arn | core | string     | The ARN of an IAM role with permission to access the configuration at the specified <code>LocationUri</code>.                                                                                                                                                                                                                                                                                                                                                    |
| tags               | core | hstore_csv |
| type               | core | string     | The type of configurations contained in the profile. AppConfig supports <code>feature flags</code> and <code>freeform</code> configurations. We recommend you create feature flag configurations to enable or disable new features and freeform configurations to distribute configurations to an application. When calling this API, enter one of the following values for <code>Type</code>: <code>AWS.AppConfig.FeatureFlags</code> <code>AWS.Freeform</code> |
| validators         | core | json       | A list of methods for validating the configuration.                                                                                                                                                                                                                                                                                                                                                                                                              |
