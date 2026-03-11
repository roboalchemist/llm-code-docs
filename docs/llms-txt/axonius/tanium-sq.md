# Source: https://docs.axonius.com/docs/tanium-sq.md

# Tanium Interact

The Tanium Interact adapter lets you ask questions to gather live endpoint data in order to create an up-to-date inventory of hardware and software assets.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Aggregated Security Findings, Software, SaaS Applications

## Parameters

1. **Hostname or IP Address** *(required)* - The Hostname or IP address of the Tanium server that Axonius can communicate with via the [Required Ports](#required-ports). This adapter supports both on-premise and Tanium Cloud instances. When connecting to a Tanium Cloud instance, "**-api**" must be added to the end of the subdomain of your Tanium Cloud instance. For example: "*domain.cloud.tanium.com*" should be entered as "*domain-api.cloud.tanium.com*".
2. **User Name or API Token ID** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets. If an API token is being used for authentication, this must be the ID of the API token. The Token ID column in Tanium may be hidden.
3. **Password or API Token** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets. If an API token is being used for authentication, this must be the API token string.

<Callout icon="📘" theme="info">
  More information on API Tokens

  * When connecting to a Tanium Cloud instance, an API token **must** be used.
  * When creating an API token in Tanium, the default value for "Expire in Days" is 7. It is recommended to set this value to the maximum allowed value of 365.
  * Please see the Tanium Documention on [Managing API tokens](https://www.tanium.com/blog/getting-data-out-of-tanium-with-the-api-gateway-and-graphql/) for more information.
</Callout>

5. **Names of Saved Questions to fetch (comma separated)** *(required)* - A comma separated list of Saved Questions names that meet the [Requirements for Saved Question](#requirements-for-saved-questions).

6. **Re-ask every fetch** - When fetching data for a connection, ask Tanium to issue a new question to get the current results for each value supplied to **Names of Saved Questions to fetch (comma separated)**.

7. **Re-ask if results are older than N hours** *(optional, default: 24)* - When fetching data for a connection, if the results for each value supplied to **Names of Saved Questions to fetch (comma separated)** are older than this many hours, ask Tanium to issue a new question to get the current results.
   * If the value provided is 0, no age check is performed and a new question will not be issued based on the value supplied here.

8. **Re-asking waits until all answers are returned** - When re-asking a question for a Saved Question, only consider all answers in when the question expires.
   * If enabled, if a new question is issued for a Saved Question, wait until the question expires (10 minutes) before fetching assets.
   * If disabled, if a new question is issued for a Saved Question, wait until all clients have answers (up until the question expires) before fetching assets.

9. **Use Server Side Export** - Utilize Tanium's Server Side Export to export all of the data on the Tanium platform into one XML file instead of paging through the data utilizing the Tanium REST API.

10. **Parse Dynamic Fields** *(optional, default: true)* - Enable/disable the creation of adapter specific dynamic fields being created for every sensor included in the supplied Saved Questions.
    * If enabled, adapter specific dynamic fields will be created for every sensor included in the supplied Saved Questions.
    * If disabled, adapter specific dynamic fields will NOT be created for every sensor included in the supplied Saved Questions. Only the fields that are listed in [Aggregated Fields](#aggregated-fields) will be processed.

11. **Parse Advanced View** *(optional, default: true)* - Enable/disable the processing of raw data from Tanium into the Advanced View of each asset.

12. **Get hostname from "Short Hostname" instead of "Computer Name"** - Select this option to parse the hostname with the local name of the machine.

13. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

14. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="tanium_interact_add_connection_dialog.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/tanium_interact_add_connection_dialog.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Number of assets to fetch per page** *(optional, default: 1000)* - Control the number of assets that are fetched per page.
2. **Number of seconds to wait in between each page fetch** *(optional, default: 2)* - Control the number of seconds to wait in between each page.
3. **Fetch results from all endpoints (including offline endpoints)** - Select this option to include the most recent results for all endpoints, including the most recent results for offline endpoints.
4. **Max processes for parallel parsing** *(optional, default: 10)* - Control the maximum number of processes launched for parallel parsing of data received from Tanium.
5. **Dynamic fields to be converted to vulnerabilities** - Enter a comma separated lists of columns in Tanium containing CVE IDs. These will be displayed in the Aggregated Security Findings module.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Requirements for Saved Questions

Each value supplied  in [Names of Saved Questions to fetch (comma separated](#parameters) must include the following sensors:

* **Computer ID**
* **Computer Name**
* **Network Adapters** *or*  (**IPv4 Address** *and* **MAC Address**)
* **Computer Serial Number**

<Callout icon="📘" theme="info">
  Additional Information

  The **Network Adapters** sensor is only available if you have purchased and installed the Tanium Discover module.

  You can provide both the **IPv4 Address** and **MAC Address** sensors if you do not have the **Network Adapters** sensor available.

  While these two sensors are available in the Base content provided with the Tanium platform, they do not provide a mapping of which IP address maps to which MAC address, so the information provided by these two sensors will not be as accurate as the **Network Adapters** sensor.
</Callout>

<Callout icon="💡" theme="warn">
  RBAC Errors

  If the user supplied in **User Name** is a limited privilege user and one of the Saved Questions supplied in **Names of Saved Questions to fetch** is open for editing in the Tanium Interact console, the Tanium Interact adapter will be unable to fetch assets for that Saved Question.

  When a Saved Question is open for editing in the Tanium Interact console it repeatedly re-asks the question to populate the "Preview" portion of the Edit page. The question that is asked is only accessible to Administrators and the user who has the Saved Question open for editing.
</Callout>

## Required Ports

Axonius must be able to communicate with the value supplied in [Hostname or IP Address](#parameters) via the following ports:

* **TCP port 443**: REST API

## Required Permissions

Tanium Cloud requires the "Token-Use" permission assigned to the persona.

### For Tanium 7.5

* [Required Module Permissions](#required-module-permissions)
* [Required Advanced Permissions](#required-advanced-permissions)
* [Required Computer Group Permissions](#required-computer-group-permissions)

### For Tanium 7.4

* [Required Module Permissions](#required-module-permissions)
* [Required Advanced Permissions](#required-advanced-permissions)
* [Required Computer Group Permissions](#required-computer-group-permissions)

## Required Module Permissions

A Module Role named **Interact Read-Only User** exists that provides these Module Permissions:

1. Show Interact
2. Interact Module Read

## Required Advanced Permissions

You must [Create an Advanced Role](#create-an-advanced-role) since none exists that grants these Advanced Permissions:

1. Ask Dynamic Questions
2. Read Sensor - with content sets granted for the assigned content sets of the sensors being used in each value supplied in [Names of Saved Questions to fetch (comma separated](#parameters)
3. Read Saved Question - with content sets granted for the assigned content set of each value in [Names of Saved Questions to fetch (comma separated](#parameters)

## Required Computer Group Permissions

Access must be granted to the Computer Groups targeted by each value supplied in [Names of Saved Questions to fetch (comma separated](#parameters).

## Create an Advanced Role

These are the steps to create a role that grants the [Required Advanced Permissions](#required-advanced-permissions):

1. Log in to the value supplied in [Hostname or IP Address](#parameters) with an account that has the permissions necessary to edit roles.
2. In the navigation menu:
   1. Go to the **Permissions** `>` **Roles** page.
3. In the **Permissions Page**:
   1. Click **New Role**.
   2. Select **Grant Advanced Role**.
4. In the **Create Role** page in the **Role Details** section:
   1. Fill in the **Name** field. *(for example: Saved Questions Read Only)*
5. In the **Create Role** page in the **All Content Sets Option** section:
   1. Click the checkbox for **Add all Content Sets that exist or will exist to the permissions selected below**.
   2. Alternatively, you can add specific content sets that allow access to each value supplied in [Names of Saved Questions to fetch (comma separated](#parameters) and the sensors defined in those Saved Questions.
6. In the **Create Role** page in the **Ask Dynamic Question** section:
   1. Click the plus sign next to **Ask Dynamic Questions**.
7. The top of the **Create Role** page should look like:

<Image align="center" alt="tanium_create_advanced_role_top" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/tanium_create_advanced_role_top.png" />

8. In the **Create Role** page In the **Advanced Permissions** section click the plus sign next to the following permissions:
   1. Read Sensor
   2. Read Saved Question
9. The bottom of the **Create Role** Page should look like:

   <Image align="center" alt="tanium_create_advanced_role_bottom" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/tanium_create_advanced_role_bottom.png" />
10. At the bottom of the **Create Role** page:
    1. Click  **Save**.
11. In the **Notice** dialog window:
    1. Click **Continue**.

## Assigning Required Permissions

These are the steps to assign the [Required Permissions](#required-permissions) to the value supplied in [User Name](#parameters):

1. Log in to the value supplied in [Hostname or IP Address](#parameters) with an account that has the permissions necessary to edit users.
2. In the navigation menu:
   1. Go to the **Administration** `>` **Users** page.
3. In the **Users** Page:
   1. Select the value supplied in [User Name](#parameters) from the list of users.
   2. Click **View User**.
4. In the **User Administration** page in the **Computer Groups** section:
   1. Click **Manage Computer Groups**:
5. In the **Assign Computer Groups** page in the **Manage Computer Groups** section:
   1. Section click **Edit**.
6. In the **Edit Computer Group Assignments** dialog window:
   1. De-select the **No Computers** value .
   2. Select the **All Computers** value.
   3. Alternatively, you can select specific Computer Groups targeted by each value supplied in [Names of Saved Questions to fetch (comma separated](#parameters).
   4. Click **Save**.
7. At the bottom of the **Assign Computer Groups** page:
   1. Click **Show Preview to Continue**.
8. At the bottom of the **Assign Computer Groups** page:
   1. Click **Save**.
9. In the **User Administration** page in the **Roles and Effective Permissions** section:
   1. Click **Edit Roles**.
10. In the **Assign Roles** page in the **Role Management** `>` **Grant Roles** section:
    1. Click **Edit**:
11. In the **Edit Grant Roles** dialog window:
    1. Select the role created in [Create Advanced Role](#create-advanced-role).
    2. Select the role named **Interact Read-Only User**.
    3. Click **Save**.
12. At the bottom of the **Assign Roles** page:
    1. Click **Show Preview to Continue**.
13. At the bottom of the **Assign Roles** page:
    1. Click **Save**.
14. In the **Notice** dialog window:
    1. Click **Continue**.
15. The **User Administration** page should look like this:

<Image align="center" alt="tanium_useradmin_interact" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/tanium_useradmin_interact.png" />

14. Perform the steps in [Verifying Permissions](#verifying-permissions)

## Verifying Permissions

1. Log in to the value supplied in [Hostname or IP Address](#parameters) with the values supplied in [User Name and Password](#parameters).
2. In the navigation menu:
   1. Go to the **Content** `>` **Saved Questions** page.
3. In the **Content** `>` **Saved Questions** page:
   1. For each of the values supplied in [Names of Saved Questions to fetch (comma separated](#parameters):
      1. Select the value from the list of Saved Questions.
      2. Click **Load**.

## Creating a Saved Question

1. Log in to the value supplied in [Hostname or IP Address](#parameters) using an account that has the privileges necessary to create Saved Questions.
2. In the **Home** page:
   1. Fill in the **Ask a Question** field with the question that you want to create as a Saved Question in.[You can find example questions here](#example-questions).
   2. Click **Search**.
   3. Select the query that matches the question you want to ask.
3. In the **Question Results** page:
   1. Click **Save this question**
4. In the **New Saved Question** page in the **Details** section:
   1. Fill in the **Name** field. This value will be one of the values that you enter into [Names of Saved Questions to fetch (comma separated)](#parameters).
5. In the **New Saved Question** page in the **Preferences & Tags** section:
   1. *Filling in this section is optional! Instead of filling in this section, you can use the [Re-ask connection parameters](#parameters) to control the recurrence.*
   2. Select **Reissue this question every**.
   3. Enter the recurrence values you want.
6. At the bottom of the **New Saved Question** page:
   1. Click **Create Saved Question**.

## Example Questions

1. Includes just the sensors in the [Requirements for Saved Questions](#requirements-for-saved-questions):
   * **Get Computer ID and Computer Name and Network Adapters and Computer Serial Number from all machines**
2. Includes just the sensors in the [Requirements for Saved Questions](#requirements-for-saved-questions) and targets a specific group of computers instead of all machines:
   * **Get Computer ID and Computer Name and Network Adapters and Computer Serial Number from all machines with Operating System contains Windows**
3. Includes the sensors in the [Requirements for Saved Questions](#requirements-for-saved-questions) and includes sensors that are not defined in [Field Mappings](#field-mappings) but will have Adapter Specific fields dynamically created for their results:
   * **Get Computer ID and Computer Name and Network Adapters and Computer Serial Number and USB Device Details and CPU by Process from all machines**
4. Includes the sensors in the [Requirements for Saved Questions](#requirements-for-saved-questions) and includes all of the sensors in [Field Mappings](#field-mappings) that will map to Aggregated fields in Axonius:
   * **Get Computer ID and Computer Name and Network Adapters and Computer Serial Number and AD Organizational Unit and Applicable Patches and BIOS Version and Chassis Type and CPU Details and Custom Tags and Domain Member and Installed Applications and Is Virtual and Last Logged In User and Manufacturer and Model and Motherboard Manufacturer and Motherboard Version and Open Ports and Open Share Details and Operating System Build Number and Operating System Install Date and Operating System and OS Platform and RAM and Running Processes and Service Details and Service Pack and Tanium Client Version and Time Zone and Total Memory and Uptime from all machines**:

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axoniuscom) if you have a version that is not listed and it is not functioning as expected.

| Version                               | Supported | Notes                                                                      |
| ------------------------------------- | --------- | -------------------------------------------------------------------------- |
| Tanium versions prior to 7.3.314.3424 | No        | This adapter utilizes the REST API, which was added in Tanium 7.3.314.3424 |
| Tanium 7.3.314.3424                   | Yes       |                                                                            |
| Tanium 7.3.314.3668                   | Yes       |                                                                            |
| Tanium 7.3.314.4147                   | Yes       |                                                                            |
| Tanium 7.3.314.4250                   | Yes       |                                                                            |
| Tanium Cloud                          | Yes       |                                                                            |

### Interact Module Versions

Modules within Tanium have their own version which is separate from the platform version.

| Version                    | Supported | Notes |
| -------------------------- | --------- | ----- |
| Interact Module 2.0.3.0012 | Yes       |       |