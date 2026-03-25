# Source: https://docs.axonius.com/docs/dell-emc-avamar.md

# Dell EMC Avamar

Dell EMC Avamar is a backup and recovery solution that enables daily backups of physical and virtual environments, NAS servers, enterprise applications, remote offices and desktops/laptops.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Avamar Domain** *(required)* - The hostname or IP address of the Dell EMC Avamar server that  Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the the permissions to fetch assets.

3. **Client ID** and **Client Secret** *(optional)* - The Client ID and the Client Secret that have the permissions to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Dell EMC Avamar.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Dell%20EMC%20Avamar.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch clients groups** - Select this option to fetch clients groups.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Ports

Axonius must be able to communicate with the value supplied in [Avamar Domain](#parameters) via the following ports:

* TCP port 443