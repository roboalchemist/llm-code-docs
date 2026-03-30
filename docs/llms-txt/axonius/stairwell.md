# Source: https://docs.axonius.com/docs/stairwell.md

# Stairwell

Stairwell offers a threat hunting and detection and response platform called “Inception.”

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required, default: `https://app.stairwell.com`)* - The hostname or IP address of the Stairwell server.

2. **API Key** *(required)* -  An API Key used to send requests to the Notifications API.

3. **Environment ID** *(required)* - Specify the ID of the environment from which you want to fetch the devices. Refer to [this guide](https://docs.stairwell.com/docs/how-to-find-the-environment-id) for instructions on how to find the environment ID.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Stairwell](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Stairwell.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Parse label as Asset Name & Host Name** - Select this option to parse the label field as the asset name and host name.
2. **Parse hostname and serial number if hyphen is surrounded by spaces** - Select this option to parse the hostname and serial number if there are spaces surrounding the hyphen in the asset name for macOS devices. For example: ABCD-1234 will not be parsed, but ABCD - 1234 will be parsed.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the following APIs:

* [Notifications API ](https://stairwell.notion.site/Partner-Inception-API-Docs-7ce117297b464facaf8865fce9437633#f724bca7cb024db28546f99cc4a17a50)
* [File Enhancments API](https://help.stairwell.com/en/knowledge/stairwell-inception-file-reputation-api)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 4.8