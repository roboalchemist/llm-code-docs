# Source: https://docs.axonius.com/docs/checkpoint-harmony-mobile.md

# Check Point Harmony Mobile

Check Point Harmony Mobile uses file protection capabilities to block the download of malicious files to mobile devices and prevent file-based cyberattacks on organizations.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Infinity Portal Region** *(required)* - The Check Point Infinity Portal region where the customer’s Infinity Portal services are hosted.  Used for authentication.

2. **Client ID** and **Access Key** *(required)* - API key for authentication. Refer to [Checkpoint API keys](https://sc1.checkpoint.com/documents/Infinity_Portal/WebAdminGuides/EN/Infinity-Portal-Admin-Guide/Content/Topics-Infinity-Portal/API-Keys.htm?tocpath=Global%20Settings%7C_____7#API_Keys) for information on how to geneate the API Key.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![CheckPointHarmonyMobile](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CheckPointHarmonyMobile.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  From Version 4.6, Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Devices per page** *(default: 200)* -  Set the number of devices per page to fetch, min 10, max 1000

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Harmony API](https://app.swaggerhub.com/apis-docs/Check-Point/harmony-mobile/1.0.0-oas3)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Required Permissions

The value supplied in [Client ID](#parameters) must be associated with credentials that have Admin permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 4.8