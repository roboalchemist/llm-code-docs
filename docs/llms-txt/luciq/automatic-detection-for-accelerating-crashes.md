# Source: https://docs.luciq.ai/product-guides-and-integrations/product-guides/automation-and-workflows/alerts-and-rules/automatic-detection-for-accelerating-crashes.md

# Automatic Detection for Accelerating Crashes

### Overview

Luciq's new automatic detection of accelerating crashes alert type allows you to safely ignore non-critical crashes by notifying you only when a crash starts accelerating. This feature ensures that you can focus on significant crashes that require immediate attention without being overwhelmed by sporadic, non-critical crashes.

#### Use Case

Consider the scenario where a crash occurs intermittently. Initially, this crash might not warrant immediate action. However, if the frequency of this crash begins to increase rapidly, it could indicate a growing problem that needs addressing. With automatic detection of accelerating crashes, Luciq monitors the rate of a crash’s occurrences and alerts you when there is a notable acceleration.

**Examples:**

1. **Sudden Spike in Crash Occurrences**:
   * In this graph, you can see a crash occurrence that suddenly spikes. Luciq detects this rapid increase and triggers the accelerating crash alert.<br>

     <figure><img src="https://files.readme.io/6c19ec6-image.png" alt=""><figcaption></figcaption></figure>
2. **Stable Crash starting to accelerate**:
   * This graph shows a crash that was stable for a while, started to accelerate, stabilized again, and then accelerated once more. We identify both acceleration patterns and notify you accordingly.<br>

     <figure><img src="https://files.readme.io/b7d0e17-image.png" alt=""><figcaption></figcaption></figure>

#### Technical Details

We run an algorithm on incoming crashes to analyze crash patterns and identify accelerations. We do so by comparing the occurrence of each particular crash against its historical average, determining whether there is a significant increase. The decision-making process is outlined in the flow chart below:

<figure><img src="https://files.readme.io/6fdfd8b-image.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The default values used in this flow chart are configurable to fit your company's specific needs. Please contact our customer support team ([support@luciq.com](mailto:support@instabug.com)) for any customization requests, and we will adjust these settings accordingly.
{% endhint %}

### Alert Creation

You can create a new alert for detecting accelerating crashes by following these steps:

1. Go to the Alerts & Rules section in your Luciq dashboard.
2. Select **“For → Crashes”**.
3. Choose **“Trigger → A crash is accelerating”**.

<figure><img src="https://files.readme.io/ba6302f1520d5821fc28462967b30ab8b41d27e765854ccffeedbe21e6c75195-image.png" alt=""><figcaption></figcaption></figure>

#### Available Alert Conditions

To provide you with precise control over which accelerating crashes trigger alerts, we've included several customizable conditions:

* **Exception Message**: Specify the exception message text of crashes you want to be alerted on.
* **Path (Package)**: Get alerted on crashes occurring within specific packages or paths.
* **Filename**: Focus on crashes originating from particular files.
* **Crash Type**: Differentiate between various crash types (e.g., OOMs, ANRs).
* **Tags**: Filter crashes based on assigned tags.
* **Priority**: Restrict alerts to crashes with a specific priority.
* **Team**: Restrict alerts to crashes owned by specific teams.
* **Assignee**: Restrict alerts to crashes owned by specific team members.
* **Total Occurrences Count Greater Than X**: Only evaluate crashes with a total occurrence count above a set threshold.
* **Total Affected Users Greater Than X**: Only evaluate crashes impacting more than a specified number of users.

#### Available Actions

Once an accelerating crash is detected, you can choose from a variety of actions to ensure prompt resolution:

* **Forwarding**:
  * **Jira**: Automatically create and assign Jira issues.
  * **Slack**: Send notifications to specific Slack channels.
  * **PagerDuty**: Trigger incidents in PagerDuty.
  * **Webhook**: Integrate with custom webhooks.
  * **MS Teams**: Notify teams via Microsoft Teams.
* **Email**: Send detailed crash reports via email to designated recipients.
* **Assigning to Team/Member**: Automatically assign the crash to the relevant team or team member.
* **Changing Status/Priority**: Update the status or priority of the crash for better tracking.
* **Adding a Tag**: Tag the crash for easier identification and filtering.

By leveraging these alert conditions and actions, you can efficiently manage and resolve accelerating crashes.

### Tracking the Accelerating Crash

Once an accelerating crash is detected and the alert is triggered, it will be reflected on the **Triggered Alerts** page in your Luciq dashboard. You can track and manage all triggered alerts from this page, ensuring that you stay informed about any accelerating crashes and take appropriate action in a timely manner.
