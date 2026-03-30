# Source: https://docs.axonius.com/docs/tesma.md

# Tesma

Tesma provides a central database for business information and makes it available in real-time.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Tesma server.

2. **Corporate Group Name** *(required)* - The name of your corporate group as given to you by CHG Meridian.

3. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets, refer to [Tesma Authentication](https://developer.tesma.com/docs/documentation/j0ar436uoufmh-authentication) for details of how to get the API Key.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="tesma" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/tesma.png" />

## APIs

Axonius uses the <Anchor label="Tesma API" target="_blank" href="https://developer.tesma.com/docs/documentation/f3s62o3qpprvb-introduction">Tesma API</Anchor>.

## Supported From Version

Supported from Axonius version 6.0