# Source: https://help.aikido.dev/dast-surface-monitoring/allowing-ip-addresses-for-dast-surface-monitoring.md

# IP Addresses for Domain Scanning

Aikido uses dedicated IP addresses to perform scanning of your domains (DAST). To prevent connectivity issues, rate limiting, or security blocks, add these IPs to your firewall’s allowlist or other security software.  After this, rescan your domains to confirm connectivity.

{% hint style="warning" %}
To use 'Fetch OpenAPI by URL', you must also add the [Code & Container scanning IP addresses.](https://help.aikido.dev/code-scanning/miscellaneous/allowing-ip-addresses-for-code-container-scanning)
{% endhint %}

**EU-based IP addresses:**

* 3.248.4.169
* 54.76.211.68
* 54.228.156.63
* 54.247.155.164
* 18.200.152.99
* 18.202.99.112
* 52.48.122.82
* 54.194.175.200

**US-based IP addresses**

* 98.85.190.95
* 52.204.144.1
* 44.209.56.130
* 18.210.114.117
* 35.168.38.209
* 35.173.56.162
* 54.227.161.94
* 44.209.154.183

**ME-based IP addresses**

* 158.252.118.40
* 158.252.52.197
* 40.172.160.56

**Optional IP addresses (used for troubleshooting with support):**

* 79.127.239.171

#### Request Headers

All requests from Aikido's scans include one of the following headers, which can also be used for allowlisting:

* `aikido-scan-agent/1.0`

## Third party provider instructions <a href="#third-party-provider-instructions" id="third-party-provider-instructions"></a>

For instructions on whitelisting IP addresses with third-party providers, refer to the following resources:

* [Cloudflare WAF](https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-ips-in-allowlist/)
  * Cloudflare Turnstile does not support allowlisting specific client IP addresses. If you need to [bypass Turnstile for Aikido scanning traffic, you must do it in your application code.](https://developers.cloudflare.com/turnstile/tutorials/conditionally-enforcing-turnstile/) We recommend bypassing only when both conditions are true:
    1. The request originates from an Aikido IP range
    2. The request includes the `aikido` User Agent in headers as described above
* [Azure WAF](https://learn.microsoft.com/en-us/azure/web-application-firewall/ag/custom-waf-rules-overview)
* [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-ipset-match.html).
  * For WAFs behind Application Load Balancers or CloudFront, your [WAF should check the last IP address in the `X-Forwarded-For` header](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-forwarded-ip-address.html).
* [Vercel WAF](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules)
  * Use the ["bypass" action](https://vercel.com/docs/vercel-firewall/firewall-concepts#bypass) for trusted IPs

{% hint style="info" %}
[The IP address lists are also available as JSON arrays](https://aikido.help/ips/)
{% endhint %}

***
