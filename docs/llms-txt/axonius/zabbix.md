# Source: https://docs.axonius.com/docs/zabbix.md

# Zabbix

Zabbix is an open source monitoring software tool for networks, servers, virtual machines and cloud services.

### Use Cases the Adapter Solves

* **Unmanaged Asset Detection**: Identify devices monitored in Zabbix that are missing from your inventory or security agents.
* **Infrastructure Visibility**: Gain a comprehensive view of servers and virtual machines by correlating Zabbix monitoring data with other infrastructure sources.

### Asset Types Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Software.svg) Software | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg) SaaS Applications

***

## Before You Begin

**Ports**

* TCP port 80/443 (or 8080 depending on configuration)

**Authentication Method**

API Token or User Name and Password

### APIs

Axonius uses the [Zabbix API](https://www.zabbix.com/documentation/7.0/en/manual/api).

### Permissions

The following permissions are required:

Admin or Super Admin Roles are required, refer to [User Roles](https://www.zabbix.com/documentation/7.0/en/manual/web_interface/frontend_sections/users/user_roles).

For User Name and Password Authentication the user account needs sufficient permissions to access host data via the Zabbix API. For more details about creating users in Zabbix, see [Zabbix documentation - Users and user groups](https://www.zabbix.com/documentation/4.2/manual/config/users_and_usergroups).

### Setting Up Zabbix to Work with Axonius

Refer to [API Tokens](https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/users/api_tokens) for information about how to create an API Token.

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for **Zabbix**, and click on the adapter tile.\
Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Zabbix Domain** - The hostname/IP address, method, and port of the Zabbix API. Specify the appropriate port (80 or 8080) and method (HTTPS/HTTP) in this field.
   * **Examples**: `http://www.example.com:80`, `https://www.example.com:8080`
2. **Default Zabbix Url Path** - The path to the parent directory of 'api\_jsonrpc.php'. Unless customized, the value should be a forward slash: `/`
3. Authentication can be either **User Name and Password** or **API Token**.

<Tabs>
  <Tab title="User Name and Password">
    The credentials for a user account that has Permissions to fetch assets.
  </Tab>

  <Tab title="API Token">
    An API Token that can be used for Authenication.
  </Tab>
</Tabs>

4. **Connection Label** - A label to help you distinguish between multiple connections for the same adapter. See [Connection label](/docs/adding-a-new-adapter-connection#setting-adapter-connection-parameters).

<Image align="center" alt="Zabbix connection screen" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/zabbix.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network and not from the primary Axonius instance, which may be an Axonius-hosted (SaaS) instance or Customer-hosted (on-premises / private cloud). To use this option, you need to set up an Axonius Gateway.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

***

## Advanced Settings

<Callout icon="📘" theme="info">
  Note:

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Fetch items** - Select this option to fetch items. Items are individual metrics on the host, for instance processor load average, incoming traffic on some network interfaces, memory usage, etc. refer to [Items](https://www.zabbix.com/documentation/current/en/manual/config/items) for more information.
2. **Determine Hostname From Items** - Select this option to set hostnames from the relevant item in the item section that has a hostname. If there are none, then use the hostname from “host”.
3. **Determine Hostname From Inventory** - Select this option to set hostnames from the relevant item in the inventory section that has a hostname. If there are none, then use the hostname from “host”.
4. **Determine Hostname From DNS** - Select this option to set the hostname from the Zabbix DNS field.
5. **Custom Select items to fetch (comma separated)** - Enter a comma-separated list of additional items to fetch.
6. **Fetch problems** - Select this option to enrich devices with corresponding problems.