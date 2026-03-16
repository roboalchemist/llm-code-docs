# Source: https://docs.rootly.com/on-call/on-call.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Started

> Understand how Rootly On-Call ensures the right people are paged at the right time using schedules, escalation policies, and real-time routing.

## What Is Rootly On-Call?

Rootly On-Call is the decision engine that determines who should respond, how urgently, and through which channels when something requires immediate attention.\
It brings together all the components required for reliable paging—**schedules**, **escalation policies**, **notification rules**, **live call routing**, and **health checks**—and applies them consistently across alerts, incidents, phone calls, and automations.

Rootly’s goal is simple:  **Every critical signal reaches the right human, right away, with zero manual coordination.**

To achieve this, On-Call unifies:

* **On-Call Schedules** — define coverage, rotations, and business-hour logic
* **Escalation Policies** — define how Rootly escalates until someone responds
* **Notification Channels** — voice, SMS, Slack, email, push, with urgency-aware delivery
* **Live Call Routing** — turn a phone call into a page or live connection
* **Heartbeats** — detect system failures proactively
* **Urgency Rules** — ensure critical alerts bypass delays and DND

<Check>
  If alerts are the *signal*, On-Call is the *routing system* that ensures the signal always reaches a human responder—reliably and consistently.
</Check>

***

### Why It Matters

A robust on-call program is foundational to operational reliability. It’s the safety net that ensures issues are detected early, routed correctly, and acted on quickly—no matter when they occur or who is available. Rootly On-Call centralizes this responsibility by coordinating schedules, escalation logic, and notification channels so teams never have to wonder who should respond or how alerts should flow. It eliminates guesswork, reduces manual coordination, and brings consistency to the moments where clarity matters most. Rootly On-Call ensures:

#### **Fast, accurate detection**

Monitoring tools send alerts → Rootly immediately routes them to the correct responder based on urgency and routing rules.

#### **Predictable coverage**

Schedules define who is responsible at any moment—across time zones, rotations, and business hours.

#### **Reliable escalation**

If a responder does not acknowledge in time, Rootly automatically escalates until someone does—no pager fatigue, no dropped alerts.

#### **Multi-channel delivery**

Rootly intelligently chooses notification channels based on urgency, fallback logic, user preferences, and device availability.

#### **Consistent workflow integration**

All paging activity flows naturally into Incident Management, Workflows, Analytics, and communication channels like Slack.

***

### Key Components of On-Call

#### **1. Schedules**

Schedules define **who is on duty right now**. They support:

* Multi-person rotations
* Layered coverage (primary / secondary)
* Business-hour–only schedules
* Time-zone–aware planning
* Slack usergroup auto-updates
* Shift overrides and handoff workflows

Schedules provide the “real-time roster” that escalation policies use when selecting responders.

#### **2. Escalation Policies**

Escalation Policies define **how Rootly should escalate if no one responds**.

They support:

* Multiple sequential levels
* Paging Users, Groups (Teams), Services, or Schedules
* Working-hours logic (different paths for after-hours alerts)
* Custom repeat rules
* Dynamic escalation paths filtered by alert urgency or alert content

Escalation Policies guarantee alerts do not stall on a single unresponsive user.

#### **3. Notification Channels**

Rootly uses multiple channels to maximize responder reach:

* Phone calls (with DND override for critical alerts)
* SMS with retry logic
* Push notifications from the mobile app
* Slack notifications
* Email

Rootly automatically handles fallbacks, retries, and acknowledgement tracking.

#### **4. Live Call Routing**

Allows employees, customers, or automated systems to trigger a page via phone call.

Capabilities include:

* Live connection to the on-call responder
* Voicemail → auto-page flow
* IVR calling trees for multi-team routing
* Per-destination urgency settings
* Failover to voicemail if unanswered
* Custom greetings and waiting music

This is the fastest way for a human caller to reach “whoever is on call right now.”

#### **5. Heartbeats**

Heartbeats ensure systems are actively reporting in.\
If a system fails to ping Rootly within the expected interval:

* A heartbeat alert is triggered
* Escalation Policies route it to the correct team
* Recovery pings automatically resolve the alert

Heartbeats reduce reliance on external uptime tools and provide first-party liveness checks.

***

### How Rootly On-Call Fits Into the Incident Workflow

1. **Monitoring detects a problem**\
   → Datadog, Grafana, Sentry, or any alert source sends a signal.

2. **On-call routing determines who to notify**\
   → Escalation Policies + Schedules identify the correct responder.

3. **Rootly notifies them through the appropriate channels**\
   → Based on user preferences, urgency, and fallback rules.

4. **Responder acknowledges**\
   → Escalation pauses; Rootly records the event.

5. **An incident is optionally created or updated**\
   → Workflows determine whether to open a new incident, attach alerts, or notify stakeholders.

<Info>
  On-Call is the bridge between *systems detecting issues* and *humans resolving them*.
</Info>

***

### Best Practices

* Keep rotation structures simple and predictable.
* Use escalation policies consistently across services.
* Set quiet vs. audible notification rules for each urgency level.
* Use business hours paths to avoid unnecessary nighttime paging.
* Pair schedules with Slack usergroups so teams always know who’s on call.
* Review unacknowledged alerts and escalation depth in On-Call Metrics.

***

### Frequently Asked Questions (FAQs)

<AccordionGroup>
  <Accordion title="What determines who gets paged?" iconType="thin">
    Rootly looks at the alert’s routing target (service, team, escalation policy) and then uses schedules + escalation rules to select the responder.
  </Accordion>

  <Accordion title="Does Rootly notify across multiple channels?">
    Yes. Rootly can send voice calls, SMS, push notifications, Slack messages, and emails—based on urgency and user preferences.
  </Accordion>

  <Accordion title="What if no one responds?">
    Rootly automatically escalates to the next level in the escalation policy until someone acknowledges.
  </Accordion>

  <Accordion title="Do we need Live Call Routing or Heartbeats?">
    They’re optional but highly recommended:

    * Live Call Routing lets callers reach on-call responders instantly
    * Heartbeats detect silent system failures proactively
  </Accordion>
</AccordionGroup>

***


Built with [Mintlify](https://mintlify.com).