# Source: https://docs.datadoghq.com/security/application_security/setup/python/aws-fargate.md

# Source: https://docs.datadoghq.com/security/application_security/setup/php/aws-fargate.md

# Source: https://docs.datadoghq.com/security/application_security/setup/nodejs/aws-fargate.md

# Source: https://docs.datadoghq.com/security/application_security/setup/java/aws-fargate.md

# Source: https://docs.datadoghq.com/security/application_security/setup/go/aws-fargate.md

# Source: https://docs.datadoghq.com/security/application_security/setup/ruby/aws-fargate.md

# Source: https://docs.datadoghq.com/security/application_security/setup/dotnet/aws-fargate.md

---
title: Set up App and API Protection for .NET on AWS Fargate
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > App and API Protection > Enabling App and API
  Protection > Enabling AAP for .NET > Set up App and API Protection for .NET on
  AWS Fargate
---

# Set up App and API Protection for .NET on AWS Fargate

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

App and API Protection leverages the [Datadog .NET library](https://github.com/DataDog/dd-trace-dotnet/) to monitor and secure your .NET service. The library integrates seamlessly with your existing application without requiring code changes.

For detailed compatibility information, including supported DOTNET versions, frameworks, and deployment environments, see [.NET Compatibility Requirements](https://docs.datadoghq.com/security/application_security/setup/dotnet/compatibility).

This guide explains how to set up App and API Protection (AAP) for .NET applications. The setup involves:

1. Installing the Datadog Agent.
1. Enabling App and API Protection monitoring.
1. Running your .NET application with the Datadog Agent.
1. Verifying the setup.

## Prerequisites{% #prerequisites %}

- AWS Fargate environment
- .NET application containerized with Docker
- AWS CLI configured with appropriate permissions
- Your Datadog API key
- Datadog .NET tracing library (see [version requirements](https://docs.datadoghq.com/security/application_security/setup/dotnet/compatibility))

## 1. Installing the Datadog Agent

Install the Datadog Agent in your Fargate task definition:

```json
{
  "containerDefinitions": [
    {
      "name": "datadog-agent",
      "image": "public.ecr.aws/datadog/agent:latest",
      "environment": [
        {
          "name": "DD_API_KEY",
          "value": "<YOUR_API_KEY>"
        },
        {
          "name": "DD_APM_ENABLED",
          "value": "true"
        },
        {
          "name": "DD_APM_NON_LOCAL_TRAFFIC",
          "value": "true"
        }
      ]
    }
  ]
}
```

## 2. Enabling App and API Protection monitoring
If your Java service already has APM tracing set up and running, you can automatically enable App and API Protection through Remote Configuration.If not, enable App and API Protection with the manual configuration instructions..navigation-menu{background:#f8f9fa;border:1px solid #e9ecef;border-radius:8px;padding:20px;margin:20px 0}.nav-container h3{margin-top:0;margin-bottom:15px;color:#333;font-size:1.1em}.nav-list{list-style:none;padding:0;margin:0}.nav-list li{margin-bottom:8px}.nav-list a{color:#06c;text-decoration:none;font-weight:500}.nav-list a:hover{text-decoration:underline;color:#049}
### Automatically enabling App and API Protection through Remote Configuration{% #automatically-enabling-app-and-api-protection-through-remote-configuration %}

You can enable services with remote configuration on your [services dashboard](https://app.datadoghq.com/security/configuration/asm/setup?services=recommended). Check the box for the service you want to enable App and API Protection for under Activate on your APM services.

### Manually enabling App and API Protection monitoring{% #manually-enabling-app-and-api-protection-monitoring %}

Ensure your Dockerfile includes the Datadog .NET library:

```dockerfile
# Download and install Datadog .NET Tracer
ENV DD_TRACE_VERSION=3.20.0
RUN curl -sSL https://github.com/DataDog/dd-trace-dotnet/releases/download/v${DD_TRACE_VERSION}/datadog-dotnet-apm-${DD_TRACE_VERSION}.linux-x64.tar.gz \
    | tar -xz -C /opt/datadog

# Set environment variables for Datadog automatic instrumentation
ENV CORECLR_ENABLE_PROFILING=1 \
    CORECLR_PROFILER="{846F5F1C-F9AE-4B07-969E-05C26BC060D8}" \
    CORECLR_PROFILER_PATH=/opt/datadog/Datadog.Trace.ClrProfiler.Native.so \
    DD_DOTNET_TRACER_HOME=/opt/datadog \
```

{% collapsible-section %}
#### APM Tracing Enabled

Update your task definition to include the .NET agent and App and API Protection configuration:

```json
{
  "containerDefinitions": [
    {
      "name": "your-dotnet-app",
      "image": "your-dotnet-app-image",
      "environment": [
        {
          "name": "DD_APPSEC_ENABLED",
          "value": "true"
        },
        {
          "name": "DD_SERVICE",
          "value": "<YOUR_SERVICE_NAME>"
        },
        {
          "name": "DD_ENV",
          "value": "<YOUR_ENVIRONMENT>"
        }
      ]
    }
  ]
}
```

{% /collapsible-section %}

{% collapsible-section %}
#### APM Tracing Disabled

To disable APM tracing while keeping App and API Protection enabled, you must set the APM tracing variable to false.

Update your task definition to include the .NET agent and App and API Protection configuration with APM tracing disabled:

```json
{
  "containerDefinitions": [
    {
      "name": "your-dotnet-app",
      "image": "your-dotnet-app-image",
      "environment": [
        {
          "name": "DD_APPSEC_ENABLED",
          "value": "true"
        },
        {
          "name": "DD_APM_TRACING_ENABLED",
          "value": "false"
        },
        {
          "name": "DD_SERVICE",
          "value": "<YOUR_SERVICE_NAME>"
        },
        {
          "name": "DD_ENV",
          "value": "<YOUR_ENVIRONMENT>"
        }
      ]
    }
  ]
}
```

{% /collapsible-section %}

## 3. Run your application

Deploy your Fargate task with the updated configuration:

```bash
aws ecs register-task-definition --cli-input-json file://task-definition.json
aws ecs run-task --cluster your-cluster --task-definition your-task-definition
```

## 4. Verify setup

To verify that App and API Protection is working correctly:

1. Send some traffic to your application
1. Check the [Application Signals Explorer](https://app.datadoghq.com/security/appsec) in Datadog
1. Look for security signals and vulnerabilities

## Troubleshooting{% #troubleshooting %}

If you encounter issues while setting up App and API Protection for your .net application, see the [.NET App and API Protection troubleshooting guide](https://docs.datadoghq.com/security/application_security/setup/dotnet/troubleshooting).

## Further Reading{% #further-reading %}

- [How App and API Protection Works](https://docs.datadoghq.com/security/application_security/how-it-works/)
- [OOTB App and API Protection Rules](https://docs.datadoghq.com/security/default_rules/?category=cat-application-security)
- [Troubleshooting App and API Protection](https://docs.datadoghq.com/security/application_security/troubleshooting)
