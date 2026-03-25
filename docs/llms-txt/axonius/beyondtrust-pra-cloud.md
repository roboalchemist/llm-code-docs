# Source: https://docs.axonius.com/docs/beyondtrust-pra-cloud.md

# BeyondTrust PRA Cloud

BeyondTrust PRA Cloud is a privileged remote access solution that provides secure remote access to critical systems without requiring a VPN, enhancing secure management of privileged accounts.

### Asset Types Fetched

* Devices, Users

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Client ID / Client Secret

### APIs

Axonius uses the [BeyondTrust Privileged Remote Access API](https://www.beyondtrust.com/docs/privileged-remote-access/how-to/integrations/api/open-api-configuration/methods.htm#api.config.user.index).

### Permissions

* Configuration API: Allow access

#### Supported From Version

Supported from Axonius version 6.1.40.0

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the BeyondTrust PRA Cloud server.

2. **Client ID** and **Client Secret** - The credentials for a user account that has permission to fetch assets. For information about authentication, see [Authenticate to the Privileged Remote Access API](https://www.beyondtrust.com/docs/privileged-remote-access/how-to/integrations/api/authentication.htm).

![BeyondTrustPRACloud.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BeyondTrustPRACloud.png)

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

* **Enrich Users with Jump Group Users** *(default: enabled)* - Enable this option to enrich users with the Jump Group Users endpoint.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>