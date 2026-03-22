# Source: https://docs.rootly.com/managing-teams/configuring-teams.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring Teams

> Create and manage teams in Rootly, including members, ownership, channels, and integration mappings.

Teams allow you to organize responders, define ownership of operational resources, and configure how groups of users interact with incidents, alerts, and communication channels inside Rootly.

By creating teams, organizations can structure incident response responsibilities more clearly. Teams help determine who should be notified during incidents, which resources a group is responsible for maintaining, and how alerts or updates are distributed across communication platforms like Slack or email.

From the **Teams** page, administrators and authorized users can create new teams, manage membership, assign ownership to infrastructure components, configure routing channels, and link teams to third-party incident management tools.

***

## Create a Team

Creating a team allows you to group responders together and define how that group participates in incidents and operational workflows.

To create a new team:

1. Navigate to **Configuration → Teams**
2. Click **Add New Team**
3. Enter the team details:
   * **Name** — A clear identifier for the team
   * **Description** — Optional context about the team's role or responsibilities
   * **Color** — A visual identifier used throughout the interface
4. Click **Save**

<Frame>
    <img src="https://mintcdn.com/rootly/7ojKISea6oiQMk0o/images/teams/configuring-teams.webp?fit=max&auto=format&n=7ojKISea6oiQMk0o&q=85&s=96fe773b55153fe4095af68850e9cef3" alt="Document image" width="2616" height="1466" data-path="images/teams/configuring-teams.webp" />
</Frame>

After the team is created, it becomes available for incident assignment, alert routing, schedule ownership, and workflow automation.

<Callout icon="info" color="#3b82f6">
  After creating a team, you are automatically added as a member. Membership, permissions, and administrative settings can be modified later from the **Members** tab.
</Callout>

Organizations often create teams that reflect operational structures such as **Infrastructure**, **Security**, **SRE**, **Customer Support**, or **Platform Engineering**. Teams should represent logical responder groups responsible for services or systems.

***

## Import Teams

If your organization already manages response teams in external tools, Rootly allows you to import those teams directly.

Teams can be imported from supported third-party integrations such as **PagerDuty** or **Opsgenie**, allowing organizations to maintain consistent team structures across platforms.

To import teams:

1. Navigate to **Configuration → Teams**
2. Select the relevant import option
3. Choose the teams you want to import
4. Confirm the import

Imported teams will automatically appear in your Rootly configuration and can then be customized further with additional members, channels, and ownership settings.

<Card title="Importing Teams" icon="plug" href="/managing-teams/importing-teams">
  Learn how to import teams from supported integrations.
</Card>

***

## Edit a Team

Once a team has been created, it can be updated at any time to reflect changes in organizational structure, staffing, or responsibilities.

To edit a team:

1. Navigate to **Configuration → Teams**
2. Select the team you want to configure
3. Open the relevant configuration tab
4. Update the settings as needed
5. Save your changes

Team settings can be modified without impacting historical incident data. Updates to members, ownership, or communication channels will apply to future incidents and alerts.

***

## Members

The **Members** tab is where you manage the people who belong to a team.

Adding users to a team ensures they can participate in incidents involving that team and receive relevant notifications.

From this section you can:

* Add existing Rootly users to the team
* Assign a **default Incident Role**
* Designate **team administrators**

### Adding Members

To add a member:

1. Click **Add Member**
2. Search for an existing Rootly user
3. Optionally assign a default **Incident Role**
4. Save the changes

Assigning a default incident role allows Rootly to automatically apply the correct role when the team is attached to an incident.

For example, a team member may automatically become an **Incident Commander**, **Responder**, or **Communications Lead** whenever the team is assigned to an incident.

<Callout icon="info" color="#3b82f6">
  Users must already exist in your Rootly organization before they can be added to a team.
</Callout>

***

### Team Admins

Team administrators have additional permissions for managing team-owned resources.

These users are typically responsible for maintaining operational configurations such as schedules, escalation policies, or services owned by the team.

