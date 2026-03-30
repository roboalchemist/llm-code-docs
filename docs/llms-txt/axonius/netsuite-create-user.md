# Source: https://docs.axonius.com/docs/netsuite-create-user.md

# Netsuite - Create User

**Netsuite - Create User** creates new employee records in NetSuite directly from Axonius for:

* Assets returned by the selected query or assets selected on the relevant asset page.

When triggered, this action:

* Connects to your NetSuite instance using the REST API.
* Creates a new employee record with the specified first name, last name, and email domain.
* Automatically generates the employee's email address in the format: `firstname.lastname@domain`.
* Reports success or failure for the creation operation.

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

These fields must be configured to run the Enforcement Action.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Oracle NetSuite adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

    <Callout icon="📘" theme="info">
      Note

      To use this option, you must successfully configure a [Oracle NetSuite](https://docs.axonius.com/update/docs/netsuite) adapter connection.
    </Callout>

* **First Name** - The first name of the employee to create.

* **Last Name** - The last name of the employee to create.

* **Domain** - The email domain for the employee (e.g., "company.com").

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Company ID** - Your NetSuite Company ID (for example: `COMPANY_ID` from `https://COMPANY_ID.netsuite.com`).
  * **Client ID** - The OAuth 2.0 Client ID for API access.
  * **Certificate ID** - The Certificate ID for authentication.
  * **Private Key** - Upload the private key file for authentication.
  * **Private Key Algorithm** - Select the algorithm used for the private key.
  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.
  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

### How the Action Works

When this action is triggered:

1. Axonius validates that all required parameters are provided (first\_name, last\_name, domain).
2. The action connects to the NetSuite REST API using the provided credentials or stored adapter connection.
3. A pre-hook function (`create_user_email`) constructs the email address: `{first_name}.{last_name}@{domain}`
4. It calls the API endpoint: `POST /services/rest/record/v1/employee`
5. The request body includes:
   * `Email`: The constructed email address in the format: `firstname.lastname@domain`.
6. The NetSuite API creates the employee record and returns the new employee details.
7. Axonius records the result (success/failure) for the operation.

### APIs

Axonius uses the Oracle NetSuite API.

**API Endpoint:** `POST /services/rest/record/v1/employee`

**Request Body:**

```json
{
  "Email": "firstname.lastname@domain.com"
}
```

**Response:** Returns the created employee record with ID and details.

### Testing the Connection

Before using this action in a production enforcement, you can test the connection:

1. Configure all required parameters (or select a stored adapter connection).
2. Click **Test Connection**.
3. Verify that the connection to NetSuite is successful.