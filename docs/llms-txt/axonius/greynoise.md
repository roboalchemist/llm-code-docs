# Source: https://docs.axonius.com/docs/greynoise.md

# GreyNoise

GreyNoise collects, analyzes, and filters internet scan activity.

## Asset Types Fetched

* Devices, Aggregated Security Findings, SaaS Applications

## Before You Begin

### APIs

Axonius uses the <Anchor label="GNQL Query" target="_blank" href="https://docs.greynoise.io/reference/gnqlstats-1">GNQL Query</Anchor>.

### Required Ports

* **80**
* **443**

### Required Permissions

The value supplied for **API Key** must be associated with credentials that have GNQL endpoint access.

## Connecting the Adapter in Axonius

### Required Parameters

1. **Subnets** - Enter one or more subnets to fetch. Multiple values are separated by a semicolon.

2. **Host Name or IP Address**  - The hostname or IP address of the Greynoise server.

3. **Key** - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/greynoise%20connect.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

5. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image align="center" alt="Greynoise" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Greynoise.png" />

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| API v2  | Yes       |       |

### Supported From Version

Supported from Axonius version 4.5

### Related Enforcement Actions

[GreyNoise - Enrich Asset Data](https://docs.axonius.com/axonius-help-docs/docs/enrich-device-data-with-grey-noise-io)