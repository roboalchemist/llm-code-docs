# Source: https://docs.axonius.com/docs/paloalto-xdr-run-script.md

# PANW Cortex XDR - Run Script

**PANW Cortex XDR - Run Script** runs scripts on assets returned by the selected query or assets selected on the relevant asset page. This enables Axonius to automate security response and remotely manage endpoints

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

* **Use stored credentials from the Palo Alto Networks Cortex XDR adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Palo Alto Networks Cortex XDR](/docs/palo-alto-networks-cortex-xdr) adapter connection.
</Callout>

* **Script ID** - The ID of the script you want to run.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Cortex XDR Domain** - The hostname of the Palo Alto Networks Cortex XDR API server. Example: `api-CUSTOMER.xdr.us.paloaltonetworks.com`

  * **URL Base Path** - Specify the fully qualified domain name (FQDN). For more details, see [Get Started with Cortex XDR APIs](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR-REST-API/Get-Started-with-Cortex-XDR-APIs).

  * **API Key ID** and **API Key** - Specify the API key and the API key ID of an **Advanced Security Level API**, as generated in Cortex XDR app. A standard API key will not work — this integration requires an Advanced Security level API key. For more details on generating an Advanced Security Level API, see [Get Started with Cortex XDR APIs](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR-REST-API/Get-Started-with-Cortex-XDR-APIs).

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Additional fields (json format)** - Specify additional fields to be added as part of the script as key/value pairs in a JSON format. For example:

```json
{"field1": "value1", "field2": "value2"}
```

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Cortex XDR API](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR-REST-API/Run-Script).

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).