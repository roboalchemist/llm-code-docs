# Source: https://docs.axonius.com/docs/ibm-qradar.md

# IBM QRadar

IBM QRadar is a Security Information and Event Management (SIEM) solution that enables security teams to detect, prioritize and response to threats across the enterprise.

<br />

### Asset Types Fetched

* Devices, Users, Networks (if enabled in Advanced Settings)

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password for Cloud
* API Token for on-prem

### APIs

Axonius uses [IBM QRadar REST API V20.0](https://ibmsecuritydocs.github.io/qradar_api_20.0/).

### Permissions

The value supplied in [API Token](#required-parameters) must have read access to devices.

* Steps for creating an API token for IBM QRadar On Prem can be found here: [Adding An Authorized Service](https://www.ibm.com/docs/en/qsip/7.5?topic=services-adding-authorized-service)

* Steps for creating an API token for IBM QRadar On Cloud can be found here: [Adding An Authorized Service Token](https://www.ibm.com/docs/en/qradar-on-cloud?topic=tokens-adding-authorized-service-token)

Both of these methods produce a token that is only displayed once. Please be sure to copy down the token at the end of the creation process as it can't be viewed again.

IBM QRadar On Cloud users may need to also whitelist the IP address of the Axonius instance. Instructions on doing so can be found here: <Anchor label="Editing or deleting an allowlisted IP address" target="_blank" href="https://www.ibm.com/docs/en/qradar-on-cloud?topic=console-editing-deleting-allowlisted-ip-address">Editing or deleting an allowlisted IP address</Anchor>

The following endpoints require permissions:

* `/api/asset_model/*` - Requires Vulnerability Management or Assets permissions. Data returned is restricted based on the security profile assigned.
* `/api/system/*` - Requires Admin permission and Admin security profile.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the IBM QRadar server.
2. **User Name** and **Password** - The credentials for a user account that has the permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  If **API Token** is not supplied, these fields are required.
</Callout>

3. **API Token**  - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

<Callout icon="📘" theme="info">
  Note

  If **User Name** and **Password** are not supplied, this field is required.
</Callout>

<br />

<Image alt="IBM QRadar" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IBM%20QRadar.png" />

<br />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password**  - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Log Sources without Pagination** *(default: false)* - Select this option to fetch all log sources at once without pagination. When enabled, this setting may assist Axonius in receiving log sources that were not received with pagination.
2. **Fetch All Asset Model Assets** - Select this option to fetch all asset model assets as devices.
3. **Network Interface Enrichment** - Select this option to parse network interface related fields.
4. **Fetch Networks** - Select this option to fetch networks.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version                      | Supported | Notes |
| ---------------------------- | --------- | ----- |
| IBM QRadar V7.3.0 and higher |           |       |