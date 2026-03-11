# Source: https://docs.axonius.com/docs/backstage.md

# Backstage

Backstage is an open platform for building developer portals.

### Asset Types Fetched

* Users, Groups, Business Applications

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Access Token

### APIs

Axonius uses the [Backstage API](https://backstage.io/docs/features/software-catalog/software-catalog-api/).

### Permissions

Consult with your vendor for permissions for reading the objects.

#### Supported From Version

Supported from Axonius version 5.0

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Backstage server.
2. **Access Token** - An Access Token associated with a user account that has the Required Permissions to fetch assets.

![Backstage](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Backstage.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

5. **Generate a JWT Token Using the API Key** *(default: true)* - By default this adapter generates a JWT token using the API key. Clear this option to not generate a JWT token.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).