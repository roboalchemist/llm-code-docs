# Source: https://docs.rootly.com/managing-teams/viewing-teams.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Viewing Teams

> View and navigate the teams available in your Rootly organization.

The **Teams** dashboard gives you a centralized view of the teams available in your Rootly organization. From this page, you can see the teams you belong to, review basic team information, and switch between team workspaces.

In Rootly, teams act as separate operational workspaces. Each team maintains its own configuration, users, schedules, alerts, integrations, and incident-related settings. This separation helps organizations keep ownership, response workflows, and configuration clearly scoped to the appropriate team.

If you work across multiple teams, the Teams dashboard makes it easy to move between them and quickly understand which workspace you are currently viewing.

## Open the Teams Dashboard

To open the Teams dashboard:

1. In the Rootly navigation bar, open **Configuration**
2. Select **Teams**

<Frame>
    <img src="https://mintcdn.com/rootly/7ojKISea6oiQMk0o/images/teams/viewing-teams.webp?fit=max&auto=format&n=7ojKISea6oiQMk0o&q=85&s=32e72e720c6da06660ce179cf02ae4b4" alt="Teams dashboard" width="3208" height="1676" data-path="images/teams/viewing-teams.webp" />
</Frame>

Once opened, the page displays the teams you belong to in your current organization.

## Teams Dashboard Overview

The Teams dashboard presents each available team as a separate card, making it easy to scan and navigate your team structure.

Each team card includes:

* **Team name**, which you can click to switch into that team
* **Team member avatars**, showing the first few users in the team
* A **“+ X more”** indicator when additional users belong to the team beyond those shown on the card

This layout is designed to give you a quick, lightweight overview of your available teams without requiring you to open each one individually.

<Callout icon="info" color="#3b82f6">
  If you only belong to one team, Rootly automatically opens that team’s dashboard instead of showing the Teams list first.
</Callout>

## Switching Teams

If you belong to more than one team, you can switch between them directly from the Teams dashboard.

To switch teams:

1. Open the **Teams** dashboard
2. Click the **team name** for the team you want to view

Rootly immediately switches your active workspace to that team and redirects you to the selected team’s dashboard.

This allows you to move between operational contexts without leaving the product or manually reconfiguring your view.

<Callout icon="info" color="#3b82f6">
  Each team has its own incidents, alerts, users, integrations, and configuration settings. When you switch teams, you are changing the active workspace context.
</Callout>

<Callout icon="warning" color="#f59e0b">
  You cannot switch to teams that have been disabled.
</Callout>

## Team Selector

You can also switch teams from the **team selector** in the top-left navigation menu.

The team selector provides a faster way to move between teams without returning to the Teams dashboard. It displays:

* Your **current team**
* Other teams you belong to
* Teams sorted alphabetically for easier navigation

Selecting a team from this menu immediately switches your active workspace.

This is especially helpful for users who frequently work across multiple teams and need a quick way to move between configurations, incidents, and operational responsibilities.

## Why Team Context Matters

Because teams in Rootly operate as separate workspaces, the team you are currently viewing affects the data and settings available to you.

For example, the selected team determines which:

* incidents you see
* users and memberships are active
* schedules and escalation policies are available
* integrations and ownership settings apply

Understanding which team you are currently in is important when reviewing incident data, updating configuration, or making operational changes.

## Related Documentation

<CardGroup cols={2}>
  <Card title="Creating Teams" icon="plus" href="/team-user-management/creating-teams">
    Learn how to create new teams in your organization.
  </Card>

  <Card title="Managing Teams" icon="gear" href="/team-user-management/manage-teams">
    Update team settings, members, and configuration.
  </Card>

  <Card title="Groups" icon="users" href="/team-user-management/groups">
    Organize responders and schedules within a team.
  </Card>

  <Card title="Inviting Users" icon="envelope" href="/team-user-management/inviting-users">
    Add users to your organization.
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).