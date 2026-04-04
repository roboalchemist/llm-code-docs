# Source: https://docs.datadoghq.com/containers/monitoring/amazon_elastic_container_explorer.md

---
title: Amazon Elastic Container (ECS) Explorer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Containers > Container Monitoring > Amazon Elastic Container (ECS)
  Explorer
---

# Amazon Elastic Container (ECS) Explorer

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/orch_ecs_ex.d4e092a9c47e1b17752d81c467fc8e15.png?auto=format"
   alt="ECS Explorer displaying ECS tasks." /%}

## Overview{% #overview %}

The Datadog Agent and Datadog Amazon ECS integration can retrieve ECS resources for the [ECS Explorer](https://app.datadoghq.com/orchestration/explorer/ecsTask). This feature enables you to monitor the status of EC2 and Fargate tasks, services, and other ECS components across all of your AWS accounts. You can view resource specifications for tasks within a service and correlate them with related logs, metrics, profiling, and more.

**Note**: The Datadog Agent only reports ECS tasks. Enable AWS Resource Collection to populate all ECS resources.

### Prerequisites{% #prerequisites %}

- **[AWS resource collection](https://docs.datadoghq.com/integrations/amazon_web_services/#resource-collection)**: Required for collecting ECS resources.
- **[ECS on EC2 integration](https://docs.datadoghq.com/integrations/amazon_ecs)**: Required for monitoring clusters using the EC2 launch type.
- **[ECS on Fargate integration](https://docs.datadoghq.com/integrations/ecs_fargate)**: Required for monitoring clusters using the Fargate launch type.
- **Datadog Agent version >= 7.58.0**: Recommended for a shorter refresh rate on the ECS Explorer page.

## Setup{% #setup %}

Ensure you have enabled [AWS resource collection](https://docs.datadoghq.com/integrations/amazon_web_services/#resource-collection), the [ECS on EC2 integration](https://docs.datadoghq.com/integrations/amazon_ecs), and the [ECS on Fargate integration](https://docs.datadoghq.com/integrations/ecs_fargate).

**Note**: The collection interval for these integrations is approximately 15 minutes. Datadog recommends installing the Datadog Agent in your ECS cluster to achieve a shorter collection interval of 15 seconds.

{% tab title="Task Definition" %}
If using the [task definition to install the Datadog Agent](https://docs.datadoghq.com/containers/amazon_ecs/?tab=awscli#setup), add this environment variable to the Datadog Agent container to activate this feature.

This feature is enabled by default in Datadog Agent version 7.64.0 and later.

```yaml
{
  "containerDefinitions": [
    {
      "name": "datadog-agent",
      "environment": [
        {
          "name": "DD_ECS_TASK_COLLECTION_ENABLED",
          "value": "true"
        }
        # (...)
      ]
      # (...)
    }
  ],
# (...)
}
```

{% /tab %}

{% tab title="Configuration File" %}
For manual configuration, include the following line in the Datadog Agent configuration file.

```yaml
ecs_task_collection_enabled: true
```

{% /tab %}

### Logs{% #logs %}

For ECS on Fargate, it is recommended to use the [AWS FireLens integration](https://docs.datadoghq.com/integrations/aws-fargate/?tab=webui#fluent-bit-and-firelens) built on Datadog's Fluent Bit output plugin to send logs to Datadog. To ensure that logs are properly correlated between ECS resources and the log explorer, set `dd_source` to `ecs`:

```
{
  "logConfiguration": {
    "logDriver": "awsfirelens",
    "options": {
      "Name": "datadog",
      "apikey": "<DATADOG_API_KEY>",
      "Host": "http-intake.logs.datadoghq.com",
      "dd_service": "...",
      "dd_source": "ecs",
      "dd_message_key": "log",
      "dd_tags": "...",
      "TLS": "on",
      "provider": "ecs"
    }
  }
}
```

## Usage{% #usage %}

### Views{% #views %}

Use the **Select Resources** dropdown menu in the top left corner of the page to switch between **Tasks**, **Services**, **Clusters**, and other ECS resources.

Each view includes a data table for organizing information by fields such as status, name, and AWS tags, along with a detailed Cluster Map to provide an overview of your tasks and ECS clusters.

Refer to Query filter details for information on filtering these views.

#### Group by functionality and facets{% #group-by-functionality-and-facets %}

Group tasks by tags for an aggregated view that helps you find information more efficiently. You can group tasks using the **Group by** bar located at the top right of the page or by clicking on a specific tag and finding the group by function in the context menu, as illustrated below.

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/orch_ecs_ex_groupby.da4bc88473307c020a8c89dfb5fd277e.png?auto=format"
   alt="Example of grouping by launch type" /%}

Additionally, use facets on the left side of the page to filter or group resources according to your interests, such as tasks with Fargate launch type.

{% video
   url="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/fargate.mp4" /%}

### Cluster map{% #cluster-map %}

The cluster map provides a comprehensive view of your tasks and ECS clusters, allowing you to see all resources on one screen with customizable groups and filters. You can also select which metrics to color the nodes.

To examine resources from the cluster map, click on any circle or group to display a detailed panel.

{% video
   url="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/ecs-cluster-map.mp4" /%}

### Information panel{% #information-panel %}

Click on any row in the table or any object in the Cluster Map to display detailed information about a specific resource in a side panel.

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/orch_ecs_ex_panel.bc0a542dfe485a7ed4b69b687fda023a.png?auto=format"
   alt="View of resources in the side panel, showing related resources." /%}

The **Task Definition** tab in the side panel shows the complete task definition.

For task definitions, it also provides a history of seven days, allowing you to view all task definition revisions used by running tasks over the past week and compare changes between them.

{% image
   source="https://datadog-docs.imgix.net/images/infrastructure/livecontainers/orch_ecs_ex_manifest_history.f525c8b5893b082ca1d3ced2adcf0226.png?auto=format"
   alt="View of resource details in the side panel, highlighting task definition history feature" /%}

Other tabs provide additional information for troubleshooting the selected resource:

- **Related Resources**: View all related resources in a tree structure.
- [**Logs**](https://docs.datadoghq.com/logs): Access logs from your container or resource. Click on any log entry to view the full log details in the Log Explorer.
- [**Metrics**](https://docs.datadoghq.com/metrics): View live metrics for your container or resource. You can maximize any graph for full-screen viewing, share a snapshot, or export it from this tab.
- [**APM**](https://docs.datadoghq.com/tracing): Access traces from your container or resource, including details such as date, service, duration, method, and status code.
- **Network**: View network performance metrics for a container or resource, including source and destination, sent and received volume, and throughput. Use the **Destination** field to filter by tags like `DNS` or `ip_type`, or use the **Group by** filter to group network data by tags, such as `task_name` or `service`.
- **Monitors**: View monitors that are tagged, scoped, or grouped for this resource.

## Query filter details{% #query-filter-details %}

You can refine displayed resources by entering a query in the **Filter by** search bar at the top left of the page. The query filtering operates similarly to the filtering in the [Kubernetes Explorer](https://docs.datadoghq.com/infrastructure/containers/orchestrator_explorer/?tab=manual#query-filter-details).

### AWS tags{% #aws-tags %}

In the ECS Explorer, you can use `tag#` to search across both Datadog tags and AWS tags.

### Extracted tags{% #extracted-tags %}

In addition to the tags you have [configured](https://docs.datadoghq.com/getting_started/tagging/assigning_tags/?tab=containerizedenvironments) in your Datadog Agent, Datadog generates additional tags based on resource attributes, which can assist in your searching and grouping needs. These tags are conditionally added to resources when relevant.

#### All resources{% #all-resources %}

All resources include the following tags:

- `aws_account`: AWS account ID
- `region`: AWS account region
- `<resource_name>_arn`: Resource ARN tags, such as `task_arn`, `task_definition_arn`, `service_arn`, and more.
- `ecs_<resource_name>`: Resource name tags, such as `ecs_task`, `ecs_task_definition`, `ecs_service`, and more.

#### Relationships{% #relationships %}

Related Resources are tagged in relation to one another. Some examples include:

- A task belonging to the "XYZ" service, with an ARN of `XYZ-ARN`, can have tags `ecs_service:xyz` and `service_arn:xyz-arn`.
- A service that is part of the "XYZ" cluster, identified by the ARN `XYZ-ARN`, can have tags `ecs_cluster:xyz` and `cluster_arn:xyz-arn`.

**Tip:** Use the filter query autocomplete feature to explore available related resource tags. Type `ecs_` to see suggested results.

#### Resource specific tags{% #resource-specific-tags %}

Some resources have specific tags. The following tags are available in addition to the shared tags mentioned above.

| Resource            | Extracted Tags                                                        |
| ------------------- | --------------------------------------------------------------------- |
| **Task**            | `task_family``task_version``task_launch_type`                         |
| **Task Definition** | `task_family``task_version``task_launch_type``task_definition_status` |
| **Service**         | `task_family``task_version``task_launch_type``service_status`         |

## Notes and known issues{% #notes-and-known-issues %}

- The Agent and AWS integration setup affects how often the ECS Explorer refreshes:

| **Resource**           | **Resource Collection With Datadog Agent** | **Resource Collection Without Datadog Agent** | **Datadog Agent Without Resource Collection** |
| ---------------------- | ------------------------------------------ | --------------------------------------------- | --------------------------------------------- |
| **Cluster**            | ~15 minutes                                | ~15 minutes                                   | Not Collected                                 |
| **Task**               | ~15 seconds                                | ~15 minutes                                   | ~15 seconds                                   |
| **Task Definition**    | ~15 seconds                                | ~15 minutes                                   | Not Collected                                 |
| **Service**            | ~15 seconds                                | ~15 minutes                                   | Not Collected                                 |
| **Container Instance** | ~15 minutes                                | ~15 minutes                                   | Not Collected                                 |

- A newly created ECS Service is typically collected within approximately 15 seconds. However, for status changes in an existing Service, a refresh within 15 seconds is not guaranteed.
- Installing the Datadog Agent in your cluster enables visibility into task lifecycle changes. Without the Datadog Agent, stopped tasks can appear as running for up to 15 minutes.
- Installing the Datadog Agent in your cluster provides additional, relevant host-level tags, such as `availability_zone`.

## Further reading{% #further-reading %}

- [Catch and remediate ECS issues faster with default monitors and the ECS Explorer](https://www.datadoghq.com/blog/ecs-default-monitors/)
- [Monitor ECS Managed Instances with Datadog](https://www.datadoghq.com/blog/ecs-managed-instances)
