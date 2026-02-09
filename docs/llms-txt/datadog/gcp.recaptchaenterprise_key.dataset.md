# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.recaptchaenterprise_key.dataset.md

---
title: reCAPTCHA Enterprise Key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > reCAPTCHA Enterprise Key
---

# reCAPTCHA Enterprise Key

reCAPTCHA Enterprise Key in Google Cloud is a security resource used to protect applications from fraudulent activity, spam, and abuse. It provides site keys and secret keys that integrate with reCAPTCHA Enterprise to verify user interactions, helping distinguish between real users and automated traffic. This key is required to enable reCAPTCHA checks on websites or mobile apps.

```
gcp.recaptchaenterprise_key
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                      | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| android_settings     | core | json          | Settings for keys that can be used by Android apps.                                            |
| create_time          | core | timestamp     | Output only. The timestamp corresponding to the creation of this key.                          |
| datadog_display_name | core | string        |
| express_settings     | core | json          | Settings for keys that can be used by reCAPTCHA Express.                                       |
| gcp_display_name     | core | string        | Required. Human-readable display name of this key. Modifiable by user.                         |
| ios_settings         | core | json          | Settings for keys that can be used by iOS apps.                                                |
| labels               | core | array<string> | Optional. See [Creating and managing labels] (https://cloud.google.com/recaptcha/docs/labels). |
| name                 | core | string        | Identifier. The resource name for the Key in the format `projects/{project}/keys/{key}`.       |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| testing_options      | core | json          | Optional. Options for user acceptance testing.                                                 |
| waf_settings         | core | json          | Optional. Settings for Web Application Firewall (WAF).                                         |
| web_settings         | core | json          | Settings for keys that can be used by websites.                                                |
| zone_id              | core | string        |
