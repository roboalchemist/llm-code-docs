# Source: https://docs.rootly.com/on-call/heartbeats.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Heartbeats

> Continuously verify system health using Rootly Heartbeats and automatically trigger alerts on missed pings.

### Overview

Heartbeats allow you to monitor critical systems by requiring them to “check in” on a regular cadence.\
If a heartbeat fails to ping within the expected interval, Rootly automatically triggers an alert and notifies the appropriate on-call responders.

This ensures:

* Early detection of system failures
* Automatic paging when checks go silent
* Reliable uptime verification across services
* Zero reliance on external monitoring tools for liveness checks

<iframe width="100%" height="420" src="https://www.loom.com/embed/708aeaaa8c3448b0bda312bb769b2fce" frameborder="0" allowfullscreen title="Heartbeat Overview" />

***

### How Heartbeats Work

Each Heartbeat cycles through three statuses:

* **waiting** — newly created or recently updated; awaiting first ping
* **active** — successfully pinged and within its valid interval
* **expired** — missed its expected check-in; triggers a Heartbeat Alert

Each heartbeat is **disabled by default**. When enabled, Rootly tracks pings and expiration windows.

When a ping is received:

* `last_pinged_at` is updated
* `expires_at` is set to `now + interval`
* Status becomes **active**
* If transitioning from non-active → active, Rootly **resolves all open heartbeat alerts**

***

### Creating & Configuring Heartbeats

<Steps>
  <Step title="Step 1: Create a Heartbeat">
    Navigate to **On-Call → Heartbeats** and click **+ New Heartbeat**.

    You must configure:

    * **Name** (required, unique per team)
    * **Description** (optional)
    * **Notification Target** (required)
      * Escalation Policy
      * Service
      * Team (Group)
      * User
    * **Alert Summary** (required, 1–100 chars)
    * **Alert Urgency** (optional, recommended)
    * **Expected Ping Interval**
      * Interval: `1–300`
      * Unit: seconds, minutes, or hours

    Heartbeats start in **waiting** and **disabled** until explicitly enabled.

    <Frame>
      <img src="https://mintcdn.com/rootly/d2dmochhUzziYtkZ/images/heartbeats/1.webp?fit=max&auto=format&n=d2dmochhUzziYtkZ&q=85&s=c2b8bfef1498a6d830cc183131922de6" alt="Create Heartbeat" width="949" height="1561" data-path="images/heartbeats/1.webp" />
    </Frame>
  </Step>

  <Step title="Step 2: Enable and Activate the Heartbeat">
    Enabling a heartbeat begins the monitoring cycle. Note:

    * Changing **interval**, **interval unit**, or **enabling** a heartbeat resets it back to **waiting**
    * A heartbeat becomes **active** only after its **first successful ping**
  </Step>
</Steps>

***

### Pinging Heartbeats

Systems can ping heartbeats using **HTTP** or **email**.\
Both methods behave identically: they reset the timer and, if previously expired, will **resolve all heartbeat alerts**.

#### HTTP Ping (recommended)

Use the automatically generated ping URL:

```bash  theme={null}
curl -X POST https://api.rootly.com/v1/heartbeats/{heartbeat_id}/ping
```

Replace `{heartbeat_id}` with your Heartbeat’s UUID.\
The ping URL is displayed directly in the Heartbeat’s configuration page.

<Info>
  HTTP pings are ideal for scripts, cron jobs, containers, CI pipelines, and any system capable of making HTTP requests.
</Info>

***

#### Email Ping

Every Heartbeat is also assigned a **unique email address**:

```
heartbeat-<unique_key>@<your-inbound-domain>
```

Sending *any* email to this address counts as a valid ping.

**Common use cases:**

* Legacy systems that only support email notifications
* Backup/cron jobs that already send “success” emails
* Air-gapped or restricted systems that cannot perform HTTP requests

Behavior:

* Email subject/body do **not** matter
* Each valid email resets the Heartbeat’s timer
* Invalid addresses return a bounce notification

<Note>
  You can find the Heartbeat’s email address directly in its configuration panel.
</Note>

***

### Heartbeat Expiration & Recovery

#### When does a heartbeat expire?

A Heartbeat transitions to **expired** when:

```
current_time > expires_at
```

When expired:

* A **Heartbeat Alert** is created
* Routing rules determine who gets paged
* Escalation Policies and Alert Urgency define notification behavior

***

#### Automatic Recovery

If an expired heartbeat receives a ping:

1. Status transitions **expired → active**
2. All open Heartbeat Alerts are **automatically resolved**
3. A recovery event is added to the alert timeline

This avoids noisy follow-up alerts and validates system recovery.

<Info>
  Rootly guarantees that recovery events propagate even when grouped alerts are involved.
</Info>

***

### Special Behavior: Rootly API Heartbeat

Rootly includes a special internal Heartbeat named:

```
rootly-api-heartbeat
```

When pinged:

* **All** Heartbeats in the workspace reset to **waiting**
* Their timers and expiration windows are cleared

This is used internally for environment-wide health resets and should not be modified.

***

### Who Gets Paged for a Missed Heartbeat

Every Heartbeat must be configured with **one notification target**:

* **Escalation Policy**
* **Service**
* **Team (Group)**
* **User**

Rootly applies your workspace’s:

* Escalation rules
* Working hours
* Alert urgency
* Notification channels (SMS, phone, push, Slack, email)

This ensures missed pings integrate seamlessly with on-call workflows.

***

### Best Practices

* Use **short intervals** (1–5 minutes) for critical services
* Set **High urgency** for production-impacting checks
* Use **email pings** for legacy or offline systems
* Name Heartbeats clearly (e.g., `api-liveness`, `db-backup-success`)
* Use separate Heartbeats for independent components
* Review heartbeat alerts weekly to detect flapping or missing pings

***

### Troubleshooting

<AccordionGroup>
  <Accordion title="Heartbeat stays in 'waiting'">
    * Heartbeat may not be **enabled**
    * Interval or unit was recently changed → resets to waiting
    * No valid pings received yet
    * Verify ping URL or email address is correct
  </Accordion>

  <Accordion title="Heartbeat never expires">
    * Interval may be too large
    * System may be sending frequent pings
    * Verify whether alert resolution is immediately resetting intervals
  </Accordion>

  <Accordion title="Alerts do not resolve after pings">
    * Check whether status transitioned `expired → active`
    * Ensure ping reached the correct Heartbeat ID
    * Review timeline for recovery events
  </Accordion>

  <Accordion title="Email pings aren’t registering">
    * Inbound email domain may not be configured
    * MX records could be missing or misconfigured
    * Invalid email formats will bounce
  </Accordion>
</AccordionGroup>

***


Built with [Mintlify](https://mintlify.com).