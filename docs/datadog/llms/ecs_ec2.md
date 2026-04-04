# Source: https://docs.datadoghq.com/security/workload_protection/setup/agent/ecs_ec2.md

# Source: https://docs.datadoghq.com/security/cloud_security_management/setup/agent/ecs_ec2.md

---
title: Setting up Cloud Security on ECS EC2
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud Security > Setting up Cloud Security >
  Deploying Cloud Security on the Agent > Setting up Cloud Security on ECS EC2
---

# Setting up Cloud Security on ECS EC2

Use the following instructions to enable Misconfigurations and Vulnerability Management.

{% alert level="info" %}
Collecting events using Cloud Security Management will affect your billing. For more information, see [Datadog Pricing](https://www.datadoghq.com/pricing/?product=cloud-security-management#products).
{% /alert %}

## Prerequisites{% #prerequisites %}

- Datadog Agent version `7.46` or later.

## Installation{% #installation %}

Add the following environment variables to your `datadog-agent` container definition:

```json
{
  "containerDefinitions": [
    {
      "name": "datadog-agent",
      ...
      "mountPoints": [
        {
          "sourceVolume": "docker_sock",
          "containerPath": "/var/run/docker.sock",
          "readOnly": true
        },
        {
          "sourceVolume": "proc",
          "containerPath": "/host/proc/",
          "readOnly": true
        },
        {
          "sourceVolume": "cgroup",
          "containerPath": "/host/sys/fs/cgroup",
          "readOnly": true
        },
        {
          "sourceVolume": "passwd",
          "containerPath": "/etc/passwd",
          "readOnly": true
        },
        {
          "sourceVolume": "os_release",
          "containerPath": "/host/etc/os-release",
          "readOnly": true
        },
        {
          "sourceVolume": "kernel_debug",
          "containerPath": "/sys/kernel/debug"
        },
        {
          "sourceVolume": "root",
          "containerPath": "/host/root",
          "readOnly": true
        }
      ],
      ...
      "environment": [
        ...
        {
          "name": "DD_COMPLIANCE_CONFIG_ENABLED",
          "value": "true"
        },
        {
          "name": "DD_COMPLIANCE_CONFIG_HOST_BENCHMARKS_ENABLED",
          "value": "true"
        },
        {
          "name": "DD_SYSTEM_PROBE_ENABLED",
          "value": "true"
        },
        {
          "name": "DD_SBOM_ENABLED",
          "value": "true"
        },
        {
          "name": "DD_SBOM_CONTAINER_IMAGE_ENABLED",
          "value": "true"
        },
        {
          "name": "DD_CONTAINER_IMAGE_ENABLED",
          "value": "true"
        },
        {
          "name": "DD_SBOM_HOST_ENABLED",
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
    }
  ],
  ...
  "volumes": [
    {
      "name": "docker_sock",
      "host": {
        "sourcePath": "/var/run/docker.sock"
      }
    },
    {
      "name": "proc",
      "host": {
        "sourcePath": "/proc/"
      }
    },
    {
      "name": "cgroup",
      "host": {
        "sourcePath": "/sys/fs/cgroup/"
      }
    },
    {
      "name": "passwd",
      "host": {
        "sourcePath": "/etc/passwd"
      }
    },
    {
      "name": "os_release",
      "host": {
        "sourcePath": "/etc/os-release"
      }
    },
    {
      "name": "kernel_debug",
      "host": {
        "sourcePath": "/sys/kernel/debug"
      }
    },
    {
      "name": "root",
      "host": {
        "sourcePath": "/"
      }
    }
  ],
  "requiresCompatibilities": [
    "EC2"
  ]
}
```

If the Agent fails to extract the SBOM from the container image, increase the Agent memory in the container definition:

```yaml
{
    "containerDefinitions": [
        {
            "name": "datadog-agent",
            "memory": 256,
            ...
        }
     ]
    ...
}
```
