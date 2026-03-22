# Source: https://docs.rootly.com/on-call/on-call-notifications.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# On-Call Notifications

> Learn how to set up shift reminders and notification rules!

To configure your on-call notification preferences, navigate to **Account Settings → Notifications → On-Call Notifications**.

This page is where you define two things that matter during every high-pressure moment: **how Rootly reaches you when you’re paged**, and **how Rootly reminds you about upcoming coverage**. The goal isn’t just “send a notification.” The goal is to make sure the right signal reaches the right person, in the right way, without adding noise or relying on manual coordination.

***

## Notification Rules

Notification Rules control how you are notified when an alert is assigned to you. They are evaluated as an ordered sequence of “steps.” If an alert remains unacknowledged, Rootly moves forward to the next step and continues escalating until someone responds or the escalation path completes.

You configure **Audible** and **Quiet** rules separately so you can treat urgent alerts differently from low-priority alerts. In practice, this is what allows teams to page hard for production-impacting issues while still keeping informational signals visible without waking someone up unnecessarily.

<img src="https://mintcdn.com/rootly/DKlgfX6OLf3Gcj0a/images/CleanShot2026-01-29at16.51.45@2x.png?fit=max&auto=format&n=DKlgfX6OLf3Gcj0a&q=85&s=fb374d371c6ad93f3f2a671a87274381" alt="Clean Shot2026 01 29at16 51 45@2x" width="3410" height="1990" data-path="images/CleanShot2026-01-29at16.51.45@2x.png" />

### How notifications are delivered

Rootly supports several delivery methods for notification rules, and each is intentionally designed for a slightly different purpose.

Email and SMS are great for redundancy and visibility. Phone calls are harder to miss and are commonly used as a fallback when an alert remains unacknowledged. Push notifications come in two flavors: **Critical Alerts** and **Push Notifications (non-critical)**. That distinction matters—especially if you rely on Do Not Disturb.

<Note>
  **Critical Alerts** are delivered as a device push that is intended to bypass Do Not Disturb.\
  **Push Notifications (non-critical)** are delivered as a device push that respects Do Not Disturb.
</Note>

If you’re trying to create a setup that is “reliable but not disruptive,” you’ll typically reserve Critical Alerts (and calls) for audible paging, and use non-critical push, SMS, or email for quiet paging.

### Audible notifications

Audible rules are how you want to be contacted when an alert requires immediate action. Think of this as your “wake-me-up” configuration.

Rootly enforces a few guardrails here because audible paging is only effective if it’s impossible to configure into a state where urgent alerts can silently fail. In other words: Rootly won’t let you accidentally create an audible policy that can’t actually reach you.

The most important rule is the first step. On the first audible step, Rootly requires a real-time, high-reliability delivery method:

* If you have a connected mobile device, **Critical Alerts are required on step 1**.
* If you do not have a connected mobile device, **a phone call is required on step 1**.

After step 1, you still have flexibility, but Rootly continues to protect you from building “quiet audible” rules. For any audible step after the first, at least one of the following must remain enabled: **Phone call** or **Critical Alerts**.

<Warning>
  Audible notification steps are validated to prevent missed pages. If you try to save an audible step that can’t reliably reach you (for example, no Critical Alerts on step 1 when a device is connected), Rootly will block the save until the rule is made safe.
</Warning>

This is also why many teams pair Critical Alerts with a secondary channel (like SMS or email). Even if you’re confident push will reach your device, redundancy makes paging behavior more resilient under real-world conditions.

### Quiet notifications

Quiet rules are for alerts that still matter, but don’t justify immediate interruption. Quiet notifications can still escalate through multiple steps, but the intent is fundamentally different: keep responders informed and create visibility without forcing someone to wake up or break focus unless it’s truly necessary.

Quiet rules are where teams typically lean on email, SMS, and **non-critical push notifications**. Quiet push is especially useful when you want alerts to land on a phone without cutting through Do Not Disturb.

<Note>
  If you want “push to phone” without bypassing Do Not Disturb, make sure you’re using **Push Notifications (non-critical)** rather than Critical Alerts.
</Note>

### Testing your notifications

On-Call Notifications is also where you can validate your setup before you depend on it. The **Test Notifications** action lets you send test messages to the targets you’ve configured so you can confirm that delivery works end-to-end.

Testing is available for the same core delivery methods used by notification rules, including email, SMS, phone call, and device push. This is worth doing any time you change phones, update a phone number, reinstall the mobile app, or simply want to confirm that your current configuration still behaves the way you expect.

<Tip>
  A good rule of thumb is to test at least one audible path (Critical Alerts or call) and one quiet path (email or non-critical push) after setting up notifications—before you go on-call.
</Tip>

***

## Verification requirements

To protect responders from configuration that looks valid but can’t actually deliver, Rootly requires contact methods to be verified before they can be used for paging.

If you attempt to save rules using an unverified phone number (for SMS or call) or an unverified email address (for email), Rootly will block the configuration until verification is complete. Shift Reminders follow the same principle: reminder delivery methods must be verified when the reminder is enabled.

