# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/empty_roles_for_ecs_cluster_task_definitions.md

---
title: Empty roles for ECS cluster task definitions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Empty roles for ECS cluster task definitions
---

# Empty roles for ECS cluster task definitions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `7f384a5f-b5a2-4d84-8ca3-ee0a5247becb`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html)

### Description{% #description %}

ECS services must reference task definitions that assign a specific task role (`TaskRoleArn`) so containers run with scoped IAM credentials and follow the principle of least privilege.

If a task definition lacks `TaskRoleArn`, containers may run without credentials or inherit broader instance credentials (for the Amazon EC2 launch type). This can allow unnecessary access to AWS APIs, data exposure, or privilege escalation.

This rule checks `AWS::ECS::Service` resources' `Properties.TaskDefinition` and verifies the referenced `AWS::ECS::TaskDefinition` resource defines `Properties.TaskRoleArn` (an IAM role ARN or a `Ref` to an `AWS::IAM::Role`). Resources missing `TaskDefinition`, referencing a non-existent task definition, or referencing a task definition that does not define `TaskRoleArn` will be flagged. `TaskDefinition` may be specified as a resource name string or as a `Ref` object.

Secure example with a task role referenced:

```yaml
MyTaskRole:
  Type: AWS::IAM::Role
  Properties:
    AssumeRolePolicyDocument: {...}

MyTaskDef:
  Type: AWS::ECS::TaskDefinition
  Properties:
    TaskRoleArn: !Ref MyTaskRole
    ContainerDefinitions: [...]

MyService:
  Type: AWS::ECS::Service
  Properties:
    TaskDefinition: !Ref MyTaskDef
    Cluster: !Ref MyCluster
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
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
  ECSTaskDefinition:
    Type: AWS::ECS::TaskDefinition
    Properties:
      Family: !Ref 'ServiceName'
      Cpu: !Ref 'ContainerCpu'
      Memory: !Ref 'ContainerMemory'
      NetworkMode: awsvpc
      RequiresCompatibilities:
        - FARGATE
      ExecutionRoleArn:
        Fn::ImportValue:
          !Join [':', [!Ref 'StackName', 'ECSTaskExecutionRole']]
      TaskRoleArn:
        Fn::If:
          - 'HasCustomRole'
          - !Ref 'Role'
          - !Ref "AWS::NoValue"
      ContainerDefinitions:
        - Name: !Ref 'ServiceName'
          Cpu: !Ref 'ContainerCpu'
          Memory: !Ref 'ContainerMemory'
          Image: !Ref 'ImageUrl'
          PortMappings:
            - ContainerPort: !Ref 'ContainerPort'
```

```json
{
  "Resources": {
    "ECSTaskDefinition": {
      "Properties": {
        "Memory": "ContainerMemory",
        "NetworkMode": "awsvpc",
        "RequiresCompatibilities": [
          "FARGATE"
        ],
        "ExecutionRoleArn": {
          "Fn::ImportValue": [
            ":",
            [
              "StackName",
              "ECSTaskExecutionRole"
            ]
          ]
        },
        "TaskRoleArn": {
          "Fn::If": [
            "HasCustomRole",
            "Role",
            "AWS::NoValue"
          ]
        },
        "ContainerDefinitions": [
          {
            "Name": "ServiceName",
            "Cpu": "ContainerCpu",
            "Memory": "ContainerMemory",
            "Image": "ImageUrl",
            "PortMappings": [
              {
                "ContainerPort": "ContainerPort"
              }
            ]
          }
        ],
        "Family": "ServiceName",
        "Cpu": "ContainerCpu"
      },
      "Type": "AWS::ECS::TaskDefinition"
    },
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
    "InvalidTaskDefinition": {
      "DependsOn": [
        "Listener"
      ],
      "Properties": {
        "Role": {
          "Ref": "ECSServiceRole"
        },
        "TaskDefinition": {
          "Ref": "MissingTaskDefinition"
        },
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
        }
      },
      "Type": "AWS::ECS::Service"
    },
    "TaskNoRole": {
      "Type": "AWS::ECS::Service",
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
        "LoadBalancers": [
          {
            "ContainerPort": 80,
            "ContainerName": "sample-app",
            "TargetGroupArn": {
              "Ref": "TargetGroup"
            }
          }
        ],
        "Cluster": {
          "Ref": "ECSCluster"
        }
      }
    },
    "ECSTaskDefinition": {
      "Type": "AWS::ECS::TaskDefinition",
      "Properties": {
        "ContainerDefinitions": [
          {
            "Image": "ImageUrl",
            "PortMappings": [
              {
                "ContainerPort": "ContainerPort"
              }
            ],
            "Name": "ServiceName",
            "Cpu": "ContainerCpu",
            "Memory": "ContainerMemory"
          }
        ],
        "Family": "ServiceName",
        "Cpu": "ContainerCpu",
        "Memory": "ContainerMemory",
        "NetworkMode": "awsvpc",
        "RequiresCompatibilities": [
          "FARGATE"
        ],
        "ExecutionRoleArn": {
          "Fn::ImportValue": [
            ":",
            [
              "StackName",
              "ECSTaskExecutionRole"
            ]
          ]
        }
      }
    },
    "NoTaskDefinition": {
      "Type": "AWS::ECS::Service",
      "DependsOn": [
        "Listener"
      ],
      "Properties": {
        "Role": {
          "Ref": "ECSServiceRole"
        },
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
        }
      }
    }
  }
}
```

```yaml
Resources:
  NoTaskDefinition:
    Type: AWS::ECS::Service
    DependsOn:
    - Listener
    Properties:
      Role:
        Ref: ECSServiceRole
      DesiredCount: 1
      LoadBalancers:
      - TargetGroupArn:
          Ref: TargetGroup
        ContainerPort: 80
        ContainerName: sample-app
      Cluster:
        Ref: ECSCluster
  InvalidTaskDefinition:
    Type: AWS::ECS::Service
    DependsOn:
    - Listener
    Properties:
      Role:
        Ref: ECSServiceRole
      TaskDefinition:
        Ref: MissingTaskDefinition
      DesiredCount: 1
      LoadBalancers:
      - TargetGroupArn:
          Ref: TargetGroup
        ContainerPort: 80
        ContainerName: sample-app
      Cluster:
        Ref: ECSCluster
  TaskNoRole:
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
  ECSTaskDefinition:
    Type: AWS::ECS::TaskDefinition
    Properties:
      Family: !Ref 'ServiceName'
      Cpu: !Ref 'ContainerCpu'
      Memory: !Ref 'ContainerMemory'
      NetworkMode: awsvpc
      RequiresCompatibilities:
        - FARGATE
      ExecutionRoleArn:
        Fn::ImportValue:
          !Join [':', [!Ref 'StackName', 'ECSTaskExecutionRole']]
      ContainerDefinitions:
        - Name: !Ref 'ServiceName'
          Cpu: !Ref 'ContainerCpu'
          Memory: !Ref 'ContainerMemory'
          Image: !Ref 'ImageUrl'
          PortMappings:
            - ContainerPort: !Ref 'ContainerPort'
```
