# Source: https://docs.axonius.com/docs/oracle-identity-management.md

# Oracle Identity and Access Management (IAM)

Oracle Identity and Access Management (IAM) is a software suite that enables enterprises to manage and automate user identities.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* Roles

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Oracle Identity and Access Management (IAM) server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Oracle IAM" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Oracle%20IAM.png" />

## APIs

Axonius uses the [Oracle Identity Governance Self Service REST API](https://docs.oracle.com/cd/E52734_01/oim/OIGSS/index.html).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

### Parsing Config - Custom Parsing

Enable **Custom Parsing** to define how to parse specific fields from the raw data fetched. You can choose to parse the data into an already existing field, or create a new one. This can be set separately for each type of asset fetched by the adapter: Users and Roles.

<Image align="center" alt="OracleCustomParsing" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-0VLWEW3A.png" />

Expand each asset type's Custom Parsing section to add fields. For each field, specify the following:

* **Field Title** - Select a column title from the list. Note that you can also select nested fields of complex fields.

* **Raw Path** - The path to the field in the raw data, for example: `my_path|my_sub_path`

* **Type** - Select a field type from the list: string, boolean, etc. Will be ignored for common fields.

* **Field Structure** - Specify whether the field is a single value or list field. Will be ignored for common fields.
  Click **+ Add Field** to add as many fields as you like, or **x** to delete the row.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Supported From Version

Supported from Axonius version 6.1