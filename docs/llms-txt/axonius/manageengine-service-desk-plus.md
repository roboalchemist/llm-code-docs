# Source: https://docs.axonius.com/docs/manageengine-service-desk-plus.md

# ManageEngine ServiceDesk Plus

ManageEngine ServiceDesk Plus is an IT help desk and customer support system.

## Asset Types Fetched

This adapter fetches the following types of assets:

* Devices, Software, SaaS Applications, Networks

## Before You Begin

### Authentication Methods

You can connect the adapter with either of the following method:

* **Basic Authentication** - Use this option for on-prem deployment of ManageEngine ServiceDesk Plus.
* **oAuth 2.0** - Use this option for cloud deployment of ManageEngine ServiceDesk Plus (SDP).

### APIs

Axonius uses the following APIs:

* api/v3/assets

* api/v3/workstations

### Required Permissions

See [Generating a Technician Key Token](https://docs.axonius.com/docs/manageengine-service-desk-plus#for-basic-authentication-generating-a-technician-key-token) for the permissions required for the Technician key token.

## Initial Setup

### For Basic Authentication: Generating a Technician Key Token

<Callout icon="📘" theme="info">
  Notes

  * Only an administrator can generate the authentication key for technicians with login permission.

  * If a login for the technician is disabled, the API key is deleted.
</Callout>

**To generate an API Key for Technician Key Token:**

1. Login to ManageEngine ServiceDesk Plus as an administrator.
2. From the **User** section, click **Admin** `>` **Technicians** icon.
3. Select the existing Technician account (or create a new one) that will be used for the Axonius adapter connection.
   * To generate the API key for an existing technician, click  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Edit_icon.png) (**Edit**) on the same row as the desired technician.
   * To generate the API key for a new technician, click **Add New Technician**, enter the technician details and provide the login permission.  The **Generate API Key** window appears.

<Image align="center" alt="Generate API Key.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Generate%20API%20Key.png" />

3. Configure the following permissions for this technician account:
   1. Login Permission
   2. Read-only Access - Crucial for Axonius to successfully fetch asset data.
4. In **Key expires on**, click the **Never expires** option to generate a permanent API Key.
5. Click **Generate**. If a key is already generated for the technician, click **Regenerate**.
6. Copy the API Key and paste it into the Axonius **API Key** parameter.

### For oAuth 2.0: Configuring OAuth Authentication

To generate the **OAuth Client ID**, **OAuth Client Secret** and **OAuth Refresh Token:**

1. Go to the Zoho API Console: [https://api-console.zoho.com/](https://api-console.zoho.com/)

2. Click **Add client**.

3. Select **Self Client** and click **Create**. If a popup asks you to confirm, click **OK**.

4. On the API Console main page, select the **Self Client** application

5. From the **Generate Code** tab, enter the following details, then click **Create**:
   * Scope:
     * "SDPOnDemand.assets.READ"

     * Time Duration: “10 minutes”

     * Scope Description: free text (could be anything)

6. A popup **Generated Code** appears. Copy and paste the code to a temporary file.

7. From the **Client Secret** tab, copy the **Client ID** and **Client Secret** values to a temporary file.

8. Enter the values you copied to the following command on a Llinux machine (or Windows with curl):

```TEXT
curl -X POST "https://accounts.zoho.com/oauth/v2/token?grant_type=authorization_code&code=&client_id=&client_secret="
```

8. From the command's response, copy the value of `refresh_token` and save it in a temporary file.

9. Copy the **OAuth Client ID**, **OAuth Client Secret** and **OAuth Refresh Token** to the appropriate places in Axonius.

## Connecting the Adapter in Axonius

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the ManageEngine ServiceDesk Plus server that Axonius can communicate with.

2. **Select Authentication method** - the options are **oAuth 2.0** or **Basic Authentication**.

#### Basic Authentication

1. **Technician key token** - See [Generating a Technician Key Token](https://docs.axonius.com/docs/manageengine-service-desk-plus#for-basic-authentication-generating-a-technician-key-token) for information on how to obtain this token.

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/ManageEngineServiceDeskPlus_basic%20auth.png" />

#### oAuth 2.0

1. **OAuth Client ID**,  **OAuth Client Secret**  and  **OAuth Refresh Token** - See [Configuring OAuth Authentication](https://docs.axonius.com/docs/manageengine-service-desk-plus#for-oauth-20-configuring-oauth-authentication) for information on how to obtain these parameters.
   b. **OAuth Zoho Accounts URL** - Select the account URL from the menu or add your own. See [Refresh Access Tokens](https://www.manageengine.com/products/service-desk/sdpod-v3-api/getting-started/data-centers.html) for information on how to obtain the account URL.

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/ManageEngineServiceDeskPlus_oauth20.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Enrich device with installed software data** - Select this option to enrich devices with data about installed software.
2. **Enrich device with workstation data** - By default this adapter enriches devices with workstation data. Clear this option to not enrich devices with workstation data.
3. **Include Only Devices with Last Seen value** - Select this option to include devices in which Last Seen information is available.
4. **Exclude devices with the Product Type** - Enter specific device product type values to exclude.

#### **Showing Advanced Fields in Basic View**

You can configure fields that generally appear in 'Advanced'   to appear in 'Basic' view.
Use the plus sign to add an entry to each field.

<Image alt="ManageEngineAdditionalFields" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ManageEngineAdditionalFields.png" />

Enter fields in the following JSON format:

```JSON
[
{
    "label":"My First Field", 
    "raw_field": "field_a",
    "field_type": "str"
},
{
    "label":"My Second Field",
    "raw_field": "field_b",
    "field_type": "int"
}
]
```

* `label` - The name for the field you want to appear in the basic view.
* `raw_field` - The name of the field as it appears in JSON format on the Adapter Connections page of the Asset Profile (or Advanced view table).
* `field_type` - The field type as  it appears in JSON format. The following field types are supported. int, string, datetime, float, bool. You can write them in the following ways:

  'int', 'string', 'str', 'date', 'datetime', 'float', 'bool', 'boolean'.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Related Enforcement Actions

* [ManageEngine ServiceDesk Plus - Create Request](/docs/manage-engine-sdp-create-request)

* [ManageEngine ServiceDesk Plus - Create Request per Asset](/docs/create-manage-engine-sdp-request-per-entity)

### Supported From Version

Supported from Axonius version 4.7