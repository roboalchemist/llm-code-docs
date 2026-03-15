# Source: https://docs.firehydrant.com/docs/the-command-center.md

# The Command Center

<Image alt="Overview of Command Center" align="center" width="650px" src="https://files.readme.io/62c336a-image.png">
  Overview of Command Center
</Image>

The Command Center, the hub of every incident on FireHydrant, is a crucial component of our incident management process. It aggregates all information and activity related to the incident, serving as a vital interface for incident management, especially when Slack is unavailable.

## How to get to the Command Center

After you've started an incident, the link to the Command Center is available from multiple locations:

* As a bookmark in the incident's Slack channel, if the channel has been created

<Image alt="via Bookmark in the Incident Channel" align="center" src="https://files.readme.io/e0a5745-command-center-bookmark.png">
  via Bookmark in the Incident Channel
</Image>

* As a link on the pinned message in the incident channel, and/or a notification message posted to any other Slack channels

<Image alt="via Notification messages sent to other Slack channels" align="center" width="650px" src="https://files.readme.io/bb926b8-Screenshot_2023-12-05_at_4.49.16_PM.png">
  via Notification and pinned messages
</Image>

* On the **Incidents** page under **Active Incidents**

<Image alt="via Incidents page with 'Active' filter" align="center" width="650px" src="https://files.readme.io/7087cee-image.png">
  via Incidents page with 'Active' filter
</Image>

* On your Dashboard page, either in "My Active" or "All Active" tabs, or at the very top if you are watching the incident

<Image alt="via user's Dashboard page" align="center" width="650px" src="https://files.readme.io/f29899a-image.png">
  via user's Dashboard page
</Image>

You can also use various other locations to navigate to the incident, including the Service Catalog. Getting to an incident's home page should not be difficult regardless of where you are.

> 📘 Note:
>
> If you know the incident's number (e.g, 455), you can also directly navigate to it by punching the following URL in the address bar: `app.firehydrant.io/incidents/{number}`

## Details Panel

The Command Center is divided into two sections: the details panel on the right side and the central section, which occupies most of the page.

The Details panel shows some of the high-level details of the incident:

