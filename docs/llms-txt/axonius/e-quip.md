# Source: https://docs.axonius.com/docs/e-quip.md

# E-Quip

E-Quip is a specialized asset management solution designed for healthcare engineering to track medical device inventory and lifecycle maintenance.

The E-Quip adapter enables Axonius to fetch and catalog medical assets, providing visibility into their inventory details and related maintenance information.

## Asset Types Fetched

* Devices

## Data Retrieved through the Adapter

* **Equipment Identification** - Serial numbers, model names, brand details, and internal equipment codes or IDs.
* **Location and Ownership** - Site codes, specific locations, organization details, and responsible teams.
* **Status and Classification** - Equipment categories, risk levels, test equipment flags, and current operational status.
* **Maintenance and Lifecycle** - Calibration dates (expiry/last), repair history, and Planned Preventative Maintenance (PPM) schedules including last performed and next due dates.

## Before You Begin

### Required Ports

* TCP port 443 (HTTPS)
* TCP port 80 (HTTP, if SSL is not configured on the E-Quip instance).

### Authentication Methods

* The E-Quip adapter uses token-based authentication and connects using a User Name and Password.
* The authentication token is used in the authorization header (`Bearer <token>`) for all subsequent requests to fetch device data.

### Required Permissions

* **API Access** - The user account must be able to generate authentication tokens via the API.
* **Asset Read Access** - The account requires **Read-only** permissions for the device/equipment inventory to fetch asset details.
* **Best Practice** - Use a dedicated Service Account with the principle of least privilege (Read-only).

### APIs

Axonius uses the E-Quip REST API to retrieve asset data..

<Callout icon="📘" theme="info">
  Note

  The E-Quip REST API documentation is not publicly available. Please contact Integra Support or your E-Quip administrator to obtain the API specifications for your version.
</Callout>

* **Base URL** - `https://<host-url>/api/v1/`
* **Authentication endpoint** - `/api/v1/Auth/token`

### Supported from Version

This adapter is supported from Axonius version 8.0.4.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** - Enter the hostname or IP address of the E-Quip server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** - Enter the credentials for a user account that has permission to fetch assets.

<Image align="center" alt="E-Quip adapter - Add Connection" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/E-Quip_Add_Connection.png" className="border" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Configuration

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

Specific advanced settings that relate to the E-Quip adapter are shown in the following figure.

<Image align="center" alt="E-Quip adapter - Advanced Configuration" border={true} width="80% " src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/E-Quip_Advanced_Configuration.png" className="border" />

* **Enrich List Devices with Device Details** – Select this option to fetch the full set of attributes for each device. When enabled, the adapter performs an additional API request per device to retrieve detailed information that is not included in the initial inventory list.