# Source: https://documentation.onesignal.com/docs/en/disabled-apps.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Disabled apps & organizations

> Understand why your OneSignal app or organization may be disabled, what functionality is affected, and how to restore access or prevent future disablements.

## Overview

A OneSignal App or Organization may be disabled to protect platform stability, enforce billing and compliance requirements, or prevent unintended messaging behavior.

This guide explains:

* How Apps and Organizations become disabled
* What happens when an App or Organization is disabled
* How to re-enable an App or Organization

Before continuing, review:

* [Apps, Organizations, & Accounts](./apps-organizations) to understand how ownership and billing are structured.
* [Team members](./manage-team-members) to understand how to manage team access.

<Note> An **App** holds user and messaging data for a single project, across multiple platforms (web, iOS, Android, email, etc.). An **Organization** is a container for managing multiple apps, billing, and team permissions. </Note>

***

## How Apps and Organizations become disabled

An **App** may be disabled:

* Manually by an App Admin in the dashboard **Settings > Manage App > Disable App buttons**
* Automatically due to:
  * [API rate limits](/reference/rate-limits)
  * Violations of the [Acceptable Use Policy](https://onesignal.com/aup)

**Organization** may be disabled due to:

* Overdue invoices on a paid plan. See [Billing FAQ](./billing-faq) for more details.
* Violations of the [Acceptable Use Policy](https://onesignal.com/aup)

When an Organization is disabled, all Apps within the Organization are disabled, and billing or compliance issues must be resolved first.

***

## What happens when an App or Organization is disabled

When an **App** is disabled:

* ❌ New messages cannot be sent.
* ❌ In-app messages are paused.
* ❌ Scheduled messages waiting to send are cancelled.
* ❌ Journeys get Stopped and Archived.
* ❌ Data cannot be deleted or exported.
* ✅ Existing data remains intact within normal retention periods.
* ✅ SDK initialization will continue to collect new and update existing user data.
* ✅ You will continue to be billed for the App if within an enabled Organization using a paid plan.

<Warning>
  You will continue to be billed for the App if within an enabled Organization using a paid plan. To stop billing:

* Delete the app, or
* Move it to a Free Organization

  Contact `support@onesignal.com` for assistance.
</Warning>

When an **Organization** is disabled:

* ❌ All apps in the organization are disabled
* ❌ Messaging, exports, and deletions are blocked
* ❌ Apps cannot be removed or transferred

<Warning>Organization-level disablement is more restrictive than App-level disablement.</Warning>

***

## How to re-enable an App or Organization

You must be an **App Admin** to re-enable an App and an **Org Admin** to re-enable an App or Organization. See [Team members](./manage-team-members) for details.

App re-enablement:

* If you manually disabled the App, go back to **Settings > Manage App > Disable App buttons** and click **Re-enable**.
* If the App was disabled due to rate limits, you can re-enable it within the dashboard following the warning prompt.
* If the App was disabled for any other reason, contact `support@onesignal.com` for assistance.

Organization re-enablement:

* If the Organization was disabled due to an overdue invoice, pay the invoice and the Organization will be re-enabled.
* If the Organization was disabled for any other reason, contact `support@onesignal.com` for assistance.

***

## FAQ & support

### Does disabling an app stop billing?

No. Disabled apps still count toward MAU billing.

### Does disabling an app stop new users?

No. You must remove the OneSignal SDK to prevent new subscriptions.

### Can I re-enable a disabled app?

Yes in some cases. App Admins can re-enable disabled apps from the dashboard.

### How do I know why something was disabled?

Check dashboard warnings, recent send activity, and billing status. If unsure, contact support with your App ID.

### Need help?

Contact `support@onesignal.com` with the OneSignal App ID (found in **Settings > [Keys & IDs](./keys-and-ids)**) and our team will assist you as soon as possible.

***

<Check>
  Next steps:

* Learn how to [Manage team members](./manage-team-members)
* Review [Apps, Organizations, & Accounts](./apps-organizations)
* Review [Keys & IDs](./keys-and-ids)
* Review [Billing FAQ](./billing-faq)
</Check>

Built with [Mintlify](https://mintlify.com).
