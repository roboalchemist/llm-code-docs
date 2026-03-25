# Source: https://docs.axonius.com/docs/create-manage-engine-sdp-request-per-entity.md

# ManageEngine ServiceDesk Plus - Create Request per Asset

**ManageEngine ServiceDesk Plus  - Create Request per Asset** creates a ManageEngine ServiceDesk Plus request for each individual asset for:

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

* **Use stored credentials from [ManageEngine ServiceDesk Plus (SDP)](/docs/manageengine-service-desk-plus) adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [ManageEngine ServiceDesk Plus (SDP)](/docs/manageengine-service-desk-plus) adapter connection.
</Callout>

* **Request Title** *(default: Axonius-created Request)* - Enter a name for the request.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** - The hostname or IP address of the Manage Engine ServiceDesk Plus server that Axonius can communicate with.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

  * **Authentication Methods** - Select an Authentication method:

  * **oAuth 2.0** - Use for cloud deployment of ManageEngine ServiceDesk Plus (SDP). These fields are required when oAuth 2.0 is selected:

  * **OAuth Client ID**,  **OAuth Client Secret** and **OAuth Refresh Token** - parameters for OAuth authentication, used in the cloud version of ManageEngine ServiceDesk Plus. Refer to [Configuring OAuth Authentication](/docs/create-manage-engine-sdp-request-per-entity#configuring-oauth-authentication) for information on how to generate them.

  * **OAuth Zoho Accounts URL**   - Select the account URL, or add your own. Refer to [Refresh Access Tokens](https://www.manageengine.com/products/service-desk/sdpod-v3-api/getting-started/data-centers.html) for information on how to obtain the account URL.

  * **Basic Authentication** - When selected, the **Technician key token** field is available. Use for on-prem deployment of ManageEngine ServiceDesk Plus (SDP). An API Key associated with a user account that has the  Required Permissions  to fetch assets.
    To obtain a technician key token, see [Generate a Technician Key Token](/docs/manageengine-service-desk-plus#generate-a-technician-key-token).
</Callout>

* **Requester E-mail** - Enter the email address of the requester.
* **Description** *(default: Axonius-created request)* - Enter a description of the request.
* **Status** - Enter a status.
* **Priority** - Enter a priority.
* **Category** - Enter a category.
* **Additional fields** - Specify additional fields to be added as key/value pairs in a JSON format.\
  For example:

```json
{"field1": "value1", "field2": "value2"}
```

If one of the specified fields is invalid, the request might fail.

* **Append EC metadata to the request description** - When selected, includes information about the Enforcement Action runs in the request description.
* **Send CSV data** - Select to attach a CSV with the asset data to the request.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

**Additional CSV Settings**

* **Split by asset entities**  -  Select to create a CSV file where each asset on a device is shown as a separate row. This separates each asset as the 'expand' option in the application. It separates each asset by its entity. For example, you will be able to know which values were fetched from each adapter connection.

  * If supplied, each value on a device or user is shown as a separate row.
  * If not supplied all values on a device are in the same cell on the CSV file.

* **Export CSV delimiter to use for multi-value fields** *(default:**Export CSV delimiter to use for multi-value fields** field under the **System Settings** section in the **[GUI Settings](/docs/gui-settings#system-settings)**)* - Specify a delimiter to separate between values within the same field of an exported CSV file, otherwise the delimiter defined in **Export CSV delimiter to use for multi-value fields** is used.

* **Maximum rows** *(default: 1048500)* - Specify the maximum number of rows to be included in the CSV file.  When you set a value here the generated CSV file will include the top x rows, based on the specified values. Otherwise, the generated CSV file will include the default maximum rows, set as 1048500.

* **Include associated devices (only for Aggregated Security Findings and Software)** - For Software and Aggregated Security Findings queries. Toggle on this option to include the associated devices with the preferred hostname as a predefined field for each Software or Aggregated Security Finding. When you create a CSV file with associated devices (for Aggregated Security Findings or Software),  if the exported query results are larger than the value set under Maximum rows (or the default value of 1048500), an appropriate notice is displayed at the end of the CSV file.

  * **Device fields** -  This option is available for Software and Aggregated Security Findings. Select the device fields to add. By default Preferred Host Name is selected. Click add to select more fields. At least one field must be selected. Click the bin icon to remove a device field.

## APIs

Axonius uses these APIs:

* [ManageEngine ServiceDesk Plus Cloud API V3 Documentation](https://www.manageengine.com/products/service-desk/sdpod-v3-api/)
* [ManageEngine ServiceDesk Plus](https://demo.servicedeskplus.com/app#/admin/api)

## Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

### Configuring OAuth Authentication

This adapter supports OAuth Authentication

#### Generating the **OAuth Client ID**,  **OAuth Client Secret**  and  **OAuth Refresh Token**

To use OAuth Authentication you need to generate the **OAuth Client ID**,  **OAuth Client Secret**  and  **OAuth Refresh Token**. To generate them:

1. Go to the Zoho API Console: [https://api-console.zoho.com/](https://api-console.zoho.com/)
2. Click 'Add client', choose 'Self Client' and click 'Create' (if a popup asks you to confirm, click “OK“).
3. On the API Console main page, click on the 'Self Client' application
4. In the tab 'Generate Code', enter the following details, and click 'Create':
   * Scope:
     * "SDPOnDemand.assets.READ,SDPOnDemand.requests.CREATE"
     * Time Duration: “10 minutes”
     * Scope Description: free text (could be anything)
5. A popup “Generated Code“  opens, click copy, and paste the code in a temporary file.
6. In the tab “Client Secret“, copy “Client ID“ and “Client Secret“ to a temporary file
7. Enter the values you’ve copied to the following command on a linux machine (or Windows with curl):
   ```
   curl -X POST "https://accounts.zoho.com/oauth/v2/token?grant_type=authorization_code&code=&client_id=&client_secret="
   ```
8. From the response of the command, copy the value of “refresh\_token“, and save it to a temporary file.
9. Copy the OAuth Client ID, OAuth Client Secret, OAuth Refresh Token to the appropriate places in the Configuration dialog.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).