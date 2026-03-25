# Source: https://docs.axonius.com/docs/nozomi-networks-guardian.md

# Nozomi Guardian and CMC

Nozomi Guardian and CMC (formerly Nozomi Networks Guardian) monitors network communications and device behavior for physical and virtual appliances.

## Types of Assets Fetched

* Devices
* Aggregated Security Findings
* SaaS Applications

## Parameters

1. **Guardian Appliance Domain** *(required)* - The Nozomi Networks Solution's web interface IP or domain that  Axonius can communicate with via the [Required Ports](#required-ports).
2. **User Name** and **Password** *(optional)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **OpenAPI Key Name** and **OpenAPI Key Token** are not supplied, **User Name** and **Password** are required.
</Callout>

3. **OpenAPI Key Name** and **OpenAPI Key Token** *(optional)* - This is an OpenAPI key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. See Chapters 3 and 5 in the N2OS User Manual for instructions on creating an OpenAPI key.

<Callout icon="📘" theme="info">
  Note

  When **User Name** and **Password** are not supplied, **OpenAPI Key Name** and **OpenAPI Key Token** are required.
</Callout>

4. **Custom Assets Query (Overrides default query)** *(optional)* - Provide a custom query to fetch specific assets, with the same syntax as in the Nozomi console. The query must refer to the "assets" table.

   * Example custom query: `assets | where concat(mac_address_level,ip) include? "confirmed"`
   * If no custom query is supplied, the default query is "assets," which will fetch all assets.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="nozomi guardian connection" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/nozomi%20guardian%20connection.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Do not populate hostnames and asset names with MAC addresses** *(optional, default: False)* - When selected, hostnames and asset names of devices will remain empty if the source has a MAC address for the asset's name/hostname.
2. **Pagination page size**  -  The number of devices to fetch in each request.
3. **Async chunks in parallel**  -  The number of requests to run in parallel.
4. **Fetch devices vulnerabilities** - Select this option to fetch vulnerabilities.
5. **Use last seen by** - Select which field to use as the aggregated “Last Seen“ field, either "Time" (default) or "Last activity time".
6. **Skip Vulnerabilities below likelihood value** - Enter a value so that the adapter won't fetch vulnerabilities that have a likelihood value below the set value.
   * The default is 0, meaning all vulnerabilities will be fetched if **Fetch devices vulnerabilities** is also turned on.
   * In order to enable **Skip Vulnerabilities below likelihood value**, **Fetch devices vulnerabilities** must not be selected.
7. **Ignore device if its name matches the appliance host** - Select to ignore assets whose name matches the appliance host value.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Ports

Axonius must be able to communicate with the value supplied in [Guardian Appliance Domain](#parameters) via the following ports:

* **TCP port 443**: SOAP API

## Required Permissions

The value supplied in [User Name](#parameters) must have read access to devices.
The credentials of the user performing the OpenAPI call to query data must be in a group that has the Queries and exports permission set. This allows the user to view the query section and to export data.

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1023)(708).png" />