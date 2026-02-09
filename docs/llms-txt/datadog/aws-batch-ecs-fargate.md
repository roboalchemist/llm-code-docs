# Source: https://docs.datadoghq.com/containers/guide/aws-batch-ecs-fargate.md

---
title: AWS Batch with ECS Fargate and the Datadog Agent
description: >-
  Deploy the Datadog Agent alongside AWS Batch jobs running on ECS Fargate for
  comprehensive monitoring
breadcrumbs: >-
  Docs > Containers > Containers Guides > AWS Batch with ECS Fargate and the
  Datadog Agent
---

# AWS Batch with ECS Fargate and the Datadog Agent

You can run the Datadog Agent alongside your AWS Batch job containers by adding the container to your job definition.

## Prerequisites{% #prerequisites %}

- AWS Batch compute environment
- AWS Batch job queue associated with a compute environment

## Create the job definition{% #create-the-job-definition %}

{% tab title="AWS Web UI" %}

1. Log in to your [AWS Web Console](https://app.datadoghq.com/organization-settings/api-keys) and navigate to the AWS Batch section.
1. Click on **Job Definitions** in the left menu, then click the **Create** button or choose an existing AWS Batch job definition.
1. For new job definitions:
   1. Select **Fargate** as the orchestration type.
   1. Unselect **Use legacy containerProperties structure** option.
   1. Enter a **Job Definition Name**, such as `my-app-and-datadog`.
   1. Select an execution IAM role. See permission requirements in the Create or Modify your IAM Policy section below.
   1. Enable **Assign public IP** to allow outbound network access, then click the **Next** button.
   1. Configure the Datadog Agent container.
      1. For **Container name** enter `datadog-agent`.
      1. For **Image** enter `public.ecr.aws/datadog/agent:latest`.
      1. Configure **CPU** and **Memory** resource requirements based on your needs.
      1. For **Env Variables**, add the **Key** `DD_API_KEY` and enter your [Datadog API Key](https://app.datadoghq.com/organization-settings/api-keys) as the value.
      1. Add another environment variable using the **Key** `ECS_FARGATE` and the value `true`. Click **Add** to add the container.
      1. Add another environment variable using the **Key** `DD_SITE` and the value . This defaults to `datadoghq.com` if you don't set it.
   1. Add your other application containers to the job definition.
   1. AWS Batch supports [Fluent Bit and Firelens](https://aws.amazon.com/about-aws/whats-new/2025/04/aws-batch-amazon-elastic-container-service-exec-firelens-log-router/). To enable log collection for your application containers with Datadog:
      1. Create a separate log router container in the job definition.
      1. Configure the image `amazon/aws-for-fluent-bit:stable"` for the container.
      1. In the Firelens Configuration section:
         - Configure the **Type** to be `fluentbit`.
         - Configure the **Options** to include `enable-ecs-log-metadata` set to `true` to the **Name** and **Value** respectively
      1. For your application containers, in the Log Configuration section:
         - Configure the **Log Driver** to `awsfirelens`
         - Configure the **Options** to include the following **Name** and **Value** similar to Step 2 of the [ECS Fargate Fluent Bit and Firelens section](https://docs.datadoghq.com/integrations/ecs_fargate/?tab=webui#fluent-bit-and-firelens)
   1. Click **Create job definition** to create the job definition.

{% /tab %}

{% tab title="AWS CLI" %}

1. Download [datadog-agent-aws-batch-ecs-fargate.json](https://docs.datadoghq.com/resources/json/datadog-agent-aws-batch-ecs-fargate.json).

**Note**: If you are using Internet Explorer, this may download as a gzip file, which contains the JSON file mentioned below.

1. Update the JSON with a `JOB_DEFINITION_NAME`, your [Datadog API Key](https://app.datadoghq.com/organization-settings/api-keys), and the appropriate `DD_SITE` ().

**Note**: The environment variable `ECS_FARGATE` is already set to `"true"`.

1. Add your other application containers to the job definition.

1. AWS Batch supports [Fluent Bit and Firelens](https://aws.amazon.com/about-aws/whats-new/2025/04/aws-batch-amazon-elastic-container-service-exec-firelens-log-router/). To enable log collection for your application containers with Datadog:

   - In the JSON file, add an additional `log_router` container with the following in the `containers` section:
     ```json
      {
          "name": "log_router",
          "image": "amazon/aws-for-fluent-bit:stable",
          "essential": true,
          "firelensConfiguration": {
              "type": "fluentbit",
              "options": {
                  "enable-ecs-log-metadata": "true"
              }
          },
          "resourceRequirements": [
              {
                  "value": "0.25",
                  "type": "VCPU"
              },
              {
                  "value": "512",
                  "type": "MEMORY"
              }
          ]
      }
     ```
   - In your application containers, add the relevant `logConfiguration` options similar to Step 2 of the [ECS Fargate Fluent Bit and Firelens section](https://docs.datadoghq.com/integrations/ecs_fargate/?tab=webui#fluent-bit-and-firelens)

1. Execute the following command to register the job definition:

   ```bash
   aws batch register-job-definition --cli-input-json file://<PATH_TO_FILE>/datadog-agent-aws-batch-ecs-fargate.json
   ```

{% /tab %}

## Submit the AWS Batch job{% #submit-the-aws-batch-job %}

{% tab title="AWS Web UI" %}

1. Log in to your [AWS Web Console](https://aws.amazon.com/console) and navigate to the AWS Batch section. If needed, create a [compute environment](https://docs.aws.amazon.com/batch/latest/userguide/create-compute-environment.html) and/or [job queue](https://docs.aws.amazon.com/batch/latest/userguide/create-job-queue-fargate.html) associated with a compute environment.
1. On the **Jobs** tab, click the **Submit new job** button.
1. Enter a **Job name**.
1. For **Job Definition**, select the job created in the previous steps.
1. Choose the job queue to run the Datadog Agent on.
1. **Container overrides** are optional based on your preference.
1. Click the **Next** button, then click the **Create job** button.

{% /tab %}

{% tab title="AWS CLI" %}

1. Execute the following command to submit a job for your job definition:

```bash
aws batch submit-job --job-name <JOB_NAME> \
--job-queue <JOB_QUEUE_NAME> \
--job-definition <JOB_DEFINITION_NAME>:1
```

{% /tab %}

## Further Reading{% #further-reading %}

- [Amazon ECS on AWS Fargate with AWS Batch](https://docs.datadoghq.com/integrations/ecs_fargate/?tab=webui#aws-batch-on-ecs-fargate)
