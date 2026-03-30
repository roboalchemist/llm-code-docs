# Source: https://docs.axonius.com/docs/domotz.md

# Domotz

Domotz is network monitoring software.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Domotz server.

2. **API Key** *(required)* - An API Key associated with a user account that has the [required permissions](/docs/domotz#required-permissions) to fetch assets.
   **To create an API Key**
   1. From the Domotz portal, under the **Settings** section, select the **API Key** tab.

   2. Click **Create an API Key**.

   3. Enter the password of your Domotz account and click **Unlock** to unlock the service.

   4. Provide a name to the new API Key and click **Create**. The API Key is created. Copy the API Key code and save it in a secure location, as you won't be able to retrieve the API Key later.

3. **Verify SSL**  - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image align="center" alt="Domotz" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/domotz.png" />

## APIs

Axonius uses the [Domotz Public API v1.6.0](https://portal.domotz.com/developers/).

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have Read-only permissions to fetch assets.

## Supported From Version

Supported from Axonius version 4.5