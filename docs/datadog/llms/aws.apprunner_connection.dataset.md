# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apprunner_connection.dataset.md

---
title: App Runner Connection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > App Runner Connection
---

# App Runner Connection

App Runner Connection in AWS represents a link between App Runner and an external source code repository or service provider. It allows App Runner to securely access and deploy applications directly from repositories such as GitHub or Bitbucket. This connection manages authentication and permissions, enabling automated builds and deployments without requiring manual credential handling.

```
aws.apprunner_connection
```

## Fields

| Title           | ID   | Type       | Data Type                                                                                                                                | Description |
| --------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key            | core | string     |
| account_id      | core | string     |
| connection_arn  | core | string     | The Amazon Resource Name (ARN) of this connection.                                                                                       |
| connection_name | core | string     | The customer-provided connection name.                                                                                                   |
| created_at      | core | timestamp  | The App Runner connection creation time, expressed as a Unix time stamp.                                                                 |
| provider_type   | core | string     | The source repository provider.                                                                                                          |
| status          | core | string     | The current state of the App Runner connection. When the state is AVAILABLE, you can use the connection to create an App Runner service. |
| tags            | core | hstore_csv |
