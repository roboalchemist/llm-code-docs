# Source: https://docs.axonius.com/docs/cynerio.md

# Cynerio

Cynerio is a healthcare IoT security platform that identifies, monitors, and secures connected medical devices.

### Asset Types Fetched

* Devices, Vulnerabilities, SaaS Applications

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Client ID/Authentication Secret

### APIs

Axonius uses the [Cynerio API](https://us.app.cynerio.com/outbound-integrations/docs#/).

### Permissions

Consult with your vendor for permissions for reading the objects.

### Supported From Version

Supported from Axonius version 6.1

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Availability Zone** *(default: US)* - From the dropdown, select in which availability zone your Cynerio account is located (US or EU).

2. **Client ID** - Credentials associated with a user account that has permissions to fetch assets.

3. **Authentication Secret** -  The authentication secret received from Cynerio.

<Image alt="Cynerio" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Cynerio.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Risks/Vulnerabilities from the last X days** *(optional, default: 30)* - Fetch risks/vulnerabilities from the specified number of days.
2. **Fetch Non-NDR events from the last X days** *(optional, default: 7)* - Fetch non-NDR events from the specified number of days.
3. **Fetch NDR Events from the last X days** *(optional, default: 7)* - Fetch NDR events from the specified number of days.
4. **Fetch Incidents created in the last X days** *(optional, default: 7)* - Fetch incidents created in the specified number of days.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>