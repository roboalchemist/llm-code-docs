# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.devicefarm_instanceprofile.dataset.md

---
title: Devicefarm Instanceprofile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Devicefarm Instanceprofile
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.devicefarm_instanceprofile.dataset/index.html
---

# Devicefarm Instanceprofile

This table represents the devicefarm_instanceprofile resource from Amazon Web Services.

```
aws.devicefarm_instanceprofile
```

## Fields

| Title                             | ID   | Type          | Data Type                                                                                                                                                                                                                              | Description |
| --------------------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                              | core | string        |
| account_id                        | core | string        |
| arn                               | core | string        | The Amazon Resource Name (ARN) of the instance profile.                                                                                                                                                                                |
| description                       | core | string        | The description of the instance profile.                                                                                                                                                                                               |
| exclude_app_packages_from_cleanup | core | array<string> | An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes. The list of packages is considered only if you set <code>packageCleanup</code> to <code>true</code>. |
| name                              | core | string        | The name of the instance profile.                                                                                                                                                                                                      |
| package_cleanup                   | core | bool          | When set to <code>true</code>, Device Farm removes app packages after a test run. The default value is <code>false</code> for private devices.                                                                                         |
| reboot_after_use                  | core | bool          | When set to <code>true</code>, Device Farm reboots the instance after a test run. The default value is <code>true</code>.                                                                                                              |
| tags                              | core | hstore        |
