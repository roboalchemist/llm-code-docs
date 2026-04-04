# Source: https://docs.datadoghq.com/incident_response/incident_management/investigate.md

---
title: Investigate Incidents
description: Manage the context and work for an incident
breadcrumbs: Docs > Incident Response > Incident Management > Investigate Incidents
---

# Investigate Incidents

## Overview{% #overview %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/incidents/investigate/incidents_overview_tab.be98c713078bba11adbf0e3769b54d69.png?auto=format"
   alt="Example incident details view from the Overview tab" /%}

An effective incident investigation starts with identifying and categorizing the incident, followed by comprehensive data collection to construct a detailed timeline of events. The Datadog Incident Details page helps you investigate incidents by providing a centralized platform for real-time monitoring, investigation, remediation, collaboration, and analysis. It includes dynamic dashboards and interactive timelines which assist responders in visualizing incident data and patterns. Use the incident details to:

- Aggregate and display data in real time to help teams identify root causes and assess impacts efficiently.
- Communicate, track progress, and coordinate remediation efforts by using team collaboration features.
- Pivot between various views to explore affected services and dependencies, ensuring a thorough investigation and resolution.

## Incident details{% #incident-details %}

Every incident in Datadog has its own Incident Details page where you can manage property fields, signals, tasks, documents, responders, and notifications. The Incident Details page contains a global header for quick access to key actions. The remainder of the page is divided into tabbed sections which group related incident data together.

### Global header{% #global-header %}

The global header provides access to the [Status and Severity](https://docs.datadoghq.com/incident_response/incident_management/describe/#incident-details) selectors and links to your [Incident Integrations](https://docs.datadoghq.com/incident_response/incident_management/#integrations). For more information on how to configure automatic Slack and Microsoft Teams links for every new incident, see the [Incident Settings](https://docs.datadoghq.com/incident_response/incident_management/incident_settings#integrations) documentation.

After an incident is resolved, an option appears in the header to generate a postmortem Notebook using a [postmortem template](https://docs.datadoghq.com/incident_response/incident_management/incident_settings/templates#postmortems). To configure your postmortem templates in the app, navigate to the [Incident Settings](https://app.datadoghq.com/incidents/settings#Postmortems) page and define the structure and content of your postmortems.

### Overview tab{% #overview-tab %}

The Overview tab serves as the main page to view an incident's properties and define customer impact. By default, it includes properties such as Root Cause, Services, Teams, Detection Method, and Summary. These properties are categorized into the What Happened, Why it Happened, and Attributes sections.

Add more property fields using `<KEY>:<VALUE>` pairs from Datadog metric tags, or create custom fields through [Incident Settings](https://docs.datadoghq.com/incident_response/incident_management/incident_settings/property_fields). Assign values to these properties to improve searches and queries in the Incident Homepage and Incident Management Analytics. To prioritize critical information, you can reorder property fields and move them under various headings.

For customer-facing incidents, specify impact details by adding them in the **Impacts** section:

{% image
   source="https://datadog-docs.imgix.net/images/service_management/incidents/investigate/incident_details_impacts.4d3c7dcfe97c1d806f3ae663e908c87e.png?auto=format"
   alt="Your image description" /%}

1. Click **Add**.
1. Specify a start date and time for the impact.
1. Specify an end date and time for the impact or leave blank if the impact is still ongoing.
1. Describe the nature of the impact on customers in `Scope of impact`.
1. Click **Save**.

In addition to housing your property fields, the Overview tab also provides the following at-a-glance summary modules:

| Summary Module          | Description                                                                                                                                                                                                                                                      |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Condensed Timeline      | Displays the timestamps when incident status changes occurred, as well as when impact started and ended. This provides a high-level view of the incident's lifecycle.                                                                                            |
| Latest Notifications    | Displays the most recent notification sent for the incident, with quick access to the full list of notifications in the [Notification tab](https://docs.datadoghq.com/incident_response/incident_management/notification/).                                      |
| Pending Tasks           | Displays the most recent incomplete task, with quick access to the full list of tasks in the Remediation tab.                                                                                                                                                    |
| Responders              | Displays the current incident commander as well as avatars for the remaining responders assigned to the incident.                                                                                                                                                |
| Recent Timeline Entries | Displays the five most recent entries in the incident timeline, with quick access to see the entire Timeline tab. For more information, see the [Timeline](https://docs.datadoghq.com/incident_response/incident_management/investigate/timeline) documentation. |

## Additional investigation tools{% #additional-investigation-tools %}

After declaring an incident, responders can use the Incident Details Page to apply available information so that they can describe and analyze the incident thoroughly.

- [**Timeline**: Track the sequence of events leading to and during the incident. Use visualizations and time-based data to understand the chronology and impact of events.](https://docs.datadoghq.com/incident_response/incident_management/investigate/timeline)

## Further Reading{% #further-reading %}

- [Declare an Incident](https://docs.datadoghq.com/incident_response/incident_management/declare)
- [Describe an Incident](https://docs.datadoghq.com/incident_response/incident_management/describe)
