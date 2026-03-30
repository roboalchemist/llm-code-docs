# Source: https://docs.axonius.com/docs/viptela-sd-wan.md

# Viptela (Cisco) SD-WAN

Cisco SD-WAN (previously Viptela) allows users to establish an SD-WAN overlay fabric that connects data centers, branches, campuses, and colocation facilities.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Viptela SD-WAN server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **API Rate Limit per Minute** *(default 6000)* - Enter an API rate limit per minute.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![ViptelaSDWAN](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ViptelaSDWAN.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  From Version 4.6, Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch ARP data as device** *(optional)* - Select whether to fetch ARP data as a device.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Cisco SD-WAN vManage API](https://developer.cisco.com/docs/sdwan/#!introduction/cisco-sd-wan-vmanage-api).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80**
* **TCP port 443**

## Supported From Version

Supported from Axonius version 4.7