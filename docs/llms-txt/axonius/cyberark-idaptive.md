# Source: https://docs.axonius.com/docs/cyberark-idaptive.md

# CyberArk Idaptive

Idaptive Identity Management Platform is an identity and access management solution that unifies identity and access management services.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the CyberArk Idaptive server.

2. **App ID** *(required)* -  Your CyberArk App ID

3. **Client ID** and **Client Secret** *(required)* -  The Client ID and Client Secret for an account that has read access to the API. Provided by CyberArk Refer to [Cyber Ark Documentation](https://docs.cyberark.com/identity/latest/en/content/developer/use-queries.htm) for details of how to get these parameters

4. **Password** *(optional)* -  A password used for Advanced Authentication.

5. **Verify SSL** - Select this option to verify the SSL certificate of the server against the CA database inside of Axonius. To learn more, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![CyberArkIdaptive](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CyberArkIdaptive.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch user roles** - Select this option to fetch user roles.
2. **Fetch user groups** - Select this option to fetch user groups.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [CyberArk Identity API](https://docs.cyberark.com/identity/latest/en/content/developer/use-queries.htm).

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| 2.0     | Yes       | --    |
|         |           |       |

## Supported From Version

Supported from Axonius version 4.8