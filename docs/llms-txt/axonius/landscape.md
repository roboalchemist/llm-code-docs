# Source: https://docs.axonius.com/docs/landscape.md

# Landscape

Landscape by Canonical is a management tool used to deploy, monitor and manage Ubuntu servers.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Software
* SaaS Applications

## Parameters

1. **Endpoint URL** *(required, default: landscape.canonical.com)* - The hostname or IP address of the Landscape server. If you want to access another endpoint URL, enter: https\://*server*/ (replace *server* with the FQDN of Landscape server you are accessing).
2. **Access Key** and **Secret Key** *(optional)* - An API Access Key and API Secret Key associated with a user account that has permissions to fetch assets.
   To obtain the access key and secret key, login to Landscape and click on your username in the top right corner.

<Callout icon="📘" theme="info">
  Note

  If enabling API Version 1, **Access Key** and **Secret Key** are required.
</Callout>

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

<Callout icon="📘" theme="info">
  Note

  * Self-signed certificates don't work on the Landscape server. The certificates must be signed by a CA.

  * To prevent failed fetches, verify that the time on the Landscape server is set correctly.
</Callout>

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

9. **API Version** *(default: Version 1)* - The version number of the Landscape API. Select either Version 1 or Version 2. If you select Version 2, the following fields appear:
   * **Email** and **Password** - The email and password of the user.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Landscape](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Landscape.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Enrich Devices with Installed Packages** - Select this option to fetch devices with packages installed on Linux laptops covered by Landscape.
2. **Enrich Devices With Installed Snaps (API v2 only)** - Select this option to fetch devices with snaps installed on Linux laptops covered by Landscape.
3. **Parse 'title' as Last Used Users** - Select this option to parse the title to Last Used Users and the hostname to Asset Name.
4. **Fetch Software Deny List (API v1 only)** - Toggle on this option to fetch the software deny list. If enabled, the following options are available:
   * **Package Profile Name** - Enter the package profile name.
   * **Package Profile ID** -  Specify the package profile ID number.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Landscape API](https://landscape.canonical.com/static/doc/api/).

## Supported From Version

Supported from Axonius version 4.5