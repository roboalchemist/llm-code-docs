# Source: https://docs.datadoghq.com/administrators_guide/plan.md

---
title: Plan your Datadog installation
description: Plan out your Datadog installation for success.
breadcrumbs: Docs > Administrator's Guide > Plan your Datadog installation
source_url: https://docs.datadoghq.com/plan/index.html
---

# Plan your Datadog installation

## Overview{% #overview %}

When you plan a new software installation, its crucial to understand its capabilities, objectives, timelines, teams, and design patterns. In the plan phase, learn Datadog basics, define your most important objectives, understand best practices, and identify how to optimize your Datadog installation.

## Design{% #design %}

### Scoping exercise{% #scoping-exercise %}

Setting a clear goal is critical for installing Datadog. However, in a practical world, it is impossible to predict everything you might need at the outset. Product engineers iterate their rollouts and systems operators control their changes, all to control risk. Implementing a large-scale Datadog installation will benefit from standard project management practices. As part of that process, there are certain Datadog elements that you should include.

**Recommendations:**Start collecting and consolidating a survey of your organization early. Create a comprehensive view of your ecosystems, application languages, data storage, networking, and infrastructure.

A sample survey form might look like this:

```
Application name:  
  Language:  
     Frameworks:  
  Model layer:  
  View layer: 
  Controller layer:  
  Infra type:  
  Operating systems:
```

## General best practices{% #general-best-practices %}

Complete the scoping exercise to understand the types of technologies you're working with, and start mapping those to core products in Datadog.

### Resource tagging{% #resource-tagging %}

Datadog is a tool for correlating machine data with the running applications and its physical descriptors. It can cross-reference an individual piece of data against others, regardless of type. Hostname, cloud regions, operating system version, and IP are just some of the automatically applied resource attributes. Additionally, Datadog allows you to generate custom tags such as `cost-code`, `AppName`, `environment`, and `version`.

Datadog's strength lies in its capability to maintain and manage a unified vocabulary and includes built-in data features. [Unified Service Tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/) uses reserved tags that enable telemetry correlation across all features of the Datadog platform.

Tags are `key:value` pairs or simple values. They add dimension to application performance data and infrastructure metrics. Before you begin monitoring with Datadog, take advantage of the tagging capabilities that your platforms offer, as Datadog automatically imports these tags through its integrations. The following table is a representation of how `key:value` pairs work and whether the tags are added automatically or manually.

| TAG                     | KEY            | VALUE     | METHOD    |
| ----------------------- | -------------- | --------- | --------- |
| env:staging             | env            | staging   | automatic |
| component_type:database | component_type | database  | manual    |
| region:us-west-1        | region         | us-west-1 | automatic |

