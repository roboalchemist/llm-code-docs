# Source: https://docs.firehydrant.com/docs/linking-alerts-to-incidents.md

# Linking Alerts to Incidents

If you use [Alert Routing](https://docs.firehydrant.com/docs/alert-routing) to open an incident from an alerting or monitoring tool, the alert will automatically be linked to the incident it opens.

However, if you have an incident already open on FireHydrant and want to link an alert manually, you may do so via [The Command Center](https://docs.firehydrant.com/docs/the-command-center) of an incident.

1. On the **Linked Alerts** tab, click on '+ Link an Alert'. This will pull up a complete list of alerts FireHydrant can read within your linked provider.

2. Next to the alert you want to attach to the incident, click '+ Attach.'

This will link the alert to the incident.

<Image alt="Alert linking modal in Command Center" align="center" width="400px" src="https://files.readme.io/3c6db88-image.png">
  Alert linking modal in Command Center
</Image>

### Marking alerts as primary

Any linked alerts will have a **Primary** checkbox. If you select this box to set the alert as **Primary**, it tracks the incident states in FireHydrant. Uncheck this box if you don't want a FireHydrant incident to be automatically resolved when the linked external alert is resolved.

In addition, checking this box also allows you to use the [Resolve Linked Alerts](https://docs.firehydrant.com/docs/runbook-step-resolve-linked-alerts) Runbook step, automatically resolving an alert if the FireHydrant incident it's attached to is resolved.