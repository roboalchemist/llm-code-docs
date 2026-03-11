# Source: https://docs.axonius.com/docs/confluent.md

# Confluent

Confluent is a data streaming platform that enables you to easily access, store, and manage data as continuous, real-time streams.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Confluent server that Axonius can communicate with

2. **API Key ID** *(required)* - An API Key associated with a user account that has the OrganizationAdmin role to fetch assets.

3. **API Secret Key** *(required)* - An API Secret associated with a user account that has permissions to fetch assets.

<Callout icon="💡" theme="warn">
  Note

  The API Secret Key is only exposed momentarily in the Create API key dialog. Make sure to store the secret and its corresponding key in a secure location.
</Callout>

For more details about obtaining an API Key and API Secret Key, see [Create a Cloud API Key](https://docs.confluent.io/cloud/current/access-management/authenticate/api-keys/api-keys.html).

4. **Verify SSL** Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![confluent\_fields](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/confluent_fields.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **External Cluster Data to Fetch** *(required, default: Configs)* - From the dropdown, select one or more options to fetch external cluster data.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Confluent REST Proxy API](https://docs.confluent.io/platform/current/kafka-rest/api.html#).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The value supplied in [API Key](#parameters) must have basic authentication.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                          | Supported | Notes |
| -------------------------------- | --------- | ----- |
| Confluent REST Proxy API V1 & V3 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.5