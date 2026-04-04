# Source: https://docs.datadoghq.com/security/cloud_siem/respond_and_report.md

---
title: Respond (SOAR) and Report
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Cloud SIEM > Respond (SOAR) and Report
---

# Respond (SOAR) and Report

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



{% alert level="danger" %}
Workflow Automation is not available in the selected site ().
{% /alert %}


{% /callout %}

## Overview{% #overview %}

Datadog Security Orchestration, Automation, and Response (SOAR) helps you orchestrate security operations, investigate signals, and remediate threats using [Workflow Automation](https://docs.datadoghq.com/actions/workflows/). For example, you can [run a workflow](https://docs.datadoghq.com/security/cloud_siem/investigate_security_signals#run-workflow-automation) to:

- Block an IP address from your environment.
- Disable a user account.
- Look up an IP address with a third-party threat intelligence provider.
- Send Slack messages to your colleagues to get help with your investigation.
- Assign signals for investigation.
- Automatically enrich cases and close duplicate cases.

SOAR also includes ready-to-use customizable [blueprints](https://docs.datadoghq.com/actions/workflows/build/#build-a-workflow-from-a-blueprint) to help you build workflows for remediating threats. For example:

- An Identity and Access Management (IAM) workflow that automates responses to suspicious logins and account compromises.
- An Endpoint Detection and Response (EDR) workflow that speeds up the investigation and containment of endpoint threats.
- A Threat Intelligence Enrichment workflow that enriches alerts with external data so you can prioritize and respond more effectively.

Cloud SIEM also provides [security operational metrics](https://docs.datadoghq.com/security/cloud_siem/security_operational_metrics/), so you can determine the efficiency and effectiveness of your security processes.

## Further reading{% #further-reading %}

- [Automate identity protection, threat containment, and threat intelligence with Datadog SOAR workflows](https://www.datadoghq.com/blog/soar/)
- [Measure and optimize security team efficiency with Cloud SIEM security operational metrics](https://www.datadoghq.com/blog/security-operational-metrics/)
