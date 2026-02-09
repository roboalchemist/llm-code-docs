# Source: https://docs.datadoghq.com/security/cloud_siem/triage_and_investigate/entities_and_risk_scoring.md

---
title: Risk Insights
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Cloud SIEM > Triage and Investigate > Risk Insights
---

# Risk Insights

## Overview{% #overview %}

[Cloud SIEM's Risk Insights](https://app.datadoghq.com/security/siem/risk-insights) consolidates multiple data sources, such as SIEM threats and Cloud Security insights, into a profile representing a single security entity, such as an IAM user.

With Risk Insights, you can:

- Explore entities, filtering them by attributes such as risk score severity and configuration risks.
- View all data relevant to an entity, such as signals, misconfigurations, and identity risks.
- Configure notifications so you can address risky entities as they emerge.
- Triage relevant items in bulk.
- Take mitigation steps such as creating a global suppression or creating a case for an entity.

## Prerequisites{% #prerequisites %}

- For Risk Insights coverage, either GitHub, [Azure](https://docs.datadoghq.com/security/cloud_siem/guide/azure-config-guide-for-cloud-siem/), [GCP](https://docs.datadoghq.com/security/cloud_siem/guide/google-cloud-config-guide-for-cloud-siem/), or [AWS](https://docs.datadoghq.com/security/cloud_siem/guide/aws-config-guide-for-cloud-siem/) must be configured for Cloud SIEM.
- (Optional) To view associated Cloud Security insights in the entity panel, [Cloud Security must be configured](https://docs.datadoghq.com/security/cloud_security_management/setup).

## Explore risk insights{% #explore-risk-insights %}

### Query and filter entities{% #query-and-filter-entities %}

On the [Risk Insights Explorer](https://app.datadoghq.com/security/siem/risk-insights), you can view all entities that have a non-zero risk score associated to them.

{% image
   source="https://datadog-docs.imgix.net/images/security/entities/entities-explorer3.81cd665f1f8dedd5f3184334128b8c13.png?auto=format"
   alt="A list of entities and their risk scores in the Risk Insights Explorer" /%}

### Quickly build context on an entity{% #quickly-build-context-on-an-entity %}

Click an entity in the [Explorer](https://app.datadoghq.com/security/siem/risk-insights) to open the entity side panel.

{% image
   source="https://datadog-docs.imgix.net/images/security/entities/entity-side-panel3.d3935b8af60559b3d532268d5ed3a7f2.png?auto=format"
   alt="The side panel for an entity" /%}

The **What Happened** section of the panel summarizes the count of signals, misconfigurations, and identity risks and how they have contributed to the risk score, as well as any potential configuration risks.

The **What contributes to the score** section displays the list of fired signals, relevant misconfigurations, and identity risks.

### Triage and mitigate threats in bulk{% #triage-and-mitigate-threats-in-bulk %}

The **Next steps** section of the entity side panel includes the available mitigation steps for SIEM signals, misconfigurations, and identity risks.

{% image
   source="https://datadog-docs.imgix.net/images/security/entities/entities-next-steps2.a96a8635630f6bf3ff443dcea71b1992.png?auto=format"
   alt="The available next steps for an entity as shown in the entity side panel" /%}

## Configure notifications for Risk Insights{% #configure-notifications-for-risk-insights %}

You can configure Datadog to send you notifications as soon as it detects new threats that match your criteria.

1. Navigate to the **Create a new Risk Insight notification** page. There are two ways to do this:
   - In Datadog, go to the [Risk Insights Explorer](https://app.datadoghq.com/security/siem/risk-insights), then click **Create Notification Rule**.
   - In Datadog, go to **Cloud SIEM** > [**Settings**](https://app.datadoghq.com/security/configuration/siem/risk-insights). Under **Products**, in the **Cloud SIEM** section, click **Risk Insights**; then, under **Notification rules**, click **New notification rule**.
1. Under **Define entity attributes**, specify the attributes that should trigger notifications when Datadog detects them on an entity. Beside **Entities matching**, start typing entity attributes and values. As you type, the preview table dynamically displays risk insights that match your criteria.Important alert (level: info): This step is optional, but if you don't enter any attributes, the notification defaults to sending alerts for all entities.
1. Under **Set notification conditions**, specify the risk score threshold to trigger notifications for.
1. Under **Configure notification**, enter a name for the notification, and recipients to send it to.
   - Optionally, you can also turn on re-notifications, and specify the period of time that should pass before Datadog re-notifies the recipients that the risk insight still meets the criteria you specified.

## Risk scoring{% #risk-scoring %}

An entity's risk score approximates the entity's risk level over the past 14 days of activity.

The risk score is calculated from the characteristics of the entity's associated signals, such as the severity level of the signal and how many times the signal has fired.

### Signal's score impact{% #signals-score-impact %}

Each signal has a score impact. You can see a signal's score impact in the entity panel.

**Note**: A signal's score impact lasts for 2 weeks, after which the score drops to `0`.

| Signal Severity  | Number of points |
| ---------------- | ---------------- |
| `Critical`       | `100`            |
| `High`           | `50`             |
| `Medium`         | `5`              |
| `Low` and `Info` | `0`              |

### Entity's severity threshold{% #entitys-severity-threshold %}

The severity threshold of an entity is calculated by adding up the score impact for all signals associated with the entity.

| Entity's Severity Threshold | Sum of the score impact for all related signals    |
| --------------------------- | -------------------------------------------------- |
| `Critical`                  | Greater than or equal to `100`.                    |
| `High`                      | Greater than or equal to `50` and less than `100`. |
| `Medium`                    | Greater than or equal to `25` and less than `50`.  |
| `Low`                       | Greater than or equal to `10` and less than `25`.  |
| `Info`                      | Less than `10`.                                    |

## Further reading{% #further-reading %}

- [Accelerate investigations with Datadog Cloud SIEM Risk-based Insights and AWS Entity Analytics](https://www.datadoghq.com/blog/risk-prioritization-entity-analytics/)
