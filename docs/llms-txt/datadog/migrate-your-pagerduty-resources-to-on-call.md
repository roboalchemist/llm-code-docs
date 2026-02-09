# Source: https://docs.datadoghq.com/incident_response/on-call/guides/migrate-your-pagerduty-resources-to-on-call.md

---
title: Migrate PagerDuty resources to Datadog On-Call
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Incident Response > On-Call > On-Call Guides > Migrate PagerDuty
  resources to Datadog On-Call
---

# Migrate PagerDuty resources to Datadog On-Call

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Follow this migration workflow to rebuild your PagerDuty on-call structure in Datadog, team by team. It reuses your existing PagerDuty schedules and escalation policies as building blocks so you can review, tweak, or discard each resource before it goes live.

By rebuilding your onâcall setup from only current, relevant PagerDuty data, you avoid bringing legacy clutter into Datadog and start with a concise, maintainable configuration.

## Prerequisites{% #prerequisites %}

1. Configure the [PagerDuty integration](https://app.datadoghq.com/integrations/pagerduty) in Datadog.
1. Create a PagerDuty API key, if you don't have one already, that can read PagerDuty assets like schedules, escalation policies, and teams.
1. Confirm your user has `on_call_write` and `teams_manage` permissions.

## Migration steps{% #migration-steps %}

### Select team to migrate{% #select-team-to-migrate %}

1. Visit the [On-Call Teams list](https://app.datadoghq.com/on-call/teams) and select **Add Team to OnâCall** > **Import team from PagerDuty**. Datadog loads all your teams from PagerDuty.
1. Pick the team to migrate and choose **Next**. A preview pane shows the team's members and settings.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/oncall/pagerduty_migration_import_team.52e38ff2bdab78438caeb4105446f411.png?auto=format"
   alt="UI that lists PagerDuty teams and shows a preview of the selected team" /%}

### Map the team and its members{% #map-the-team-and-its-members %}

1. Select one of the following options:

   - **Map with another Datadog team**: Choose the appropriate Datadog team from the list.

   - **Create a new team**: Enter a team name when prompted. Datadog builds the team using the structure and members from your PagerDuty team.

   {% image
      source="https://datadog-docs.imgix.net/images/service_management/oncall/pagerduty_migration_map_users.77551e0b0c4bcc2a3d0f7ad807e3926e.png?auto=format"
      alt="UI for mapping PagerDuty users to Datadog users or inviting new users" /%}

1. Handle unmapped users:

Datadog matches users by email address. For unmapped users you can:

   - Invite them to Datadog (the UI sends an email invitation), or
   - Skip them if they no longer need access.

1. When the mapping looks correct, select **Import team**.

### Configure routing rules{% #configure-routing-rules %}

Choose a template to define how alerts reach the team:

- **All alerts to escalation policy**: forward every alert to a designated escalation policy.
- **Business hours**: send alerts to the team only during specified hours and use chat channels as fallbacks.
- **Alert priority**: route alerts based on their priority and impact.
- **Start from scratch**: customize routing rules to fit your team's workflows.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/oncall/pagerduty_migration_select_routing_rule_template.6dc8a4a51290d00b4bbd5f9653da5a94.png?auto=format"
   alt="UI with routingârule templates such as 'All alerts to escalation policy', 'Business hours', and 'Alert priority'" /%}

### Reuse escalation policies and schedules{% #reuse-escalation-policies-and-schedules %}

When you edit routing rules, you can import existing PagerDuty escalation policies and schedules instead of recreating them.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/oncall/pagerduty_migration_migrate_escalation_policies_and_schedules.86c1abe4c88a6087f1f7c321001ae613.png?auto=format"
   alt="UI for selecting existing PagerDuty escalation policies and schedules" /%}

Datadog will automatically apply the imported configurations. You can change the policies and schedules at any time.

## Further reading{% #further-reading %}

- [On-Call Documentation](https://docs.datadoghq.com/incident_response/on-call/)
- [PagerDuty Integration](https://docs.datadoghq.com/integrations/pagerduty/)
