# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.gamelift_location.dataset.md

---
title: GameLift Location
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > GameLift Location
---

# GameLift Location

This table represents the GameLift Location resource from Amazon Web Services.

```
aws.gamelift_location
```

## Fields

| Title         | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                      | Description |
| ------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key          | core | string     |
| account_id    | core | string     |
| location_arn  | core | string     | The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to a custom location resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:&lt;region&gt;::location/location-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912</code>. |
| location_name | core | string     | The location's name.                                                                                                                                                                                                                                                                                                                           |
| ping_beacon   | core | json       | Information about the UDP ping beacon for this location.                                                                                                                                                                                                                                                                                       |
| tags          | core | hstore_csv |
