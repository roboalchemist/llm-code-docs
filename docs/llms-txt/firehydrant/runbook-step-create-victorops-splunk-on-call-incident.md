# Source: https://docs.firehydrant.com/docs/runbook-step-create-victorops-splunk-on-call-incident.md

# Create VictorOps (Splunk On-Call) Incident

<Image alt="Create VictorOps Incident step" align="center" width="650px" src="https://files.readme.io/c7df4c9-image.png">
  Create Splunk On-Call Incident step
</Image>

This Runbook step allows the creation of a Splunk On-Call incident/alert as part of Runbook automation.

> 📘 Note:
>
> VictorOps was acquired by Splunk before being rebranded to Splunk On-Call. The rest of this article uses the term "Splunk On-Call" although there are parts in our user interface and documentation that may still refer to it as VictorOps.

## Configuration

This Runbook step has the following fields:

* **Incident name** - The name of the incident. [Template Variables](https://docs.firehydrant.com/docs/template-variables) are supported.
* **Incident description** - A brief description of the incident. This specifically maps to the `state_message` of the incident in Splunk On-Call. [Template Variables](https://docs.firehydrant.com/docs/template-variables) are supported.
* **Additional Routing Key** - Lets you specify an additional routing key that should always be paged, even if it is not linked to an impacted service
  * By default, when you create an incident with impacted services, this Runbook step will page all routing keys linked to all impacted services
* **Alert default escalation policy?** -  Specifies if you want to alert a default escalation policy when no impacted services are present and no additional Routing Key is specified in the box above.
  * Selecting **Yes** will cause FireHydrant to submit an alert to Splunk On-Call *without a routing key*. That alert is then directed to whatever escalation policy is set as the default in in Splunk On-Call.

Once this Runbook step has executed, the alert will automatically be attached to the incident.

> 📘 Note:
>
> We recommend also adding the step to [Resolve Linked Alerts](https://docs.firehydrant.com/docs/runbook-step-resolve-linked-alerts), which will automatically resolve or close the external alert when the FireHydrant incident is resolved. By default, we do not do this and resolving the FireHydrant incident will not automatically resolve the Splunk On-Call alert.

## Other Capabilities to Explore

* Automatically escalate to the right on-call teams in Opsgenie by [linking services](https://docs.firehydrant.com/docs/link-external-services) between FireHydrant and Opsgenie and then marking the service impacted on an incident.
* You can manually [page users](https://docs.firehydrant.com/docs/on-call-paging-and-lookup) from the Slack incident channel.
* Incidents can be started from inbound alerts via [Alert Routing](https://docs.firehydrant.com/docs/alert-routing).