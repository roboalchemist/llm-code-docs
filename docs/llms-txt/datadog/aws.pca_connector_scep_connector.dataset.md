# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.pca_connector_scep_connector.dataset.md

---
title: PCA Connector Scep Connector
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > PCA Connector Scep Connector
---

# PCA Connector Scep Connector

This table represents the PCA Connector Scep Connector resource from Amazon Web Services.

```
aws.pca_connector_scep_connector
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                                                                                                                                                                                | Description |
| ------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| arn                       | core | string     | The Amazon Resource Name (ARN) of the connector.                                                                                                                                                                                         |
| certificate_authority_arn | core | string     | The Amazon Resource Name (ARN) of the connector's associated certificate authority.                                                                                                                                                      |
| created_at                | core | timestamp  | The date and time that the challenge was created.                                                                                                                                                                                        |
| endpoint                  | core | string     | The connector's HTTPS public SCEP URL.                                                                                                                                                                                                   |
| mobile_device_management  | core | json       | Contains settings relevant to the mobile device management system that you chose for the connector. If you didn't configure <code>MobileDeviceManagement</code>, then the connector is for general-purpose use and this object is empty. |
| open_id_configuration     | core | json       | Contains OpenID Connect (OIDC) parameters for use with Microsoft Intune.                                                                                                                                                                 |
| status                    | core | string     | The connector's status. Status can be creating, active, deleting, or failed.                                                                                                                                                             |
| status_reason             | core | string     | Information about why connector creation failed, if status is <code>FAILED</code>.                                                                                                                                                       |
| tags                      | core | hstore_csv |
| type                      | core | string     | The connector type.                                                                                                                                                                                                                      |
| updated_at                | core | timestamp  | The date and time that the challenge was updated.                                                                                                                                                                                        |
