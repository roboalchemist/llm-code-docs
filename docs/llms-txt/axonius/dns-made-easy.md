# Source: https://docs.axonius.com/docs/dns-made-easy.md

# DNS Made Easy

DNS Made Easy offers DNS management services.

**Related Enforcement Actions**:
[DNS Made Easy - Remove Subdomain](/docs/remove-subdomain-from-dns-made-easy)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required, default: api.dnsmadeeasy.com)* - The hostname or IP address of the DNS Made Easy server.
2. **API Key** and **Secret Key** *(required)* - An API Key and Secret Key pair associated with a user account that has permissions to fetch assets.
3. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-amp-ca-settings).
   * If enabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** will be verified against the CA database inside of Axonius. If the SSL certificate can not be validated against the CA database inside of Axonius, the connection will fail with an error.
   * If disabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** will not be verified against the CA database inside of Axonius.
4. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.
   * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **Host Name or IP Address**.
   * If not supplied, Axonius will connect directly to the value supplied in **Host Name or IP Address**.
5. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
6. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
7. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1292\).png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Fetch all record types** *(required, default: False)* - Select whethet to fetch only 'A' records or all the record types from DNS Made Easy.
   * If enabled, all connections for this adapter will fetch all available record types from DNS Made Easy. The available record types are:
     * A
     * AAAA
     * ANAME
     * CAA
     * CNAME
     * HTTP Redirection
     * MX
     * NS
     * PTR
     * SPF
     * SRV
     * System NS
     * TXT
   * If disabled, all connections for this adapter will fetch all 'A' records from DNS Made Easy.

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1308\).png)

<Callout icon="📘" theme="info">
  NOTE

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [DNS Made Easy API](https://api-docs.dnsmadeeasy.com/?version=latest).

## Required Permissions

The value supplied in [**API Key** and **Secret Key**](#parameters) must have read access to devices.

To generate an API Key and Secret Key pair:

1. Navigate there through the  **Config** dropdown menu item in the top navigation bar.
   ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1293\).png)

2. You will find your **API Key** and **Secret Key** at the bottom of your Account Information page.
   ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1294\).png)

3. If you have not generated an API Key and Secret Key pair yet, then this area will be blank.

   In that case you will need to **Generate New API Credentials**, to do that  check the provided checkbox and click Save. The page will refresh and you will be provided with the credentials you need.
   ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1295\).png)

<Callout icon="📘" theme="info">
  Note

  The DNS Made Easy Enforcement Action requires additional permissions, Refer to [DNS Made Easy - Remove Subdomain](/docs/remove-subdomain-from-dns-made-easy).
</Callout>