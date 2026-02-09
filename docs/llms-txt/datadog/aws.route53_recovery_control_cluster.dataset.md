# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.route53_recovery_control_cluster.dataset.md

---
title: Route 53 Recovery Control Cluster
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Route 53 Recovery Control Cluster
---

# Route 53 Recovery Control Cluster

This table represents the Route 53 Recovery Control Cluster resource from Amazon Web Services.

```
aws.route53_recovery_control_cluster
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                                                                                                                                                                     | Description |
| ----------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| cluster_arn       | core | string     | The Amazon Resource Name (ARN) of the cluster.                                                                                                                                                                                                                |
| cluster_endpoints | core | json       | Endpoints for a cluster. Specify one of these endpoints when you want to set or retrieve a routing control state in the cluster. To get or update the routing control state, see the Amazon Route 53 Application Recovery Controller Routing Control Actions. |
| name              | core | string     | The name of the cluster.                                                                                                                                                                                                                                      |
| network_type      | core | string     | The network type of the cluster. NetworkType can be one of the following: IPV4, DUALSTACK.                                                                                                                                                                    |
| owner             | core | string     | The Amazon Web Services account ID of the cluster owner.                                                                                                                                                                                                      |
| status            | core | string     | Deployment status of a resource. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.                                                                                                                                                     |
| tags              | core | hstore_csv |