* **Description** is a general description of the incident. Response teams generally use it to give a brief overview of the incident for themselves, but it can be used for other purposes via [Liquid templating](https://docs.firehydrant.com/docs/template-variables).
* **Links** show any integration links like [Slack](https://docs.firehydrant.com/docs/slack-integration), [Jira tickets](https://docs.firehydrant.com/docs/jira-cloud-integration), attached [status pages](https://docs.firehydrant.com/docs/status-page-overview), as well as external links that users add manually.\*
* **Related Incidents** allow responders to mark multiple incidents as [Related Incidents](https://docs.firehydrant.com/docs/related-incidents).
* **Suggested Incidents** (requires [enabling AI features](https://docs.firehydrant.com/docs/ai-powered-incident-summaries)) will show a list of past incidents most similar to the current one.
* **Responders** section shows assigned teams and team members involved in the incident and their [assigned roles](https://docs.firehydrant.com/docs/adding-responders).
* **Custom Fields** created by your organization will also be displayed here. Learn more about [Custom Fields](https://docs.firehydrant.com/docs/incident-custom-fields).
* **Impacted Components** denotes which [Catalog items](https://docs.firehydrant.com/docs/service-catalog-basics) are impacted during the incident.
* **Customer Impact Summary** is a description of the impact to customers, if any.
* **Customer Support Issues** shows any linked [Zendesk tickets](https://docs.firehydrant.com/docs/zendesk-integration) and respective customers linked to them.
* **[Tags](https://docs.firehydrant.com/docs/incident-tags)** and **[Labels](https://docs.firehydrant.com/docs/incident-labels)** allow you to track and organize custom data about your incidents.

> 📘 \*Note:
>
> You are able to edit video conferencing links to replace them with different URLs (e.g., you want to use a different Zoom link than what FireHydrant generates, etc.).

## Main Section

The main section of the page is split into multiple tabs for various purposes and a top title section.

### Title Section

The topmost section contains high-level details such as the name of the incident, who opened the incident, and when, as well as who is currently looking at the incident. In addition, there are more important details about the incident which can also be modified:

* **[Priority](https://docs.firehydrant.com/docs/severities-and-priorities)** is the priority of an incident\*\*.
* **[Severity](https://docs.firehydrant.com/docs/severities-and-priorities)** describes how major/urgent an incident is\*\*.
* **[Milestone](https://docs.firehydrant.com/docs/incident-milestones)** is the current status of the incident. You can also click here to modify any timestamps of previous milestones.
* **[Incident Slack channel](https://docs.firehydrant.com/docs/slack-integration)**, if one exists
* **[Internal status page](https://docs.firehydrant.com/docs/internal-status-pages)**, which every incident has on FireHydrant.

> 📘 \*\*Note:
>
> Some FireHydrant users may use only Severity, only Priority, or both. It's up to you to decide what makes the most sense, but **Severities** have a lot more functionality across the platform overall. Priority can be disabled in your Organization's settings under **Settings> Organization**.

### Summary (requires AI)

<Image alt="The new Summary tab" align="center" width="400px" src="https://files.readme.io/c2c2987-CleanShot_2024-04-24_at_15.48.202x.png">
  The new Summary tab
</Image>

The **Summary** tab is a new tab introduced together with new [AI-Powered Incident Management](https://docs.firehydrant.com/docs/ai-powered-incident-management) capabilities on FireHydrant. On this tab, there's a visual representation of the current milestone/status of the incident and a few fields:

* **Incident Summary** provides an AI-generated summary of everything that has happened so far on the incident. You can regenerate the summary at any time to get the latest updates with all the newest information included in the context.
* **Transcript** provides real-time transcription of the conversation being had on the meeting bridge, if there is one (currently only available for Zoom).
* **Recent Updates** shows any recent updates posted to the incident and allows the user to also generate a new update and post it.

To learn more about FireHydrant's incident AI copilot, visit [AI-Powered Incident Management](https://docs.firehydrant.com/docs/ai-powered-incident-management).

### Incident Timeline

The **Incident Timeline** is a running timeline of all events that have occurred throughout the incident. Things we track include:

* Runbook steps execution and status
* Users performing actions like posting notes, updating task completion, etc.
* Any messages or images posted both to the Slack channel or in the user interface

<Image alt="Attaching images to the timeline" align="center" width="650px" src="https://files.readme.io/d11c1f0-Screenshot_2023-11-30_at_5.23.17_PM.png">
  Attaching images to the timeline
</Image>

See [Incident Timeline](https://docs.firehydrant.com/docs/incident-timeline) to read more about the incident timeline.

### Tasks

<Image alt="Tasks + Follow-Ups tab" align="center" width="650px" src="https://files.readme.io/9c4d4521fb84ae3305587c281fbc40b7de4197d23e6494162b8feddab65cb66f-CleanShot_2025-01-13_at_18.10.12.png">
  Tasks + Follow-Ups tab
</Image>

The **Tasks** tab shows all of the [Tasks](https://docs.firehydrant.com/docs/managing-tasks) and [Follow-Ups](https://docs.firehydrant.com/docs/managing-follow-ups) added to the incident and who they've been assigned to. You can directly manage Tasks and Follow-Ups from this page and Slack.

### Status Pages

<Image alt="Status Pages tab" align="center" width="650px" src="https://files.readme.io/4cf8d13-image.png">
  Status Pages tab
</Image>

The **Status Pages** tab shows all attached (active) status pages for the incident. By default, FireHydrant won't post automatically to a status page, but you can automate this via Runbooks. See [Publish to Status Page (FireHydrant)](https://docs.firehydrant.com/docs/runbook-step-publish-to-status-page-firehydrant) and [Create a Statuspage.io Incident](https://docs.firehydrant.com/docs/runbook-step-create-a-statuspageio-incident).

FireHydrant also allows you to directly post to your status page(s) from Slack as well via the `/fh update` command.

### Runbooks

<Image alt="Runbooks tab" align="center" width="650px" src="https://files.readme.io/a849b1a-image.png">
  Runbooks tab
</Image>

The **Runbooks** tab shows all attached Runbooks, their steps, and the statuses of each step.

This allows you to see which Runbooks are running on this particular incident as well as if any steps errored or executed successfully. This is useful for both keeping tabs on each incident's automation as well as debugging.

### Linked Alerts

The **Linked Alerts** tab shows any alerts linked to this incident from your alerting provider. If you use [Alert Routing](https://docs.firehydrant.com/docs/alert-routing) to create incidents on FireHydrant, then the corresponding alert will automatically be attached to the incident. Otherwise, alerts can be manually attached to an incident here.

### Change Events

<Image alt="Command Center Change Events tab" align="center" width="650px" src="https://files.readme.io/ea80c3e-Screenshot_2023-12-01_at_9.30.12_AM.png">
  Command Center Change Events tab
</Image>

The final tab, **Change Events**, showcases any recent changes to your system that FireHydrant automatically associated with the incident because of the impacted Catalog items.

Alongside out-of-box integrations for [GitHub](https://docs.firehydrant.com/docs/github-integration) and [Kubernetes](https://docs.firehydrant.com/docs/kubernetes-integration), FireHydrant has both a [robust API](https://developers.firehydrant.com/#/operations/postV1Changes) as well as a [FireHydrant CLI (fhcli)](https://docs.firehydrant.com/docs/firehydrant-cli) that allows you to automate logging changes to your systems from various other sources.

Some examples include Continuous Integration workflows as well as serverless function webhooks upon detecting infrastructure changes.

Associating change events with incidents can potentially help your team identify contributing factors for the incident faster.

## Action Buttons

<Image alt="Contextual dropdown menu" align="center" width="400px" src="https://files.readme.io/cc308dc-image.png">
  Contextual dropdown menu
</Image>

The top right section includes action buttons for the incident and is split into a contextual menu and a "primary" action.

The contextual menu includes actions such as [converting the incident to private](https://docs.firehydrant.com/docs/private-incidents), switching to the [Retrospective](https://docs.firehydrant.com/docs/conducting-retrospectives) view of the incident (without making any updates), and [archiving the incident](https://docs.firehydrant.com/docs/archiving-incidents).

Once your incident has started, the primary action at the top right is to **Resolve** the incident. When the incident is resolved, the primary action becomes **Start Retrospective** to start the [incident retrospective](https://docs.firehydrant.com/docs/conducting-retrospectives), which changes the [Milestone](https://docs.firehydrant.com/docs/incident-milestones) to "Retrospective Started" and also flips over to the retrospective view.

<Image alt="Additional primary action (update)" align="center" width="400px" src="https://files.readme.io/3e6658e-image.png">
  Additional primary action (update)
</Image>

The last dropdown on the far right is for [Posting Updates](https://docs.firehydrant.com/docs/posting-updates), which functions very similarly to the same modal in Slack.

## Next Steps

Now that you've gotten an overview of the **Command Center**, you can learn more about FireHydrant by reading in greater detail about various aspects of incidents:

* [Lifecyle Phases](https://docs.firehydrant.com/docs/lifecycle-phases) are the status/progress of each incident
* [Incident Roles](https://docs.firehydrant.com/docs/incident-roles) help align responders behind specific responsibilities
* [Managing Tasks](https://docs.firehydrant.com/docs/managing-tasks) helps keep responders on track and with clear guidelines
* See the quickstart guides for [conducting incidents from Slack](https://docs.firehydrant.com/docs/slack-responder-guide) and [from the web UI](https://docs.firehydrant.com/docs/ui-responder-guide).