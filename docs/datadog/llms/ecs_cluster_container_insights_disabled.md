# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/ecs_cluster_container_insights_disabled.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/ecs_cluster_container_insights_disabled.md

---
title: ECS cluster with Container Insights disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > ECS cluster with Container Insights disabled
---

# ECS cluster with Container Insights disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `ab759fde-e1e8-4b0e-ad73-ba856e490ed8`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html#cfn-ecs-cluster-clustersettings)

### Description{% #description %}

Amazon ECS clusters should have Container Insights enabled to collect container-level metrics and logs for monitoring, performance troubleshooting, and security visibility.

The `ClusterSettings` property in `AWS::ECS::Cluster` resources must include a `ClusterSetting` with `Name` set to `containerInsights` and `Value` set to `enabled`. Resources missing `ClusterSettings` or without an entry setting `containerInsights` to `enabled` will be flagged.

Secure configuration example:

```yaml
MyCluster:
  Type: AWS::ECS::Cluster
  Properties:
    ClusterSettings:
      - Name: containerInsights
        Value: enabled
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
  ECSCluster:
    Type: 'AWS::ECS::Cluster'
    Properties:
      ClusterName: MyCluster
      ClusterSettings:
        - Name: containerInsights
          Value: enabled
      Tags:
        - Key: environment
          Value: production
```

```json
{
  "Resources": {
    "ECSCluster": {
      "Type": "AWS::ECS::Cluster",
      "Properties": {
        "ClusterName": "MyCluster",
        "ClusterSettings": [
          {
              "Name": "containerInsights",
              "Value": "enabled"
          }
        ],
        "Tags": [
          {
              "Key": "environment",
              "Value": "production"
          }
        ]
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "Resources": {
    "ECSCluster": {
      "Type": "AWS::ECS::Cluster",
      "Properties": {
        "ClusterName": "MyCluster",
        "ClusterSettings": [
          {
              "Name": "containerInsights",
              "Value": "disabled"
          }
        ],
        "Tags": [
          {
              "Key": "environment",
              "Value": "production"
          }
        ]
      }
    }
  }
}
```

```json
{
  "Resources": {
    "ECSCluster": {
      "Type": "AWS::ECS::Cluster",
      "Properties": {
        "ClusterName": "MyCluster",
        "ClusterSettings": [],
        "Tags": [
          {
              "Key": "environment",
              "Value": "production"
          }
        ]
      }
    }
  }
}
```

```yaml
Resources:
  ECSCluster:
    Type: 'AWS::ECS::Cluster'
    Properties:
      ClusterName: MyCluster
      Tags:
        - Key: environment
          Value: production
```
