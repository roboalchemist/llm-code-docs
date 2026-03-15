# Source: https://docs.firehydrant.com/docs/linking-on-call-schedules-to-teams.md

# Linking On-Call Schedules to Teams

> 📘 Note:
>
> This page details instructions for 3rd-party alerting providers like Opsgenie, PagerDuty, and VictorOps. For information about FireHydrant's alerting platform, Signals, visit [Introduction to Signals](https://docs.firehydrant.com/docs/signals-introduction).

FireHydrant can integrate and directly pull people from your escalation policies and on-call schedules if you use an alerting provider.

## Prerequisites

Currently, FireHydrant supports the following providers:

* [Opsgenie](https://docs.firehydrant.com/docs/opsgenie-integration)
* [PagerDuty](https://docs.firehydrant.com/docs/pagerduty-integration)
* [Splunk On-Call (VictorOps)](https://docs.firehydrant.com/docs/splunk-on-call-victorops-integration)

Ensure you have one of these providers set up and configured for your FireHydrant account.

## Set on-call schedules in FireHydrant Teams

1. Navigate to **Settings** > **Teams**.
2. From here, you can either **+ Add team** or find the team you'd like to edit, click into it, and then **Edit team**.
3. In the **Memberships** section of the page, click on the **Member name** dropdown. Along with the users from your FireHydrant organization, you will also see your PagerDuty, Opsgenie, or Splunk On-Call (VictorOps) escalation policies.

   * When you select an on-call schedule as a member, the person who is on-call for that schedule at the time of the Team's assignment to an incident will be the user brought in to said incident.

     <Image align="center" alt="Selecting a schedule or escalation policy as a team member" border={false} caption="Selecting a schedule or escalation policy as a team member" src="https://files.readme.io/ca48147-image.png" width="400px" />
4. Under **Role**, select a role to assign this on-call user to.
5. Make other changes to the team as needed, and click **Create team** or **Save changes**.

### Other Important Notes

* The on-call user **must also have an account in FireHydrant**, and **email addresses between the apps must match** for FireHydrant to pull them into the incident channel.
* Changes, such as deletions or additions of on-call schedules or escalation policies, aren't automatically detected by FireHydrant. If, for example, you add a new on-call schedule to your alerting provider, you will need to go to the integration settings for said alerting provider and click **Refresh Schedules** before that new schedule shows as an option in the dropdown in other parts of FireHydrant (like Teams configuration).

<Image align="center" alt="Refresh schedules button on PagerDuty. This button is present on all alerting integrations' pages" border={false} caption="Refresh schedules button on PagerDuty. This button is present on all alerting integrations' pages" src="https://files.readme.io/ace882a-Screenshot_2024-01-04_at_12.31.43_PM.png" width="650px" />

## Pulling in on-call responders

Once you've completed the above steps, FireHydrant will automatically pull in whoever is on-call when the [Team is assigned to an incident](/docs/adding-responders#assigning-teams). This will work regardless of whether the team was manually assigned or automatically as part of Runbooks or Service Catalog settings.

> 🚧 Note:
>
> For **OpsGenie**, FireHydrant only invites the user on the Primary rotation layer when a team is assigned