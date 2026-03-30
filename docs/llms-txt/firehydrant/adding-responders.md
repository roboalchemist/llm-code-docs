# Source: https://docs.firehydrant.com/docs/adding-responders.md

# Adding Responders

Incident roles help align responders behind a clear set of tasks, responsibilities, and expectations. FireHydrant comes with several default roles, but they can be customized. [Read more about customizing roles](https://docs.firehydrant.com/docs/incident-roles).

## Assigning Users to Roles

During an incident, you typically assign users so that there is a record of who was involved. In addition, on FireHydrant, assigning users will automatically pull them into the incident Slack channel and notify them. Assigning users is easy and can be done in multiple ways.

### Manually via Slack

<Image alt="Assigning responders via Slack" align="center" width="400px" src="https://files.readme.io/61c3d15-assign-users-slack.png">
  Assigning responders via Slack
</Image>

From **Slack**, within the Incident channel, you can run the `/fh assign role` command to open a modal where you can assign a user. You can also use the quick action button located on the pinned message in the channel:

<Image alt="Assigning responders via quick action button" align="center" width="650px" src="https://files.readme.io/c45210f-Screenshot_2023-12-01_at_11.35.37_AM.png">
  Assigning responders via quick action button
</Image>

### Manually via UI

<Image alt="Assigning responders via Command Center" align="center" width="400px" src="https://files.readme.io/f6e6876-Screenshot_2023-12-01_at_11.12.05_AM.png">
  Assigning responders via Command Center
</Image>

In the **Command Center** during an incident, you can click the Pencil icon next to **Responders** in the Details panel. This will open a modal to edit the responders on an incident.

### Automatically via Runbook

<Image alt="Assigning roles via Runbook step" align="center" width="650px" src="https://files.readme.io/207f226-Screenshot_2023-12-01_at_11.37.11_AM.png">
  Assigning roles via Runbook step
</Image>

Using [Runbooks](https://docs.firehydrant.com/docs/introduction-to-runbooks), you can automatically [assign individuals to certain roles](https://docs.firehydrant.com/docs/runbook-step-assign-a-role) when incidents start. Codifying this in a Runbook can help make your process repeatable and consistent.

## Assigning Teams

Alongside assigning specific users, you can also assign entire teams of people, grouped together by various traits.

Some organizations will group their team members by function, such as **Incident Commanders**, **Infrastructure Engineers**, and more. Other organizations may group their team members by component ownership, such as by specific [services, functionalities, or environments](https://docs.firehydrant.com/docs/intro-to-service-catalog).

It's up to your organization how you want to organize your teams. You can learn more about [configuring your teams here](https://docs.firehydrant.com/docs/team-configuration).

The biggest difference is that with teams, you can designate roles for all users within the team, as well as for people from [on-call schedules](https://docs.firehydrant.com/docs/linking-on-call-schedules-to-teams).

Just like with users, you can also assign Teams in multiple places.

### Manually via Slack

<Image alt="Assigning teams via Slack" align="center" width="400px" src="https://files.readme.io/8860410-image.png">
  Assigning teams via Slack
</Image>

Within Slack, the command for assigning teams is `/fh assign team`. This will also open a modal for selecting which team you'd like to pull into the incident.

You can also [customize the **New Incident** form for UI and Slack](https://docs.firehydrant.com/docs/incident-fields) to allow selecting teams before declaring the incident.

### Manually via UI

<Image alt="Add Responders modal via Command Center" align="center" width="400px" src="https://files.readme.io/6c53772-Screenshot_2023-12-01_at_11.29.08_AM.png">
  Add Responders modal via Command Center
</Image>

Within an incident's Command Center, just like assigning roles, you can click the pencil icon next to **Response Team** in the details panel. When the modal opens, you can change the radio selection to "Team" instead of "User", allowing you to select a team to assign instead.

You can also choose which team(s) should be included in an incident while declaring a new one in the web UI.

### Automatically via Runbooks

<Image alt="Assigning a team via Runbook step" align="center" width="650px" src="https://files.readme.io/dd29f10-Screenshot_2023-12-01_at_11.39.07_AM.png">
  Assigning a team via Runbook step
</Image>

Just like assigning roles, you can also automate pulling teams into incidents via a [Runbook step](https://docs.firehydrant.com/docs/runbook-step-assign-a-team).

This enables powerful automation such as conditionally pulling certain teams in based on certain conditions - certain Severity, certain milestones, certain tags, etc.

### Automatically via Service Catalog

<Image alt="Auto-add responding team setting for a service/functionality" align="center" width="650px" src="https://files.readme.io/18e2287-Screenshot_2023-12-01_at_11.40.24_AM.png">
  Auto-add responding team setting for a service/functionality
</Image>

If you are making use of the [Catalog](https://docs.firehydrant.com/docs/intro-to-service-catalog), once you've assigned the Responding Team(s) for a Service or Functionality, you can check the setting just below to **Auto-add responding team**. You can configure this in each Service/Functionality's respective settings by going to \*\*Catalog> tionalities] > \[Name] > Ed > .

Onc > Edit\*\*.

Once this setting is enabled, any time this particular Service/Functionality is marked as impacted in an incident, FireHydrant will automatically pull in the responding teams. If you know what system components are involved, it's a fast, highly effective way to pull in the right people.

## Handing Off a Role to Someone Else

<Image alt="Example handoff modal in Slack" align="center" width="400px" src="https://files.readme.io/934b0589a51eb4fc9ab7d027b3291f02d4e4e771d8fd3d1eb5390af80ceac74b-CleanShot_2025-02-10_at_14.50.412x.png">
  Example handoff modal in Slack
</Image>

FireHydrant has a powerful capability that allows you to hand off your role to someone else. From Slack, you can do this with `/fh handoff`. Alternatively, if your organization has [Nudges](https://docs.firehydrant.com/docs/other-incident-settings#incident-nudge-duration) configured, after a set period of inactivity, the incident will also ping people directly reminding them of the open incident, and from there, there will also be buttons that allow handing off the role.

When handing off, you can select which role(s) you're currently assigned to hand off, and when handing off, whether or not to reassign all open/incomplete tasks to the new user.

## Next Steps

* You can also use your alerting provider's escalation policies or on-call schedules to [pull whoever's on call for a particular service](https://docs.firehydrant.com/docs/linking-on-call-schedules-to-teams)
* Make use of FireHydrant's [task lists](https://docs.firehydrant.com/docs/managing-tasks) to effectively align responders or roles to tasks that need to be done