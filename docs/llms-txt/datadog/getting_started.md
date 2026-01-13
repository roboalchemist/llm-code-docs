# Source: https://docs.datadoghq.com/administrators_guide/getting_started.md

# Source: https://docs.datadoghq.com/getting_started.md

---
title: Getting Started
description: >-
  Introduction to Datadog's observability platform with guides for installation,
  configuration, and getting started with key features.
breadcrumbs: Docs > Getting Started
source_url: https://docs.datadoghq.com/index.html
---

# Getting Started

## What is Datadog?{% #what-is-datadog %}

Datadog is an observability platform that supports every phase of software development on any stack. The platform consists of many products that help you build, test, monitor, debug, optimize, and secure your software. These products can be used individually or combined into a customized solution.

The table below lists a few examples of Datadog products:

| Category            | Product examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Development**     | - Highlight code vulnerabilities in your text editor or on GitHub with [Code Security](https://docs.datadoghq.com/security/code_security/).
  - Facilitate a remote pair-programming session with [CoScreen](https://docs.datadoghq.com/coscreen/).                                                                                                                                                                                                                                                                                                  |
| **Testing**         | - Block faulty code from deploying to production with [PR Gates](https://docs.datadoghq.com/pr_gates/).
  - Simulate users around the globe to test your web app, API, or mobile application with [Synthetic Monitoring](https://docs.datadoghq.com/synthetics/).                                                                                                                                                                                                                                                                                    |
| **Monitoring**      | - Ingest [logs](https://docs.datadoghq.com/logs/), [metrics](https://docs.datadoghq.com/metrics/), [events](https://docs.datadoghq.com/events/), and [network traces](https://docs.datadoghq.com/tracing/glossary/#trace) with granular control over processing, aggregation, and [alerting.](https://docs.datadoghq.com/monitors/)
  - Assess host performance with [Continuous Profiler](https://docs.datadoghq.com/profiler/).
  - Assess application performance with [Application Performance Monitoring](https://docs.datadoghq.com/tracing/). |
| **Troubleshooting** | - Manage [errors](https://docs.datadoghq.com/error_tracking/) and [incidents](https://docs.datadoghq.com/incident_response/incident_management/), summarizing issues and suggesting fixes.
  - Measure user churn and detect user frustration with [Real User Monitoring](https://docs.datadoghq.com/real_user_monitoring/).                                                                                                                                                                                                                         |
| **Security**        | - Detect threats and attacks with [Datadog Security](https://docs.datadoghq.com/security/).                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

Additionally, hundreds of [integrations](https://docs.datadoghq.com/getting_started/integrations/) allow you to layer Datadog features over the technologies you already use. For example, the [AWS integration](https://docs.datadoghq.com/integrations/amazon_web_services/) collects logs, events, and metrics from more than 90 AWS services.

## Learn more{% #learn-more %}

{% callout %}
##### Join an enablement webinar session

This foundation enablement session helps answer the key question: "What is Datadog, and what can it do for me?" You will learn how to send data to Datadog and which pages to visit to better understand the state of your various environments, applications, and infrastructure.

[SIGN UP](https://www.datadoghq.com/technical-enablement/session/datadog-overview/)
{% /callout %}

### Take a course{% #take-a-course %}

The Datadog Learning Center offers hands-on experience with the Datadog platform. The [Getting Started courses](https://learn.datadoghq.com/collections/getting-started) cover observability practices, key Datadog concepts, and more.

For the fastest introduction to navigating Datadog, try the [Quick Start course](https://learn.datadoghq.com/courses/course-quickstart).

### Dive deeper into a product area{% #dive-deeper-into-a-product-area %}

- [Datadog: Discover how to use the Datadog UI: Dashboards, infrastructure list, maps, and more.](https://docs.datadoghq.com/getting_started/application)
- [Datadog Site: Select the appropriate Datadog site for your region and security requirements.](https://docs.datadoghq.com/getting_started/site)
- [DevSecOps Bundles: Get started with the Infrastructure DevSecOps bundles.](https://docs.datadoghq.com/getting_started/devsecops)
- [Agent: Send metrics and events from your hosts to Datadog.](https://docs.datadoghq.com/getting_started/agent)
- [API: Get started with the Datadog HTTP API.](https://docs.datadoghq.com/getting_started/api)
- [Integrations: Learn how to collect metrics, traces, and logs with Datadog integrations.](https://docs.datadoghq.com/getting_started/integrations)
- [Search: Learn the fundamentals of searching and filtering across Datadog products.](https://docs.datadoghq.com/getting_started/search)
- [Tags: Start tagging your metrics, logs, and traces.](https://docs.datadoghq.com/getting_started/tagging)
- [OpenTelemetry: Learn how to send OpenTelemetry metrics, traces, and logs to Datadog.](https://docs.datadoghq.com/getting_started/opentelemetry)
- [Learning Center: Follow a learning path, take a self-guided class or lab, and explore the Datadog certification program.](https://docs.datadoghq.com/getting_started/learning_center)

- [Dashboards: Create, share, and maintain dashboards that answer the work questions that matter to you.](https://docs.datadoghq.com/getting_started/dashboards)
- [Incident Management: Communicate and track problems in your systems.](https://docs.datadoghq.com/getting_started/incident_management)
- [Monitors: Set up alerts and notifications so that your team knows when critical changes occur.](https://docs.datadoghq.com/getting_started/monitors)
- [Notebooks: Combine live graphs, metrics, logs, and monitors to isolate issues and create interactive guides.](https://docs.datadoghq.com/getting_started/notebooks)
- [Workflow Automation: Automate end-to-end processes in response to alerts and security signals.](https://docs.datadoghq.com/getting_started/workflow_automation)

- [Containers: Learn how to use Agent Autodiscovery and the Datadog operator.](https://docs.datadoghq.com/getting_started/containers)
- [Serverless for AWS Lambda: Learn how to collect metrics, logs, and traces from your serverless infrastructure.](https://docs.datadoghq.com/getting_started/serverless)
- [Internal Developer Portal: Unify telemetry, metadata, and workflows to accelerate delivery.](https://docs.datadoghq.com/getting_started/internal_developer_portal)
- [Tracing: Set up the Agent to trace a small application.](https://docs.datadoghq.com/getting_started/tracing)
- [Profiler: Use Continuous Profiler to find and fix performance problems in your code.](https://docs.datadoghq.com/getting_started/profiler)
- [Database Monitoring: View the health and performance of databases, and quickly troubleshoot any issues that arise.](https://docs.datadoghq.com/getting_started/database_monitoring)
- [Synthetic Monitoring: Start testing and monitoring your API endpoints and key business journeys with Synthetic tests.](https://docs.datadoghq.com/getting_started/synthetics)
- [Continuous Testing: Run end-to-end Synthetic tests in your CI pipelines and IDEs.](https://docs.datadoghq.com/getting_started/continuous_testing)
- [Session Replay: Get an in-depth look at how users are interacting with your product with Session Replays.](https://docs.datadoghq.com/getting_started/session_replay)
- [App and API Protection: Discover best practices for getting your team up and running with AAP.](https://docs.datadoghq.com/getting_started/application_security)
- [Cloud Security: Discover best practices for getting your team up and running with Cloud Security.](https://docs.datadoghq.com/getting_started/cloud_security_management)
- [Cloud SIEM: Discover best practices for getting your team up and running with Cloud SIEM.](https://docs.datadoghq.com/getting_started/cloud_siem)
- [Logs: Send your first logs and use log processing to enrich them.](https://docs.datadoghq.com/getting_started/logs)
- [CI Visibility: Collect CI pipeline data by setting up integrations with your CI providers.](https://docs.datadoghq.com/getting_started/ci_visibility)
- [Feature Flags: Manage feature delivery and personalize user experiences, with built-in observability.](https://docs.datadoghq.com/getting_started/feature_flags)
- [Test Optimization: Collect CI test data by setting up test services in Datadog.](https://docs.datadoghq.com/getting_started/test_optimization)
- [Test Impact Analysis: Optimize your test suite and reduce CI costs by only running tests that are relevant to your code changes.](https://docs.datadoghq.com/getting_started/test_impact_analysis)
- [Code Security: Analyze your first-party code and open source libraries in your applications from development to runtime.](https://docs.datadoghq.com/getting_started/code_security)

## Try a Preview product or feature{% #try-a-preview-product-or-feature %}

Datadog Product teams are frequently adding new features that might help you. You can try some of these out before they are generally available to see if they help you and to give us feedback to make them better. To see a complete list of active previews, get more information, and sign up to participate, go to [Datadog Product Preview Program](https://www.datadoghq.com/product-preview/).

## Further Reading{% #further-reading %}

- [Take a course to get started with Datadog](https://learn.datadoghq.com/)
- [Learn about new Datadog products and features, integrations, and more](https://datadoghq.com/blog/)
- [Explore the Quick Start Guide](https://app.datadoghq.com/help/quick_start)
