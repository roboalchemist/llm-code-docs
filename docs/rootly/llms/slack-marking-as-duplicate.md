# Source: https://docs.rootly.com/incidents/incident-operations/slack-marking-as-duplicate.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Marking Incidents as Duplicate via Slack

> Learn how to mark incidents as duplicates directly from Slack incident channels using the /rootly dup command.

You can mark an incident as a duplicate directly from Slack using a simple slash command. This helps consolidate related incidents quickly and keep responders aligned in a single source of truth.

<Info>
  This operation links the current incident to a **canonical incident** via `duplicate_incident_id`.\
  This is separate from **sub-incidents**, which use `parent_incident_id`.
</Info>

***

## Mark a Duplicate in Slack

In any **incident Slack channel**, type:

```
/rootly dup
```

or

```
/rootly duplicate
```

<Frame>
    <img src="https://mintcdn.com/rootly/ljLqQxzWDg3HgLpA/images/marking-as-duplicate/slack.webp?fit=max&auto=format&n=ljLqQxzWDg3HgLpA&q=85&s=64504603b588daff2a1dc3c772e40923" alt="Slack duplicate modal" width="912" height="815" data-path="images/marking-as-duplicate/slack.webp" />
</Frame>

A modal opens allowing you to select the original incident and configure cancellation options.

***

## Modal Fields

The Slack modal includes:

* **Assign to Incident** — search for the canonical incident
* **Auto Cancel Current Incident** — optional toggle (on by default)
* **Summary (reason for cancellation)** — optional free text, added to the timeline

<Info>
  Slack enforces the same permissions as the web interface.\
  You must be able to **update** the incident to mark it as a duplicate.
</Info>

***

## What Happens After Submission

When you confirm the duplicate:

* The current incident is linked to the selected original incident
* A non-editable **timeline entry** is created
* Slack posts a confirmation message in the duplicate’s channel (if applicable)
* If **Auto Cancel** is enabled:
  * The duplicate is cancelled
  * Alerts attached to the duplicate are resolved automatically
  * Slack posts a “Duplicate incident detected” message

<Info>
  Rootly also updates Slack summaries and workflows that rely on incident lifecycle changes.
</Info>

***

## Best Practices

* **Run the command from the incident channel**\
  Slack automatically associates the action with the incident the channel is tied to.

* **Use the canonical incident with the most context**\
  Choose the incident that contains the most accurate investigation details or customer-facing messaging.

* **Provide a clear cancellation summary**\
  This helps responders understand why context moved and assists retrospectives.

* **Auto-cancel when appropriate**\
  This prevents duplicate incidents from remaining open and triggering unnecessary automations.

* **Avoid marking scheduled maintenance as duplicates**\
  Slack prevents this automatically, since maintenance incidents follow different lifecycle rules.

***

## Troubleshooting

<AccordionGroup>
  <Accordion title="“This command cannot be used here”">
    You must run `/rootly dup` inside a **Rootly incident Slack channel**.\
    The command will not work in normal or private Slack channels.
  </Accordion>

  <Accordion title="The modal does not open">
    Possible reasons:

    * You do not have **update** permissions on the incident
    * The incident is a **scheduled maintenance incident** (duplicates are disallowed)
    * The incident is **already marked as a duplicate**
  </Accordion>

  <Accordion title="The original incident doesn’t appear in the dropdown">
    Slack only shows incidents you have permission to view.\
    Private or restricted incidents may not appear unless you have the required access.
  </Accordion>

  <Accordion title="The incident did not auto-cancel">
    Common causes:

    * Auto-cancel was toggled **off**
    * The incident was already cancelled
    * Slack permissions prevented cancellation
    * Workflow or feature flags restricting cancellation were active
  </Accordion>

  <Accordion title="Slack did not post a confirmation message">
    This can occur when:

    * Slack is not integrated or connected for your team
    * The duplicate incident has **no Slack channel**
    * Notifications are suppressed by workspace settings
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).