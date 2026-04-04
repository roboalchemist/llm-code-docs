# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.iam_service_account_key.dataset.md

---
title: Service Account Key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Service Account Key
---

# Service Account Key

A Service Account Key in Google Cloud is a credential file that allows applications or services to authenticate as a service account. It contains private key information used to securely access Google Cloud resources without user interaction. These keys are typically used for server-to-server communication, automation, or workloads running outside Google Cloud. Proper management and rotation of keys are critical to maintain security.

```
gcp.iam_service_account_key
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                       | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| disabled             | core | bool          | The key status.                                                                                                                                                                                                                                                 |
| key_algorithm        | core | string        | Specifies the algorithm (and possibly key size) for the key.                                                                                                                                                                                                    |
| key_origin           | core | string        | The key origin.                                                                                                                                                                                                                                                 |
| key_type             | core | string        | The key type.                                                                                                                                                                                                                                                   |
| labels               | core | array<string> |
| name                 | core | string        | The resource name of the service account key in the following format `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}/keys/{key}`.                                                                                                                              |
| organization_id      | core | string        |
| parent               | core | string        |
| private_key_type     | core | string        | The output format for the private key. Only provided in `CreateServiceAccountKey` responses, not in `GetServiceAccountKey` or `ListServiceAccountKey` responses. Google never exposes system-managed private keys, and never retains user-managed private keys. |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| valid_after_time     | core | timestamp     | The key can be used after this timestamp.                                                                                                                                                                                                                       |
| valid_before_time    | core | timestamp     | The key can be used before this timestamp. For system-managed key pairs, this timestamp is the end time for the private key signing operation. The public key could still be used for verification for a few hours after this time.                             |
| zone_id              | core | string        |
