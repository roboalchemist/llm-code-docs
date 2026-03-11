# Source: https://docs.axonius.com/docs/symantec-edr.md

# Symantec Endpoint Detection and Response (EDR)

Symantec Endpoint Detection and Response (EDR) detects, protects, and responds to threats to the organization's network.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Symantec EDR server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Symantec EDR.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Symantec%20EDR.png" />

## APIs

Axonius uses the [EDR Entities Resource API](https://apidocs.securitycloud.symantec.com/#/doc?id=entities_resource).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* TCP port 443

## Required Permissions

The value supplied in [Client ID and Client Secret](#parameters) must by associated to a user that have read access to devices.
The user must have **atp\_view\_entities** permission (Included under User privileges).

To generate an OAuth client:

<Callout icon="📘" theme="info">
  Note

  You must have Admin rights to generate an OAuth client. Only users with the Admin role that created the OAuth client can view the Client ID and Client Secret. Other Admin roles can only view the Client ID.
</Callout>

1. Do one of the following:
   * In the EDR cloud console, click **Settings**.
     * Under **Environment**, select an appliance and then click **Data Sharing**.
   * In the EDR appliance console, click **Settings** > **Data Sharing**.
2. In the **OAuth Clients** section, click **Add Application**.
3. In the **App Name** field, type the name of the application that you want to register.
4. Select the API version that you intend to use.
   * The default setting is version 2.
5. Select to enable version 2 APIs.
   * A **Role** option appears.
   * Click the drop-down menu and select the user role for the app.
6. Click **Generate**. The client ID and client secret appear.