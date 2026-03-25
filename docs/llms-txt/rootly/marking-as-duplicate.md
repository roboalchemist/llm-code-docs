# Source: https://docs.rootly.com/incidents/incident-operations/marking-as-duplicate.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Marking Incidents as Duplicate

> Understand how to mark incidents as duplicates, consolidate response efforts, and maintain clear relationships between canonical and duplicate incidents across the web and Slack.

### How Duplicate Incidents Work

During fast-moving operational issues, teams may accidentally create multiple incidents describing the same underlying problem. Rootly allows you to **mark one incident as the duplicate of another**, ensuring responders align around a single source of truth.

When an incident is marked as a duplicate:

* The *duplicate* incident is linked to a *canonical* (primary) incident
* The duplicate’s timeline records the change
* Workflows, alerts, and Slack channels can consolidate under the primary incident
* Optionally, the duplicate incident can be automatically **cancelled**

This helps reduce fragmentation, avoid duplicate work, and maintain accurate historical records.

<Info>
  Duplicate incidents use a dedicated field (`duplicate_incident_id`) and are **not** the same as sub-incidents, which use `parent_incident_id`.
</Info>

***

### Why Mark Incidents as Duplicate

Teams benefit from merging duplicates because it:

* Ensures responders focus on the correct incident
* Reduces conflicting updates or duplicated communication
* Clarifies ownership and priority
* Simplifies retrospectives and reporting
* Maintains a clean incident list without losing context

Typical scenarios include:

* Multiple teams declare the same outage simultaneously
* Monitoring tools trigger multiple detection paths
* Slack responders create overlapping incidents during triage

***

### What Happens When You Mark an Incident as Duplicate

When you mark Incident A as a duplicate of Incident B:

* Incident A becomes linked to Incident B
* A timeline entry is added to Incident A
* Slack responders receive a confirmation message
* (Optional) Incident A is automatically **cancelled** and any attached alerts are resolved
* The “Duplicate of …” banner appears in the duplicate incident UI

This ensures full transparency on how and why incidents were consolidated.

<Info>
  Auto-cancellation is enabled by default when marking a duplicate but can be turned off during the action.
</Info>

***

### Where You Can Manage Duplicates

#### **In the Web Interface**

From an incident, open the action menu and select **Mark as Duplicate**.\
You can then:

* Search for the canonical incident
* Choose whether to auto-cancel the duplicate
* Add a cancellation reason for context

A redirect takes you to the canonical incident after completion.

[Learn how to mark duplicates via Web →](/incidents/incident-operations/web-marking-as-duplicate)

***

#### **In Slack**

Use one of the supported commands:

* **`/rootly dup`**
* **`/rootly duplicate`**

This opens a modal where you can:

* Select the canonical incident
* Provide a cancellation reason
* Enable/disable auto-cancel

Slack posts a confirmation message to the duplicate’s channel when completed.

<Info>
  Duplicate marking is not available for scheduled maintenance incidents.
</Info>

[Learn how to mark duplicates via Slack →](/incidents/incident-operations/slack-marking-as-duplicate)

***

### API Support

You can also mark incidents as duplicates programmatically using:

```
POST /api/v1/incidents/:id/duplicate
```

Supported attributes include:

* `duplicate_incident_id`
* `auto_cancel_incident`
* `reason_for_cancellation`

Rootly updates the relationship and adds a timeline entry automatically.

<Info>
  API duplicate linking does not automatically resolve attached alerts—this behavior is only available via Slack or Web.
</Info>

***

### Best Practices

* **Always consolidate early**\
  Merge duplicate incidents as soon as duplication is detected to reduce confusion.

* **Use auto-cancel thoughtfully**\
  Cancelling duplicates keeps your incident list clean, but you may leave them open temporarily during complex triage.

* **Write clear cancellation reasons**\
  Adds helpful context for retrospectives and audit history.

* **Educate responders on Slack commands**\
  Many duplicates are resolved faster when responders use `/rootly dup`.

* **Review duplicate patterns**\
  Repeated duplicates may highlight monitoring or workflow tuning opportunities.

***

### FAQ

<AccordionGroup>
  <Accordion title="What is the difference between a duplicate and a sub-incident?">
    Duplicate incidents refer to the **same problem**, while sub-incidents represent **related but distinct workstreams**.
  </Accordion>

  <Accordion title="Can a duplicate be re-opened as a normal incident?">
    Yes. Edit the incident to remove the duplicate relationship and update the status.
  </Accordion>

  <Accordion title="Can I mark an incident as duplicate of a private incident?">
    Yes, but only if you have permission to view the target incident.
  </Accordion>

  <Accordion title="Who can mark incidents as duplicates?">
    Any responder with **update** permission on the incident (including private-incident permissions when relevant).
  </Accordion>

  <Accordion title="Does marking as duplicate merge timelines?">
    No. Timelines remain separate, but all future response activity should occur in the canonical incident.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).