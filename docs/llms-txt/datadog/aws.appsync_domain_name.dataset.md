# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.appsync_domain_name.dataset.md

---
title: AppSync Domain Name
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AppSync Domain Name
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.appsync_domain_name.dataset/index.html
---

# AppSync Domain Name

This table represents the AppSync Domain Name resource from Amazon Web Services.

```
aws.appsync_domain_name
```

## Fields

| Title               | ID   | Type   | Data Type                                                                                                                                                              | Description |
| ------------------- | ---- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string |
| account_id          | core | string |
| appsync_domain_name | core | string | The domain name that AppSync provides.                                                                                                                                 |
| certificate_arn     | core | string | The Amazon Resource Name (ARN) of the certificate. This can be an Certificate Manager (ACM) certificate or an Identity and Access Management (IAM) server certificate. |
| description         | core | string | A description of the <code>DomainName</code> configuration.                                                                                                            |
| domain_name         | core | string | The domain name.                                                                                                                                                       |
| domain_name_arn     | core | string | The Amazon Resource Name (ARN) of the domain name.                                                                                                                     |
| hosted_zone_id      | core | string | The ID of your Amazon Route&nbsp;53 hosted zone.                                                                                                                       |
| tags                | core | hstore |
