# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.medialive_sdi_source.dataset.md

---
title: Elemental MediaLive SDI Source
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Elemental MediaLive SDI Source
---

# Elemental MediaLive SDI Source

Elemental MediaLive SDI Source represents a live video input from an on-premises SDI (Serial Digital Interface) feed into AWS Elemental MediaLive. It allows broadcasters to ingest uncompressed video directly from professional video equipment into the cloud for real-time encoding and processing.

```
aws.medialive_sdi_source
```

## Fields

| Title      | ID   | Type          | Data Type                                                                                                                    | Description |
| ---------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key       | core | string        |
| account_id | core | string        |
| arn        | core | string        | The ARN of this SdiSource. It is automatically assigned when the SdiSource is created.                                       |
| id         | core | string        | The ID of the SdiSource. Unique in the AWS account.The ID is the resource-id portion of the ARN.                             |
| inputs     | core | array<string> | The list of inputs that are currently using this SDI source. This list will be empty if the SdiSource has just been deleted. |
| mode       | core | string        | Applies only if the type is QUAD. The mode for handling the quad-link signal QUADRANT or INTERLEAVE.                         |
| name       | core | string        | The name of the SdiSource.                                                                                                   |
| state      | core | string        | Specifies whether the SDI source is attached to an SDI input (IN_USE) or not (IDLE).                                         |
| tags       | core | hstore_csv    |
| type       | core | string        | Used in SdiSource, CreateSdiSourceRequest, UpdateSdiSourceRequest.                                                           |
