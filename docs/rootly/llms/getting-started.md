# Source: https://docs.rootly.com/notifications/getting-started.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started

> Configure general and on-call notifications including email, Slack, SMS preferences, shift reminders, and escalation rule layers.

Rootly notifications ensure responders stay informed without needing to constantly monitor Slack channels or dashboards. Delivery is multi-channel (Email, Slack, SMS, Phone Calls, and Push Notifications), and you can configure how and when you receive signals depending on urgency and context.

Manage your preferences in **Account Settings → Notifications**.

Notifications are divided into two categories:

* **General Notifications** — awareness-based updates (assignments, mentions, summaries).
* **On-Call Notifications** — paging and escalation behavior during active shifts.

***

# General Notifications

General notifications keep you informed about operational activity even when you are not actively on call. These updates are informational — they are not designed to page you urgently.

## Email Notifications

Email is optimized for durable updates and summaries you may want to reference later.

By default, new users are subscribed to:

* Weekly incident summaries
* Postmortem publications

Depending on configuration, you may also receive assignment-based updates (such as action items or incident role assignments).

<Callout icon="envelope-circle-check" color="#16A34A">
  **Email requires verification**

  Rootly will only deliver email notifications if your email address is verified.\
  If delivery fails, verify your address before testing rules again.
</Callout>

***

## Slack Notifications

Slack notifications are designed for real-time collaboration and in-channel visibility.

These may include:

* Incident invitations
* Assignment notifications
* Mentions in incident messages
* Mentions in timeline events

Slack delivery requires a connected Slack account and workspace authorization.

<Callout icon="slack" color="#0EA5E9">
  **Slack must be connected**

  If Slack is not connected, Rootly will fall back to other enabled contact methods where possible.
</Callout>

***

# On-Call Notifications

On-call notifications control paging behavior during active shifts. These are designed for urgent, actionable signals.

There are two core components:

1. **Shift Reminders** — pre-shift and post-shift notifications
2. **Notification Rules** — escalation logic when alerts require action

***

## Shift Reminders

Shift reminders reduce missed handoffs and give responders time to prepare.

### Default Behavior

Shift reminders are **enabled by default** for new users. Rootly automatically creates reminders for:

* `at_start` — before a shift begins
* `at_end` — before a shift ends

By default:

* Email: enabled
* Slack: enabled
* SMS: disabled
* Push notifications: disabled

### Reminder Timing

Shift reminders use **human-readable delay values**, such as:

* `"3 days"`
* `"1 day"`
* `"1 hour"`

Additional minute-level options may be available depending on feature configuration.

<Callout icon="hourglass-half" color="#2563EB">
  **Shift reminder delays are string-based**

  Reminder timing uses values like `"1 hour"` or `"3 days"` —\
  this is different from escalation rules, which use integer delays measured in minutes.
</Callout>

### Guardrails

To prevent broken configurations:

* Maximum **3 reminders per kind** (`at_start` or `at_end`)
* Each enabled reminder must:
  * Have a delay selected
  * Include at least one contact method
* SMS and Phone delivery require verified numbers

***

## Notification Rules (Escalation Logic)

Notification rules define how Rootly pages you when action is required.

Each rule consists of **layers**, and each layer can:

* Wait a specified number of minutes
* Use one or more contact methods
* Escalate progressively if no acknowledgment occurs

***

### Rule Types: Quiet vs Audible

Rootly separates paging into two escalation categories:

* **Quiet** — respects Do Not Disturb and reduces disruption for lower-urgency notifications
* **Audible** — intended for urgent alerts and can break through suppression (for example, critical push alerts)

Both rule types are created automatically for new users.

### Default Rules

New users receive:

* One **Quiet** rule (0-minute delay, Email enabled)
* One **Audible** rule (0-minute delay, Email enabled)

These can be modified, but:

* You must always maintain **at least one Quiet rule**
* You must always maintain **at least one Audible rule**
* You cannot delete the final rule of either type

***

### Escalation Layers

Within each rule, you can:

1. Set a delay (**integer minutes**)
2. Choose contact methods
3. Reorder layers to control escalation flow
4. Test delivery

Delays are always measured in minutes (for example, `0`, `5`, `15`).

***

### Supported Contact Methods

Rootly supports:

* `email`
* `sms`
* `call`
* `device` (critical push notifications)
* `non_critical_device` (standard push notifications)

<Callout icon="shield-check" color="#F97316">
  **Verification is enforced**

  * SMS and Call require verified phone numbers
  * Email requires a verified email address
  * Push requires the Rootly mobile app

  This prevents silent paging failures.
</Callout>

***

### Audible Rule Requirements

Audible rules include additional safeguards to ensure responders are actually reachable:

* Layer 1 must include **Critical Alerts (`device`)**
* Subsequent layers must include at least one of:
  * Critical Alerts (`device`)
  * Phone Call (`call`)

These constraints ensure urgent incidents cannot rely solely on passive delivery channels.

