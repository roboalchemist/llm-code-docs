# Source: https://docs.rootly.com/on-call/edit-schedules.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Edit Schedules

> Learn how to update on-call schedules, manage overrides, and pause paging without disrupting historical data.

## Overview

On-call schedules are living configurations that evolve as teams grow, coverage changes, and real-world situations arise. While schedules define *who* is responsible at any given moment, Rootly is designed so that edits to schedules are **safe, auditable, and non-destructive**.

When you update a schedule—whether by adding users, creating overrides, or temporarily pausing paging—Rootly ensures that **historical records remain intact**. Past incidents, alerts, and timelines continue to reflect exactly who was on call at that moment in time, while your changes only apply going forward.

This page walks through how to confidently edit schedules after they’ve been created, including managing overrides and pausing schedules without deleting them.

<Note>
  ### How schedule changes work

  Any changes made to a schedule only affect **future shifts**.\
  Rootly intentionally prevents edits from modifying past on-call history to preserve accurate audits, incident timelines, and compliance records.
</Note>

<Warning>
  ### Required permissions

  Only users with the following **On-Call roles** can create, edit, or delete schedules:

  * Admin
  * User

  Users with Observer access can view schedules but cannot make changes.
</Warning>

***

## Managing Overrides

Overrides are the safest and most flexible way to handle short-term coverage changes. Instead of editing a rotation—which can affect many future shifts—an override temporarily assigns a specific shift to a different user while leaving the underlying schedule unchanged.

Common use cases include vacations, sick days, training, or one-off coverage swaps.

Overrides always apply to **individual users** and automatically take precedence over rotation-based shifts. Rootly enforces guardrails to ensure overrides do not overlap or create paging conflicts.

### Reassigning or Reverting an Override

To manage an override, navigate to **On-Call → Schedules** and open the schedule you want to modify. Shifts that are currently overridden are clearly marked with an **Override** label, making it easy to distinguish them from standard rotation shifts.

***

### Reverting an Override

Reverting an override restores the shift to its original assignee based on the schedule’s rotation logic. This is commonly used once the temporary coverage change is no longer needed.

Select the overridden shift, then choose **Revert to original**. The shift will immediately return to the user originally assigned by the rotation.

<Frame>
  <img src="https://mintcdn.com/rootly/7ojKISea6oiQMk0o/images/schedules/9.webp?fit=max&auto=format&n=7ojKISea6oiQMk0o&q=85&s=bac289535660368334e26907b5c142c6" width="897" height="780" data-path="images/schedules/9.webp" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/rootly/7ojKISea6oiQMk0o/images/schedules/10.webp?fit=max&auto=format&n=7ojKISea6oiQMk0o&q=85&s=456f08ded7fd82750db07aae46ebbdcf" width="896" height="559" data-path="images/schedules/10.webp" />
</Frame>

<Note>
  Overrides can also be reverted from the **On-Call Shifts** page.\
  All override actions—including creation, reassignment, and reversion—are logged and auditable.
</Note>

***

### Reassigning an Override

If coverage needs to change again, you can reassign an existing override to a different user.

After selecting the overridden shift, choose the new user who should cover it and click **Create Override**. Rootly validates the change automatically, ensuring the override does not overlap with other overrides or violate paging rules.

<Frame>
  <img src="https://mintcdn.com/rootly/7ojKISea6oiQMk0o/images/schedules/11.webp?fit=max&auto=format&n=7ojKISea6oiQMk0o&q=85&s=dea3655d908bb008edce810598b654e9" width="900" height="443" data-path="images/schedules/11.webp" />
</Frame>

Overrides cannot be assigned to another schedule and must always map to a single user. This ensures accountability and predictable paging behavior.

***

## Pausing a Schedule

Sometimes a schedule needs to be temporarily disabled without being deleted. This might happen during a service deprecation, team reorganization, or a period where paging should be suppressed.

In Rootly, schedules do not page responders on their own. Paging only occurs when a schedule is referenced by an **Escalation Policy**. This makes pausing a schedule both simple and reversible.

To pause a schedule, remove it from any escalation policies that reference it. The schedule itself remains fully intact and can be reactivated later by re-adding it to an escalation policy.

### How to Pause a Schedule

1. Navigate to **On-Call → Escalation Policies**.
2. Open the escalation policy that includes the schedule.
3. Edit the policy and remove the schedule from the **Who do we notify?** section.
4. Save the escalation policy.

Once removed, the schedule will stop paging immediately, but no configuration or historical data is lost.

***

## Best Practices

When editing schedules, use overrides for short-term changes and reserve rotation edits for long-term structural updates. Pausing schedules by removing them from escalation policies is safer than deleting them outright, especially if you may need them again in the future.

Regularly reviewing schedules after team changes helps prevent stale paging paths and ensures alerts always reach the correct responder.

***

## Frequently Asked Questions (FAQs)

<AccordionGroup>
  <Accordion title="Do overrides affect past shifts?">
    No. Overrides only apply to future shifts. Rootly never rewrites historical on-call data, ensuring incident timelines and audits remain accurate.
  </Accordion>

  <Accordion title="Can I assign an override to another schedule?">
    No. Overrides must always be assigned to an individual user. Schedules cannot be used as override targets.
  </Accordion>

  <Accordion title="What happens when an override is created or reverted?">
    Rootly records the change in the audit log and can notify responders through integrated channels such as Slack, ensuring visibility into coverage changes.
  </Accordion>

  <Accordion title="What’s the safest way to temporarily stop paging?">
    Remove the schedule from all associated escalation policies. This pauses paging while preserving the schedule for future use.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).