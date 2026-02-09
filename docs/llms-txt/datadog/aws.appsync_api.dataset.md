# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.appsync_api.dataset.md

---
title: AppSync GraphQL API
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AppSync GraphQL API
---

# AppSync GraphQL API

AppSync GraphQL API is a managed service in AWS that allows you to build scalable GraphQL APIs by securely connecting to data sources like DynamoDB, Lambda, or HTTP endpoints. It handles real-time data synchronization, offline access, and subscriptions, making it easier to develop responsive applications without managing backend infrastructure.

```
aws.appsync_api
```

## Fields

| Title           | ID   | Type       | Data Type                                                                                                                                       | Description |
| --------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key            | core | string     |
| account_id      | core | string     |
| api_arn         | core | string     | The Amazon Resource Name (ARN) for the Api.                                                                                                     |
| api_id          | core | string     | The Api ID.                                                                                                                                     |
| created         | core | timestamp  | The date and time that the Api was created.                                                                                                     |
| dns             | core | hstore     | The DNS records for the API. This will include an HTTP and a real-time endpoint.                                                                |
| event_config    | core | json       | The Event API configuration. This includes the default authorization configuration for connecting, publishing, and subscribing to an Event API. |
| name            | core | string     | The name of the Api.                                                                                                                            |
| owner_contact   | core | string     | The owner contact information for the Api                                                                                                       |
| tags            | core | hstore_csv |
| waf_web_acl_arn | core | string     | The Amazon Resource Name (ARN) of the WAF web access control list (web ACL) associated with this Api, if one exists.                            |
| xray_enabled    | core | bool       | A flag indicating whether to use X-Ray tracing for this Api.                                                                                    |
