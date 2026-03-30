# Source: https://docs.rootly.com/on-call/on-call-shadowing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# On-Call Shadowing

> Learn how to use on-call shadowing to safely train new responders without duplicating schedules.

## Overview

On-call shadowing is designed to help teams ramp new responders with confidence—without putting production reliability at risk.

Instead of duplicating schedules or manually coordinating training shifts, Rootly allows you to add **shadow users** directly onto an existing on-call schedule. Shadow users are notified alongside the primary on-call responder, giving them real-world exposure to alerts, workflows, and incident patterns while keeping ownership and accountability with the primary responder.

Shadowing is commonly used for onboarding new engineers, preparing responders for rotation changes, or temporarily training team members on unfamiliar systems.

Once a shadowing period ends, Rootly automatically removes the shadow user—no cleanup required.

***

## Shadow Setup

To get started, navigate to **On-Call → Schedules**, then either create a new schedule or edit an existing one.\
From the schedule editor, open the **Shadows** tab to manage shadow users.

<Frame>
  <img src="https://mintcdn.com/rootly/7ojKISea6oiQMk0o/images/schedules/3.webp?fit=max&auto=format&n=7ojKISea6oiQMk0o&q=85&s=1da538ce48e295bd4132b2641a468728" width="897" height="690" data-path="images/schedules/3.webp" />
</Frame>

From here, you can define *who* should shadow, *what* they should shadow, and *when* they should receive notifications.

***

## Define Active Hours for Shadow Paging

Not every team wants shadow users to be paged 24/7.

The **Page shadow user during specific hours** option allows you to restrict when shadow users are notified. This is especially useful if your primary schedule runs around the clock, but shadow users should only be paged during business hours.

When enabled, shadow paging respects the schedule’s configured business hours. You can optionally include weekends if desired, giving you fine-grained control over the shadowing experience without modifying the primary schedule.

<Frame>
  <img src="https://mintcdn.com/rootly/7ojKISea6oiQMk0o/images/schedules/4.webp?fit=max&auto=format&n=7ojKISea6oiQMk0o&q=85&s=57147e4ef799a1748c0b36233ad16bf4" width="900" height="385" data-path="images/schedules/4.webp" />
</Frame>

This ensures shadowing is educational—not overwhelming.

***

## Add Shadow Users

Rootly supports two shadowing modes depending on how you want the training experience to work: **shadowing a specific user** or **shadowing an entire schedule**.

Once configured, click **Add shadow user** to begin.

***

### Shadow a User

Shadowing a specific user is ideal when you want a trainee to learn directly from a particular responder.

In **Shadow a user** mode, you select the individual on-call responder to shadow and define the timeframe during which shadowing should occur. During this period, the shadow user is notified whenever that responder is paged—subject to any active hour restrictions you’ve configured.

<Frame>
  <img src="https://mintcdn.com/rootly/7ojKISea6oiQMk0o/images/schedules/5.webp?fit=max&auto=format&n=7ojKISea6oiQMk0o&q=85&s=0f64d571b4a572cdd7e784fdb6a4dc2f" width="902" height="970" data-path="images/schedules/5.webp" />
</Frame>

This approach works well for mentorship-driven onboarding or pairing junior responders with experienced engineers.

***

### Shadow a Schedule

Shadowing an entire schedule is useful when training should follow the rotation itself rather than a single person.

In **Shadow a schedule** mode, the shadow user is notified whenever *any* responder on the schedule is paged during the configured shadowing window. As the schedule rotates, the shadow user follows along automatically.

<Frame>
  <img src="https://mintcdn.com/rootly/7ojKISea6oiQMk0o/images/schedules/6.webp?fit=max&auto=format&n=7ojKISea6oiQMk0o&q=85&s=5c8d5e6fb14403adcf5eb304570d2294" width="895" height="844" data-path="images/schedules/6.webp" />
</Frame>

This provides a broader view of how a team handles incidents across shifts and responders.

***

You can configure **multiple shadow users at the same time**, each with their own shadowing targets and time windows. Shadowing periods may overlap, and Rootly will handle notification delivery accordingly.

