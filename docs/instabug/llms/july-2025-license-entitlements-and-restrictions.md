# Source: https://docs.instabug.com/organization-settings/billing/license-entitlements-and-restrictions/july-2025-license-entitlements-and-restrictions.md

# July 2025 License Entitlements and Restrictions

Effective for Enterprise deals starting July 28, 2025

This page describes Luciq’s license entitlements, restrictions and definitions for Luciq Enterprise customers. See the glossary below if any word is unclear.

For more information on the licensing terms please see [luciq.ai/terms](https://www.luciq.ai/terms)

### Glossary

| Term                           | Definition                                                                                                                                            |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account                        | Container for your Apps, Users, and Data in Luciq.                                                                                                    |
| App                            | One mobile application bundle ID connected to Luciq.                                                                                                  |
| User                           | A user who downloaded your App, whether the user opted in or out of analytics sharing.                                                                |
| Daily Active Users (DAU)       | The number of unique users who start at least one Session in any 24-hour window. Your Account DAU equals the sum of DAU for every App in the Account. |
| Session                        | One instance of a User running the app for at least one second.                                                                                       |
| SDK (Software Development Kit) | The Luciq library you embed in your App to collect telemetry such as crashes, performance data, and user feedback.                                    |
| Telemetry                      | Data automatically sent from the SDK to Luciq, including session counts, crashes, and performance metrics.                                            |
| Trace                          | A timed performance span such as a screen load or network call.                                                                                       |

### 1) What You Are Buying?

This section summarizes what your license includes and how usage is measured. As part of your license, you purchase a **range of daily active users (DAU)** for any of the following products:

1. Bug Reporting
2. Crash Reporting
3. Application Performance Monitoring (APM)
4. Session Replay
5. Surveys
6. Rollout management
7. App Ratings and Reviews

### 2) DAU Definitions and Session Entitlements

Here’s how we define and measure usage across users and sessions, and how that translates into your entitlements.

#### How we calculate DAU?

Luciq reconciles two trusted signals:

1. **Third-party app-store analytics** (for example, Sensor Tower) that report how many people opened your App each day.
2. **First-party telemetry** from the Luciq SDK embedded in your App.

We compare the two streams and count the higher value so your invoice reflects real-world usage.

#### Session Entitlement

For every 1 DAU you are entitled to **180 Sessions per month**.

### 3) Role Types: Who Can Do What?

This section outlines the access levels available for team members within your account.

| Role      | Access Scope                                              |
| --------- | --------------------------------------------------------- |
| Member    | Edit rights on assigned Apps                              |
| Associate | Read-only rights on assigned Apps, with limited debugging |
| Observer  | Read-only on aggregated analytics                         |

The Enterprise Plan includes **100 Observers**. Additional Observers can be provisioned upon written request. You may add additional Members or Associates for a fee at any time.

### 4) Platform Entitlements

Purchase of the Luciq Platform entitles you to:

* Unlimited Apps per account
* Unlimited available integrations

### 5) Usage Entitlements

This section defines what each product includes and the limits associated with them. You only receive access to products listed on your Order Form.

#### Crash Reporting

What you get with Luciq’s Crash Reporting, including event limits, retention, and dashboard performance guarantees.

| Item              | Value                                                                                                                                                                                                                                                      |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Event allowance   | <p>Luciq supports unlimited events, constrained only by the following rate limits (requests/min/app):</p><ul><li>Crashes: 3,000</li><li>ANR Errors: 2,000</li><li>Non-Fatal Errors: 2,000</li><li>Force Restarts: 2,000</li><li>App Hangs: 2,000</li></ul> |
| Crash-group cap   | 5,000 groups in the dashboard list                                                                                                                                                                                                                         |
| Pattern search    | Up to 1,000 values returned                                                                                                                                                                                                                                |
| Data retention    | 180 days                                                                                                                                                                                                                                                   |
| Crash Sync timing | Crashes are sent on the next app launch (i.e., when the user reopens the app).                                                                                                                                                                             |

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

| Platform      | Network           | Flows        | Screen Loading | Screen Rendering | Webviews     |
| ------------- | ----------------- | ------------ | -------------- | ---------------- | ------------ |
| iOS & Android | 10,000 URL Groups | 10,000 Flows | 500 Screens    | 500 Screens      | 500 Webviews |

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
