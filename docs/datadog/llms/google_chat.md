# Source: https://docs.datadoghq.com/incident_response/incident_management/integrations/google_chat.md

---
title: Integrate Google Chat with Datadog Incident Management
description: Manage Datadog incidents directly from Google Chat.
breadcrumbs: >-
  Docs > Incident Response > Incident Management > Incident Integrations >
  Integrate Google Chat with Datadog Incident Management
---

# Integrate Google Chat with Datadog Incident Management

## Overview{% #overview %}

The Google Chat integration for Datadog Incident Management connects your incident response workflows directly to Google Chat. When your team declares a Datadog incident, the integration automatically creates a Google Chat space for collaboration.

## Prerequisites{% #prerequisites %}

Install the integration through the [Google Chat Integration tile](https://app.datadoghq.com/integrations/google-hangouts-chat). A Google Workspace administrator must configure delegated user permissions and set up a target audience and add that to the integration tile. For more information, see the [Google Chat integration](https://docs.datadoghq.com/integrations/google-hangouts-chat/) documentation.

## Incident Spaces{% #incident-spaces %}

You can configure Incident Management to automatically create a dedicated Google space for each incident that meets the criteria you define. Your responders can then manage the incident directly in Google Chat from the incident space.

To use incident spaces:

1. In Datadog, go to **[Incident Response > Incident Management > Settings > Integrations > Google Chat](https://app.datadoghq.com/incidents/settings?section=integrations)** and enable **Automatically create Google Chat spaces for incidents**.

1. Select an **Organization** from the dropdown. If you don't see any options, reach out to your Google Workspace administrator to connect your Google organization to Datadog.

1. Select a **Target Audience** from the dropdown. **Default** is the default target audience set by your Google Workspace administrator, which could be a private or public target audience group. Reach out to your Google Workspace administrator if this is unclear.

1. The **Channel Name Template** you define determines how Datadog names the incident spaces it creates. The following variables are available in channel name templates:

   - `{{public_id}}`: Incident's numeric ID
   - `{{title}}`: Incident's title
   - `{{created}}`: Incident's creation date in format `MM_DD_YYYY`
   - `{{yyyy}}`: Incident's four-digit creation year
   - `{{mm}}`: Incident's two-digit creation month
   - `{{dd}}`: Incident's two-digit creation day of month
   - `{{severity}}`: Incident's severity
   - `{{random_adjective}}`: Random adjective
   - `{{random_noun}}`: Random noun
   - `{{slug}}`: Slug (when slug source is set to `servicenow`, this will display the ServiceNow record number)

## Further reading{% #further-reading %}

- [Incident Integrations Settings](https://docs.datadoghq.com/incident_response/incident_management/incident_settings/integrations)
- [Google Chat Integration](https://docs.datadoghq.com/integrations/google-hangouts-chat)
