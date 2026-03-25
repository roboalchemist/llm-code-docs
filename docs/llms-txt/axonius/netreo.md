# Source: https://docs.axonius.com/docs/netreo.md

# Netreo

Netreo is an IT infrastructure monitoring platform.

### Asset Types Fetched

* Devices, Alerts/Incidents

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key

### APIs

Axonius uses the following APIs:

* [Device Performance API](https://solutions.netreo.com/docs/device-performance-api)
* [Incidents API](https://solutions.netreo.com/docs/incidents-api)
* [Device Management API](https://solutions.netreo.com/docs/device-management-api)

### Permissions

Consult with your vendor for the exact permissions to fetch the objects.

#### Supported From Version

Supported from Axonius version 6.1

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Netreo server.

2. **API Key** - An API Key associated with a user account that has permissions to fetch assets. For information on how to find the API Key, see [Find Your API Key](https://solutions.netreo.com/docs/how-to-enable-netreo-api-access#find-your-api-key).

3. **API Pin** - The value required to access the Netreo API if using the SaaS version; if using the on-premise version, it is not required. For information on how to find the API Pin, see [Find Your Netreo SaaS API Pin](https://solutions.netreo.com/docs/how-to-enable-netreo-api-access#find-your-netreo-saas-api-pin).

![Netreo](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Netreo.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Devices from Devices** *(default: true)* - Enable this option to fetch devices from the Devices endpoint. When this setting is enabled, the following settings may be configured:
   * **Enrich Devices with Device Details** *(default: true)*
   * **Enrich Devices with Device Statistic Categories** *(default: true)*
   * **Enrich Device Statistic Categories with Device Statistic Instance**
     * **Enrich Device Statistic Instance with Performance Endpoint**
2. **Fetch Incidents from List Incidents** *(default: true)* - Enable this option to fetch incidents from the List Incidents endpoint. When this setting is enabled, the following setting may be configured:
   * **Enrich List Incidents with Incident Details**

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>