# Source: https://docs.axonius.com/docs/sentinelone-send-broadcast-msg.md

# SentinelOne - Send Broadcast Message

**SentinelOne - Send Broadcast Message** sends a broadcast message to:

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
* **Use stored credentials from the [SentinelOne](/docs/sentinelone) adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [SentinelOne](/docs/sentinelone) adapter connection.
</Callout>

* **Message** - Enter the content of the broadcast message.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  <br />

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **SentinelOne Domain** - The hostname or IP Address of the SentinelOne management server. This field format is '\[instance].sentinelone.net'.

  * **User Name** and **Password** - The user name and password for an account that has site viewer access to the management server. For information on how to create users in SentinelOne, see [Create a Single User](https://euce1-100.sentinelone.net/login#creating-a-single-user).

  * **2FA Secret** *(only for accounts with SaaS Management capability)* - The secret generated in SentinelOne for setting up two-factor authentication for the adapter user created for collecting SaaS data.

  * **Singularity Data Lake (SDL) API Key** - Relevant for enabling SDL queries. See the [Parameters section](/docs/sentinelone#parameters) in the SentinelOne adapter page for details.

  * **API token** - The API token is created within the My User Profile of the account with viewer access to the management server.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## API

Axonius uses the [SentinelOne](https://usea1-009.sentinelone.net/login) API.

## Required Ports

Axonius must be able to communicate via the following ports:

* 80
* 443

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).