# Source: https://docs.axonius.com/docs/algosec-firewall-analyzer.md

# AlgoSec Firewall Analyzer

AlgoSec Firewall Analyzer (AFA) is a device analysis solution that builds a model of users' network security postures and Layer 3 connectivity.

## Asset Types Fetched

* Devices, Users, Network/Firewall Rules

## Before You Begin

### APIs

Axonius uses the <Anchor label="ASMS API" target="_blank" href="https://techdocs.algosec.com/en/asms/a32.60/asms-help/content/api-guide/afa-rest-web-services.htm">ASMS API</Anchor>.

### Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80**
* **TCP port 443**

### Required Permissions

The value supplied in [User Name](#parameters) must have Admin privileges.

## Deploying the Adapter in Axonius

### Required Parameters

<Image border={false} src="https://files.readme.io/f9a631f836fa53438bd8a0a0806fa846ae17847e8a1cff4bd6e43f9364a1b6e8-image.png" />

### Optional Parameters

1. **Host Name or IP Address**  - The hostname or IP address of the AFA server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **AlgoSec Domain ID** - Enter your unique domain ID, obtainable from the **Domains** tab in the AlgoSec dashboard.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch users** *(default: True)* -  By default this adapter fetches users. Clear this option to not fetch users.
2. **Fetch Firewall Rules** - Select this option to fetch devices with Firewall Rules.
3. **Parse Rules As Firewall Assets** - Select this option to parse Rules as Network/Firewall Rules.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| 1.0.0   | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.7