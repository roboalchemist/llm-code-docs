# Source: https://docs.axonius.com/docs/tanium-deploy-software.md

# Tanium - Create Software Deployment

**Tanium - Create Software Deployment** installs, updates, or removes existing software packages preconfigured on the Tanium server from specific devices for.

* Assets that match the results of the selected saved query, and match the Enforcement Action Conditions, if defined or assets selected on the relevant asset page.

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

* **Use stored credentials from the  Tanium Client Status  adapter** - Select this option to use **[Tanium Client Status](/docs/tanium-status)** connected adapter credentials.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Tanium Client Status](/docs/tanium-status) adapter connection.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

1. **Tanium Software Package ID** - Software Package ID for the software to be deployed.
2. **Deployment Operation** - Select the operation to run, either 'Install', 'Update' or 'Remove'.
3. **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Hostname or IP Address**  - The Hostname or IP address of the Tanium server that Axonius can communicate with. The adapter supports both on-premise and Tanium Cloud instances. When connecting to a Tanium Cloud instance, "**-api**" must be added to the end of the subdomain of your Tanium Cloud instance. For example: "*domain.cloud.tanium.com*" should be entered as "*domain-api.cloud.tanium.com*".

  * **User Name or API Token ID** - The credentials for a user account that has   Permissions  to perform this action. If an API token is being used for authentication, this must be the ID of the API token. The Token ID column in Tanium may be hidden.

  * **Password or API Token** - The credentials for a user account that has the  Permissions  to perform this action. If an API token is being used for authentication, this must be the API token string.

  <Callout icon="📘" theme="info">
    Note

    Refer to [Tanium Client Status Adapter](/docs/tanium-status#parameters) to learn more about the API Token.
  </Callout>

  * **Only fetch clients that have registered in the past N minutes**   - Only fetch assets that have registered with the Tanium platform within the past minutes supplied by this value. Tanium considers any agent that has not reported in the past 5 minutes as "broken". However, leave this value **empty** if you want to be able to build queries in Axonius that check for "broken agents". A value of **0** will disable this filter.
  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
  * **Max devices per deploy** *(default: 10)* - Set a maximum number of devices on which to run this action.
</Callout>

## Required Permissions

The credentials used to connect to Tanium must have permission to create software deployments.

***

For more details about other Enforcement Actions available, see [Action Library](https://docs.axonius.com/docs/action-library).