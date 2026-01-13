# Source: https://docs.datadoghq.com/containers/amazon_ecs/managed_instances.md

---
title: Amazon ECS Managed Instances
description: >-
  Install and configure the Datadog Agent on Amazon Elastic Container Service
  Managed Instances
breadcrumbs: Docs > Container Monitoring > Amazon ECS > Amazon ECS Managed Instances
source_url: https://docs.datadoghq.com/amazon_ecs/managed_instances/index.html
---

# Amazon ECS Managed Instances

Datadog Container Monitoring enables visibility into applications running on [Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ManagedInstances.html).

### How it works{% #how-it-works %}

To monitor your ECS Managed Instances tasks with Datadog, run the Datadog Agent as a container in **same task definition** as your application container. When a Datadog Agent is run as an additional container within an ECS task definition, the Agent can use the task's [metadata endpoint](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-metadata-endpoint-v4-managed-instances-response.html) to collect data. This endpoint returns a Docker stats JSON for all containers associated with the task.

For more information about the collected Docker stats, see [Docker API: ContainerStats](https://docs.docker.com/reference/api/engine/version/v1.30/#tag/Container/operation/ContainerStats) in the Docker documentation.

## Setup{% #setup %}

{% alert level="info" %}
This setup requires Datadog Agent 7.73.0+.
{% /alert %}

The following instructions assume that you have configured an ECS Managed Instances cluster. See the [Amazon ECS Managed Instances documentation for creating a cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/getting-started-managed-instances.html).

1. Create an ECS Managed Instances task definition file
1. Register the task definition
1. Run the task as a replica service

### Create an ECS Managed Instances task definition file{% #create-an-ecs-managed-instances-task-definition-file %}

This ECS task definition launches the Datadog Agent container with the necessary configurations.

1. Download [datadog-agent-ecs-managed-instances-sidecar.json](https://docs.datadoghq.com/resources/json/datadog-agent-ecs-managed-instances-sidecar.json). This files provide minimal configuration for core infrastructure monitoring. For more sample task definition files with various features enabled, see the Set up additional Agent features section on this page.
1. Modify the task definition file:
   - Set the `DD_API_KEY` environment variable by replacing `<YOUR_DATADOG_API_KEY>` with the [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys) for your account. Alternatively, you can also [supply the ARN of a secret stored in AWS Secrets Manager](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data-tutorial.html).
   - Set the `DD_SITE` environment variable to your [Datadog site](https://docs.datadoghq.com/getting_started/site/). Your site is:
1. (Optional) To add an Agent health check, add the following line to your ECS task definition:
   ```json
   "healthCheck": {
     "retries": 3,
     "command": ["CMD-SHELL","agent health"],
     "timeout": 5,
     "interval": 30,
     "startPeriod": 15
   }
   ```

### Register the task definition{% #register-the-task-definition %}

{% tab title="AWS Console" %}

1. Log in to your [AWS Console](https://aws.amazon.com/console) and navigate to the Elastic Container Service section.
1. Select **Task Definitions** in the navigation pane. On the **Create new task definition** menu, select **Create new task definition with JSON**.
1. In the JSON editor box, paste the contents of your task definition file.
1. Select **Create**.

{% /tab %}

{% tab title="AWS CLI" %}
Use the [AWS CLI](https://aws.amazon.com/cli) to execute the following command:

```bash
aws ecs register-task-definition --cli-input-json file://<path to datadog-agent-ecs-managed-instances-sidecar.json>
```

{% /tab %}

### Run the task as a replica service{% #run-the-task-as-a-replica-service %}

Because ECS Managed Instances does not support daemon scheduling, run the task as a [replica service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_service-options.html#service_scheduler_replica).

{% tab title="AWS Console" %}

1. Log in to your [AWS Web Console](https://aws.amazon.com/console) and navigate to the Elastic Container Service section.
1. Choose the cluster to run the Datadog Agent on.
1. On the **Services** tab, click **Create**.
1. For **Task Definition**, select the task created in the previous steps.
1. Enter a **Service name**.
1. For **Launch type**, choose **Capacity Provider** and select the Manged Instance capacity provider tied to the cluster.
1. For **Number of tasks**, enter `1`. Click **Next step**.
1. Fill in the rest of the optional fields based on your preference.
1. Click **Next step**.
1. Click **Create service**.

{% /tab %}

{% tab title="AWS CLI" %}
Use the [AWS CLI](https://aws.amazon.com/cli) to execute the following command:

```bash
aws ecs create-service --cluster <CLUSTER_NAME> \
--service-name <SERVICE_NAME> \
--task-definition <TASK_DEFINITION_ARN> \
--desired-count 1 \
--network-configuration "awsvpcConfiguration={subnets=[subnet-abcd1234],securityGroups=[sg-abcd1234]}"
```

{% /tab %}

## Set up additional Datadog Agent features{% #set-up-additional-datadog-agent-features %}

### Metrics collection{% #metrics-collection %}

Docker labels are not supported for ECS Managed Instances. To provide a custom integration configuration, you must mount a configuration file directly onto the Datadog Agent container.

**Example**: Setting up a Datadog Agent with custom configuration files mounted

Create the following file structure:

```
|- datadog
  |- Dockerfile
  |- conf.d
    |-redis.yaml
```

The `redis.yaml` file contains the configurations for the [Redis](https://docs.datadoghq.com/integrations/redis/?tab=ecs) integration.

In the `redis.yaml` file:

```yaml
ad_identifiers:
  - redis

init_config:

instances:
    - host: %%host%%
      port: 6379
```

The `Dockerfile` is used to build a Datadog Agent image and include the `redis.yaml` file at the correct location:

In the `Dockerfile` file:

```Dockerfile
FROM public.ecr.aws/datadog/agent:latest

COPY conf.d/ /etc/datadog-agent/conf.d/
```

After the image is built and pushed to an image registry, reference the custom image in the ECS task definition:

```
{
    "containerDefinitions": [
        {
            "image": "<registry-domain>/<namespace-or-account>/<repository>:<tag>",
            "name": "datadog-agent",
            ...
        }
    ],
    ...
}
```

### Trace collection (APM){% #trace-collection-apm %}

Instrument your application based on your setup:

| Language                                                                                                                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------- |
| [Java](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/java?tab=containers#automatic-instrumentation)                    |
| [Python](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/python?tab=containers#instrument-your-application)              |
| [Ruby](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/ruby#instrument-your-application)                                 |
| [Go](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/go/?tab=containers#activate-go-integrations-to-create-spans)        |
| [Node.js](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/nodejs?tab=containers#instrument-your-application)             |
| [PHP](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/php?tab=containers#automatic-instrumentation)                      |
| [C++](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/cpp?tab=containers#instrument-your-application)                    |
| [.NET Core](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/dotnet-core?tab=containers#custom-instrumentation)           |
| [.NET Framework](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/dotnet-framework?tab=containers#custom-instrumentation) |

#### UDP{% #udp %}

To collect traces over UDP, do not set `DD_AGENT_HOST`. Keep the default `localhost` value.

#### UDS{% #uds %}

To collect traces over UDS:

1. Add an empty volume onto the task definition using the `volumes` parameter.
1. Mount the volume onto the agent and application container using the `mountPoints` parameter.
1. Configure the environmental variable `DD_DOGSTATSD_SOCKET` on the application container and set it to `/var/run/datadog/dsd.socket`.

**Example**: Container definitions that configure collecting traces over UDS

```gdscript3
{
    "containerDefinitions": [
        {
            "image": "datadog/agent:latest",
            "mountPoints": [
                {
                    "containerPath": "/var/run/datadog",
                    "readOnly": false,
                    "sourceVolume": "dd-sockets"
                }
            ],
            "name": "datadog-agent",
            ...
            ...
        },
        {
            "environment": [
                {
                    "name": "DD_DOGSTATSD_SOCKET",
                    "value": "/var/run/datadog/dsd.socket"
                }
            ],
            "mountPoints": [
                {
                    "containerPath": "/var/run/datadog",
                    "readOnly": false,
                    "sourceVolume": "dd-sockets"
                }
            ],
            "name": "app",
            ...
            ...
        }
    ],
    ...
    "volumes": [
        {
            "host": {},
            "name": "dd-sockets"
        }
    ]
}
```

### Log collection{% #log-collection %}

The setup for log collection is identical to the setup for log collection in ECS Fargate. Follow the instructions in the [ECS Fargate documentation](https://docs.datadoghq.com/integrations/ecs_fargate/?tab=awscli#log-collection). These instructions give you the option to use either AWS FireLens in combination with Datadog's Fluent Bit output plugin, or the `awslogs` log driver.

### Process collection{% #process-collection %}

You can monitor processes in ECS Managed Instances in Datadog by using the [Live Processes page](https://docs.datadoghq.com/process). To enable process collection, add the [`PidMode` parameter](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html#task_definition_pidmode) in the task definition and set it to `task` as follows:

```
"pidMode": "task"
```

## Troubleshooting{% #troubleshooting %}

Need help? Contact [Datadog support](https://docs.datadoghq.com/help/).

## Further reading{% #further-reading %}

- [Collect your application logs](https://docs.datadoghq.com/agent/amazon_ecs/logs/)
- [Collect your application traces](https://docs.datadoghq.com/agent/amazon_ecs/apm/)
- [Collect ECS metrics](https://docs.datadoghq.com/agent/amazon_ecs/data_collected/#metrics)
- [Assign tags to all data emitted by a container](https://docs.datadoghq.com/agent/amazon_ecs/tags/)
- [Catch and remediate ECS issues faster with default monitors and the ECS Explorer](https://www.datadoghq.com/blog/ecs-default-monitors/)
