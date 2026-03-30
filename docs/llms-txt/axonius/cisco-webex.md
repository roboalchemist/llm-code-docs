# Source: https://docs.axonius.com/docs/cisco-webex.md

# Cisco Webex

Cisco Webex is an enterprise solution for video conferencing, online meetings, screen share, and webinars.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required, default: empty)* - The hostname or IP address of the Cisco Webex server that Axonius can communicate with via the [Required Ports](#required-ports). For the cloud version the default domain is `https://webexapis.com`.  For Cloud server,

2. **Server Type** - From the dropdown, select one of the following:
   * **On-Prem** (default) - This type of server has the following connection parameter:
     * **Access Token** *(required, default: empty)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.
   * **Cloud** - - This type of server has the following connection parameters:
     * **Client ID** - The client ID that was provided after creating the integration.
     * **Client Secret** - The client secret that was provided after creating the integration.
     * **MFA Code** - The code provided in the query params of the OAuth2 redirection. As it appears here:
       `http://your-server.com/auth?code=YjAzYzgyNDYtZTE3YS00OWZkLTg2YTgtNDc3Zjg4YzFiZDlkNTRlN2FhMjMtYzUz`. For more information, see [Authenticating and Receiving the MFA Code](#authenticating-and-receiving-the-mfa-code).
     * **Redirect URL** *(required, default: `http://localhost`)* - The redirection URI provided during the integration’s creation.
       **Important:** Make sure that the redirect URI you registered to the integration is the same one entered for the adapter connection and the same one you authenticate to.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="CiscoWebexOnPremServer" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CiscoWebexOnPremServer.png" />

<Image alt="CiscoWebexCloudServer" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CiscoWebexCloudServer.png" />

## APIs

Axonius uses the [Cisco Webex Devices API](https://developer.webex.com/docs/api/v1/devices).

Axonius uses the [Cisco Webex People API](https://developer.webex.com/docs/api/v1/people).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Required Permissions

The value supplied in [Access Token](#parameters) must be associated with the following permissions in order to fetch assets:

* **Devices**
  * **spark:devices\_read** - See details for the devices in the integration's organization (associated with the creator's organization).
  * **spark-admin:devices\_read** - See details for the devices in your entire organization.

* **Users**

  * **spark-admin:people\_read** - Viewing the list of all people in your organization requires admin privileges.

## Setting Up the Integration

To create an integration, follow the instructions in [Build - Integrations | Webex for Developers](https://developer.webex.com/docs/integrations#registering-your-integration), making sure to do the following:

* In the **Requesting Permission** section of the integration, select the following options:
  * **spark:devices\_read** - See details for the devices in the integration's organization (associated with the creator's organization).

  * **spark-admin:devices\_read** - See details for the devices in your entire organization.
* To fetch users, the signed-in user must have Admin privileges.
  * **spark-admin:people\_read** - Viewing the list of all people in your organization.

## Authenticating and Receiving the MFA Code

1. Navigate to `https://webexapis.com/v1/authorize?client_id=\{client_id}&response_type=code&redirect_uri=\{redirect_uri}&scope=spark-admin:people_read&spark-admin:devices_read&state=AXONIUS_STATE`

   * Replace CLIENT\_ID and REDIRECT\_URI with the actual values.
     You are redirected to a Webex login page.

2. Log in to Webex.
   You are redirected to the REDIRECT\_URI that you provided.
   It should look like this: `http://localhost?code=YjAzYzgyNDYtZTE3YS00OWZkLTg2YTgtNDc3Zjg4YzFiZDlkNTRlN2FhMjMtYzUz&state=AXONIUS_STATE`

3. Copy the **code** query parameter and use it as the MFA Code in your Webex adapter.

<Callout icon="📘" theme="info">
  Note

  Your code ends right before the “&”. In the example above, your code is: `YjAzYzgyNDYtZTE3YS00OWZkLTg2YTgtNDc3Zjg4YzFiZDlkNTRlN2FhMjMtYzUz`
</Callout>

## Related Enforcement Actions

* [Webex - Add People to Room](https://docs.axonius.com/axonius-help-docs/docs/webex-add-people-to-room)
* [Webex - Send Message to Room](https://docs.axonius.com/axonius-help-docs/docs/webex-send-message-to-room)