# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.codedeploy_deployment_config.dataset.md

---
title: CodeDeploy Deployment Config
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CodeDeploy Deployment Config
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.codedeploy_deployment_config.dataset/index.html
---

# CodeDeploy Deployment Config

CodeDeploy Deployment Config in AWS defines how deployments are carried out, specifying rules for updating instances or resources during an application deployment. It controls aspects like the minimum number of healthy instances that must remain available while new versions are deployed. This ensures application availability and reliability during updates.

```
aws.codedeploy_deployment_config
```

## Fields

| Title                  | ID   | Type      | Data Type                                                                                                                                      | Description |
| ---------------------- | ---- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string    |
| account_id             | core | string    |
| compute_platform       | core | string    | The destination platform type for the deployment (Lambda, Server, or ECS).                                                                     |
| create_time            | core | timestamp | The time at which the deployment configuration was created.                                                                                    |
| deployment_config_id   | core | string    | The deployment configuration ID.                                                                                                               |
| deployment_config_name | core | string    | The deployment configuration name.                                                                                                             |
| minimum_healthy_hosts  | core | json      | Information about the number or percentage of minimum healthy instances.                                                                       |
| tags                   | core | hstore    |
| traffic_routing_config | core | json      | The configuration that specifies how the deployment traffic is routed. Used for deployments with a Lambda or Amazon ECS compute platform only. |
| zonal_config           | core | json      | Information about a zonal configuration.                                                                                                       |
