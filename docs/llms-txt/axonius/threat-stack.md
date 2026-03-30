# Source: https://docs.axonius.com/docs/threat-stack.md

# Threat Stack

Threat Stack is a provider of cloud security management and compliance solutions.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Threat Stack server. Default value is set to api.threatstack.com
2. **API Key** *(required)* - An API Key to be obtained from the Threat Stack platform. See [Find your Threat Stack API Key and IDs](https://clouddocs.f5.com/training/community/threat-stack/html/class2/Threat_Stack_API.html#environmental-variables) for more information.
3. **Organization ID** *(required)* - An Organization ID to be obtained from the Threat Stack platform. See [Find your Threat Stack API Key and IDs](https://clouddocs.f5.com/training/community/threat-stack/html/class2/Threat_Stack_API.html#environmental-variables) for more information.
4. **User ID** *(required)* - A User ID to be obtained from the Threat Stack platform. See [Find your Threat Stack API Key and IDs](https://clouddocs.f5.com/training/community/threat-stack/html/class2/Threat_Stack_API.html#environmental-variables) for more information.
5. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).
   * If enabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** will be verified against the CA database inside of Axonius. If the SSL certificate can not be validated against the CA database inside of Axonius, the connection will fail with an error.
   * If disabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** will not be verified against the CA database inside of Axonius.
6. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.
   * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **Host Name or IP Address**.
   * If not supplied, Axonius will connect directly to the value supplied in **Host Name or IP Address**.
7. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
8. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
9. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image align="center" alt="image\(1826\)" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1826).png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  From version 4.6 Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Fetch vulnerabilities** *(required, default: False)* - Select whether to fetch devices' vulnerabilities from Threat Stack.
   If enabled, Axonius will fetch vulnerabilities data from Threat Stack.
   If disabled, Axonius will not fetch any vulnerabilities data from Rapid7 Threat Stack.

<Callout icon="📘" theme="info">
  NOTE

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the Threat Stack API. See script examples [here](https://threatstack-python-client.readthedocs.io/en/latest/) and [here](https://github.com/threatstack/threatstack-api-scripts).

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| V2      | Yes       |       |