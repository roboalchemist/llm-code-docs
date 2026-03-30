# Source: https://docs.rootly.com/alerts/alert-statuses.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Alert Statuses

> Understand how alerts progress through their lifecycle and how Rootly enforces valid state transitions.

### Overview

Every alert in Rootly progresses through a well-defined **finite state machine (FSM)** that dictates how it escalates, notifies responders, synchronizes with alert groups, and ultimately resolves.\
Understanding these states ensures predictable behavior across Routing, On-Call Escalation Policies, Alert Grouping, and integrations like Slack.

Rootly alerts can be in one of four statuses:

* **open**
* **triggered**
* **acknowledged**
* **resolved**

These values are stored on the alert’s canonical `status` enum. All transitions, notification triggers, and timeline events are governed by Rootly’s internal state machine.

<Frame>
  <img src="https://mintcdn.com/rootly/usuFKS3869pMrird/images/AlertStatusesFSM(1).png?fit=max&auto=format&n=usuFKS3869pMrird&q=85&s=b822f5cddb15db20f81a14f12421245d" alt="Alert Status State Machine" title="Alert Status State Machine" width="2196" height="836" data-path="images/AlertStatusesFSM(1).png" />
</Frame>

***

### Status Definitions

#### **open**

The alert has been created but **has not yet been assigned a notification target**.

Typical reasons for an `open` alert:

* The alert was ingested but did not match a Routing Rule
* The alert is a *non-paging alert*
* It was created manually without a destination

This status allows two transitions:

* `open → triggered` (once a notification target is assigned via routing or manual paging)
* `open → resolved`

<Info>
  An alert immediately transitions from **open → triggered** when Routing assigns a team, service, user, or escalation policy.
</Info>

#### **triggered**

The alert is **actively paging responders**. This is the state where on-call users are notified based on escalation logic.

A triggered alert:

* Sends notifications (SMS, push, phone call, Slack)
* Can be acknowledged by responders
* Can be resolved manually or via automation

Allowed transitions:

* `triggered → acknowledged`
* `triggered → resolved`
* `triggered → triggered` (retrigger—e.g., ack timeout, forced escalation, manual actions)

<Note>
  All transitions into `triggered` create a `status_update` timeline event.
</Note>

#### **acknowledged**

A responder confirmed that they have seen the alert and are working on it. Escalation pauses unless a timeout or retrigger occurs.

Allowed transitions:

* `acknowledged → resolved`
* `acknowledged → triggered` (ack timeout or manual retrigger)

<Info>
  If an acknowledged alert hits **acknowledgement timeout**, Rootly automatically **re-triggers** it and resumes escalation.
</Info>

#### **resolved**

A terminal state indicating no further action is required. Notifications cease and Rootly records `ended_at`.

However, Rootly allows:

* `resolved → triggered` (re-open regression, manual retrigger, new escalation)

This ensures alerts can be reopened without creating duplicates.

<Note>
  Resolved alerts remain visible and analyzable in your alert history, even after re-triggering.
</Note>

***

### Summary Table of Allowed Transitions

| From ↓           | To: triggered | To: acknowledged | To: resolved |
| ---------------- | ------------- | ---------------- | ------------ |
| **open**         | ✅             | —                | ✅            |
| **triggered**    | —             | ✅                | ✅            |
| **acknowledged** | ✅ (retrigger) | —                | ✅            |
| **resolved**     | ✅ (retrigger) | —                | —            |

<Tip>
  Retriggering is a first-class action in Rootly. A retrigger transitions an alert **back to `triggered`**, restarts escalation, and produces appropriate timeline events.
</Tip>

***

### How Rootly Records Status Changes

Every transition writes a `status_update` event into the alert timeline.

A status event includes:

* The new status
* The previous status
* Who performed the action (user or system)
* Metadata such as escalation step, ack timeout, grouping rule, or routing origin

These timeline entries power audit trails, analytics, and seamless Slack updates.

***

### Interaction With Alert Grouping

When an alert is part of an **Alert Group**, status synchronization is automatic:

#### Leader Alert Behavior

* The **group leader** is the first alert in the group (the one that paged).
* Any change to the leader’s status cascades to all members.
* Member alerts update timestamps, noise indicators, and events to match the leader.

#### Member Alert Behavior

* Members never independently influence group state.
* Status changes come exclusively from the group leader.
* Retriggering the leader retriggers all members.

<Info>
  This ensures responders never lose the true “source of paging,” even when many alerts represent the same event.
</Info>

***

### Visual Indicators Across Rootly

Rootly uses consistent color/status styling across the Web UI, Slack, and Mobile:

* 🟥 **Open / Triggered** — Requires action
* 🟧 **Acknowledged** — Someone is actively working the alert
* 🟩 **Resolved** — Incident has concluded

These indicators appear in:

* Alert lists
* Slack alert threads
* Alert details
* Incident sidebars when alerts link to incidents

***

### Timestamp Behavior

Each alert automatically manages its own lifecycle timestamps:

* **started\_at** – Set when the alert is created
* **ended\_at** – Set when transitioning into `resolved`
* **ended\_at** is cleared if later retriggered

This enables clean duration metrics (MTTA, MTTR, paging duration, escalation analytics).

***

### Troubleshooting

<AccordionGroup>
  <Accordion title="My alert is stuck in open">
    * It may not match any routing rules
    * The alert source may not be associated with an Alert Route
    * No notification target was assigned
    * The alert may be a non-paging alert
  </Accordion>

  <Accordion title="An alert never triggered escalation">
    * Ensure its status is **triggered**, not **open**
    * Validate the routing rule actually assigned a team or escalation policy
    * Confirm notification channels are enabled
    * Check for quiet-only escalation paths
  </Accordion>

  <Accordion title="Acknowledged alerts are retriggering unexpectedly">
    * Review acknowledgement timeout settings
    * Check whether escalation policies intentionally retrigger
    * Ensure grouping leader logic isn’t retriggering members
  </Accordion>

  <Accordion title="Resolved alerts are triggering again">
    This is expected if:

    * A user manually retriggered
    * The system detected a regression
    * A new routing condition matched and assigned a destination
  </Accordion>
</AccordionGroup>

***

### Summary

Alert Statuses are the backbone of Rootly’s alerting engine.

They define:

* How and when responders are notified
* How escalation policies activate
* How grouping behaves
* How alerts appear in dashboards and Slack
* How timeline events reflect real-world activity

By enforcing strict, predictable transitions—and exposing complete audit trails—Rootly ensures smooth, reliable alerting workflows from ingestion → paging → acknowledgment → resolution → retriggering if needed.


Built with [Mintlify](https://mintlify.com).