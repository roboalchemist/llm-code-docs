# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iot_securityprofile.dataset.md

---
title: Iot Securityprofile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Iot Securityprofile
---

# Iot Securityprofile

This table represents the iot_securityprofile resource from Amazon Web Services.

```
aws.iot_securityprofile
```

## Fields

| Title                           | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                         | Description |
| ------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                            | core | string        |
| account_id                      | core | string        |
| additional_metrics_to_retain    | core | array<string> | <i>Please use <a>DescribeSecurityProfileResponse$additionalMetricsToRetainV2</a> instead.</i> A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's <code>behaviors</code>, but it is also retained for any metric specified here. |
| additional_metrics_to_retain_v2 | core | json          | A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's behaviors, but it is also retained for any metric specified here.                                                                                                            |
| alert_targets                   | core | string        | Where the alerts are sent. (Alerts are always sent to the console.)                                                                                                                                                                                                                               |
| behaviors                       | core | json          | Specifies the behaviors that, when violated by a device (thing), cause an alert.                                                                                                                                                                                                                  |
| creation_date                   | core | timestamp     | The time the security profile was created.                                                                                                                                                                                                                                                        |
| last_modified_date              | core | timestamp     | The time the security profile was last modified.                                                                                                                                                                                                                                                  |
| metrics_export_config           | core | json          | Specifies the MQTT topic and role ARN required for metric export.                                                                                                                                                                                                                                 |
| security_profile_arn            | core | string        | The ARN of the security profile.                                                                                                                                                                                                                                                                  |
| security_profile_description    | core | string        | A description of the security profile (associated with the security profile when it was created or updated).                                                                                                                                                                                      |
| security_profile_name           | core | string        | The name of the security profile.                                                                                                                                                                                                                                                                 |
| tags                            | core | hstore_csv    |
| version                         | core | int64         | The version of the security profile. A new version is generated whenever the security profile is updated.                                                                                                                                                                                         |
