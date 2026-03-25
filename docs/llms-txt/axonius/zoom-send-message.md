# Source: https://docs.axonius.com/docs/zoom-send-message.md

# Zoom - Send Message

**Zoom - Send Message** sends a message in Zoom Team Chat for:

* Assets returned by the selected query or assets selected on the relevant asset page.

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

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.
* **Use stored credentials from Zoom Adapter** - Select this option to use [Zoom](/docs/zoom) connected adapter credentials.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a Zoom adapter connection.
</Callout>

* **Zoom Domain** - The hostname of the Zoom server.
* **Message** - Specify an incident description to be included in the Zoom message.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

<Callout icon="💡" theme="warn">
  <br />

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.
  For more information about these fields, see the Zoom adapter connection form.

  * **Zoom Account ID** - Zoom account ID.

  * **OAuth Client ID** and **OAuth Client Secret** - Zoom uses Server-to-Server OAuth authentication method, enter the Account ID, OAuth Client ID, and OAUth Client Secret to be used to authenticate the request. For more details, see [Create a Server-to-Server OAuth App](https://marketplace.zoom.us/docs/guides/build/server-to-server-oauth-app/#create-a-server-to-server-oauth-app)

  * **Zoom Account ID** - Enter the Zoom Subdomain in the following format: "https//\[account].zoom.us"

  * **Username** and **Password** - The value you enter in the User Name and Password fields in Zoom for the new user you created to allow Axonius to fetch SaaS data.

  * **2FA Secret Key** - The secret generated in Zoom for setting up 2-factor authentication for the Zoom user created for fetching SaaS data.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

## API

Axonius uses the [Zoom Team Chat API](https://developers.zoom.us/docs/api/rest/reference/chat/methods/#operation/sendaChatMessage).

## Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* chat\_message:write:admin
* chat\_message:write

## Required Ports

Axonius must be able to communicate with the Zoom domain via **port 80**.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).