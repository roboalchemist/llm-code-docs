# Source: https://docs.firehydrant.com/docs/external-status-pages.md

# External Status Pages

One of the primary components of incident response is managing communications with end users or other stakeholders. Often, organizations use status pages for these updates.

The FireHydrant platform offers both [internal status pages](https://docs.firehydrant.com/docs/internal-status-pages), which are meant for the internal team only and require no setup, as well as external status pages (Atlassian and FireHydrant-hosted).

## Prerequisites

To publish incidents and post updates to these status pages, you will need to first:

1. **Set up the integrations.** Visit the documentation links for the supported provider(s) below:
   1. [FireHydrant Status Pages Overview](https://docs.firehydrant.com/docs/status-page-overview)
   2. [Atlassian Statuspage](https://docs.firehydrant.com/docs/atlassian-statuspage-integration)
2. If you'd like FireHydrant to mark components impacted on the status page automatically, then you'll need to do one of the following:
   1. If using FireHydrant Status Pages, then you'll need to ensure the relevant components are visible when [setting up the page](https://docs.firehydrant.com/docs/status-page-setup)
   2. If using Atlassian Statuspage, you must link Statuspage components to FireHydrant Services or Functionalities.

## Attaching Status Pages to Incidents

Attaching status pages to FireHydrant incidents allows creating incidents on said pages, automatically marking relevant components impacted, and seamlessly posting incident updates.

### Automatically via Runbook

<Image alt="The Atlassian Statuspage Runbook step" align="center" width="400px" src="https://files.readme.io/ec36397-runbook-step-atlassian-status-page.png">
  The Atlassian Statuspage Runbook step
</Image>

Runbook steps will automatically create incidents on the status pages and link the status pages to the incident. If you have fulfilled #2 above in [Prerequisites](#prerequisites), then FireHydrant will also mark the linked components as impacted.

Depending on which provider you're using, you can make use of different Runbook steps. See the documentation for:

* [Publish to Status Page (FireHydrant)](https://docs.firehydrant.com/docs/runbook-step-publish-to-status-page-firehydrant)
* [Create a Statuspage.io Incident](https://docs.firehydrant.com/docs/runbook-step-create-a-statuspageio-incident)

### Manually via Slack

You can also add status pages to your incident directly from Slack - you can navigate to the command and click it by running `/fh help`, or you can directly execute the `/fh add status-page` command.

<Image alt="Modal for adding a status page via Slack" align="center" width="400px" src="https://files.readme.io/3925a3e-image.png">
  Modal for adding a status page via Slack
</Image>

### Manually via Command Center

<Image alt="Status Pages tab in UI with &#x22;unattached&#x22; pages" align="center" src="https://files.readme.io/8bb79d3-image.png">
  Status Pages tab in UI with "unattached" pages
</Image>

From the Command Center of an existing incident, click on the **Status Pages** tab. Below is a list of your configured status pages (FireHydrant or Atlassian Statuspage) under the **Inactive** section. Click '+ Add' next to the page you'd like to attach to the incident, and it will attach to the incident and move to the **Active** section. Once a page is added, you will be allowed to post updates.

## Next Steps

* See how to [seamlessly post updates](https://docs.firehydrant.com/docs/posting-updates) to status pages mid-incident
* See how to [integrate Atlassian Statuspage](https://docs.firehydrant.com/docs/atlassian-statuspage-integration)
* Look at configuring [FireHydrant Status Pages](https://docs.firehydrant.com/docs/status-page-setup)