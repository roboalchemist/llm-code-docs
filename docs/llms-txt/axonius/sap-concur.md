# Source: https://docs.axonius.com/docs/sap-concur.md

# SAP Concur 3.x

SAP Concur provides travel, expense and invoice management.

<Callout icon="📘" theme="info">
  Note

  This adapter supports SAP Concur API Version 3. If you are using SAP Concur API v4 use the [SAP Concur 4.x](/docs/sap-concur-4) adapter.
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* SaaS Data
  ​

## Parameters

1. **Geo Location (Domain)** *(required)* - The hostname or IP address of the SAP Concur server, provided by Concur when registering the application. Refer to step one of [SAP Concur OAuth2 API](https://developer.concur.com/api-reference/authentication/getting-started.html) for more information about registering an application with Concur.

2. **Client ID** and **Client Secret** *(required)* - Provided by SAP when registering the application.

3. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![SAP%20Concur%203.x](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SAP%20Concur%203.x.png)

## APIs

Axonius uses the:

* [SAP Concur OAuth2 API](https://developer.concur.com/api-reference/authentication/getting-started.html)

* [SAP Concur List Users API V3.0](https://developer.concur.com/api-explorer/v3-0/Users.html)

## Required Ports

Axonius must be able to communicate with the value supplied in [Geo Location](#parameters) via the following ports:

* **TCP port 443**: (HTTPS default)

## Required Permissions

* The value supplied in [User Name](#parameters) must have  **list users/read all** users permissions to fetch assets.

* The value supplied in [Client ID](#parameters) must be associated with credentials that have permissions to fetch assets.
  **To fetch SaaS data**

* Read permissions to the following endpoints is required:
  * /api/v3.0/common/users
  * /api/v3.0/expense/reports
  * /api/expense/expensereport/v2.0/report/

* The API client requires read permissions to the following report fields:
  * ExpenseTypeName
  * SpendCategory
  * VendorDescription
  * CardTransaction `>` TransactionMerchantName

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                        | Supported | Notes |
| ------------------------------ | --------- | ----- |
| SAP Concur List Users API V3.0 | Yes       |       |
| SAP Concur OAuth2 API          | Yes       |       |