<Frame>
  <img src="https://mintcdn.com/rootly/7ojKISea6oiQMk0o/images/schedules/7.webp?fit=max&auto=format&n=7ojKISea6oiQMk0o&q=85&s=6ae2176569a83b804f723cb4f1041081" width="928" height="1718" data-path="images/schedules/7.webp" />
</Frame>

***

## Viewing Shadow Users on the Calendar

Shadowing visibility is built directly into the schedule calendar.

Shifts that include shadow users are marked with a **ghost icon**, making it easy to identify shadowed coverage at a glance. Clicking into a shift reveals the shadow users listed beneath the primary on-call responder.

<Frame>
  <img src="https://mintcdn.com/rootly/7ojKISea6oiQMk0o/images/schedules/8.webp?fit=max&auto=format&n=7ojKISea6oiQMk0o&q=85&s=d2df8cdee310c175df65b2635da3d3f4" width="875" height="627" data-path="images/schedules/8.webp" />
</Frame>

This makes it easy for managers and responders to understand who is learning alongside active coverage.

***

## Automatic Expiration

Shadowing is always time-bound.

Once a shadowing period reaches its configured end time, Rootly automatically removes the shadow user from the schedule. Paging stops immediately, and no manual action is required. Historical records remain intact for auditing and visibility, but shadow users are never left attached unintentionally.

This ensures shadowing stays intentional, controlled, and low-risk.

***

## Permissions

Only users with sufficient On-Call permissions can manage shadowing.\
Users with **On-Call Admin** or **On-Call User** roles can create, edit, and remove shadow users. Observers have read-only access.

***

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="Who gets paged when shadowing is enabled?">
    When shadowing is active, **both the primary on-call responder and the shadow user are notified** for eligible alerts.\
    The primary responder remains fully responsible for acknowledging and resolving alerts, while the shadow user receives the same notifications for learning and visibility purposes.
  </Accordion>

  <Accordion title="Does shadowing affect escalation policies or alert ownership?">
    No. Shadowing does **not** change escalation behavior, alert ownership, or acknowledgement logic.\
    Escalation policies continue to function exactly as configured, and alerts are still assigned to the primary responder. Shadow users are purely additive and do not interfere with alert flow.
  </Accordion>

  <Accordion title="Can I limit when shadow users are paged?">
    Yes. Shadow paging can be restricted to specific hours by enabling the **Page shadow user during specific hours** option.\
    When enabled, Rootly respects the schedule’s business hours configuration and optionally includes or excludes weekends. This is ideal for training during working hours without overnight interruptions.
  </Accordion>

  <Accordion title="Can multiple shadow users be active at the same time?">
    Absolutely. You can configure **multiple shadow users simultaneously**, each with their own shadowing targets and time windows.\
    Shadow users may overlap in time, and Rootly will ensure notifications are delivered appropriately without conflict.
  </Accordion>

  <Accordion title="What happens when the shadowing period ends?">
    Shadowing automatically expires at the configured end time.\
    Once expired, the shadow user is removed from paging immediately—no manual cleanup is required. Historical records remain available for auditing, but the shadow user will no longer receive notifications.
  </Accordion>

  <Accordion title="Can a shadow user acknowledge or resolve alerts?">
    Shadow users receive notifications but **do not replace the primary responder**.\
    Depending on their permissions, they may view alerts and incidents, but operational responsibility and escalation remain with the primary on-call responder.
  </Accordion>

  <Accordion title="Can I shadow a team instead of a user or schedule?">
    No. Shadowing supports **specific users or entire schedules only**.\
    Teams cannot be shadowed directly. If you want team-level shadowing behavior, create a schedule for that team and shadow the schedule instead.
  </Accordion>
</AccordionGroup>

***

## Best Practices

* Use shadowing during onboarding instead of duplicating schedules
* Limit shadow paging to business hours for new responders
* Start with shadowing a specific user before moving to full schedule shadowing
* Use calendar visibility to communicate training coverage to the team
* Let shadowing expire naturally—avoid long-running, open-ended shadows

Shadowing is most effective when treated as a temporary learning tool, not a permanent paging mechanism.

***


Built with [Mintlify](https://mintlify.com).