# Source: https://docs.axonius.com/docs/shadowserver.md

# Shadowserver

Shadowserver gathers and analyzes data on malicious internet activity including malware, botnets, DDoS, fraud, and more.

### Asset Types Fetched

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg" /> Devices | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Vulnerabilities.svg" /> Aggregated Security Findings | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg" /> SaaS Applications

## Before You Begin

### Ports

TCP port 443

### Authentication Method

API Key + Secret Key Authentication

### APIs

Axonius uses the [Shadowserver Reports Query API](https://github.com/The-Shadowserver-Foundation/api_utils/wiki/API:-Reports-Query).
For more information, see [Shadowserver API documentation](https://github.com/The-Shadowserver-Foundation/api_utils/wiki).

The adapter interacts with the following Shadowserver API endpoints:

1. **`POST /api2/reports/types`**   List available report types for the organization

2. **`POST /api2/reports/list`**  List specific reports available for download

3. **`GET https://dl.shadowserver.org/{report_id}`**  Download report CSV files

### Required Permissions

Access is controlled at the organization/subscription level.

The API key and secret must have the following permissions:

1. **Read Access to Subscribed Reports** The API key must be associated with an organization/recipient that has subscribed to Shadowserver's free daily network reports.
2. **Report Types Access** - Ability to query which report types are available for the organization.
3. **Report Download Access** - Ability to list and download reports for networks/systems that the organization is responsible for.

Note: Scoped Access

* Users can **ONLY** access data for networks they are responsible for.
* For National CERT/CSIRT organizations, access is limited to the country they are responsible for.

**No Cross-Organization Access**

* Recipients **cannot** request or receive data about other networks or systems that are not theirs.
* Access is strictly controlled at the organizational/network ownership level.

#### Supported From Version

Supported from Axonius version 4.6

<br />

### Setting Up Shadowserver  to Work with Axonius

You need to obtain the unique API key and secret for your organization from Shadowserver's subscription and request process.

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for Shadowserver, and click on the adapter tile.\
Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Shadowserver server. (default: transform.shadowserver.org)

2. **API Key**  - An API Key associated with a user account that has the Required Permissions to fetch assets.

3. **Connection Label** - A label to help you distinguish between multiple connections for the same adapter. See [Connection label](/docs/adding-a-new-adapter-connection#setting-adapter-connection-parameters) .

<Image align="center" alt="Shadowserver connection screen" border={false} width={500} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Shadowserver.png" />

### Optional Parameters

1. **Secret** - The secret ID for the password. This secret ID represents a unique identifier for the secret in Shadowserver.

2. **Download Base URL**  *(default: `https://dl.shadowserver.org`)* - The base URL used to download report CSV files from Shadowserver. Reports are downloaded by appending the report ID (from the reports/list API response) to this URL.  You should only enter a different value and override the default setting if Shadowserver provides an alternative download endpoint for your organization, or if you need to route downloads through a specific proxy or mirror.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

7. **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network and not from the primary Axonius instance, which may be an Axonius-hosted (SaaS) instance or Customer-hosted (on-premises / private cloud). To use this option, you need to set up an Axonius Gateway.

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

1. **Enabled reports types** (required, default: Device, Device IPV6, Scan SSL) - Select one or more report types to enable.
2. **Reports fetch type** (default Fetch 7 days back) - Use the drop-down to select whether to fetch **All reports**, or to fetch reports from a date range. To choose a date range select **Fetch x days back**, and enter the number of days ago from which to fetch reports.
3. **Fetch all report types** - Select this option to fetch all of the report types that are available in the Shadowserver system. When you choose this option, the the report types selected in 'Enabled reports types' are not relevant.

<br />