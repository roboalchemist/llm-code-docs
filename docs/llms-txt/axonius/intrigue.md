# Source: https://docs.axonius.com/docs/intrigue.md

# Intrigue

Intrigue enables IT and Security teams with a complete and always up to date view of Cloud and Internet-exposed assets and exposures.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Collection Name** *(required)* - The Intrigue collection name.
2. **Access API Key** and **Secret API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.
3. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by **[https://app.intrigue.io/](https://app.intrigue.io/)**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-amp-ca-settings).
   * If enabled, the SSL certificate offered by **[https://app.intrigue.io/](https://app.intrigue.io/)** will be verified against the CA database inside of Axonius. If the SSL certificate can not be validated against the CA database inside of Axonius, the connection will fail with an error.
   * If disabled, the SSL certificate offered by **[https://app.intrigue.io/](https://app.intrigue.io/)** will not be verified against the CA database inside of Axonius.
4. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to **[https://app.intrigue.io/](https://app.intrigue.io/)**.
   * If supplied, Axonius will utilize the proxy when connecting to **[https://app.intrigue.io/](https://app.intrigue.io/)**.
   * If not supplied, Axonius will connect directly to **[https://app.intrigue.io/](https://app.intrigue.io/)**.
5. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to **[https://app.intrigue.io/](https://app.intrigue.io/)** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
6. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to **[https://app.intrigue.io/](https://app.intrigue.io/)** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1401).png" />

## APIs

Axonius uses the [Intrigue.io APIs](https://help.intrigue.io/reference/authenticating-to-intrigueio-apis).

## Required Permissions

The values supplied in [**Access API Key** and **Secret API Key**](#parameters) must have read access to devices.

To generate [**Access API Key** and **Secret API Key**](#parameters), login to Intrigue, browse to your profile, and select **Generate Token** under  the **API Access** section.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1402\).png)