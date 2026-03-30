# Source: https://docs.axonius.com/docs/itpie.md

# ITPIE

ITPIE (Information Technology Programmable Integration Engine) is a suite of network analysis tools that uses proprietary algorithms and the organization's data to analyze IT infrastructure and provide a model that can be used for management.

### Use Cases the Adapter Solves

* **Network Infrastructure Discovery:** Discover and inventory all network devices analyzed by ITPIE to ensure comprehensive visibility of your IT infrastructure in Axonius.
* **Network Topology Validation:** Correlate ITPIE's network analysis and device fingerprinting data with other sources to validate network topology and identify discrepancies.
* **Device Lifecycle Management:** Track device first seen and last seen timestamps from ITPIE to identify stale or inactive network devices that may need decommissioning.

### Asset Types Fetched

* Devices

## Data Retrieved through the Adapter

The following data can be fetched by the adapter:

**Devices**: Fields such as Hostname, Device Manufacturer, Device Model, Operating System

## Before You Begin

### Required Ports

* TCP port 443 (HTTPS)
* TCP port 80 (HTTP)

### Authentication Methods

API Key Authentication.

### APIs

Axonius uses the ITPIE REST API v1. The following endpoint is called:

* `GET /api/collection/device`

### Required Permissions

The following permissions are required:

* **Read-only access** — The API key must have read access to device collection data.

### Supported From Version

Supported from Axonius version 4.5

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for **ITPIE**, and click on the adapter tile.

Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The ITPIE server domain or IP address. Example: `https://itpie.example.com`
2. **API Key** - The API key generated from the ITPIE console.

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/ITPIE.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />