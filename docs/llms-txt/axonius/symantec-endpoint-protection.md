# Source: https://docs.axonius.com/docs/symantec-endpoint-protection.md

# Symantec Endpoint Protection 14.x

Symantec Endpoint Protection 14.x manages events, policies, and registration for the client computers that connect to customer networks.

<Callout icon="📘" theme="info">
  Note
  This page describes how to connect Symantec Endpoint Protection 14.x deployments. To connect Symantec Endpoint Protection 12.x, see [Symantec Endpoint Protection 12.x](/docs/symantec-endpoint-protection-12x).
</Callout>

### Asset Types Fetched

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg" /> Devices

## Before You Begin

**Ports**

* TCP port 8446 (default)

**Authentication Method**

### APIs

Axonius uses the Symantec Endpoint Protection Remote Management (SEMP) API.

### Permissions

The following permissions are required:

* A user account with permissions to fetch assets from the Symantec Endpoint Protection Manager (SEPM).
* If using the SEMP Database connection: Read access to the SEMP database, specifically the `agent_def_cache` table.

<br />

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for Symantec Endpoint Protection 14.x, and click on the adapter tile.\
Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Symantec Endpoint Protection Address** - The hostname or IP address of the Symantec Endpoint Protection 14.x server.
2. **User Name** and **Password** - The credentials for a user account that has the Required Permissions to fetch assets.
3. **Connection Label** - A label to help you distinguish between multiple connections for the same adapter. See [Connection label](/docs/adding-a-new-adapter-connection#setting-adapter-connection-parameters) .

<Image align="center" alt="Symantec Endpoint Protection 14.x connection screen" border={false} width={500} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/SymantecEndPointPRotection.png" />

### Optional Parameters

1. **Port** *(default: 8446)* - The port used for the connection.
2. **User Name Domain** *(default: Default)* - Specify the Symantec Endpoint Protection domain, if defined. A domain is a structural container in the console that you use to organize a hierarchy of groups, clients, computers, and policies.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
5. **Use SEMP Database In Connection** - Toggle on to connect the SEMP database and fetch data from it using the **Fetch Device Definitions** advanced setting. When you enable this setting, provide the following credentials to connect the SEMP database:
   * **Database** - The SEMP database name.
   * **Database Address** - The SEMP database server address.
   * **Database Port** - The SEMP database port.
   * **Database Username** and **Database Password** - The SEMP username and password.
6. **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network and not from the primary Axonius instance, which may be an Axonius-hosted (SaaS) instance or Customer-hosted (on-premises / private cloud). To use this option, you need to set up an Axonius Gateway.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note:

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Fetch Device Definitions (requires database credentials)** - Select this option to query device definitions from the `agent_def_cache` table in the SEMP database. To use this setting you need to enable [**Use SEMP Database In Connection**](/docs/symantec-endpoint-protection#parameters) in the adapter connection configuration.