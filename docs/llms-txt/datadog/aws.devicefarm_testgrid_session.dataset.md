# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.devicefarm_testgrid_session.dataset.md

---
title: Devicefarm Testgrid Session
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Devicefarm Testgrid Session
---

# Devicefarm Testgrid Session

This table represents the devicefarm_testgrid_session resource from Amazon Web Services.

```
aws.devicefarm_testgrid_session
```

## Fields

| Title               | ID   | Type       | Data Type                                                                 | Description |
| ------------------- | ---- | ---------- | ------------------------------------------------------------------------- | ----------- |
| _key                | core | string     |
| account_id          | core | string     |
| arn                 | core | string     | The ARN of the session.                                                   |
| billing_minutes     | core | float64    | The number of billed minutes that were used for this session.             |
| created             | core | timestamp  | The time that the session was started.                                    |
| ended               | core | timestamp  | The time the session ended.                                               |
| selenium_properties | core | string     | A JSON object of options and parameters passed to the Selenium WebDriver. |
| status              | core | string     | The state of the session.                                                 |
| tags                | core | hstore_csv |
