# Source: https://help.aikido.dev/zen-firewall/zen-features/blocking-tor-traffic-with-zen-firewall.md

# Blocking or Monitoring Tor traffic with Zen Firewall

Zen Firewall by Aikido helps you identify and block users who are accessing your application through the [Tor network](https://www.torproject.org/). This feature enhances your security measures by providing visibility and control over [Tor-based traffic](https://www.torproject.org/).

> **Important**: Tor blocking operates independently of the global "[Blocking/Detection Mode](https://help.aikido.dev/zen-firewall/zen-features/blocking-vs-detection-mode-in-zen-firewall)" setting. When you enable tor blocking, it will always be enforced, even if Zen is in Detection Mode.

## Use Cases <a href="#use-cases" id="use-cases"></a>

* 🛡️ **Block or Monitor Tor Users**: Automatically prevent access from Tor exit nodes when needed for security compliance or risk mitigation
* 🔒 **Meet Compliance**: Satisfy regulatory requirements that mandate blocking anonymous proxy traffic
* 💳 **Protect Transactions**: Ensure financial transactions come from identifiable, non-anonymous sources

## How to block tor traffic <a href="#how-to-block-tor-traffic" id="how-to-block-tor-traffic"></a>

Select a specific app and continue to the **Firewall** tab. Click the toggle next to "**Block Tor Traffic"** to enable Tor blocking. You can Ignore, Monitor or Block Tor traffic.

![Firewall settings for a demo app with attack and Tor traffic blocking options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Ffa6GIKv4bBcjzGZRE3A9%2FScreenshot%202025-08-13%20at%2017.22.40.png?alt=media\&token=dd495b61-3cf3-4c07-ade4-d1c39161e15d)

{% hint style="info" %}
Note that Tor blocking is not immediate; it takes up to a minute for the block to take effect.
{% endhint %}
