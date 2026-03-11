# Source: https://docs.axonius.com/docs/cisco-intersight.md

# Cisco Intersight

Cisco Intersight is a cloud operations platform that consists of optional, modular capabilities of infrastructure, workload optimization, and Kubernetes services.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **URL** *(required)* - The hostname or IP address of the Cisco Intersight server. For North America, use *`https://www.intersight.com`*. For EU, use *`https://eu-central-1.intersight.com`*.

2. **API Key** *(required)* - An API key ID generated using Cisco Intersight.

3. **Client Secret** *(required)* - Select **Upload File** to upload a file with the credentials generated using Cisco Intersight.

4. **Secret Passphrase** *(optional)* - Specify a passphrase for the private key.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Cisco Intersight" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Cisco%20Intersight.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch physical summaries** - Select this option to fetch physical devices as assets.
2. **Fetch SAN switches as assets** - Select this option to fetch SAN switches as assets.
3. **Override SAN switches name with MDS standard** - Select this option to follow Cisco Intersight Dashboard naming logic and override the available name in the SAN Switch API response using the MDS prefix along with the Network Policy Name.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the following APIs:

* [Cisco Intersight API](https://intersight.com/apidocs/apirefs/aaa/AuditRecords/model/)

* [Cisco Intersight OpenAPI V3](https://cdn.intersight.com/components/an-apidocs/1.0.11-17412/model/intersight-openapi-v3-1.0.11-17412.json)

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version   | Supported | Notes |
| --------- | --------- | ----- |
| Version 2 | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.6