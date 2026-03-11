# Source: https://docs.axonius.com/docs/dnsfilter.md

# DNSFilter

DNSFilter is a cloud-based web content filtering solution that protects users from accessing malicious or inappropriate websites.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

### Required Parameters

1. **Authentication Method** - Select between Basic Authentication and API Key Authentication.

**When using Basic Authentication, provide the following parameters:**

1. **User Name** and **Password** - The credentials for a user account that has permission to fetch assets. For information on authentication, see [Obtaining a Token](https://app.swaggerhub.com/apis/DNSFilter/dns-filter_api/1.0.3#/info).
2. **2FA Secret Key** *(optional)* - Enter a secret key to use Multi-Factor Authentication.

**When using API Key Authentication, provide an API Key.**

![dnsfilter](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-4W7BMQTI.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## APIs

Axonius uses the [DNSFilter API](https://app.swaggerhub.com/apis/DNSFilter/dns-filter_api/1.0.3).

## Supported From Version

Supported from Axonius version 6.1