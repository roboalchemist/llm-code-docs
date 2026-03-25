# Source: https://docs.axonius.com/docs/statseeker-adapter.md

# Statseeker

Statseeker is a network performance monitoring solution.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Statseeker server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has  permission to fetch assets and has been [assigned permissions to interact with the API](#apis).

3. **Connection Type** - Select the connection type, *Bearer Token* (default) or *Basic Authentication* (deprecated in Statseeker). The credentials required are the same for each option. Refer to [Token-based Authentication](https://docs.statseeker.com/api/restful-api-latest/#apiAuthMethod:~:text=%5Btop%5D-,Token%2DBased%20Authentication,-The%20Statseeker%20server).

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Statseeker" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Statseeker.png" />

<br />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

<br />

## APIs

Axonius uses the [Statseeker RESTful API v2.1 r14 (latest)](https://docs.statseeker.com/api/restful-api-latest/) API.

Refer to [Manage API User's access to Data](https://docs.statseeker.com/api/restful-api-latest/#dataRequirements) on how to assign to users API access (read-write, read, or write) and data access permissions.

## Supported From Version

Supported from Axonius version 6.0