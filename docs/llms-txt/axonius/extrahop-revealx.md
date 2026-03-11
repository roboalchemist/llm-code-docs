# Source: https://docs.axonius.com/docs/extrahop-revealx.md

# ExtraHop Reveal(x)

ExtraHop Reveal(x) is a network detection and response (NDR) solution that provides visibility, real-time threat detection, and response.

## Parameters

1. **Domain** *(required)* - The hostname or IP address of the ExtraHop Reveal(x) server.
2. **API Key** *(required)* - An API Key associated with a user account that has one of the following privilege a user account that has the [Required Permissions](#required-permissions) to fetch assets.
3. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Domain**. For more details, see [SSL Trust & CA Settings](../global-settings#ssl-trust-amp-ca-settings).
   * If enabled, the SSL certificate offered by the value supplied in **Domain** will be verified against the CA database inside of Axonius. If the SSL certificate can not be validated against the CA database inside of Axonius, the connection will fail with an error.
   * If disabled, the SSL certificate offered by the value supplied in **Domain** will not be verified against the CA database inside of Axonius.
4. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Domain**.
   * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **Domain**.
   * If not supplied, Axonius will connect directly to the value supplied in **Domain**.
5. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(777\).png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Calculate last seen using only "Last Seen Time”** - Select this option to only use the field "Last Seen Time" to determine the last seen of the device. Otherwise the system uses the most recent value from the fields mod\_time, discover\_time, user\_mod\_time, last\_seen\_time.
2. **Exclude devices without IP addresses** -  Select this option so that the adapter will not fetch devices without an IPV4 IP address.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [ExtraHop REST API v1](https://docs.extrahop.com/8.0/rest-api-guide/#generate-an-api-key).

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with a user account that has one of the following privilege levels that enables them to fetch assets, achieved by 'Perform all GET operations through the REST API':

* "write": "personal"
* "write": "limited"

To generate an API Key, see [ExtraHop REST API - Generate an API Key](https://docs.extrahop.com/8.0/rest-api-guide/#generate-an-api-key).

## Version Matrix

Axonius should be compatible with any version of the ExtraHop Reveal(x) that works with ExtraHop REST API v1. Please contact [Axonius Support](mailto:support@axoniuscom) if you have a version that is not functioning as expected.