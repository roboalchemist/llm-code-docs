# Source: https://docs.axonius.com/docs/sectigo.md

# Sectigo

Sectigo provides digital certificate lifecycle and PKI management.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Certificates

## Parameters

1. **Host Name or IP Address** *(required, default for cloud instances: [https://cert-manager.com](https://cert-manager.com))* - The hostname or IP address of the Sectigo server.

2. **Username** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Customer URI** *(required)* - Specify the identifier of the resource to use, this must be entered in lower case.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Sectigo](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Sectigo.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Async Chunks** *(required, default: 50)* - Specify the number of parallel requests all connections for this adapter will send to the Sectigo server in parallel at any given point.
2. **Fetch Administrator users** - Select this option to fetch Administrator users in addition to regular users.
3. **Fetch Users** *(required, default: true)* - By default Axonius fetches users. Clear this option to not fetch users.
4. **Fetch device certificates** - Select this option to fetch device certificates.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Sectigo API](https://sectigo.com/knowledge-base/detail/Sectigo-Certificate-Manager-SCM-REST-API/kA01N000000XDkE).

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| V1      | Yes       |       |

## Supported From Version

Supported from Axonius version 4.5