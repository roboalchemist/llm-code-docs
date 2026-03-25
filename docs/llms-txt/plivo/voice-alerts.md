# Source: https://plivo.com/docs/voice/use-cases/voice-alerts.md

# Source: https://plivo.com/docs/voice/concepts/voice-alerts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Voice Alerts (New)

> Send automated voice notifications and alerts to phone numbers

Voice Alerts, developed by Plivo, is an active monitoring system that employs an advanced algorithm capable of detecting voice traffic anomalies in real-time. Voice Alerts swiftly identifies and resolves potential issues to maintain a reliable, efficient voice service for our users.

Voice Alerts leverages a sophisticated algorithm to detect anomalies in voice traffic, continuously monitoring various parameters to pinpoint deviations from expected norms. The system keeps a vigilant eye on multiple factors, including calls per second (CPS) utilization, errors in posting callbacks to customer callback servers, configuration errors that may result in call failures, and call patterns.

Upon detecting an anomaly, Voice Alerts promptly emails customers about the identified issue. This alert allows users to rectify the problem quickly.

## Alerts category

### Call dequeue delays

Long call queues are often caused by breaching the CPS limit. Voice Alerts diligently monitors the duration of calls in the queue. While a small number of queued calls may not significantly impact delays, a substantial accumulation could lead to delayed call dispatch and potentially affect the timely delivery of notifications to your customers.

To tackle this issue, Voice Alerts will automatically notify your registered email address if calls remain in the queue for over two minutes. If you consistently encounter prolonged queue times, we suggest reaching out to our support to discuss increasing the CPS limit.

### Error in posting event callbacks

Plivo customers often depend on event callbacks to determine the call flow. Any issues in posting these callbacks could lead to call failures. Voice Alerts will monitor these failures and notify your registered email if we detect more than 5% of callback failures.

If you receive one of these emails, we advise checking the health of your callback server and address any issues you may have.

### Configuration errors

Configuration errors can lead to call failures. A configuration error could be as simple as an invalid XML returned in the response. Voice Alerts will monitor for these errors and raise an alert if we detect more than 5% of such failures.

If you receive this notification, we advise you to check the application logic from your end.

### Call pattern alerts

Call pattern alerts encompass a variety of parameters designed to detect unusual calling patterns associated with your account. They are intended to notify customers proactively of irregular activities and safeguard the overall ecosystem.

#### Call volume, call duration, and spend

Voice Alerts monitors the call volume, call duration and spending of your voice traffic on a country level. Compared to the previous usage, any usual spike in these parameters is alarming as this can also be an effect of some bad actors in the ecosystem inflating volume. Voice Alerts has an intelligent algorithm to map your current usage with historical data. Any abnormal deviation in the current traffic will alert you to review the call samples.

#### Calls to premium/shared cost numbers

Most businesses do not require placing calls to premium or shared-cost numbers. Any spike in calls to these destination numbers is a red flag. Voice Alerts proactively identifies such calls and notifies your registered email address.

#### Calls to repeated destinations or the same range of destination numbers

Multiple calls to repeated destinations and calls to the same range of destination numbers may be a sign of robocalling activity. Voice Alerts proactively identifies such calls and notifies your registered email address.

#### Short-duration and zero-duration calls

Short-duration calls are answered calls with a duration of less than or equal to six seconds. A spike in both short-duration and zero-duration calls indicates that either intended call recipient is rejecting the calls or that your call is being blocked by someone in the call flow chain. Investigating any abnormal spike in short-duration and zero-duration calls is necessary to maintain good stats. Voice Alerts compares your previous usage and will notify you if there is an abnormal spike.

#### High-risk countries

An abnormal spike in calls towards high-risk destinations can incur high costs, and should be cause for alarm. Voice Alerts will notify your registered email if there is a surge in calls to one or more high-risk countries listed below:

* Albania
* Belarus
* Bulgaria
* Cuba
* Ecuador
* Haiti
* Ivory Coast
* Papua New Guinea
* Samoa
* Latvia
* Somalia
* Gambia
* Zimbabwe
* Tunisia
* Guinea
* Liberia
* Solomon Islands
* Vanuatu
