# Source: https://docs.rootly.com/on-call/request-coverage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Requesting Shift Coverage

> Request coverage when you can’t work an on-call shift and automatically reassign responsibility.

## Overview

When you’re part of an on-call rotation, Rootly automatically assigns you shifts based on your team’s schedules and escalation policies. While this ensures consistent coverage, real life doesn’t always align perfectly with on-call rotations. Planned time off, unexpected conflicts, or last-minute changes can make it difficult to cover an assigned shift.

**Coverage Requests** are designed to solve this problem without disrupting schedules or requiring an administrator to intervene. Instead of editing schedules directly, you can request help from teammates who are already part of the same rotation. Rootly then coordinates notifications, tracks responses, and automatically reassigns the shift when someone accepts.

Coverage Requests are available across **Web and Slack**, allowing teams to handle coverage quickly in the tools they already use.

## What Is a Coverage Request?

A Coverage Request is a lightweight way to say, “I can’t cover this shift—can someone else take it?”

When you submit a request, Rootly identifies the shifts affected during the selected time window and notifies other responders on the same schedule. Teammates can review the request, accept it if they’re available, or simply ignore it. Once a single person accepts, Rootly automatically creates the required override and closes the request.

This approach keeps schedules intact while ensuring accountability and visibility.

## Submitting Coverage Requests

<Info>
  If you have permission to create overrides directly, you can still reassign a shift manually. Coverage Requests are optimized for self-service coordination among teammates.
</Info>

### Requesting Coverage on Web

Coverage Requests can be created directly from both the **On-Call Shifts** view and the **Schedule** editor.

From the **On-Call Shifts** page, select the shift you’re unable to cover and choose **Request Coverage**.\
From a **Schedule**, edit the schedule you’re currently rotating on, navigate to the **Override & Coverage** tab, and select **Request Coverage**.

<img src="https://mintcdn.com/rootly/RUi0EYcf6x_7UXYC/images/CleanShot2025-08-06at12.41.54@2x.png?fit=max&auto=format&n=RUi0EYcf6x_7UXYC&q=85&s=0e4b6e7c5ffaed0841f2def04b07eee5" alt="Clean Shot2025 08 06at12 41 54@2x Pn" width="2832" height="1664" data-path="images/CleanShot2025-08-06at12.41.54@2x.png" />

After opening the request modal, you’ll define the time range during which you’re unavailable. Rootly automatically detects all shifts assigned to you within that window and presents them for review. Once submitted, notifications are sent immediately.

<img src="https://mintcdn.com/rootly/RUi0EYcf6x_7UXYC/images/CleanShot2025-08-06at12.42.45@2x.png?fit=max&auto=format&n=RUi0EYcf6x_7UXYC&q=85&s=7776e4f1c3d8ea14d86eac2d8b24e1ae" alt="Clean Shot2025 08 06at12 42 45@2x Pn" width="2400" height="1658" data-path="images/CleanShot2025-08-06at12.42.45@2x.png" />

### Requesting Coverage on Slack

If your team primarily operates in Slack, Coverage Requests can be created without ever leaving the conversation.

Run `/rootly override` in Slack, select the time window you need coverage for, and review the affected shifts. When you submit the request, Rootly sends actionable messages to eligible teammates and the schedule’s Slack channel (if configured).

<img src="https://mintcdn.com/rootly/RUi0EYcf6x_7UXYC/images/CleanShot2025-08-06at12.51.03@2x.png?fit=max&auto=format&n=RUi0EYcf6x_7UXYC&q=85&s=bc8a1fc8fa760265174cb307c495debc" alt="Clean Shot2025 08 06at12 51 03@2x Pn" width="1074" height="1240" data-path="images/CleanShot2025-08-06at12.51.03@2x.png" />

### Requesting Coverage on Mobile

Mobile support for Coverage Requests is coming soon and will provide the same end-to-end experience available on Web and Slack.

## Managing Your Coverage Requests

