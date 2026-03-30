# Source: https://docs.axonius.com/docs/digital-shadows-searchlight.md

# Digital Shadows SearchLight

Digital Shadows SearchLight is a digital risk protection solution that protects organizations against external risk exposure.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Aggregated Security Findings
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Digital Shadows SearchLight server.
2. **API Key** and **API Secret** *(required)* - An API Key associated with a user account that has permissions to fetch assets.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Digital Shadows SearchLight.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Digital%20Shadows%20SearchLight.png" />