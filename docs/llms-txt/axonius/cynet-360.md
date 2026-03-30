# Source: https://docs.axonius.com/docs/cynet-360.md

# Cynet 360

Cynet 360 is a detection and response security platform for finding, ranking, and remediating unknown, camouflaged threats.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Cynet Domain** *(required)* - The hostname or IP address of the Cynet server that Axonius can communicate with via the [Required Ports](#required-ports).
2. **Site ID** *(optional)* - Enter the Client ID supplied by Cynet 360 Support.

<Callout icon="📘" theme="info">
  Note

  **Site ID** is required when using the Cloud version of Cynet 360.
</Callout>

3. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

4. **Is Cloud** *(optional, default: true)* - Select if you use the Cloud version of Cynet 360.

5. **Verify SSL** - Select to verify the SSL certificate offered by the value supplied in **Cynet Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Cynet Domain**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Cynet360.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Cynet360.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch Devices Last Seen in X Days** *(required, default: 90)* - Fetch devices last seen by the number specified.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**