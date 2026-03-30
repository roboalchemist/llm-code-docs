# Source: https://docs.mailtrap.io/email-api-smtp/deliverability/deliverability-alerts.md

# Deliverability Alerts

Deliverability Alerts help you monitor your email performance by providing automated notifications about your sending metrics.

{% hint style="info" %}
A minimum of 500 emails per week is required to receive alerts, as the system needs sufficient data to provide meaningful statistics.
{% endhint %}

If you want, you can toggle the alerts off. However, we recommend keeping them enabled because a missed issue may affect your domain authority and sender reputation.

## Health Status Weekly

Health Status Weekly alerts are sent out on Mondays and provide a detailed preview of the following stats:

* Opened
* Clicks
* Bounces
* Unsubscribes
* Spam

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-a4267082e8c18bc0c134789ecc9779045b6ea308%2Fdeliverability-alerts-weekly-stats.png?alt=media" alt="Weekly stats table showing email metrics with color-coded status indicators for All good, Attention required, and Critical" width="563"><figcaption></figcaption></figure></div>

The report includes clearly color-coded comparisons to the previous week, making it immediately obvious if one or more stats need your attention or show a negative trend. Additionally, there are insights (digest explanations of the stats) to help you troubleshoot your email infrastructure faster.

## Integrate Mailtrap Alerts with Slack

Each Slack channel has a unique email address. You can leverage that to route Mailtrap Alerts directly to Slack. Here's how to do it on the desktop app:

{% stepper %}
{% step %}
Click the channel name in the header and select **Integrations**.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-3a0b8d3d8a76529aa5f617bfc8228837e707448d%2Fslack-channel-integrations.png?alt=media" alt="Slack channel settings showing Integrations tab highlighted with arrow" width="375"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Click **Send emails to this channel**, then the **Get Email Address** button.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-16d5cfe0ff6b7ab90bf9c194fe10b437195d6270%2Fslack-get-email-address.png?alt=media" alt="Slack modal showing Get Email Address button for sending emails to channel" width="375"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Navigate to the Deliverability Alerts page in Mailtrap, and paste the Slack email address into the field under **Who receives notifications?**

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-c9154ed305e8f0298a47a0ae3a358a78d9485fca%2Fdeliverability-alerts-settings.png?alt=media" alt="Mailtrap Deliverability Alerts settings page showing notification recipients field with Save button" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Click **Save** and all alerts will be routed to the Slack channel instead of your email.
{% endstep %}
{% endstepper %}

## Critical Alerts

{% hint style="warning" %}
Critical Alerts feature is currently switched off. We'll notify you once it's back on.
{% endhint %}

Critical Alerts are sent hourly (the system checks your metrics every three hours for the past 24 hours) when one or more of your critical stats are below the predetermined threshold.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-614c1e107dc21ce8bb17ccf17cc0b3295c4b89d5%2Fcritical-alerts-demo.gif?alt=media" alt="Animated demonstration of Critical Alerts notification appearing on mobile device" width="563"><figcaption></figcaption></figure></div>

The predetermined thresholds are based on extensive cross-industry research and examples of best practices.

{% hint style="info" %}
If you're getting a lot of false positives or negatives, feel free to reach out to us at <support@mailtrap.io>.
{% endhint %}
