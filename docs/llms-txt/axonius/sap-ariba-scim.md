# Source: https://docs.axonius.com/docs/sap-ariba-scim.md

# SAP Ariba SCIM

SAP Ariba SCIM is a REST API that provides standardized identity and group master data provisioning for SAP Ariba environments based on the SCIM protocol.

### Asset Types Fetched

* Users, Groups

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Client ID / Client Secret
* API Key

### APIs

Axonius uses the SAP Ariba SCIM API.

### Permissions

**User Account Requirements**:
The integration must authenticate with a user that has permissions to:

* Access user identity information, including relevant attributes such as status, contact details, and organizational metadata
* Retrieve group data, including group names and user membership
* View extended user details when applicable, such as cost centers, company codes, and other business-related attributes.

#### Supported From Version

Supported from Axonius version 7.0.10

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the SAP Ariba SCIM server.
2. **Authentication Domain** - The OAuth Server URL Prefix for your region on the SAP Ariba Developer Portal.
3. **Client ID** and **Client Secret** - The credentials for a user account that has the Required Permissions to fetch assets.
4. **API Key** - An API Key associated with a user account that has the Required Permissions to fetch assets.
5. **AN ID or Unique Customer ID** - The AN ID or Unique Customer ID, by which the customer can be identified in Ariba Systems. (e.g., ANXXX002).

<Image alt="SAP Ariba SCIM connection screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/SAPAribaSCIM_AddConnection.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Enrich Users with User Details** - Enable this option to enrich the Users asset type with more user information.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](https://docs.axonius.com/docs/advanced-settings).
</Callout>

<br />

### Related Enforcement Actions

* [SAP Ariba SCIM - Create User](https://docs.axonius.com/axonius-help-docs/docs/docssap-ariba-scim-create-user)
* [SAP Ariba SCIM - Suspend User](https://docs.axonius.com/axonius-help-docs/docs/sap-ariba-scim-suspend-user)
* [SAP Ariba SCIM - Delete User](https://docs.axonius.com/axonius-help-docs/docs/sap-ariba-scim-delete-user)
* [SAP Ariba SCIM - Create Group](https://docs.axonius.com/axonius-help-docs/docs/sap-ariba-scim-create-group)
* [SAP Ariba SCIM - Assign User to Group](https://docs.axonius.com/axonius-help-docs/docs/sap-ariba-scim-assign-user-to-group)
* [SAP Ariba SCIM - Delete Group](https://docs.axonius.com/axonius-help-docs/docs/sap-ariba-scim-delete-group)