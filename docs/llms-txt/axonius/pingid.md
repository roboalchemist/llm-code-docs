# Source: https://docs.axonius.com/docs/pingid.md

# PingOne

Ping offers an identity management solution that includes multi-factor authentication, single sign-on, identity verification, and more.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.pingone.com`)* - The hostname or IP address of the PingOne server.

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Environment ID** *(required)* - Specify the ID of the environment from which you want to fetch the users. If the parameter is left empty, all environments associated with the **Client ID** will be fetched.
   To locate the **Client ID** and **Environment ID**, refer to this [ Ping article](https://support.pingidentity.com/s/question/0D51W00006rlXsXSAU/another-helpful-tip-locating-the-client-id-and-environment-id-on-the-app-configuration-page).

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![PingID](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PingID.png)

## APIs

Axonius uses the [PingOne Platform APIs](https://apidocs.pingidentity.com/pingone/platform/v1/api/).

## Supported From Version

Supported from Axonius version 4.6