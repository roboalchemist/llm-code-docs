# Source: https://docs.axonius.com/docs/truefort.md

# TrueFort

TrueFort offers application behavior analytics, control, and protection.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Truefort Domain** *(required)* - The hostname or IP address of the Truefort server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

<Image alt="TrueFort" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TrueFort.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch asset profiles** - Select this option to fetch asset profiles for each application.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Permissions

The value supplied in **User Name** must have the same permissions as the Axonius user.