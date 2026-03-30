# Source: https://docs.axonius.com/docs/tenable-ad.md

# Tenable Identity Exposure (formerly Tenable.ad)

Tenable Identity Exposure (formerly Tenable.ad) provides real-time security monitoring for Microsoft Active Directory (AD) infrastructures.

## Asset Types Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Alerts_Incidents.svg) Alerts/Incidents

## Before You Begin

### APIs

Axonius uses the [Tenable.ad API](https://doc.tenable.ad/reference/get_api-about).

### Supported From Version

Supported from Axonius version 6.0

## Connecting the Adapter in Axonius

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Tenable Identity Exposure server.

2. **API Key** -  An API Key associated with a user account that has permissions to fetch assets. See [Tenable Identity Exposure documentation](https://docs.tenable.com/identity-exposure.htm) for information about how to retrieve the API Key (under the **Product Documentation** section).

<Image alt="TenableIdentityExposure" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-ZU76FGCZ.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**  - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

### Endpoints Config

* **Enrich Users with Deviances** - Enable this to enrich Users with information on Deviances, which are the actual instances of issues. When enabled, you also have the option to enable the following setting:
  * **Enrich Deviances with Checkers** - Enable to enrich Deviances with Checker details (issue type). Here is some sample data that can be fetched when this is enabled:

    <Image border={false} src="https://files.readme.io/46c59fe60ca111c9cf2e88acddc17d26055bd67a897bf9311289dae9a0a67e9c-image.png" />
* **Enrich LDAP Objects - Users with Deviances** - Enable this to enrich LDAP Users with information on Deviances. When enabled, you also have the option to enable the following setting:
  * **Enrich Deviances with Checkers** - see above.
* **Enrich AD LDAP Objects - Devices with Deviances** - Enable this to enrich LDAP Devices with information on Deviances. When enabled, you also have the option to enable **Enrich Deviances with Checkers**.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>