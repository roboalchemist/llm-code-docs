# Source: https://docs.axonius.com/docs/tines.md

# Tines

Tines is a no-code Security Orchestration Automation & Response (SOAR) solution.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users, Devices

## Before You Begin

### APIs

Axonius uses the [Tines REST API](https://www.tines.com/api/admin/users/list).

### Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

### Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.0

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Tines server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Tines.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**- The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

Expand the **Endpoints Config** section to access the following settings:

1. **Fetch Users of sub type Record User from User Records** - Enable to fetch Users from the User Records endpoint.
   * **Users Record Type ID** *(optional)* - Specify a record type ID (table ID) to fetch assets from.
2. **Fetch Devices from Device Records** - Enable to fetch Users from the Device Records endpoint.
   * **Devices Record Type ID** *(optional)* - Specify a record type ID (table ID) to fetch assets from.

For more information on these endpoints, refer to the [Tines documentation](https://www.tines.com/api/records/list/).

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />