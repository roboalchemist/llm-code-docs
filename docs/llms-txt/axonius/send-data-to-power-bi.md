# Source: https://docs.axonius.com/docs/send-data-to-power-bi.md

# Microsoft Azure - Send Assets to Microsoft Power BI

**Microsoft Azure - Send Assets to Microsoft Power BI** (Send Data to Microsoft Power BI) inserts the assets returned by the selected query or assets selected on the relevant asset page into the Microsoft Power BI table.

When used with a query, only the fields configured in the query are inserted to the table.

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

* **Authentication Method** - Select the authentication method to use and fill out the fields for the selected method.
  * Application Authentication
  * Username and Password
  * OAuth and Redirect URI

* **Azure Client ID** - The Application ID of the Axonius application, as detailed in the Required Permissions section.

* **Azure Client Secret**  - A user created key for the Axonius application, as detailed in the Required Permissions section.

* **Azure Tenant ID** -  Microsoft Azure Active Directory ID.

* **Microsoft Username** and **Microsoft Password** - Microsoft Account credentials.

* **OAuth Code** - The authorization code to connect to Microsoft Intune. For more information see Generate the OAuth Authorization Code.

* **OAuth Redirect URI** - The location where the authorization server sends the user once the Azure has been successfully authorized and granted an authorization code or an access token. See [Microsoft Power BI](/docs/power-bi) for more information.

* **Workspace ID** - Workspace ID in PowerBI. You can copy the Workspace ID  from the URL of a report or dashboard when viewed from within Power BI.

* **Semantic Model Name** *(default: AxoniusSemanticModel)* - the Semantic Model (previously Dataset) name in Power BI. In Power BI, select a workspace and then select the required Semantic Model:

<Image alt="SelectWorkspace" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-1DOXBSTQ.png" />

<Image alt="SelectSemanticModel" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-IDZCKLPR.png" />

* **Table Name** *(default: AxoniusTable)* - the table name in Power BI.

<Image alt="SelectTable" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-67SPCU55.png" />

<Callout icon="📘" theme="info">
  Notes

  * If no Semantic Model or table exist in Power BI, the Enforcement Action will created new ones according to the names entered.

  * When a change is made to a table, the table is recreated with the new data (if any). Power BI does not have an *Update Table* function.
</Callout>

* **API Type** *(default: Commercial)*  - Select the API type. When a government entity is selected, sends the data to *app.powerbigov.us* for government use instead of *app.powerbi.com*.

## Additional Fields

These fields are optional.

* **Include Fields from Saved Query** - If enabled, the fields specified in the saved query will be sent to Power BI.
* **Split by field values** - Splits the field values by the selected adapter and field.
* **Create record for each** *(default: N/A)* - Select the type of assets for which records will be created: *N/A*, *Security Findings*, *Installed Software*.
* **Map Axonius fields to Power BI fields** - Use the **Field Mapping Wizard** to map Axonius fields to fields in Power BI. In this way you can transfer data found in Axonius into Power BI. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  NOTE

  For details, see [Axonius to External Field Mapping](/docs/axonius-to-cmdb-field-mapping).
</Callout>

* **Verify URL** - Verify the SSL certificate offered by Power BI. For more details, see [SSL Trust & CA Settings](../global-settings#ssl-trust-amp-ca-settings).
* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

## APIs

Axonius uses the [Microsoft Power BI Rest API Push Dataset](https://docs.microsoft.com/en-us/rest/api/power-bi/pushdatasets).

## Required Permissions

### Preferred Methodology for Creating Permissions

1. Create an application in the Microsoft Azure Portal. For details, see [Creating an application in the Microsoft Azure Portal](/docs/microsoft-azure#creating-an-application-in-the-microsoft-azure-portal).

2. This application  requires the **Power BI Service → Tenant.ReadWrite.All Application** access.

<Callout icon="📘" theme="info">
  Note

  If you already have an Azure client  configured for the Azure adapter, you can add this permission to the existing application.
</Callout>

<Image alt="PowerBIPermission1" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PowerBIPermission1.png" />

3. In Power BI, Go to **Settings → Admin portal → Tenant Settings → Developer settings → Enable Allow** service principals to use Power BI APIs.

4. Either apply this change to the entire organization or include a specific security group and include your new Service Principal (the application we just created) into the group. In this example, the Service Principal is a member of the axonius-powerbi security group.

   <Image align="center" alt="PowerBIPermission2" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PowerBIPermission2.png" />

5. Within the specific **workspace** → access, include the Service Principal or security group as a **contributor**.

<Image align="center" alt="powerbipermission3" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/powerbipermission3.png" />

6. When using this method, the Tenant ID is required for the Service Principal.

### Creating Permissions Using a Master User

You can also use **Delegated** permissions and a user account to send data to Power BI.

<Callout icon="📘" theme="info">
  Note

  Common Microsoft security practices, such as [Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview), may block this approach.
</Callout>

* To connect with delegated permissions, you must register an Azure AD application with Power BI.
* The application needs to  have **Power BI Service → Dataset.ReadWrite.All** Delegated access.
* When using this method, the **Username** and **Password** of the Master user account is needed.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).