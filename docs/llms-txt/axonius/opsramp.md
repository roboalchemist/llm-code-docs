# Source: https://docs.axonius.com/docs/opsramp.md

# OpsRamp

OpsRamp is an AIOps-powered IT operations management (ITOM) solution.

### Asset Types Fetched

This adapter fetches the following types of assets:

<br />

Asset Types Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Software.svg) Software | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg) SaaS Applications | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Compute_Services.svg) Compute Services | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Application_Services.svg) Application Services | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Load_Balancers.svg) Load Balancers | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Databases.svg) Databases | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Containers.svg) Containers | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Object_Storage.svg) Object Storage | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Network_Services.svg) Network Services | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Serverless_Functions.svg) Serverless Functions | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Compute_Image.svg) Compute Images

<br />

## Before You Begin

**Ports**

**TCP port 443**

**Authentication Method**

Tenant ID and Key

### APIs

Axonius uses the [OpsRamp API](https://docs.opsramp.com/api/).

<br />

#### Supported From Version

Supported from Axonius version 4.4

<br />

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for **OpsRamp**, and click on the adapter tile.
Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** *( default: `https://api.opsramp.com`)* - The hostname or IP address of the OpsRamp server.
2. **Tenant ID**  - Use for server authentication. You can enter a comma separated list of Tenant Ids to fetch devices for more than one tenant with the same credentials. Refer to [OpsRamp API Guide ](https://docs.opsramp.com/api/api-getting-started/getting-started/) for information about obtaining the Tenant ID, Key and Secret.
3. **Key**  - An API Key associated with a user account that has permissions to fetch assets.
4. **Secret** - OAuth credentials. Refer to [OpsRamp Getting Started](https://docs.opsramp.com/api/api-getting-started/getting-started/) for information about how to get the OAuth credentials.

<br />

<Image align="center" alt="OpsRamp.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OpsRamp.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy**  - Connect the adapter to a proxy instead of directly connecting it to the domain.
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

1. **Device query filter** *(optional, default: empty)* - Define to use as a query filter when fetching devices. The format of the query filter, is the OpsRamp format fieldname:value1,value2+fieldname2:value1,value2. Refer to [OpsRamp Serach Resources](https://docs.opsramp.com/api/resource-management/tenants-tenantid-resources-search/) for a list of supported fields.
2. **Fetch applications** - Select this option to fetch software installed on devices.
3. **Device data enrichment** - Choose options by which to enrich the devices. The options are 'Scan Status' and 'Custom Attributes', the default is both enabled.
4. **Account number include list** - Enter a comma-separated list of account numbers from which data will be fetched. If no account number is entered, all account numbers are fetched.
5. **Parse tags as fields** - Select this option to parse tags as fields in addition to parsing them as tags.
6. **Fetch assets only as devices (Legacy Mode)** - Select this option to fetch assets only as devices instead of parsing them as different kinds of devices (i.e. compute services, databases, etc.).
7. **Prefer Cisco IOS Over Apple iOS** - Select this option to Prefer Cisco IOS Over Apple iOS.
8. **Filter uninstalled agents** - Select this option to filter uninstalled agents.

<br />