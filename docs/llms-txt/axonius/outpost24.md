# Source: https://docs.axonius.com/docs/outpost24.md

# Outpost24

Outpost24 is a cyber risk management platform that helps organizations assess their attack surface and prioritize vulnerabilities.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Aggregated Security Findings, SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required, default: `https://outscan.outpost24.com`)* - The hostname or IP address of the Outpost24 server.
2. **User Name** and **Password** *(optional)* - The credentials for a user account that has the permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **User Name** and **Password** are not supplied, **API Token** is required.
</Callout>

4. **API Token** *(optional)* - An API Key associated with a user account that has permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **API Token** is not supplied, **User Name** and **Password** are required.
</Callout>

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

9. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image align="center" alt="Outpost24" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Outpost24.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch NetSec Devices**  - Toggle on to fetch network security devices.
2. **Fetch NetSec Vulnerabilities** *(appears only when **Fetch NetSec Devices** is toggled on)* - Select whether to fetch network security vulnerabilities.
3. **Fetch Vulnerabilities** - Select whether to fetch Aggregated Security Findings (vulnerabilities).
4. **Fetch NetSec findings from the last X days**  - Select this option to specify a value in  days from the current day to fetch netsec vulnerabilities according to the last seen date.
5. **Socket receive timeout** *(required, default: 600)* - Enter the number of seconds Axonius should wait for a response for each request sent.

<Image align="center" alt="Outpost24_Advanced" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Outpost24_Advanced.png" />

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the:

* [Outscan API](https://outscan.outpost24.com/opi/rest)
* [Outscan API (if you have your own appliance)](https://your-appliance.outpost24.com/opi/rest)

The REST API uses JWT tokens for granting access to the API's resources.

**To generate a new token, do one of the following**

* Login with username and password by sending a POST request to `/auth/login`

  OR

* Call GET /auth/login with an existing, valid token

For more information, see the [REST API Interface Technical Document](https://kb.outpost24.com/kb/rest-api-interface-technical-document).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port  80**
* **TCP port 443**

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| V1      | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.6