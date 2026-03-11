# Source: https://docs.axonius.com/docs/real-vnc-gateway-service.md

# RealVNC

RealVNC is a remote access software that provides secure connectivity and control over devices.

### Asset Types Fetched

* Users
* Groups

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* Access Key/Access Secret

### APIs

Axonius uses the following APIs:

* [List team members](https://docs.realvnc.com/api-access.html?lai_vid=WKjAdp2EWHKN1\&lai_sr=40-44\&lai_sl=m\&lai_p=1#tag/Members)

* [List user groups](https://docs.realvnc.com/api-access.html?lai_vid=WKjAdp2EWHKN1\&lai_sr=40-44\&lai_sl=m\&lai_p=1#tag/User-groups)

* [List team events](https://docs.realvnc.com/api-access.html?lai_vid=WKjAdp2EWHKN1\&lai_sr=40-44\&lai_sl=m\&lai_p=1#tag/Audit)

  **Note**: Yield the audit events as Activities for SM customers as well.

### Permissions

The following permissions are required:

* **List team members**: This endpoint requires a session token with the LIST\_TEAM\_MEMBERS permission.

* **List user groups**: This endpoint requires a session token with the LIST\_USER\_GROUPS permission.

* **List team events**: This endpoint requires a session token with the LIST\_AUDIT\_EVENTS permission.

#### Supported From Version

Supported from Axonius version 6.1.70

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the RealVNC server (This should be: `https://connect-api.services.vnc.com`).
2. **Access Key** and **Access Secret**  - The credentials for a user account that has the Required Permissions to fetch assets.

<Image alt="RealVNC.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RealVNC.png" />

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

* **X number of days before today** *(default: 7)* - Use this option to search for team events that happened in the last X number of days.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>