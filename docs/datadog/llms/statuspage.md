# Source: https://docs.datadoghq.com/incident_response/incident_management/integrations/statuspage.md

---
title: Integrate Atlassian Statuspage with Datadog Incident Management
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Incident Response > Incident Management > Incident Integrations >
  Integrate Atlassian Statuspage with Datadog Incident Management
---

# Integrate Atlassian Statuspage with Datadog Incident Management

## Overview{% #overview %}

Atlassian's Statuspage conveys real-time status of an organization's services on a webpage. Enable the integration to automatically link and update your Statuspage incident within Datadog's Incident Management platform. As an Incident Commander or Responder, you can:

- Send customer facing messages with accurate and up to date information
- Update Statuspage while investigating an incident without leaving the Datadog platform
- Resolve both Datadog incidents and the linked Statuspage incident at the same time

## Prerequisites{% #prerequisites %}

Install the integration through the [Statuspage Integration tile](https://app.datadoghq.com/integrations/statuspage). For more information, see the [Statuspage integration](https://docs.datadoghq.com/integrations/statuspage/) documentation.

You must have a role with the Incident Settings Write permission to enable the Atlassian Statuspage integration for Incident Management.

## Setup{% #setup %}

1. In the [Integration Settings page](https://app.datadoghq.com/incidents/settings?section=integrations), find the Atlassian Statuspage integration.
1. Toggle **Enable Atlassian Statuspage incident creation**.

## Add a Statuspage incident{% #add-a-statuspage-incident %}

You must have a role with Incidents Write and Integrations Read permissions to add a Statuspage incident.

1. In the [Incidents page](https://app.datadoghq.com/incidents), open an existing incident.
1. At the top of the incident page, click **Add a Statuspage incident**.
1. Enter all the required fields, which include Select a Statuspage, Incident name, and Incident status. You can also specify which Statuspage components are affected.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/incidents/guide/statuspage/add_update_statuspage_form.b179a8e2b561d48f1ad93d0b00fda531.png?auto=format"
   alt="Form to add or update a Statuspage incident, including required fields for Select a Statuspage, Incident name, and Incident status" /%}

## Update status{% #update-status %}

After a Statuspage is added to an incident, you can continue updating the Statuspage until the incident is resolved.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/incidents/guide/statuspage/update_status_modal.89fee0b03e00396f4fcd9d4075a09a9d.png?auto=format"
   alt="Example incident highlighting the linked statuspage incident and the option to Update Statuspage incident" /%}

1. In the [Incidents page](https://app.datadoghq.com/incidents), open the incident you want to update.
1. Find the Statuspage you added and click the button to open an integration modal. You can unlink the Statuspage integration, change the impact, or update the Statuspage.
1. Click **Update Statuspage** to open the linked Statuspage details and make your modifications.
1. Click **Update** to update the Statuspage incident.

## Further Reading{% #further-reading %}

- [Install the Atlassian Statuspage Integration](https://docs.datadoghq.com/integrations/statuspage/)
- [In-app Statuspage integration tile](https://app.datadoghq.com/integrations/statuspage)
- [Integrating Monitors With Statuspage](https://docs.datadoghq.com/monitors/guide/integrate-monitors-with-statuspage/)
- [Integrate your Synthetic test monitor with Statuspage](https://docs.datadoghq.com/synthetics/guide/synthetic-test-monitors/#integrate-your-synthetic-test-monitor-with-atlassian-statuspage)
