# Source: https://docs.nimbleway.io/nimble-sdk/proxy-api/nimble-ip-functions/using-ipv6-proxies.md

# Using IPv6 Proxies

IPv4 and IPv6 are versions of the Internet Protocol (IP), which is a set of rules for routing and addressing data so it can travel across networks and reach the correct destination.

**IPv4 (Internet Protocol version 4):**

* **IPv4** is the fourth version of the Internet Protocol and has been widely used since its development in the 1980s. It uses a 32-bit address scheme, which limits the number of unique addresses it can provide. This limitation led to the development of IPv6.
* **Example Address:** `192.168.1.1`

**IPv6 (Internet Protocol version 6):**

* **IPv6** is the most recent version of the Internet Protocol. It was developed to address the shortage of IP addresses available under IPv4. IPv6 uses a 128-bit address scheme, significantly increasing the number of available addresses.
* **Example Address:** `2001:0db8:85a3:0000:0000:8a2e:0370:7334`

Nimble's Residential Proxy pool includes both IPv4 and IPv6 IPs. Because IPv4 is still the predominant IP address, there are many more IPv4 addresses available, and some websites still require them.&#x20;

As such, we have enabled the option to use IPv6 addresses in addition to IPv4 addresses. Including IPv6 is set in your pipeline settings. This can be adjusted via the [Nimble Dashboard](https://docs.nimbleway.io/management-tools/nimble-dashboard/managing-pipelines) under a pipeline's configuration, or [Nimble Admin API's](https://docs.nimbleway.io/management-tools/nimble-admin-api/admin-api-reference) `/v1/account/pipelines/{pipelineName}` "Update a Pipeline" endpoint.
