# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apigateway_domainnameaccessassociation.dataset.md

---
title: API Gateway Domain Name Access Association
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > API Gateway Domain Name Access
  Association
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.apigateway_domainnameaccessassociation.dataset/index.html
---

# API Gateway Domain Name Access Association

This table represents the API Gateway Domain Name Access Association resource from Amazon Web Services.

```
aws.apigateway_domainnameaccessassociation
```

## Fields

| Title                              | ID   | Type   | Data Type                                                                                         | Description |
| ---------------------------------- | ---- | ------ | ------------------------------------------------------------------------------------------------- | ----------- |
| _key                               | core | string |
| access_association_source          | core | string | The ARN of the domain name access association source. For a VPCE, the ARN must be a VPC endpoint. |
| access_association_source_type     | core | string | The type of the domain name access association source.                                            |
| account_id                         | core | string |
| domain_name_access_association_arn | core | string | The ARN of the domain name access association resource.                                           |
| domain_name_arn                    | core | string | The ARN of the domain name.                                                                       |
| tags                               | core | hstore |
