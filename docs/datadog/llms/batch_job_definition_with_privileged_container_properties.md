# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/batch_job_definition_with_privileged_container_properties.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/batch_job_definition_with_privileged_container_properties.md

---
title: Batch job definition with privileged container properties
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Batch job definition with privileged container
  properties
---

# Batch job definition with privileged container properties

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `76ddf32c-85b1-4808-8935-7eef8030ab36`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html)

### Description{% #description %}

Running Batch job containers in privileged mode grants them elevated access to the host kernel and device nodes, which can enable container escape, host compromise, and lateral movement across your environment. The `Privileged` property under `Properties.ContainerProperties` in `AWS::Batch::JobDefinition` must be set to `false`. Resources with `Privileged` set to `true` will be flagged. If a job legitimately requires extra capabilities, avoid privileged mode and instead grant only the specific capabilities needed or run the workload on dedicated, hardened hosts.

Secure configuration example:

```yaml
MyJobDefinition:
  Type: AWS::Batch::JobDefinition
  Properties:
    ContainerProperties:
      Image: my-image
      Vcpus: 1
      Memory: 1024
      Privileged: false
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "BatchJobDefinition"
Resources:
  JobDefinition:
    Type: AWS::Batch::JobDefinition
    Properties:
      Type: container
      JobDefinitionName: nvidia-smi
      ContainerProperties:
        MountPoints:
          - ReadOnly: false
            SourceVolume: nvidia
            ContainerPath: /usr/local/nvidia
        Volumes:
          - Host:
              SourcePath: /var/lib/nvidia-docker/volumes/nvidia_driver/latest
            Name: nvidia
        Command:
          - nvidia-smi
        Memory: 2000
        Privileged: false
        JobRoleArn: String
        ReadonlyRootFilesystem: true
        Vcpus: 2
        Image: nvidia/cuda
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "BatchJobDefinition",
  "Resources": {
    "JobDefinition1": {
      "Type": "AWS::Batch::JobDefinition",
      "Properties": {
        "Type": "container",
        "JobDefinitionName": "nvidia-smi",
        "ContainerProperties": {
          "Memory": 2000,
          "JobRoleArn": "String",
          "ReadonlyRootFilesystem": true,
          "Vcpus": 2,
          "Image": "nvidia/cuda",
          "MountPoints": [
            {
              "SourceVolume": "nvidia",
              "ContainerPath": "/usr/local/nvidia",
              "ReadOnly": false
            }
          ],
          "Volumes": [
            {
              "Host": {
                "SourcePath": "/var/lib/nvidia-docker/volumes/nvidia_driver/latest"
              },
              "Name": "nvidia"
            }
          ],
          "Command": [
            "nvidia-smi"
          ]
        }
      }
    }
  }
}
```

```yaml


AWSTemplateFormatVersion: "2010-09-09"
Description: "BatchJobDefinition"
Resources:
  JobDefinition1:
    Type: AWS::Batch::JobDefinition
    Properties:
      Type: container
      JobDefinitionName: nvidia-smi
      ContainerProperties:
        MountPoints:
          - ReadOnly: false
            SourceVolume: nvidia
            ContainerPath: /usr/local/nvidia
        Volumes:
          - Host:
              SourcePath: /var/lib/nvidia-docker/volumes/nvidia_driver/latest
            Name: nvidia
        Command:
          - nvidia-smi
        Memory: 2000
        JobRoleArn: String
        ReadonlyRootFilesystem: true
        Vcpus: 2
        Image: nvidia/cuda
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "BatchJobDefinition",
  "Resources": {
    "JobDefinition": {
      "Type": "AWS::Batch::JobDefinition",
      "Properties": {
        "Type": "container",
        "JobDefinitionName": "nvidia-smi",
        "ContainerProperties": {
          "Memory": 2000,
          "Privileged": true,
          "Vcpus": 2,
          "MountPoints": [
            {
              "ReadOnly": false,
              "SourceVolume": "nvidia",
              "ContainerPath": "/usr/local/nvidia"
            }
          ],
          "Command": [
            "nvidia-smi"
          ],
          "ReadonlyRootFilesystem": true,
          "Image": "nvidia/cuda",
          "Volumes": [
            {
              "Host": {
                "SourcePath": "/var/lib/nvidia-docker/volumes/nvidia_driver/latest"
              },
              "Name": "nvidia"
            }
          ],
          "JobRoleArn": "String"
        }
      }
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: "BatchJobDefinition"
Resources:
  JobDefinition:
    Type: AWS::Batch::JobDefinition
    Properties:
      Type: container
      JobDefinitionName: nvidia-smi
      ContainerProperties:
        MountPoints:
          - ReadOnly: false
            SourceVolume: nvidia
            ContainerPath: /usr/local/nvidia
        Volumes:
          - Host:
              SourcePath: /var/lib/nvidia-docker/volumes/nvidia_driver/latest
            Name: nvidia
        Command:
          - nvidia-smi
        Memory: 2000
        Privileged: true
        JobRoleArn: String
        ReadonlyRootFilesystem: true
        Vcpus: 2
        Image: nvidia/cuda
```