<Warning>
  If you can’t save notification rules or reminders, verification is the first thing to check. Unverified phone numbers and email addresses will prevent delivery-enabled configurations from being saved.
</Warning>

### Shift Reminders

Shift Reminders notify you before your shift starts and when your shift ends. This is less about “paging” and more about preventing operational surprise. Reminders are especially helpful when you rotate frequently, cover multiple schedules, or switch between teams.

You can enable reminders and choose how you want them delivered. Shift reminders support email, SMS, push notifications, and Slack (Slack reminders require your Slack account to be connected).

<Frame>
    <img src="https://mintcdn.com/rootly/dh_btGDqFCP-4ebs/images/CleanShot2025-09-26at09.23.14@2x.png?fit=max&auto=format&n=dh_btGDqFCP-4ebs&q=85&s=4057d32c72cf5d3f5e084c65c69f200e" alt="Shift reminders configuration" width="3406" height="1940" data-path="images/CleanShot2025-09-26at09.23.14@2x.png" />
</Frame>

### Reminder timing and limits

Reminders are configured using a delay (how long before the shift boundary you want to be notified). By default, you’ll commonly see delays like **3 days**, **1 day**, and **1 hour**.

Some workspaces also support additional reminder options—such as **30 minutes**, **15 minutes**, and **1 minute**—to better fit short rotations or “handoff-heavy” teams. When those additional options are enabled, you can configure up to **three reminders per reminder type** (for example: multiple reminders before shift start). If those additional options are not enabled, reminders are typically limited to one reminder per type (one for start, one for end).

<Note>
  If you only see one reminder available for start/end, your workspace may not have the additional shift reminder options enabled. In workspaces where the expanded options are enabled, you can configure up to three reminders per type.
</Note>

### Slack reminders (when available)

Slack delivery is available for shift reminders, but only when your Slack account is connected. If Slack isn’t connected, the UI will prevent enabling Slack reminders because Rootly has no valid user destination to deliver to.

### Nested schedules and reminder behavior

Shift reminders are sent for the schedule you are directly on-call for. If your schedule is included in another schedule (a “parent schedule” pattern), reminders do not fire for the nested schedule coverage in order to avoid duplicate reminders and confusing overlap.

<Warning>
  You won’t receive shift reminders for shifts where your schedule is on-call indirectly through a parent schedule.
</Warning>

***

## Default setup behavior

If notification rules or reminders are missing, Rootly automatically creates a safe baseline so new responders aren’t left unpaged.

Typically, that means a default quiet rule (commonly email), a default audible rule (email plus a high-reliability channel when available), and two shift reminders (one for shift start and one for shift end) initially delivered via email. These defaults are meant to be edited—not treated as “best possible forever”—but they provide immediate coverage while a team finalizes their preferred setup.

***

## Troubleshooting

<AccordionGroup>
  <Accordion title="I can’t save an audible notification step">
    Audible rules have strict safety requirements so that urgent alerts can’t be configured into a non-deliverable state. The most common causes are missing Critical Alerts on the first audible step (when a device is connected) or missing phone call coverage on the first step (when no device is connected). For later audible steps, Rootly requires that at least one of phone call or Critical Alerts remains enabled so escalation can’t become “quiet” by accident.
  </Accordion>

  <Accordion title="My phone number or email won’t work in rules or reminders">
    Notification rules and enabled shift reminders require verified contact methods. If your email address or phone number is unverified, Rootly will block saving configurations that depend on those channels because delivery would fail at runtime. Verify the contact method first, then return to On-Call Notifications and save again.
  </Accordion>

  <Accordion title="I’m not receiving push notifications">
    First, confirm whether you’re expecting Critical Alerts (bypass DND) or non-critical push (respects DND). Then confirm your mobile device is connected and registered. If you recently changed phones, reinstalled the app, or disabled notification permissions at the OS level, push delivery may fail until the device is reconnected and permissions are restored. Use Test Notifications to validate push delivery immediately.
  </Accordion>

  <Accordion title="Shift reminders aren’t firing for my shift">
    If your on-call coverage is coming from a nested schedule (your schedule is on rotation for another schedule), reminders may not fire for the nested layer. This is expected behavior to prevent duplicate reminders. Also confirm your reminder is enabled, the delivery channel is verified, and (for Slack reminders) that Slack is connected.
  </Accordion>

  <Accordion title="I can’t add multiple reminders before shift start">
    Some workspaces support additional reminder timing options and allow up to three reminders per start/end type. If your workspace doesn’t have that enabled, you may be limited to one reminder per type. In that case, choose the single timing that best matches your handoff needs (for example, 1 hour before shift start).
  </Accordion>
</AccordionGroup>

***

## Best practices

A notification setup is “good” when it’s reliable under stress. Most teams land on a pattern where audible paging is intentionally hard to miss (Critical Alerts and/or calls), quiet paging provides visibility without interrupting (email or non-critical push), and shift reminders reduce handoff confusion.

If you only do one thing, make it this: configure an audible step that will reach you even when your phone is silenced, and then test it. Everything else can evolve over time—but missed pages are expensive, and Rootly’s notification rules exist specifically to prevent them.


Built with [Mintlify](https://mintlify.com).