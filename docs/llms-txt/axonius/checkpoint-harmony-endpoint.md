# Source: https://docs.axonius.com/docs/checkpoint-harmony-endpoint.md

# Check Point Harmony Endpoint

Check Point Harmony Endpoint is a suite of endpoint protection products that include mobile, email, collaboration, and SASE security.

### Asset Types Fetched

* Devices, Aggregated Security Findings, SaaS Applications

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Client ID/Access Key

### APIs

Axonius uses the Harmony Endpoint API.

### Permissions

The value supplied in [Access Key](#required-parameters) must be associated with credentials that have permissions to fetch assets.

**To use the Harmony Endpoint External API service**

1. Create a suitable API Key by entering in the **Service** field: Harmony Endpoint

   Once the key is created, it can be used indefinitely (unless an expiration date was explicitly set for it).

2. Authenticate using the [Infinity Portal External Authentication Service](https://app.swaggerhub.com/apis-docs/Check-Point/infinity-portal-api/1.0.1), making sure to select the correct Infinity Portal API Server for the geographic region of your tenant.

#### Supported From Version

Supported from Axonius version 4.5

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Infinity Portal Region** - From the dropdown, select the Check Point Infinity Portal region where your Infinity Portal services are hosted. Available options are US, APAC, or EU.
2. **Client ID** - Enter the Client ID, provided by Check Point.
3. **Access Key** - The credentials for a user account that has the required permissions to fetch assets.

<Image alt="CheckPoint_Harmony" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CheckPoint_Harmony.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Device Types to query** *(default: DEVICES)*  - From the dropdown, select which device type to query.
2. **Devices per page** *(optional, default: 2000)* - Specify the number of devices fetched per page.
3. **Fetch Vulnerabilities** - Select this option to fetch vulnerabilities for devices.
4. **Ignore Deleted Devices** - Select this option to ignore all devices that are deleted (set by the field isDeleted).

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version      | Supported | Notes |
| ------------ | --------- | ----- |
| 1.9.105 OAS3 | Yes       |       |