# Source: https://docs.axonius.com/docs/soti-mobicontrol.md

# SOTI MobiControl

SOTI MobiControl is a software system for managing mobile devices in the enterprise.

### Asset Types Fetched

* Devices, Users, Software, SaaS Applications

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password
* Client ID/Client Secret

### APIs

Axonius uses the [MobiControl REST API](https://s095155.mobicontrolcloud.com/mobicontrol/api/docs/index/index.html?url=/mobicontrol/api/swagger/v2/swagger.json).

### Permissions

Consult with your vendor for permissions for reading the objects.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **MobiControl Domain** - The hostname / domain of the SOTI MobiControl server.
2. **User Name** and **Password** - Enter the credentials of a MobiControl administrator.
3. **Client ID** and **Client Secret** - Enter the Client ID and Client Secret to be used to authenticate the request. For details on finding the Client ID and Client Secret, see [SOTI MobiControl Help - Finding Your Client ID and Client Secret](https://www.soti.net/mc/help/v14.3/en/console/data/sotisurf/surf_find_clientID.html).

![SOTI.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SOTI.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch Installed Software** - Select whether to fetch installed software for devices.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>