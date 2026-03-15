# Source: https://docs.firehydrant.com/docs/runbook-step-resolve-linked-alerts.md

# Resolve Linked Alerts

<Image alt="Resolve Linked Alerts Runbook step" align="center" width="650px" src="https://files.readme.io/c32cf31-image.png">
  Resolve Linked Alerts Runbook step
</Image>

## Prerequisites

* This step won't do anything unless you have an [alerting provider](/docs/integrations-overview#alerting-integrations) configured and one or more alerts are attached to the incident

## Configuration

The resolve linked alerts runbook step requires no configuration and has straightforward functionality. For all third-party alerts attached to an incident through automation or manually, this runbook step will resolve those alerts in the third party when the runbook step is completed.

This Runbook step also works with Alerts generated in [Signals](https://docs.firehydrant.com/docs/signals-introduction), FireHydrant's built-in alerting.