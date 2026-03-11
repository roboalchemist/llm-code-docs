# Source: https://docs.axonius.com/docs/patch-manager.md

# PATCH MANAGER

PATCH MANAGER is a network infrastructure management tool that provides graphical planning, documentation, and control of physical connectivity and asset information.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the PATCH MANAGER REST API.

### Permissions

The following permissions are required to fetch assets:

* **Action-Specific Permissions**: For any specific action (like creating or deleting equipment), the user also needs the corresponding permissions for that task (e.g., "Modify Infrastructure") assigned to their account.

#### Supported From Version

Supported from Axonius version 7.0.11

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the PATCH MANAGER server.
2. **User Name** and **Password**  - The credentials for a user account that has the Required Permissions to fetch assets.

<Image alt="PatchManager.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PatchManager.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Equipment Export Format** *(optional, default: equipment\_export\_axonius)* - Enter the equipment export format
2. **Enrich Equipment Endpoint with Port Endpoint** - Enable this option to enrich the Equipment endpoint with the Port endpoint. When enabled, the following setting may be configured.
   * **Port Export Format** *(optional, default: port\_export)* - Enter the port export format.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>