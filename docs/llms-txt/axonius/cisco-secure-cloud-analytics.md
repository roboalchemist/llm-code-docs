# Source: https://docs.axonius.com/docs/cisco-secure-cloud-analytics.md

# Cisco Secure Cloud Analytics

Cisco Secure Cloud Analytics provides network visibility and threat detection for cloud and on-premises environments.

Cisco Secure Cloud Analytics (formerly Stealthwatch Cloud) is a SaaS-delivered network detection and response solution that provides comprehensive visibility and high-fidelity threat detection across hybrid and multi-cloud environments using dynamic entity modeling.

### Use Cases the Adapter Solves

* **Network Device Discovery:** Automatically discover and inventory network devices across cloud and on-premises environments to maintain an accurate asset inventory and identify shadow IT or unmanaged devices.
* **Threat Detection Correlation:** Correlate network threat detection data from Cisco Secure Cloud Analytics with asset information from other sources to prioritize security incidents based on device criticality and exposure.
* **Cloud Security Visibility:** Gain comprehensive visibility into cloud-based network infrastructure to ensure security coverage and compliance across hybrid and multi-cloud deployments.

### Asset Types Fetched

* Devices

<br />

## Data Retrieved through the Adapter

The following data can be fetched by the adapter:

**Devices**:  Fields such as Hostname, IP Address, Namespace, Created Date

## Before You Begin

### Required Ports

* TCP port 443 (HTTPS)

### Authentication Methods

API Key Authentication

The adapter uses API Key authentication with a username and API key combination.

### APIs

Axonius uses the Cisco Secure Cloud Analytics API version 3. The following endpoints are called:

* `GET /api/v3/hostnames/all/` - Retrieves all hostnames and associated device information

### Required Permissions

The API user must have access to the user management settings in the Cisco Secure Cloud Analytics portal in order to generate an API key.

**Note:** The exact permission names and role requirements should be confirmed with your Cisco Secure Cloud Analytics administrator or Cisco support, as detailed API permission documentation is not publicly available. The user account used for API access should have sufficient permissions to read device and hostname information.

### Supported From Version

Supported from Axonius version 8.0.14.0

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for Cisco Secure Cloud Analytics, and click on the adapter tile.

Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The base URL of your Cisco Secure Cloud Analytics portal. Example: `https://your-portal.obsrvbl.com`
2. **User Name** - The username associated with the API key in Cisco Secure Cloud Analytics
3. **API Key** - The API key generated from your user settings in the Cisco Secure Cloud Analytics portal

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/CiscoSecureCloudAnalytics.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

<br />

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />

<br />

<br />

<br />