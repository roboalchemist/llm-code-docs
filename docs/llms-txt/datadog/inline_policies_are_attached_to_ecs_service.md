# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/inline_policies_are_attached_to_ecs_service.md

---
title: Inline policies are attached to an ECS service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Inline policies are attached to an ECS service
---

# Inline policies are attached to an ECS service

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `9e8c89b3-7997-4d15-93e4-7911b9db99fd`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html)

### Description{% #description %}

ECS services must reference an IAM role, not an IAM policy, because pointing the service `Role` property to a policy resource can break permission binding, make access controls harder to manage and audit, and increase the chance of privilege misconfiguration. Check `AWS::ECS::Service` resources' `Properties.Role`. The value must be a reference to an `AWS::IAM::Role` (logical ID or ARN) and must not be the logical ID of an `AWS::IAM::Policy` resource. Attach permissions to that role using `ManagedPolicyArns`, an `AWS::IAM::ManagedPolicy`, or inline policies defined on the `AWS::IAM::Role` itself. ECS services whose `Role` property refers to an `AWS::IAM::Policy` logical ID will be flagged.

Secure configuration example:

```yaml
MyEcsRole:
  Type: AWS::IAM::Role
  Properties:
    AssumeRolePolicyDocument:
      Statement:
        - Effect: Allow
          Principal:
            Service: ecs-tasks.amazonaws.com
          Action: sts:AssumeRole
    ManagedPolicyArns:
      - arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy

MyEcsService:
  Type: AWS::ECS::Service
  Properties:
    Role: !Ref MyEcsRole
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml

Resources:
  InlinePolicy:
    Type: AWS::ECS::Service
    DependsOn:
    - Listener
    Properties:
      LoadBalancers:
      - TargetGroupArn:
          Ref: TargetGroup
        ContainerPort: 80
        ContainerName: sample-app
      Cluster:
        Ref: ECSCluster
  IAMPolicy:
    Type: 'AWS::IAM::Policy'
    Properties:
      PolicyName: root
      PolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Action: '*'
            Resource: '*'
```

```json
{
  "Resources": {
    "IAMPolicy": {
      "Properties": {
        "PolicyName": "root",
        "PolicyDocument": {
          "Version": "2012-10-17T00:00:00Z",
          "Statement": [
            {
              "Effect": "Allow",
              "Action": "*",
              "Resource": "*"
            }
          ]
        }
      },
      "Type": "AWS::IAM::Policy"
    },
    "InlinePolicy": {
      "DependsOn": [
        "Listener"
      ],
      "Properties": {
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
        }
      },
      "Type": "AWS::ECS::Service"
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "Resources": {
    "InlinePolicy": {
      "Type": "AWS::ECS::Service",
      "DependsOn": [
        "Listener"
      ],
      "Properties": {
        "Role": {
          "Ref": "IAMPolicy"
        },
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
        }
      }
    },
    "IAMPolicy": {
      "Type": "AWS::IAM::Policy",
      "Properties": {
        "PolicyName": "root",
        "PolicyDocument": {
          "Version": "2012-10-17T00:00:00Z",
          "Statement": [
            {
              "Effect": "Allow",
              "Action": "*",
              "Resource": "*"
            }
          ]
        }
      }
    }
  }
}
```

```yaml
Resources:
  InlinePolicy:
    Type: AWS::ECS::Service
    DependsOn:
    - Listener
    Properties:
      Role:
        Ref: IAMPolicy
      LoadBalancers:
      - TargetGroupArn:
          Ref: TargetGroup
        ContainerPort: 80
        ContainerName: sample-app
      Cluster:
        Ref: ECSCluster
  IAMPolicy:
    Type: 'AWS::IAM::Policy'
    Properties:
      PolicyName: root
      PolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Action: '*'
            Resource: '*'
```
