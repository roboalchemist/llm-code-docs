# Source: https://docs.axonius.com/docs/uyuni.md

# Uyuni

Uyuni is an open-source configuration and infrastructure management solution for software-defined infrastructure.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Software
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Uyuni server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Uyuni" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-Q3QS7T89.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Additional system methods** - Enter names of system methods to enrich device information with.

2. **Fetch Patches** - Enable this option to fetch patches according to their status.
   1. **Patches Types to Fetch** - Select the patch statuses you want to fetch:
      * AFFECTED\_PATCH\_INAPPLICABLE - affected, patch available in unassigned channel
      * AFFECTED\_PATCH\_APPLICABLE - affected, patch available in assigned channel
      * NOT\_AFFECTED - not affected
      * PATCHED - patched

3. **Fetch Suggested Reboots** - Enable this to enrich devices with additional information about suggested reboots. The information will appear under the Suggested Reboots fields.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Uyuni API Version 26](https://www.uyuni-project.org/uyuni-docs-api/uyuni/index.html)

## Supported From Version

Supported from Axonius version 4.8