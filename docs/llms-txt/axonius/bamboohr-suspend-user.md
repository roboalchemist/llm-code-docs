# Source: https://docs.axonius.com/docs/bamboohr-suspend-user.md

# BambooHR - Suspend Employee

**BambooHR - Suspend Employee** deactivates the BambooHR account for:

* Assets that match the results of the selected saved query and match the Enforcement Action dynamic statement, if defined, or assets selected on the relevant asset page.

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

* **Use stored credentials from BambooHR adapter** - Select this option to use the BambooHR connected adapter credentials.
  * When you select this option, the **Select Adapter Connection** dropdown is available, and you can choose which adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [BambooHR](/docs/bamboohr) adapter connection.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

<Callout icon="💡" theme="warn">
  <br />

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **BambooHR Subdomain** - The BambooHR Subdomain value is used to log into your BambooHR instance. For example, if your BambooHR instance is *mycompany.bamboohr.com*, specify "mycompany".

  * **API Key** - To get the API key value, go to *https\://\<your\_subdomain>.bamboohr.com/settings/permissions/api.php* and create a new key. If you do not have permission to do so, contact your BambooHR administrator.

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **Fetch users from endpoint** - From the dropdown, select the endpoint from which to fetch users.

  * **Reports/Custom** - Select users from custom reports. Recommended. Refer to [Custom report API](https://documentation.bamboohr.com/reference/request-custom-report-1) for information.

  * **Employees/Directory** - Select users from the employees directory.
</Callout>

<Callout icon="📘" theme="info">
  Note

  As these parameters are customer specific, Axonius does not validate them. You must make sure the provided values are correct. Otherwise, the request might fail.
</Callout>

## APIs

Axonius uses the [Get Employee](https://documentation.bamboohr.com/reference/get-employee) API.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).