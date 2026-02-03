# Source: https://docs.datadoghq.com/incident_response/incident_management/describe.md

---
title: Describe an Incident
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Incident Response > Incident Management > Describe an Incident
---

# Describe an Incident

## Overview{% #overview %}

No matter where you [declare an incident](https://docs.datadoghq.com/incident_response/incident_management/declare), it's important to describe it as thoroughly as possible to share the information with other people involved in your organization's incident management process. The incident details should give information on:

- What happened
- Why it happened
- Attributes associated with the incident

## Incident details{% #incident-details %}

An incident's status and details can be updated on the incident's Overview tab. Within an incident, fill out the Overview tab with relevant detailsâincluding incident summary, customer impact, affected services, incident responders, root cause, detection method, and severityâto give your teams all the information they need to investigate and resolve an incident.

Update the impact section to record customer impacts, including their start and end times. These impacts influence incident analytics to help your organization analyze the impact of incidents on your business.

You can define your own custom incident fields on the [Incident Settings Property Fields](https://app.datadoghq.com/incidents/settings#Property-Fields) page.

### Status levels{% #status-levels %}

The default statuses are **Active**, **Stable**, and **Resolved**. You can add the **Completed** status and customize the description of each status level in the Incident Settings page.

- Active: Incident affecting others.
- Stable: Incident no longer affecting others, but investigations incomplete.
- Resolved: Incident no longer affecting others and investigations complete.
- Completed: All remediation complete.

## Further reading{% #further-reading %}

- [Customize incidents in Incident Settings](https://docs.datadoghq.com/incident_response/incident_management/incident_settings)
- [Configure Incident Notifications](https://docs.datadoghq.com/incident_response/incident_management/notification)
