# Source: https://developers.make.com/custom-apps-documentation/other/https-custom-ca.md

# HTTPS self-signed or with custom CA

**This guide is relevant only for special cases where it is reasonably expected that the application may need to communicate with third-party servers using HTTPS connections that rely on either a self-signed certificate or a custom certificate authority (CA) instead of a widely trusted public CA.**

**If your custom app only interacts with services that use publicly trusted certificates, you can safely ignore this guide.**

***

{% hint style="warning" %}
**BREAKING CHANGE** – Coming 30.4.2026

We would like to inform you in advance about an upcoming change that will strengthen our HTTPS validation policy.

Beginning on 30.4.2026, Make will begin **blocking untrusted HTTPS connections by default**.

If your servers are using self-signed or otherwise untrusted certificates, please carefully review the guide below and update your custom app accordingly.

While this change may affect a small number of edge-case usages, we are confident that it brings a clear security benefit to all customers.
{% endhint %}

***

## Solution

Your custom app can be extended to accept a custom certificate (trusted CA or self-signed). A certificate issued by a globally trusted CA is preferred.

There are two options to choose from:

* [Define the certificate statically](#define-certificate-statically)
* [Ask the user for the certificate dynamically](#ask-user-for-certificate-dynamically)

### Define certificate statically

Add the trusted custom CA certificate (or self-signed certificate) to both the `base` and `connection` JSON configurations of the custom app.

You need to add the certificate in both places, because connections do not inherit configuration from the base code.

{% tabs %}
{% tab title="Custom app" %}

```jsonc
// custom app's base
{
    // Your default base config like `baseUrl`, `headers`, `response`, `log`, ...
    "baseUrl": "https://some-my-private-service.example.com/api",

    // Add the property `ca` with public cert of your own CA or of your self-signed cert.
    "ca": "-----BEGIN CERTIFICATE-----\nMIIDeTCCAmGgAwIBAgIJAOSe0iZEklcXMA0GCSqGSIb3DQEBCwUAMGIxCzAJBgNV\nBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRYwFAYDVQQHDA1TYW4gRnJhbmNp\n... (certificate truncated in example) ...\ny4qocoQVErLCN+R1VscdmTgNgIypce6+Dirco8Skh5/V7KgLXHUZ7BPyaxJpzxxM\nvJEZ/1G0g7NopNIOKcCBBneqjir85QUYQ9DZDNY=\n-----END CERTIFICATE-----"
}
```

{% hint style="info" %}
The example above shows the principle of how to configure it. But defining the CA cert statically is useful in limited cases, where the certificate is fixed and known in advance.
{% endhint %}
{% endtab %}

{% tab title="Connection" %}

```jsonc
// connection's communication
{
    "ca": "-----BEGIN CERTIFICATE-----\nMIIDeTCCAmGgAwI ...", // certificate truncated in example

    // ... and other config like `url`, `headers`, `response`.
}
```

{% hint style="info" %}
The example above shows the principle of how to configure it. But defining the CA cert statically is useful in limited cases, where the certificate is fixed and known in advance.
{% endhint %}
{% endtab %}
{% endtabs %}

### Ask user for certificate dynamically

Let the customer enter the certificate themselves during the connection creation. This is useful if you need to give your custom app the flexibility to connect to any instance on the internet (for example, by having the customer enter their own URL).

For the implementation, add a new `mappable parameter` with `type: "cert"` into the Connection and then reference it in both the base and the connection's communication.

{% tabs %}
{% tab title="Connection" %}

```jsonc
// connections's mappable parameters
[
    // Ask user for extra CA of HTTPS connection
    {
        "name": "ca",
        "label": "Trusted Custom CA / Self-Signed Certificate",
        "help": "Upload a certificate if an HTTPS server uses custom Certificate Authority (CA) or a self-signed certificate. This allows to trust connections to that server.",
        "type": "cert",
        "advanced": true, // display only after click to "Show advanced settings"
        "editable": true, // allow to enable/disable in connection edit

    },
]
```

{% endtab %}

{% tab title="Connection" %}

```jsonc
// connection's communication
{
    // use the user uploaded certificate in the Connection
    "ca": "{{connection.ca}}",

    // ... other config like `url`, `headers`, `response`.
}
```

{% endtab %}

{% tab title="Custom app" %}

```jsonc
// custom app's base
{
    // use the user uploaded certificate in the rest of custom app
    "ca": "{{connection.ca}}",

    // ... and other config like `baseUrl`, `headers`, `response`.
}
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
**Tip: Download the CA certificate from the existing HTTPS service**

The following Linux / macOS command can help you retrieve the required CA certificate (or self-signed certificate) from an existing HTTPS service.

In the first line of the command below, replace `YOUR_DOMAIN.com` with your actual domain, then copy the certificate string, including the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` sections.

{% tabs %}
{% tab title="Source" %}

```bash
# Replace YOUR_DOMAIN.com below with your actual domain
openssl s_client -showcerts -connect YOUR_DOMAIN.com:443 </dev/null 2>/dev/null | \
awk '/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/' | \
awk 'BEGIN{n=0} 
     /BEGIN CERTIFICATE/{n++; out[n]=$0; next} 
     /END CERTIFICATE/{out[n]=out[n] ORS $0; next} 
     {out[n]=out[n] ORS $0} 
     END{print out[n]}'
```

{% endtab %}
{% endtabs %}
{% endhint %}

## Common certificate issues

* **Self-signed certificate**\
  Often used in internal or test environments. These certificates are created and signed by the server itself, not by a Certificate Authority (CA).
* **Custom Certificate Authority (CA)**\
  Common in company-internal tools and services. Organizations may run their own CA and issue certificates for internal domains. These CAs are not globally trusted, so the trust must be added manually.
* **Expired certificate**\
  [A certificate that has passed its validity period](#https-with-invalid-or-expired-certificate) will be treated as invalid. Even if it was originally issued by a trusted CA, it is no longer accepted unless renewed.
* **Other certificate problem examples**
  * **Invalid CN/SAN**: The domain name does not match the one in the certificate.
  * **Incomplete chain**: Missing intermediate certificates required for full trust.
  * **Unknown or weak signature algorithms**: Outdated encryption methods (e.g. MD5).

***

## Behavior quick reference guide

### Behavior until 30.4.2026

By default, Make **allows** connections to HTTPS services even when the certificate is invalid or untrusted. In such cases, the platform **generates a warning** for each affected scenario module.

<table><thead><tr><th valign="top">Certificate Issue</th><th valign="top">Default Behavior</th></tr></thead><tbody><tr><td valign="top">✅ Public HTTPS certificate</td><td valign="top">✅ Connection allowed</td></tr><tr><td valign="top">❗ Self-signed certificate</td><td valign="top">🔔 Connection allowed, produces warning</td></tr><tr><td valign="top">❗ Custom CA certificate</td><td valign="top">🔔 Connection allowed, produces warning</td></tr><tr><td valign="top">❗ Expired certificate</td><td valign="top">🔔 Connection allowed, produces warning</td></tr><tr><td valign="top">❗ Invalid or weak certificate</td><td valign="top">🔔 Connection allowed, produces warning</td></tr></tbody></table>

### Behavior from 30.4.2026 (breaking change)

Starting from this date, Make will **block** HTTPS connections by default if the certificate is untrusted or invalid. To maintain functionality, follow the recommended steps in your custom app:

<table><thead><tr><th valign="top">Certificate Issue</th><th valign="top">Default Behavior</th><th valign="top">Recommended Custom App improvement</th><th valign="top">Behavior After the Custom app improvement</th></tr></thead><tbody><tr><td valign="top">✅ Public HTTPS certificate</td><td valign="top">✅ Connection allowed</td><td valign="top">✅ No action needed</td><td valign="top">✅ Connection allowed</td></tr><tr><td valign="top">❗ Self-signed certificate</td><td valign="top">❌ Connection blocked</td><td valign="top">🔧 <a href="#solution">Upload the self-signed certificate</a></td><td valign="top">✅ Connection allowed</td></tr><tr><td valign="top">❗ Custom CA certificate</td><td valign="top">❌ Connection blocked</td><td valign="top">🔧 <a href="#solution">Upload the custom CA certificate</a></td><td valign="top">✅ Connection allowed</td></tr><tr><td valign="top">❗ Expired certificate</td><td valign="top">❌ Connection blocked</td><td valign="top">❌ No fix in Custom App is possible</td><td valign="top">❌ Connection blocked</td></tr><tr><td valign="top">❗ Invalid or weak certificate</td><td valign="top">❌ Connection blocked</td><td valign="top">❌ No fix in Custom App is possible</td><td valign="top">❌ Connection blocked</td></tr></tbody></table>

***

## HTTPS with invalid or expired certificate

Due to security implications, it is not possible to configure the custom app to connect to an HTTPS service if the certificate is **invalid** or **expired**.

The only secure solution in this case is to **replace the invalid or expired certificate** on the server. This process lies outside of Make's control and must be coordinated directly with the third-party technical support team responsible for the affected server.

## `rejectUnauthorized` directive deprecation notice

The directive `rejectUnauthorized: false` usable in custom apps for allowing connections to untrusted HTTPS servers with security issues is being deprecated and will be removed in the future.
