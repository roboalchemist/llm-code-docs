# Source: https://docs.axonius.com/docs/eclypsium.md

# Eclypsium

Eclypsium protects the foundation of the computing infrastructure, controlling risks and stopping threats to enterprise firmware and hardware devices.

## Asset Types Fetched

* Devices, Aggregated Security Findings, SaaS Applications

## Adapter Parameters

1. **Eclypsium Domain** *(required)* - The hostname of the Eclypsium server.

2. **Client ID** and **Client Secret** *(required)* - The Client ID and Client Secret for an account that has read access to the API.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Eclypsium" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Eclypsium.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Enrich devices with full hosts data**  - Select this option to fetch extra data for each device  from the endpoint "api/v1/fullhosts/`{device_id}`"

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>