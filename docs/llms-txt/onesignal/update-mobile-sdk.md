# Source: https://documentation.onesignal.com/docs/en/update-mobile-sdk.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update mobile SDKs

> Why updating mobile SDKs matters, how to do it efficiently, and how to make it part of your workflow.

## Overview

Learn why keeping your mobile SDKs—like OneSignal—updated is essential for app health, and how to build updates into your workflow.

<Note>
  If you're just getting started with OneSignal, see the [Mobile SDK setup guide](./mobile-sdk-setup).
</Note>

***

## OneSignal SDK releases

All OneSignal SDKs are open source. Use the links below to access the latest versions and release notes:

* [OneSignal iOS SDK](https://github.com/OneSignal/OneSignal-iOS-SDK/releases)
* [OneSignal Android SDK](https://github.com/OneSignal/OneSignal-Android-SDK/releases)
* [OneSignal Unity SDK](https://github.com/OneSignal/OneSignal-Unity-SDK/releases)
* [OneSignal Flutter SDK](https://github.com/OneSignal/OneSignal-Flutter-SDK/releases)
* [OneSignal React Native SDK](https://github.com/OneSignal/react-native-onesignal/releases)
* [OneSignal DotNet SDK](https://github.com/OneSignal/onesignal-dotnet-sdk/releases)
* [OneSignal Ionic/Cordova SDK](https://github.com/OneSignal/OneSignal-Cordova-SDK/releases)

***

## Why updating mobile SDKs matters

Your app relies on SDKs for critical features like messaging, analytics, and engagement. Regular updates help you:

* **Unlock new features** – Improve UX and boost engagement.
* **Enhance performance** – Stay fast and stable.
* **Stay secure** – Fix vulnerabilities before they impact users.
* **Maintain compatibility** – Avoid issues with OS or SDK version changes.

<Warning>
  Outdated SDKs increase technical debt, introduce bugs, and delay your access to new capabilities.
</Warning>

***

## Why frequent updates are easier

Smaller, more frequent updates reduce complexity and risk. Benefits include:

* Fewer breaking changes to fix.
* Easier debugging and regression testing.
* Faster adoption of vendor support and best practices.

<Check>
  Example: OneSignal iOS SDK `v5.2.0` introduced Live Activities PushToStart—an enhancement only available by updating.
</Check>

***

## Why teams delay SDK updates (and how to fix that)

### “We don’t have time”

* **Reality**: Most SDK updates are quick.
* **Fix**: Use versioning to scope the effort:
  * **PATCH** (e.g. `5.2.0 → 5.2.1`): Small fixes. Safe to auto-upgrade.
  * **MINOR** (e.g. `5.2.2 → 5.3.0`): New features, backward compatible.
  * **MAJOR** (e.g. `5.2.2 → 6.0.0`): Breaking changes. Needs review and planning.

### “If it works, don’t touch it”

* **Reality**: “Works” doesn’t mean “optimized” or “future-proof.”
* **Fix**: Review changelogs to understand what’s improved and what risks you’re carrying.

***

## Build SDK updates into your workflow

### 1. Set a regular cadence

* Review SDK versions **monthly or quarterly**.
* Batch **PATCH/MINOR** updates in normal sprints.
* Schedule **MAJOR** updates with dedicated planning.

### 2. Assign clear roles

* **SDK Owner** – Tracks new releases and initiates upgrades.
* **Developers** – Implement and test updates.
* **Marketing/Product** – Identify and use new capabilities.

### 3. Automate where possible

* Use scripts to monitor SDK versions and notify your team.
* Add SDK version checks to your CI/CD pipeline.
* Set up alerts for performance changes post-update.

<Check>
  After an SDK update, always test notification delivery and user engagement to catch regressions early.
</Check>

***

## Communicate SDK updates internally

* **Share changelogs** with cross-functional teams.
* **Include updates in sprint demos or standups**.
* **Keep internal docs current**—prevent confusion from outdated guidance.

***

## Encourage users to update the app

SDK updates only reach users if they update your app.

Use in-app messaging or push notifications to:

* Inform users about new updates.
* Promote benefits (e.g. speed, stability, new features).
* Encourage downloads from the app store.

***

## TL;DR: Make SDK updates a habit

* Treat SDK updates like routine maintenance—don’t wait until something breaks.
* Avoid major version leaps by updating frequently.
* Use versioning and automation to stay ahead.
* Make it a team responsibility, not a one-off task.
* Start by auditing your current SDK versions and update any that are out of date.

***

## Next steps

* [Mobile SDK setup](./mobile-sdk-setup)
* [Mobile SDK reference](./mobile-sdk-reference)
* [Mobile SDK troubleshooting](./mobile-troubleshooting)

***

Built with [Mintlify](https://mintlify.com).
