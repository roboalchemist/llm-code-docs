# Source: https://docs.axonius.com/docs/defender-atp-tag-assets.md

# Microsoft Defender ATP - Add or Remove Tag to/from Assets

**Microsoft Defender ATP - Add or Remove Tag to/from Assets** adds or removes tags to or from assets in Microsoft Defender ATP for:

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

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from Microsoft Defender for Endpoint (Microsoft Defender ATP) adapter** - Select this option to use the first connected Microsoft Defender for Endpoint adapter credentials.

  * When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Microsoft Defender for Endpoint](/docs/microsoft-defender-atp) adapter connection.
  </Callout>

* **Tag Names** - The name of the tags to add or remove. You can enter multiple tags separated by commas.

* **Action** - Select whether to **Add** or **Remove** the tag.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Source Host Name** *(default: api.securitycenter.microsoft.com)* - Select the domain field configuration. If you access the Azure US government environment, select **api-gcc.securitycenter.microsoft.us**

  * **Tenant ID** - The Azure Tenant ID.

  * **Client ID** - The Application ID of the Axonius application

  * **Client Secret** - A user created key for the Axonius application.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Use only assets from Defender last fetch** - Enable this to include only assets from the last Defender fetch in the query. This can help avoid potential errors, such as assets with two different machine IDs.

## APIs

Axonius uses the following API and other materials:

* [Add or Remove Machine Tags API](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/add-or-remove-machine-tags?view=o365-worldwide)
* [How to use tagging effectively (Part 3)](https://www.drware.com/how-to-use-tagging-effectively-part-3/).

## Required Permissions

The value supplied in [User name](#parameters) must have write/admin permissions.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).