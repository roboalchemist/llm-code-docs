# Source: https://help.aikido.dev/code-scanning/miscellaneous/allowing-ip-addresses-for-code-container-scanning.md

# Allowing IP Addresses for Code and Container Scanning

If your Git provider only allows specific static IP addresses to access your code, you will have to whitelist Aikido's static IP addresses for code scanning before you can start scanning.

**EU-based IP addresses (default region):**

* 52.214.244.18
* 18.202.209.180
* 52.50.198.227
* 52.51.98.186

**US-based IP addresses:**

* 3.211.221.73
* 54.163.131.24
* 54.225.143.47

**ME-based IP addresses:**

* 3.29.13.194
* 40.172.18.244
* 40.172.67.79

The ports required to be opened are at least port **443** for HTTPS. For Docker container registries, additional ports might be required. For example, the Gitlab Container Registry requires port **4567** to be open.

After adding the IPs, rescan your repositories to confirm connectivity.

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