Team admins may be able to:

* Edit team configuration
* Manage team members
* Update schedules owned by the team
* Maintain escalation policies
* Modify ownership of operational resources

To assign a team admin:

1. Add the user as a team member
2. Select them in the **Team Admin** field

<Callout icon="warning" color="#f59e0b">
  Only existing team members can be assigned as team admins.
</Callout>

Organizations typically assign team admins to engineering leads, SRE managers, or other operational owners responsible for maintaining response readiness.

***

## Ownership

The **Ownership** section identifies which operational resources are managed by a particular team.

Ownership helps teams understand their responsibilities during incidents and determines which users are allowed to manage certain resources.

Teams can own the following resources:

* **Alert Sources**
* **Alert Routes**
* **Services**
* **Schedules**
* **Escalation Policies**

Ownership can help answer questions such as:

* Which team owns a service?
* Who is responsible for maintaining an escalation policy?
* Which responders should be contacted when a specific alert is triggered?

<AccordionGroup>
  <Accordion title="Alert Sources" icon="bell">
    Alert sources represent systems or monitoring tools that generate alerts inside Rootly. When a team owns an alert source, that team is typically responsible for responding to alerts originating from that source.
  </Accordion>

  <Accordion title="Alert Routes" icon="route">
    Alert routes define how alerts are processed and where they are directed. Teams that own alert routes may manage routing logic, escalation behavior, and response procedures for those alerts.
  </Accordion>

  <Accordion title="Services" icon="layers">
    Services can be associated with teams to represent operational ownership of infrastructure or applications. This ownership information helps responders quickly identify which team is responsible for investigating or resolving issues affecting a service.
  </Accordion>

  <Accordion title="Schedules" icon="calendar">
    Teams often own on-call schedules that define responder availability. When a schedule is owned by a team, that team is responsible for maintaining the rotation and ensuring responders are correctly assigned.
  </Accordion>

  <Accordion title="Escalation Policies" icon="sitemap">
    Escalation policies determine how alerts are escalated if they are not acknowledged. Teams that own these policies manage the escalation steps and ensure the correct responders are notified.
  </Accordion>
</AccordionGroup>

***

## Channels

The **Channels** tab connects a team to the communication systems used during incidents.

These configurations allow Rootly to automatically notify the correct Slack channels, user groups, or email recipients when the team is involved in an incident.

You can configure:

* **Slack channels**
* **Slack user groups**
* **Notify emails**
* **Default alert broadcast channels**
* **Default incident broadcast channels**

These settings are frequently used by **automation workflows** to route notifications or tag responders automatically.

***

### Broadcast Channels

Teams can define default Slack channels where Rootly will automatically post updates.

These channels provide centralized visibility for operational events related to the team.

Two broadcast types are available:

**Alerts Channel**

Used to post notifications when the team is paged or when alerts are triggered for that team.

**Incidents Channel**

Used to post updates whenever the team is attached to an incident.

This allows stakeholders and responders to monitor activity without needing to join each individual incident channel.

Teams can also enable automatic behavior that adds team members to an incident’s Slack channel when the team becomes involved.

***

## Integrations

The **Integrations** tab allows Rootly teams to be mapped to external systems.

These mappings connect Rootly to existing incident response or service management platforms, enabling synchronized ownership and automated workflows.

Supported integrations may include:

* **PagerDuty**
* **Opsgenie**
* **Splunk On-Call**
* **PagerTree**
* **Cortex**
* **OpsLevel**
* **ServiceNow**
* **Backstage**

Mapping external teams allows Rootly workflows to interact with those systems more effectively and ensures operational ownership stays aligned across tools.

<Callout icon="info" color="#3b82f6">
  The corresponding integration must already be configured before it can be linked to a team.
</Callout>

***

## Best Practices

When configuring teams, consider the following recommendations:

* Use **clear, descriptive team names** that match your operational structure
* Add **all relevant responders** so incidents reach the correct people
* Assign **team administrators** for teams responsible for schedules or escalations
* Configure **Slack channels** to improve incident visibility
* Map teams to **external systems** when using integrations
* Regularly review membership and ownership to keep team configuration accurate

