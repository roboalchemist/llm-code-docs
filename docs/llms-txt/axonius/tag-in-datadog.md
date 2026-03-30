# Source: https://docs.axonius.com/docs/tag-in-datadog.md

# Datadog - Add Tag to Assets

**Datadog - Add Tag to Assets** adds or removes a specified tag to the Datadog hosts that are the result of the saved query supplied as a trigger (or devices selected in the asset table).

<Callout icon="📘" theme="info">
  Note

  This action uses the Datadog adapter credentials to perform the tagging.
</Callout>

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

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

1. **Use stored credentials from the adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

   * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

   <Callout icon="📘" theme="info">
     Note

     To use this option, you must successfully configure a [Datadog](/docs/datadog) adapter connection.
   </Callout>

2. **Tag name** - Specify a tag name to be added to the host.

3. **Source name** - Source name to attach to tag. A list of valid source names can be found here:[List of valid source names](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value)

4. **Compute Node** - The Axonius node to use when connecting to the specified host. For more details, see [Connecting Additional Axonius Nodes](/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  1. **Datadog Domain** - The hostname or IP address of the Datadog server.
  2. **Application Key** and **API Key** - API and Application Keys associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

  <Callout icon="📘" theme="info">
    Note

    You must generate the API and Application Keys from two locations in the Datadog admin console.  In order for this to work, you need to pair both keys in the adapter wizard, as Datadog doesn't authenticate using only the Application Key — even with the scope of the key specified.
  </Callout>

  3. **Verify SSL** - Verify the SSL certificate offered by the value supplied in **Datadog Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
  4. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Datadog Domain**.
</Callout>

* **Use lowercase hostnames** *(default: true)* - Enable this to send the hostnames to Datadog in lowercase.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).