***

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="Why can't I delete my last notification rule?" icon="lock">
    Rootly requires at least one **Quiet** rule and one **Audible** rule to ensure there is always a valid notification path.

    You can modify rules, adjust layers, or change contact methods — but the final rule of each type cannot be deleted. This prevents misconfiguration where alerts cannot be delivered.
  </Accordion>

  <Accordion title="What's the difference between Audible and Quiet notifications?" icon="volume-high">
    **Audible notifications** are designed for urgent alerts that require immediate attention. They:

    * Can bypass Do Not Disturb (via Critical Alerts)
    * Require Critical Alerts (`device`) on the first layer
    * Require Critical Alerts or Phone Call on subsequent layers

    **Quiet notifications** are intended for lower-urgency signals. They:

    * Respect Do Not Disturb
    * Can rely on email or standard push notifications
    * Are suitable for informational updates

    Both rule types are created automatically for new users and can be customized independently.
  </Accordion>

  <Accordion title="How do I verify my phone number or email address?" icon="shield-check">
    **Phone numbers**

    1. Go to **Account Settings → Notifications**
    2. Add a number under **Phone Numbers**
    3. Enter the verification code sent via SMS or call

    **Email addresses**

    * Primary emails are verified automatically
    * Additional emails require confirmation via a verification link

    Verification is required before email, SMS, or call delivery can be used in notification rules.
  </Accordion>

  <Accordion title="Why aren't my shift reminders working?" icon="clock">
    Common causes include:

    * Reminder is disabled
    * No contact methods selected
    * Contact information is unverified
    * No delay selected
    * No scheduled shift

    Use the **Test** option in notification settings to validate delivery.
  </Accordion>

  <Accordion title="Can I customize shift reminder times?" icon="sliders">
    Yes. Shift reminders support:

    * 3 days before
    * 1 day before
    * 1 hour before

    Additional minute-level options may be available depending on configuration.

    You can configure up to **3 reminders per kind** (before shift start or end).\
    Reminder delays use human-readable values (e.g., `"1 hour"`), not integer minutes.
  </Accordion>

  <Accordion title="What happens if I don't have a verified phone number?" icon="phone">
    If your phone number is not verified:

    * SMS will not be sent
    * Phone calls will not be sent

    Email, Slack, and push notifications will still function if configured.

    For Audible rules, ensure either Critical Push (`device`) or Phone Call is properly set up to maintain compliance.
  </Accordion>

  <Accordion title="How do notification rules escalate?" icon="arrow-up">
    Rules escalate sequentially through configured layers:

    1. The first layer triggers immediately (or after its delay)
    2. If unacknowledged, Rootly waits the configured delay (in minutes)
    3. The next layer activates
    4. Escalation continues until acknowledgment or layers are exhausted

    Delays are cumulative and measured in integer minutes.
  </Accordion>

  <Accordion title="What's the difference between 'device' and 'non_critical_device'?" icon="mobile-screen-button">
    **`device` (Critical Alerts)**

    * Bypasses Do Not Disturb
    * Required on layer 1 of Audible rules
    * Designed for urgent wake-up scenarios

    **`non_critical_device` (Standard Push)**

    * Respects Do Not Disturb
    * Suitable for Quiet rules
    * Used for informational alerts

    Both require the Rootly mobile app.
  </Accordion>

  <Accordion title="Can I disable shift reminders?" icon="toggle-off">
    Yes. You can toggle reminders off without deleting them:

    1. Go to **Account Settings → Notifications → Shift Reminders**
    2. Disable the reminder

    Disabled reminders remain saved and can be re-enabled later.
  </Accordion>

  <Accordion title="How do I test my notification configuration?" icon="flask">
    Use the **Test** button on any rule layer:

    1. Navigate to **Notifications → On-Call Notifications**
    2. Select a rule layer
    3. Click **Test**

    Rootly will attempt delivery using the configured contact methods.\
    Ensure contact information is verified before testing.
  </Accordion>

  <Accordion title="Can I have different notification rules per team?" icon="sitemap">
    Notification rules are **user-level**, not team-level.

    Teams and services control routing via **Escalation Policies**, while users control how they personally receive alerts.
  </Accordion>

  <Accordion title="What happens if all notification methods fail?" icon="triangle-exclamation">
    Rootly will continue attempting delivery according to your configured layers.\
    Failed attempts are logged, and escalation continues until all layers are exhausted.

    To reduce risk:

    * Configure multiple contact methods
    * Verify all contact information
    * Connect the mobile app
    * Test regularly
  </Accordion>
</AccordionGroup>

***

<Callout icon="life-ring" color="#F59E0B">
  **Need help configuring notifications?**

  If you're unsure which channels to enable or are experiencing delivery issues, contact  **[support@rootly.com](mailto:support@rootly.com)** or use **`/rootly support`** in Slack.
</Callout>


Built with [Mintlify](https://mintlify.com).