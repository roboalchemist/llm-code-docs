# Source: https://docs.axonius.com/docs/riskiq-digital-footprint.md

# RiskIQ Digital Footprint

RiskIQ Digital Footprint software provides an active, comprehensive inventory of all of the organization’s IPs, domains, and hosts.

## Parameters

1. **RiskIQ Domain** *(required, default: `https://ws.riskiq.net`)* - The domain of the RiskIQ server.
2. **API Key** and **API Secret** *(required)* - The API Key and API Secret provided by RiskIQ.
3. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **RiskIQ Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
   * If enabled, the SSL certificate offered by the value supplied in **RiskIQ Domain** will be verified against the CA database inside of Axonius. If the SSL certificate can not be validated against the CA database inside of Axonius, the connection will fail with an error.
   * If disabled, the SSL certificate offered by the value supplied in **RiskIQ Domain** will not be verified against the CA database inside of Axonius.
4. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **RiskIQ Domain**.
   * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **RiskIQ Domain**.
   * If not supplied, Axonius will connect directly to the value supplied in **RiskIQ Domain**.
5. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1488\).png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Inventory state Include list** *(optional, default: empty)* - Specify a comma-separated list of RiskIQ inventory states.
   * If supplied, all connections for this adapter will only fetch devices if their inventory state in RiskIQ is provided in this list. The valid states are:
     * CANDIDATE - A candidate asset, pending user decision if this asset should be confirmed into inventory or dismissed.
     * CONFIRMED - An asset that is confirmed to belong to this inventory.
     * ARCHIVED - An asset that has been archived.
     * DISMISSED - An asset that has been dismissed and removed from this inventory.
   * If not supplied, all connections for this adapter will fetch all devices from RiskIQ.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>