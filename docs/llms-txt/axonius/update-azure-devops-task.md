# Source: https://docs.axonius.com/docs/update-azure-devops-task.md

# Microsoft Azure DevOps - Update Task

**Microsoft Azure DevOps - Update Task** updates a task status for:

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

* **Use stored credentials from the Azure DevOps adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Azure DevOps](/docs/azure-devops) adapter connection.
</Callout>

* **Project** - Enter the project name.
* **Work item ID** - Enter the ID of the work item to update.
* **Work item new status** - Enter the updated status of the work item.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  **General parameters:**

  * **Domain or IP**  - The hostname or IP address of the Azure DevOps server. The default is [https://vssps.dev.azure.com/](https://vssps.dev.azure.com/).

  * **Port**   - If not supplied, Axonius will use TCP port 443.

  * **API Version** - Select the API version. The default is 6.1-preview\.1.

  * **Organization**  - The name of the Azure DevOps organization. For more derails, see [Azure DevOps - About organization management in Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/organization-management?view=azure-devops).

  **Fields required when authenticating with a personal access token:**

  * **Token Name** and **Personal Access Token** - The generated personal access token (PAT) used to authenticate into Azure DevOps that has the [required permissions](#required-permissions) to read, write and manage work items.

  **Fields required when authenticating with a service principal:**

  * **Azure Client ID, Azure Client Secret, Azure Tenant ID, Cloud Environment** - See details on the [ Microsoft Entra ID documentation](/docs/microsoft-azure-active-directory-ad#create-an-application-key).

  **Additional parameters:**

  * **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the Azure DevOps server via the value supplied in **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

## APIs

Axonius uses the [Azure DevOps - Work Items - Update API](https://learn.microsoft.com/en-us/rest/api/azure/devops/wit/work-items/update?view=azure-devops-rest-7.1\&tabs=HTTP).

## Required Permissions

* The values supplied in [Token Name and Personal Access Token](/docs/azure-devops#authenticating-with-a-personal-access-token) refer to a generated personal access token (PAT) used to authenticate into Azure DevOps that has permission to read, write and manage work items. For details, see [ Azure DevOps - Create a personal access token (PAT)](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops\&tabs=preview-page#create-a-pat).
* The values supplied in [Azure Client ID, Azure Client Secret, Azure Tenant ID and Cloud Environment](/docs/azure-devops#authenticating-with-a-service-principal) must have permission to read, write and manage work items. For details, see [Add a service principal to an Azure DevOps organization](https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/service-principal-managed-identity?view=azure-devops).

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).