All active Coverage Requests are visible in the Rootly web app. Navigate to **On-Call → Shifts**, then switch to the **Coverage Requests** view.

This page shows open requests, affected time ranges, and current status. Once a teammate accepts a request, it disappears from the list and the shift is immediately reassigned.

<img src="https://mintcdn.com/rootly/RUi0EYcf6x_7UXYC/images/CleanShot2025-08-06at12.23.37@2x.png?fit=max&auto=format&n=RUi0EYcf6x_7UXYC&q=85&s=4afab4d1f18ec73f3895f0afd8bd065f" alt="Clean Shot2025 08 06at12 23 37@2x Pn" width="2834" height="1516" data-path="images/CleanShot2025-08-06at12.23.37@2x.png" />

## Accepting Coverage Requests

Anyone who is part of the same schedule can accept a Coverage Request, as long as they are not already committed to overlapping on-call responsibilities.

Only **one** person can accept a request. As soon as it’s taken, Rootly creates an override, updates all relevant views, and notifies the original requester. If someone else attempts to accept after that point, they’ll be informed that the request has already been fulfilled.

<Info>
  If you rotate on multiple schedules, make sure accepting a request won’t conflict with another on-call commitment.
</Info>

### Accepting on Web

Coverage Requests can be accepted from both the **On-Call Shifts** page and the **Schedule** editor.

From a schedule, navigate to the **Override & Requests** tab to review and accept open requests. Only users with schedule edit permissions can accept requests from this view.

### Accepting on Slack

When a Coverage Request is created, Rootly sends interactive Slack messages to:

1. All active users on the schedule
2. The schedule’s configured Slack channel, if one exists

These messages include actions to **Take the shift**, **View on web**, or ignore the request entirely.

<img src="https://mintcdn.com/rootly/RUi0EYcf6x_7UXYC/images/CleanShot2025-08-06at12.14.05@2x.png?fit=max&auto=format&n=RUi0EYcf6x_7UXYC&q=85&s=b8249bf23fe932cfb4dadc75c017dce3" alt="Clean Shot2025 08 06at12 14 05@2x Pn" width="1312" height="252" data-path="images/CleanShot2025-08-06at12.14.05@2x.png" />

### Accepting on Mobile

Mobile acceptance is coming soon and will mirror the Slack and Web workflows.

## Best Practices

Coverage Requests work best when they’re used early and intentionally. Submitting a request as soon as you know you’ll be unavailable gives teammates more time to plan and respond.

Avoid creating multiple overlapping requests for the same shift window. Rootly prevents duplicates by design, so updating an existing request is the best way to make changes.

Teams should also ensure schedules have a Slack channel configured. This improves visibility and dramatically increases response rates, especially for time-sensitive coverage gaps.

Finally, remember that Coverage Requests are meant for **user-assigned shifts**. If your shift is owned by a schedule rather than an individual, an administrator may need to intervene.

## Frequently Asked Questions (FAQs)

<AccordionGroup>
  <Accordion title="What shifts can I request coverage for?">
    Coverage Requests can only be created for shifts that are assigned to individual users. If a shift is schedule-based, it must first be reassigned to a user before coverage can be requested.
  </Accordion>

  <Accordion title="What happens after someone accepts my request?">
    Once a teammate accepts, Rootly automatically creates an override for the shift, reassigns responsibility, and closes the request. You don’t need to take any further action.
  </Accordion>

  <Accordion title="Can multiple people accept the same request?">
    No. Only one person can accept a Coverage Request. If someone else tries to accept after it’s been taken, Rootly will notify them that the shift is no longer available.
  </Accordion>

  <Accordion title="What notifications are sent when I request coverage?">
    Rootly sends notifications to eligible teammates via Slack (DMs and channels, if configured) and also sends a push notification to your device so you can track the request’s status.
  </Accordion>

  <Accordion title="Can I cancel or change a coverage request?">
    Yes. If your plans change, you can delete the existing request and submit a new one with updated timing. Overlapping requests for the same window are not allowed.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).