# Source: https://docs.rootly.com/managing-teams/managing-teams.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Create and manage teams in Rootly to organize on-call schedules, route alerts, configure Slack automation, and import team structures from PagerDuty or Opsgenie.

In Rootly, **Teams** represent groups of users responsible for a specific department, service, or product within your organization. Teams provide the organizational structure used to manage on-call coverage, route alerts, and configure team-specific workflows across the platform.

## What Teams Can Do

Teams in Rootly enable you to:

* **Own On-Call Schedules and Escalation Policies**\
  Teams manage their own on-call rotations and escalation policies through Rootly On-Call.

* **Route Alerts to the Right Responders**\
  Alerts from integrated monitoring tools or email sources can be routed directly to teams to ensure the correct responders are notified immediately.

* **Configure Slack Automation**\
  Teams can be mapped to specific Slack channels and user groups, enabling automated notifications, incident collaboration, and response workflows.

## Managing Teams

Teams can be created and managed directly in the Rootly web interface, where you can assign members, configure team settings, and manage access.

Rootly also supports importing teams from third-party platforms to simplify migrations and maintain existing team structures.

### Supported Imports

* **PagerDuty**
* **Opsgenie**

Additional integrations and migration options will continue to be added.

<Frame>
    <img src="https://mintcdn.com/rootly/JFQ1ZeVNi4nNRKF5/images/user-management/manage-teams.webp?fit=max&auto=format&n=JFQ1ZeVNi4nNRKF5&q=85&s=33b97eb67035acd40be7678464fa4c6d" alt="Document image" width="2174" height="1476" data-path="images/user-management/manage-teams.webp" />
</Frame>

## Frequently Asked Questions

### Team Membership

<AccordionGroup>
  <Accordion title="Can users belong to multiple teams?" icon="users">
    Yes. Users can belong to multiple teams in Rootly.

    Each team membership has its own:

    * **Role** (Owner, Admin, Member, etc.)
    * **On-Call Role**
    * **Permissions**

    Users can switch teams using the **team selector** in the navigation bar.

    <Callout icon="info" color="#3b82f6">
      **Team Switching:** When users switch teams, they only see the data, incidents, and configurations for that team.
    </Callout>
  </Accordion>

  <Accordion title="How do permissions work across teams?" icon="shield-check">
    Permissions in Rootly are **team-scoped**.

    This means:

    * Roles apply only within a specific team
    * Permissions in one team do not affect another
    * Users can have different roles across teams

    Example: A user could be an **Owner** in Engineering but a **Member** in Operations.
  </Accordion>

  <Accordion title="How do I manage team members?" icon="user-cog">
    Team members can be managed through:

    * **Web UI:** Settings → Teams → Members
    * **Email Invitations**
    * **SCIM provisioning** when SSO is enabled
    * **API** for programmatic management
  </Accordion>

  <Accordion title="Can I restrict access by email domain?" icon="mail">
    Yes. Teams can restrict membership to specific **email domains**.

    To configure this:

    1. Navigate to **Settings → Team Settings**
    2. Configure the **Email Domains** restriction
    3. Only users with matching domains can be added
  </Accordion>
</AccordionGroup>

***

### Teams & Organizational Structure

<AccordionGroup>
  <Accordion title="What's the difference between Teams and Groups?" icon="layers">
    **Teams** are top-level organizational units that contain users, schedules, alerts, and configurations.

    **Groups** are sub-units within a team used for:

    * On-call rotations
    * Alert routing
    * Incident assignment
    * Slack channel mapping

    Think of it as:

    **Teams = organizations**\
    **Groups = sub-teams within that organization**
  </Accordion>

  <Accordion title="Can teams share resources or data?" icon="database">
    No. Teams are **fully isolated**.

    Each team has its own:

    * Incident data
    * Alerts and action items
    * Configuration settings
    * On-call schedules
    * Alert routing rules

    Users must be explicitly added to each team to access it.
  </Accordion>

  <Accordion title="Can teams have different configurations?" icon="sliders">
    Yes. Each team can configure its own settings including:

    * AI features
    * Alert routing
    * Incident workflows
    * Sub-statuses
    * Retrospective templates
    * Integrations
    * Time zones

    This allows teams to operate independently.
  </Accordion>

  <Accordion title="What's the difference between a team and an escalation policy?" icon="alarm">
    A **Team** is the organizational container that includes users, schedules, and configuration.

    An **Escalation Policy** defines **how alerts notify responders within that team**, including:

    * Who gets notified
    * Escalation order
    * Notification timing
    * Notification methods
  </Accordion>
</AccordionGroup>

***

### Team Management

<AccordionGroup>
  <Accordion title="Can I change a team's name or settings later?" icon="edit">
    Yes. Team settings can be updated at any time.

    You can modify:

    * Team name
    * Time zone
    * Email domain restrictions
    * Feature configurations
    * Team logo and branding

    All settings are available under **Settings → Team Settings**.
  </Accordion>

  <Accordion title="What happens when a team is deleted?" icon="trash">
    Teams are **soft deleted** rather than permanently removed.

    When a team is deleted:

    * Historical incident data is preserved
    * Users immediately lose access
    * Integrations are disconnected

    <Callout icon="warning" color="#f59e0b">
      **Important:** Team deletion is irreversible. Ensure you export any required data beforehand.
    </Callout>
  </Accordion>

  <Accordion title="Can I duplicate a team?" icon="copy">
    Yes. Teams can be duplicated to quickly create similar team structures.

    Duplication can include:

    * Team settings
    * Schedules and escalation policies
    * Groups and configurations
    * Optional user memberships
  </Accordion>

  <Accordion title="How many teams can I create?" icon="hash">
    The number of teams available depends on your **Rootly plan**.

    You can review limits in **Settings → Billing** or contact your account manager.
  </Accordion>
</AccordionGroup>

***

### Migrations & Integrations

<AccordionGroup>
  <Accordion title="How do I migrate teams from PagerDuty or Opsgenie?" icon="arrow-right">
    Rootly provides migration tools to import your existing team structure.

    Supported imports include:

    **PagerDuty**

    * Teams
    * Users
    * Schedules
    * Escalation policies
    * On-call rotations

    **Opsgenie**

    * Teams
    * Schedules
    * Routing rules
    * Escalation policies

    <Card title="Migration Guide" icon="book-open" href="/migrations/pagerduty">
      Learn more about migrating from PagerDuty or Opsgenie
    </Card>
  </Accordion>

  <Accordion title="How do I configure Slack channels for teams?" icon="slack">
    Slack channels can be configured in two ways:

    1. **Team-level mapping** for default notifications
    2. **Group-level mapping** for more granular routing

    To configure:

    1. Navigate to **Settings → Integrations → Slack**
    2. Configure team-level settings
    3. Map groups to Slack channels

    <Card title="Slack Integration" icon="slack" href="/integrations/slack">
      Learn more about configuring Slack for teams
    </Card>
  </Accordion>

  <Accordion title="Can teams create status pages?" icon="globe">
    Yes. Teams can manage their own **public or private status pages**.

    Status pages support:

    * Custom domains
    * Service components
    * Incident communication templates
    * Automated updates

    <Card title="Status Pages" icon="globe" href="/status-pages/status-pages">
      Learn more about creating and managing status pages
    </Card>
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).