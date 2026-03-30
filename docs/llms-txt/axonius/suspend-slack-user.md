# Source: https://docs.axonius.com/docs/suspend-slack-user.md

# Slack - Suspend User

**Slack - Suspend User** deactivates the Slack account for:

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

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from Slack adapter** - Select this option to use the [Slack](/docs/slack) connected adapter credentials.
  When you select this option, the **Select Adapter Connection** dropdown is available, and you can choose which adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Slack](/docs/slack) adapter connection.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** - The hostname or IP address of the Slack server that Axonius can communicate with via the [Required Ports](#required-ports)..

  * **Authentication Token** -  An Authentication Token associated with a user account that has the Required Permissions to fetch assets.

  * **Account Sub Domain** - The Slack user account subdomain value used to log into your Slack instance. For example, if your Slack instance is *mycompany.slack.com*, specify "mycompany".

  * **Username and Password** - The credentials for the Slack user account that has the [Required Permissions](#required-permissions) to fetch assets.

  * **MFA Secret** - The MFA Secret Key configured for the [Slack](/docs/slack) adapter.

  * **Enterprise Grid Organization** - Select whether to use the Slack plan that allows connecting multiple workspaces inside Axonius.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## API

Axonius uses the [Slack SCIM API](https://api.slack.com/admins/scim#patch-users-id).

## Required Ports

Axonius must be able to communicate with the value supplied in [Hostname or IP Address](#parameters) via the following port:

* **TCP port 80**: HTTP

## Required Permissions

The stored credentials, or those provided in Connection and Credentials, must have have the  following permissions:

* OAuth token with admin scope

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).