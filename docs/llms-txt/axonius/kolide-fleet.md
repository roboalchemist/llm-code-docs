# Source: https://docs.axonius.com/docs/kolide-fleet.md

# FleetDM

FleetDM (formerly Kolide Fleet) is an is an open-source query manager for device management.

### Asset Types Fetched

* Devices, Vulnerabilities, Software, SaaS Applications

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password for Cloud
* API Token for on-prem

### APIs

Axonius uses the [Fleet REST API](https://fleetdm.com/docs/using-fleet/rest-api).

### Permissions

Consult with your vendor for permissions for reading the objects.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the FleetDM server.
2. **User Name** and **Password** - The credentials for a user account that has the permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  If **API Token** is not supplied, **User Name** and **Password** are required.
</Callout>

3. **API Token** - An API Key associated with a role that has permissions to fetch assets. Only API Token is supported in v4 of FleetDM and higher.

<Callout icon="📘" theme="info">
  Note

  If **User Name** and **Password** are not supplied, **API Token** is required.
</Callout>

<Image alt="FleetDM" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FleetDM.png" />

### Optional Parameters

1. **Custom API Path** - Fill in the field to use a different custom API path. You can use this field as a prefix for the API (generally not required, only for advanced deployments).

2. **Verify SSL** - Select whether to verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

3. **HTTPS Proxy** - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.

4. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password** - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch software** *(default: true)* - Select whether to fetch software information.
2. **Fetch vulnerabilities** - Select whether to fetch vulnerabilities.
3. **Legacy Mode** - Select this option to enable legacy mode and fetch all hosts and host details.
4. **Async Chunks in parallel** *(optional, default: 100)* - Set the number of asynchronous chunks that will run in parallel. You can set any integer number between 1 and 100.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>