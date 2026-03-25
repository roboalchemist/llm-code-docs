# Source: https://docs.axonius.com/docs/devo.md

# Devo

Devo is a cloud-native logging and security analytics solution that delivers real-time visibility for security and operations teams.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Devo Query API Endpoint** *(required)* - The API domain. Use [ Query API](https://docs.devo.com/confluence/ndt/latest/api-reference/query-api) to set your API endpoint. The default value is `https://apiv2-us.devo.com/search`.

2. **Query** *(required)* - The Query to perform in Devo. This adapter uses the same logic that the [CSV adapter](/docs/csv) uses. The queries configured in the adapter should have column names that are mapped to aggregated fields in order for the fields to be parsed. The adapter fetches each row as a device or a user, so if the queried table has multiple rows for each device, it’s better to add aggregation to the query, so that each device will have one row in the query result, with the relevant data.

3. **Query Data From Date Range** - The time range to query the data from

4. **Fetch Users** *(required)* - Check this to fetch users, otherwise Axonius fetches devices.

5. **OAuth Token** *(required)* - An OAuth Token associated with a user account that has permissions to fetch assets. Follow the guidance here [OAuth token](http://docs.devo.com/confluence/ndt/latest/api-reference/query-api/authorizing-query-api-requests#AuthorizingQueryAPIrequests-OAuthtoken) to get the token.

6. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).
   * When enabled, the SSL certificate offered by the value supplied in **Devo Query API Endpoint** is verified against the CA database inside of Axonius. When the SSL certificate can not be validated against the CA database inside  Axonius, the connection fails with an error.
   * When disabled, the SSL certificate offered by the value supplied in **Devo Query API Endpoint** is not verified against the CA database inside Axonius.

7. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Devo Query API Endpoint**.
   * When supplied, Axonius uses the proxy when connecting to the value supplied in **Devo Query API Endpoint**.
   * When not supplied, Axonius connects directly to the value supplied in **Devo Query API Endpoint**.

8. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Devo Query API Endpoint** via the value supplied in **HTTPS Proxy**.
   * When supplied, Axonius authenticates with this value when connecting to the value supplied in **HTTPS Proxy**.
   * When not supplied, Axonius does not perform authentication when connecting to the value supplied in **HTTPS Proxy**.

9. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the value supplied in **Devo Query API Endpoint** via the value supplied in **HTTPS Proxy**.
   * When supplied, Axonius authenticates with this value when connecting to the value supplied in **HTTPS Proxy**.
   * When not supplied, Axonius does not perform authentication when connecting to the value supplied in **HTTPS Proxy**.

10. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

The adapter uses the  CSV adapter logic for additional fields.
Queries configured in the adapter should have column names which are mapped to aggregated fields (the CSV field list) in order for those fields to be parsed.

In addition, the adapter fetches every row as a device (or a user), so if the queried table has multiple rows for each device, it’s better to add aggregation to the query, to make sure every device has one row in the query result, with the relevant data. For more information refer to [CSV adapter](/docs/csv).

<Image alt="Devo.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Devo(1).png" />

## APIs

Axonius uses the [Devo API](https://docs.devo.com/confluence/ndt/latest/api-reference).

## Required Ports

Axonius must be able to communicate with the value supplied in [Devo Query API Endpoint](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 4.5