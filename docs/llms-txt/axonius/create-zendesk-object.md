# Source: https://docs.axonius.com/docs/create-zendesk-object.md

# Zendesk - Create Custom Object per Asset

The **Zendesk - Create Custom Object per Asset** action creates a custom object per asset in Zendesk for each asset that matches the parameters of the selected query or assets selected in one of the asset tables.

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

## Required Fields

* **Use stored credentials from the Zendesk adapter** *(required)* - Select this option to use the first connected Zendesk adapter credentials.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Zendesk](/docs/Zendesk) adapter connection.
  </Callout>

* **Custom Object Key** - Key of the custom object type being created in Zendesk.

* **Map Axonius fields to Zendesk Custom Object Fields** -  Use the **Field Mapping Wizard** to map Axonius fields to fields in Zendesk. In this way you can transfer data found in Axonius into Zendesk. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

  <Callout icon="📘" theme="info">
    Note

    For details, see [Axonius to CMDB Field Mapping](/docs/axonius-to-cmdb-field-mapping).
  </Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Sub Domain** - The subdomain used to access Zendesk. For example, Axonius is the subdomain for [https://axonius.zendesk.com/](https://axonius.zendesk.com/).

  * **User name and Password** - The username and password of your Zendesk user.

  * **API Key/Token** - An API Key/Token associated with a user account that has permissions to  perform this action.

  * **2FA Secret Key** - The secret generated in Zendesk for setting up two-factor authentication for the Zendesk user created to collect SaaS Management data.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

* **Update Object if External ID exists** *(optional)* - Select this option to update existing custom object with the given external ID (the default is Axonius ID), with the fields specified in the Axonius to Zendesk Field Mapping.

* **Create Custom Object Key if not exists** *(optional)* - Select this option to create a custom object key when a key does not exist.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Zendesk API](https://developer.zendesk.com/api-reference/custom-data/custom-objects/custom_object_records/#create-custom-object-record).

## Required Permissions

To perform this action, the Zendesk user must have Agent permissions.

***

For more Enforcement Actions, see [Manage CMDB Assets Category](/docs/manage-cmdb-computer-category).