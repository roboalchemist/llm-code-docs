# Source: https://docs.port.io/solutions/incident-management/detect-and-diagnose-incidents.md

# Detect & diagnose incidents

Modern incident management is broken. Too many tools, too many silos, and not enough context. At Port, we believe incident management should be unified, contextual, and automatedâso teams can focus on resolution, not wrangling alerts.

![](/img/solutions/incident-management/unify_alerts.png)

## Why incident management needs to change[â](#why-incident-management-needs-to-change "Direct link to Why incident management needs to change")

Traditional incident management is reactive and fragmented. Alerts come from everywhere, context is missing, and manual processes slow everything down. This leads to longer outages, frustrated teams, and unhappy users.

## The Port approach: unify, enrich, automate[â](#the-port-approach-unify-enrich-automate "Direct link to The Port approach: unify, enrich, automate")

There's a better way:

1. **Unify Alerts**: Bring all your alerts into a single, actionable stream.
2. **Enrich with Context**: Automatically add relevant metadata, ownership, and dependencies to every incident.
3. **Automate Creation**: Trigger incident workflows, notifications, and remediation stepsâno manual handoffs.

## How to put this into practice[â](#how-to-put-this-into-practice "Direct link to How to put this into practice")

### Unify alerts[â](#unify-alerts "Direct link to Unify alerts")

Connect all your monitoring and alerting tools to Port. Our integrations make it easy to centralize alerts from sources like Datadog, PagerDuty, and more.

* [Prometheus](/build-your-software-catalog/custom-integration/webhook/examples/prometheus.md)
* [Grafana](/build-your-software-catalog/custom-integration/webhook/examples/grafana.md)
* [Datadog Monitors](/build-your-software-catalog/sync-data-to-catalog/apm-alerting/datadog/examples.md)
* [Dynatrace Problems](/build-your-software-catalog/sync-data-to-catalog/apm-alerting/dynatrace/.md)
* [New Relic Issues](/build-your-software-catalog/sync-data-to-catalog/apm-alerting/newrelic/.md)

[Production Readiness Scorecards](https://www.youtube.com/embed/W4kQ8O2w0WA)

### Enrich with context[â](#enrich-with-context "Direct link to Enrich with context")

Context is everything

Teams that have rich context on incidents resolve them up to 40% faster. Make sure your catalog is up to date!

Every alert in Port is automatically enriched with context of all the related data: who owns the service, what dependencies are involved, and recent changes. This means faster diagnosis and fewer escalations.

[Learn how to build your software catalog](/getting-started/overview.md)

## Real-world benefits[â](#real-world-benefits "Direct link to Real-world benefits")

* **Fewer False Positives**: Fewer False Positives - meaning incident teams aren't exhausted from alerts "crying wolf".
* **Better Incident Assignment**: The right people are looped in for an incident, based on context, not just a hardcoded automation rule in your APM tooling.
* **Alert Deduplication**: By grouping alerts by other related data (service, team), we can avoid duplicate incidents for our incoming alerts.
