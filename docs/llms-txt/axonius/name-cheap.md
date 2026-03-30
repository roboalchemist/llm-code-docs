# Source: https://docs.axonius.com/docs/name-cheap.md

# Namecheap

Namecheap offers free public DNS to help users get connected quickly and securely.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required, default api.namecheap.com)* - The hostname of the  NameCheap server.

2. **User Name** *(required*)- The user name for which the command is run. Should be the same as API User.

3. **API User** *(required)* - The user name needed to access the API

4. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. Refer to [NameCheap API documentation](https://www.namecheap.com/support/knowledgebase/article.aspx/9739/63/api-faq/#a) for information on how to configure the API User and Key.

5. **Client IP** *(required*) - An IP address of the server from which Axonius receives API calls (only IPv4 can be used).

6. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

7. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

8. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

9. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

10. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Namecheap](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Namecheap.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Get SSL certificates** *(required, default: false)* - Select whether to fetch SSL certificates.
2. **Get DNS servers** *(required, default: false)* - Select whether to fetch DNS servers.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [namecheap API](https://www.namecheap.com/support/api/intro/).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version      | Supported | Notes |
| ------------ | --------- | ----- |
| NameCheap v1 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.7