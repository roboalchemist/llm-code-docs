# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.deadline_license_endpoint.dataset.md

---
title: Deadline Cloud License Endpoint
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Deadline Cloud License Endpoint
---

# Deadline Cloud License Endpoint

Deadline Cloud License Endpoint in AWS provides the connection details required for render farm workers to access and use licensed software within AWS Deadline Cloud. It enables secure retrieval of license server information so that rendering jobs can run with the necessary third-party application licenses.

```
aws.deadline_license_endpoint
```

## Fields

| Title               | ID   | Type          | Data Type                                                               | Description |
| ------------------- | ---- | ------------- | ----------------------------------------------------------------------- | ----------- |
| _key                | core | string        |
| account_id          | core | string        |
| dns_name            | core | string        | The DNS name.                                                           |
| license_endpoint_id | core | string        | The license endpoint ID.                                                |
| security_group_ids  | core | array<string> | The security group IDs for the license endpoint.                        |
| status              | core | string        | The status of the license endpoint.                                     |
| status_message      | core | string        | The status message of the license endpoint.                             |
| subnet_ids          | core | array<string> | The subnet IDs.                                                         |
| tags                | core | hstore_csv    |
| vpc_id              | core | string        | The VCP(virtual private cloud) ID associated with the license endpoint. |
