# Source: https://docs.axonius.com/docs/tag-tenableio-assets.md

# Tenable Vulnerability Management - Add or Remove Tags to/from Assets

**Tenable Vulnerability Management - Add or Remove Tags to/from Assets** adds or removes specified tags to/from:

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

## APIs

To successfully run this Enforcement Set, the following API endpoints and roles are required:

**API Endpoints**

* GET /tags/values
* POST /tags/values
* POST /tags/assets/assignments

**User Role:** Scan Manager \[40] user role

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Tenable Vulnerability Management Adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the Select Adapter Connection drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Tenable Vulnerability Management](/docs/tenableio) adapter connection.
  </Callout>

* **Action type** - Select the action type:
  * **Add** *(default)* - Select to add tags. The **Category Name** field is required when adding tags. It can be found in the **Additional Fields** section.
  * **Remove** - Select to remove tags.

* **Tags Names** - Specify a comma-separated list of Tags to be add/removed to or from Tenable Vulnerability Management assets. Enter only the *value* part of each *key:value* tag.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

***

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Tenable Vulnerability Management domain** *(optional, default: empty)* - The IP address or hostname of your Tenable Vulnerability Management management server.

  * **Access API key** and **Secret API key** - These values must be created in the Tenable Vulnerability Management console. To generate an API key in the Tenable Vulnerability Management console, see [Tenable Vulnerability Management - Generate an API Key](https://docs.tenable.com/cloud/Content/Settings/GenerateAPIKey.htm).

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Create new tags if they do not exist** - Select to create new tags that do not already exist in Tenable Vulnerability Management. If not selected, tags that do not exist in Tenable Vulnerability Management will not be created and will not be added to the assets.
* **Category Name** *(optional)* - Add a Tenable Vulnerability Management category name.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).