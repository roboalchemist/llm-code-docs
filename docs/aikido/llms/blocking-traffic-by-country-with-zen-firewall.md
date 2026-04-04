# Source: https://help.aikido.dev/zen-firewall/zen-features/blocking-traffic-by-country-with-zen-firewall.md

# Blocking Traffic by Country with Zen Firewall

Zen Firewall by Aikido helps you control access to your application based on geographic location. This feature enhances your security measures by providing precise control over which countries can access your application.

> **Important**: Country blocking operates independently of the global "[Blocking/Detection Mode](https://help.aikido.dev/zen-firewall/zen-features/blocking-vs-detection-mode-in-zen-firewall)" setting. When you enable country blocks, they will always be enforced, even if Zen is in Detection Mode.

## Use Cases <a href="#use-cases" id="use-cases"></a>

* 🛡️ **Comply with Regulations**: Restrict access from countries based on compliance requirements
* 💰 **Reduce Fraud**: Block traffic from high-risk regions known for malicious activities
* 🔒 **Data Protection**: Limit access to specific geographic regions for data sovereignty
* ⚡ **Focus Resources**: Optimize performance by serving only your target markets

## How to monitor or block country traffic <a href="#how-to-block-country-traffic" id="how-to-block-country-traffic"></a>

Select a specific app and continue to the **Firewall** tab. Click the "**Manage Countries**" next to "**Block Traffic by Countries**" to configure Country blocking.

![Firewall settings interface for blocking attacks, bots, Tor traffic, threat IPs, and countries.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F4UlCUQuHn6PSQTCp1fAI%2FScreenshot%202025-10-30%20at%2012.03.07.png?alt=media\&token=bf6185d0-e5d2-461f-b979-885836856bbb)

You can either **select the countries to allow**, or **select the ones to block** using the blocking mode. Use the **Countries** dropdown to select the lists you want to enable and click on "**Save Changes**".&#x20;

![Interface for selecting and blocking IPs from specific countries.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FEwJMeB9PyvLOXdtYhOBU%2FScreenshot%202025-08-13%20at%2017.26.42.png?alt=media\&token=86e4d883-a5ba-4462-b20d-995ff0e1c530)

{% hint style="info" %}
Note that country blocking is not immediate; it takes up to a minute for the block to take effect.
{% endhint %}
