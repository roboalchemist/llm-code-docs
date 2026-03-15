# Source: https://docs.firehydrant.com/docs/runbook-step-update-a-statuspageio-incident.md

# Update a Statuspage.io Incident

<Image alt="Update a Statuspage.io Incident step" align="center" width="650px" src="https://files.readme.io/4e5e500-image.png">
  Update a Statuspage.io Incident step
</Image>

If a FireHydrant incident is synced with an Atlassian Statuspage incident, you can continue to [post updates](https://docs.firehydrant.com/docs/posting-updates) to that Statuspage incident via the usage of `/fh update`. This Runbook step exists for historical reasons and is an alternative way to post updates to an Atlassian status page.

## Prerequisites

* You must have [Atlassian Statuspage](https://docs.firehydrant.com/docs/atlassian-statuspage-integration) configured
* Your incident should already have a Statuspage [attached to the incident](https://docs.firehydrant.com/docs/external-status-pages), either manually or [automatically via Runbook step](https://docs.firehydrant.com/docs/runbook-step-create-a-statuspageio-incident)

## Configuration

This step only has one field, which is **Default Message**. This is the message that will be prefilled into the input when a responder pulls up this step in Slack or the Command Center.

> 📘 Note:
>
> This step can only be executed manually, not automatically.

## Runbook Execution

To execute the step, responders can pull it up via `/fh runbooks` in Slack or via the Command Center's Runbooks tab.