# Source: https://docs.axonius.com/docs/torii.md

# Torii

Torii is a SaaS Management Platform letting IT professionals discover, optimize, and control SaaS usage and costs.

## Parameters

1. **Torii Domain** *(required, default: `https://api.toriihq.com`)* - The hostname of the Torii server.
2. **API Key** *(required)* - Specify the API Key provided by Torii.
3. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Torii Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
   * If enabled, the SSL certificate offered by the value supplied in **Torii Domain** will be verified against the CA database inside of Axonius. If the SSL certificate can not be validated against the CA database inside of Axonius, the connection will fail with an error.
   * If disabled, the SSL certificate offered by the value supplied in **Torii Domain** will not be verified against the CA database inside of Axonius.
4. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Torii Domain**.
   * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **Torii Domain**.
   * If not supplied, Axonius will connect directly to the value supplied in **Torii Domain**.
5. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(407\).png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  From version 4.6 Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Exclude External Users** *(required, default: False)* - Choose whether to fetch external users.
   * If enabled, all connections for this adapter will not fetch Torii external users.
   * If disabled, all connections for this adapter will fetch Torii external users.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the Adapter Configuration tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>