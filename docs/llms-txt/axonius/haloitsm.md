# Source: https://docs.axonius.com/docs/haloitsm.md

# HaloITSM

HaloITSM is a cloud-based IT service management solution designed for ITIL-aligned service delivery.

<br />

### Asset Types Fetched

* Devices, Users

<br />

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Client ID/Client Secret

### APIs

Axonius uses the [Halo REST API](https://halo.haloservicedesk.com/apidoc/info).

### Permissions

Consult with your vendor for the exact permissions to fetch the objects.

#### Supported From Version

Supported from Axonius version 6.0

<br />

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the HaloITSM server.

2. **Client ID** and **Client Secret** - The credentials for a user account that has permissions to fetch assets.

<br />

<Image alt="HaloITSM" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HaloITSM.png" />

<br />

### Optional Parameters

1. **Tenant**  - Used with hosted solutions of Halo to specify the tenant in the URL.

2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

3. **HTTPS Proxy**  - Connect the adapter to a proxy instead of directly connecting it to the domain.

4. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Devices from Assets** - Toggle on to fetch devices.
2. **Fetch Users from Users** - Toggle on to fetch users.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />

### Related Enforcement Actions

* [Halo - Create or Update Device](/docs/halo-create-update-device)

* [Halo - Create or Update User](/docs/halo-create-update-user)