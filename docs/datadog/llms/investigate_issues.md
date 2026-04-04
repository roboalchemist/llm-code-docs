# Source: https://docs.datadoghq.com/bits_ai/bits_ai_sre/investigate_issues.md

---
title: Investigate issues
description: >-
  Use Bits AI SRE to automatically investigate monitor alerts and provide root
  cause analysis for faster incident resolution.
breadcrumbs: Docs > Bits AI > Bits AI SRE > Investigate issues
---

# Investigate issues

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com, ap2.datadoghq.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Start a Bits AI SRE investigation{% #start-a-bits-ai-sre-investigation %}

You can start a Bits AI SRE investigation from:

- Monitor alerts, which you can trigger in two ways:
  - **Manual**: Start from an individual monitor alert, APM latency graph, or APM Watchdog story
  - **Automatic**: Configure monitors so that whenever they alert, Bits launches an investigation
- APM latency graphs on service pages (Preview)
- APM latency Watchdog stories (Preview)

### Manually start an investigation{% #manually-start-an-investigation %}

#### Monitor alerts{% #manual-monitor-alerts %}

You can invoke Bits on an individual monitor alert or warn event from several entry points:

##### Option 1: Bits AI SRE Monitors list{% #monitor-list %}

1. Go to [**Bits AI SRE** > **Monitors** > **Supported**](https://app.datadoghq.com/bits-ai/monitors/supported).
1. Click **Investigate Recent Alerts** and select an alert.

##### Option 2: Monitor status page{% #option-2-monitor-status-page %}

Navigate to the monitor status page of a Bits AI SRE-supported monitor and click **Investigate with Bits AI SRE** in the top-right corner.

##### Option 3: Monitor event side panel{% #option-3-monitor-event-side-panel %}

In the monitor event side panel of a Bits AI SRE-supported monitor, click **Investigate with Bits AI SRE**.

##### Option 4: Slack{% #option-4-slack %}

To use the Slack integration, [connect your Slack workspace to Bits AI SRE](https://docs.datadoghq.com/bits_ai/bits_ai_sre/configure#slack).

In Slack, reply to a monitor notification with `@Datadog Investigate this alert`.

#### APM latency{% #apm-latency %}

{% callout %}
##### Join the Preview!

Bits AI SRE investigations from APM latency graphs and APM Watchdog stories are in Preview. Click **Request Access** to join the Preview program.

[Request Access](http://datadoghq.com/product-preview/bits-ai-sre-pilot-features)
{% /callout %}

##### APM latency graphs on service pages{% #apm-latency-graphs-on-service-pages %}

1. In Datadog, navigate to [APM](https://app.datadoghq.com/apm/home) and open the service or resource page you want to investigate. Next to the latency graph, click **Investigate**.
1. Click and drag your cursor over the point plot visualization to make a rectangular selection over a region that shows unusual latency to seed the analysis. Initial diagnostics on the latency issue appear, including the observed user impact, anomalous tags contributing to the issue, and recent changes. For more information, see [APM Investigator](https://docs.datadoghq.com/tracing/guide/latency_investigator/).
1. Click **Investigate with Bits AI SRE** to run a deeper investigation.

##### APM latency Watchdog stories{% #apm-latency-watchdog-stories %}

On a Watchdog APM latency story, click **Investigate with Bits AI SRE**.

### Enable automatic investigations{% #enable-automatic-investigations %}

In addition to manual investigations, you can configure Bits to run automatically when a monitor transitions to the alert state:

#### From the Bits AI SRE Monitors list{% #from-the-bits-ai-sre-monitors-list %}

1. Go to [**Bits AI SRE** > **Monitors** > **Supported**](https://app.datadoghq.com/bits-ai/monitors/supported).
1. Toggle **Auto-Investigate** on for a single monitor, or bulk-edit multiple monitors by selecting multiple monitors, then clicking **Auto-Investigate All**.

#### For a single monitor{% #for-a-single-monitor %}

1. Open the monitor's status page and click **Edit**.
1. Scroll to **Configure notifications & automations** and toggle **Investigate with Bits AI SRE**.

{% alert level="info" %}

- Enabling automatic investigations using the Datadog API or Terraform is not supported.
- An investigation initiates when a monitor transitions to the alert state.
- Transitions to the warn or no data state, [renotifications](https://docs.datadoghq.com/monitors/notify/#renotify), and test notifications do not trigger automatic investigations.

{% /alert %}

### Supported monitors{% #supported-monitors %}

Bits is able to run investigations on the following monitor types:

- Metric
- Anomaly
- Forecast
- Integration
- Outlier
- Logs
- APM (`APM Metrics` type only; `Trace Analytics` is not supported)
- Synthetics API tests (Preview)

{% callout %}
##### Join the Preview!

Bits AI SRE investigations from Synthetic API tests are now in Preview. Click **Request Access** to join the Preview program.

[Request Access](http://datadoghq.com/product-preview/bits-ai-sre-pilot-features)
{% /callout %}

### Best practices: Add investigation context to your monitors{% #best-practices %}

Think of onboarding Bits as you would a new teammate: the more context you provide, the better it can investigate.

- **Include Datadog telemetry links**: Add at least one helpful telemetry link in the monitor message. Think about the first place you'd normally look in Datadog when this monitor triggers. It could be a link to any of the following:

  - Datadog dashboard
  - Logs
  - Traces
  - Datadog notebook with helpful widgets
  - Confluence runbook page containing Datadog telemetry links (requires a configured [Confluence integration](https://docs.datadoghq.com/bits_ai/bits_ai_sre/configure/#configure-knowledge-base-integrations))

Bits uses these links during the *Runbook* steps of the initial investigation to identify potential problem areas. Because these links are user-defined, you have control over what Bits reviews, ensuring it focuses on the same data you would, and giving you the flexibility to tailor investigations to your team's workflows. You don't have to format the links in any particular way; plain links work.

- **Add service scoping**: For monitors associated with a service, add a service tag to the monitor, or filter or group the monitor query by service.

  {% image
     source="https://datadog-docs.imgix.net/images/bits_ai/optimization_example.c01fa15f4528b26f3910c030de93c9a8.png?auto=format"
     alt="Example monitor with optimization steps applied" /%}

For additional suggestions on how to optimize investigations, see [Help Bits learn](https://docs.datadoghq.com/bits_ai/bits_ai_sre/help_bits_learn/).

## How Bits AI SRE investigates{% #how-bits-ai-sre-investigates %}

Investigations happen in two phases:

1. Bits begins by **gathering initial context** on the problem and any information that might help it troubleshoot further. Depending on the starting point of the investigation, you may see one or more of the following types of step:

   - **Runbook**: If the starting point is a monitor alert, Bits begins by parsing Datadog or Confluence links that you have added to the monitor's message, and uses them as entry points into the investigation.
   - **Memory**: If you have previously interacted with an investigation for the same monitor, Bits recalls any [memories](https://docs.datadoghq.com/bits_ai/bits_ai_sre/help_bits_learn/) associated with the monitor to inform and accelerate the current investigation.
   - **General search**: Bits automatically scans your Datadog environment to gather additional context about what's happening around the alert.
   - **Trace Analysis**: If the starting point is an APM latency graph, Bits automatically inspects anomalous traces to identify the specific services or tags contributing to latency hotspots.

   {% image
      source="https://datadog-docs.imgix.net/images/bits_ai/bits_ai_sre_investigation_context.2727cdee78ee127e5f40e20431595aff.png?auto=format"
      alt="Flowchart showing Bits AI SRE combining runbook, memory, and general search into initial findings" /%}

1. Using the collected context, Bits **builds multiple root cause hypotheses and tests them concurrently**. Bits looks at the following data sources:

   - Metrics
   - Traces
   - Logs
   - Dashboards
   - [Change events](https://docs.datadoghq.com/change_tracking)
   - Kubernetes events

Each hypothesis ends in one of three states: validated, invalidated, or inconclusive. When a hypothesis is validated, Bits generates sub-hypotheses and repeats the same investigative process on them.

   {% image
      source="https://datadog-docs.imgix.net/images/bits_ai/bits_ai_sre_investigation_hypotheses.388a74db896dcfc962a133b702e62bfa.png?auto=format"
      alt="Flowchart showing the hypotheses Bits AI SRE built and tested" /%}

## Reports{% #reports %}

The Reports tab enables you to track the number of investigations run over time by monitor, user, service, and team. You can also track the mean time to initial findings and conclusion to assess the impact of Bits on your on-call efficiency.
