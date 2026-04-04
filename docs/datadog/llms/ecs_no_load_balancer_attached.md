# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/ecs_no_load_balancer_attached.md

---
title: ECS no load balancer attached
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > ECS no load balancer attached
---

# ECS no load balancer attached

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `fb2b0ecf-1492-491a-a70d-ba1df579175d`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html)

### Description{% #description %}

Amazon ECS services must be configured with a load balancer so traffic is distributed across tasks and a single task does not become a single point of failure for availability and scaling.

For `AWS::ECS::Service` resources, the `Properties.LoadBalancers` property must be defined and contain at least one entry. Resources missing this property or where `LoadBalancers` is an empty array will be flagged.

Each `LoadBalancers` entry should reference the service port mapping (for example, `ContainerName` and `ContainerPort`) or a `TargetGroupArn` when using an Application Load Balancer or Network Load Balancer so traffic can be routed to task containers.

Secure configuration example:

```yaml
MyEcsService:
  Type: AWS::ECS::Service
  Properties:
    Cluster: !Ref MyEcsCluster
    TaskDefinition: !Ref MyTaskDef
    LoadBalancers:
      - ContainerName: my-app-container
        ContainerPort: 80
        # or: TargetGroupArn: arn:aws:elasticloadbalancing:region:acct:targetgroup/...
    DesiredCount: 2
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
#this code is a correct code for which the query should not find any result
Resources:
  ECSService:
    Type: AWS::ECS::Service
    DependsOn:
    - Listener
    Properties:
      Role:
        Ref: ECSServiceRole
      TaskDefinition:
        Ref: ECSTaskDefinition
      DesiredCount: 1
      LoadBalancers:
      - TargetGroupArn:
          Ref: TargetGroup
        ContainerPort: 80
        ContainerName: sample-app
      Cluster:
        Ref: ECSCluster
```

```json
{
  "Resources": {
    "ECSService": {
      "Type": "AWS::ECS::Service",
      "DependsOn": [
        "Listener"
      ],
      "Properties": {
        "DesiredCount": 1,
        "LoadBalancers": [
          {
            "TargetGroupArn": {
              "Ref": "TargetGroup"
            },
            "ContainerPort": 80,
            "ContainerName": "sample-app"
          }
        ],
        "Cluster": {
          "Ref": "ECSCluster"
        },
        "Role": {
          "Ref": "ECSServiceRole"
        },
        "TaskDefinition": {
          "Ref": "ECSTaskDefinition"
        }
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "Resources": {
    "ECSService": {
      "DependsOn": [
        "Listener"
      ],
      "Properties": {
        "Role": {
          "Ref": "ECSServiceRole"
        },
        "TaskDefinition": {
          "Ref": "ECSTaskDefinition"
        },
        "DesiredCount": 1,
        "Cluster": {
          "Ref": "ECSCluster"
        }
      },
      "Type": "AWS::ECS::Service"
    },
    "ECSService2": {
      "Properties": {
        "TaskDefinition": {
          "Ref": "ECSTaskDefinition"
        },
        "DesiredCount": 1,
        "LoadBalancers": [],
        "Cluster": {
          "Ref": "ECSCluster"
        },
        "Role": {
          "Ref": "ECSServiceRole"
        }
      },
      "Type": "AWS::ECS::Service",
      "DependsOn": [
        "Listener"
      ]
    }
  }
}
```

```yaml
#this is a problematic code where the query should report a result(s)
Resources:
  ECSService:
    Type: AWS::ECS::Service
    DependsOn:
    - Listener
    Properties:
      Role:
        Ref: ECSServiceRole
      TaskDefinition:
        Ref: ECSTaskDefinition
      DesiredCount: 1
      Cluster:
        Ref: ECSCluster
  ECSService2:
    Type: AWS::ECS::Service
    DependsOn:
    - Listener
    Properties:
      Role:
        Ref: ECSServiceRole
      TaskDefinition:
        Ref: ECSTaskDefinition
      DesiredCount: 1
      LoadBalancers: []
      Cluster:
        Ref: ECSCluster
```
