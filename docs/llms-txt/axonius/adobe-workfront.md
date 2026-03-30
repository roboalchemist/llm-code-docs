# Source: https://docs.axonius.com/docs/adobe-workfront.md

# Adobe Workfront

Adobe Workfront is work and project management software for enterprise resource management, cross-team collaboration, and strategic planning.

Related Enforcement Action:

[Adobe Workfront - Create Issue](/docs/adobe-wf-create-issue)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* Tickets

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Adobe Workfront server that Axonius can communicate with via the [Required Ports](#required-ports).

<Callout icon="📘" theme="info">
  Note

  One of the following options is required for authentication: **API Key**, **User Name**/**Password**, or **Client ID**/**Client Secret**.
</Callout>

2. **API Key** *(optional)* - An API Key associated with a user account that has the appropriate permissions to make the API calls below. For more information, see [API key Authentication](https://developer.adobe.com/developer-console/docs/guides/authentication/APIKeyAuthentication/).

<Callout icon="📘" theme="info">
  Note

  In order to ensure that Adobe servers accept API requests from all the domains your application uses, you must add the IP address of your Axonius system as 'allow listed origins' during API Key credential setup. On Axonius-hosted systems, contact Axonius support to get your Axonius IP address.
</Callout>

3. **Username** and **Password** *(optional)* - The credentials for a user account that has permission to fetch assets.

4. **Client ID** and **Client Secret** *(optional)* - The parameters for oAuth authentication, used in the cloud version of Adobe Workfront. Learn [how to create an oAuth2 application and generate these parameters](https://experienceleague.adobe.com/en/docs/workfront/using/adobe-workfront-api/api-notes/oauth-app-jwt-flow).

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

9. **API Version** *(optional; default: v14.0)* - From the dropdown, select the required API version **v14.0** or **v15.0**.

<Image alt="AdapterAdobeWorkfront.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdapterAdobeWorkfront.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch EC Action ticket updates** - Select this option to configure the adapter to fetch updates on tickets created by Axonius users. The updated ticket information is displayed in the **Tickets** table showing information on all tickets in the system (**Assets> Tickets**) or on Tickets of a specific asset (in the **Asset Profile** of the relevant asset).

## APIs

Axonius uses the [Adobe Workfront One API](https://developer.workfront.com/index.html).

Axonius uses the following endpoint:

* [API Basics](https://experienceleague.adobe.com/en/docs/workfront/using/adobe-workfront-api/api-general-information/api-basics)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80**
* **TCP port 443**

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| V14.0   | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.6