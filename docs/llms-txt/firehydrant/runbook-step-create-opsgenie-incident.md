# Source: https://docs.firehydrant.com/docs/runbook-step-create-opsgenie-incident.md

# Create Opsgenie Incident

<Image alt="Create Opsgenie Incident step" align="center" width="650px" src="https://files.readme.io/2272f5e-image.png">
  Create Opsgenie Incident step
</Image>

This Runbook step allows the creation of an Opsgenie incident as part of a Runbook automation.

## Configuration

* **Incident Title** - The default title for the new Opsgenie incident. [Template Variables](https://docs.firehydrant.com/docs/template-variables) are supported.
* **Incident Details** - The default description for the new Opsgenie incident. [Template Variables](https://docs.firehydrant.com/docs/template-variables) are supported.
* **Priority** - The priority to set on the new Opsgenie incident as defined by Opsgenie
* **Team** - Which Opsgenie team should be assigned to and notified of the incident

After the step in your Runbook is executed, an incident is created in Opsgenie, and you are provided with the link. This alert will also then be linked to the incident automatically, like so:

<Image alt="Example incident with attached Opsgenie incident/alert" align="center" width="650px" src="https://files.readme.io/410e231-image.png">
  Example incident with attached Opsgenie incident/alert
</Image>

> 📘 Note:
>
> We recommend also adding the step to [Resolve Linked Alerts](https://docs.firehydrant.com/docs/runbook-step-resolve-linked-alerts), which will automatically resolve or close the external alert when the FireHydrant incident is resolved. By default, we do not do this and resolving the FireHydrant incident will not automatically resolve the Opsgenie alert.

## Other Capabilities to Explore

* Automatically escalate to the right on-call teams in Opsgenie by [linking services](https://docs.firehydrant.com/docs/link-external-services) between FireHydrant and Opsgenie and then marking the service impacted on an incident.
* You can manually [page users](https://docs.firehydrant.com/docs/on-call-paging-and-lookup) from the Slack incident channel.
* Incidents can be started from inbound alerts via [Alert Routing](https://docs.firehydrant.com/docs/alert-routing).