# Source: https://docs.axonius.com/docs/productiv.md

# Productiv

Productiv is a SaaS management platform that provides real-time visibility into application usage, spend, and compliance to optimize software investments and governance.

### Asset Types Fetched

* Licenses
* Expenses
* SaaS Applications

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* Client ID/Client Secret

### APIs

Axonius uses the the following APIs:

* [Provisioned users](https://docs.app.productiv.com/developer-api/users.html)
* [App details](https://docs.app.productiv.com/developer-api/app-details.html)
* [App summaries](https://docs.app.productiv.com/developer-api/app-summaries.html)

### Permissions

The following scopes are required:

* [https://api.productiv.com/apps.read](https://api.productiv.com/apps.read)

* [https://api.productiv.com/users.read](https://api.productiv.com/users.read)

#### Supported From Version

Supported from Axonius version 6.1.71

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** *(default: `https://public-api.productiv.com/`)* - The hostname or IP address of the Productiv server.
2. **Authentication Domain** *(default: `https://login.api.productiv.com/`)* - Specify the name of the authentication domain.
3. **Client ID** and **Client Secret** - The credentials for a user account that has the Required Permissions to fetch assets.

<Image alt="Productiv.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Productiv.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).