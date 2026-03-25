# Source: https://docs.axonius.com/docs/bigfix-create-fixlet-action.md

# BigFix - Create Fixlet Action

**BigFix - Create Fixlet Action** creates and executes a BigFix Fixlet action on:

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

* **Use stored credentials from the BigFix Adapter** - Select this option to use   BigFix adapter credentials.

  When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

  To use this option, you must successfully configure a [BigFix](/docs/ibm-bigfix) adapter connection.

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Site name** - The related site name for the Fixlet.
* **Fixlet ID** - The BigFix ID of the Fixlet the Enforcement Action will run.
* **Bigfix Action Name** *(required)* - a name for the action in the BigFix environment. The name should be the name from the fixlet action in BigFix
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **BigFix Domain**  - The hostname or IP address of the BigFix server that Axonius can communicate with via the Port.

  * **Port**  - Enter the port.

  * **User Name** and **Password** - The credentials for a user account that has the  Required Permissions   perform this action.

  * **Advanced Settings** *(optional)* - Use to run a query by Relevance expression instead of the regular flow.<br />
    **To run by a Relevance expression in Advanced Settings**

    a. Create a JSON file containing the parameters **relevance** (string) and **fields** (list of fields).

    For example:

    ```
    {
    'relevance': "User-defined name",
    'fields': ['field1', 'field2']
    }
    ```

    b. Upload the JSON file by clicking **Choose file**.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Action | BigFix Developer](https://developer.bigfix.com/rest-api/api/action.html) API.

## Required Ports

Axonius must be able to communicate with the Bigfix server via the following ports:

* TCP port 443
* TCP port 80

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).