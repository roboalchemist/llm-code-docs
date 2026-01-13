# Source: https://docs.datadoghq.com/containers/amazon_ecs.md

---
title: Amazon ECS
description: Install and configure the Datadog Agent on Amazon Elastic Container Service
breadcrumbs: Docs > Container Monitoring > Amazon ECS
source_url: https://docs.datadoghq.com/amazon_ecs/index.html
---

# Amazon ECS

## Overview{% #overview %}

Amazon ECS is a scalable, high-performance container orchestration service that supports Docker containers. With the Datadog Agent, you can monitor ECS containers and tasks on every EC2 instance in your cluster.

To configure Amazon ECS with Datadog, you can either use **Fleet Automation** or **install manually**. If you prefer to install manually, run one Agent container per Amazon EC2 host by creating a Datadog Agent task definition and deploying it as a daemon service. Each Agent then monitors the other containers on its host. See the Install manually section for more details.

## Fleet Automation setup{% #fleet-automation-setup %}

Follow the [in-app installation guide in Fleet Automation](https://app.datadoghq.com/fleet/install-agent/latest?platform=ecs) to complete setup on ECS. After completing the outlined steps in the in-app guide, [Fleet Automation](https://app.datadoghq.com/fleet/install-agent/latest?platform=ecs) generates a ready-to-use task definition or CloudFormation template, with your API key pre-injected.

{% image
   source="https://datadog-docs.imgix.net/images/agent/basic_agent_usage/ecs_install_page.f9eb4152161e990dc5f6843bc174cb41.png?auto=format"
   alt="In-app installation steps for the Datadog Agent on ECS." /%}

{% alert level="info" %}
If you want to monitor **ECS on Fargate**, see [Amazon ECS on AWS Fargate](https://docs.datadoghq.com/integrations/ecs_fargate/).
{% /alert %}

## Manual setup{% #manual-setup %}

To monitor your ECS containers and tasks, deploy the Datadog Agent as a container **once on each EC2 instance** in your ECS cluster. You can do this by creating a task definition for the Datadog Agent container and deploying it as a daemon service. Each Datadog Agent container then monitors the other containers on its respective EC2 instance.

The following instructions assume that you have configured an EC2 cluster. See the [Amazon ECS documentation for creating a cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-ec2-cluster-console-v2.html).

1. Create and add an ECS task definition
1. Schedule the Datadog Agent as a daemon service
1. (Optional) Set up additional Datadog Agent features

**Note:** Datadog's [Autodiscovery](https://docs.datadoghq.com/agent/autodiscovery/) can be used in conjunction with ECS and Docker to automatically discover and monitor running tasks in your environment.

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



## FIPS Compliance{% #fips-compliance %}

Some setup steps are different for FIPS compliance. Please take into account the specific setup instructions in the [FIPS Compliance](https://docs.datadoghq.com/agent/configuration/fips-compliance/) documentation.


{% /callout %}

### Create an ECS task definition{% #create-an-ecs-task-definition %}

This [ECS task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html) launches the Datadog Agent container with the necessary configurations. When you need to modify the Agent configuration, update this task definition and redeploy the daemon service. You can configure this task definition by using the AWS Management Console, or with the [AWS CLI](https://aws.amazon.com/cli).

The following sample is a minimal configuration for core infrastructure monitoring. However, additional Task Definition samples with various features enabled are provided in the Setup additional Agent features section if you want to use those instead.

#### Create and manage the task definition file{% #create-and-manage-the-task-definition-file %}

1. For Linux containers, download [datadog-agent-ecs.json](https://docs.datadoghq.com/resources/json/datadog-agent-ecs.json).

   - If you are using Amazon Linux 1 (AL1, formerly Amazon Linux AMI), use [datadog-agent-ecs1.json](https://docs.datadoghq.com/resources/json/datadog-agent-ecs1.json)
   - If you are using Windows, use [datadog-agent-ecs-win.json](https://docs.datadoghq.com/resources/json/datadog-agent-ecs-win.json)
Important alert (level: info): These files provide minimal configuration for core infrastructure monitoring. For more sample task definition files with various features enabled, see the Set up additional Agent features section on this page.
1. Edit your base task definition file

   - Set the `DD_API_KEY` environment variable by replacing `<YOUR_DATADOG_API_KEY>` with the [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys) for your account. Alternatively, you can also [supply the ARN of a secret stored in AWS Secrets Manager](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data-tutorial.html).

   - Set the `DD_SITE` environment variable to your [Datadog site](https://docs.datadoghq.com/getting_started/site/). Your site is: 
Important alert (level: info): If `DD_SITE` is not set, it defaults to the `US1` site, `datadoghq.com`.
   - Optionally, add a `DD_TAGS` environment variable to specify any additional tags.

1. (Optional) To deploy on an [ECS Anywhere cluster](https://www.datadoghq.com/blog/amazon-ecs-anywhere-monitoring/), add the following line to your ECS task definition:

   ```json
   "requiresCompatibilities": ["EXTERNAL"]
   ```

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

#### Register the task definition{% #register-the-task-definition %}

{% tab title="AWS CLI" %}
After you have created your task definition file, execute the following command to register the file in AWS.

```bash
aws ecs register-task-definition --cli-input-json file://<path to datadog-agent-ecs.json>
```

{% /tab %}

{% tab title="Web UI" %}
After you have your task definition file, use the AWS Console to register the file.

1. Log in to your AWS Console and navigate to the Elastic Container Service section.
1. Select **Task Definitions** in the navigation pane. On the **Create new task definition** menu, select **Create new task definition with JSON**.
1. In the JSON editor box, paste the contents of your task definition file.
1. Select **Create**.

{% /tab %}

### Run the Agent as a daemon service{% #run-the-agent-as-a-daemon-service %}

To have one Datadog Agent container running on each EC2 instance, run the Datadog Agent task definition as a [daemon service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html#service_scheduler_daemon).

#### Schedule a daemon service in AWS using Datadog's ECS task{% #schedule-a-daemon-service-in-aws-using-datadogs-ecs-task %}

1. Log in to the AWS Console and navigate to the ECS section. On the **Clusters** page, choose the cluster you run the Agent on.
1. On your cluster's **Services** tab, select **Create**.
1. Under **Deployment configuration**, for **Service type**, select **Daemon**.
1. You do not need to configure load balancing or autoscaling.
1. Click **Next Step**, and then **Create Service**.

### Set up additional Agent features{% #set-up-additional-agent-features %}

The task definition files provided in the previous section are minimal. These files deploy an Agent container with a base configuration to collect core metrics about the containers in your ECS cluster. The Agent can also run Agent integrations [based on Docker Labels](https://docs.datadoghq.com/containers/docker/integrations/?tab=docker) discovered on your containers.

For additional features:

#### APM{% #apm %}

Consult the [APM setup documentation](https://docs.datadoghq.com/containers/amazon_ecs/apm/) and the sample [datadog-agent-ecs-apm.json](https://docs.datadoghq.com/resources/json/datadog-agent-ecs-apm.json).

#### Log Management{% #log-management %}

Consult the [Log collection documentation](https://docs.datadoghq.com/containers/amazon_ecs/logs/) and the sample [datadog-agent-ecs-logs.json](https://docs.datadoghq.com/resources/json/datadog-agent-ecs-logs.json)

#### DogStatsD{% #dogstatsd %}

If you're using [DogStatsD](https://docs.datadoghq.com/developers/dogstatsd/?tab=containeragent), edit your Datadog Agent's container definition to add in host port mapping for 8125/udp and set the environment variable `DD_DOGSTATSD_NON_LOCAL_TRAFFIC` to `true`.:

```json
{
 "containerDefinitions": [
  {
   "name": "datadog-agent",
   (...)
   "portMappings": [
     {
      "hostPort": 8125,
      "protocol": "udp",
      "containerPort": 8125
     }
   ],
   "environment" : [
     {
       "name": "DD_API_KEY",
       "value": "<YOUR_DATADOG_API_KEY>"
     },
     {
       "name": "DD_SITE",
       "value": "datadoghq.com"
     },
     {
       "name": "DD_DOGSTATSD_NON_LOCAL_TRAFFIC",
       "value": "true"
     }
   ]
  }
 ],
 (...)
}
```

This setup allows DogStatsD traffic to be routed from the application containers, through the host and host port, to the Datadog Agent container. However, the application container must use the host's private IP address for this traffic. You can enable this by setting the environment variable `DD_AGENT_HOST` to the private IP address of the EC2 instance, which you can retrieve from the Instance Metadata Service (IMDS). Alternatively, you can set this in the code during initialization. The implementation for DogStatsD is the same as for APM. See [Configure the Trace Agent endpoint](https://docs.datadoghq.com/containers/amazon_ecs/apm/?tab=ec2metadataendpoint#configure-the-trace-agent-endpoint) for examples of setting the Agent endpoint.

Ensure that the security group settings on your EC2 instances do not publicly expose the ports for APM and DogStatsD.

#### Process collection{% #process-collection %}

To collect Live Process information for all your containers and send it to Datadog, update your task definition with the `DD_PROCESS_AGENT_ENABLED` environment variable:

```json
{
 "containerDefinitions": [
  {
   "name": "datadog-agent",
   (...)
   "environment" : [
     {
       "name": "DD_API_KEY",
       "value": "<YOUR_DATADOG_API_KEY>"
     },
     {
       "name": "DD_SITE",
       "value": "datadoghq.com"
     },
     {
       "name": "DD_PROCESS_AGENT_ENABLED",
       "value": "true"
     }
   ]
  }
 ],
 (...)
}
```

#### Cloud Network Monitoring{% #cloud-network-monitoring %}

{% alert level="danger" %}
This feature is only available for Linux.
{% /alert %}

Consult the sample [datadog-agent-sysprobe-ecs.json](https://docs.datadoghq.com/resources/json/datadog-agent-sysprobe-ecs.json) file.

If you are using Amazon Linux 1 (AL1, formerly Amazon Linux AMI), consult [datadog-agent-sysprobe-ecs1.json](https://docs.datadoghq.com/resources/json/datadog-agent-sysprobe-ecs1.json).

If you already have a task definition, update your file to include the following configuration:

```json
{
  "containerDefinitions": [
    (...)
      "mountPoints": [
        (...)
        {
          "containerPath": "/sys/kernel/debug",
          "sourceVolume": "debug"
        },
        (...)
      ],
      "environment": [
        (...)
        {
          "name": "DD_SYSTEM_PROBE_NETWORK_ENABLED",
          "value": "true"
        }
      ],
      "linuxParameters": {
       "capabilities": {
         "add": [
           "SYS_ADMIN",
           "SYS_RESOURCE",
           "SYS_PTRACE",
           "NET_ADMIN",
           "NET_BROADCAST",
           "NET_RAW",
           "IPC_LOCK",
           "CHOWN"
         ]
       }
     },
  ],
  "requiresCompatibilities": [
   "EC2"
  ],
  "volumes": [
    (...)
    {
     "host": {
       "sourcePath": "/sys/kernel/debug"
     },
     "name": "debug"
    },
    (...)
  ],
  "family": "datadog-agent-task"
}
```

#### Network Path{% #network-path %}

{% alert level="info" %}
Network Path for Datadog Cloud Network Monitoring is in Limited Availability. Reach out to your Datadog representative to sign up.
{% /alert %}

1. To enable [Network Path](https://docs.datadoghq.com/network_monitoring/network_path) on your ECS clusters, enable the `system-probe` traceroute module by adding the following environment variable in your `datadog-agent-sysprobe-ecs.json` file:

   ```json
      "environment": [
        (...)
        {
          "name": "DD_TRACEROUTE_ENABLED",
          "value": "true"
        }
      ],
   ```

1. To monitor individual paths, follow the instructions here to set up additional Agent features:

These files deploy an Agent container with a base configuration to collect core metrics about the containers in your ECS cluster. The Agent can also run Agent integrations based on Docker Labels discovered on your containers.

1. To monitor network traffic paths and allow the Agent to automatically discover and monitor network paths based on actual network traffic, without requiring you to specify endpoints manually, add the following additional environment variables to your `datadog-agent-sysprobe-ecs.json`:

   ```json
      "environment": [
        (...)
        {
          "name": "DD_NETWORK_PATH_CONNECTIONS_MONITORING_ENABLED",
          "value": "true"
        }
      ],
   ```

1. Optionally, to configure number of workers (default is 4) adjust the following environment variable in your `datadog-agent-sysprobe-ecs.json` file:

   ```json
      "environment": [
        (...)
        {
          "name": "DD_NETWORK_PATH_COLLECTOR_WORKERS",
          "value": "10"
        }
      ],
   ```

## AWSVPC mode{% #awsvpc-mode %}

For Agent v6.10+, `awsvpc` mode is supported for applicative containers, provided that security groups are set to allow the host instance's security group to reach the applicative containers on relevant ports.

You can run the Agent in `awsvpc` mode, but Datadog does not recommend this because it may be difficult to retrieve the ENI IP to reach the Agent for DogStatsD metrics and APM traces. Instead, run the Agent in bridge mode with port mapping to allow easier retrieval of [host IP through the metadata server](https://docs.datadoghq.com/containers/amazon_ecs/apm/).

## Troubleshooting{% #troubleshooting %}

Need help? Contact [Datadog support](https://docs.datadoghq.com/help/).

## Further reading{% #further-reading %}

- [Monitor ECS Managed Instances with Datadog](https://www.datadoghq.com/blog/ecs-managed-instances)
- [Collect your application logs](https://docs.datadoghq.com/agent/amazon_ecs/logs/)
- [Collect your application traces](https://docs.datadoghq.com/agent/amazon_ecs/apm/)
- [Collect ECS metrics](https://docs.datadoghq.com/agent/amazon_ecs/data_collected/#metrics)
- [Announcing support for Amazon ECS Anywhere](https://www.datadoghq.com/blog/amazon-ecs-anywhere-monitoring/)
- [Understand your Kubernetes and ECS spend with Datadog Cloud Cost Management](https://www.datadoghq.com/blog/cloud-cost-management-container-support/)
- [Catch and remediate ECS issues faster with default monitors and the ECS Explorer](https://www.datadoghq.com/blog/ecs-default-monitors/)
- [Using Datadog with ECS Fargate](https://www.datadoghq.com/architecture/using-datadog-with-ecs-fargate/)
