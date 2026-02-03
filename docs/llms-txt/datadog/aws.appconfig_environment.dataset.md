# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.appconfig_environment.dataset.md

---
title: AWS AppConfig Environment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AWS AppConfig Environment
---

# AWS AppConfig Environment

An AWS AppConfig Environment is a logical deployment space within AWS AppConfig where configuration profiles are deployed and managed. It represents a specific application stage, such as development, testing, or production, allowing controlled rollout and monitoring of configuration changes.

```
aws.appconfig_environment
```

## Fields

| Title          | ID   | Type       | Data Type                                                                                                                                         | Description |
| -------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key           | core | string     |
| account_id     | core | string     |
| application_id | core | string     | The application ID.                                                                                                                               |
| description    | core | string     | The description of the environment.                                                                                                               |
| id             | core | string     | The environment ID.                                                                                                                               |
| monitors       | core | json       | Amazon CloudWatch alarms monitored during the deployment.                                                                                         |
| name           | core | string     | The name of the environment.                                                                                                                      |
| state          | core | string     | The state of the environment. An environment can be in one of the following states: READY_FOR_DEPLOYMENT, DEPLOYING, ROLLING_BACK, or ROLLED_BACK |
| tags           | core | hstore_csv |
