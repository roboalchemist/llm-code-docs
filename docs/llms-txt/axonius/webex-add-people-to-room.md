# Source: https://docs.axonius.com/docs/webex-add-people-to-room.md

# Webex - Add People to Room

**Webex - Add People to Room** adds users to a specified Webex room for:

* Users returned by the selected query or assets selected on the relevant asset page.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Required Fields

These fields must be configured to run the Enforcement Action.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Cisco Webex adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

    <Callout icon="📘" theme="info">
      To use this option, you must successfully configure a [Cisco Webex](https://docs.axonius.com/axonius-help-docs/docs/cisco-webex) adapter connection.
    </Callout>

* **Room Title** - The name of the room to which to add users.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** *(required, default: empty)* - The hostname or IP address of the Cisco Webex server that Axonius can communicate with via the [Required Ports](#required-ports). For the cloud version the default domain is `https://webexapis.com`.  For Cloud server,
  * **Server Type** - From the dropdown, select one of the following:
    * **On-Prem** (default) - This type of server has the following connection parameter:
      * **Access Token** *(required, default: empty)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.
    * **Cloud** - - This type of server has the following connection parameters:
      * **Client ID** - The client ID that was provided after creating the integration.
      * **Client Secret** - The client secret that was provided after creating the integration.
      * **MFA Code** - The code provided in the query params of the OAuth2 redirection. As it appears here:
        `http://your-server.com/auth?code=YjAzYzgyNDYtZTE3YS00OWZkLTg2YTgtNDc3Zjg4YzFiZDlkNTRlN2FhMjMtYzUz`. For more information, see [Authenticating and Receiving the MFA Code](#authenticating-and-receiving-the-mfa-code).
      * **Redirect URL** *(required, default: `http://localhost`)* - The redirection URI provided during the integration’s creation.
        **Important:** Make sure that the redirect URI you registered to the integration is the same one entered for the adapter connection and the same one you authenticate to.
  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.
  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

* **Additional People to Add** - Enter the username of users you want to add to the room who were not included in the query results.

## APIs

Axonius uses the [Cisco Webex Devices API](https://developer.webex.com/docs/api/v1/devices).

Axonius uses the [Cisco Webex People API](https://developer.webex.com/docs/api/v1/people).

## Required Ports

Axonius must be able to communicate via the following ports:

* **TCP port 443**

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).