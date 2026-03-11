# Source: https://docs.axonius.com/docs/fortify-software-security-center.md

# Fortify Software Security Center

Fortify Software Security Center offers security assurance solutions that address the threats posed by security flaws in business-critical software apps.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key/API Token

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Fortify Software Security Center server.
2. **Token** - Specify your account API key or an API token you have created. For details see [Fortify Software Security Center - Authentication](https://fortify.github.io/ssc-js-sandbox-docs/#/2017/08/03/authentication).

![Fortify Software Security Center](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Fortify%20Software%20Security%20Center.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Ignore removed issues** *(required, default: true)*
   * If enabled, for each project, removed issues will not be fetched.
   * If disabled, for each project, all issues will be fetched.
2. **Fetch Attributes** - Select this option to fetch attributes from another endpoint.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version        | Supported | Notes |
| -------------- | --------- | ----- |
| fortifyapi 2.3 | Yes       |       |