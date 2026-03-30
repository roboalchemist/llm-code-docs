# Source: https://www.elastic.co/docs/solutions/observability

﻿---
title: Elastic Observability solution overview
description: The Observability reference documentation is available in the Elastic reference documentation. You can also browse reference documentation for the following...
url: https://www.elastic.co/docs/solutions/observability
products:
  - Elastic Cloud Serverless
  - Elastic Distribution of OpenTelemetry Collector
  - Elastic Observability
  - Kibana
applies_to:
  - Elastic Cloud Serverless: Generally available
  - Elastic Stack: Generally available
---

# Elastic Observability solution overview
Elastic Observability provides unified observability across applications and infrastructure. It combines logs, metrics, application traces, user experience data, and more into a single, integrated platform.
This consolidation allows for powerful, cross-referenced analysis, enabling teams to move from detecting issues to understanding their root causes quickly and efficiently.
By leveraging the search and analytics capabilities of Elasticsearch, it offers a holistic view of system behavior.
Elastic Observability embraces open standards like OpenTelemetry for flexible data collection, and offers scalable, cost-efficient data retention with tiered storage.
<tip>
  New to Elastic? Refer to [Elastic Fundamentals](https://www.elastic.co/docs/get-started) to understand the Elastic Stack, its components, and your deployment options.
</tip>


## Use cases

Apply Observability to various scenarios to improve operational awareness and system reliability.
<dropdown title="Use cases">
  - **[Log monitoring and analytics](https://www.elastic.co/docs/solutions/observability/logs):** Centralize and analyze petabytes of log data from any source. This enables quick searching, ad-hoc queries with ES|QL, and visualization with prebuilt dashboards to diagnose issues.
  - **[Application Performance Monitoring (APM)](https://www.elastic.co/docs/solutions/observability/applications):** Gain code-level visibility into application performance. By collecting and analyzing traces with native OTel support, teams can identify bottlenecks, track errors, and optimize the end-user experience.
  - **[Infrastructure monitoring](https://www.elastic.co/docs/solutions/observability/infra-and-hosts):** Monitor metrics from servers, virtual machines, containers, and serverless environments with over 400 out-of-the-box integrations, including OpenTelemetry. This provides deep insights into resource utilization and overall system health.
  - **[AI-powered log analysis with Streams](https://www.elastic.co/docs/solutions/observability/streams/streams):** Ingest raw logs in any format directly to a single endpoint without the need for complex agent management or manual parsing pipelines. Streams leverages AI to automatically parse, structure, and analyze log data on the fly.
  - **Digital experience monitoring:**
    - **[Real User Monitoring (RUM)](https://www.elastic.co/docs/solutions/observability/applications/user-experience):** Capture and analyze data on how real users interact with web applications to improve perceived performance.
  - **[Synthetic monitoring](https://www.elastic.co/docs/solutions/observability/synthetics):** Proactively simulate user journeys and API calls to test application availability and functionality.
  - **[Uptime monitoring](https://www.elastic.co/docs/solutions/observability/uptime):** Continuously check the status of services and applications to ensure they are available.
  - **[LLM Observability](https://www.elastic.co/docs/solutions/observability/applications/llm-observability):** Gain deep insights into the performance, usage, and costs of Large Language Model (LLM) prompts and responses.
  - **[Incident response and management](https://www.elastic.co/docs/solutions/observability/incident-management):** Investigate operational incidents by correlating data from multiple sources, accelerating root cause analysis and resolution.
  - **[Universal Profiling](https://www.elastic.co/docs/solutions/observability/infra-and-hosts/get-started-with-universal-profiling):** Gain visibility into system performance and identify expensive lines of code without application instrumentation, helping to increase CPU efficiency and reduce cloud spend.
</dropdown>

To start your Observability journey, read the [**Get started**](https://www.elastic.co/docs/solutions/observability/get-started) guide, which presents all the essential steps, with links to valuable resources. You can also browse the Observability [**Quickstart guides**](https://www.elastic.co/docs/solutions/observability/get-started/quickstarts).

## Core concepts

At the heart of Elastic Observability are several key components that enable its capabilities.
<dropdown title="Concepts">
  - The three pillars of Observability are:
    - [**Logs:**](https://www.elastic.co/docs/solutions/observability/logs) Timestamped records of events that provide detailed, contextual information.
  - [**Metrics:**](https://www.elastic.co/docs/solutions/observability/infra-and-hosts/analyze-infrastructure-host-metrics) Numerical measurements of system performance and health over time.
  - [**Traces:**](https://www.elastic.co/docs/solutions/observability/apm/traces) Representations of end-to-end journeys of requests as they travel through distributed systems.
  - [**OpenTelemetry:**](https://www.elastic.co/docs/solutions/observability/apm/opentelemetry) Observability offers first-class, production-grade support for OpenTelemetry. This allows organizations to use vendor-neutral instrumentation and stream native OTel data without proprietary agents, leveraging the Elastic Distribution of OpenTelemetry (EDOT).
  - [**AIOps and AI Assistant:**](https://www.elastic.co/docs/solutions/observability/ai/observability-ai-assistant) Leverages predictive analytics and an LLM-powered AI Assistant to reduce the time required to detect, investigate, and resolve incidents. This includes zero-config anomaly detection, pattern analysis, and the ability to surface correlations and root causes.
  - **[Alerting](https://www.elastic.co/docs/solutions/observability/incident-management/alerting)**: Allows you to create  rules to detect complex conditions and perform actions.
  - **[Cases](https://www.elastic.co/docs/solutions/observability/incident-management/observability-cases):** Cases allows teams to stay aware of potential issues and track investigation details, assign tasks, and collaborate on resolutions.
  - [**Service Level Objectives (SLOs):**](https://www.elastic.co/docs/solutions/observability/incident-management/service-level-objectives-slos) A framework for defining and monitoring the reliability of a service. Elastic Observability allows for creating and tracking SLOs to ensure you meet your performance targets.
</dropdown>


## Related reference

The Observability reference documentation is available in the [Elastic reference documentation](https://www.elastic.co/docs/reference/observability).
You can also browse reference documentation for the following components:
- [Elastic Distributions of OpenTelemetry (EDOT)](https://www.elastic.co/docs/reference/opentelemetry)
- [Fleet and Elastic Agent](https://www.elastic.co/docs/reference/fleet)
- [Elastic APM](https://www.elastic.co/docs/reference/apm/observability/apm)
- [Elastic APM agents](https://www.elastic.co/docs/reference/apm-agents)

Browse the latest [Observability release notes](https://www.elastic.co/docs/release-notes/observability) for more information on new features, enhancements, and fixes.