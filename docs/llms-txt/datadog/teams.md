# Source: https://docs.datadoghq.com/cloudcraft/api/teams.md

# Source: https://docs.datadoghq.com/account_management/teams.md

---
title: Teams
description: >-
  Organize team assets, filter Datadog experiences, and manage team membership
  with team handles, notifications, and resource associations.
breadcrumbs: Docs > Account Management > Teams
source_url: https://docs.datadoghq.com/teams/index.html
---

# Teams

## Overview{% #overview %}

Datadog Teams allow groups of users to organize their team assets within Datadog and automatically filter their Datadog-wide experience to prioritize these assets.

Use Teams to link resources such as dashboards, services, monitors, and incidents to a group of users. You can also add team-specific links to Slack channels, Jira boards, GitHub repositories, and more.

Team membership is flexible. Users can join teams, be added by other members, or be added by an administrator. Users can belong to multiple teams.

## Setup{% #setup %}

### Navigation{% #navigation %}

Access the team directory page from [Organization Settings](https://app.datadoghq.com/organization-settings/teams) or by navigating to [**Teams**](https://app.datadoghq.com/teams). The [team directory page](https://app.datadoghq.com/organization-settings/teams) lists all teams within your organization.

### Create team{% #create-team %}

1. On the [team directory page](https://app.datadoghq.com/organization-settings/teams), click **New Team** at the upper right.
1. Choose a **Team Name**.
1. The **Handle** populates based on your team name.
1. Use the dropdown menu to select team members and team managers.
1. Provide an optional **Description**.
1. Click **Create**.

**Notes**:

- Allowed characters for team names are `a-z`, `A-Z`, `0-9`, and `._-:/`. Replace spaces with underscores.
- Allowed characters for team handles are `a-z`, `0-9`, and `._-:/`. The last character cannot be an underscore.

### Modify team{% #modify-team %}

1. On the [team directory page](https://app.datadoghq.com/organization-settings/teams), click the team you wish to modify. The [team detail page](https://docs.datadoghq.com/account_management/teams/manage/) appears.
1. Click the **Settings** cog at the top of the screen. A pop-up window appears.
1. Select the item you wish to modify.
1. Make your changes, then click **Save**.

### Choose provisioning source{% #choose-provisioning-source %}

Choose from three options to determine how admins and team managers may update team membership:

{% dl %}

{% dt %}
UI and API
{% /dt %}

{% dd %}
Update membership through UI actions and API calls only
{% /dd %}

{% dt %}
SAML
{% /dt %}

{% dd %}
Use a *SAML strict* model so the identity provider data determines team membership
{% /dd %}

{% dt %}
All sources
{% /dt %}

{% dd %}
Use SAML as a starting point, and allow overrides through the UI and API
{% /dd %}

{% /dl %}

1. On the [team directory page](https://app.datadoghq.com/organization-settings/teams), click **Teams Settings**.
1. Select one of the options under **Team Provisioning Sources**.

If you have teams with existing members, picking the SAML strict option overrides your settings and removes team members from those teams. Picking the All Sources option preserves existing memberships. To manage teams and team membership using SAML attributes, see [Map SAML attributes to Teams](https://docs.datadoghq.com/account_management/saml/mapping/#map-saml-attributes-to-teams).

## Team handle{% #team-handle %}

A team handle links teams to Datadog resources. Team handles appear in search bars and facets in the format `team:<team-handle>` or `teams:<team-handle>`.

To find a team handle:

1. Click the team's name in the team directory page. The team detail page appears.
1. The team handle appears to the right of the name, at the top of the page.

To associate a resource with a defined team, a Team must exist in Datadog with a matching team handle. When you click on a resource associated with a defined team, a small window appears with the team handle and additional information. Defined teams provide additional functionality such as the Team filter below.

Team handles that aren't associated with a defined team in Datadog behave similarly to tags. Convert any undefined team handles to defined teams to take advantage of Teams features.

### Associate resources with team handles{% #associate-resources-with-team-handles %}

Datadog supports associating the following resources with team handles:

- [Dashboards](https://docs.datadoghq.com/dashboards/#dashboard-details)
- [Incidents](https://docs.datadoghq.com/incident_response/incident_management/)
- [Monitors](https://docs.datadoghq.com/monitors/configuration/?tab=thresholdalert#add-metadata)
- [Resource Catalog](https://docs.datadoghq.com/infrastructure/resource_catalog/)
- [Software Catalog](https://docs.datadoghq.com/tracing/software_catalog/adding_metadata/#add-metadata-from-the-datadog-ui)
- [Service Level Objectives](https://docs.datadoghq.com/service_level_objectives/#slo-tags)
- Synthetic Tests, Global Variables, Private Locations

### Send notifications to a specific communication channel{% #send-notifications-to-a-specific-communication-channel %}

Add a notification channel to your Team to route alerts to communication channels such as Slack or Microsoft Teams. Monitor alerts targeting `@team-<handle>` are redirected to the selected channel.

1. On the [team directory page](https://app.datadoghq.com/organization-settings/teams), click the team you wish to modify.
1. Click the **Settings** cog at the top of the screen. A pop-up window appears.
1. Select **Notifications**.
1. Add a channel, then click **Save**.

## Team filter{% #team-filter %}

The team filter tailors your experience across Datadog by showing you content associated with your teams. The **My Teams** list includes teams you are a member of and teams you selected as a favorite.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/teams/team-filter.63865696b308faae72de4632479a5b4c.png?auto=format"
   alt="Monitor list page with red box around the team filter. Two out of three My Teams selected." /%}

When you enable the team filter, you see only the resources associated with your teams or with the services owned by your teams. The team filter state is global and persistent, so Datadog applies your team context as you navigate across different products.

The team filter works by adding team-based search terms to the search query. When you enable the team filter, you can see the team-based search terms it adds in the search bar.

### Favorite teams{% #favorite-teams %}

You may be interested in a particular team's resources without being a member of that team. Adding a team to your favorite teams allows you to get filtered views on that team's resources without joining the team.

Your favorite teams appear alongside teams you belong to at the top of the team directory page and in the team filter.

#### Add or remove favorite teams{% #add-or-remove-favorite-teams %}

You can add or remove a team from your favorites from the team directory page or from the team filter.

From the [team directory page](https://app.datadoghq.com/organization-settings/teams):

1. Click the team you wish to add as a favorite. The [team detail page](https://docs.datadoghq.com/account_management/teams/manage/) appears.
1. Click **Add Favorite** or **Remove Favorite** in the upper right.

Alternatively, also from the team directory page:

1. Hover over the team you wish to add or remove. Inline icons appear to the right of the team name.
1. Click the star (**Add to Favorites** or **Remove from Favorites**) icon.

From the team filter:

1. If the filter is collapsed, click **My Teams** to expand it.
1. Click **Add Favorites**. A search box and list of teams appear.
1. To narrow the list of teams, start typing a team name in the search box.
1. Click the star next to the desired team to add or remove it from your favorites.

### Supported products{% #supported-products %}

The following table describes the products in which you can use the team filter:

| Product List Page                                                               | Filter basis                                                                                                       |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| [Dashboards](https://app.datadoghq.com/dashboard/lists)                         | Team handle                                                                                                        |
| [Resource Catalog](https://docs.datadoghq.com/infrastructure/resource_catalog/) | Team handle                                                                                                        |
| [Software Catalog](https://app.datadoghq.com/services)                          | Team handle                                                                                                        |
| [Incidents](https://app.datadoghq.com/incidents)                                | Team handle                                                                                                        |
| [Monitors](https://app.datadoghq.com/monitors/manage)                           | Team handle                                                                                                        |
| [APM Error Tracking](https://app.datadoghq.com/apm/error-tracking)              | Service owned by teams (determined by ownership inside the [Software Catalog](https://app.datadoghq.com/services)) |
| [Logs Error Tracking](https://app.datadoghq.com/logs/error-tracking)            | Service owned by teams (determined by ownership inside the [Software Catalog](https://app.datadoghq.com/services)) |
| [Service Level Objectives](https://app.datadoghq.com/slo/manage)                | Team handle                                                                                                        |
| [Data Streams Monitoring](https://app.datadoghq.com/data-streams)               | Team handle                                                                                                        |
| [Synthetic Tests](https://app.datadoghq.com/synthetics)                         | Team handle                                                                                                        |
| [Notebooks](https://app.datadoghq.com/notebook/list/)                           | Team handle                                                                                                        |

## Permissions{% #permissions %}

Any user in a role with the Teams Manage permission can create teams, rename teams, delete teams, and change team handles. Users with `user_access_manage` can add, remove, and promote team members and managers.

## Manage teams{% #manage-teams %}

To customize your team, see [Team Management](https://docs.datadoghq.com/account_management/teams/manage/).
