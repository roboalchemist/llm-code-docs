# Source: https://docs.statsig.com/feature-flags/safeguards-manage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage a Safeguard

> Learn how to view and manage safeguards for your feature flags

## View a Safeguard

To view an existing Safeguard, tap the blue pill on your Feature Gate's targeting rule. Here you can see how your Safeguard is currently defined and make any changes if you want. You can add/remove alerts, change the action, or adjust the evaluation period.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/safeguards/view-safeguard.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=e9b8a3fb3bfc3982297135e2f7e5bee2" alt="View an existing Safeguard" width="1230" height="282" data-path="images/safeguards/view-safeguard.png" />
</Frame>

## When a Safeguard triggers

When a safeguard is triggered because of an alert:

* The configured action executes automatically (rollback/pause/complete)
* A banner appears on the targeting rule with action taken, timestamp, and diagnostic link
* Further rule modifications are blocked until the alert is resolved
* Notifications are sent per your alert configuration

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/qCcEV56Te17RWbGF/images/safeguards/safeguard-rule-banner.png?fit=max&auto=format&n=qCcEV56Te17RWbGF&q=85&s=9f3e092381075550a283b0e8b861a106" alt="Safeguard is triggered on a rule" width="1228" height="280" data-path="images/safeguards/safeguard-rule-banner.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).