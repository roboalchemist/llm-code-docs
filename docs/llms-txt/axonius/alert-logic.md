# Source: https://docs.axonius.com/docs/alert-logic.md

# Alert Logic

Alert Logic provides vulnerability and asset visibility, endpoint protection, threat detection, incident management, and a web application firewall.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Alert Logic Domain** *(required, default: publicapi.alertlogic.net)* - The Alert Logic server.
2. **API Key** *(required)* - Use the API key provided by Alert Logic support. Refer to [ Alert Logic Access Key Management](https://docs.alertlogic.com/prepare/access-key-management.htm) for information about getting your Alert Logic Key.
3. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Alert Logic Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-amp-ca-settings).
   * If enabled, the SSL certificate offered by the value supplied in **Alert Logic Domain** will be verified against the CA database inside of Axonius. If the SSL certificate can not be validated against the CA database inside of Axonius, the connection will fail with an error.
   * If disabled, the SSL certificate offered by the value supplied in **Alert Logic Domain** will not be verified against the CA database inside of Axonius.
4. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Alert Logic Domain**.
   * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **Alert Logic Domain**.
   * If not supplied, Axonius will connect directly to the value supplied in **Alert Logic Domain**.
5. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Alert Logic Domain** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
6. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the value supplied in **Alert Logic Domain** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
7. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="image.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1178).png" />