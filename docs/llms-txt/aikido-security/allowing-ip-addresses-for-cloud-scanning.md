# Source: https://help.aikido.dev/cloud-scanning/connect-your-cloud/allowing-ip-addresses-for-cloud-scanning.md

# Allowing IP Addresses for Cloud Scanning

Aikido’s Cloud Scanning checks your cloud environments for misconfigurations (CSPM).

These scans are performed from a fixed set of Aikido IP addresses. To allow scanning, you may need to allowlist these IPs in your cloud provider.

{% hint style="warning" %}
This applies only to cloud misconfiguration scanning (CSPM).

Other Aikido features—such as [container scanning](https://help.aikido.dev/code-scanning/miscellaneous/allowing-ip-addresses-for-code-container-scanning), [code scanning](https://help.aikido.dev/code-scanning/miscellaneous/allowing-ip-addresses-for-code-container-scanning), or [api scanning](https://help.aikido.dev/dast-surface-monitoring/allowing-ip-addresses-for-dast-surface-monitoring)—do not use these IPs.
{% endhint %}

## Why allowlist our IPs?

Some cloud providers or firewall setups block requests from unknown sources. Adding Aikido’s IPs ensures our scanner can reach your environment and report on misconfigurations.

Common use cases in which you need to allowlist IP addresses include:

* Access to specific Azure resources, such as [Key Vaults](https://learn.microsoft.com/en-us/azure/key-vault/general/network-security#key-vault-firewall-enabled-ipv4-addresses-and-ranges---static-ips).
* 3rd-party monitoring systems detecting cloud API requests.

## Current IP addresses

The list of IP addresses used for cloud scanning can be found here:

#### EU-based IP addresses

* 34.240.182.181
* 52.31.217.247

#### US-based IP addresses

* 98.80.32.100
* 52.54.124.156

#### ME-based IP addresses

* 40.172.244.108
* 3.29.255.25
