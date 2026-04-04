# Source: https://docs.datadoghq.com/incident_response/incident_management/incident_settings/information.md

---
title: Information
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Incident Response > Incident Management > Incident Settings >
  Information
---

# Information

## Overview{% #overview %}

From the [Incident Settings Information](https://app.datadoghq.com/incidents/settings#Information) page, you can customize the statuses and severities of your incidents and enable core incident capabilities, such as private incidents, test incidents, and timestamp overrides.

## Severity levels{% #severity-levels %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/incidents/incident_settings/settings_info_severity_levels.cb7d570f3965393617cf5b5e39403768.png?auto=format"
   alt="Customizable severity levels in incident settings" /%}

Use severity level settings to:

1. Define your most critical severity as `SEV-0` or `SEV-1` (defaults to `SEV-1`)
1. Customize the sub-labels of your severities (**Defaults:** Critical, High, Moderate, Low, Minor)
1. Customize the descriptions of your severities
1. Add or delete severities from the bottom of your list, with a minimum of one and a maximum of ten
1. Enable the "Unknown" severity

**Note**: If you attempt to delete a severity that is referenced in a [notification rule](https://docs.datadoghq.com/incident_response/incident_management/incident_settings/notification_rules), you are prompted to confirm your decision. Choosing to proceed disables the impacted notification rules as they are no longer valid. Deleting a severity or changing the starting severity does not automatically update any [Incident Management Analytics](https://docs.datadoghq.com/incident_response/incident_management/analytics) queries.

## Status levels{% #status-levels %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/incidents/incident_settings/settings_info_status_levels.603d9b135d690a06762e1bddaa2cf17a.png?auto=format"
   alt="Customizable status levels in incident settings" /%}

Use status level settings to:

1. Customize the descriptions of the statuses
1. Enable the optional `Completed` status

**Note**: Deleting the `Completed` status does not automatically update incidents in the `Completed` status and does not automatically update any [Incident Management Analytics](https://docs.datadoghq.com/incident_response/incident_management/analytics) query that explicitly references it. Any notification rule that references the `Completed` status becomes disabled.

## Helper text{% #helper-text %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/incidents/incident_settings/settings_info_helper_text.28f104109573573d43d368ef58903266.png?auto=format"
   alt="Declare Incident Helper Text Settings" /%}

Helper text appears alongside the [Incident Creation Modal](https://docs.datadoghq.com/incident_response/incident_management/#from-the-incidents-page) and helps your responders understand how they should define the incident.

You can use markdown in helper text to add indented lists, formatted text, and hyperlinks to other resources.

## Private incidents (incident visibility){% #private-incidents-incident-visibility %}

*Default: disabled*

An incident's **visibility** determines what users in your Datadog organization can see it. If an incident's visibility is **organization**, any user with the **Incidents Read** permission can see it. If the incident's visibility is **private**, only the incident's responders or users with the **Private Incidents Global Access** permission can see it.

On the [Datadog Incidents page](https://app.datadoghq.com/incidents), you can search for private incidents using the **Visibility** facet on the left. You can also add conditions around incident visibility when defining incident [notification rules](https://docs.datadoghq.com/incident_response/incident_management/incident_settings/notification_rules).

### Private incidents in Slack{% #private-incidents-in-slack %}

When you declare private incidents, Datadog creates private Slack channels instead of public channels.

If you convert an incident to private, Datadog archives the existing incident channel, creates a new private channel, and adds all existing responders to it.

To convert an incident to private in Slack, use `/datadog incident private`.

## Incident deletion{% #incident-deletion %}

*Default: disabled*

When incident deletion is enabled for an incident type, any user with the **Incidents Write** permission can delete any incident of the incident type.

After you delete an incident, it no longer influences incident analytics, and no user can access it. Deleted incidents cannot be recovered.

## Override status timestamps{% #override-status-timestamps %}

*Default: disabled*

When timestamp overrides are enabled in an incident type, any user with the **Incidents Write** permission can define timestamp overrides in any incident of that incident type.

When enabled, you can define overrides for the `declared`, `detected`, and `resolved` timestamps on an incident. To learn more, see [Incident Analytics](https://docs.datadoghq.com/incident_response/incident_management/analytics).

## Test incidents{% #test-incidents %}

*Default: disabled*

When test incidents are enabled in an incident type, any user with the **Incidents Write** permission can declare test incidents of the incident type.

Test incidents are visually distinguished by a purple banner. By default, test incidents do not by appear in incident search, execute automations, execute notification rules, or affect analytics. The declarer can opt into these functions during declaration.
