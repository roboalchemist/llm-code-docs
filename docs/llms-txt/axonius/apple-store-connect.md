# Source: https://docs.axonius.com/docs/apple-store-connect.md

# Apple App Store Connect

Apple App Store Connect is a platform for developers to manage, release, and report on their iOS apps.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.appstoreconnect.apple.com`)* - The hostname or IP address of the Apple App Store Connect server.

2. **Private Key** *(required)* - Upload the private key you have generated. For information on how to generate a private key, see [Creating API Keys for App Store Connect API](https://developer.apple.com/documentation/appstoreconnectapi/creating_api_keys_for_app_store_connect_api).

3. **Private Key ID** *(required)* - The Private Key ID. To get your key ID, copy it from App Store Connect by logging in to App Store Connect, then:
   1. Select **Users and Access**, then select the **API Keys** tab.
   2. The key IDs appear in a column under the **Active** heading. Hover the cursor next to a key ID to display the Copy Key ID link.
   3. Click **Copy Key ID**.

4. **Issuer ID** *(required)* - The Issuer ID. To get your issuer ID, log in to App Store Connect and:
   1. Select **Users and Access**, then select the **API Keys** tab.
   2. The issuer ID appears near the top of the page. To copy the issuer ID, click **Copy** next to the ID.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Apple%20App%20Store%20Connect](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Apple%20App%20Store%20Connect.png)

## APIs

Axonius uses the [App Store Connect API](https://developer.apple.com/documentation/appstoreconnectapi).

## Supported From Version

Supported from Axonius version 6.1