# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ivs_ingest_configuration.dataset.md

---
title: Ivs Ingest Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Ivs Ingest Configuration
---

# Ivs Ingest Configuration

This table represents the ivs_ingest_configuration resource from Amazon Web Services.

```
aws.ivs_ingest_configuration
```

## Fields

| Title           | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                    | Description |
| --------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key            | core | string     |
| account_id      | core | string     |
| arn             | core | string     | Ingest configuration ARN.                                                                                                                                                                                                                                                                                                                                    |
| attributes      | core | hstore     | Application-provided attributes to to store in the IngestConfiguration and attach to a stage. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.</i>          |
| ingest_protocol | core | string     | Type of ingest protocol that the user employs for broadcasting.                                                                                                                                                                                                                                                                                              |
| name            | core | string     | Ingest name                                                                                                                                                                                                                                                                                                                                                  |
| participant_id  | core | string     | ID of the participant within the stage.                                                                                                                                                                                                                                                                                                                      |
| stage_arn       | core | string     | ARN of the stage with which the IngestConfiguration is associated.                                                                                                                                                                                                                                                                                           |
| state           | core | string     | State of the ingest configuration. It is <code>ACTIVE</code> if a publisher currently is publishing to the stage associated with the ingest configuration.                                                                                                                                                                                                   |
| tags            | core | hstore_csv |
| user_id         | core | string     | Customer-assigned name to help identify the participant using the IngestConfiguration; this can be used to link a participant to a user in the customer's own systems. This can be any UTF-8 encoded text. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.</i> |
