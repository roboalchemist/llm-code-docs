# Source: https://docs.axonius.com/docs/workday.md

# Workday

Workday offers software solutions for financial management, human resources, and planning.

### Asset Types Fetched

* Devices, Users, Roles, Application Settings, User Extensions

## Resources Required by Asset Type

The following connection parameters, advanced settings, permissions, and configurations are required to fetch each asset type.

Search by Asset Type to find the resources required for your specific needs.

<Table align={["left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Asset Type
      </th>

      <th>
        [Connection Parameters](/docs/workday#connecting-the-adapter-in-axonius)
      </th>

      <th>
        [Advanced Settings](/docs/workday#advanced-settings)
      </th>

      <th>
        Permissions
      </th>

      <th>
        Additional Configuration
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Devices
      </td>

      <td>
        * Workday Domain
        * Workday Tenant Name
        * User Name/Client ID and Password/Client Secret
        * Custom Report URL
      </td>

      <td>
        No specific setting required
      </td>

      <td>
        Access to the following domains:

        * Worker Data: Workers
        * Worker Data: Public Worker Reports
        * Any other datasets that are used for the custom report. You need to configure these in the Workday portal
      </td>

      <td>
        [Finding the Workday Domain](/docs/workday#finding-the-workday-domain)
      </td>
    </tr>

    <tr>
      <td>
        Users, Roles
      </td>

      <td>
        * Workday Domain
        * Workday Tenant Name
        * User Name/Client ID and Password/Client Secret
      </td>

      <td>
        No specific setting required
      </td>

      <td>
        Access to the following domains:

        * Self-Service: Current Staffing Information
        * Worker Data: Current Staffing Information
        * Worker Data: Workers
        * Worker Data: Public Worker Reports
      </td>

      <td>
        [Finding the Workday Domain](/docs/workday#finding-the-workday-domain)
        [Creating an Integration System User](/docs/workday#creating-an-integration-system-user)
      </td>
    </tr>

    <tr>
      <td>
        User Extensions
      </td>

      <td>
        * Workday Domain
        * Workday Tenant Name
        * User Name/Client ID and Password/Client Secret
      </td>

      <td>
        Fetch integration system users
      </td>

      <td>
        Access to the following domain:

        * Integrations: System Users
      </td>

      <td>
        [Finding the Workday Domain](/docs/workday#finding-the-workday-domain)
        [Creating an Integration System User](/docs/workday#creating-an-integration-system-user)
      </td>
    </tr>

    <tr>
      <td>
        Application Settings
      </td>

      <td>
        * Tenant Login URL
        * Read Only Admin Username and Read Only Admin Password
        * 2FA Secret Key (if your organization requires setting 2-factor authentication)
      </td>

      <td>
        Fetch Application Setting
      </td>

      <td>
        * The user must belong to security domains that allow access to the Workday UI through their user credentials
        * View only access to the following Workday tasks:
          * Tenant Setup/security
          * Password rules
      </td>

      <td>
        [Creating an Integration System User](/docs/workday#creating-an-integration-system-user)
      </td>
    </tr>
  </tbody>
</Table>

### APIs

Axonius uses the Workday Human Resources SOAP API.

## Before You Begin

### Finding the Workday Domain

1. Log into the Workday console.
2. Search for the **Public Web Services** report and open it. ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-KCNXF5UJ.png)
3. Hover over **Human Resources** and click the three dots to access the menu.
4. Navigate to **Web Services** `>` **View WSDL**.
5. On the bottom of the page, find the `location` parameter in the `soapbind:address` tag: ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-YID45H3C.png)
6. Copy the parameter until (and not including)`/ccx`, for example `https://wd5-services1.myworkday.com`
7. Back in Axonius, paste the copied value in the **Workday Domain** connection field.

### Creating an Integration System User

To fetch Users data, you need to create an Integration System User (ISU) with the [required permissions](/docs/workday#resources-required-by-asset-type). To create an ISU, follow the instructions in [How to create an ISU user in Workday](https://workday.my.site.com/CommunityAccess/s/article?no=000019472).

To fetch Application Settings data, create a dedicated workday user account (auditor group read-only).

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters - Users and Devices

1. **Workday Domain** - The hostname of the Workday server. For more information, see [Finding the Workday Domain](/docs/workday#finding-the-workday-domain).
2. **Workday Tenant Name** - The Tenant name as supplied by Workday.
3. **User Name/Client ID** and **Password/Client Secret** - The credentials for a user account that has the [required permissions](/docs/workday#resources-required-by-asset-type) to fetch assets. You can either enter here a user name and a password, **or** a\*\*\*\* Client ID and a Client Secret. Learn how to [get the Client ID and Client Secret](https://doc.workday.com/admin-guide/en-us/authentication-and-security/authentication/oauth/dan1370797831458.html). **If you are using Client ID and Client Secret, provide the following additional parameters:**

   1. **Use OAuth Authentication** - Select to enable OAuth 2 authentication for this adapter connection.
   2. **OAuth Refresh Token** - The token required to access the relevant API endpoints. Once this token expires, it needs to be updated. To get the refresh token, follow the instructions in the [Workday documentation](https://doc.workday.com/admin-guide/en-us/integrations/integration-services/integration-apis/launch-integrations-using-oauth-2-0-bearer-tokens.html).

**Custom Report URL** - Enter a SOAP URL for a Workday Custom Report endpoint. **This parameter is required to fetch Devices, and optional for fetching Users. See**[Optional Parameters](/docs/workday#optional-parameters)**for more details on this parameter.**

#### X.509 Certificate Authentication

You have the option to authenticate with an X.509 Certificate. If you are using this option, provide the **User Name**parameter, as well as the following parameters:

1. **X.509 Private Key** - Upload the private key file (required for X.509 authentication). This key is used only locally to decrypt responses from Workday\*\*.\*\*
2. **X.509 Public Key** - Upload the X.509 certificate file issued by Workday.
3. **X.509 Passphrase** - Enter your passphrase.

### Required Parameters - Application Settings

1. **Tenant Login URL** - Enter the login URL where admins sign in to their working environment.
2. **Read Only Admin Username** and **Read Only Admin Password** - The credentials that are separate from the already existing username and password fields. These are needed in order to fetch application settings.
3. **2FA Secret Key** - The secret generated in the adapter for setting up 2-factor authentication for the adapter user created to fetch Application Settings.

<Image align="center" border={false} width="auto" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-3WPL16UN.png" height="auto" />

### Optional Parameters

1. **Fetch Events Effective X Days Forward** *(default: 30)* - Specify a numerical value to set an effective future date to ensure that information about future hires is accurate. The value can be any integer.

* If a value is specified, this adapter will fetch information relating to future events up to the number of days set in the future.
* If this field is left empty, this adapter will fetch information relating to events up to 30 days in the future.

2. **Custom Report URL** *(required for Devices, optional for Users)* - Enter a SOAP URL for a Workday Custom Report endpoint. To get the URL from the custom report, on your Workday console, navigate to **Related Actions** `>` **Webservices** `>` **URLs to access a list of links**. Click on the CSV link to generate the required URL, copy the URL path from your browser, and paste it into this field in the Adapter Connection page.

   * Do not include the main Workday domain base or the "?wsdl" portion of the URL. For example, if the custom report URL is `https://wd5-services1.myworkday.com/ccx/service/customreport1/example/custom_report?wdsl`, the value you should enter here should just be ccx/service/customreport1/example/custom\_report.
   * The Custom Report must also contain the `Employee_ID` field to match the corresponding worker, or the `Device_ID` field to match the corresponding device.

3. **Custom Report Asset Type** *(default: Users)* - Select whether the custom report applies to Users or Devices.

4. **Fetch Only from the Custom Report** - Select this option to create users only from the custom report data.

<Accordion title="Notes on Users Custom Report" icon="fa-info-circle">
  <Callout icon="📘" theme="info">
    * Each entry should have the following field for uniqueness: `Employee_ID`

    * Each entry should include the following fields for correlation: `mail`, `username`, `first_name`, `last_name`

    * The following fields are parsed as mail: `Work_Email`, `Email`, and `email`

    * When a report includes a complex field, only the contents of the Descriptor field are parsed. For example, `{Location: { Descriptor: "Main street" }}` is parsed as `Location: Main street`.
  </Callout>
</Accordion>

2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

3. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

4. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note:

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Users Chunk Per Page (default: 200)** - Enter the number of users per a single request.
2. **Preferred Email Domain (optional)** - Enter the preferred domain for work email addresses (such as ThisEmailDomain.com) for each user. When the field is empty, Axonius uses the last email address within the list of addresses in the Mail field.
3. **Exclude Specified User Email (optional)** - Enter an email address that you want to exclude from the fetch.
4. **Include Contingent Workers in Fetch** - Select to include contingent workers in the fetch.
5. **Disable Management Chain Enrichment** - Select this option to disable the Management Chain Enrichment process and thus not enrich the management workers list with additional information about each manager.
6. **Fetch only the most recent records for each worker** - Select this option to fetch only the most recent records for each worker.
7. **Fetch integration system users** - Enable to fetch integration system users and their corresponding extensions.
8. **Enrich users with Workday assets** - User assets refer to fetching data from the **Get\_Assets Workday SOAP** service.  These are assets associated with a user. These assets populate an enrichment field called “Assets” on the Workday users. The assets can be almost any business asset that is tracked in Workday, for example, laptops, software licenses, company phones, etc. Workday describes business assets as follows: “In Workday, a business asset is anything you want to track, from tractors to software licenses.” For more information, see [Operation: Get\_Assets](https://community.workday.com/sites/default/files/file-hosting/productionapi/Resource_Management/v43.2/Get_Assets.html).
9. **Fetch workers by organization (optional)** - Select this option to fetch workers filtered by organization to reduce the number of response results. This setting is recommended only for accounts with more than one million worker records. When this option is enabled, the adapter only fetches Active users.
10. **Include Custom Organization Data** - Select this option to fetch custom organization data.
11. **Include Cost Center Organization Data** - Select this option to fetch cost center data under organization data.
12. **Include Organization Support Role Data** - Select this to fetch Organization Support Role Data. Note that this data is heavy and might increase fetch time.
13. **Enable real-time asset updates (Supported events: New hires, New terminations)** - Select this option to trigger an event in a workflow. Enabling the option will both fetch users that have been hired or terminated in the last time interval and will trigger the respective event. All workflows configured with this event are then triggered.
14. **Fetch Application Settings** - Select this option to enable fetch of Application Settings.
15. **Fetch Only Application Settings** - Select this option to fetch **only** Application Settings. No other assets will be fetched.
16. **List of worker custom IDs to fetch** - Add a list of custom IDs, located under `Identification_Data`, to add as dynamic fields in the Users module.
17. **Fetch custom report for each year in time range** - Select this option when the connection configuration uses a Custom Report, which is filtered by the `TermDates` range parameters. If the custom report includes a time range using the `TermDates` range parameters, Axonius will fetch the report for each year in the defined time range until the current year. **Example:** `customreport.url?TermDateStart='2020-01-01'&TermDateEnd='2020-12-31'` If 2025 is considered the current year, the adapter will call the custom report 5 times, one for each year from 2020 until 2025.

<Callout icon="📘" theme="info">
  Note:

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Related Enforcement Actions

[Workday - Activate User](/docs/activate-workday-user)

[Workday - Suspend User](https://docs.axonius.com/axonius-help-docs/docs/suspend-workday-user)

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version     | Supported | Notes |
| ----------- | --------- | ----- |
| 34.0 and up | Yes       | --    |