# Source: https://docs.datadoghq.com/actions/app_builder/events.md

# Source: https://docs.datadoghq.com/account_management/audit_trail/events.md

# Source: https://docs.datadoghq.com/api/latest/events.md

# Source: https://docs.datadoghq.com/events.md

---
title: Event Management
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Event Management
---

# Event Management

{% image
   source="https://datadog-docs.imgix.net/images/service_management/events/correlation/event_management.a3f8cd0d834fad20182d2cc01953dcbd.png?auto=format"
   alt="what is event management" /%}

## Overview{% #overview %}

Ingest, enrich and normalize, and correlate your events from any source into actionable insights. Datadog automatically creates events from various products including monitors, Watchdog, and Error Tracking. You can also track events generated from the Agent and installed integrations. Event Management can also ingest events from any source, including alert events from third parties, change requests, deployments, configuration changes.

More than 100 Datadog integrations support events collection, including [Kubernetes](https://docs.datadoghq.com/agent/kubernetes/#event-collection), [Docker](https://docs.datadoghq.com/agent/docker/#events), [Jenkins](https://docs.datadoghq.com/integrations/jenkins/#events), [Chef](https://docs.datadoghq.com/integrations/chef/#report-handler), [Puppet](https://docs.datadoghq.com/integrations/puppet/#events), [Amazon ECS](https://docs.datadoghq.com/integrations/amazon_ecs/#events) or [Autoscaling](https://docs.datadoghq.com/integrations/amazon_auto_scaling/#events), [Sentry](https://docs.datadoghq.com/integrations/sentry/), and [Nagios](https://docs.datadoghq.com/integrations/nagios/#events).

**Tip**: To open the Event Management page from Datadog's global search, press `Cmd`/`Ctrl` + `K` and search for `event explorer`.

**Update to Datadog monitor events `aggregation_key` starting March 1, 2025:** The Datadog monitor events `aggregation_key` is unique to each Monitor ID. Starting March 1st, this key will also include Monitor Group, making it unique per *Monitor ID and Monitor Group*. If you're using monitor events `aggregation_key` in dashboard queries or the Event API, you must migrate to use `@monitor.id`. Reach out to [support](https://docs.datadoghq.com/help/) if you have any questions.

## Components{% #components %}

- [Ingest events- Learn how to send events to Datadog](https://docs.datadoghq.com/events/ingest/)
- [Triage Inbox- Triage, investigate, collaborate, and resolve incidents](https://docs.datadoghq.com/events/triage_inbox)
- [Pipelines and Processors- Enrich and Normalize your events](https://docs.datadoghq.com/events/pipelines_and_processors/)
- [Events Explorer- View, search and send notifications from events coming into Datadog](https://docs.datadoghq.com/events/explorer/)
- [Using events- Analyze, investigate, and monitor events](https://docs.datadoghq.com/events/guides/usage/)
- [Correlation- reduce alert fatigue and the number of tickets/notifications you receive](https://docs.datadoghq.com/events/correlation/)

## Further Reading{% #further-reading %}

- [Datadog Events API](https://docs.datadoghq.com/api/latest/events/)
- [Best Practices for Tagging Events](https://docs.datadoghq.com/events/guides/recommended_event_tags/)
- [Identify and redact sensitive data in Events with Sensitive Data Scanner](https://www.datadoghq.com/blog/identify-sensitive-data-leakage-in-apm-rum-with-sensitive-data-scanner/)
- [Quick Start Guide](https://app.datadoghq.com/event/configuration/quick-start)
- [Aggregate, correlate, and act on alerts faster with AIOps-powered Event Management](https://www.datadoghq.com/blog/datadog-event-management)
- [Ensure high service availability with Datadog Service Management](https://www.datadoghq.com/blog/datadog-service-management/)
