# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.datasync_location_objectstorage.dataset.md

---
title: DataSync Location Object Storage
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DataSync Location Object Storage
---

# DataSync Location Object Storage

This table represents the DataSync Location Object Storage resource from Amazon Web Services.

```
aws.datasync_location_objectstorage
```

## Fields

| Title                 | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                    | Description |
| --------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string        |
| account_id            | core | string        |
| agent_arns            | core | array<string> | The ARNs of the DataSync agents that can connect with your object storage system.                                                                                                                                                                                                            |
| cmk_secret_config     | core | json          | Describes configuration information for a DataSync-managed secret, such as an authentication token or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed KMS key.                                                                          |
| creation_time         | core | timestamp     | The time that the location was created.                                                                                                                                                                                                                                                      |
| custom_secret_config  | core | json          | Describes configuration information for a customer-managed secret, such as an authentication token or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed KMS key.                                                                          |
| location_arn          | core | string        | The ARN of the object storage system location.                                                                                                                                                                                                                                               |
| location_uri          | core | string        | The URI of the object storage system location.                                                                                                                                                                                                                                               |
| managed_secret_config | core | json          | Describes configuration information for a DataSync-managed secret, such as an authentication token or set of credentials that DataSync uses to access a specific transfer location. DataSync uses the default Amazon Web Services-managed KMS key to encrypt this secret in Secrets Manager. |
| server_port           | core | int64         | The port that your object storage server accepts inbound network traffic on (for example, port 443).                                                                                                                                                                                         |
| server_protocol       | core | string        | The protocol that your object storage system uses to communicate.                                                                                                                                                                                                                            |
| tags                  | core | hstore_csv    |
