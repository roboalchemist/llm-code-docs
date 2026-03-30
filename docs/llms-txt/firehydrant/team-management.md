# Source: https://docs.firehydrant.com/docs/team-management.md

# Team Management

<Image alt="Team page in web interface" align="center" width="650px" src="https://files.readme.io/a76ffe1-CleanShot_2024-08-13_at_12.32.552x.png">
  Team page in web interface
</Image>

FireHydrant teams allow you to quickly assign the right group of people to an incident from your chat application or the FireHydrant UI. You can use FireHydrant Teams to:

* Automatically assign responders to incidents based on various criteria, including impacted infrastructure, tags, and any other incident parameter
* Organize and see which team owns which components throughout your infrastructure
* Automatically assign on-call responders from your alerting provider to an incident

## Create and edit teams

To create and manage teams:

1. Go to **Teams** (or **Settings > Teams**, if you do not have [Signals](https://docs.firehydrant.com/docs/signals-introduction) enabled.
2. Click "+ Add team" on the right side of the page if creating, or directly click on the team whose settings you'd like to edit.
3. There are several different fields you can configure and set on Teams:

   1. **Name** - The team name
   2. **Description** - A longer description for the team
   3. **Slug** - The slug for the team. This will be automatically generated from the team name if left blank, but can be edited
   4. **Slack Channel (Signals-only)** - The designated Slack channel for the team. This allows notifications for things like coverage requests to be posted to the team's Slack channel. This setting is only visible for users with Signals enabled.
   5. **Microsoft Teams Channel (Signals-only)** - The designated Microsoft Teams channel for the team. Like for Slack, this allows for things like coverage request notifications to be posted directly to the team. This setting is only visible for users with Signals enabled.
   6. **Memberships** - The list of team members and their default roles\*\* when assigned to incidents. Memberships can also link directly with on-call schedules from Signals or 3rd-party alerting providers.

      <Image alt="Example of adding a member to the team" align="center" width="650px" src="https://files.readme.io/5c9d430-image.png">
        Example of adding a member to the team
      </Image>
   7. **Services for incident response** - Teams can be configured as responders for Services and Functionalities in FireHydrant. This allows automatically assigning teams to incidents when components are marked as impacted.
   8. **Services owned** - Teams can be set as owners for several components and settings throughout FireHydrant, including Services. See the section below on [component ownership](#component-ownership).
4. Once finished, click "Save" or "Create team" to persist changes.

> 📘 \*\*Note:
>
> FireHydrant provides default [Incident Roles](https://docs.firehydrant.com/docs/incident-roles), but you can configure roles however you like. FireHydrant also allows automating team assignments using [SSO](https://docs.firehydrant.com/docs/sso-with-saml) and [SCIM](https://docs.firehydrant.com/docs/scim-configuration).

## Assigning on-call users from alerting providers

<Image alt="Example of seeing VictorOps routing keys when configuring team membership" align="center" width="650px" src="https://files.readme.io/ffcd91a-CleanShot_2024-08-13_at_14.50.54.png">
  Example of seeing VictorOps routing keys when configuring team membership
</Image>

FireHydrant supports assigning users to roles from on-call schedules directly within teams if you are using a 3rd-party alerting provider. These are the providers FireHydrant supports:

* [Opsgenie](https://docs.firehydrant.com/docs/opsgenie-integration)
* [PagerDuty](https://docs.firehydrant.com/docs/pagerduty-integration)
* [Splunk On-Call (VictorOps)](https://docs.firehydrant.com/docs/splunk-on-call-victorops-integration)

Once your chosen alerting provider is set up and configured, you should see your escalation policies, on-call schedules, or routing keys available in the dropdown when configuring team membership.

> 📘 Note:
>
> To assign on-call users when using FireHydrant's [Signals](https://docs.firehydrant.com/docs/signals-introduction), we recommend the following two approaches:
>
> * [Assign a Role runbook step](https://docs.firehydrant.com/docs/runbook-step-assign-a-role) - On top of specific users, this Runbook step allows choosing Signals [Escalation Policies](https://docs.firehydrant.com/docs/signals-escalation-policies) and [On-Call Schedules](https://docs.firehydrant.com/docs/signals-on-call-schedules). When the step executes, it will dynamically look up whoever is on-call according to the chosen policy/schedule and assign them.
> * [Associating Teams in Service Catalog](https://docs.firehydrant.com/docs/associating-teams) - When a Team is a responder to a Service/Functionality and it has a default escalation policy, FireHydrant will automatically look up who's on call in that EP when the Service/Functionality is impacted on an incident.

## Component ownership

FireHydrant teams can own several components or objects throughout the FireHydrant platform. The default behavior is that anyone with <Glossary>Member</Glossary> permissions and higher can make edits to most settings in FireHydrant.

But when an owning team is set on an object, only members of that team can make updates to that object henceforth. FireHydrant supports team ownership for the following items:

* [Runbooks](https://docs.firehydrant.com/docs/runbook-basics#runbook-ownership)
* [Services and Functionalities](https://docs.firehydrant.com/docs/service-catalog-basics)
* [Readiness Checklists](https://docs.firehydrant.com/docs/readiness-checklists)

> 🚧 Note:
>
> If someone sets an owning team on an object, and they are not part of that owning team, they will immediately lose edit access after clicking **Save** unless they have <Glossary>Owner</Glossary> permissions.

## Next Steps

Once you have your teams configured, you can continue expanding your usage of FireHydrant:

* Learn about [assigning users, teams, and roles](https://docs.firehydrant.com/docs/adding-responders) to incidents
* [Set up some Services or Functionalities](https://docs.firehydrant.com/docs/intro-to-service-catalog) in the Catalog and set the responding teams so that whenever an incident occurs, users always know which team(s) need to be involved for which services
* Learn more about setting up [escalation policies, on-call schedules, and more](https://docs.firehydrant.com/docs/signals-introduction) with FireHydrant Signals