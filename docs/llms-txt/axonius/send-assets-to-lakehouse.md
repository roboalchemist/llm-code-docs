# Source: https://docs.axonius.com/docs/send-assets-to-lakehouse.md

# Microsoft Fabric - Send Assets to Lakehouse

**Microsoft Fabric - Send Assets to Lakehouse** uses Microsoft Fabric to send assets from Axonius to OneLake and from OneLake to Lakehouse for:

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

## Before You Begin

To successfully run the Enforcement Set, follow these steps first. Also refer to [Required Permissions](/docs/send-assets-to-lakehouse#required-permissions).

1. Create a Fabric Capacity in the Azure Portal.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-HJ63JITO.png)

2. Create a Workspace in the Fabric Capacity.

3. Under **Workspace Settings** `>` **License Info**, link it to Fabric capacity license.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-2X2HS1V5.png)

4. Under **Manage Access**, add the name of the app used for the adapter (Microsoft Azure of Entra ID) in Axonius.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-FFQ4SD0T.png)

5. In the Microsoft Fabric Admin Portal, navigate to **Tenant settings** `>` **Developer settings** and enable the following option: **Service principals can use Fabric APIs**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-CNTDSWJ3.png)

6. Define the region of the Fabric Capacity's resource group as one of regions listed in [Fabric region availability](https://learn.microsoft.com/en-us/fabric/admin/region-availability).

7. In the Microsoft Fabric Admin Portal, navigate to **Tenant settings** `>` **OneLake settings** and enable the following option: **Users can access data stored in OneLake with apps external to Fabric**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-4E8B68YB.png)

### Required Permissions

The following permissions are required:

**Power BI Permissions**

* Lakehouse.ReadWrite.All
* OneLake.ReadWrite.All

**OneLake Permissions**

* Storage.ReadWrite.All

<Image alt="Permissions1" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-WIRIPRQT.png" />

<Image alt="Permissions2" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-QA9L2K90.png" />

### Troubleshooting

If you get the following error message:

```
The resource principal named https://onelake.dfs.fabric.microsoft.com was not found in the tenant named <TENANT NAME>. This can happen if the application has not been installed by the administrator of the tenant or consented to by any user in the tenant. You might have sent your authentication request to the wrong tenant.
```

Follow these steps while trying to get the access token:

1. In Azure Portal, go to **Azure AD Enterprise Applications**.
2. Select **All Applications**.
3. In the search box, enter **OneLake**.
4. If OneLake does not appear, it is not registered in your tenant. This might be due to the tenant’s region.
5. If OneLake does appear, create an application with OneLake.

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Azure Client ID**, **Azure Client Secret**, and **Azure Tenant ID** - You can copy these parameters from the app registrations.

* **Workspace ID** - The ID of the Fabric Capacity workspace. The ID can be found in the workspace's URL.

* **Lakehouse ID** - The ID of the Lakehouse that you want to send the data to. The ID can be found in the Lakehouse's URL.

* **Table Name** - The name ot the table to create or overwrite.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the following APIs:
[Tables - Load Table](https://learn.microsoft.com/en-us/rest/api/fabric/lakehouse/tables/load-table?tabs=HTTP)
[Connecting to Microsoft OneLake](https://learn.microsoft.com/en-us/fabric/onelake/onelake-access-api)

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).