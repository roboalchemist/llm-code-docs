# Source: https://docs.rootly.com/managing-teams/attaching-teams-to-incidents.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Attaching Teams To Incidents

> Learn how to associate teams with incidents using Slack commands to ensure proper notifications and team involvement during incident response.

Teams can be attached to incidents in Rootly to ensure the appropriate responders are notified and involved in the incident response process.

When a team is attached to an incident, Rootly can trigger notifications, invite responders into the incident Slack channel, and apply automation workflows related to that team. Attaching teams helps organizations coordinate response efforts by clearly identifying which groups are responsible for investigating or resolving the issue.

If the **Slack integration** is enabled, teams can be attached directly from Slack using Rootly’s slash commands. This allows responders to quickly involve the right team without leaving the incident channel.

***

## Attaching Teams via Slack

If your organization has configured the Slack integration, you can attach teams directly from the Slack incident channel.

To attach a team using Slack:

1. Open the **Slack channel associated with the incident**
2. Type the following command:

```
/rootly add team
```

3. Press **Enter**

Rootly will open a Slack modal where you can select one or more teams to attach to the incident.

<Note>
  You must run this command from the **incident-specific Slack channel**. The command will not work in other Slack channels.
</Note>

***

## Selecting Teams

After running the command, a dialog appears in Slack with a searchable list of available teams.

From this dialog you can:

* Search for teams by name
* Select one or multiple teams
* Review currently attached teams
* Submit the changes

Once you click **Submit**, the selected teams are attached to the incident.

<Frame>
    <img src="https://mintcdn.com/rootly/7ojKISea6oiQMk0o/images/teams/attaching-teams.webp?fit=max&auto=format&n=7ojKISea6oiQMk0o&q=85&s=7f00fbe242e1a80bb8e3e840d24d6769" alt="Attaching teams using Slack" width="847" height="552" data-path="images/teams/attaching-teams.webp" />
</Frame>

***

## What Happens When a Team Is Attached

Attaching a team to an incident can trigger several actions depending on your Rootly configuration.

Common behaviors include:

* **Inviting team members** into the incident Slack channel
* **Sending notifications** to the team’s configured Slack channels
* **Triggering workflows** associated with team involvement
* **Recording team ownership** on the incident timeline

These actions help ensure the correct responders are notified and can begin investigating the incident quickly.

In many organizations, teams represent functional groups such as **Infrastructure**, **Security**, or **SRE**, so attaching the appropriate team helps route the incident to the right experts.

***

## Automatically Adding Team Members

Teams can be configured to automatically add their members to an incident’s Slack channel when they are attached.

When this setting is enabled:

* All members of the team are invited to the incident channel
* Responders can immediately join the conversation and begin coordinating the response

This behavior can be configured from the **team settings** under the team’s communication or channel configuration.

***

## Permissions

Attaching teams to incidents requires permission to update incidents.

If you attempt to run the Slack command without the required permissions, Rootly will return an authorization error.

In most organizations, these permissions are granted to:

* Incident responders
* Incident commanders
* Team administrators
* Organization administrators

If the command does not work for you, contact your Rootly administrator to confirm your access level.

***

## Troubleshooting

<AccordionGroup>
  <Accordion title="The command doesn't work in Slack" icon="triangle-alert">
    The command must be used inside an **incident Slack channel**. If the command is run in a regular Slack channel or a channel that is not linked to an incident, Rootly will not be able to identify the incident.
  </Accordion>

  <Accordion title="I cannot attach a team" icon="lock">
    You may not have permission to update incidents. Attaching teams requires update access to the incident. Contact your administrator if you need this permission.
  </Accordion>

  <Accordion title="The team list is empty" icon="users">
    If no teams appear in the selection dialog, it may mean that no teams have been created in your Rootly organization yet. Teams can be created from the **Configuration → Teams** page.
  </Accordion>

  <Accordion title="Team members were not added to the Slack channel" icon="slack">
    Automatic Slack invitations only occur if the team has the **auto-add members when attached** setting enabled. If the setting is disabled, team members will not automatically join the incident channel.
  </Accordion>
</AccordionGroup>

***

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="What does attaching a team to an incident do?" icon="link">
    Attaching a team to an incident helps identify which group of responders is responsible for investigating or resolving the issue. Once attached, Rootly can trigger notifications, invite team members into the incident Slack channel, and apply any automation workflows configured for that team. This ensures the right responders are aware of the incident and can begin coordinating a response quickly.
  </Accordion>

  <Accordion title="Can I attach more than one team to an incident?" icon="users">
    Yes. Multiple teams can be attached to the same incident. This is common when incidents involve several areas of responsibility, such as infrastructure, security, and application teams. Attaching multiple teams ensures all relevant responders are notified and able to collaborate during the incident response process.
  </Accordion>

  <Accordion title="Do team members automatically join the incident Slack channel?" icon="slack">
    Team members can be automatically invited to the incident Slack channel when a team is attached, depending on the team's configuration. If the **auto-add members when attached** setting is enabled for that team, Rootly will invite all team members to the incident channel so they can participate in the response.
  </Accordion>

  <Accordion title="Why can't I run the Slack command?" icon="triangle-alert">
    The `/rootly add team` command must be run inside the Slack channel associated with the incident. If the command is used in another channel, Rootly cannot determine which incident the command should apply to. Additionally, you must have permission to update the incident in order to attach or modify teams.
  </Accordion>

  <Accordion title="Can I remove a team after attaching it?" icon="unlink">
    Yes. Teams can be removed from an incident if they were attached by mistake or if their involvement is no longer required. This can be done through Slack using the appropriate Rootly command or from the incident interface in the Rootly dashboard.
  </Accordion>

  <Accordion title="Do teams receive notifications when they are attached?" icon="bell">
    In many cases, yes. When a team is attached to an incident, Rootly can send notifications to the communication channels configured for that team, such as Slack channels or email addresses. The exact behavior depends on your team's notification settings and any workflows configured in your organization.
  </Accordion>

  <Accordion title="Who is allowed to attach teams to incidents?" icon="user-shield">
    Only users with permission to update incidents can attach or remove teams. These permissions are typically granted to incident responders, incident commanders, team administrators, or organization administrators depending on your Rootly permission model.
  </Accordion>
</AccordionGroup>

***

## Related Documentation

<CardGroup cols={2}>
  <Card title="Configuring Teams" icon="gear" href="/team-user-management/configuring-teams">
    Configure team members, ownership, and communication settings.
  </Card>

  <Card title="Viewing Teams" icon="group-arrows-rotate" href="/team-user-management/viewing-teams">
    View and switch between teams in your organization.
  </Card>

  <Card title="Managing Incidents" icon="triangle-exclamation" href="/incident-management/managing-incidents">
    Learn how to manage and coordinate incident response.
  </Card>

  <Card title="Slack Integration" icon="slack" href="/integrations/slack">
    Configure Slack to enable chat-ops commands and incident channels.
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).