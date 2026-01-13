# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apigateway_usageplan.dataset.md

---
title: API Gateway Usage Plan
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > API Gateway Usage Plan
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.apigateway_usageplan.dataset/index.html
---

# API Gateway Usage Plan

This table represents the API Gateway Usage Plan resource from Amazon Web Services.

```
aws.apigateway_usageplan
```

## Fields

| Title        | ID   | Type   | Data Type                                                                                                                                         | Description |
| ------------ | ---- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key         | core | string |
| account_id   | core | string |
| api_stages   | core | json   | The associated API stages of a usage plan.                                                                                                        |
| description  | core | string | The description of a usage plan.                                                                                                                  |
| id           | core | string | The identifier of a UsagePlan resource.                                                                                                           |
| name         | core | string | The name of a usage plan.                                                                                                                         |
| product_code | core | string | The Amazon Web Services Marketplace product identifier to associate with the usage plan as a SaaS product on the Amazon Web Services Marketplace. |
| quota        | core | json   | The target maximum number of permitted requests per a given unit time interval.                                                                   |
| tags         | core | hstore |
| throttle     | core | json   | A map containing method level throttling information for API stage in a usage plan.                                                               |
