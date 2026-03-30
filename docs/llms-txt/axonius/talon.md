# Source: https://docs.axonius.com/docs/talon.md

# Talon

Talon is a secure enterprise browser designed to defend against malware and prevent data loss for managed and unmanaged devices.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Talon server.

2. **API Token** *(required)* - The credentials for a user account that has the permissions to fetch assets.

   To obtain the credentials, see [Obtain the API Token](/docs/talon#obtain-the-tenant-id-and-api-token).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Talon" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Talon.png" />

## Obtain the API Token

**To obtain the  API Token**

1. Access the Talon Management Console using a user with an Admin role.
2. Select **Administration** `>` **API Integrations**.
3. Click **Add API Client**.
4. Create a client with the desired name.
5. Copy the **API Token**.

## Supported From Version

Supported from Axonius version 4.6