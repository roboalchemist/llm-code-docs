# Source: https://docs.firehydrant.com/docs/runbook-step-page-people-via-signals.md

# Page people via Signals

<Image alt="Page people via Signals Runbook step" align="center" width="650px" src="https://files.readme.io/e23070dc1198adc915eb7dbea1cbb2fbca3a2395f5413d373ae8fd3375ae33fa-CleanShot_2024-10-09_at_14.14.48.png">
  Page people via Signals Runbook step
</Image>

The **Page people via Signals** Runbook step allows you to automatically page out to various targets on FireHydrant's [Signals alerting platform](https://docs.firehydrant.com/docs/signals-introduction) as part of workflow automations of incidents.

## Configuration

1. When editing or creating a new Runbook, click "+ Add Step" and search for the FireHydrant dropdown. Select **Page people via Signals**.
2. On the next page, you will have the following fields to fill out for the step:
   1. **Name (required)** - A descriptive name for the step. This will be what is shown on the **Runbooks** tab for any incidents this Runbook has attached to.
   2. **Alert Summary (required)** - The summary/title of the alert. It defaults to the name of the incident, but you can adjust it as needed\*\*
   3. **Alert Body** - A description/body for the alert
   4. **Who to page (required)** - Select the target(s) to page as part of this Runbook step. The available targets include [Teams](https://docs.firehydrant.com/docs/team-management), [Escalation Policies](https://docs.firehydrant.com/docs/signals-escalation-policies), [On-Call Schedules](https://docs.firehydrant.com/docs/signals-on-call-schedules), [Users](https://docs.firehydrant.com/docs/user-administration), and [Webhook Targets](https://docs.firehydrant.com/docs/signals-webhook-alert-targets).
3. Once configured, click Save on the modal, and then remember to click Save Runbook at the top right to persist Runbook changes.

When the Runbook step executes, you should see a Signals alert created and automatically linked to the incident that executed the step.