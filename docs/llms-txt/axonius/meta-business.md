# Source: https://docs.axonius.com/docs/meta-business.md

# Meta Business

Meta Business is a customer relationship management (CRM) and advertising platform for management of customer data, marketing campaigns, and advertising efforts across Meta's social media platforms.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(default: `https://graph.facebook.com`)* - The hostname or IP address of the Meta Business server.

2. **Access Token** *(required)* - An Access Token associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. For information on how to create an access token, see [Install Apps, Generate, Refresh, and Revoke Tokens](https://developers.facebook.com/docs/marketing-api/system-users/install-apps-and-generate-tokens).

3. **Business ID** *(required)* - The business ID obtained when creating the Business Manager, which is necessary for querying it. For more details, see [Business Manager - Get Started](https://developers.facebook.com/docs/marketing-api/business-manager/get-started/).

4. **API Version** *(optional)* - Enter the version of the Meta Business Management API. For more details, see [Platform Versioning](https://developers.facebook.com/docs/graph-api/guides/versioning/).

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Meta Business](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Meta%20Business.png)

## APIs

Axonius uses the [Meta Business Management APIs](https://developers.facebook.com/docs/business-management-apis).

## Required Permissions

Meta Business requires 'Advanced Access' for permissions. For more information, see [Access Levels](https://developers.facebook.com/docs/graph-api/overview/access-levels/).

## Supported From Version

Supported from Axonius version 6.1