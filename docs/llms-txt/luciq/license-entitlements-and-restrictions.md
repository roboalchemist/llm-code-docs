# Source: https://docs.luciq.ai/organization-settings/billing/license-entitlements-and-restrictions.md

# License Entitlements and Restrictions

Effective for Enterprise deals starting November 5, 2025

This page describes Luciq’s license entitlements, restrictions and definitions for Luciq Enterprise customers. See the glossary below if any word is unclear.

For more information on the licensing terms please see [luciq.ai/terms](https://www.luciq.ai/terms)

### Glossary

| Term                           | Definition                                                                                                                                                            |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account                        | Container for your Apps, Users, and Data in Luciq.                                                                                                                    |
| App                            | One mobile application bundle ID connected to Luciq.                                                                                                                  |
| User                           | A user who downloaded your App, whether the user opted in or out of analytics sharing.                                                                                |
| Daily Active Users (DAU)       | The number of unique devices that start at least one Session in any 24-hour window. If the same user uses the app on multiple devices, each device counts separately. |
| Session                        | One instance of a User running the app for at least one second.                                                                                                       |
| SDK (Software Development Kit) | The Luciq library you embed in your App to collect telemetry such as crashes, performance data, and user feedback.                                                    |
| Telemetry                      | Data automatically sent from the SDK to Luciq, including session counts, crashes, and performance metrics.                                                            |
| Trace                          | A timed performance span such as a screen load or network call.                                                                                                       |

#### 1) What You Are Buying?

This section summarizes what your license includes and how usage is measured. As part of your license, you purchase a **range of daily active users (DAU)** for any of the following products:

1. Bug Reporting
2. Crash Reporting
3. Application Performance Monitoring (APM)
4. Session Replay
5. Surveys
6. Rollout management
7. App Ratings and Reviews

#### 2) DAU Definitions and Session Entitlements

Here’s how we define and measure usage across users and sessions, and how that translates into your entitlements.

#### How we calculate DAU?

* **Pre-purchase:** We use third-party app-store analytics (e.g., Sensor Tower) to estimate your DAU and determine the appropriate range.
* **Post-onboarding:** We use Luciq SDK telemetry from your app to measure your actual DAU.

#### Session Entitlement

For every 1 DAU you are entitled to **180 Sessions per month**.

#### 3) Role Types: Who Can Do What

This section outlines the access levels available for team members within your account.

| Role      | Access Scope                                              |
| --------- | --------------------------------------------------------- |
| Member    | Edit rights on assigned Apps                              |
| Associate | Read-only rights on assigned Apps, with limited debugging |
| Observer  | Read-only on aggregated analytics                         |

The Enterprise Plan includes **100 Observers**. Additional Observers can be provisioned upon written request. You may add additional Members or Associates for a fee at any time.

#### 4) Platform Entitlements

Purchase of the Luciq Platform entitles you to:

* Unlimited Apps per account
* Unlimited available integrations

#### 5) Usage Entitlements

{% hint style="info" %}

* This section defines what each product includes and the limits associated with them. You only receive access to products listed on your Order Form.
* If your Order Form specifies different retention for any product, your Order Form takes precedence.
* Need longer retention? Data retention can be extended by request. Please [contact our Sales team](https://www.luciq.ai/request-demo).
  {% endhint %}

#### Standard data retention

Use this section as the default retention snapshot for this version. The detailed per-product retention remains listed under each product below.

| Data Type                                                                                                                                                                                                                  | Enterprise Tier |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [Bugs/Issues](https://app.gitbook.com/o/CZDQbFlEcy4BPZkMujai/s/Cha1KrkvNKPdcC0aGvuB/~/edit/~/changes/80/organization-settings/billing/license-entitlements-and-restrictions/~/agent#bug-reporting)                         | 365 days        |
| [Crash Reports](https://app.gitbook.com/o/CZDQbFlEcy4BPZkMujai/s/Cha1KrkvNKPdcC0aGvuB/~/edit/~/changes/80/organization-settings/billing/license-entitlements-and-restrictions/~/agent#crash-reporting)                     | 180 days        |
| [APM Events](https://app.gitbook.com/o/CZDQbFlEcy4BPZkMujai/s/Cha1KrkvNKPdcC0aGvuB/~/edit/~/changes/80/organization-settings/billing/license-entitlements-and-restrictions/~/agent#application-performance-monitoring-apm) | 60-90 days      |
| User Sessions                                                                                                                                                                                                              | 365 days        |
| Chats/Communication                                                                                                                                                                                                        | 365 days        |
| [Survey Responses](https://app.gitbook.com/o/CZDQbFlEcy4BPZkMujai/s/Cha1KrkvNKPdcC0aGvuB/~/edit/~/changes/80/organization-settings/billing/license-entitlements-and-restrictions/~/agent#surveys)                          | 180 days        |
| Feature Requests                                                                                                                                                                                                           | 180 days        |
| Aggregated Metrics                                                                                                                                                                                                         | 180-397 days    |

#### Crash Reporting

What you get with Luciq’s Crash Reporting, including event limits, retention, and dashboard performance guarantees.

| Item              | Value                                                                                                                                                                                                                                                           |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Event allowance   | <p>Luciq supports unlimited events, constrained only by the following rate limits (requests/min/app):</p><ul><li>Crashes: 3,000</li><li>ANR Errors: 2,000</li><li>Non-Fatal Errors: 2,000</li><li>Force Restarts: 2,000</li><li>App Hangs: 2,000</li></ul>      |
| Crash-group cap   | 5,000 groups in the dashboard list                                                                                                                                                                                                                              |
| Pattern search    | Up to 1,000 values returned                                                                                                                                                                                                                                     |
| Data retention    | <ul><li>Fatal Crashes: <strong>6 Months</strong></li><li>App Hangs: <strong>6 Months</strong></li><li>ANRs: <strong>6 Months</strong></li><li>Non-Fatals: <strong>1 Month</strong></li><li>dYSM & Mapping Files: <strong>90 Days if not used</strong></li></ul> |
| Crash Sync timing | Crashes are sent on the next app launch (i.e., when the user reopens the app).                                                                                                                                                                                  |

#### **Crash Filter Limits**

| Filter              | Limit |
| ------------------- | ----- |
| App versions        | 400   |
| Devices             | 300   |
| Operating systems   | 150   |
| Current views       | 300   |
| Feature flags       | 4000  |
| User-attribute keys | 100   |

#### **Log limits per crash occurrence**

Limits are configurable; these are the default limits.

| Platform | Console Logs | Luciq Logs                 | Network Logs | Network Request Size |
| -------- | ------------ | -------------------------- | ------------ | -------------------- |
| iOS      | 500 lines    | 1000 lines, 500 chars each | 100 entries  | 10KB                 |
| Android  | 700 lines    | 1000 lines, 500 chars each | 100 entries  | 10KB                 |

#### **Stacktrace limits per crash**

Limits are configurable; these are the default limits.

| Platform | Stacktrace Frames | Background Threads |
| -------- | ----------------- | ------------------ |
| iOS      | 50 lines/frames   | No limits          |
| Android  | 100 lines/frames  | 200 threads        |

#### Bug Reporting

Details of what’s included in Bug Reporting, including allowances, and retention.

| Item                      | Value                                                                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Event allowance           | Unlimited bug reports, subject to the general rate limit for non-critical events (30,000 requests/min/App) |
| Data retention            | 365 days                                                                                                   |
| Bug Reporting Sync timing | Bugs are sent in real time.                                                                                |

#### **Log limits per bug**

Limits are configurable; these are the default limits.

| Platform | Console Logs | Luciq Logs                 | Network Logs | Network Request Size |
| -------- | ------------ | -------------------------- | ------------ | -------------------- |
| iOS      | 500 lines    | 1000 lines, 500 chars each | 100 entries  | 10KB                 |
| Android  | 700 lines    | 1000 lines, 500 chars each | 100 entries  | 10KB                 |

#### Application Performance Monitoring (APM)

This section outlines APM limits, including supported event types, rate limits, and data retention.

| Item            | Value                                                                                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Event allowance | Unlimited traces (app launches, screens, networks, hangs, screen rendering).Ingest shares the 2,000,000 requests/min/App pool with other non-critical events. |
| Data retention  | 8 Weeks                                                                                                                                                       |
| APM Sync timing | Session data is synced every 6 hours, but only after the user reopens the app.                                                                                |

#### **Group limits per metric**

Limits are configurable; these are the default limits.

<table><thead><tr><th width="104.6357421875">Platform</th><th>Network</th><th>Flows</th><th>Screen Loading</th><th>Screen Rendering</th><th>Webviews</th></tr></thead><tbody><tr><td>iOS &#x26; Android</td><td>10,000 URL Groups</td><td>10,000 Flows</td><td>500 Screens</td><td>500 Screens</td><td>500 Webviews</td></tr></tbody></table>

#### Session Replay

What’s included in Session Replay usage, including ingestion limits, retention periods, and dashboard guarantees.

| Item                       | Value                                                                         |
| -------------------------- | ----------------------------------------------------------------------------- |
| Event allowance            | Unlimited sessions, rate-limited at 6,000 requests/min/App                    |
| Data retention             | 4 weeks                                                                       |
| Session Replay Sync timing | Session data is synced every 6 hours, but only after the user reopens the app |

#### Surveys

What’s included in Surveys usage, including ingestion limits, retention periods, and dashboard guarantees.

| Item                | Value                                                      |
| ------------------- | ---------------------------------------------------------- |
| Event allowance     | Unlimited Surveys, rate-limited at 35,000 requests/min/App |
| Data retention      | 365 days                                                   |
| Surveys Sync timing | Surveys are sent in real time.                             |

#### Rollout Management

What’s included in Rollout Management usage, including ingestion limits and retention periods.

| Item            | Value              |
| --------------- | ------------------ |
| Event allowance | Unlimited Rollouts |
| Data retention  | No Data Retention  |

### Version History:

| Version          | Link                                                                                                                                                                                                                      | Effective Date   |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| Current Version  | <https://docs.luciq.ai/docs/license-entitlements-and-restrictions#/>                                                                                                                                                      | November 5, 2025 |
| Previous Version | [https://docs.luciq.ai/docs/july-2025-license-entitlements-and-restrictions#/](https://docs.luciq.ai/organization-settings/billing/license-entitlements-and-restrictions/july-2025-license-entitlements-and-restrictions) | July 1, 2025     |
