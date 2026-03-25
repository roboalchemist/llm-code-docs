# Source: https://docs.firehydrant.com/docs/on-call-paging-and-lookup.md

# On-Call Paging and Lookup

FireHydrant allows you to directly page teams as well as look up who's on call for any given Service or Functionality.

## Prerequisites

* **You need to have configured an alerting provider**. The providers we support are:
  * [Signals](https://docs.firehydrant.com/docs/signals-introduction) (FireHydrant native alerting/on-call)
  * [Opsgenie](https://docs.firehydrant.com/docs/opsgenie-integration)
  * [PagerDuty](https://docs.firehydrant.com/docs/pagerduty-integration)
  * [Splunk On-Call (VictorOps)](https://docs.firehydrant.com/docs/splunk-on-call-victorops-integration)
* **If you want to page Services, Functionalities, or Environments**, you'll first need to [link them with external services/schedules](https://docs.firehydrant.com/docs/import-and-link-components).

## Paging users, teams, and escalation policies

### via User Interface (Signals only)

<Image alt="Sending a page from FireHydrant's UI" align="center" src="https://files.readme.io/e305fa1-CleanShot_2024-03-13_at_18.48.24.png">
  Sending a page from FireHydrant's UI
</Image>

You can page users/teams from anywhere within FireHydrant by clicking on "Send Alert" at the top header bar. When you page from the UI, you can choose to target [Escalation Policies](https://docs.firehydrant.com/docs/signals-escalation-policies), [On-Call Schedules](https://docs.firehydrant.com/docs/signals-on-call-schedules), [Teams](https://docs.firehydrant.com/docs/team-management), or [Users](https://docs.firehydrant.com/docs/user-administration).

Note that any targets missing required settings or configurations will be marked with a small warning triangle :warning: and an indicator will be shown in the UI.

<Image alt="Warning when trying to page a team without an EP. This warning is shown for teams and users." align="center" width="400px" src="https://files.readme.io/b1b241a-image.png">
  Warning when trying to page a team without an EP. This warning is shown for teams and users.
</Image>

### via Slack

For any of the 3rd party alerting providers that FireHydrant supports, you can easily page any user, team, escalation policy, or service (depending on which alerting provider you use). The command is:

```julia Slack Command
/fh page                      # Opens up the general paging modal
```

`/fh page` opens the general paging modal, which allows you to choose your provider (if multiple are configured) and directly choose other details like who/what to page.

<Image alt="Running the `/fh page` command" align="center" width="650px" src="https://files.readme.io/7ca5273-image.png">
  Running the `/fh page` command
</Image>

If you want to add additional users, teams, or escalation policies to a page or alert that has already been connected to an incident, you can select that page/alert from the "Select or create a page" dropdown.

<Image alt="Create a new page or add responders to an existing page" align="center" width="650px" src="https://files.readme.io/47edc91-image.png">
  Create a new page or add responders to an existing page
</Image>

You can craft a quick message and longer description for your page, and FireHydrant will also add a link to the Slack channel when sending the page through your alerting provider.

Each provider will have slightly different requirements around fields, services, and who to page.

| Provider           | Required Fields                  | Optional Fields                                                |
| ------------------ | -------------------------------- | -------------------------------------------------------------- |
| **Signals**        | - Summary - Who should be paged? | - Description                                                  |
| **PagerDuty**      | - Message - Affected Services    | - Description - Who should be paged?                           |
| **Opsgenie**       | - Message                        | - Incident Priority - Affected Services - Who should be paged? |
| **Splunk On-Call** | - Message - Who should be paged? | - Description                                                  |

Once a page has been sent, FireHydrant will post a message in the channel that will track the status of the page, and a link to the page will be included in the incident's list of external links.

<Image alt="A message to the Incident channel will show and track the page's status" align="center" src="https://files.readme.io/3b8f70f-image.png">
  A message to the Incident channel will show and track the page's status
</Image>

## Paging specific component owners

> 📘 Note:
>
> As of today, you can't page specific component's owners if you're using FireHydrant's Signals. You'll need to use `/fh page` above and page the team(s) directly.

In addition to paging a user or team directly, you can page a team that is linked to a service or functionality. To page a team this way, you can run:

```julia Slack Commands
/fh page service [slug]       # Page a specific service's on-call responders
/fh page functionality [slug] # Page a specific functionality's on-call responders
```

<Image alt="After running `/fh page service` with no arguments" align="center" width="400px" src="https://files.readme.io/f3fd5a5-Screenshot_2023-12-01_at_11.51.04_AM.png">
  After running `/fh page service` with no name
</Image>

## Lookup who's on-call for specific components

> 📘 Note:
>
> As of today, you can't look up on-call for specific components if you're using FireHydrant's Signals. You'll need to use `/fh signals-on-call` and check the team(s) directly.

Directly from Slack, you can run `/fh oncall` or `/fh on-call`. This will pop up a contextual message asking which Service or Functionality you'd like to see the on-call information for.

<Image alt="After running `/fh oncall`" align="center" width="650px" src="https://files.readme.io/a3a7e91-Screenshot_2023-12-01_at_12.28.59_PM.png">
  After running `/fh oncall`
</Image>

Selecting the Service or Functionality will return the information your alerting provider gave to FireHydrant.

If you're using [FireHydrant's Signals](https://docs.firehydrant.com/docs/signals-introduction), you can use the `/fh signals-on-call` to look up who is on-call for your teams or teams across the entire company.

## Next Steps

* See the [Integrations Overview](https://docs.firehydrant.com/docs/integrations-overview) for more information about our alerting integrations
* See [Slack Commands](https://docs.firehydrant.com/docs/slack-commands) for the full list of available Slack commands
* Continue on to [Managing Tasks](https://docs.firehydrant.com/docs/managing-tasks)