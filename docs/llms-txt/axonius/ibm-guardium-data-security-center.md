# Source: https://docs.axonius.com/docs/ibm-guardium-data-security-center.md

# IBM Guardium Data Security Center

IBM Guardium Data Security Center is a platform that offers comprehensive data protection and security management solutions.

### Asset Types Fetched

* Devices, Users, Databases

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* API Key and Secret
* Encoded Token

### APIs

Axonius uses the [IBM Security Guardium Insights API](https://www.ibm.com/docs/en/guardium-insights/3.x?topic=security-api-keys#settings_api).

### Permissions

The Administrator Role or the Database Administrator role is required to fetch policies. For more information, see [Predefined roles, pages, and permissions](https://www.ibm.com/docs/en/guardium-insights/3.x?topic=management-predefined-roles-pages-permissions).

#### Supported From Version

Supported from Axonius version 6.1.67

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the IBM Guardium Data Security Center server.
2. **Authentication Methods** - Select an Authentication method, either **API Key and Secret** (default) or **Encoded Token**. For information on how to generate API keys, see [Creating API keys](https://www.ibm.com/docs/en/guardium-insights/3.x?topic=security-api-keys#settings_api).
   * **API Key** and **API Secret** - The API Key and API Secret for an account that has the Required Permissions to fetch assets.
   * **Encoded Token** - The token used to create the token header that you use to call the Guardium Insights API.

![IBM Guardium Data Security Center.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IBM%20Guardium%20Data%20Security%20Center.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).