# Source: https://docs.axonius.com/docs/cylance-delete-devices.md

# Cylance - Delete Devices

**Cylance - Delete Devices** deletes assets in Cylance for each asset that matches the parameters of the selected saved query, and the other Enforcement Action settings or the assets selected on the relevant asset page.
​

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

* **Use stored credentials from CylancePROTECT adapter** - Select this option to use the first CylancePROTECT connected adapter credentials. [SAS Concur](/docs/sap-concur)
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

## Required Fields

These fields are required to run the Enforcement Action.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Cylance Domain** - Use **protectapi.cylance.com**. Note this value is different than the common domain, which is **protect.cylance.com**.

  * **Application ID** , **Application Secret** and **Tenant API Key** - The application ID, secret and associated API Key created in the 'Integrations' section of the Cylance console.

  * **Tenant Tag** - Automatically tag all devices discovered by the specific adapter server.

  * **Cylance Zones Include list** - Specify a comma-separated list of Cylance zones. The connection for this adapter will only fetch devices associated with at least one of the zones provided in this list. Otherwise, it will fetch all devices from Cylance.

  * **Cylance Zones Exclude list** - Specify a comma-separated list of Cylance zones. The connection for this adapter will not fetch devices associated with at least one of the zones provided in this list. Otherwise, it will fetch all devices from Cylance.

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

***

For more details about other Enforcement Actions available, see [Action Library](https://docs.axonius.com/docs/action-library).