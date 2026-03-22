# Source: https://docs.rootly.com/incidents/managing-incidents/updating-incident-integration-links.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Updating Incident Integration Links

> Learn how to view, edit, and update external integration links for incidents through both the Rootly web interface and Slack.

### Overview

Many incidents rely on external systems—ticketing tools, documentation platforms, notebooks, meeting links, and on-call providers.\
Rootly centralizes these external references by allowing teams to store and update integration links directly on the incident.

These links may be:

* Automatically created by integrations
* Generated through workflows
* Manually added or corrected by responders

You can update integration links through both the Rootly web interface and the Rootly Slack bot.

<Info>
  The list of editable links depends on which integrations your workspace has enabled. Only integrations your team has configured will appear in the editor.
</Info>

***

### Editing Integration Links via the Web UI

<Steps>
  <Step title="Open the Incident">
    Navigate to the incident whose integration links you want to modify.
  </Step>

  <Step title="Open the Edit Integrations Dialog">
    In the **Integrations** section of the incident page, click **Edit Integrations**.

    This opens a modal listing all editable integration link fields—for example, Jira, Asana, PagerDuty, Google Drive, Zoom, Confluence, and others.

    <Frame>
            <img src="https://mintcdn.com/rootly/7ojKISea6oiQMk0o/images/updating-incident-links/1.webp?fit=max&auto=format&n=7ojKISea6oiQMk0o&q=85&s=3fea0a3a0bda85e6ef1501479e4664a4" alt="Edit integration dialog screenshot" width="899" height="559" data-path="images/updating-incident-links/1.webp" />
    </Frame>
  </Step>

  <Step title="Update or Clear Links">
    Each field represents an external system link. You may:

    * Replace an existing URL
    * Add a missing link
    * Leave the field blank to remove it

    All links require a valid URL format.

    <Frame>
            <img src="https://mintcdn.com/rootly/JFQ1ZeVNi4nNRKF5/images/updating-incident-links/2.webp?fit=max&auto=format&n=JFQ1ZeVNi4nNRKF5&q=85&s=8f9779df55dd661503a8bdb19fa9b4c0" alt="Integration link input view" width="900" height="640" data-path="images/updating-incident-links/2.webp" />
    </Frame>
  </Step>

  <Step title="Save Changes">
    Click **Update** to apply your changes.

    Your updated links will immediately appear in the Integrations section of the incident.
  </Step>
</Steps>

<Tip>
  Use the web interface when updating multiple links at once or when cleaning up links after workflows or automations.
</Tip>

***

### Editing Integration Links via Slack

You can also update integration links without leaving Slack.\
This is useful during active response when responders are working primarily in the incident channel.

There are two ways to open the integration editor in Slack.

***

#### Option 1: Use the Pinned Incident Overview

When viewing an incident channel, the pinned incident summary includes an **Integrations** section with an **Edit** button.

Clicking **Edit** opens the same integration editor modal used in the web interface.

<Frame>
    <img src="https://mintcdn.com/rootly/JFQ1ZeVNi4nNRKF5/images/updating-incident-links/3.webp?fit=max&auto=format&n=JFQ1ZeVNi4nNRKF5&q=85&s=8d111adfff79c555589a9498f1aa97f6" alt="Slack pinned overview integration edit" width="902" height="710" data-path="images/updating-incident-links/3.webp" />
</Frame>

***

#### Option 2: Use the Slash Command

You can also open the integration editor by typing:

<Code>
  /incident integration
</Code>

inside the incident channel.

Rootly will open a modal where you can update any of the available integration links.

<Frame>
    <img src="https://mintcdn.com/rootly/JFQ1ZeVNi4nNRKF5/images/updating-incident-links/4.webp?fit=max&auto=format&n=JFQ1ZeVNi4nNRKF5&q=85&s=65a2e61b7aafe4e7c54e5bf7c75190fe" alt="Slack integration modal screenshot" width="901" height="603" data-path="images/updating-incident-links/4.webp" />
</Frame>

<Info>
  Slack commands must be run inside the **incident channel**.\
  Rootly identifies the incident based on the channel ID.
</Info>

***

### Which Integrations Can Be Edited?

The integrations editor displays only the links that apply to the integrations your team has enabled.\
Common examples include:

* Jira
* Asana
* PagerDuty
* ServiceNow
* Zendesk
* GitHub
* Linear
* Confluence
* Google Drive / Google Docs / Google Meet / Google Calendar
* Zoom / Webex / GoToMeeting
* Trello
* Notion
* Shortcut
* Coda
* Airtable
* Datadog Notebook

<Tip>
  If an integration is installed but a link was not automatically created, you can manually add it here.
</Tip>

***

### Troubleshooting

<AccordionGroup>
  <Accordion title="I don’t see any fields in the integrations editor">
    Your workspace may not have any integrations enabled for this incident type.\
    Only integrations your team has configured will appear.
  </Accordion>

  <Accordion title="The Slack command didn’t work">
    Make sure you are running the command **inside the incident channel**.\
    Commands sent from other channels or DMs cannot be mapped to an incident.
  </Accordion>

  <Accordion title="I can’t save my changes">
    Integration links must be valid URLs.\
    Invalid or improperly formatted URLs will cause a validation error.
  </Accordion>

  <Accordion title="I don’t see an Edit button in Slack or on the web">
    You may not have permission to update incidents.\
    Check your incident role or workspace access settings.
  </Accordion>

  <Accordion title="Some integrations I expected are missing">
    Only integrations with active workspace configuration appear.\
    Ensure the integration is fully set up under **Configuration → Integrations**.
  </Accordion>
</AccordionGroup>

***

### Best Practices

* **Use workflows to automatically generate links**\
  For example, create Jira issues or PagerDuty incidents automatically and populate the link fields.

* **Maintain consistency across incident types**\
  Standardizing where each system’s link is stored makes retrospectives and auditing much easier.

* **Remove outdated or incorrect links**\
  Leaving fields blank clears stale or incorrect values to avoid confusion later.

* **Encourage responders to update links early**\
  Accurate integration links ensure the right systems stay connected throughout the lifecycle.

* **Use Slack for quick updates, Web UI for bulk editing**\
  Slack is ideal during active response; the web interface is better for comprehensive cleanup.


Built with [Mintlify](https://mintlify.com).