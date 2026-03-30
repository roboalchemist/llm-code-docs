# Source: https://checklyhq.com/docs/detect/uptime-monitoring/url-monitors/configuration.md

# Source: https://checklyhq.com/docs/detect/uptime-monitoring/tcp-monitors/configuration.md

# Source: https://checklyhq.com/docs/detect/uptime-monitoring/icmp-monitors/configuration.md

# Source: https://checklyhq.com/docs/detect/uptime-monitoring/dns-monitors/configuration.md

# Source: https://checklyhq.com/docs/detect/synthetic-monitoring/playwright-checks/configuration.md

# Source: https://checklyhq.com/docs/detect/synthetic-monitoring/api-checks/configuration.md

# Source: https://checklyhq.com/docs/communicate/dashboards/configuration.md

# Source: https://checklyhq.com/docs/communicate/alerts/configuration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Alert Configuration

> Complete guide to configuring alert settings, escalation strategies, retry mechanisms, and threshold alerting in Checkly for optimal incident response.

Alert configuration controls **when** and **how often** you receive notifications when checks fail, degrade, or recover. Proper configuration minimizes alert fatigue while ensuring critical issues receive immediate attention.

## Configuration Hierarchy

Checkly provides a three-tier configuration system that allows for flexible alert management across your organization:

<Accordion title="Account Level">
  * Applied to all checks unless overridden
  * Organization-wide defaults
  * Simplifies management at scale
  * Consistent baseline behavior
</Accordion>

<Accordion title="Group Level">
  * Override account defaults for checks within Groups
  * Team-based alert preferences
  * Service-specific requirements
  * Departmental escalation policies
</Accordion>

<Accordion title="Check Level">
  * Fine-tune specific check behavior
  * Handle special requirements
  * Debug and testing scenarios
  * Legacy system accommodations
</Accordion>

<Note>
  ### Configuration Inheritance

  Understanding how settings cascade through the hierarchy:

  1. **Check-level settings** always take highest precedence
  2. **Group-level settings** override account defaults for member checks
  3. **Account-level settings** provide the baseline for all other configurations
  4. **Explicit overrides** can be enabled/disabled at group level
</Note>

## Alert Configuration

### Account-Level

Configure organization-wide defaults that apply to all checks:

<Frame>
    <img src="https://mintcdn.com/checkly-422f444a/riTtJrRZAx73iREC/images/docs/images/alerting/alert-settings.png?fit=max&auto=format&n=riTtJrRZAx73iREC&q=85&s=0b55a21417289d26ee34140a8ff30089" alt="Account-level alert settings" width="1400" height="1099" data-path="images/docs/images/alerting/alert-settings.png" />
</Frame>

**Account Settings Benefits:**

* Consistency: Uniform alerting behavior across all monitoring
* Efficiency: Configure once, apply everywhere
* Compliance: Meet organizational alerting requirements
* Scalability: Easy to manage large numbers of checks

### Group-Level

Configure alerts for teams and service categories:

<img src="https://mintcdn.com/checkly-422f444a/riTtJrRZAx73iREC/images/docs/images/alerting/alert-settings-group.png?fit=max&auto=format&n=riTtJrRZAx73iREC&q=85&s=33e3aadf78cc7d64b987ec7d004d19f0" alt="Group-level alert settings" width="1400" height="1454" data-path="images/docs/images/alerting/alert-settings-group.png" />

<Note>
  #### Group Override

  Configure how group settings interact with individual checks:

  **If checked, Group settings override individual check settings**

  * Group settings take precedence
  * Ensures consistency within teams
  * Prevents individual check drift
  * Simplifies management

  **If unchecked, individual check settings take precedence**

  * Check-level customization allowed
  * Handle special cases easily
  * Legacy system accommodation
  * Granular control when needed
</Note>

### Check-Level

Fine-tune alerting for specific checks with unique requirements:

<Frame>
    <img src="https://mintcdn.com/checkly-422f444a/riTtJrRZAx73iREC/images/docs/images/alerting/alert-settings-check.png?fit=max&auto=format&n=riTtJrRZAx73iREC&q=85&s=23c4def5a21cc448501156bb185159d9" alt="Check-level alert settings" width="1400" height="1264" data-path="images/docs/images/alerting/alert-settings-check.png" />
