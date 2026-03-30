# Source: https://docs.axonius.com/docs/red-canary.md

# Red Canary

The Red Canary suite includes products that record telemetry, detect and investigate threats, and automate remediation.

### Asset Types Fetched

* Devices
* Users

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* API Key

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Red Canary Domain** *(required)* - The hostname or IP address of the Red Canary server.
2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

<Image alt="Red Canary.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Red%20Canary.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch users** - Select this option to fetch users.
2. **Fetch decommissioned devices** - Select whether to fetch decommissioned devices.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>