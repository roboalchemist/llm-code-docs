# Source: https://docs.axonius.com/docs/update-sap-concur-4-user.md

# Update User - SAP Concur 4

**Update User - SAP Concur 4** updates a user in SAP Concur 4.x for:

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

* **Use stored credentials from the SAP Concur 4.x adapter** - Select this option to use the  first connected SAP Concur 4.x adapter credentials.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [SAP Concur 4.x](/docs/sap-concur-4) adapter connection.
</Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** - The host name or IP address of the SAP Concur 4.x server.

  * **Client ID** - The Concur ID used to log in and create the users.

  * **Client Secret** - The Concur secret used to log in and create the users.

  * **Refresh Token** - The token used for company level authentication. In order to retrieve the Refresh Token, send the following code:

    ```
    curl -X POST “https://DOMAIN/oauth2/v0/token” \
         -H “Content-Type: application/x-www-form-urlencoded” \
         -d     “client_id=CLIENT_ID&client_secret=CLIENT_SECRET&grant_type=password&username=COMPA NY_ID&password=COMPANY_AUTH_TOKEN&credtype=authtoken”
    ```

    <br />

  <Callout icon="📘" theme="info">
    Note:

    You will need to replace the values for: DOMAIN, CLIENT\_ID, CLIENT\_SECRET, COMPANY\_ID, COMPANY\_AUTH\_TOKEN.
  </Callout>

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
    <br />
</Callout>

* **Employee Number** - The employee number.
* **Company ID (Concur ID of the Company)** - The Concur ID of the user.
* **First Name** - The user's first name.
* **Last Name** - The user's last name.
* **User Name Suffix** - The domain after the @ sign.
* **Emails** - Click `+` to add the user's email address. Multiple email addresses can be added. Click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TrashcanIcon-gray.png) to delete an email address.
  * **Email Address** - Select an adapter and a field that contains an email address.
  * **Email Type** - Select an email type from the list of options.
* **Preferred Language** - The user's preferred language.
* **Timezone** - The timezone where the user is located.
* **Cash Advance Account Code** - The cash advance code of the user.
* **Ledger Code** - The ledger code of the user.
* **Country** - The user's country.
* **Locale** - The language code for the selected country.
* **Reimbursement Currency** - The currency to use for reimbursements.
* **Travel Rule Class ID** - The name of the rule class to which the travel user belongs.
* **Employee Number of the Manager** -  The employee number of the manager.
* * **Is Active User** - When selected, sets the user as active.
* **Display Name** - The user's display name. Can be different than their First Name or Last Name. Select an adapter and a field that contains the display name.
* **Travel CRS Name** - The name of the profile in the GDS system.
* **Job Title** - Select an adapter and a field that contains a job title.
* **Enterprise Start Date** - The date the enterprise user started.
* **User Name** - The name that can be used to log in to CTE.
* **Phone Numbers** - Cick `+` to add the user's phone number. Multiple phone numbers can be added. Click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TrashcanIcon-gray.png) to delete a phone number.
  * **Number** - Select an adapter and a field that contains a phone number.
  * **Phone Number Type** - Select a phone number type from the list of options.
* **Approvers** - Click `+` to add multiple approvers. Click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TrashcanIcon-gray.png) to delete an approver.
  * **Approver Employee Number** - The employee number of the approver.
  * **Is Primary Approver** - Select if the approver is a primary approver.
* **Spend Custom Data** - Click `+` to add spend custom data.  Click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TrashcanIcon-gray.png) to delete a custom field.
  * **Custom Field ID** - Enter the custom field ID.
  * **Custom Field Value** - Enter the custom field value.
* **Disable User** - Set all users as non active. When enabled, this field overrides **Is Active User** (in case the latter is enabled too).
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [SAP User Provisioning Service](https://developer.concur.com/api-reference/user-provisioning/v4.user-provisioning.html) API.

## Required Permissions

To obtain the [Client ID and Client Secret](#connection-parameters), you need to register your application with SAP Concur. For more information, see [Getting Started](https://developer.concur.com/api-reference/authentication/getting-started.html#obtain-your-application-clientid-and-clientsecret-).

## Version Matrix

This Enforcement Action has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| 4.1     |           |       |

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).