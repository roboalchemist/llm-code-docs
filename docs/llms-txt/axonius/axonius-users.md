# Source: https://docs.axonius.com/docs/axonius-users.md

# Axonius Users

The Axonius Users adapter fetches users with Axonius credentials and their permissions using our API client.

## Asset Types Fetched

* Users
* Roles

## Before You Begin

### Authentication Methods

* API Key and API Secret
* Certificate and Private Key files

### Required Permissions

The value supplied in [API Key and API Secret](#connection-parameters) must be associated with a user that is assigned to a role with the following permissions:

* **System Management** - Manage admin users - in order to be able to fetch admin users
* **System Management** - View system settings
* **Users Management** - View user accounts and roles
* **Users Management** - Manage Service Accounts
* **Dashboard** - View Dashboard
* **Activity Logs** - View activity logs to fetch User Activity Time Range

### APIs

To obtain an API Key and an API Secret, see [Axonius REST API](/docs/axonius-rest-api).

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Axonius Domain** *(required)* - The URL or IP address for the **Axonius instance**. Note: When configuring this adapter on a standalone local instance, instead of the URL or IP address, use `gui.axonius.local`.

2. **API Key** and **API Secret** *(required)* - An API Key and API Secret associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

<Image align="center" alt="Axonius Users - Add Connection" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Axonius_Users_Add_Connection.png" className="border" />

### Optional Parameters

1. **Certificate file** - Upload a client certificate file in `.pem` format if client certificate validation is required.

2. **Private key file** - Upload the corresponding private key file in `.pem` format for the client certificate.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

7. **User Activity Time Range (days)** - Enter a number of days to retrieve all activity logs for that user in that time range. Note that this requires the following permission: **Activity Logs -> View Activity Logs**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

* **Fetch service accounts** *(default: false)* - Select this option to fetch service accounts.  This setting requires the `Users Management: Manage Service Accounts` permission.
* **Get user query history** *(default: false)* - Select this option to get the user's query history actions from the number of days configured in the connection parameter **User Activity Time Range (days)**.

### Related Enforcement Actions

* [Axonius - Delete System Users](/docs/axonius-delete-system-users)
* [Axonius - Deactivate User](https://docs.axonius.com/axonius-help-docs/docs/deactivate-axonius-user)