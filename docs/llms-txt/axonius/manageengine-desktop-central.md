# Source: https://docs.axonius.com/docs/manageengine-desktop-central.md

# ManageEngine Endpoint (Desktop) Central and Patch Manager Plus

ManageEngine Endpoint (Desktop) Central and Patch Manager Plus is a desktop management and mobile device management software for managing desktops in LAN and across WAN and mobile devices from a central location, including automated patch deployment for Windows, macOS and Linux endpoints.

### Asset Types Fetched

* Devices, Aggregated Security Findings, Software, SaaS Applications

## Before You Begin

**Ports**

* TCP port 8020/443

### Connecting the Adapter

**When your license is for Patch Manager Plus**

* Set the domain to [https://patch.manageengine.com](https://patch.manageengine.com)
* Set the port to 443

Note that the inventory is not fetched in this case.

**Authentication Method**

* OAuth Client ID / OAuth Client Secret / OAuth Refresh Token for Cloud
* User Name/Password for on-prem

### APIs

Axonius uses the [ManageEngine Desktop Central REST API](https://www.manageengine.com/products/desktop-central/api/).

### Configuring OAuth Authentication and Authorization

This adapter supports OAuth Authentication to connect to the Cloud Instance.

#### Generating the **OAuth Client ID**,  **OAuth Client Secret**  and  **OAuth Refresh Token**

To use OAuth Authentication you need to generate the **OAuth Client ID**,  **OAuth Client Secret**  and  **OAuth Refresh Token**. To generate them:

1. Go to the Zoho API Console:[https://api-console.zoho.com/](https://api-console.zoho.com/)
2. Click 'Add client', choose 'Self Client' and click 'Create' (if a pop-up asks you to confirm, click “OK“).
3. On the API Console main page, click on the 'Self Client' application
4. In the tab 'Generate Code', enter the following details, and click 'Create':
   * **Scope**:
   * **Desktop/Endpoint Central Scopes**   "DesktopCentralCloud.Common.READ,DesktopCentralCloud.SOM.READ,DesktopCentralCloud.Inventory.READ,DesktopCentralCloud.PatchMgmt.READ,DesktopCentralCloud.restapi.READ,DesktopCentralCloud.SOM.UPDATE,DesktopCentralCloud.Inventory.UPDATE,DesktopCentralCloud.PatchMgmt.UPDATE,DesktopCentralCloud.VulnerabilityMgmt.READ"
   * **Patch Manager Plus Scopes**
   * "PatchManagerPlusCloud.Common.READ,PatchManagerPlusCloud.PatchMgmt.READ,PatchManagerPlusCloud.SOM.READ,PatchManagerPlusCloud.restapi.READ,PatchManagerPlusCloud.PatchMgmt.UPDATE,PatchManagerPlusCloud.SOM.UPDATE"

* Time Duration: “10 minutes”

* Scope Description: free text (could be anything)

5. A pop-up “Generated Code“  opens, click copy, and paste the code in a temporary file.

6. In the tab “Client Secret“, copy “Client ID“ and “Client Secret“ to a temporary file.

7. Enter the values you’ve copied to the following command:

```
curl -X POST "https://accounts.zoho.com/oauth/v2/token?grant_type=authorization_code&redirect_uri=http://localhost/callback&code=&client_id=&client_secret="
```

8. Execute the command on a Linux machine (or Windows with curl)
9. From the response of the command, copy the value of “refresh\_token“ (might start with “1000.“), and save it to a temporary file.

#### Using OAuth Authentication

* In Axonius, add a new connection in the ManageEngine Desktop Central/Patch Manager adapter, and fill the following details:
  * Domain - the domain of Desktop Central/Patch Manager (for cloud - use desktopcentral.manageengine.com).
  * Port - the port of the domain (for cloud - 443)
  * OAuth Client ID, OAuth Client Secret, OAuth Refresh Token - the values you copied to a temporary file
  * OAuth Zoho Accounts URL - The relevant url for your Zoho account, from [Refresh Access Tokens - APIs ](https://www.zoho.com/crm/developer/docs/api/v2/refresh.html)

Axonius will now fetch devices from Desktop Central/Patch Manager using OAuth.

### Authentication and Authorization for On-Prem Instances

You need to generate a password and then add permissions:

**To generate a password:**

1. From Desktop Central's web console, navigate to Admin -> API Explorer.
2. On the left pane, click Authentication -> Login.
3. Choose the authentication type as either Local authentication or AD authentication and furnish the user name and password.
4. Upon execution, you will obtain a password along with the auth token.

Use that password in the [Password](#required-parameters) field.
If you have selected the AD authentication, specify the domain in the [User Name Domain](#parameters) field.

**Editing Permissions**
To edit permissions for an existing role in ManageEngine Endpoint Central On-prem,  follow the steps given below:

1. Log in to the ManageEngine Endpoint Central On-prem console using your admin credentials.
2. Click on the “Admin” tab and select “Roles” from the left-hand side menu.
3. Locate the role you want to edit from the list of roles, and click on the role name to open the role details page.
4. On the role details page, you will see a list of permissions assigned to that role. To edit the permissions, click on the “Edit” button located at the top right corner of the page.
5. In the “Edit Role” page, you can add or remove permissions by selecting or deselecting the checkboxes for each permission.
6. To grant permissions for REST API, click on the “API Access” tab and select the appropriate REST API methods you want to allow for this role.
7. Grant the following permissions: SOM, Report, Inventory, Software Deployment, Patch Management.
8. Once you have made the necessary changes, click **Update** to save the updated role.

#### Supported From Version

Supported from Axonius version 4.4

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Domain** - The hostname or IP address of the ManageEngine Endpoint Central or Patch Manager server.
   For cloud Endpoint/Desktop Central use: `desktopcentral.manageengine.com`
   For cloud Patch Manager Plus use: `patch.manageengine.com`
2. **Port** *(default: 8020)* - The port Axonius will use to communicate with the server (for cloud use 443).
3. **User Name** and **Password** - The credentials for a user account that has permissions to fetch assets. For details, see [Authentication and Authorization for On-Prem Instances](#Authentication-and-Authorization-for-On-Prem-Instances).

<Callout icon="📘" theme="info">
  Note

  When **OAuth Client ID**,  **OAuth Client Secret**  and  **OAuth Refresh Token** are not supplied, **User Name** and **Password** are required.
</Callout>

4. **User Name Domain** *(optional)* - The AD domain. Use this option if you are using the AD authentication method.
5. **OAuth Client ID**,  **OAuth Client Secret**,  and  **OAuth Refresh Token** - The parameters for OAuth authentication, used in the cloud version of ManageEngine Endpoint Central and Patch Manager Plus. Refer to [APIs](#apis) for information on how to generate them.
6. **OAuth Zoho Accounts URL** *(default: `https://accounts.zoho.com`)* - The account URL for your Zoho account. Refer to [Refresh Access Tokens](https://www.zoho.com/crm/developer/docs/api/v2/refresh.html) for information on how to obtain the account URL.

<Callout icon="📘" theme="info">
  Note

  When **User Name** and **Password** are not supplied, **OAuth Client ID**,  **OAuth Client Secret**,  and  **OAuth Refresh Token** are required.
</Callout>

![ManageEngine Endpoint (Desktop) Central and Patch Manager Plus](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ManageEngine%20Endpoint%20\(Desktop\)%20Central%20and%20Patch%20Manager%20Plus.png)

### Optional Parameters

1. **Domain Authorization Token** - Token to access the AD domain.
2. **Fetch Desktop Central Data** *(default: enabled)* - Select this parameter to fetch desktop central data. If you do not select this option, only patch data is fetched (patch data is available from both products).
3. **MFA QR Code** *(optional)* - If MFA is enabled using Google Authenticator, save the QR code received as a PNG file and upload it.
   * If supplied, the connection for this adapter will use the uploaded file to authenticate the specified **User Name** and **Password**.
   * If not supplied, the connection for this adapter will not add any additional authentication to the specified **User Name** and **Password**.
4. **MSP Customer ID** - Customer ID to fetch information for, when connecting to Endpoint Central MSP.  Only use this when connecting to Endpoint Central MSP, otherwise leave empty.
5. **API Version** - Select the API version, either 1.3 or 1.4 (Beta).
6. **DC Instance** - The ID used to add to the headers for the API calls, if specified.
7. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
8. **HTTP Proxy** and **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Calculate with binary (ie. 1024 vs 1000)** - Select this option to obtain the total physical memory by dividing the computer hardware memory by 1024 instead of dividing by 1000.
2. **Fetch custom fields (only for on-prem)** - Select this option to fetch all Desktop Central fields that are considered custom fields. Relevant to on-prem customer only.
3. **Enrich device with vulnerability data** - Select this option to enrich the device with vulnerability data. The DesktopCentralCloud.VulnerabilityMgmt.READ scope is required for this.
4. **Enrich devices with data about high risk installed software** - Select this option to fetch high risk installed software data from the Desktop Central API endpoint: `/dcapi/patch/reports/highRiskSoftwareDetailedView`. This data includes End of Life (EOL) software data.
5. **Fetch only vulnerabilities with expanded data from threats/vulnerabilities list** - Select this option to fetch extended vulnerabilities information from the `threats/vulnerabilities` endpoint, validate them and return only the device's vulnerabilities that exists in this endpoint  - thus skipping vulnerabilities without extended information. If you disable this option, all the device's vulnerabilities will be populated.
6. **Seconds to sleep between requests (per endpoint)** *(default: System Report, Installed Software, Vulnerabilities)* - Select an endpoint to apply the sleep seconds configuration. To add more endpoints, click the + icon. To remove endpoints, click the x icon.
   * **Seconds to sleep** - Set the number of seconds to sleep between system reports and software requests. This is useful in cases where the server is not sending 429 responses, but is still rate-limiting the client.
7. **Assets per page** - Set the number of assets to manage per page. The default amount is 200.
8. **Fetch installed software** *(default: enabled)*- By default, Axonius fetches device software from `inventory/installedsoftware`. Clear this option to not fetch device software.
9. **Fetch system reports** - Select this option to fetch device patch data from `patch/systemreport`.
10. **Fetch inventory computer scan details** - Select this option to fetch data from `/inventory/scancomputers` endpoint.
11. **Enrich Assets Raw Data from query reports** - This section allows you to enrich asset raw data by scanning system reports for specific query reports. Data from the first matched query report found will be used for this enrichment.

    To configure a report for scanning, click **+ Add Query Report Enrichment**.
    For each query report you add, provide the following information:

    1. **Query Report Name** - The name of the query report to scan for.
    2. **Report JSON key to match the Asset JSON data** *(optional)* - Enter a JSON key from the report's data. This key will be matched against the asset JSON key.
    3. **Asset JSON key to match the Report JSON data** - Enter a JSON key from the asset's raw data. This key will be matched against the report JSON key.
12. **Fetch custom groups** - Select to fetch custom groups data from the customgroup endpoint.
13. **Custom Parsing** - See [Adapter Custom Parsing](/docs/adapter-custom-parsing) for more information.
14. **Include Only Devices with Last Seen value**  - Select whether to only fetch devices that have a last seen value. Devices that do not have a value for last seen are not fetched.
15. **Only fetch devices from the following types** - Enter a comma separated list of configured device\_type values. Devices will only be fetched if they have the device\_type values listed.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Related Enforcement Actions

* [ManageEngine Endpoint (Desktop) Central and Patch Manager Plus - Create Patch Action](https://docs.axonius.com/docs/desktop-central-create-patch-action)
* [ManageEngine Endpoint (Desktop) Central and Patch Manager Plus - Create Software Action](/docs/desktop-central-create-software-action)
* [ManageEngine Endpoint (Desktop) Central and Patch Manager Plus - Create Software Action per Asset](https://docs.axonius.com/axonius-help-docs/docs/desktop-central-create-software-action-per-asset)

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                                  | Supported | Notes |
| ---------------------------------------- | --------- | ----- |
| ManageEngine Desktop Central 10.1.2121.1 | Yes       |       |