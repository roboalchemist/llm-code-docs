# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ivs_composition.dataset.md

---
title: Ivs Composition
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Ivs Composition
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ivs_composition.dataset/index.html
---

# Ivs Composition

This table represents the ivs_composition resource from Amazon Web Services.

```
aws.ivs_composition
```

## Fields

| Title        | ID   | Type      | Data Type                                                                                                                                                                           | Description |
| ------------ | ---- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key         | core | string    |
| account_id   | core | string    |
| arn          | core | string    | ARN of the Composition resource.                                                                                                                                                    |
| destinations | core | json      | Array of Destination objects. A Composition can contain either one destination (<code>channel</code> or <code>s3</code>) or two (one <code>channel</code> and one <code>s3</code>). |
| end_time     | core | timestamp | UTC time of the Composition end. This is an ISO 8601 timestamp; <i>note that this is returned as a string</i>.                                                                      |
| layout       | core | json      | Layout object to configure composition parameters.                                                                                                                                  |
| stage_arn    | core | string    | ARN of the stage used as input                                                                                                                                                      |
| start_time   | core | timestamp | UTC time of the Composition start. This is an ISO 8601 timestamp; <i>note that this is returned as a string</i>.                                                                    |
| state        | core | string    | State of the Composition.                                                                                                                                                           |
| tags         | core | hstore    |
