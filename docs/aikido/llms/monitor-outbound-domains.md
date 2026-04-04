# Source: https://help.aikido.dev/zen-firewall/zen-features/monitor-outbound-domains.md

# Monitor Outbound Domains

Zen Firewall by Aikido allows you to monitor outbound domains and IP addresses.

### Use Cases <a href="#use-cases" id="use-cases"></a>

* **Detection of Shadow IT:** are developers knowingly or unknowingly sharing production data with 3rd parties (eg [api.openai.com](http://api.openai.com) )
* **PII Leakage**: Avoid accidental leakage of PII or sensitive data to 3rd parties
* **Compliance:** Map existing data streams for compliance.

> When you have setup Zen, outbound domain monitoring works **out-of-the-box.**

### Future <a href="#future" id="future"></a>

* Block certain outbound domains so app is safe against SSRF
* PII leakage to unsanctioned 3rd party services

### How to monitor your outbound domains <a href="#how-to-monitor-your-outbound-domains" id="how-to-monitor-your-outbound-domains"></a>

Select a specific app and continue to the Outbound Domains tab. You will get a full overview of all outbound domains.

![Demo App outbound domains table showing hostnames, ports, and last seen times.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fc7hTcSV8lWEaRag4NfJe%2FScreenshot%202025-08-13%20at%2017.30.19.png?alt=media\&token=cd2a6fa4-47e2-45a7-a96d-c2ede5041a69)

### Get notified when new outbound domains were detected <a href="#get-notified-when-new-outbound-domains-were-detected" id="get-notified-when-new-outbound-domains-were-detected"></a>

Knowing when your apps connect to new external destinations is crucial for security and oversight. Get alerted whenever an application makes an outbound connection to a hostname it hasn't contacted before.

To receive these alerts, go to the [**Services Overview**](https://app.aikido.dev/runtime/services) and click **Manage Alerts**. Find and enable the setting **"Send notifications for new outbound hostnames"**. On this same page, you can also fine-tune which specific apps trigger these alerts and choose your preferred Slack or Microsoft Teams channels.

![Configure Slack alerts by selecting apps, channel, and notification preferences for instant alerts.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-358030d8e909f861ac786d27deb16e84a601b943%2Fmonitor-outbound-domains_9e0a4d0b-ed14-4581-985a-24a399f5faba.png?alt=media)
