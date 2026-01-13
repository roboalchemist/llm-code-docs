# Source: https://docs.datadoghq.com/cloud_cost_management/setup/aws.md

# Source: https://docs.datadoghq.com/account_management/billing/aws.md

---
title: AWS Integration Billing
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Account Management > Billing > AWS Integration Billing
source_url: https://docs.datadoghq.com/billing/aws/index.html
---

# AWS Integration Billing

## Overview{% #overview %}

Datadog bills for AWS hosts running the Datadog Agent and all EC2 instances picked up by the Datadog-AWS integration. **You are not billed twice** if you are running the Agent on an EC2 instance picked up by the AWS integration.

**IMPORTANT**: Datadog uses EC2 instance metadata to ensure you aren't billed twice for hosts both running the agent and being crawled by the AWS integration. If your EC2 instances are configured to require the use of [Instance Metadata Service Version 2 (IMDSv2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html), then you must set the parameter `ec2_prefer_imdsv2` to `true` in your [Agent configuration](https://github.com/DataDog/datadog-agent/blob/main/pkg/config/config_template.yaml) to avoid double-billing.

When you set up the Fargate and Lambda integration tiles, and any custom metrics, it impacts your Datadog bill.

Other AWS resources such as ELB, RDS, and DynamoDB are not part of monthly infrastructure billing, and configuration exclusions do not apply.

## AWS resource exclusion{% #aws-resource-exclusion %}

You can limit the AWS metrics collected for some services to specific resources. On the [Datadog-AWS integration page](https://app.datadoghq.com/integrations/amazon-web-services), select the AWS account and click on the **Metric Collection** tab. Under **Limit Metric Collection to Specific Resources** you can then limit metrics for one or more of EC2, Lambda, ELB, Application ELB, Network ELB, RDS, SQS, Step Functions, and CloudWatch custom metrics. Ensure that the tags added to this section are assigned to the corresponding resources on AWS.

**Note**: If using exclusion notation (`!`), ensure the resource lacks the specified tag.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/billing/aws-resource-exclusion.9f9985112d1b045593d21bb6c583888c.png?auto=format"
   alt="The metric collection tab of an AWS account within the Datadog AWS integration page showing the option to limit metric collection to specific resources with a dropdown menu to select AWS service and a field to add tags in key:value format" /%}

You can also limit AWS metrics using the [API](https://docs.datadoghq.com/api/latest/aws-integration/#set-an-aws-tag-filter).

**Note**: Only EC2 (hosts), Lambda (active functions), CloudWatch Custom Metrics (custom metrics), and [containers](https://docs.datadoghq.com/account_management/billing/containers/) are billable by Datadog. Metrics integrated for the other services you can filter do not incur Datadog charges.

### EC2{% #ec2 %}

EC2 metrics resource exclusion settings apply to both EC2 instances and any attached EBS volumes. When adding limits to existing AWS accounts within the integration page, the previously discovered instances could stay in the [Infrastructure List](https://docs.datadoghq.com/infrastructure/) for up to two hours. During the transition period, EC2 instances display a status of `???`. This does not count towards your billing.

Hosts with a running Agent still display and are included in billing. Use the limit option to restrict `aws.ec2.*` metrics collection from AWS and restrict the AWS resource EC2 instance hosts.

#### Examples{% #examples %}

The following filter excludes all EC2 instances that contain the tag `datadog:no`:

```
!datadog:no
```

The following filter *only* collects metrics from EC2 instances that contain the tag `datadog:monitored` **or** the tag `env:production` **or** an `instance-type` tag with a `c1.*` value **and not** a `region:us-east-1` tag:

```
datadog:monitored,env:production,instance-type:c1.*,!region:us-east-1
```

**Note**: In Datadog, uppercase letters are changed to lowercase letters and spaces are replaced with underscores. For example, to collect metrics from EC2 instances with the tag `Team:Frontend App`, in Datadog, the tag applied should be `team:frontend_app`.

### CloudWatch Metric Streams with Amazon Data Firehose{% #cloudwatch-metric-streams-with-amazon-data-firehose %}

You can optionally [send CloudWatch metrics to Datadog using CloudWatch Metric Streams and Amazon Data Firehose](https://docs.datadoghq.com/integrations/guide/aws-cloudwatch-metric-streams-with-kinesis-data-firehose/?tab=cloudformation#streaming-vs-polling) instead of using the default API polling method. Tag filtering configured in the AWS Integration tile **also applies** to CloudWatch Metric Streams.

## Check if a host is monitored by the Agent or AWS{% #check-if-a-host-is-monitored-by-the-agent-or-aws %}

In the Infrastructure Host list:

- **Monitored by AWS Integration**

If a host displays only the AWS logo, or if its metrics are limited to the `aws.*` namespace, it indicates that the host is monitored exclusively through the AWS integration.

  {% image
     source="https://datadog-docs.imgix.net/images/account_management/billing/infra-aws.653bb0e5b5a1abfc8db2eeb7533a259e.png?auto=format"
     alt="Infrastructure Host list showing multiple hosts with only the AWS logo, indicating monitoring through the AWS integration." /%}

- **Monitored by the Datadog Agent**

If a host displays the Datadog Agent logo but not the AWS logo, or if its metrics are collected from the Datadog Agent (such as `datadog.*`, `system.*`, etc.), it indicates that the host is being monitored by the Datadog Agent.

  {% image
     source="https://datadog-docs.imgix.net/images/account_management/billing/infra-agent.f0400a010ddf5616bf8c7f3428154126.png?auto=format"
     alt="Infrastructure Host List showing a host with the Datadog Agent logo but no AWS logo, indicating monitoring through the Datadog Agent." /%}

## Troubleshooting{% #troubleshooting %}

For technical questions, contact [Datadog support](https://docs.datadoghq.com/help/).

For billing questions, contact your [Customer Success](mailto:success@datadoghq.com) Manager.
