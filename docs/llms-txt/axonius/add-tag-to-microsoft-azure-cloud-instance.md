# Source: https://docs.axonius.com/docs/add-tag-to-microsoft-azure-cloud-instance.md

# Microsoft Azure - Add Tag to Cloud Instance

**Microsoft Azure - Add Tag to Cloud Instance** adds a tag to Microsoft Azure cloud instances for:

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

* **Use stored credentials from the Microsoft Azure Adapter** - Select this option to use the connected Microsoft Azure adapter credentials.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Microsoft Azure](https://docs.axonius.com/docs/microsoft-azure-overview) adapter connection.
</Callout>

* **Tag names** - The tag name to be added to the Microsoft Azure cloud instance.
  * A tag name can have a maximum of 512 characters and is case-insensitive.
  * Tag names cannot have the following prefixes which are reserved for Azure use: 'microsoft', 'azure', 'windows'.
* **Tag values** - The tag value to be added to the Microsoft Azure cloud instance.
  * If the tag already exists on the cloud instances, its value will be overridden with the specified value.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Azure subscription ID** - The Subscription ID access control role in IAM for the Axonius application, as detailed in the [Required Permissions](#required-permissions) section.

  * **Cloud environment** *(default: Azure Public Cloud)* - Select your Azure cloud environment type.

  * **Authentication Method** - Each authentication method requires different connection parameters. See the [Microsoft Azure documentation](https://docs.axonius.com/docs/azure-deploying-the-adapter#required-fields) for explanations on each method and its parameters.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
</Callout>

## APIs

Axonius uses the [Microsoft Azure - Tags - Create Or Update API](https://docs.microsoft.com/en-us/rest/api/resources/tags/createorupdate).

## Required Permissions

To connect to Microsoft Azure, you need to create a designated Axonius application in the Microsoft Azure Portal and grant it read-only permissions. All required credentials will be given once an application is created. For details, see [Creating an application in the Microsoft Azure Portal](/docs/microsoft-azure-and-azure-active-directory-ad#creating-an-application-in-the-microsoft-azure-portal).

Using **Add Tag to Microsoft Azure Cloud Instance** action requires a role similar to "Tag Contributor" (build-in role). At the very least, read access to the relevant resources is required, along with the permission to read and write tags (microsoft.resource.tags).

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).