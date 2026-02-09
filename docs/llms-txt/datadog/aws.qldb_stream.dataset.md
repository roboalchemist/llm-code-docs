# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.qldb_stream.dataset.md

---
title: QLDB Stream
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > QLDB Stream
---

# QLDB Stream

This table represents the QLDB Stream resource from Amazon Web Services.

```
aws.qldb_stream
```

## Fields

| Title                 | ID   | Type       | Data Type                                                                                                                                                                                | Description |
| --------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string     |
| account_id            | core | string     |
| arn                   | core | string     | The Amazon Resource Name (ARN) of the QLDB journal stream.                                                                                                                               |
| creation_time         | core | timestamp  | The date and time, in epoch time format, when the QLDB journal stream was created. (Epoch time format is the number of seconds elapsed since 12:00:00 AM January 1, 1970 UTC.)           |
| error_cause           | core | string     | The error message that describes the reason that a stream has a status of <code>IMPAIRED</code> or <code>FAILED</code>. This is not applicable to streams that have other status values. |
| exclusive_end_time    | core | timestamp  | The exclusive date and time that specifies when the stream ends. If this parameter is undefined, the stream runs indefinitely until you cancel it.                                       |
| inclusive_start_time  | core | timestamp  | The inclusive start date and time from which to start streaming journal data.                                                                                                            |
| kinesis_configuration | core | json       | The configuration settings of the Amazon Kinesis Data Streams destination for a QLDB journal stream.                                                                                     |
| ledger_name           | core | string     | The name of the ledger.                                                                                                                                                                  |
| role_arn              | core | string     | The Amazon Resource Name (ARN) of the IAM role that grants QLDB permissions for a journal stream to write data records to a Kinesis Data Streams resource.                               |
| status                | core | string     | The current state of the QLDB journal stream.                                                                                                                                            |
| stream_id             | core | string     | The UUID (represented in Base62-encoded text) of the QLDB journal stream.                                                                                                                |
| stream_name           | core | string     | The user-defined name of the QLDB journal stream.                                                                                                                                        |
| tags                  | core | hstore_csv |