A well-structured team configuration helps reduce confusion during incidents and ensures alerts reach the correct responders quickly.

***

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="Who can create or edit a team?" icon="user-shield">
    Creating or editing teams typically requires administrative permissions within Rootly. Organization administrators or users with configuration access can create teams, update team settings, manage members, and configure ownership or integrations.

    If you do not see the option to create or edit teams, you may not have the necessary permissions. In that case, contact your Rootly administrator for assistance.
  </Accordion>

  <Accordion title="Do users need to exist in Rootly before being added to a team?" icon="users">
    Yes. Users must first be invited to your Rootly organization before they can be added to a team.

    Once a user account exists, the user can be added as a team member, assigned a default incident role, or designated as a team admin.
  </Accordion>

  <Accordion title="What does a team admin do?" icon="shield-check">
    Team admins help maintain team-level configurations and operational resources.

    Depending on your organization's permissions model, team admins may be responsible for managing schedules, maintaining escalation policies, updating team ownership, and modifying communication channels or integrations associated with the team.
  </Accordion>

  <Accordion title="Can I assign an incident role to a team member?" icon="user-plus">
    Yes. When adding or editing a team member, you can optionally assign a default incident role.

    This role is automatically applied whenever the team is attached to an incident, ensuring responders receive the appropriate responsibilities without requiring manual assignment.
  </Accordion>

  <Accordion title="What can a team own?" icon="layers">
    Teams can own operational resources across the Rootly platform.

    These may include alert sources, alert routes, services, schedules, and escalation policies. Ownership helps identify which team is responsible for maintaining or responding to issues involving those resources.
  </Accordion>

  <Accordion title="What are team channels used for?" icon="slack">
    Team channels connect a team to communication endpoints such as Slack channels, Slack user groups, or email addresses.

    These channels allow Rootly to automatically route notifications, tag responders, and distribute updates whenever the team becomes involved in an incident or alert.
  </Accordion>

  <Accordion title="What's the difference between an Alerts Channel and an Incidents Channel?" icon="messages-square">
    The **Alerts Channel** is used to broadcast notifications whenever the team is paged or when alerts are triggered.

    The **Incidents Channel** posts updates whenever the team is added to an incident. This allows organizations to track team activity across multiple incidents in a centralized Slack channel.
  </Accordion>

  <Accordion title="Can I connect a team to PagerDuty or Opsgenie?" icon="plug">
    Yes. Rootly supports mapping teams to external services such as PagerDuty or Opsgenie.

    These integrations allow Rootly workflows to coordinate with existing incident response systems and help maintain consistent ownership across platforms.
  </Accordion>

  <Accordion title="Can I import teams from another tool?" icon="download">
    Yes. If your organization already manages teams in a third-party system such as PagerDuty or Opsgenie, those teams can be imported directly into Rootly.

    Imported teams can then be customized further with additional members, ownership settings, or communication channels.
  </Accordion>

  <Accordion title="Can I change team settings later?" icon="file-pen">
    Yes. Teams can be modified at any time.

    You can update team members, adjust ownership, change Slack channels, or modify integration mappings without affecting historical incident records.
  </Accordion>
</AccordionGroup>

***

## Related Documentation

<CardGroup cols={2}>
  <Card title="Viewing Teams" icon="group-arrows-rotate" href="/team-user-management/viewing-teams">
    View and switch between teams in your organization.
  </Card>

  <Card title="Importing Teams" icon="plug" href="/managing-teams/importing-teams">
    Import teams from PagerDuty or Opsgenie.
  </Card>

  <Card title="Schedules" icon="calendar" href="/on-call/schedules">
    Configure on-call schedules owned by teams.
  </Card>

  <Card title="Escalation Policies" icon="sitemap" href="/on-call/escalation-policies">
    Manage escalation policies for team-based alerting.
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).