</Frame>

<Note>
  Start with conservative alert settings and gradually tune based on your team's response patterns and service reliability characteristics. Too many alerts can be worse than too few.
</Note>

## Escalation Configuration

<Tip>
  **Monitoring as Code**: Learn more about [configuring escalation strategies for your Checkly constructs](/constructs/alert-escalation-policy).
</Tip>

The escalation box allows you to decide when an alert should be triggered. We give you three options that are applied to all checks:

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/checkly-422f444a/kI4TboyZqmjcifb3/images/next/alerts-escalation-light.png?fit=max&auto=format&n=kI4TboyZqmjcifb3&q=85&s=433ed26a3a8a912523dd21180dd0f50a" alt="Light mode interface" width="1094" height="538" data-path="images/next/alerts-escalation-light.png" />

  <img className="hidden dark:block" src="https://mintcdn.com/checkly-422f444a/kI4TboyZqmjcifb3/images/next/alerts-escalation-dark.png?fit=max&auto=format&n=kI4TboyZqmjcifb3&q=85&s=e8627e727c4757f8b6f5411b02d39800" alt="Dark mode interface" width="1094" height="522" data-path="images/next/alerts-escalation-dark.png" />
</Frame>

### Run-Based Escalation

Get alerted when a check has failed a number of times consecutively. We call this a *Run Based* escalation. Note that failed checks retried
from a different region are not considered "consecutive".

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/checkly-422f444a/AjkvXEcScX1FkLbF/images/next/alerts-run-escalation-light.png?fit=max&auto=format&n=AjkvXEcScX1FkLbF&q=85&s=fd40fbfd8a7dff7c22ed116bcb6bc1f7" alt="Light mode interface" width="1060" height="70" data-path="images/next/alerts-run-escalation-light.png" />

  <img className="hidden dark:block" src="https://mintcdn.com/checkly-422f444a/kI4TboyZqmjcifb3/images/next/alerts-run-escalation-dark.png?fit=max&auto=format&n=kI4TboyZqmjcifb3&q=85&s=966b9433bcea61179dbd2083b3fb95d9" alt="Dark mode interface" width="1060" height="76" data-path="images/next/alerts-run-escalation-dark.png" />
</Frame>

**How it works:**

* Consecutive Failure Counting
* Counts failed check runs in sequence
* Resets counter on successful run
* Cross-location failures count as one run
* Retries don't count as separate runs

**Best for: Stable Systems**

* Predictable failure patterns
* Clear success/failure states
* Services with known reliability
* APIs with consistent behavior

### Time-Based Escalation

We alert you when a check is still failing after a period of time, regardless of the amount of check runs that are failing.
This option should mostly be used when checks are run very regularly, i.e. once every minute or five minutes.

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/checkly-422f444a/kI4TboyZqmjcifb3/images/next/alerts-duration-light.png?fit=max&auto=format&n=kI4TboyZqmjcifb3&q=85&s=4390043d5cd6bb60ec1764617700887d" alt="Light mode interface" width="1060" height="72" data-path="images/next/alerts-duration-light.png" />

  <img className="hidden dark:block" src="https://mintcdn.com/checkly-422f444a/kI4TboyZqmjcifb3/images/next/alerts-duration-dark.png?fit=max&auto=format&n=kI4TboyZqmjcifb3&q=85&s=9d751b675af15441c67110e513c96cd3" alt="Dark mode interface" width="1060" height="74" data-path="images/next/alerts-duration-dark.png" />
</Frame>

**How it works:**

* Monitors failure duration, not count
* Ideal for high-frequency checks
* Ignores individual run results
* Focuses on sustained problems

**Best for: High-Frequency Monitoring**

* Checks running every 1-5 minutes
* Services with intermittent issues
* Rate-limited APIs
* Network-dependent services

### Location-Based Escalation

