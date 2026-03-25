# Source: https://docs.axonius.com/docs/guardicore.md

# Guardicore

Guardicore is a data center and cloud security company that protects the organization’s core assets.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Guardicore Domain** - The hostname of the Guardicore server.
2. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![guardicore.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/guardicore.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Avoid Cloud duplications** - Select this option to skip cloud duplications.
2. **Fetch agents status flags** - Select this option to fetch agent status flags.
3. **Fetch agents information** - Select this option to fetch full agent information for a device.
4. **Fetch incidents from X days ago** - By default Axonius fetches incidents from up to 100 days back.
5. **Fetch incidents to X days ago** - Select this option to fetch incidents up to 100 days ahead.
6. **Module Status Enforcement** - From the drop-down, select the `module_status_enforcement` filter to use for the agent fetch. Possible values: No Filter, Active, Not Deployed, Enforcement.
7. **Fetch Agents as Devices** - Select this option to create devices on agents.
8. **Fetch Users** - By default Axonius fetches users. Clear this option to not fetch users.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>