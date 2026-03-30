# Source: https://docs.axonius.com/docs/aruba-mobility-master.md

# Aruba Mobility Master

Aruba Mobility Master enables deployment and management of up to 1,000 Mobility Controllers to scale large deployments. Integrate Aruba Mobility Master with the Axonius Cybersecurity Asset Management Platform.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Mobility Master IP** *(required)* - The hostname or IP address of the Aruba Mobility Master server.

2. **Port** *(required, default: 4343)* - The port used for the connection.

3. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Aruba Mobility Master](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Aruba%20Mobility%20Master.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Filter Out Access Points When Fetch Is Run**  - Select whether to exclude all Access Point devices from the fetch if a valid Access Point Type field value is present in the device.
2. **Fetch LLDP Neighbors** - Select this option to fetch LLDP neighbors as devices.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [ArubaOS JSON API](https://developer.arubanetworks.com/aruba-aos/reference/get_object-ntp-server-disable).

## Required Permissions

The value supplied in [User Name](#parameters) must have Administrator permissions to fetch assets.

## Supported From Version

Supported from Axonius version 4.5.27