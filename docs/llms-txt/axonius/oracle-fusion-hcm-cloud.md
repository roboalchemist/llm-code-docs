# Source: https://docs.axonius.com/docs/oracle-fusion-hcm-cloud.md

# Oracle Fusion HCM Cloud

Oracle Cloud Human Capital Management is a cloud-based HCM software application suite for global HR, talent, and workforce management.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* Roles

## Connecting the Adapter in Axonius

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Oracle Fusion HCM Cloud server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Auth Type** - Select between Basic and OAuth.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

### Parameters Required for Basic Authentication

**User Name** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

### Parameters Required for OAuth Authentication

**Client ID** and **Client Secret** - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets. For detailed explanation on how to obtain these parameters, see <Anchor label="Configure OAuth Using Client Credentials Grant Type (2-legged OAuth)" target="_blank" href="https://docs.oracle.com/en/cloud/saas/applications-common/25c/oaext/configure-oauth.html#Configure-OAuth-Using-Client-Credentials-Grant-Type-(2-legged-OAuth)">Configure OAuth Using Client Credentials Grant Type (2-legged OAuth)</Anchor>

### Optional Parameters

1. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

2. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

3. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image border={false} src="https://files.readme.io/5d9ae308084a9474d5b06067fdb29e303b039cd52017cb1ebe347c5968d8a76d-image.png" />

<br />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Sensitive Fields to Include** - Enter a list of sensitive fields to be included.
2. **Parse user assignments as roles** - Select this option to parse user assignments as Security Roles.
3. **Parse Person Number as Employee ID** - Select this option to parse the Person Number as the Employee ID.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Oracle Fusion Cloud HCM REST API](https://docs.oracle.com/en/cloud/saas/human-resources/22c/farws/rest-endpoints.html).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port  80**
* **TCP port 443**

## Required Permissions

The value supplied in [User Name](#parameters) must have the following security privileges and roles to fetch assets.

<Table>
  <thead>
    <tr>
      <th>
        Grant Type
      </th>

      <th>
        Privilege
      </th>

      <th>
        Resource
      </th>

      <th>
        Available in Roles
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Function Privilege
      </td>

      <td>
        Use REST Service - Workers (PER\_REST\_SERVICE\_ACCESS\_WORKERS\_PRIV)
      </td>

      <td>
        workers (Get)
      </td>

      <td>
        * HCM Connections REST Services (ORA\_PER\_CONNECTIONS\_DUTY)
        * Use REST Service - Worker as Worker (ORA\_PER\_REST\_SERVICE\_ACCESS\_WORKER\_AS\_WORKER)
        * Use REST Service - Worker as Manager (ORA\_PER\_REST\_SERVICE\_ACCESS\_WORKER\_AS\_MANAGER)
        * Use REST Service - Worker as HR (ORA\_PER\_REST\_SERVICE\_ACCESS\_WORKER\_AS\_HR)
        * Use REST Service - Worker Sensitive Details (ORA\_PER\_REST\_SERVICE\_ACCESS\_WORKER\_SENSITIVE)
        * Use REST Service - Worker PII (ORA\_PER\_REST\_SERVICE\_ACCESS\_WORKER\_PII)
        * Use REST Service - Worker Details (ORA\_PER\_REST\_SERVICE\_ACCESS\_WORKER\_PERSON)
        * Use REST Service - Worker Employment (ORA\_PER\_REST\_SERVICE\_ACCESS\_WORKER\_EMPLOYMENT)
        * Use REST Service - Person Identifiers for External Applications (ORA\_PER\_REST\_SERVICE\_ACCESS\_PERSON\_IDS\_FOR\_EXTERNAL\_APPS)
      </td>
    </tr>
  </tbody>
</Table>

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version     | Supported | Notes |
| ----------- | --------- | ----- |
| 11.13.18.05 | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.7