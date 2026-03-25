# Source: https://docs.axonius.com/docs/rumble-network-discovery.md

# runZero

runZero (formerly Rumble Network Discovery) is a cloud-based network discovery platform that identifies and monitors network-connected IT assets.

## Asset Types Fetched

This adapter fetches the following types of assets:

* Devices, Aggregated Security Findings, SaaS Applications, Domains & URLs, Certificates

## Parameters

1. **Rumble Network Discovery Domain** *(required, default: `https://console.rumble.run`)* - The hostname of the runZero server. Use the default value.

2. **API Key** *(required)* - An API Key associated with the  organization assets to be fetched. For details, see [Generate API Key](#generate-api-key).

3. **Download Token** *(optional)* - An optional download token.
   * If supplied, Axonius will deploy the runZero agent on the host it is running on.
   * If not supplied, Axonius will only fetch data from the source and will not deploy the runZero agent on the host it is running on.

4. **Verify SSL** - Select to verify the SSL certificate offered by the host supplied in **runZero Domain**. For more details, see [SSL Trust & CA Settings](/docs/global-settings#ssl-trust-amp-ca-settings).

5. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to **runZero Domain**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="runzeroconnection" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-3AUXV4GT.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Do not fetch devices with no MAC address and no hostname** - Select whether to not fetch devices with no MAC address and no hostname.

2. **Do not fetch devices that are not Alive** -  Select to not fetch devices that aren't alive.

3. **Add arp MAC to aggregated MACs** - Select whether to add the ARP MAC from services to the aggregated MACs.

4. **Skip raw data** *(default: false)* - Select this option to not save the raw data, by default this is set to false and raw data is saved.

5. **Fetch Vulnerabilities / Certificates / URLs** - Select to fetch any of these asset types (Vulnerabilities are fetched as Aggregated Security Findings).

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Generate API Key

1. Open [runZero Console](https://console.rumble.run/organizations/organizations_api).
2. Click the organization for the API token you want.
3. Generate a new **Export Token** and paste this value in the [API Key](#parameters) parameter.