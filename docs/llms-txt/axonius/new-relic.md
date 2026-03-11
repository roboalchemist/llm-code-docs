# Source: https://docs.axonius.com/docs/new-relic.md

# New Relic

New Relic provides cloud-based software to monitor and track servers, instances and services.

### Asset Types Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Software.svg) Software | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg) SaaS Applications | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_Services.svg) Application Services | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Load_Balancers.svg) Load Balancers | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Databases.svg) Databases | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Containers.svg) Containers | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Object_Storage.svg) Object Storage | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Network_Services.svg) Network Services | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Serverless_Functions.svg) Serverless Functions

## Before You Begin

**Ports**

* **TCP port 443**

**Authentication Method**

New Relic uses **API Keys** for authentication. Specifically, the REST API (v2) requires a **User Key** (personal API key) associated with a specific user account.

### APIs

Axonius uses the [New Relic REST API (v2)](https://docs.newrelic.com/docs/apis/rest-api-v2/get-started/introduction-new-relic-rest-api-v2/).

### Permissions

The following permissions are required:

* The user account associated with the **API Key** must have permissions to view and access entities (such as Applications, Hosts, and Services) across the accounts from which data is being fetched.
* The key inherits the permissions assigned to the user; therefore, the user must have a role (e.g., **Read/View** or **Admin**) that grants visibility into the relevant New Relic products (APM, Infrastructure, etc.).

#### Supported From Version

Supported from Axonius version 4.5

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for **New Relic**, and click on the adapter tile.\
Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the New Relic server.
2. **API Key** - A User API Key (personal API key) associated with a user account that has permissions to fetch assets. To obtain an API Key, see [Introduction to New Relic REST API (v2)](https://docs.newrelic.com/docs/apis/rest-api-v2/get-started/introduction-new-relic-rest-api-v2/).

<br />

<Image align="center" alt="New Relic connection screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NewRelic.png" />

### Optional Parameters

1. **Verify SSL** *(default: false)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.
5. **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network and not from the primary Axonius instance, which may be an Axonius-hosted (SaaS) instance or Customer-hosted (on-premises / private cloud). To use this option, you need to set up an Axonius Gateway.

<br />

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note:

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />

1. **Fetch Applications** - Select this option to enrich the device with applications data.
2. **Device Type inclusion list** - Enter a comma-separated list of values found in the “Field Segmentation” field on Relic. Devices that have this value will be included in the fetch.
3. **Prefer Hostname as Asset name** - Select this option to use the hostname as the device name.
4. **Enable Asset Type Segregation** - By default entities are shown as devices, select this option to segregate assets based on their asset type, rather than display them all as devices.