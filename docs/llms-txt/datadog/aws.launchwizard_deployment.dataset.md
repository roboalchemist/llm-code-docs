# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.launchwizard_deployment.dataset.md

---
title: Launch Wizard Deployment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Launch Wizard Deployment
---

# Launch Wizard Deployment

Launch Wizard Deployment in AWS helps you easily deploy and configure enterprise applications such as Microsoft SQL Server or SAP on AWS infrastructure. It guides you through sizing, configuring, and launching resources based on best practices, while automating much of the setup. This reduces the complexity of provisioning and managing application environments.

```
aws.launchwizard_deployment
```

## Fields

| Title          | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                          | Description |
| -------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key           | core | string     |
| account_id     | core | string     |
| created_at     | core | timestamp  | The time the deployment was created.                                                                                                                                                                                                                                                                                                                                                                               |
| deleted_at     | core | timestamp  | The time the deployment was deleted.                                                                                                                                                                                                                                                                                                                                                                               |
| deployment_arn | core | string     | The Amazon Resource Name (ARN) of the deployment.                                                                                                                                                                                                                                                                                                                                                                  |
| id             | core | string     | The ID of the deployment.                                                                                                                                                                                                                                                                                                                                                                                          |
| name           | core | string     | The name of the deployment.                                                                                                                                                                                                                                                                                                                                                                                        |
| pattern_name   | core | string     | The pattern name of the deployment.                                                                                                                                                                                                                                                                                                                                                                                |
| resource_group | core | string     | The resource group of the deployment.                                                                                                                                                                                                                                                                                                                                                                              |
| specifications | core | hstore     | The settings specified for the deployment. These settings define how to deploy and configure your resources created by the deployment. For more information about the specifications required for creating a deployment for a SAP workload, see SAP deployment specifications. To retrieve the specifications required to create a deployment for other workloads, use the GetWorkloadDeploymentPattern operation. |
| status         | core | string     | The status of the deployment.                                                                                                                                                                                                                                                                                                                                                                                      |
| tags           | core | hstore_csv |
| workload_name  | core | string     | The name of the workload.                                                                                                                                                                                                                                                                                                                                                                                          |
