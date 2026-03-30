# Source: https://docs.axonius.com/docs/velociraptor.md

# Velociraptor

Velociraptor is an open-source endpoint monitoring, digital forensic and cyber response platform.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Velociraptor server.

2. **Port** *(required, default: 8001)* - The port used for the connection.

3. **Config File** *(required)* -Upload a Configuration File containing the CA certificate, the client private key and the client cert. Refer to [The Velociraptor API](https://docs.velociraptor.app/docs/server_automation/server_api/) for details.

4. **Organization ID** *(optional)* - The Organization ID.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Velociraptor](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Velociraptor.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Ignore non-correlating assets** - Select this option to ignore devices that do not have data which can help  to correlate them.
2. **Use FQDN for hostname** - Select this option to use FQDN as the hostname.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Velociraptor API](https://docs.velociraptor.app/docs/server_automation/server_api/).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80**
* **TCP port 443**

## Required Permissions

The value supplied in \[API Key] must be associated with credentials that have ReadOnly permissions in order to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version            | Supported | Notes |
| ------------------ | --------- | ----- |
| Velociraptor 1.0.0 | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.7