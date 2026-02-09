# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotfleethub_application.dataset.md

---
title: IoT Fleet Hub Application
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT Fleet Hub Application
---

# IoT Fleet Hub Application

IoT Fleet Hub Application in AWS is a managed service that lets you create web applications to monitor and interact with your IoT device fleets. It provides a centralized dashboard where you can view device health, status, and operational metrics without building custom interfaces. This helps simplify fleet management and improves visibility into connected devices.

```
aws.iotfleethub_application
```

## Fields

| Title                        | ID   | Type       | Data Type                                                                                                                                                                    | Description |
| ---------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string     |
| account_id                   | core | string     |
| application_arn              | core | string     | The ARN of the web application.                                                                                                                                              |
| application_creation_date    | core | int64      | The date (in Unix epoch time) when the application was created.                                                                                                              |
| application_description      | core | string     | An optional description of the web application.                                                                                                                              |
| application_id               | core | string     | The unique Id of the web application.                                                                                                                                        |
| application_last_update_date | core | int64      | The date (in Unix epoch time) when the application was last updated.                                                                                                         |
| application_name             | core | string     | The name of the web application.                                                                                                                                             |
| application_state            | core | string     | The current state of the web application.                                                                                                                                    |
| application_url              | core | string     | The URL of the web application.                                                                                                                                              |
| error_message                | core | string     | A message that explains any failures included in the applicationState response field. This message explains failures in the CreateApplication and DeleteApplication actions. |
| role_arn                     | core | string     | The ARN of the role that the web application assumes when it interacts with Amazon Web Services IoT Core.                                                                    |
| sso_client_id                | core | string     | The Id of the single sign-on client that you use to authenticate and authorize users on the web application.                                                                 |
| tags                         | core | hstore_csv |
