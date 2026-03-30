# Source: https://docs.axonius.com/docs/zscaler-add-remove-url-category.md

# Zscaler - Add or Remove URL to/from Category

**Zscaler - Add or Remove URL to/from Category** adds a URL to or removes a URL from a custom category in Zscaler, based on the category ID, for:

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

* **Use stored credentials from Zscaler Web Security adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.
    <br />

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Zscaler Web Security](/docs/zscaler-web-security) adapter connection.
</Callout>

* **Action to perform** - Select whether to add or remove a URL.
* **Custom Category** - Enter the IDs of the custom categories.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Zscaler Domain** - Specify the Zscaler cloud name that was provisioned for your organization. For example:
    * admin.zscalerbeta.net
    * admin.zscalerone.net
    * admin.zscalertwo.net
    * admin.zscaler.net
    * admin.zscloud.net
    * admin.zscalerdomain.net
    * mobileadmin.zscalerdomain.net
    * mobile.zscalerdomain.net
  * **Auth Method** - Select **API Key** or **ZIdentity**. The relevant parameters appear according to the Auth Method you selected. See the [ Zscaler Web Security documentation](https://axonius-help-group.readme.io/docs/zscaler-web-security#/connecting-the-adapter-in-axonius) for details about the parameters required for each method.
  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
    <br />
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the <Anchor label="Zscaler API" target="_blank" href="https://help.zscaler.com/zia/configuring-url-categories-using-api">Zscaler API</Anchor>.

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).

<br />