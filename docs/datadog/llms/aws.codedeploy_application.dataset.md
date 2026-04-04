# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.codedeploy_application.dataset.md

---
title: CodeDeploy Application
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CodeDeploy Application
---

# CodeDeploy Application

An AWS CodeDeploy Application is a logical unit that defines the deployment configuration for your code. It serves as a container for deployment groups, which specify the target environments such as Amazon EC2 instances, on-premises servers, or Lambda functions. The application helps organize and manage deployments, ensuring that updates to your code are delivered consistently and reliably across your chosen infrastructure.

```
aws.codedeploy_application
```

## Fields

| Title                | ID   | Type       | Data Type                                                                                       | Description |
| -------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| application_id       | core | string     | The application ID.                                                                             |
| application_name     | core | string     | The application name.                                                                           |
| compute_platform     | core | string     | The destination platform type for deployment of the application (Lambda or Server).             |
| create_time          | core | timestamp  | The time at which the application was created.                                                  |
| git_hub_account_name | core | string     | The name for a connection to a GitHub account.                                                  |
| linked_to_git_hub    | core | bool       | True if the user has authenticated with GitHub for the specified application. Otherwise, false. |
| tags                 | core | hstore_csv |
