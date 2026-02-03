# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.greengrass_deployment.dataset.md

---
title: IoT Greengrass Deployment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT Greengrass Deployment
---

# IoT Greengrass Deployment

AWS IoT Greengrass Deployment is a resource that manages the distribution of software components, configurations, and machine learning models to Greengrass core devices. It allows you to define and deploy updates to edge devices securely and at scale, ensuring they can operate locally with cloud integration.

```
aws.greengrass_deployment
```

## Fields

| Title                 | ID   | Type       | Data Type                                                                                                                                                                      | Description |
| --------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                  | core | string     |
| account_id            | core | string     |
| components            | core | string     | The components to deploy. This is a dictionary, where each key is the name of a component, and each key's value is the version and configuration to deploy for that component. |
| created_at            | core | string     | The time, in milliseconds since the epoch, when the deployment was created.                                                                                                    |
| creation_timestamp    | core | timestamp  | The time at which the deployment was created, expressed in ISO 8601 format.                                                                                                    |
| deployment_arn        | core | string     | The ARN of the deployment.                                                                                                                                                     |
| deployment_id         | core | string     | The ID of the deployment.                                                                                                                                                      |
| deployment_name       | core | string     | The name of the deployment.                                                                                                                                                    |
| deployment_policies   | core | json       | The deployment policies for the deployment. These policies define how the deployment updates components and handles failure.                                                   |
| deployment_status     | core | string     | The status of the deployment.                                                                                                                                                  |
| deployment_type       | core | string     | The type of the deployment.                                                                                                                                                    |
| group_arn             | core | string     | The ARN of the group for this deployment.                                                                                                                                      |
| iot_job_arn           | core | string     | The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the IoT job that applies the deployment to target devices.                 |
| iot_job_configuration | core | json       | The job configuration for the deployment configuration. The job configuration specifies the rollout, timeout, and stop configurations for the deployment configuration.        |
| iot_job_id            | core | string     | The ID of the IoT job that applies the deployment to target devices.                                                                                                           |
| is_latest_for_target  | core | bool       | Whether or not the deployment is the latest revision for its target.                                                                                                           |
| parent_target_arn     | core | string     | The parent deployment's target <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> within a subdeployment.                            |
| revision_id           | core | string     | The revision number of the deployment.                                                                                                                                         |
| tags                  | core | hstore_csv |
| target_arn            | core | string     | The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the target IoT thing or thing group.                                       |
