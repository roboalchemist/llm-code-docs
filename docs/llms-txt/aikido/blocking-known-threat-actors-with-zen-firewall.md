# Source: https://help.aikido.dev/zen-firewall/zen-features/blocking-known-threat-actors-with-zen-firewall.md

# Blocking Known Threat Actors with Zen Firewall

Zen Firewall by Aikido helps you control access to your application based on known malicious actors and threats. This feature enhances your security measures by leveraging [CrowdSec's](https://www.crowdsec.net/) comprehensive IP-based threat intelligence to block various types of malicious actors and activities. Unlike content or pattern-based blocking, this feature focuses solely on IP address lists for efficient and reliable traffic filtering.

> Important: Actor blocking operates independently of the global [Blocking/Detection Mode](https://help.aikido.dev/zen-firewall/zen-features/blocking-vs-detection-mode-in-zen-firewall) setting. When you enable actor blocks, they will always be enforced, even if Zen is in Detection Mode.

## Use Cases <a href="#use-cases" id="use-cases"></a>

* 🛡️ Block Malicious Botnets: Prevent access from known botnet infrastructure
* 🔒 Stop Brute Force Attacks: Protect against credential stuffing and password attacks
* ⚔️ Prevent DoS Attacks: Block known HTTP DoS attackers
* 🚫 Reduce Exploitation Risk: Block traffic from known HTTP exploit actors
* 🕵️ Control Anonymous Access: Manage traffic from known proxy/VPN services
* 🔍 Prevent Scanning: Block reconnaissance from known internet scanners
* 🛑 WordPress Protection: Block known WordPress attackers

## How to block known threat actors <a href="#how-to-block-known-threat-actors" id="how-to-block-known-threat-actors"></a>

Select a specific app and continue to the **Firewall** tab. Click the "**Manage Threat Actors**" next to "**Block IPs used by known threat actors**" to configure known threat actors blocking.

![Demo app firewall settings interface for managing attacks, bots, threat actors, and country-based blocks.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2F2GToNNenLJGwfMMthBEs%2FScreenshot%202025-10-30%20at%2012.01.21.png?alt=media\&token=62750671-1a0e-4eab-b633-250d89b09d2e)

Use the **Known Threat Actors** dropdown to select the lists you want to enable and click on "**Manage Threat Actors**"

{% hint style="info" %}
Not all lists are available on all plans. Contact our support team if you have any questions about list availability for your subscription.
{% endhint %}

There's many different types of list available, for each it's possible to ignore, monitor or block the IP's in the list. Click on "**Update Threat Actors"**, when you're done.

![Select and block known threat actors from accessing your app with Aikido.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FZMzovyLLl73BbllsyvE5%2FScreenshot%202025-10-30%20at%2012.01.40.png?alt=media\&token=a815177d-95e1-46c1-8138-b11e55e582b7)

{% hint style="info" %}
Note that threat actors blocking is not immediate; it takes up to a minute for the block to take effect.
{% endhint %}

## Available threat actor lists <a href="#available-threat-actor-lists" id="available-threat-actor-lists"></a>

* [Botnet Actors](https://app.crowdsec.net/blocklists/65a56c160469607d9badb813)
* [Bruteforce Attackers](https://app.crowdsec.net/blocklists/66ec368bc0ad850aec9c02d4)
* [HTTP DoS Attackers](https://app.crowdsec.net/blocklists/660fc8d678dc68ae3ef065e4)
* [HTTP Exploit Attackers](https://app.crowdsec.net/blocklists/660fc91ba69671df549e3bec)
* [Proxy/VPN](https://app.crowdsec.net/blocklists/65a56839ec04bcd4f51670be)
* [Public Internet Scanners](https://app.crowdsec.net/blocklists/65f972eb807e06de7a0e3e65)
* [WordPress Attackers](https://app.crowdsec.net/blocklists/65a56c1a0469607d9badb814)
