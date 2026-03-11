# Source: https://docs.axonius.com/docs/create-topdesk-service-management-asset.md

# TOPdesk - Create or Update Asset

The **TOPdesk - Create or Update Asset** action creates or updates an asset in TOPdesk Enterprise for each asset that matches the parameters of the selected query or assets selected in one of the asset tables.

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

* **Use stored credentials from theTOPdesk adapter** - Select this option to use the first connected TOPdesk adapter credentials.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [TOPdesk](/docs/topdesk) adapter connection.
  </Callout>

## Required Fields

These fields are required to run the Enforcement Action.

* **Template Name** - Enter the name of the TOPdesk asset template.
* **Action Type** - Select whether to create a new asset or to update existing assets.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  **Host Name or IP Address** – The hostname of the TOPdesk server. Required when there is more than one connection.

  * **User Name or Application Name** – Specify the User Name or Application Name. Required when there is more than one connection.

  * **Password** - Enter the password for a user account that has the permissions required to create assets.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Map Axonius fields to TOPdesk fields** - Use the **Field Mapping Wizard** to map Axonius fields to fields in TOPdesk. In this way you can transfer data found in Axonius into TOPdesk. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

  <Callout icon="📘" theme="info">
    Note

    For details, see [Axonius to CMDB Field Mapping](/docs/axonius-to-cmdb-field-mapping).
  </Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [TOPdesk API](https://developers.topdesk.com/explorer/?page=assets#/).

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axoniuscom) if you have a version that is not listed and it is not functioning as expected.

| Version                   | Supported | Notes |
| ------------------------- | --------- | ----- |
| Topdesk API v3 and higher | Yes       |       |

***

For more Enforcement Actions, see [Manage CMDB Assets Category](/docs/manage-cmdb-computer-category).