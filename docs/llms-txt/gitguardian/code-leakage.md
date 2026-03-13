# Source: https://docs.gitguardian.com/honeytoken/code-leakage.md

# Detect code leakage on public GitHub

> Explains how GitGuardian detects when honeytokens are publicly exposed on GitHub and tags them accordingly for quick identification.

GitGuardian natively monitors all the commits on public GitHub for secrets getting leaked.

As for real secrets, whenever a honeytoken ends up in a public GitHub repository, it will be detected by GitGuardian, and this will trigger specific events.

Events originating from the IP addresses of GitGuardian monitoring of public GitHub are marked as `GitGuardian Public Monitoring IP`, and as a result, the honeytoken itself will receive tag `Publicly exposed`.

![Publicly exposed mechanism](/img/honeytoken/publicly-exposed-mechanism.png)

Clicking the `Publicly exposed` tag of the honeytoken will display all the public GitHub commits detected by GitGuardian as containing the honeytoken.

:::caution
This specific bit of feature (returning the list of public GitHub commits) is unfortunately not available for self-hosted installations.
:::

Publicly exposed honeytokens can be quickly identified and filtered from the honeytoken list.

![Publicly exposed filter](/img/honeytoken/publicly-exposed-filter.png)