The [Getting started with tagging](https://docs.datadoghq.com/getting_started/tagging/) guide is a great place to start with this topic. Here are some additional highlights:

- A service is defined as a single application footprint, something that can be deployed independently.
- Tag values must be consistent. For example, "Production" is different from "Prod".
- Define sources of truth for dynamic tags such as code version.

**Recommendations**:

- As early as possible, understand [Datadog Unified Service Tagging](https://docs.datadoghq.com/getting_started/tagging/) and develop your tagging scheme.
- Align your infrastructure with your collected tags and automate the tagging process where possible (for example, use git hash values from CI pipelines as version tags through Kubernetes labels). This unifies your data, allowing you to create informative alerts by assigning [owners to services](https://docs.datadoghq.com/software_catalog/service_definitions/) and to pivot between service metrics, logs, and traces.

The following diagram depicts how each of the three reserved tags may look as you are building out your environment:

{% image
   source="https://datadog-docs.imgix.net/images/administrators_guide/unified_service_tagging_diagram.347cd72585dd71eac5a45b33928f81e8.png?auto=format"
   alt="Diagram of Unified Service tagging with the 3 reserved tags: Service, Env, Version" /%}

### Access control{% #access-control %}

At the architectural design level, there are two main areas of access control within Datadog: organization structure, and [role-based access control (RBAC)](https://docs.datadoghq.com/account_management/rbac/?tab=datadogapplication).

#### RBAC{% #rbac %}

Datadog role-based access control can connect to your existing SAML authentication service. SAML group-mappings can be built against the Datadog default roles and team objects. Datadog provides three default roles, which you can customize to match the complexity of your own AD/LDAP Roles. You can also set up [service accounts](https://docs.datadoghq.com/account_management/org_settings/service_accounts/) for non-interactive purposes like [API and App Key](https://docs.datadoghq.com/account_management/api-app-keys/) ownership, to separate user activities from system tasks. Granular permissions set the access and protections you need.

As an additional layer, [Teams](https://docs.datadoghq.com/account_management/teams/) lets you set up flexible, informal, and ad-hoc groups that users can join or be added to. The Teams feature is available throughout Datadog products.

#### Multi-Organizational Structure{% #multi-organizational-structure %}

Larger Datadog customers often have more than one Datadog installation. This is typically used by managed service providers to ensure that their customers do not have access to one another's data. In some cases, full isolation within a single company is necessary. To accommodate this topology, you can manage [multiple organizational accounts](https://docs.datadoghq.com/account_management/multi_organization/). For example, you can view total usage at the parent level, while remaining completely separate technologically. Child organizations should be managed from a single parent organization account.

**Recommendations:**

- Establish a specific plan for building out Datadog user roles.
- Leverage service accounts for API key administration.
- Explore Teams to link resources such as dashboards, services, monitors, and incidents to a group of users.

## Product best practices{% #product-best-practices %}

### APM{% #apm %}

APM depends on the application of Unified Service Tagging. These tags are pivotal to the operational experience, and are also useful for enabling correlation across your telemetry data. This is how Datadog can help determine the owner for a random Java process it discovers.Usually, the default APM setup is sufficient for most use cases, but if, for example, you want to change sampling rates or to customize other APM configurations, use the following guidelines.

**Recommendations:**

- Identify the services to instrument and determine whether they are host-based, containerized, or serverless.
- Determine the method available for instrumenting your services in Datadog, depending on the language used or their runtime environment. These methods range from single-step to manual [instrumentation](https://docs.datadoghq.com/tracing/trace_collection/).
- Review the [ingestion controls](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls/) documentation.
- Configure your sampling rate with [Remote Configuration](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls/#managing-ingestion-for-all-services-at-the-agent-level) to scale your organization's trace ingestion according to your needs, without needing to restart your Agent. For more information, see [sampling rate use cases](https://docs.datadoghq.com/tracing/guide/ingestion_sampling_use_cases/).
- Ensure [Unified Service Tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/?tab=kubernetes) is applied, and review [span tag semantics](https://docs.datadoghq.com/tracing/trace_collection/tracing_naming_convention/).
- Opt in to [inferred service dependencies](https://docs.datadoghq.com/tracing/services/inferred_services) to enable automatic detection of your service names from span attributes.

### Log Management{% #log-management %}

Log Management capabilities allow you and your teams to diagnose and fix your infrastructure issues. [Logging without Limitsâ¢](https://docs.datadoghq.com/logs/guide/getting-started-lwl/) enables you to create tunable log collection patterns and extract information from your log data into custom metrics. You can also receive alerts about critical errors in your logs, without needing to index your logs.

{% image
   source="https://datadog-docs.imgix.net/images/administrators_guide/logging_without_limits.606e94693cb56150c9391925ea82767f.png?auto=format"
   alt="Logging without Limits diagram" /%}

Datadog's log index architecture is a distributed, timeseries, columnar store that is optimized for serving large scan and aggregation queries. See [Introducing Husky](https://www.datadoghq.com/blog/engineering/introducing-husky/) and [Husky Deep Dive](https://www.datadoghq.com/blog/engineering/husky-deep-dive/) for more information about Datadog's logging architecture.

The logging platform can be configured with many layers of logs storage. Each has its own use-cases outlined here:

| Data captured                                                                                              | Retention       | Retrieval to Datadog                                                                                  | Cost Driver |
| ---------------------------------------------------------------------------------------------------------- | --------------- | ----------------------------------------------------------------------------------------------------- | ----------- |
| Ignored                                                                                                    | No              | None                                                                                                  | None        | N/A                    |
| [Ingested](https://docs.datadoghq.com/logs/log_configuration/logs_to_metrics/)                             | Logs-to-metrics | 15m in LiveTail                                                                                       | None        | Volume                 |
| [Archive](https://docs.datadoghq.com/logs/log_configuration/archives/?tab=awss3)                           | Upon rehydrate  | Infinite                                                                                              | Slow        | Volume                 |
| [Forward logs](https://docs.datadoghq.com/logs/log_configuration/forwarding_custom_destinations/?tab=http) | Logs-to-metrics | Determined by target                                                                                  | None        | Volume                 |
| [Index](https://docs.datadoghq.com/logs/log_configuration/indexes)                                         | Yes             | 3,7,15,30 days                                                                                        | Immediate   | Volume & message count |
| [Flex Logs](https://docs.datadoghq.com/logs/log_configuration/flex_logs/)                                  | Yes*            | [Storage tiers](https://docs.datadoghq.com/logs/log_configuration/flex_logs/#configure-storage-tiers) | Rapid       | Retrieval volume       |

\* Flex Logs capability does not include monitors/alerting and Watchdog. However, you can still perform log-to-metrics on the ingestion stream before logs are indexed (in either standard or flex) and use those metrics in monitors. Correlation with other telemetry, such as traces, is supported.

With these base functions, you can ingest and monitor logs for some of the following use-cases:

{% dl %}

{% dt %}
Log format normalization
{% /dt %}

{% dd %}
Centralized control of date/time, value replacement, and referenced lookup.
{% /dd %}

{% dt %}
Global Sensitive Data and Personally Identifiable Information (PII) Management
{% /dt %}

{% dd %}
Personally Identifiable Information (PII) and Sensitive Data Scanner (SDS) are scrubbed first.
{% /dd %}

{% dt %}
Routing and forwarding
{% /dt %}

{% dd %}
One centralized UI to send logs to index, archive, or forwarding destination.
{% /dd %}

{% dt %}
Cost-effective value capture
{% /dt %}

{% dd %}
Malleable log field definition, and high volume/low value distillation.
{% /dd %}

{% dt %}
Global log archive
{% /dt %}

{% dd %}
Catch-all log archiver.
{% /dd %}

{% dt %}
Global SIEM
{% /dt %}

{% dd %}
All logs are tested for security at ingestion as a pre-processor.
{% /dd %}

{% /dl %}

**Recommendations:**

- Determine the method to ship your logs to Datadog, either directly to the Datadog logs URL intake endpoints, or from tools like Fluentbit, Syslog, or Logstash.
- Fine-tune your log ingestion plan and review best practices for log management.
- Understand [Logging without Limits](https://docs.datadoghq.com/logs/guide/getting-started-lwl/)â¢ Identify the status of your most logged services, observe high volume logging patterns, and create log pattern exclusion filters.
- Configure [log archives](https://docs.datadoghq.com/logs/log_configuration/archives/?tab=awss3).

### Real User Monitoring{% #real-user-monitoring %}

Real User Monitoring and Session Replay give detailed insights into the experiences of your service or application end-user. Install RUM on applications with high value sessions to leverage the data for meaningful changes. Session Replay provides a visual representation that is invaluable for troubleshooting issues observed by users. You can track the actual customer experience, which is most valuable in production environments.

**Recommendations:**

- Identify the websites, mobile application screens, user actions, and frontend code that is critical to your business to track.
- Deploy RUM and Session Replay to production and near-production environments.
- [Discard front-end errors](https://docs.datadoghq.com/real_user_monitoring/guide/enrich-and-control-rum-data/?tab=event).
- Configure your [RUM sampling rate](https://docs.datadoghq.com/real_user_monitoring/guide/best-practices-for-rum-sampling/).

### Synthetic Monitoring{% #synthetic-monitoring %}

Synthetic Monitoring is a full synthetic testing suite, which includes testing for browser applications, mobile apps, and APIs. Synthetic test results can be linked back to the application behavior it generated, and from there, into the database, message queues, and downstream services.

**Recommendations:**

- Identify the API endpoints and user journeys that are central to your business and test those frequently.
- Develop a roadmap of business transactions to test.
- Use Synthetic Monitoring in conjunction with [APM and RUM](https://docs.datadoghq.com/real_user_monitoring/correlate_with_other_telemetry/apm?tab=browserrum).
- Review [Synthetic monitoring consumption considerations](https://www.datadoghq.com/pricing/?product=synthetic-testing--monitoring#synthetic-testing--monitoring-common-questions).
- Reduce test maintenance by using [subtests](https://docs.datadoghq.com/synthetics/browser_tests/advanced_options/#subtests).
- Make intentional choices in test location selection. Test from where your customers actually are.
- Use the [HTTP Check](https://docs.datadoghq.com/integrations/http_check/) or [TCP check](https://docs.datadoghq.com/integrations/tcp_check/?tab=host#data-collected) to monitor SSL certificate expiration or basic uptime.

## Integrations{% #integrations %}

You can use Datadog's 1,000+ integrations to bring together all of the metrics and logs from your infrastructure, to gain insights into an entire observability system. The integrations, either SaaS-based or Agent-based, collect metrics to monitor within Datadog. Host-based integrations are configured with yaml files that live in the `conf.d` directory, and container-based integrations are configured with metadata such as annotations or labels.

There are different types of integrations in Datadog, and the order in which they are presented here is the order Datadog recommends for their installation.

| Category                                                                                                                                                                                                                                | Description                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Cloud Technologies ([AWS](https://docs.datadoghq.com/integrations/amazon_web_services/), [Google Cloud](https://docs.datadoghq.com/integrations/google_cloud_platform/), [Azure](https://docs.datadoghq.com/integrations/azure/))       | These integrations use provisioned credentials to scrape monitoring endpoints for metrics. Fine-tune these to ingest only desired telemetry.    |
| Incident Response ([Slack](https://docs.datadoghq.com/integrations/slack/?tab=datadogforslack), [Jira](https://docs.datadoghq.com/integrations/jira/), [PagerDuty](https://docs.datadoghq.com/integrations/pagerduty/))                 | These integrations send notifications when events occur and are vital for establishing an efficient alerting system.                            |
| Infrastructure ([orchestration](https://docs.datadoghq.com/integrations/#cat-orchestration), [operating system](https://docs.datadoghq.com/integrations/#cat-os-system), [network](https://docs.datadoghq.com/integrations/network/))   | These integrations serve as the foundational components for monitoring your infrastructure, gathering both metrics and logs.                    |
| Data Layers ([data stores](https://docs.datadoghq.com/integrations/#cat-data-stores), [message queues](https://docs.datadoghq.com/integrations/#cat-message-queues))                                                                    | These integrations usually query internal DB metrics tables, so this usually requires a database administrator to provide access for the Agent. |
| Development ([automation](https://docs.datadoghq.com/integrations/#cat-automation), [languages](https://docs.datadoghq.com/integrations/#cat-languages), [source control](https://docs.datadoghq.com/integrations/#cat-source-control)) | These integrations push metrics to Datadog and require configuration on their end. Some may require DogStatsD to ship metrics.                  |
| Security and Compliance ([Okta](https://docs.datadoghq.com/integrations/okta/))                                                                                                                                                         | These integrations enable you to verify compliance with your standards.                                                                         |

**Recommendations**:

- Start collecting metrics on your projects as early in the development process as possible.
- Installed Agents automatically have system and NTP integrations running and can autodetect supported technologies on the host. (Live processes must be enabled for this functionality)
- You can choose from the above list what you would like to monitor. If there are services you want to monitor that do not have an integration, you can explore Live processes, [Universal Services Monitoring](https://docs.datadoghq.com/universal_service_monitoring/), a [process integration](https://docs.datadoghq.com/integrations/process/), or a [custom check](https://docs.datadoghq.com/developers/custom_checks/#should-you-write-a-custom-agent-check-or-an-integration).

## Additional resources{% #additional-resources %}

You've achieved some important wins and adopted best practices with APM, RUM, Synthetic Monitoring and Log Management. Some additional resources that are important when planning your installation phase are outlined below.

### Live processes{% #live-processes %}

Use [Live processes](https://docs.datadoghq.com/infrastructure/process/?tab=linuxwindows) to view all of your running processes in one place. For example, see PID-level information of a running Apache process, to help you understand and troubleshoot transient issues. Additionally, you can query for processes running on a specific host, in a specific availability zone, or running a specific workload. [Configure](https://docs.datadoghq.com/infrastructure/process/?tab=linuxwindows%5c#installation) live processes on your hosts, containers, or Amazon ECS Fargate instances to take advantage of this feature.

### Availability, latency, and SSL expiration{% #availability-latency-and-ssl-expiration %}

Web server operations depend on the network availability of ports, the validity of SSL certificates, and low latencies. Install the [HTTP_Check](https://docs.datadoghq.com/integrations/http_check/) to monitor local or remote HTTP endpoints, detect bad response codes (such as 404), and use Synthetic API tests to identify soon-to-expire [SSL certificates](https://docs.datadoghq.com/synthetics/api_tests/ssl_tests/).

### Cloud Network Monitoring{% #cloud-network-monitoring %}

Web servers are almost always inter-connected with other services through a network fabric that is vulnerable to drops and can result in re-transmits. Use Datadog's [network integration](https://docs.datadoghq.com/integrations/network/) and enable [Cloud Network Monitoring](https://docs.datadoghq.com/network_monitoring/cloud_network_monitoring/) to gain visibility into your network traffic between services, containers, availability zones, and other tags on your infrastructure.

## Platform services{% #platform-services %}

Datadog infrastructure monitoring comes with additional products that you can use to maximize observability of your environments.

### Software Catalog{% #software-catalog %}

[Software Catalog](https://docs.datadoghq.com/software_catalog/) provides an overview of services, showing which were recently deployed, which haven't been deployed for a while, which services report the most errors, and those with on-going incidents, and much more.

Software Catalog also helps you evaluate the coverage of your observability setup. As you continue your roll out, you can check in on the Setup Guidance tab of each of your services, to ensure that they have the expected configurations:

{% image
   source="https://datadog-docs.imgix.net/images/administrators_guide/software_catalog_2.a228d9a5b2f15f34f7dd7a259eb913c8.png?auto=format"
   alt="Software Catalog home screen" /%}

You can add components that you aren't planning on monitoring immediately, such as cron jobs or libraries, to create a comprehensive view of your system, and to mark team members who are responsible for these components ahead of the next phase of your Datadog rollout.

Refer to the [Endpoints list](https://docs.datadoghq.com/software_catalog/endpoints/) to categorize, monitor performance and reliability, and manage ownership of your API endpoints.

### Resource Catalog{% #resource-catalog %}

Use [Resource Catalog](https://docs.datadoghq.com/infrastructure/resource_catalog/) to view key resource information such as metadata, ownership, configurations, relationships between assets, and active security risks. It is the central hub of all of your infrastructure resources. Resource Catalog offers visibility into infrastructure compliance, promotes good tagging practices, reduces application risks by identifying security vulnerabilities, provides engineering leadership with a high-level view of security practices, and allows resource export for record-keeping or auditing.

You can use Resource Catalog in a variety of contexts, including:

- Understanding the team ownership of resources and finding orphaned ones to clean up.
- Planning upgrades of resources that are running deprecated versions.
- Accessing configuration information and other metadata to speed up incident response.
- Maintaining your security posture by finding and resolving misconfigurations and vulnerabilities.

### Event Management{% #event-management %}

Without any additional setup, [Event management](https://docs.datadoghq.com/events/) can show third-party event statuses, events generated from the Agent and installed integrations. Datadog Event Management centralizes third-party events, such as alerts and change events. Datadog also automatically creates events from various products including monitors and Error Tracking. You can also use Event Management to send monitor alerts and notifications based on event queries.

### Error Tracking{% #error-tracking %}

See errors where they happen with Datadog's [Error Tracking](https://docs.datadoghq.com/error_tracking/). Error Tracking can ingest errors from APM, Log Management, and Real User Monitoring to debug issues faster.

### Fleet Automation{% #fleet-automation %}

Centrally administer and manage all of your Datadog Agents with [Fleet Automation](https://docs.datadoghq.com/agent/fleet_automation/). Fleet Automation can identify which Agents need upgrading, send a flare to support, and help in the task of disabling or rotating API keys.

{% image
   source="https://datadog-docs.imgix.net/images/administrators_guide/fleet_automation.e9d0daa5ff5fd811b750855f3593409b.png?auto=format"
   alt="Fleet Management home screen" /%}

### Remote Configuration{% #remote-configuration %}

Use Datadog's [Remote Configuration](https://docs.datadoghq.com/remote_configuration) (enabled by default), to remotely configure and change the behavior of Datadog components (for example, Agents, tracing libraries, and Observability Pipelines Worker) deployed in your infrastructure. For more information, see [supported products and capabilities](https://docs.datadoghq.com/remote_configuration#supported-products-and-features).

### Notebooks{% #notebooks %}

Use Datadog [Notebooks](https://docs.datadoghq.com/notebooks/) to share information with team members and to aid troubleshooting investigations or incidents.

## Optimizing data collection{% #optimizing-data-collection %}

Datadog collects many things in your environments, so it is important to limit the amount of collection points and establish guard rails. In this section, you'll learn the mechanisms that control the telemetry collection, and discuss how you can codify your organization's needs.

### Infrastructure{% #infrastructure %}

Datadog interacts with the monitoring API of HyperVisor managers (Hyper-V, vSphere, PCF), container schedulers (Kubernetes,Rancher, Docker), and public cloud providers (AWS, Azure, GCP). The platform to [autodiscover](https://docs.datadoghq.com/getting_started/containers/autodiscovery/?tab=adannotationsv2agent736) resources (pods, VMs, EC2s, ALBs, AzureSQL, GCP blobs) within those environments. It is important to limit the number of monitored resources, because they have billing implications.

**Recommendations**:

Enable resource collection for [AWS](https://docs.datadoghq.com/account_management/billing/aws/#aws-resource-exclusion) and [GCP](https://docs.datadoghq.com/integrations/google_cloud_platform/?tab=project#resource-changes-collection) to view an inventory of resources, as well as cost and security insights. Additionally, limit metric collection for your [Azure resources](https://docs.datadoghq.com/integrations/guide/azure-native-integration/#metrics-and-logs) and your [containerized](https://docs.datadoghq.com/containers/guide/container-discovery-management/?tab=datadogoperator) environments.

## Service Tiers{% #service-tiers %}

During the planning phase, you may find that not all instances of observability are equally important. Some are mission-critical, while others are not. For this reason, it is useful to devise patterns for coverage levels, and which environments you want to monitor with Datadog. For example, a production environment might be monitored at every level, but a development instance of the same application might only have the developer-focused tooling.

**Recommendations**:

- Establish estimates of service tiers early on. They do not need to be precise at first, but will be useful as adoption scales up.

### Software Development Lifecycle{% #software-development-lifecycle %}

To begin mapping out your installation patterns, combine the information you gathered from the scoping exercise with the [Datadog 101](https://learn.datadoghq.com/courses/dd-101-sre) training, and develop a plan of action. Consider the following example, and modify it to suit your organization's needs. The example outlines an installation pattern from the dimension of SDLC environment (dev, qa, stage, prod), and you can customize it to your standards and conditions. Begin setting expectations within your own Datadog user base what "Standard Datadog installation" means.

| Dev                      | QA         | Staging    | Prod  |
| ------------------------ | ---------- | ---------- | ----- |
| **APM**                  | Deny/Allow | Allow      | Allow | Allow |
| **Synthetic Monitoring** | Deny       | Deny/Allow | Allow | Allow |
| **Log Management**       | Allow      | Allow      | Allow | Allow |
| **RUM**                  | Deny       | Deny/Allow | Allow | Allow |
| **DBM**                  | Deny/Allow | Deny/Allow | Allow | Allow |
| **Live Processes**       | Deny       | Deny/Allow | Allow | Allow |
|  |

**Recommendations** : Not every tool suits every job. Evaluate Datadog's product use cases and match them with your needs. Consider the SDLC levels, application importance, and the purpose of each Datadog product.

## Summary{% #summary %}

It is important to develop and plan a realistic course for installing Datadog. In this section, you learned about the planning and best practices phase, setting your Datadog footprint up for success. You identified and assembled your knowledge base and team members, developed your installation models, planned optimizations, and compiled a list of best practices for core products. These foundations prepare you for the next phases of Datadog installation: build and run.

## Next Steps{% #next-steps %}

Create a detailed roll-out methodology in the [build](https://docs.datadoghq.com/administrators_guide/build) phase by focusing on the construction of Datadog itself, iterate on your environment, establish some internal support mechanisms, and prepare for production.

## Further Reading{% #further-reading %}

- [Getting Started with Unified Service Tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/)
- [Getting Started with APM Tracing](https://docs.datadoghq.com/getting_started/tracing/)
