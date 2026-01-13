# Source: https://docs.datadoghq.com/tracing/trace_collection.md

---
title: Application Instrumentation
description: Get Started with Datadog APM
breadcrumbs: Docs > APM > Application Instrumentation
source_url: https://docs.datadoghq.com/trace_collection/index.html
---

# Application Instrumentation

## Overview{% #overview %}

To get started with Datadog APM, you need to follow these key steps:

1. Install and configure the Datadog Agent.
1. Instrument your application.

{% alert level="info" %}
**Simplify your setup!** Install the Agent and instrument your application in one step with [Single Step Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/single-step-apm/).
{% /alert %}

Instrumenting your application allows observability data to be sent to the Agent, which then passes data to the Datadog backend to display in the UI.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/visualization/troubleshooting_pipeline.68ceea859e08a050cfd9a3ff155a5bd7.png?auto=format"
   alt="The APM pipeline" /%}

## Instrumentation types{% #instrumentation-types %}

There are two main approaches to instrument your application:

**Automatic instrumentation** creates span (A span is a logical unit of work in a distributed system for a given period.)s for your application with minimal manual steps, capturing essential observability data across common libraries and languages with minimal configuration.

**Custom instrumentation** captures observability data from in-house code or complex functions that aren't captured by automatic instrumentation, providing deeper visibility and context into spans when you need fine-grained control.

The following table compares the different instrumentation methods available.

{% alert level="info" %}
If you prefer vendor-neutral instrumentation, see the [OpenTelemetry documentation](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/otel_instrumentation/) for using OpenTelemetry API support in Datadog libraries.
{% /alert %}

| Automatic Instrumentation                                                                                                     | Custom Instrumentation                                                                                                                                                                                                                                                                                                |
| ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Single Step Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/) | [Manually managed SDKs](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/dd_libraries/)                                                                                                                                                                                                  | [Code-based Custom Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/)                                                                                                                                                                                                      | [Dynamic Instrumentation](https://docs.datadoghq.com/tracing/dynamic_instrumentation/)(UI-based Custom Instrumentation) |
| Description                                                                                                                   | With a single command, Datadog automatically loads language SDKs to your application processes. You can also control which processes to instrument.                                                                                                                                                                   | Add Datadog language SDKs to your applications. The SDK handles instrumentation automatically.                                                                                                                                                                                                                        | Add explicit tracing API calls or span logic in your application code.                                                  | Add instrumentation rules in the Datadog UI. Rules are applied dynamically at runtime and do not require code changes.                                                            |
| Code changes?                                                                                                                 | No                                                                                                                                                                                                                                                                                                                    | No                                                                                                                                                                                                                                                                                                                    | Yes                                                                                                                     | No                                                                                                                                                                                |
| Environment config changes?                                                                                                   | No                                                                                                                                                                                                                                                                                                                    | Yes                                                                                                                                                                                                                                                                                                                   | Yes                                                                                                                     | No                                                                                                                                                                                |
| Setup complexity                                                                                                              | Low                                                                                                                                                                                                                                                                                                                   | Medium                                                                                                                                                                                                                                                                                                                | High                                                                                                                    | Low                                                                                                                                                                               |
| Best for                                                                                                                      | SRE, admins, or central teams who want tracing across services without developer involvement.                                                                                                                                                                                                                         | App dev teams who want to instrument applications individually with granular control over configuration through environment variables.                                                                                                                                                                                | Teams needing custom logic, specialized spans, or visibility into custom code paths.                                    | Teams wanting to add spans, logs, or metrics to specific code locations at runtime without redeploying or modifying source code. Configuration is managed through the Datadog UI. |
| Use cases                                                                                                                     | Capturing essential observability data across common libraries and languages with minimal configuration.Enabling real-time monitoring with pre-configured settings for immediate insights into application performance.Simplifying the observability setup for projects where custom instrumentation is not required. | Collecting observability data from custom code with unique or complex business logic.Providing deeper visibility and context into spans, including adding span tags.Precisely monitoring specific sequences of operations or user interactions that require fine-grained control.Removing unwanted spans from traces. |

## APM setup tutorials{% #apm-setup-tutorials %}

The following tutorials guide you through setting up distributed tracing for a sample application on various infrastructure scenarios, with both automatic and custom instrumentation, using the Datadog tracing libraries:

- [Enabling Tracing on a Python Application on the Same Host as Datadog Agent](https://docs.datadoghq.com/tracing/guide/tutorial-enable-python-host)
- [Enabling Tracing on a Python Application and Datadog Agent in Containers](https://docs.datadoghq.com/tracing/guide/tutorial-enable-python-containers)
- [Enabling Tracing for a Python Application in a Container and an Agent on a Host](https://docs.datadoghq.com/tracing/guide/tutorial-enable-python-container-agent-host)
- [Enabling Tracing on a Java Application on the Same Host as Datadog Agent](https://docs.datadoghq.com/tracing/guide/tutorial-enable-java-host)
- [Enabling Tracing on a Java Application and Datadog Agent in Containers](https://docs.datadoghq.com/tracing/guide/tutorial-enable-java-containers)
- [Enabling Tracing for a Java Application in a Container and an Agent on a Host](https://docs.datadoghq.com/tracing/guide/tutorial-enable-java-container-agent-host)
- [Enabling Tracing for a Java Application on GKE](https://docs.datadoghq.com/tracing/guide/tutorial-enable-java-gke)
- [Enabling Tracing for a Java Application on AWS EKS](https://docs.datadoghq.com/tracing/guide/tutorial-enable-java-aws-eks)
- [Enabling Tracing for a Java Application in Amazon ECS with EC2](https://docs.datadoghq.com/tracing/guide/tutorial-enable-java-aws-ecs-ec2)
- [Enabling Tracing for a Java Application in Amazon ECS with Fargate](https://docs.datadoghq.com/tracing/guide/tutorial-enable-java-aws-ecs-fargate)
- [Enabling Tracing for a Java Application with the Admission Controller](https://docs.datadoghq.com/tracing/guide/tutorial-enable-java-admission-controller)
- [Enabling Tracing on a Go Application on the Same Host as Datadog Agent](https://docs.datadoghq.com/tracing/guide/tutorial-enable-go-host)
- [Enabling Tracing on a Go Application and Datadog Agent in Containers](https://docs.datadoghq.com/tracing/guide/tutorial-enable-go-containers)
- [Enabling Tracing for a Go Application in Amazon ECS with EC2](https://docs.datadoghq.com/tracing/guide/tutorial-enable-go-aws-ecs-ec2)
- [Enabling Tracing for a Go Application in Amazon ECS with Fargate](https://docs.datadoghq.com/tracing/guide/tutorial-enable-go-aws-ecs-fargate)

## Further reading{% #further-reading %}

- [Compatibility requirements](https://docs.datadoghq.com/tracing/trace_collection/compatibility)
- [APM Terms and Concepts](https://docs.datadoghq.com/tracing/glossary/)
- [Instrument your app using the Datadog Operator and Admission Controller](https://www.datadoghq.com/architecture/instrument-your-app-using-the-datadog-operator-and-admission-controller/)
