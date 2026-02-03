# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.pca_connector_ad_connector.dataset.md

---
title: PCA Connector Active Directory Connector
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > PCA Connector Active Directory
  Connector
---

# PCA Connector Active Directory Connector

This table represents the PCA Connector Active Directory Connector resource from Amazon Web Services.

```
aws.pca_connector_ad_connector
```

## Fields

| Title                                         | ID   | Type       | Data Type                                                                                                                                                                                 | Description |
| --------------------------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                          | core | string     |
| account_id                                    | core | string     |
| arn                                           | core | string     | The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html">CreateConnector</a>. |
| certificate_authority_arn                     | core | string     | The Amazon Resource Name (ARN) of the certificate authority being used.                                                                                                                   |
| certificate_enrollment_policy_server_endpoint | core | string     | Certificate enrollment endpoint for Active Directory domain-joined objects to request certificates.                                                                                       |
| created_at                                    | core | timestamp  | The date and time that the connector was created.                                                                                                                                         |
| directory_id                                  | core | string     | The identifier of the Active Directory.                                                                                                                                                   |
| status                                        | core | string     | Status of the connector. Status can be creating, active, deleting, or failed.                                                                                                             |
| status_reason                                 | core | string     | Additional information about the connector status if the status is failed.                                                                                                                |
| tags                                          | core | hstore_csv |
| updated_at                                    | core | timestamp  | The date and time that the connector was updated.                                                                                                                                         |
| vpc_information                               | core | json       | Information of the VPC and security group(s) used with the connector.                                                                                                                     |
