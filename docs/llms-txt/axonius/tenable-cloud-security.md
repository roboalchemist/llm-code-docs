# Source: https://docs.axonius.com/docs/tenable-cloud-security.md

# Tenable Cloud Security

Tenable Cloud Security (formerly Ermetic) provides cloud-native application protection platform (CNAPP) capabilities for vulnerability management, compliance, and security posture management across multi-cloud environments.

### Use Cases the Adapter Solves

* **Cloud Asset Visibility:** Gain comprehensive visibility into virtual machines across AWS, Azure, GCP, and other cloud providers to identify all cloud-based assets in your environment.
* **Vulnerability Management:** Track and prioritize vulnerabilities (CVEs) across cloud workloads with severity ratings and exploitability information to focus remediation efforts.
* **Cloud Security Posture:** Monitor cloud security configurations and compliance status across multi-cloud environments to ensure adherence to security policies.

### Asset Types Fetched

* Devices,  Aggregated Security Findings, SaaS Applications

## Data Retrieved through the Adapter

The following data can be fetched by the adapter:

**Devices**: Fields such as: Hostname, Cloud Provider, Cloud Account Name

## Before You Begin

### Required Ports

* TCP port 443 (HTTPS)

### Authentication Methods

API Token Authentication

### APIs

Axonius uses the [Tenable Cloud Security GraphQL API](docs.ermetic.com/reference/graphql-api). The following endpoint is called:

* `POST /api/graph`

### Required Permissions

The adapter requires a user with the Collaborator role at minimum.

The **Collaborator** role provides the minimum required access:

* **Inventory: view** — Required to fetch virtual machines
* **Findings: view** — Required to fetch vulnerability findings

<br />

### Supported From Version

Supported from Axonius version 8.0.17.2

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for Tenable Cloud Security, and click on the adapter tile.

Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **API Endpoint URL** - Tenable Cloud Security API endpoint URL based on your tenant region. Example: `https://us.app.ermetic.com`

   Available regions: us, eu, au, br, ca, de, fr, in, jp, sg, uk, uae

2. **API Token** - Bearer token for authentication. Obtain from Tenable Cloud Security console.

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/TenableCloudSecurity.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **API Endpoint URL** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note:
  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />

**Enrich VirtualMachines with Vulnerabilities** - Select this option to fetch vulnerability findings (CVE data) for each virtual machine and enrich device records with severity, CVSS score, and exploitability information. Disable this setting to fetch only device inventory without vulnerability data.

<br />

<br />

<br />

<br />

<br />