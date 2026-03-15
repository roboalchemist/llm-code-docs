# Source: https://docs.firehydrant.com/docs/runbook-step-create-pagerduty-incident.md

# Create PagerDuty Incident

<Image alt="Create PagerDuty Incident step" align="center" width="650px" src="https://files.readme.io/f45b281-image.png">
  Create PagerDuty Incident step
</Image>

This Runbook step allows the creation of a PagerDuty incident/alert as part of a Runbook automation.

## Configuration

* **Incident Title** - The default title for the new PagerDuty incident. [Template Variables](https://docs.firehydrant.com/docs/template-variables) are supported.
* **Incident Details** - The default description for the new PagerDuty incident. [Template Variables](https://docs.firehydrant.com/docs/template-variables) are supported.
* **Incident Creator** - The person who should be shown in PagerDuty as the alert/incident creator. We recommend using a service account.
* **PagerDuty Service** - The impacted service for the incident. Note that PagerDuty only allows attaching a single service to each PagerDuty incident.
* **Policy Name:** The escalation policy for determining the users to be alerted.

After the step in your Runbook is executed, an incident is created in PagerDuty, and you are provided with the link. This alert will also then be linked to the incident automatically, like so:

<Image alt="Linked alert from PagerDuty" align="center" width="650px" src="https://files.readme.io/c1360cd-Screenshot_2023-12-21_at_4.25.54_PM.png">
  Linked alert from PagerDuty
</Image>

> 📘 Note:
>
> We recommend also adding the step to [Resolve Linked Alerts](https://docs.firehydrant.com/docs/runbook-step-resolve-linked-alerts), which will automatically resolve or close the external alert when the FireHydrant incident is resolved. By default, we do not do this and resolving the FireHydrant incident will not automatically resolve the PagerDuty alert.

## Other Capabilities to Explore

* Automatically escalate to the right on-call teams in Opsgenie by [linking services](https://docs.firehydrant.com/docs/link-external-services) between FireHydrant and Opsgenie and then marking the service impacted on an incident.
* You can manually [page users](https://docs.firehydrant.com/docs/on-call-paging-and-lookup) from the Slack incident channel.
* Incidents can be started from inbound alerts via [Alert Routing](https://docs.firehydrant.com/docs/alert-routing).