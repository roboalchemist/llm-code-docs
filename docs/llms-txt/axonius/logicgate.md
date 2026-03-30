# Source: https://docs.axonius.com/docs/logicgate.md

# LogicGate

LogicGate provides a governance, risk, and compliance (GRC) platform.

### Asset Types Fetched

* Users

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Client ID/Client Secret

### APIs

Axonius uses the [LogicGate API](https://docs.logicgate.com/).

### Permissions

The value supplied in [Client ID and Client Secret](#required-parameters) must be associated with credentials that have admin privileges in order to fetch assets. For more details, see [/api/v1/users](https://docs.logicgate.com/#/User/findAllUsingGET_5).

#### Supported From Version

Supported from Axonius version 6.1

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the LogicGate server.

2. **Client ID** and **Client Secret** - The credentials for an account that has the Required Permissions to fetch assets. For information on how to obtain the client credentials, see [/api/v1/account/token](https://docs.logicgate.com/#/Authentication/getApiTokenUsingPOST) and [Risk Cloud API: Authentication](https://www.logicgate.com/developer/risk-cloud-api-authentication/).

![LogicGate](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/LogicGate.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Enrich Users with Records** - Enable this option to enrich users with records.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>