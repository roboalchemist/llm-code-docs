# Source: https://docs.firehydrant.com/docs/runbook-step-create-a-statuspageio-incident.md

# Create a Statuspage.io Incident

<Image alt="Example Atlassian Statuspage incident posted from FireHydrant" align="center" src="https://files.readme.io/4856d57-atlassian-statuspage-update-example.png">
  Example Atlassian Statuspage incident posted from FireHydrant
</Image>

FireHydrant integrates with [Atlassian Statuspage](https://www.atlassian.com/software/statuspage) and can automatically create incidents as part of your incident response process.

## Prerequisites

1. First, you'll want to make sure you've [set up and configured your Atlassian Statuspage(s)](/docs/integrating-atlassian-statuspage-with-firehydrant).
2. When setting up Statuspage(s), it's important that you [import or link external components](https://docs.firehydrant.com/docs/link-external-services) to FireHydrant Services or Functionalities. Only with the links can FireHydrant properly mark the appropriate components as impacted on your Atlassian Statuspage when you mark a Service or Functionality impacted on an incident.

## Adding the step

Once the integration is configured, add the **Create a Statuspage.io incident** step to a Runbook.

* On the **Details** tab, add a title for the step.
* On the **Conditions & scheduling** tab, create rules that dictate when the status page should be published during the incident response process. The typical flow we see is right at the incident's start.

A typical setup is shown below; when an incident is created, we will automatically copy over the incident name as the status page incident's title and the description of the incident as the status page incident's message.

You can parameterize and choose what information you want to include - to learn more, see our [Template Variables](https://docs.firehydrant.com/docs/template-variables) documentation.

<Image alt="Create a Statuspage.io incident step" align="center" width="650px" src="https://files.readme.io/5277983-image.png">
  Create a Statuspage.io incident step
</Image>

When this Runbook step executes, your attached Atlassian Statuspage is updated with an incident and your configured message.

## Posting to Multiple Statuspages

You can post to multiple Statuspages by adding multiple steps and selecting a different destination page for each step.