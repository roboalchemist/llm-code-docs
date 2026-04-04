# Source: https://docs.datadoghq.com/security/guide/aws_fargate_config_guide.md

---
title: AWS Fargate Configuration Guide for Datadog Security
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Security Guides > AWS Fargate Configuration Guide
  for Datadog Security
---

# AWS Fargate Configuration Guide for Datadog Security

This guide walks you through configuring [Cloud Security](https://docs.datadoghq.com/security/cloud_security_management/), [Software Composition Analysis (SCA)](https://docs.datadoghq.com/security/code_security/software_composition_analysis/), [Threat Detection and Protection (AAP)](https://docs.datadoghq.com/security/application_security/), and [Cloud SIEM](https://docs.datadoghq.com/security/cloud_siem/) on AWS Fargate.

{% image
   source="https://datadog-docs.imgix.net/images/security/datadog_security_coverage_aws_fargate2.cd4faa3fdea0c7b5ff11d18e3494eec0.png?auto=format"
   alt="Flow chart showing how Cloud Security, AAP, and Cloud SIEM are configured on AWS Fargate" /%}

## Full stack coverage for AWS Fargate{% #full-stack-coverage-for-aws-fargate %}

Datadog Security provides multiple layers of visibility for AWS Fargate. Use the products in combination with one another to gain full stack coverage, as shown in the following tables:

### Fargate assets{% #fargate-assets %}

| Asset                  | Observability                      | Vulnerabilities and Misconfiguration Remediation      | Threat Detection and Response         |
| ---------------------- | ---------------------------------- | ----------------------------------------------------- | ------------------------------------- |
| Fargate Application    | Application Performance Monitoring | Software Composition Analysis (SCA) and Code Security | AAP - Threat Detection and Protection |
| Fargate Infrastructure | Infrastructure Monitoring          | Cloud Security                                        | Workload Protection                   |

### Fargate-related resources{% #fargate-related-resources %}

| Asset                      | Observability  | Vulnerabilities and Misconfiguration Remediation | Threat Detection and Response |
| -------------------------- | -------------- | ------------------------------------------------ | ----------------------------- |
| AWS IAM roles and policies | Log Management | Cloud Security                                   | Cloud SIEM                    |
| AWS databases              | Log Management | Cloud Security                                   | Cloud SIEM                    |
| AWS S3 buckets             | Log Management | Cloud Security                                   | Cloud SIEM                    |

## Cloud Security{% #cloud-security %}

### Prerequisites{% #prerequisites %}

- The Datadog AWS integration is installed and configured for your AWS accounts
- Access to AWS Management Console
- AWS Fargate ECS or EKS workloads

{% alert level="info" %}
For additional performance and reliability insights, Datadog recommends enabling Infrastructure Monitoring with Cloud Security.
{% /alert %}

### Images{% #images %}

- `cws-instrumentation-init`: `public.ecr.aws/datadog/cws-instrumentation:latest`
- `datadog-agent`: `public.ecr.aws/datadog/agent:latest`

### Installation{% #installation %}

{% tab title="Amazon ECS" %}
#### AWS Console{% #aws-console %}

1. Sign in to [AWS Management Console](https://docs.datadoghq.com/integrations/eks_fargate/?tab=manual#amazon-eks-fargate-rbac).
1. Navigate to the ECS section.
1. On the left menu, select **Task Definitions**, and then select **Create new Task Definition with JSON**. Alternatively, choose an existing Fargate task definition.
1. To create a new task definition, use the JSON definition, or the AWS CLI method.
1. Click **Create** to create the task definition.

#### AWS CLI{% #aws-cli %}

1. Download [datadog-agent-cws-ecs-fargate.json](https://docs.datadoghq.com/resources/json/datadog-agent-cws-ecs-fargate.json).

In the `datadog-agent-cws-ecs-fargate.json` file:

```json
{
    "family": "<YOUR_TASK_NAME>",
    "cpu": "256",
    "memory": "512",
    "networkMode": "awsvpc",
    "pidMode": "task",
    "requiresCompatibilities": [
        "FARGATE"
    ],
    "containerDefinitions": [
        {
            "name": "cws-instrumentation-init",
            "image": "public.ecr.aws/datadog/cws-instrumentation:latest",
            "essential": false,
            "user": "0",
            "command": [
                "/cws-instrumentation",
                "setup",
                "--cws-volume-mount",
                "/cws-instrumentation-volume"
            ],
            "mountPoints": [
                {
                    "sourceVolume": "cws-instrumentation-volume",
                    "containerPath": "/cws-instrumentation-volume",
                    "readOnly": false
                }
            ]
        },
        {
            "name": "datadog-agent",
            "image": "public.ecr.aws/datadog/agent:latest",
            "essential": true,
            "environment": [
                {
                    "name": "DD_API_KEY",
                    "value": "<DD_API_KEY>"
                },
                {
                    "name": "DD_SITE",
                    "value": "datadoghq.com"
                },
                {
                    "name": "ECS_FARGATE",
                    "value": "true"
                },
                {
                    "name": "DD_RUNTIME_SECURITY_CONFIG_ENABLED",
                    "value": "true"
                },
                {
                    "name": "DD_RUNTIME_SECURITY_CONFIG_EBPFLESS_ENABLED",
                    "value": "true"
                }
            ],
            "healthCheck": {
                "command": [
                    "CMD-SHELL",
                    "/probe.sh"
                ],
                "interval": 30,
                "timeout": 5,
                "retries": 2,
                "startPeriod": 60
            }
        },
        {
            "name": "<YOUR_APP_NAME>",
            "image": "<YOUR_APP_IMAGE>",
            "entryPoint": [
                "/cws-instrumentation-volume/cws-instrumentation",
                "trace",
                "--",
                "<ENTRYPOINT>"
            ],
            "mountPoints": [
                {
                    "sourceVolume": "cws-instrumentation-volume",
                    "containerPath": "/cws-instrumentation-volume",
                    "readOnly": true
                }
            ],
            "linuxParameters": {
                "capabilities": {
                    "add": [
                        "SYS_PTRACE"
                    ]
                }
            },
            "dependsOn": [
                {
                    "containerName": "datadog-agent",
                    "condition": "HEALTHY"
                },
                {
                    "containerName": "cws-instrumentation-init",
                    "condition": "SUCCESS"
                }
            ]
        }
    ],
    "volumes": [
        {
            "name": "cws-instrumentation-volume"
        }
    ]
}
```

Update the following items in the JSON file:

- `TASK_NAME`
- `DD_API_KEY`
- `DD_SITE`
- `YOUR_APP_NAME`
- `YOUR_APP_IMAGE`
- `ENTRYPOINT`

You can use the following command to find the entry point of your workload:

```shell
docker inspect <YOUR_APP_IMAGE> -f '{{json .Config.Entrypoint}}'
```

or

```shell
docker inspect <YOUR_APP_IMAGE> -f '{{json .Config.Cmd}}'
```

**Note**: The environment variable `ECS_FARGATE` is already set to "true".

Add your other application containers to the task definition. For details on collecting integration metrics, see [Integration Setup for ECS Fargate](https://docs.datadoghq.com/integrations/faq/integration-setup-ecs-fargate/?tab=rediswebui).

Run the following command to register the ECS task definition:

```shell
aws ecs register-task-definition --cli-input-json file://<PATH_TO_FILE>/datadog-agent-ecs-fargate.json
```

#### Datadog Cloud Security{% #datadog-cloud-security %}

1. In Datadog, navigate to [Cloud Security > Setup > Cloud Integrations > AWS](https://app.datadoghq.com/security/configuration/csm/setup?active_steps=cloud-accounts&active_sub_step=aws&vuln_container_enabled=true&vuln_host_enabled=true&vuln_lambda_enabled=true).
1. Enable Vulnerability Management by deploying the [Datadog Agentless scanner](https://docs.datadoghq.com/security/cloud_security_management/setup/agentless_scanning/enable/?tab=existingawsaccount#set-up-aws-cloudformation) on your AWS accounts hosting your Amazon ECR.

{% /tab %}

{% tab title="Amazon EKS" %}
To collect data from your AWS Fargate pods, you must run the Agent as a sidecar of your application pod and set up Role-Based Access Control (RBAC) rules.

{% alert level="info" %}
If the Agent is running as a sidecar, it can only communicate with containers on the same pod. Run an Agent for every pod you wish to monitor.
{% /alert %}

#### Set up RBAC rules{% #set-up-rbac-rules %}

Use the following [Agent RBAC deployment instruction](https://docs.datadoghq.com/integrations/eks_fargate/?tab=manual#amazon-eks-fargate-rbac) before deploying the Agent as a sidecar.

#### Deploy the Agent as a sidecar{% #deploy-the-agent-as-a-sidecar %}

The following manifest represents the minimum configuration required to deploy your application with the Datadog Agent as a sidecar with Workload Protection enabled:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
 name: "<APPLICATION_NAME>"
 namespace: default
spec:
 replicas: 1
 selector:
   matchLabels:
     app: "<APPLICATION_NAME>"
 template:
   metadata:
     labels:
       app: "<APPLICATION_NAME>"
     name: "<POD_NAME>"
   spec:
     initContainers:
     - name: cws-instrumentation-init
       image: public.ecr.aws/datadog/cws-instrumentation:latest
       command:
         - "/cws-instrumentation"
         - "setup"
         - "--cws-volume-mount"
         - "/cws-instrumentation-volume"
       volumeMounts:
         - name: cws-instrumentation-volume
           mountPath: "/cws-instrumentation-volume"
       securityContext:
         runAsUser: 0
     containers:
     - name: "<YOUR_APP_NAME>"
       image: "<YOUR_APP_IMAGE>"
       command:
         - "/cws-instrumentation-volume/cws-instrumentation"
         - "trace"
         - "--"
         - "<ENTRYPOINT>"
       volumeMounts:
         - name: cws-instrumentation-volume
           mountPath: "/cws-instrumentation-volume"
           readOnly: true
     - name: datadog-agent
       image: public.ecr.aws/datadog/agent:latest
       env:
         - name: DD_API_KEY
           value: "<DD_API_KEY>"
         - name: DD_RUNTIME_SECURITY_CONFIG_ENABLED
           value: "true"
         - name: DD_RUNTIME_SECURITY_CONFIG_EBPFLESS_ENABLED
           value: "true"
         - name: DD_EKS_FARGATE
           value: "true"
         - name: DD_CLUSTER_NAME
           value: "<CLUSTER_NAME>"
         - name: DD_KUBERNETES_KUBELET_NODENAME
           valueFrom:
             fieldRef:
               apiVersion: v1
               fieldPath: spec.nodeName
     volumes:
       - name: cws-instrumentation-volume
     serviceAccountName: datadog-agent
     shareProcessNamespace: true
```

{% /tab %}

### Verify that the Agent is sending events to Cloud Security{% #verify-that-the-agent-is-sending-events-to-cloud-security %}

When you enable Cloud Security on AWS Fargate ECS or EKS, the Agent sends an agent event to Datadog to confirm that the default ruleset has been successfully deployed. To view the agent event, navigate to the [Agent Events](https://app.datadoghq.com/security/agent-events) page in Datadog and search for `@agent.rule_id:ruleset_loaded`.

{% alert level="info" %}
You can also verify the Agent is sending events to Cloud Security by manually triggering an AWS Fargate security signal.
{% /alert %}

In the task definition, replace the "workload" container with the following:

```yaml
            "name": "cws-signal-test",
            "image": "ubuntu:latest",
            "entryPoint": [
                "/cws-instrumentation-volume/cws-instrumentation",
                "trace",
                "--verbose",
                "--",
                "/usr/bin/bash",
                "-c",
                "apt update;apt install -y curl; while true; do curl https://google.com; sleep 5; done"
            ],
```

## App and API Protection{% #app-and-api-protection %}

### Prerequisites{% #prerequisites-1 %}

- The Datadog Agent is installed and configured for your application's operating system or container, cloud, or virtual environment
- Datadog APM is configured for your application or service

{% alert level="info" %}
For additional performance and reliability insights, Datadog recommends enabling Application Performance Monitoring with App and API Protection.
{% /alert %}

### Installation{% #installation-1 %}

#### Software Composition Analysis (SCA){% #software-composition-analysis-sca %}

[Software Composition Analysis (SCA)](https://docs.datadoghq.com/security/code_security/software_composition_analysis/) works in Fargate. Follow the [installation steps for applications that run in traditional hosts](https://docs.datadoghq.com/security/code_security/software_composition_analysis/).

#### Threat Detection and Protection{% #threat-detection-and-protection %}

For step-by-step instructions, see the following articles:

- [Java](https://docs.datadoghq.com/security/application_security/setup/java/aws-fargate)
- [.NET](https://docs.datadoghq.com/security/application_security/setup/dotnet/aws-fargate)
- [Go](https://docs.datadoghq.com/security/application_security/setup/aws/fargate)
- [Ruby](https://docs.datadoghq.com/security/application_security/setup/ruby/aws-fargate)
- [Node.js](https://docs.datadoghq.com/security/application_security/setup/nodejs/aws-fargate)
- [Python](https://docs.datadoghq.com/security/application_security/setup/python/aws-fargate)

#### Code Security{% #code-security %}

For step-by-step instructions, see the following articles:

- [Java](https://docs.datadoghq.com/security/code_security/iast/setup/java/)
- [.NET](https://docs.datadoghq.com/security/code_security/iast/setup/dotnet/)
- [Node.js](https://docs.datadoghq.com/security/code_security/iast/setup/nodejs/)

## Cloud SIEM{% #cloud-siem %}

### Prerequisites{% #prerequisites-2 %}

- [Log ingestion](https://app.datadoghq.com/security/configuration/siem/setup) is configured to collect logs from your sources.

### Installation{% #installation-2 %}

For step-by-step instructions, see [AWS Configuration Guide for Cloud SIEM](https://docs.datadoghq.com/security/cloud_siem/guide/aws-config-guide-for-cloud-siem/).

#### Enable AWS CloudTrail logging{% #enable-aws-cloudtrail-logging %}

Enable AWS CloudTrail logging so that logs are sent to a S3 bucket. If you already have this setup, skip to Send AWS CloudTrail logs to Datadog.

1. Click **Create trail** on the [CloudTrail dashboard](https://console.aws.amazon.com/cloudtrail/home).
1. Enter a name for your trail.
1. Create a new S3 bucket or use an existing S3 bucket to store the CloudTrail logs.
1. Create a new AWS KMS key or use an existing AWS KMS key, then click **Next**.
1. Leave the event type with the default management read and write events, or choose additional event types you want to send to Datadog, then click **Next**.
1. Review and click **Create trail**.

#### Send AWS CloudTrail logs to Datadog{% #send-aws-cloudtrail-logs-to-datadog %}

Set up a trigger on your Datadog Forwarder Lambda function to send CloudTrail logs stored in the S3 bucket to Datadog for monitoring.

1. Go to the [Datadog Forwarder Lambda](https://console.aws.amazon.com/lambda/home) that was created during the AWS integration set up.
1. Click **Add trigger**.
1. Select **S3** for the trigger.
1. Select the S3 bucket you are using to collect AWS CloudTrail logs.
1. For Event type, select **All object create events**.
1. Click **Add**.
1. See CloudTrail logs in Datadog's [Log Explorer](https://app.datadoghq.com/logs?query=service%3Acloudtrail).

See [Log Explorer](https://docs.datadoghq.com/logs/explorer/) for more information on how to search and filter, group, and visualize your logs.

## Further Reading{% #further-reading %}

- [Get real-time threat detection for AWS Fargate ECS and EKS environments with Datadog Cloud Security](https://www.datadoghq.com/blog/threat-detection-fargate/)
