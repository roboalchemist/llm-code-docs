# Source: https://docs.rootly.com/incidents/incident-lifecycle.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Incident Lifecycle

> Learn how Rootly represents and tracks each stage of an incident, from early triage through final closure. Each phase is represented by an incident status, and Rootly automatically records timestamps and data values as incidents progress through the lifecycle.

### Overview

Rootly models every incident using a sequence of lifecycle stages that reflect how teams actually discover, assess, respond to, and close out operational issues. Each stage corresponds to an **incident status**, and Rootly automatically records timestamps as incidents progress. These statuses power automation, analytics, retrospectives, and help teams maintain a clean, consistent operational process.

<Info>
  Each lifecycle transition can be made from the web UI or via Slack commands such as `/rootly mitigate`, `/rootly resolve`, and `/rootly cancel`. Rootly automatically records the appropriate timestamp with every status change.
</Info>

### Triage

Incidents frequently begin with incomplete or ambiguous signals.\
The **Triage** status is designed for these early situations where something may be wrong, but responders are not yet certain. Entering Triage keeps notifications limited so teams can investigate without alarming broader stakeholders.

**How to enter Triage:**

* When creating an incident, select the **Mark as In Triage** checkbox
* Or update the status from Slack or the web UI

**Data value:** `in_triage`\
**Timestamp:** `in_triage_at` (only recorded if the incident actually enters Triage)

<Frame>
    <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/incidents/1.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=f81c5e0ccacf6bb12a1784710a8b8874" alt="Document image" width="916" height="1101" data-path="images/incidents/1.webp" />
</Frame>

<Tip>
  Triage helps contain blast radius and ensures only key responders are involved before an issue is fully confirmed.
</Tip>

### Started

Once responders confirm the issue is real, the incident progresses to the **Started** status. This is the point where coordinated response begins—roles are assigned, communication channels open, and early hypotheses are formed.

**How to enter Started:**

* Leave **Mark as In Triage** **unchecked** during incident creation
* Or move from Triage → Started in the UI or via Slack

**Data value:** `started`\
**Timestamp:** `started_at`

<Frame>
    <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/incidents/2.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=f87a2d39744cd7eb3ed5ae7c79321c20" alt="Document image" width="917" height="1137" data-path="images/incidents/2.webp" />
</Frame>

<Check>
  If you skip Triage during creation, Rootly sets the incident directly to Started.
</Check>

### Detected *(Optional)*

Some teams track the moment an issue was first **noticed**, separate from when response formally began.

**Data value:** `detected`\
**Timestamp:** `detected_at`

<Info>
  Captured detection time supports metrics like MTTD (Mean Time To Detect).
</Info>

### Acknowledged *(Optional)*

Acknowledgement indicates a specific responder has taken ownership, which pauses escalations and clarifies responsibility even before major status transitions occur.

**Data value:** `acknowledged`\
**Timestamp:** `acknowledged_at`

### Mitigated

An incident becomes **Mitigated** when the immediate impact has been contained. Users may still be affected, but the issue is no longer actively worsening. This is common when temporary fixes, failovers, or emergency controls are applied.

**How to enter Mitigated:**

* Use the **Mitigate** button
* Or run `/rootly mitigate` in Slack

**Data value:** `mitigated`\
**Timestamp:** `mitigated_at`

<Frame>
    <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/incidents/3.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=9f66d84f1dc18ff77e83ef0f467b20ca" alt="Document image" width="899" height="459" data-path="images/incidents/3.webp" />
</Frame>

<Tip>
  If the incident moves straight to Resolved without entering Mitigated, Rootly automatically sets `mitigated_at` equal to `resolved_at` so analytics remain accurate.
</Tip>

### Resolved

An incident is **Resolved** when the underlying issue has been fixed and service impact is no longer present.\
This moment typically triggers stakeholder updates and begins the retrospective process.

**How to enter Resolved:**

* Click **Resolve**
* Or run `/rootly resolve` in Slack

**Data value:** `resolved`\
**Timestamp:** `resolved_at`

<Frame>
    <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/incidents/4.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=86bb23281e8e9c5cc7701166f5b3bcb0" alt="Document image" width="902" height="470" data-path="images/incidents/4.webp" />
