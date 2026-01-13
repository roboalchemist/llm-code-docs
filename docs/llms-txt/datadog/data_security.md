# Source: https://docs.datadoghq.com/data_security.md

---
title: Reducing Data Related Risks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Reducing Data Related Risks
source_url: https://docs.datadoghq.com/index.html
---

# Reducing Data Related Risks

{% alert level="info" %}
This page is about the tools and security for protecting data sent to Datadog. If you're looking for cloud and application security products and features, see the Security section.
{% /alert %}

In the normal course of using Datadog as intended, you send data to Datadog. Datadog works together with you to reduce data risk by providing you tools to appropriately limit the data you send and securing data during and after its transmission.

You may also wish to review the information available at [Datadog Security](https://www.datadoghq.com/security/) and the terms of our [Privacy Policy](https://www.datadoghq.com/legal/privacy/).

## How data gets from you to Datadog{% #how-data-gets-from-you-to-datadog %}

Datadog allows you to send data to Datadog in multiple ways, including from the Agent, [DogStatsD](https://docs.datadoghq.com/developers/dogstatsd/), the public API, and integrations. In addition, Real User Monitoring SDKs and tracing libraries generate data based on your application and services code and send it to Datadog.

Data in motion through Datadog provided tools is protected with TLS and HSTS. Data stored by Datadog is protected by encryption, access controls, and authentication. For specifics, read more at [Datadog Security](https://www.datadoghq.com/security/).

### The Datadog Agent{% #the-datadog-agent %}

The Agent is the main channel for data getting from your systems to Datadog. [Read all about data security measures in the Agent](https://docs.datadoghq.com/data_security/agent/).

To learn how to avoid storing secrets in plaintext in the Agent's configuration files, see [Secrets Management](https://docs.datadoghq.com/agent/configuration/secrets-management/).

### Third party services integrations{% #third-party-services-integrations %}

The integrations for some third party services are configured directly in Datadog and might require you to provide credentials to allow Datadog to connect to the service on your behalf. The credentials you provide are encrypted and stored by Datadog in a secure credential datastore.

All data through these integrations is encrypted when at-rest in Datadog's systems and encrypted in-transit. Access to the secure credential datastore is controlled and audited, and specific services or actions within the third party services are limited to only what is necessary. Anomalous behavior detection tools continuously monitor for unauthorized access. Datadog employee access for maintenance purposes is limited to a select subset of engineers.

### Cloud integrations{% #cloud-integrations %}

Due to their sensitive nature, additional security measures are implemented, where possible, when integrating with cloud providers, including the use of Datadog-dedicated credentials with limited permissions. For example:

- The [integration with Amazon Web Services](https://docs.datadoghq.com/integrations/amazon_web_services/) requires you to configure role delegation using AWS IAM, as per the [AWS IAM Best Practices guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#delegate-using-roles), and to grant specific permissions with an AWS Policy.
- The integration with [Microsoft Azure](https://docs.datadoghq.com/integrations/azure/) relies on you defining a tenant for Datadog, with access to a specific application granted only the "reader" role for the subscriptions you would like to monitor.
- The integration with [Google Cloud Platform](https://docs.datadoghq.com/integrations/google_cloud_platform/) relies on you defining a service account for Datadog, and granting it only the "Compute Viewer" and "Monitoring Viewer" roles.

## Measures you can implement to reduce your data risk{% #measures-you-can-implement-to-reduce-your-data-risk %}

Datadog's purpose is to gather observability information from many sources around your infrastructure and services and to bring it together in one place for you to analyze and investigate. This involves you sending a wide range of types of data content to Datadog's servers. Most of the data gathered for the intended use of the Datadog products has little chance of containing private or personal data. For the data that may contain unnecessary private or personal data, we provide instructions, tools, and recommendations to enable you to strip out, obfuscate, and otherwise reduce the inclusion of private or personal data in the data shared with Datadog.

### Sensitive Data Scanner{% #sensitive-data-scanner %}

Sensitive Data Scanner is a stream-based, pattern matching service that you can use to identify, tag, and optionally redact or hash sensitive data. With implementation, your security and compliance teams can introduce a line of defense in preventing sensitive data from leaking outside your organization. For information about the scanner and setting it up, read [Sensitive Data Scanner](https://docs.datadoghq.com/security/sensitive_data_scanner/).

### Logs Management{% #logs-management %}

Logs are records produced by your systems and services and the activities that happen within them. Read about logs data security considerations, including information about how you can filter and obfuscate logs data in [Log Management Data Security](https://docs.datadoghq.com/data_security/logs/).

Dive deep into controlling logs data with the [Manage Sensitive Logs Data Access](https://docs.datadoghq.com/logs/guide/manage-sensitive-logs-data-access/) guide and [Agent Advanced Configuration for Logs](https://docs.datadoghq.com/agent/logs/advanced_log_collection).

A key approach to reducing risk around logs data security is access control. Read [How to set up RBAC for Logs](https://docs.datadoghq.com/logs/guide/logs-rbac) and [Logs RBAC Permissions](https://docs.datadoghq.com/logs/guide/logs-rbac-permissions) to learn how to do this in Datadog.

### Live processes and containers{% #live-processes-and-containers %}

To prevent leaking sensitive data when you're monitoring live processes and live containers, Datadog provides some default sensitive keyword scrubbing in process arguments and in Helm charts. You can obfuscate additional sensitive sequences within process commands or arguments by using the [`custom_sensitive_words` setting](https://docs.datadoghq.com/infrastructure/process/#process-arguments-scrubbing), and add to the container scrubbing word list by using the [`DD_ORCHESTRATOR_EXPLORER_CUSTOM_SENSITIVE_WORDS` environment variable](https://docs.datadoghq.com/infrastructure/livecontainers/configuration/#scrubbing-sensitive-information).

### APM and other tracing library based products{% #apm-and-other-tracing-library-based-products %}

The Datadog tracing libraries are used to instrument your applications, services, tests, and pipelines, and send performance data through the Agent to Datadog. Trace and span data (along with much more) is generated for the following products to use:

- Application Performance Monitoring (APM)
- Continuous Profiler
- CI Visibility
- App and API Protection

For detailed information about how tracing-library sourced data is managed, default basic security settings, and custom obfuscating, scrubbing, excluding, and modifying of trace-related elements, read [Configuring Agent and Tracer for trace data security](https://docs.datadoghq.com/tracing/configure_data_security/).

### Serverless distributed tracing{% #serverless-distributed-tracing %}

You can use Datadog to collect and visualize the JSON request and response payloads of AWS Lambda functions. To prevent any sensitive data within request or response JSON objects from being sent to Datadog (like account IDs or addresses), you can scrub specific parameters from being sent to Datadog. Read [Obfuscating AWS Lambda payload contents](https://docs.datadoghq.com/serverless/distributed_tracing/collect_lambda_payloads#obfuscating-payload-contents) for more information.

### Synthetic Monitoring{% #synthetic-monitoring %}

Synthetic testing simulates requests and business transactions from testing locations around the world. Read about the encryption considerations for configurations, assets, results, and credentials, as well as how to use testing privacy options, in [Synthetic Monitoring Data Security](https://docs.datadoghq.com/data_security/synthetics/).

### RUM & Session Replay{% #rum--session-replay %}

You can modify the data collected by Real User Monitoring in the browser to protect personally identifiable information and to sample the RUM data you're collecting. Read [Modifying RUM Data and Context](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/browser/advanced_configuration/) for details.

Session Replay privacy options default to protecting end-user privacy and preventing sensitive organizational information from being collected. Read about masking, overriding, and hiding elements from a session replay in [Session Replay Privacy Options](https://docs.datadoghq.com/session_replay/browser/privacy_options).

### Database Monitoring{% #database-monitoring %}

The Database Monitoring Agent obfuscates all query bind parameters sent to the Datadog intake. Thus passwords, PII (Personally identifiable information), and other potentially sensitive information stored in your database will not be viewable in query metrics, query samples, or explain plans. To read about mitigating risk for other types of data involved in database performance monitoring, read [Database Monitoring Data Collected](https://docs.datadoghq.com/database_monitoring/data_collected/#sensitive-information).

## Other sources of potentially sensitive data{% #other-sources-of-potentially-sensitive-data %}

In addition to the sensitive data that you can automatically scrub, obfuscate, and otherwise avoid collecting, a lot of the data collected by Datadog is the names and descriptions of things. We recommend not including private or personal information in the text you are sending. Consider the following (non-exhaustive) list of text data you send to Datadog in the intended use of the product:

{% dl %}

{% dt %}
Metadata and tags
{% /dt %}

{% dd %}
Metadata consists primarily of [tags](https://docs.datadoghq.com/getting_started/tagging/) in the `key:value` format, for example, `env:prod`. Metadata is used by Datadog to filter and group data to help you derive meaningful information.
{% /dd %}

{% dt %}
Dashboards, notebooks, alerts, monitors, alerts, incidents, SLOs
{% /dt %}

{% dd %}
The text descriptions, titles, and names you give the things you create in Datadog are data.
{% /dd %}

{% dt %}
Metrics
{% /dt %}

{% dd %}
Metrics, including infrastructure metrics and metrics generated from integrations and other ingested data such as logs, traces, RUM, and synthetic tests, are timeseries used to populate graphs. They usually have associated tags.
{% /dd %}

{% dt %}
APM data
{% /dt %}

{% dd %}
APM data includes services, resources, profiles, traces, and spans, along with associated tags. Read [the APM Glossary](https://docs.datadoghq.com/tracing/glossary/) for an explanation about each.
{% /dd %}

{% dt %}
Database query signatures
{% /dt %}

{% dd %}
Database monitoring data consists of metrics and samples, along with their associated tags, collected by the Agent and used to track historical performance of normalized queries. The granularity of this data is defined by its normalized query signature and unique host identifier. All query parameters are obfuscated and discarded from collected samples before being sent to Datadog.
{% /dd %}

{% dt %}
Process information
{% /dt %}

{% dd %}
Processes consist of metrics and data from the `proc` filesystem, which acts as an interface to internal data structures in the kernel. Process data may contain the process command (including its path and arguments), the associated username, the ID of the process and its parent, the process state, and the working directory. Process data usually also has tag metadata associated with it.
{% /dd %}

{% dt %}
Events and comments
{% /dt %}

{% dd %}
Events data is aggregated from multiple sources into a consolidated view, including triggered monitors, events submitted by integrations, events submitted by the application itself, and comments sent by users or through the API. Events and comments usually have associated tags metadata.
{% /dd %}

{% dt %}
Continuous Integration pipelines and tests
{% /dt %}

{% dd %}
The names of branches, pipelines, tests, and test suites are all data sent to Datadog.
{% /dd %}

{% /dl %}

### Further Reading{% #further-reading %}

- [Logs Data Security](https://docs.datadoghq.com/data_security/logs/)
- [Agent Data Security](https://docs.datadoghq.com/data_security/agent/)
- [Synthetic Monitoring Data Security](https://docs.datadoghq.com/data_security/synthetics/)
- [Tracing Data Security](https://docs.datadoghq.com/tracing/configure_data_security/)
- [RUM Data Security](https://docs.datadoghq.com/data_security/real_user_monitoring/)
- [Session Replay Privacy Options](https://docs.datadoghq.com/session_replay/browser/privacy_options)
- [Sensitive Data Scanner](https://docs.datadoghq.com/security/sensitive_data_scanner/)
