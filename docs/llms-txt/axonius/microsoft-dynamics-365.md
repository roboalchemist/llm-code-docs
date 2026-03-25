# Source: https://docs.axonius.com/docs/microsoft-dynamics-365.md

# Microsoft Dynamics 365

Microsoft Dynamics 365 Finance is a Microsoft enterprise resource planning system for medium to large organizations.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Microsoft Dynamics 365 Finance server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Client ID** and **Client Secret** *(required)* - Credentials provided by Microsoft Dynamics 365 Finance for authentication to the API for read access.

3. **Tenant ID** *(optional)* - A globally unique identifier (GUID) that is different than the organization name or domain. This identifier may be needed when configuring OneDrive policies.

4. **Authorization Code** *(optional)* - The authorization code after running an Oauth authentication.  To generate the **Authorization Code** run the following URL. Replace the `TENANT_ID` and `CLIENT_ID` placeholders in the url with the actual parameters.
   ```
   https://login.microsoftonline.com/TENANT_ID/oauth2/v2.0/authorize?client_id=CLIENT_ID&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%2Faxonius%2Fmicrosoft_dynamics_365_adapter&response_mode=query&scope=offline_access+https%3A%2F%2Fgraph.microsoft.com%2F.default&state=12345
   ```
   <br />

5. **Devices Data Project** *(optional)* - The project name to fetch per device.

6. **Users Data Project** *(optional)* - The project name to fetch per user.

7. **Verify SSL** - Select this option to verify the SSL certificate of the server against the CA database inside of Axonius.  To learn more, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

8. **HTTPS Proxy** *(optional)* - Connect the adapter to this proxy instead of directly connecting it to the domain.

9. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

10. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="MicroSoftDynamics365" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MicroSoftDynamics365.png" />

## APIs

Axonius uses the [Microsoft Dynamics 365 Finance](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/data-management-api) API reference.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The values supplied in [Client ID](#parameters) and [Client Secret](#parameters) must be associated with credentials that have read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 4.8