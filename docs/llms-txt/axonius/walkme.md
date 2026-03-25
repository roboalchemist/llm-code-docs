# Source: https://docs.axonius.com/docs/walkme.md

# WalkMe

WalkMe is a digital adoption platform that provides in-app guidance, user behavior tracking, and automation to enhance software usage and engagement.

### Asset Types Fetched

* Devices, Users, SaaS Applications

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Consumer Key / Consumer Secret

**To generate the Consumer Key and Secret**:

1. Go to the [Admin Center](https://admin.walkme.com/).
2. Click the **API Keys** tab.
3. Click **Create New Key**.
4. Enter the key name.
5. Select permissions.
6. Click **Create**.

### APIs

Axonius uses the following API endpoints:

* [Get All Systems](https://developer.walkme.com/reference/get-all-systems)
* [Get All Users](https://developer.walkme.com/reference/get-all-users-1)
* [Discovery Apps API](https://developer.walkme.com/reference/discovery-apps-api)

### Permissions

The following permissions are required:

* API key Read permissions must be explicitly enabled during creation.

* The Admin Manager needs to create a user to use the API.

#### Supported From Version

Supported from Axonius version 7.0.12

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the WalkMe server.
2. **Consumer Key** and **Consumer Secret**  - The credentials for a user account that has the Required Permissions to fetch assets.

![WalkMe.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/WalkMe.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Date Range - applies context on the following endpoints: Discovery Apps**
  * **Discovery Apps Dates** *(optional)* - Enter the date range in the format YYYY-MM-DD;YYYY-MM-DD to fetch SaaS applications. The data from all the months between the specified dates will be fetched.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>