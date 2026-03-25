# Source: https://docs.axonius.com/docs/create-azure-devops-task.md

# Microsoft Azure DevOps - Create Task

**Microsoft Azure DevOps - Create Task** creates a task in Azure DevOps for:

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

* **Split Tickets By** - When enabled, group assets into different tickets based on a shared attribute. Click the adapter icon to select an adapter (or Aggregated), and then click the **Select Adapter Field** box to select the asset field used to generate a separate ticket for each unique value.

  <Callout icon="📘" theme="info">
    Note

    * The **Split Tickets By** option appears only in ticket creation actions, and does not appear in ticket-per-asset creation or ticket update actions.
    * For assets containing multiple values, the system uses only the first value to perform the split.
  </Callout>

<br />

* **Use stored credentials from Azure DevOps adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure an [Azure DevOps](/docs/azure-devops) adapter connection.
</Callout>

* **EC Domain or IP** *(default: `https://dev.azure.com`)* - The hostname or IP address of the Azure DevOps server.

* **Project**  - Enter the project name.

* **Project Process Type** - Select the Project Process Type.

* **Work Item Title**  - Specify the Work item title.

* **Include associated devices (only for Vulnerabilities and Software)** -

* **Work Item Type** *(default: Task)* - Select the work item type to be created. The types available depend on the **Project Process Type** that you choose. You can also add a new **Work Item Type**. Type a value, and select create new. This **Work Item Type** will now be available.

  <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AzureDevopsWorkitem.png" />

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

* **Description** - Enter a description of the new task.

* **Exclude Axonius EC summary description** - Select this option to **not** include the summary description of the Axonius Enforcement Action.

* **Tags** - Custom tags to be added to the new work item. Multiple tags are separated by a semicolon ";".

* **Area Path** - Enter the Area Path. This is used to group work items by team, product or feature area.

* **Iteration Path**  - Enter the Iteration Path. This is used to group the work into sprints, milestones, etc.

* **Story Points** *(default: 1)* - Enter a value.

* **Priority** *(default: 2)* - Task priority from 1 to 4.

* **Target Date (Days, today + X days)** - The target date for the task. Enter the number of days to add to today's date.

* **Risk** - Select a risk value:
  * 1 - High
  * 2 - Medium
  * 3 - Low

* **Custom Fields** - Click `+` to add custom fields. Note that you can also send native Microsoft fields, and not only Axonius custom fields.

  <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CustomFields-Plus.png" />

  Enter a **Field Name** and **Field Value** for each custom field you add.

  <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CustomFields(2).png" />

* **Parent Work Item ID** - Add the Work item with the specified ID as the Parent Work item of the new one.

* **Attach CSV** - Attach a CSV file containing the results of the query.

* **Export CSV delimiter to use for multi-value fields** - In the CSV file that is created set a delimiter to use for fields that can contain more than one value.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Azure DevOps - Work Items - Create API](https://docs.microsoft.com/en-us/rest/api/azure/devops/wit/work%20items/create?view=azure-devops-rest-6.0).

## Required Permissions

* The values supplied in [Token Name and Personal Access Token](/docs/azure-devops#authenticating-with-a-personal-access-token) refer to a generated personal access token (PAT) used to authenticate into Azure DevOps that has permission to read, write and manage work items. For details, see [ Azure DevOps - Create a personal access token (PAT)](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops\&tabs=preview-page#create-a-pat).
* The values supplied in [Azure Client ID, Azure Client Secret, Azure Tenant ID and Cloud Environment](/docs/azure-devops#authenticating-with-a-service-principal) must have permission to read, write and manage work items. For details, see [Add a service principal to an Azure DevOps organization](https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/service-principal-managed-identity?view=azure-devops).

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).