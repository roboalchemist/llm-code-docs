# Source: https://help.aikido.dev/zen-firewall/miscellaneous/outbound-network-connections-for-zen.md

# Outbound Network Connections for Zen

Zen requires outbound internet access to function correctly.

During operation, Zen [sends data](https://help.aikido.dev/zen-firewall/miscellaneous/data-sent-by-aikido-zen) to the following Aikido services:

**EU-based domains:**

* guard.aikido.dev
* runtime.aikido.dev

**US-based domains:**

* guard.us.aikido.dev
* runtime.us.aikido.dev

**ME-based domains:**

* guard.me.aikido.dev
* runtime.me.aikido.dev

{% hint style="warning" %}
Both domains use dynamic IPs managed by Aikido’s cloud infrastructure.
{% endhint %}

If your environment restricts outbound traffic, allow these domains by hostname rather than IP address.