</Frame>

<Check>
  Many teams configure workflows that automatically generate a Retrospective when an incident reaches Resolved.
</Check>

### Closed

While **Resolved** means “the system is fixed,” **Closed** means “all follow-up work is complete.”\
This includes finishing retrospectives, verifying action items, and closing out communications.

**Data value:** `closed`\
**Timestamp:** `closed_at`

<Info>
  Use Closed to separate **technical completion** from **process completion**.
</Info>

### Cancelled

A **Cancelled** incident represents a false positive or the identification of a duplicate.\
It prevents unnecessary responder work and keeps analytics clean.

**How to enter Cancelled:**

* Use the **Cancel Incident** button
* Or run `/rootly cancel`
* **Available only when the incident is in Triage**

**Data value:** `cancelled`\
**Timestamp:** `cancelled_at`

<Frame>
    <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/incidents/5.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=a68f54fb480899f743dae393ca66c797" alt="Document image" width="902" height="475" data-path="images/incidents/5.webp" />
</Frame>

<Warning>
  Cancelled incidents do not continue through the lifecycle. Only cancel when the event is truly non-actionable or duplicated.
</Warning>

### Planned Maintenance *(Optional)*

Rootly can model planned or controlled [operational work.](https://rootly.com/changelog/planned-maintenance-made-easier)\
Scheduled incident lifecycle values include:

* **planning** — defining scope
* **scheduled** — approved window (`scheduled_for`, `scheduled_until`)
* **in\_progress** — work underway
* **completed** — work finished
* **verifying** — final checks

This allows scheduled maintenance to be tracked with the same rigor as unplanned incidents.

### Timeline

Every incident includes a **Timeline**, which organizes all key moments—status changes, role assignments, workflow actions, Slack updates, alerts, and manual entries—into a coherent narrative.

<Tip>
  Timeline entries can be added via Slack, the Rootly web UI, email-to-incident, or automations. This makes retrospectives dramatically easier.
</Tip>

### Status Overview

| Status         | Data Value     |  Timestamp Field  |
| :------------- | :------------- | :---------------: |
| Triage         | `in_triage`    |   `in_triage_at`  |
| Started        | `started`      |    `started_at`   |
| Detected\*     | `detected`     |   `detected_at`   |
| Acknowledged\* | `acknowledged` | `acknowledged_at` |
| Mitigated      | `mitigated`    |   `mitigated_at`  |
| Resolved       | `resolved`     |   `resolved_at`   |
| Closed         | `closed`       |    `closed_at`    |
| Cancelled      | `cancelled`    |   `cancelled_at`  |

\*Optional depending on workflow usage.

### FAQ

<AccordionGroup>
  <Accordion title="What status should I use when I'm not sure an issue is an incident yet?">
    Use **Triage**. It limits notifications and keeps early investigation to a small responder group.\
    Use **Started** only once you are confident the issue is real.
  </Accordion>

  <Accordion title="Can I start an incident directly in the Started status?">
    Yes. If you leave **Mark as In Triage** **unchecked** during creation, Rootly will set the incident directly to **Started**.
  </Accordion>

  <Accordion title="Do I have to use Mitigated?">
    No. Mitigated is optional, but recommended. If you skip it and go straight to **Resolved**, Rootly will automatically set `mitigated_at = resolved_at` to preserve accurate analytics.
  </Accordion>

  <Accordion title="What is the difference between Resolved and Closed?">
    * **Resolved** = the technical issue is fixed
    * **Closed** = all follow-up work (retrospectives, action items, communication, cleanup) is complete

    Teams often resolve incidents quickly but close them later.
  </Accordion>

  <Accordion title="Can I add custom lifecycle statuses?">
    Yes—Rootly supports additional operational statuses such as **Detected**, **Acknowledged**, and **Scheduled Maintenance** states (`planning`, `scheduled`, `in_progress`, etc.). These are optional and configurable based on your workflow.
  </Accordion>

  <Accordion title="Where should I track follow-up actions?">
    Use **Action Items** or attach tasks directly from the incident.\
    Once these are complete, set the incident to **Closed**.
  </Accordion>
</AccordionGroup>

|   |
| - |


Built with [Mintlify](https://mintlify.com).