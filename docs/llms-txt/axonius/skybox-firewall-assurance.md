# Source: https://docs.axonius.com/docs/skybox-firewall-assurance.md

# Skybox Firewall Assurance

Skybox Firewall Assurance provides automation of firewall management tasks across different firewall vendors and complex rulesets.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Aggregated Security Findings, SaaS Applications, Network/Firewall Rules

## Parameters

1. **Skybox Domain** *(required)* - The hostname of your Skybox server.
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.
3. **Verify SSL** *(required)* - Verify the SSL certificate offered by the value supplied in **Skybox Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Skybox Domain**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Skybox Firewall Assurance.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Skybox%20Firewall%20Assurance.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch firewall rules** *(required, default: true)* - Select whether to fetch firewall rules from this adapter.
2. **Create NAT Rule Entities** - Select this option to fetch NAT rule information from Skybox.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>