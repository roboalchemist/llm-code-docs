# Source: https://docs.rootly.com/incidents/incident-operations/web-marking-as-duplicate.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Marking Incidents as Duplicate via Web Interface

> Learn how to mark incidents as duplicates in the Rootly web interface, including selecting the primary incident and optional auto-cancellation.

Marking an incident as a duplicate helps consolidate response efforts when multiple responders report the same issue. The Web UI provides a simple modal to link the current incident to its canonical incident and optionally auto-cancel it.

<Info>
  Duplicate incidents use a dedicated **duplicate\_incident\_id** relationship and are separate from sub-incidents, which use **parent\_incident\_id**.
</Info>

***

## Mark a Duplicate via the Web UI

<Steps>
  <Step title="Step 1 — Open the duplicate dialog">
    In the top-right corner of the incident page, click the **⋯** menu and select **Mark as Duplicate**.

    <Frame>
            <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/incidents/markasduplicate2.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=ac5449ba02e9eed8d27550f84763e99c" alt="Open the Mark as Duplicate action" width="400" height="345" data-path="images/incidents/markasduplicate2.webp" />
    </Frame>

    <Info>
      This option appears only when the incident is not already a duplicate and you have permission to update the incident.
    </Info>
  </Step>

  <Step title="Step 2 — Choose the original incident">
    In the modal, search for and select the **original (canonical)** incident.\
    This is the incident the current one will be linked to.

    You can also:

    * **Auto-cancel** the duplicate (enabled by default)
    * Provide a **reason for cancellation**, which appears in the timeline

    <Frame>
            <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/incidents/markasduplicate3.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=24ca79b21e5c086a0f7fbcb6ef1c29dd" alt="Duplicate modal with incident selector and auto-cancel toggle" width="592" height="466" data-path="images/incidents/markasduplicate3.webp" />
    </Frame>
  </Step>

  <Step title="Step 3 — Confirm the action">
    Click **Confirm** to save your changes.

    Rootly will:

    * Link the incident as a duplicate
    * Add a timeline entry
    * Post a notification to the duplicate’s Slack channel (if Slack is connected)
    * Cancel the duplicate (if enabled)
    * Redirect you to the original incident
  </Step>
</Steps>

***

## What Happens After Marking a Duplicate

* The duplicate incident displays **“Duplicate of …”** at the top of the page
* A non-editable timeline entry records who performed the action and why
* Auto-cancel will:
  * Move the incident to **Cancelled**
  * Resolve all attached alerts automatically
* Slack responders are notified if the Slack integration is active

<Info>
  Auto-cancel is recommended to reduce noise in reports and Slack channels, but you may disable it when the duplicate incident still contains useful investigation context.
</Info>

***

## Best Practices

* **Use “Mark as Duplicate” early**\
  Consolidating incidents right away helps reduce confusion across teams and channels.

* **Always designate a canonical incident**\
  The canonical incident should contain the most accurate timeline and central communication thread.

* **Provide a clear cancellation reason**\
  This helps responders understand why context moved and ensures retrospectives remain accurate.

* **Auto-cancel duplicate incidents when appropriate**\
  This prevents “ghost incidents” from appearing unresolved in dashboards or workflow triggers.

* **Avoid marking scheduled maintenance incidents as duplicates**\
  Maintenance windows follow different lifecycle logic and should remain separate.

* **Review duplicate frequency**\
  Frequent duplicates may indicate alerting issues, unclear runbooks, or multiple teams raising incidents for the same symptom.

***

## Troubleshooting

<AccordionGroup>
  <Accordion title="I don't see the 'Mark as Duplicate' option">
    * You may not have **update permission** for the incident.
    * The incident may already be marked as a duplicate.
    * Scheduled maintenance incidents cannot be marked as duplicates.
  </Accordion>

  <Accordion title="The original incident doesn't appear in the selector">
    * The incident you're looking for may be private and you may not have permission to view it.
    * The selector excludes the current incident automatically.
    * Try searching by title or ID.
  </Accordion>

  <Accordion title="The duplicate did not auto-cancel">
    * The auto-cancel toggle may have been turned off.
    * The incident may have already been cancelled.
    * Workflow restrictions or permissions may prevent auto-cancel in rare cases.
  </Accordion>

  <Accordion title="Slack did not post a confirmation message">
    * Slack may not be integrated for your team.
    * The duplicate incident may not have a Slack channel.
    * Notification settings may restrict posting confirmations.
  </Accordion>

  <Accordion title="My dashboards still show both incidents">
    Auto-cancel removes the duplicate from most active incident metrics.\
    If auto-cancel was disabled, manually cancel or close the duplicate to prevent clutter.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).