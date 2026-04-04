# Source: https://docs.rootly.com/incidents/incident-timeline/incident-timeline.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Incident Timeline Overview

> Understand how Rootly incident timelines capture key events, decisions, and system signals throughout the incident lifecycle.

### How Timelines Work

The incident timeline is the **authoritative record of what happened during an incident**. It brings together updates from people, systems, automations, and communication channels into one clear, chronological narrative.

Timelines help responders stay aligned during active incidents and make retrospectives far more accurate by capturing everything in one place.

This page introduces how timelines work, why they matter, and how they fit across the incident lifecycle.

***

### Why Timelines Matter

A well-maintained timeline supports every phase of the incident lifecycle. Timelines help teams:

* Build a shared understanding of what is happening
* Avoid losing critical context in Slack threads or meetings
* Track decisions and actions across engineering, support, and comms
* Maintain a consistent audit trail for compliance and reporting
* Strengthen retrospectives with accurate, timestamped history
* Align stakeholders with clear, trustworthy incident narratives

Rootly automatically logs many events, and responders can contribute additional context from wherever they work—Slack, email, the web UI, or automation.

<Info>
  Timelines ensure the full story of an incident is captured, even when many responders contribute different pieces of information.
</Info>

***

### What Appears in the Timeline

Timelines combine both **human-generated** and **system-generated** events.

Examples include:

* Status transitions (Triage → Mitigated → Resolved)
* Role assignments or reassignments
* Slack messages captured as timeline events
* Email replies
* Attachments or uploaded files
* Alert updates or linked monitoring signals
* Workflow-triggered actions
* Decisions, notes, and investigative steps
* System events such as channel membership changes

Each event includes:

* Event text or description
* Who performed the action (person or system)
* Timestamp of occurrence
* Source (Slack, Web, Email, API, etc.)
* Optional attachments
* Optional affected services/functionality
* Optional visibility (internal vs. external)

***

### Where Timelines Appear in Rootly

#### **On the Incident Detail Page (Web UI)**

The timeline appears as a chronological feed where responders can read, filter, star, export, and contribute events.

Responders can:

* Add structured events
* Upload attachments
* Adjust timestamps
* Star critical entries
* Filter system vs. responder events
* Export the timeline for reporting or retrospectives

#### **In Slack**

If Slack is integrated, responders can:

* Add events using modals
* Convert Slack messages into timeline events
* React to workflow prompts to supply investigation notes
* View system updates reflected in the timeline

This makes it easy to contribute during real-time response, when most work happens in chat.

#### **Via Email**

Replies to an incident email thread automatically appear in the timeline.\
This allows cross-functional teams (customer support, success, leadership) to contribute context from their preferred communication channel.

#### **Via API**

Engineering and SRE teams can integrate CI/CD systems, automated diagnostics, monitoring tools, or runbooks to create timeline entries programmatically.

***

### How Timelines Support the Response Process

Timelines are deeply connected to how Rootly orchestrates incident response:

* Retrospectives pull directly from timeline events
* Status changes, assignments, and communications are logged automatically
* Workflows rely on structured events for decision logic
* External timelines (if enabled) use timeline visibility settings
* Investigation notes help later teams onboard quickly
* Incident analytics leverage timeline data for MTTx measurements

<Info>
  High-quality timeline entries improve clarity during response and dramatically increase the usefulness of retrospectives afterward.
</Info>

***

### Where to Go Next

These pages explain how to add events through each method:

* **Add Events via Slack** – Capture notes, message actions, attachments, and updates
* **Add Events via Web Interface** – Use structured fields to record detailed events
* **Add Events via Email** – Ensure email replies are logged in the timeline
* **Add Events via API** – Automate system-generated timeline entries

***

### Best Practices

* **Capture important decisions explicitly**\
  Don’t rely on Slack threads—add events that explain key choices or pivots.

* **Add investigation updates as they happen**\
  Even brief notes improve clarity for downstream responders and retrospectives.

* **Use visibility settings intentionally**\
  Internal vs. external timeline events should align with your communication guidelines.

* **Star key milestones**\
  Highlight major actions like mitigations, rollbacks, or customer updates.

* **Automate system signals**\
  Use the API or workflows to consistently record deployments, alerts, or diagnostics.

* **Review the timeline during retrospectives**\
  The timeline often surfaces root causes, delayed decisions, or communication gaps.

***

### FAQ

<AccordionGroup>
  <Accordion title="Do I need to manually maintain the timeline?" iconType="thin">
    No. Rootly logs many events automatically—status changes, alerts, workflow actions, role updates, and Slack channel events.\
    Responders simply add additional context as needed.
  </Accordion>

  <Accordion title="Why is my event out of order?">
    Timeline ordering is based on the **occurred\_at** timestamp.\
    If you adjust timestamps or add events retroactively, the position may shift.
  </Accordion>

  <Accordion title="Do Slack messages automatically become timeline events?">
    Only when captured intentionally—either using the event modal, message actions, or configured workflows.\
    Regular Slack messages are not automatically converted.
  </Accordion>

  <Accordion title="Can we hide internal-only notes from external audiences?">
    Yes. Timeline events can be marked **internal** or **external**.\
    Only external events appear on public or customer-facing timelines.
  </Accordion>

  <Accordion title="Can system-generated events be hidden?">
    Yes. You can toggle system events on/off in the timeline view to reduce noise.
  </Accordion>

  <Accordion title="How can I export the full timeline?">
    The Web UI includes an **Export Timeline** option, allowing you to download timeline data for retrospectives, compliance, or reporting.
  </Accordion>

  <Accordion title="Can automated tools send events to the timeline?">
    Yes. Using the Rootly API, workflows, or integrations, systems can add structured timeline events programmatically.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).