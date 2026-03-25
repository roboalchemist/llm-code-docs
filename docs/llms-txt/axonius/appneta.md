# Source: https://docs.axonius.com/docs/appneta.md

# AppNeta

AppNeta provides monitoring of network paths, flows, packets, and web applications.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the AppNeta server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Access Token** *(required)* - An API Key associated with a user account that has permissions to fetch assets.
   To create an access token, see [Create an Access Token](/docs/appneta#create-an-access-token).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="AppNeta" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AppNeta.png" />

## APIs

Axonius uses the AppNeta API.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80**
* **TCP port 443**

## Required Permissions

The value supplied in [API Access Token](#parameters) must be associated with credentials that have permissions to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| v3      | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.6

## Create an Access Token

**To create an access token**

1. Navigate to ![cogwheel50x](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/cogwheel50x.png)  `>` **Manage Access Tokens**.
2. Click **Create Token**.
3. Enter a token name. The name can be descriptive and include spaces.
4. Specify an expiration date or select **Never**. The token is automatically revoked when reaching the expiration date.
5. In the **Roles** section, specify the permissions for the token (less than or equal to the user's permissions).
6. In the **Organization Membership** section, select **Use dynamic membership** if you want the token to access any organizations that you have now and in the future (as new organizations are added or removed).
7. In the **Select Organizations** section, select the organizations you want the token to have access to.

<Callout icon="📘" theme="info">
  Note

  The selection of organizations is static. New organizations available to you won't be accessible by the token.
</Callout>

8. Click **Create Token**.
9. Copy the token and save it to a secure location, as the token won't appear again.
10. Click **Finished**.