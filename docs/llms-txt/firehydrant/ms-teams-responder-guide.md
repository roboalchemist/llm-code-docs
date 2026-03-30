# Source: https://docs.firehydrant.com/docs/ms-teams-responder-guide.md

# MS Teams Responder Guide

## Prerequisites

For this guide, we assume:

* [ ] Your basic integrations (Jira, Zoom, MS Teams, etc.) have already been set up [by an admin](https://docs.firehydrant.com/docs/admin-quickstart)
* [ ] You have a user account on FireHydrant within your Organization\*

If the above is not met, we recommend contacting your FireHydrant <Glossary>Owner</Glossary> to invite you to the organization and set up the required integrations. Reading the introduction will give you an idea of the many moving parts of the FireHydrant platform.

> 🚧 \*Note
>
> If your organization already exists on FireHydrant, **do not register for an account directly on FireHydrant's website**—this will create a new, separate organization. Instead, ask an admin from your organization to invite you or provision an SSO seat for the existing organization.

***

## Basic FireHydrant concepts

* **Incident**: Any declared situation. Can range in severity from `UNSET` (unknown severity) to `SEV1` or [whatever you customize](https://docs.firehydrant.com/docs/severities-and-priorities). Each incident has its own [home page](https://docs.firehydrant.com/docs/the-command-center) and [timeline](https://docs.firehydrant.com/docs/incident-timeline).
* **Milestone**: The [current status](https://docs.firehydrant.com/docs/incident-milestones) of an incident. As you mitigate, you will want to keep this up-to-date, and FireHydrant will automatically log the timestamps of these transitions to generate our [Analytics](https://docs.firehydrant.com/docs/analytics-basics).
* **Runbook**: FireHydrant's [automation engine](https://docs.firehydrant.com/docs/introduction-to-runbooks). Traditionally, "runbooks" describe instructions and steps for responders to execute, but on FireHydrant, these steps will execute automatically.
* **Service Catalog**: FireHydrant's [catalog](https://docs.firehydrant.com/docs/intro-to-service-catalog) for your system's components. It helps tie together teams, users, and the components they own, making it easy to recruit the right people for the right jobs.
* **Retrospective**: A review of an incident. FireHydrant's [Retrospectives](https://docs.firehydrant.com/docs/conducting-retrospectives) contextualize and gather all incident information to make your reviews focused and productive.

For a deeper view of all parts of FireHydrant and the incident lifecycle, visit the **Incidents** section of the documentation on the left.

***

## Incident Response

With the above concepts covered, let's dive into conducting incidents.

FireHydrant supports driving incidents end-to-end from both MS Teams and the user interface. If MS Teams is ever unavailable or degraded, you can still count on FireHydrant to support your incident management. Visit the [Web UI Responder Guide](https://docs.firehydrant.com/docs/web-ui-responder-guide) to see how to conduct incidents via the web UI.

This guide covers most of the actions you can take in an incident and links to documentation pages that provide additional detail.

> 📘 Note
>
> <Image alt="How to get to the Tab" align="center" width="400px" src="https://files.readme.io/d1aff4f-CleanShot_2024-05-17_at_13.45.24.png">
>   How to get to the Tab
> </Image>
>
> The FireHydrant Tab is available in Microsoft Teams as an additional interface for conducting incidents. This tab closely mirrors our [web app UI](https://docs.firehydrant.com/docs/the-command-center), nicknamed the "Command Center."
>
> While some of the actions outlined below are in the Tab that is automatically attached to each incident channel, others are available via chat commands, and some are available via both.
>
> See the [complete list of Microsoft Teams Commands](https://docs.firehydrant.com/docs/microsoft-teams-commands)

### Logging in

For users to interact with FireHydrant, you will need to log in. There are two separate logins:

* **Bot Command Login** - You will need to run `@FireHydrant login` as a bot command. This authorizes you with the bot and connects your MS Teams account with your FireHydrant account. This login persists across all devices and instances of MS Teams.
* **Tab Login** - The Tab application is essentially a mounted iFrame hosting a web application that is an additional window to FireHydrant. Those logins are local sessions and subsequently you'll need to do a Tab login on each device you use the Tabs.

Once you're logged into your FireHydrant Bot and Tab, you'll be able to perform the actions and commands listed in the rest of this guide.

***

### Starting incidents

<Image alt="Running `@FireHydrant new` in MS Teams" align="center" width="400px" src="https://files.readme.io/491911a388e08d034e2921efa4764658d39bd06ab64c5bdf34785c5e401f643d-CleanShot_2025-01-09_at_16.58.55.png">
  Running `@FireHydrant new` in MS Teams
</Image>

* **Available as Chat Command**: ✅
* **Available in Tab UI**: -

```
@FireHydrant new
```

This will return a card with buttons for creating a new incident, a [Retroactive Incident](https://docs.firehydrant.com/docs/retroactive-incidents), or opening the help modal.

<Image alt="Example of an incident creation modal. Fields are customizable" align="center" width="400px" src="https://files.readme.io/b51fb9887a684d184ce79fee2ea782a6c0db1c9d9bc9a03b4042b2ea09509543-CleanShot_2025-01-09_at_17.01.53.png">
  Example of an incident creation modal. Fields are customizable
</Image>

When creating either a new incident or retroactive incident, a modal will pop open with the configured [Incident Fields](https://docs.firehydrant.com/docs/incident-fields) settings, editable by people in your organization with <Glossary>Owner</Glossary> and <Glossary>Member</Glossary> permissions.

The returned card is slightly modified to allow choosing an incident type if [Incident Types](https://docs.firehydrant.com/docs/incident-types) are enabled in your organization. These will prefill the opened modal with fields and values relevant to the selected type.

#### Additional Resources

* [Starting Incidents](https://docs.firehydrant.com/docs/starting-incidents)
* [Customizing Incident Fields](https://docs.firehydrant.com/docs/incident-fields)
* [Incident Types](https://docs.firehydrant.com/docs/incident-types)

***

### Assigning roles and teams

<Image alt="Assigning Roles and Teams in MS Teams" align="center" width="650px" src="https://files.readme.io/144a084-CleanShot_2024-05-17_at_13.37.58.png">
  Assigning Roles and Teams in MS Teams
</Image>

* **Available as Chat Command**: ✅
* **Available in Tab UI**: ✅

Assigning roles and teams is helpful for tracking who is working on the incident. You can assign roles and teams with the following MS Teams commands:

```
@FireHydrant assign role   # Assign individuals to roles
@FireHydrant assign team   # Assigns an entire team with preset roles
```

To assign roles in the Tab UI, you can look at the **Responders** section in the Details Panel.

<Image alt="Responders section in Details in the Tab" align="center" width="400px" src="https://files.readme.io/9c2ee30-CleanShot_2024-05-17_at_13.52.49.png">
  Responders section in Details in the Tab
</Image>

#### Additional resources

* [Adding Responders](https://docs.firehydrant.com/docs/adding-responders)
* [Incident Roles](https://docs.firehydrant.com/docs/incident-roles)
* [Linking On-Call Schedules to Teams](https://docs.firehydrant.com/docs/linking-on-call-schedules-to-teams)
* [Team Configuration](https://docs.firehydrant.com/docs/team-configuration)

***

### Managing tasks

Task management can help streamline the response and ensure responders know what to do. You may create and assign tasks ad-hoc or predefine lists of tasks to assign during incidents.

<Image alt="Adding a Task via chat command" align="center" width="400px" src="https://files.readme.io/aa6bf8b-CleanShot_2024-05-17_at_14.19.29.png">
  Adding a Task via chat command
</Image>

* **Available as Chat Command**: ✅ (adding a new, ad-hoc Task)
* **Available in Tab UI**: ✅ (all Task-related actions)

In MS Teams, you can add a new task and assign it using a command:

```
@FireHydrant add task
```

Otherwise, you will want to switch to the FireHydrant Tab and check the Tasks tab within the application to update Tasks and add Task Lists to the incident.

<Image alt="Tasks tab in the FireHydrant application Tab" align="center" width="650px" src="https://files.readme.io/57d056f-CleanShot_2024-05-17_at_14.24.35.png">
  Tasks tab in the FireHydrant application Tab
</Image>

#### Additional resources

* [Managing Tasks](https://docs.firehydrant.com/docs/managing-tasks)
* [Add Task List Runbook Step](https://docs.firehydrant.com/docs/runbook-step-add-task-list)

***

### Editing incident details

<Image alt="The Details panel in the FireHydrant Tab in Teams" align="center" width="650px" src="https://files.readme.io/3822cae-CleanShot_2024-05-17_at_15.16.11.png">
  The Details panel in the FireHydrant Tab in Teams
</Image>

* **Available as Chat Command**: -
* **Available in Tab UI**: ✅

On FireHydrant, we distinguish between **editing** vs. **posting updates** on an incident. An **Edit** modifies incident details, such as the severity, name, description, or other fields.

For Microsoft Teams, there are no specific commands to edit Incident details - you should switch to the FireHydrant tab to edit incident details fields in the right-side details panel.

***

### Posting an update

<Image alt="Posting an update via Command in MS Teams" align="center" width="650px" src="https://files.readme.io/8b6e605-CleanShot_2024-05-17_at_15.21.11.png">
  Posting an update via Command in MS Teams
</Image>

* **Available as Chat Command**: ✅
* **Available in Tab UI**: ✅

An **Update** is a more formal status message from a responder regarding the overall progress of an incident. Updates also include potential changes to the **Milestone** and impacted components.

If you have an [External Status Page](https://docs.firehydrant.com/docs/external-status-pages) configured and attached to the incident, you can also post this update to the status page(s) using the same action, reducing the need to context-switch.

The chat command for this is:

```
@FireHydrant update
```

In the FireHydrant Tab, you can find the "Update Incident" button on the right just below "Resolve Incident." It opens a modal that is similar in layout and content to the card shown above.

<Image alt="Where to find the &#x22;Update Incident&#x22; button on the Tab" align="center" width="650px" src="https://files.readme.io/75f084c-CleanShot_2024-05-17_at_15.24.28.png">
  Where to find the "Update Incident" button on the Tab
</Image>

***

### Marking important events

<Image alt="&#x22;Starring&#x22; a message" align="center" width="650px" src="https://files.readme.io/b199177-CleanShot_2024-05-17_at_15.29.55.png">
  "Starring" a message
</Image>

* **Available as Chat Command**: ✅
* **Available in Tab UI**: -

You can flag specific messages or timeline events as important. These "Starred events" are shown first in the Retrospective and exported as part of the timeline to PDF, Google Docs, and Confluence.

On Microsoft Teams, you can mark a chat message or other post in the channel as important by clicking **Ellipses** > **More actions** > **Star message**.

The same can be done to unstar a message if you decide it is no longer important to include in the review. Note that FireHydrant always tracks messages and events by default. Starring/unstarring determines whether items in the timeline are included in the post-incident review.

#### Additional Resources

* [Incident Timeline](https://docs.firehydrant.com/docs/incident-timeline)

***

### On-call lookup and paging

<Image alt="Paging out using the `@FireHydrant page` command" align="center" width="400px" src="https://files.readme.io/47b2ac2-CleanShot_2024-05-20_at_09.41.112x.png">
  Paging out using the `@FireHydrant page` command
</Image>

* **Available as Chat Command**: ✅
* **Available in Tab UI**: -

FireHydrant allows looking up who's on call and paging directly from the incident channel if you require additional help from other team members.

```
@FireHydrant oncall                                  # For 3rd-party alerting providers
@FireHydrant signals-on-call                         # For FireHydrant Signals
@FireHydrant page                                    # For all alerting providers
@FireHydrant page [team | service | functionality]   # For 3rd-party alerting providers
```

#### Additional Resources

* [On-Call Paging and Lookup](https://docs.firehydrant.com/docs/on-call-paging-and-lookup)

***

### Create follow-ups

<Image alt="Creating a follow-up in MS Teams" align="center" width="650px" src="https://files.readme.io/e8ef1a3-CleanShot_2024-05-20_at_10.17.082x.png">
  Creating a follow-up in MS Teams
</Image>

* **Available as Chat Command**: ✅
* **Available in Tab UI**: ✅

While **Tasks** are ephemeral items to handle during an incident, **Follow-Ups** are action items that should be prioritized for work later. When creating Follow-Ups, you can additionally select an external ticketing project, which creates a corresponding ticket in a third-party tool (like Jira).

```
@FireHydrant add follow-uo
```

In the Tab UI, there is a dedicated sub-tab for managing Follow-Ups, seen below.

<Image alt="Follow-ups sub-tab within the FireHydrant application tab" align="center" width="650px" src="https://files.readme.io/a7d9b60-CleanShot_2024-05-20_at_10.25.052x.png">
  Follow-ups sub-tab within the FireHydrant application tab
</Image>

#### Additional Resources

* [Managing Follow-Ups](https://docs.firehydrant.com/docs/managing-follow-ups)

***

### Resolving the incident

<Image alt="Resolving the incident in MS Teams" align="center" width="650px" src="https://files.readme.io/4979a75-CleanShot_2024-05-20_at_10.21.572x.png">
  Resolving the incident in MS Teams
</Image>

* **Available as Chat Command**: ✅
* **Available in Tab UI**: ✅

Typically, users will first transition an incident to the **Mitigated** Milestone and observe the situation for a while to ensure stability. Once engineers have confirmed or feel confident that things are fully resolved, they may close the incident on FireHydrant.

> 🚧 Note:
>
> Resolving an incident will halt all current Runbook steps, resolve the incident on any attached status pages, and update all notification messages (in e.g., chat tools) to reflect the new state.

```
@FireHydrant resolve
```

In the Tab UI, a button to resolve the incident will always be present, just like in the Command Center UI.

<Image alt="Resolving the incident via Tab UI" align="center" width="650px" src="https://files.readme.io/171ae1b-CleanShot_2024-05-20_at_10.31.042x.png">
  Resolving the incident via Tab UI
</Image>

#### Additional Resources

* [Resolving Incidents](https://docs.firehydrant.com/docs/resolving-incidents)

***

## Running a retrospective

* **Available as Chat Command**: ✅
* **Available in Tab UI**: -

A retrospective is your team's opportunity to learn from the incident. Although you can initiate the Retrospective from Microsoft Teams, you'll need to head over to the FireHydrant Web UI to fully conduct this final stage of the incident.

### Starting the retro

```
@FireHydrant start retro
```

> 🚧 Note
>
> Starting the retro will transition the milestone to **Retrospective Started**, which also resolves the incident. You can start the retro from any other state/milestone.

### Conducting the retro

<Image alt="Incident Retrospective" align="center" width="650px" src="https://files.readme.io/9be99e9-Untitled-2024-04-19-1118.png">
  Incident Retrospective
</Image>

Like the Command Center, the Retrospective has two sections: the main section and the timeline. The timeline is to the right and shows Starred Events by default. You can adjust the filters to show other events.

The main section contains the core content of the retrospective, separated into multiple tabs. You can work your way through all the details and tabs individually.

* **Summary (requires AI)** - Like the Command Center, the Summary tab functions as your AI dashboard. Here, you can get a head start on filling out your retrospective by having the AI copilot attempt to fill in all your details and fields using context from the incident.
* **Incident Overview** - Provides a summary of key information like milestones, description, customer impact, impacted components, responders, and more.
* **Contributing Factors** - These items are seen as having led to the incident or the "causes." Many of our customers do their "5 Whys" analysis here and also note any other factors that could have contributed to starting this incident.
* **Lessons Learned** - These are the review questions. FireHydrant ships with default questions, customized according to your organization's needs.
* **Tasks** - This is the same Tasks tab shown in the Command Center. Here, you can review all open/closed Tasks and Follow-Ups.
* **Change Events**- FireHydrant can ingest change events in your repositories or infrastructure and automatically associate them with incidents based on which components were impacted. You can then mark them as the cause of an incident or dismiss them.

Once you've completed the Retrospective, click **Publish** at the top right, which will transition the incident to the final milestone: **Retrospective Completed**. This will also generate a PDF report of the retrospective, and if your organization has these Runbook steps configured, will also export the report to Google Docs and Confluence.

### Additional Resources

* [Conducting Retrospectives](https://docs.firehydrant.com/docs/conducting-retrospectives)
* [Retro Collaboration](https://docs.firehydrant.com/docs/retro-collaboration)

***

## Reviewing Analytics

<Image alt="Example Analytics graphs" align="center" src="https://files.readme.io/98b1104-analytics.png">
  Example Analytics graphs
</Image>

Once you've completed the retrospective, head over to the analytics section of the FireHydrant UI to see what types of metrics we track. All of the graphs can be exported to CSV or PNG formats for easy insertion into a report, and all data is accessible via API as well.

### Additional Resources

* [Analytics Basics](https://docs.firehydrant.com/docs/analytics-basics)
* [CSV Data Export](https://docs.firehydrant.com/docs/csv-data-export)
* [FireHydrant API Docs](https://developers.firehydrant.com/#/)

***

## Wrapping Up & Next Steps

Now that you've seen how to conduct incidents in Microsoft Teams, check out the [Web UI Responder Guide](https://docs.firehydrant.com/docs/web-ui-responder-guide) to see how you can continue to reliably manage your incidents even if your chat app is not available

These guides only cover the basics of conducting incidents on FireHydrant. For more guides, see the docs sections on the left:

* **Incidents** section has in-depth guides for every piece of incident management and platform configuration
* **Runbooks** section contains details about Runbooks and how to automate and tailor your processes
* **Analytics** covers our Analytics capabilities in-depth
* **Catalog** contains documentation on our Service Catalog and how to set up and use it for more effective incident management
* **Status Pages** discusses FireHydrant's proprietary status pages. You can also integration FireHydrant with [Atlassian Statuspage](https://docs.firehydrant.com/docs/atlassian-statuspage-integration)
* **Integrations** section covers all of the available integrations FireHydrant has
* **Administration** covers general account, user, and team configurations
* **Reference** contains quick-reference documentation that users may find themselves visiting time to time again.

If you have any questions or concerns, [reach out to the Support team](https://firehydrant.zendesk.com/hc/en-us/requests/new) or your FireHydrant Account team if you're working with one.