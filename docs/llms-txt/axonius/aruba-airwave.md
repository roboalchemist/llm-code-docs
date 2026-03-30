# Source: https://docs.axonius.com/docs/aruba-airwave.md

# HPE Aruba Networking Management Software (AirWave)

HPE Aruba Networking Management Software (AirWave) is a network management system for wired and wireless infrastructure and provides granular visibility into devices, users, and applications on the network.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Aruba AirWave Domain** *(required)*  – The hostname or IP address of the HPE Aruba Networking server.

2. **User Name** and **Password** *(required)* - The user name and password for a  read only user account with **AP/Device Manager with Monitor (Read Only)** rights.

3. **Wireless SSID Exclude List** *(optional)* - Specify a comma-separated list of SSID. Devices whose SSID is in the list will not be fetched.

4. **Wireless SSID Include list** *(optional)* - Specify a comma-separated list of SSID. Only devices whose SSID is in the list will be fetched.

5. **Exclude Device With No SSID**  - Select whether to fetch devices with no SSID.

6. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

7. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

8. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

9. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

10. **Timeout when fetching extra data from AP clients** *(optional)* - Specify the number of seconds to wait when fetching extra data from AP clients.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![HPE Aruba AirWave.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HPE%20Aruba%20AirWave.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **View name** *(optional)* - Enter the view name.
2. **Use the username field to correlate Aruba devices** - Select this option to use the username field to correlate Aruba devices.
3. **Do not fetch devices without an IP address** - Select to not fetch devices without an IP address.
4. **Do not fetch devices that only have MAC addresses** - Select to not fetch any devices that only have a MAC address, but are missing the asset name and IP address.
5. **Do not fetch SSID from AP Clients** - Select this option to not fetch SSID from AP Clients.
6. **Use asynchronous requests while fetching** - Select this option to use  asynchronous requests while fetching to reduce fetch time.
7. **Fetch Network Maps for Access Points** - Select this option to fetch the network maps marking the locations of the access points.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>