This option can be selected in addition to the run or time-based escalation settings and only affect checks running in [parallel](/monitoring/global-locations/#parallel) with two or more locations selected.

When enabled, alerts will only be sent when the specified percentage of locations are failing. Use this setting to reduce alert noise and fatigue for services that can handle being unavailable from some locations before action is required.

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/checkly-422f444a/kI4TboyZqmjcifb3/images/next/alerts-location-escalation-light.png?fit=max&auto=format&n=kI4TboyZqmjcifb3&q=85&s=4a0d49d87d65d9c8fba8761647cbaad6" alt="Light mode interface" width="1094" height="140" data-path="images/next/alerts-location-escalation-light.png" />

  <img className="hidden dark:block" src="https://mintcdn.com/checkly-422f444a/kI4TboyZqmjcifb3/images/next/alerts-location-escalation-dark.png?fit=max&auto=format&n=kI4TboyZqmjcifb3&q=85&s=33d6d65eb6c7b446ae61b6382feb862a" alt="Dark mode interface" width="1094" height="140" data-path="images/next/alerts-location-escalation-dark.png" />
</Frame>

**Benefits:**

* Reduces false positives from regional issues
* Focuses on global service problems
* Accommodates CDN and geo-distributed services
* Filters out single-location network problems

## Reminder Configuration

Configure follow-up notifications for unresolved incidents.

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/checkly-422f444a/kI4TboyZqmjcifb3/images/next/alerts-reminder-light.png?fit=max&auto=format&n=kI4TboyZqmjcifb3&q=85&s=e0d203d2842bdd3de1a29276e6bc7630" alt="Light mode interface" width="1356" height="192" data-path="images/next/alerts-reminder-light.png" />

  <img className="hidden dark:block" src="https://mintcdn.com/checkly-422f444a/kI4TboyZqmjcifb3/images/next/alerts-reminder-dark.png?fit=max&auto=format&n=kI4TboyZqmjcifb3&q=85&s=980b96659d73713b41fc299f141e876f" alt="Dark mode interface" width="1356" height="188" data-path="images/next/alerts-reminder-dark.png" />
</Frame>

Checkly automatically manages reminder lifecycle:

<Steps>
  <Step title="Initial Alert Sent">
    Primary alert sent to configured channels when escalation threshold is met
  </Step>

  <Step title="Reminder Timer Starts">
    Reminder countdown begins based on configuration
  </Step>

  <Step title="Reminder Notifications">
    Follow-up alerts sent at configured intervals
  </Step>

  <Step title="Automatic Cancellation">
    All pending reminders cancelled when check recovers
  </Step>

  <Step title="Escalation Handling">
    Optional escalation to different teams/channels after maximum reminders
  </Step>
</Steps>

<Note>
  When a check failure is resolved, we cancel any outstanding reminders so you don't get mixed signals.
</Note>

## Muting and Temporary Controls

Toggling the "mute" checkbox on a check stops the sending of all alerts but keeps the check running. This is useful when
your check might be flapping or showing other unpredictable behavior. Just mute the alerts but keep the check going while
you troubleshoot.

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/checkly-422f444a/kI4TboyZqmjcifb3/images/next/alerts-muted-light.png?fit=max&auto=format&n=kI4TboyZqmjcifb3&q=85&s=fea43501080da018731a21a580750b7c" alt="Light mode interface" width="1106" height="460" data-path="images/next/alerts-muted-light.png" />

  <img className="hidden dark:block" src="https://mintcdn.com/checkly-422f444a/kI4TboyZqmjcifb3/images/next/alerts-muted-dark.png?fit=max&auto=format&n=kI4TboyZqmjcifb3&q=85&s=f6b4885bbb9ab5609653d47d7a4f7a94" alt="Dark mode interface" width="1100" height="460" data-path="images/next/alerts-muted-dark.png" />
</Frame>

<Warning>
  Always test your alert configuration changes in non-production environments first. Failed alert delivery during an actual incident can significantly impact response time.
</Warning>

<Tip>
  Use Checkly's alert notification log to analyze delivery patterns and identify optimization opportunities. Look for channels with high failure rates or excessive alert volume.
</Tip>


Built with [Mintlify](https://mintlify.com).