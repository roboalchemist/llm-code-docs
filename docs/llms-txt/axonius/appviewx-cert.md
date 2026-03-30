# Source: https://docs.axonius.com/docs/appviewx-cert.md

# AppViewX CERT+

AppViewX's CERT+ provides end–to–end lifecycle management for x.509 digital certificates across complex networks.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Certificates

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the AppViewX CERT+ server that Axonius can communicate with via the [Required Ports](#required-ports). Note: Use \[http\:// | https\:// ]host\_or\_ip:port notation. The API port is usually 31443.

   Example: `https://appviewx.local:31443`

2. **User Name** or **Client ID** *(required)* - If **Use Service Account Login** is selected, then this is used as the Client ID for authentication via the Service Account Login flow. Otherwise this is used as the user name for the User Account Login flow.

3. **Password** or **Client Secret** *(required)* - If **Use Service Account Login** is selected, then this is used as the Client Secret for authentication via the Service Account Login flow. Otherwise this is used as the password for the User Account Login flow.

<Callout icon="📘" theme="info">
  Notes

  * For information about Service Account Login, see [Authentication using a Service Account](https://helpcenter.appviewx.com/techdoc/index?GuideSearch%5Bversion_id%5D=56\&GuideSearch%5Bproduct_id%5D=\&guide_html=2023.1.0_FP3/CERT/CERT%20Guides/webhelp-responsive/oxy_ex-1/CERT%20API%20Guide/accessing_api_with_service_account.html\&guide_pdf=2023.1.0_FP3/CERT/CERT%20Guides/cert_cert_guides.pdf).

  * For information about User Account Login, see [Authentication using a User Account](https://helpcenter.appviewx.com/techdoc/index?GuideSearch%5Bversion_id%5D=56\&GuideSearch%5Bproduct_id%5D=\&guide_html=2023.1.0_FP3/CERT/CERT%20Guides/webhelp-responsive/oxy_ex-1/CERT%20API%20Guide/accessing_api_with_user_account.html\&guide_pdf=2023.1.0_FP3/CERT/CERT%20Guides/cert_cert_guides.pdf).
</Callout>

4. **Use Service Account Login** - Select this option to use the Service Account Login flow when authenticating against the API.

<Callout icon="📘" theme="info">
  Notes

  * The vendor recommends using this login flow for enhanced security.

  * This is only available in AppViewX CERT+ version 2023.1.0\_FP3 and above. Earlier versions must use the default, which is User Account Login flow, using the user name and password supplied.
</Callout>

5. **Gateway Key** *(optional)* - Add your tenant's GWKey for multi-tenant environments (deprecated in version 2023.1.0\_FP3).

6. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

7. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

8. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

9. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="AppViewX CERT" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AppViewX%20CERT.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Certificate of sub type server from Server Certificates** - By default Axonius fetches the certificate of the subtype server from Server Certificates. Toggle off to not fetch the certificate of the subtype server from Server Certificates.
2. **Fetch Certificate of sub type client from Client Certificates** - Toggle on to fetch the certificate of the subtype client from Client Certificates.
3. **Fetch Certificate of sub type code\_sign from Code Signing Certificates** - Toggle on to fetch the certificate of the subtype code\_sign from Code Signing Certificates.
4. **Fetch Certificate of sub type device from Device Certificates** - Toggle on to fetch the certificate of the subtype device from Device Certificates.
5. **Fetch Certificate of sub type root\_ca from Root CA Certificates** - Toggle on to fetch the certificate of the subtype root\_ca from Root CA Certificates.
6. **Fetch Certificate of sub type intermediate\_ca from Intermediate CA Certificates**  - Toggle on to fetch the certificate of the subtype intermediate\_ca from Intermediate CA Certificates.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the AppViewX CERT+ API.

* [Authentication using a Service Account](https://helpcenter.appviewx.com/techdoc/index?GuideSearch%5Bversion_id%5D=56\&GuideSearch%5Bproduct_id%5D=\&guide_html=2023.1.0_FP3/CERT/CERT%20Guides/webhelp-responsive/oxy_ex-1/CERT%20API%20Guide/accessing_api_with_service_account.html\&guide_pdf=2023.1.0_FP3/CERT/CERT%20Guides/cert_cert_guides.pdf)
* [Authentication using a User Account](https://helpcenter.appviewx.com/techdoc/index?GuideSearch%5Bversion_id%5D=56\&GuideSearch%5Bproduct_id%5D=\&guide_html=2023.1.0_FP3/CERT/CERT%20Guides/webhelp-responsive/oxy_ex-1/CERT%20API%20Guide/accessing_api_with_user_account.html\&guide_pdf=2023.1.0_FP3/CERT/CERT%20Guides/cert_cert_guides.pdf)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the API port, as configured in the AppViewX CERT+ application. The API port is usually 31443.

## Required Permissions

* API access

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                  | Supported | Notes                                                         |
| ------------------------ | --------- | ------------------------------------------------------------- |
| Minimum version 2023.1.0 | Yes       | Service Account Login requires at least version 2023.1.0\_FP3 |

## Supported From Version

Supported from Axonius version 6.1.29.0