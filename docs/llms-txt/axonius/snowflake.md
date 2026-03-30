# Source: https://docs.axonius.com/docs/snowflake.md

#  Snowflake Data Warehouse

Snowflake is a data warehouse built on top of the Amazon Web Services or Microsoft Azure cloud infrastructure, and allows storage and compute to scale independently.

### Asset Types Fetched

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg" /> Devices | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg" /> Users | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Roles.svg" /> Roles | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_settings.svg" /> Application Settings | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Domains_URLs.svg" /> Domains & URLs | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Databases.svg" /> Databases

## Before You Begin

**Ports**

**TCP port 443**

**Authentication Method**

Username and RSA Private Key

### APIs

Axonius uses the [Snowflake SQL API](https://docs.snowflake.com/en/developer-guide/sql-api/index.html).

### Permissions

The following permissions are required:

The value supplied in **Username** must have Read permissions for the Table/View specified in the connection details.

#### Supported From Version

Supported from Axonius version 4.5

### Setting Up Snowflake to Work with Axonius

| Attributes                  | Axonius Cyber Assets                                                | Axonius SaaS Applications                                           |
| --------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Service Account Required?   | Yes                                                                 | Yes                                                                 |
| Service Account Permissions | Read Permissions                                                    | Read Permissions                                                    |
| Required Adapter Fields     | Account Identifier, Warehouse, View Name, Username, RSA Private Key | Account Identifier, Warehouse, View Name, Username, RSA Private Key |

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for **Snowflake**, and click on the adapter tile.\
Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Account Identifier** - The Snowflake account within your organization. The preferred structure is: `<organization_name>-<account_name>` For more information, see [Account Identifiers](https://docs.snowflake.com/en/user-guide/admin-account-identifier.html).
2. **Warehouse** *(default: COMPUTE\_WH)* - Enter the relevant data warehouse. Note that the value is case-sensitive.
3. **Username** - The credentials for a user account that has [required permissions](/docs/snowflake#required-permissions) to fetch assets.
4. **RSA Private Key** - Upload the [RSA Private Key](https://docs.snowflake.com/en/user-guide/key-pair-auth.html#configuring-key-pair-authentication) associated with a user account that has permissions to fetch assets.

<br />

<Image align="center" alt="Snowflake connection screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/SnowFlakeDateWArehouse.png" />

### Optional Parameters

1. **Devices View Name** - Enter the View/Table that you want to extract data from. The View/Table requires one of the following identifiers in order to fetch devices: 'ID', 'id', 'SERIAL', 'assetname'. Note that the values are case-sensitive. In each Snowflake account the name of the View/Table is user-defined (for example, ACCOUNT\_USAGE.DATABASES).
2. **Key Passphrase** - Enter the passphrase for an encrypted key.
   <Callout icon="📘" theme="info">
     Warning: Do not provide a passphrase for an unencrypted key.
   </Callout>
3. **Fetch users** - Toggle this option on to fetch users. When you select this option, the **Users view name** field is displayed. Enter a **Users view name**, this is the View/Table that you want to extract user data from. Note that the value is case-sensitive. The name of the default users view in Snowflake is ACCOUNT\_USAGE.USERS. It should contain at least the fields: USER\_ID, LOGIN\_NAME, NAME, EMAIL.

   <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/snowflakeuserse.png" />

   <br />
4. **Fetch API URLs** - Select this option to fetch API URLs.
5. **API URLs view name** - Enter an API URLs view name, this is the View/Table that you want to extract API URL data from.
6. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
7. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
8. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
9. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.
10. <br />
    **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network and not from the primary Axonius instance, which may be an Axonius-hosted (SaaS) instance or Customer-hosted (on-premises / private cloud). To use this option, you need to set up an Axonius Gateway.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note:

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

**Fetch databases as assets** - Toggle on to fetch databases as an asset.

1. * When **Fetch databases as assets** is selected, the **Databases View Name** option appears. If databases are not specified, then only "SHOW DATABASES" is queried, which fetches only the first level of databases.
   * When **Fetch databases as assets** is selected, the **Exclude databases that contain the following strings** option appears. You can enter a list of databases that contain certain strings to exclude from the fetch.
2. **Parse Additional Device Columns** - Select this option to parse additional device columns.
3. **Fetch warehouses** - Select this option to fetch warehouses as application resource assets.
4. **Fetch databases** - Select this option to fetch database assets as application assets. Select which of the following database assets to include:
   * **Fetch schemas**
   * **Fetch tables**
   * **Fetch views**
   * **Fetch procedures**
5. **Async Query Timeout (seconds)** - Set a time in seconds after which async operations will time out.
6. **Enable Custom Parsing** - Enable this option to define how to parse specific fields from the raw data fetched. You can choose to parse the data into an already existing field, or create a new one. This adapter supports **Database Custom Parsing**. See [Adapter Custom Parsing](/docs/adapter-custom-parsing) for more information.

**The following settings are only for accounts with Axonius SaaS Applications:**

1. **Fetch Snowflake Instance Admins** - Select this option to fetch users with the capability to manage the Snowflake instance.
2. **Organization Region** - The parameter in the account URL that represents the region where the organization’s account is located.

**The following settings are only for accounts with Axonius Identities**

1. **Identities assets to fetch** - Select this option to fetch the following Identity assets:
   * User assigned roles (requires the "Fetch Snowflake instance admins" setting to be enabled)

   * Account roles

   * Account role grants

   * Database roles (requires the "Fetch databases as application resources" setting to be enabled)

   * Database role grants