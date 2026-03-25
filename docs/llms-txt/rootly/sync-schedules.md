# Source: https://docs.rootly.com/on-call/sync-schedules.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Sync Schedules to Slack User Groups

> Keep Slack user groups automatically in sync with your on-call schedules so the right responder is always reachable.

## Overview

Syncing an on-call schedule to a Slack user group makes it easy for teams to reach the correct on-call responder without needing to know who is currently covering a shift.

Instead of manually updating Slack user groups or relying on outdated documentation, Rootly keeps your Slack user groups continuously in sync with your on-call schedules. As schedules rotate, overrides are applied, or nested schedules take effect, Rootly automatically updates the Slack user group to reflect **who is on call right now**.

This allows anyone in Slack to simply mention a user group—such as `@oncall-engineering`—and reliably notify the active on-call responder, even as coverage changes behind the scenes.

***

## How Slack User Group Sync Works

When a schedule is linked to a Slack user group, Rootly treats that user group as a live reflection of the schedule’s current on-call assignee.

Each time the on-call user changes, Rootly updates the Slack user group membership to include only the active responder. This includes changes caused by:

* Normal rotation handoffs
* Overrides being created, updated, or reverted
* Nested schedules resolving to a downstream on-call user

Because Slack handles notifications when a user group is mentioned, tagging the group in a Slack message immediately notifies the on-call responder—without requiring any manual updates from your team.

<Note>
  Slack user group mentions are handled entirely by Slack.\
  Rootly’s role is to ensure the **correct Slack user is always a member of the group** based on the current on-call state.
</Note>

***

## Prerequisites

Before you can sync a schedule to a Slack user group, your workspace must meet a few requirements.

Your team must have a Slack integration connected to Rootly, and that integration must include the permissions required to manage user group membership. If the necessary scopes are missing, the Slack user group selector will not be available when editing a schedule.

Additionally, Rootly matches users to Slack accounts by email address. If a Rootly user does not have a corresponding Slack user with the same email, they cannot be added to the Slack user group.

<Warning>
  If you don’t see Slack user groups listed when editing a schedule, ask a Slack administrator to verify that the Slack integration is connected and has the required user group permissions.
</Warning>

***

## Set Up a Slack User Group Sync

To sync a schedule with a Slack user group, open the schedule you want to configure or create a new one.

Within the schedule editor, navigate to the **Notifications** tab. From there, you can select an existing Slack user group from your connected Slack workspace. Once selected, save the schedule to apply the change.

<Frame>
  <img src="https://mintcdn.com/rootly/7ojKISea6oiQMk0o/images/schedules/2.webp?fit=max&auto=format&n=7ojKISea6oiQMk0o&q=85&s=f0643b451dd08f57354bd9683c224fdd" width="1280" height="649" data-path="images/schedules/2.webp" />
</Frame>

As soon as the schedule is saved, Rootly will evaluate the current on-call shift and update the selected Slack user group to include the active responder.

***

## What Happens After Setup

Once configured, the Slack user group remains continuously updated as the schedule evolves.

When a rotation hands off, an override is applied, or a nested schedule resolves to a different user, Rootly automatically updates the Slack user group membership. No manual intervention is required.

If the Slack user group is mentioned in any Slack message, Slack will notify the current on-call responder immediately.

<Note>
  Overrides are fully supported.\
  If an override changes who is on call, the Slack user group is updated automatically to reflect that change.
</Note>

***

## Using One Slack User Group Across Multiple Schedules

You can associate the same Slack user group with multiple schedules.

This is useful if your organization wants a single user group—such as `@oncall`—that always represents *all* active on-call responders across different schedules. Rootly keeps the user group in sync across every schedule that references it, ensuring membership stays accurate even as individual schedules change.

If a schedule is removed from a Slack user group or switched to a different group, Rootly updates all affected schedules to prevent stale memberships.

***

## Best Practices

Slack user group sync works best when user emails are consistent between Rootly and Slack, schedules are connected to escalation policies, and overrides are used instead of editing rotations for short-term changes.

For critical paging paths, Slack user groups should complement—not replace—primary notification methods such as push notifications or phone calls. Slack is best used as a fast collaboration signal rather than the sole paging mechanism.

***

## Frequently Asked Questions (FAQs)

<AccordionGroup>
  <Accordion title="Does mentioning the Slack user group create an alert in Rootly?">
    No. Mentioning a Slack user group only triggers Slack’s built-in notification behavior.\
    Rootly ensures the correct user is a member of the group, but it does not create alerts or incidents from Slack mentions alone.
  </Accordion>

  <Accordion title="What happens if the on-call user doesn’t have a Slack account?">
    Rootly matches users to Slack accounts by email.\
    If no matching Slack user exists, Rootly cannot add that person to the user group, and the sync will fail for that shift.
  </Accordion>

  <Accordion title="Are nested schedules supported?">
    Yes.\
    If a parent schedule includes another schedule as a member, Rootly resolves the final on-call user and updates the Slack user group based on that resolved assignee.
  </Accordion>

  <Accordion title="Can I stop syncing without deleting the schedule?">
    Yes.\
    Simply remove the Slack user group from the schedule’s Notifications tab and save. The schedule remains intact, but Slack sync will stop.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).