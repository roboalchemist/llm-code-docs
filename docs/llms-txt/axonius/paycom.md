# Source: https://docs.axonius.com/docs/paycom.md

# Paycom

Paycom is a programmatic interface for managing user roles and permissions.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Paycom server.

2. **SID** and **Token** *(required)* - The credentials for a user account that has permission to fetch assets. You receive the SID and Token from the Paycom automation team.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Paycom](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Paycom.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Endpoints Config** - By default this adapter enriches users via various endpoints. Click on `>` to open the following settings for configurable endpoints:
  * **Enrich Employees with Non-Sensitive Employee Details** *(default: true)* - By default this adapter fetches employee data from non-sensitive endpoints. Disable this option to not fetch employee data from non-sensitive endpoints.
  * **Enrich Employees with Employee Sensitive** - Enable this option to fetch employee data from sensitive endpoints.
* **Global Endpoints Config** - Click on `>` to open the following settings for configurable endpoints:
  * **Remove PII fields** - Enter a list of raw keys that should be removed from ingested data. Click the x next to any option you want to clear from the list.
* **Parser Config** - Click on `>` to open the following settings for configurable endpoints:
  * **Custom Fields Mapping** - Enter JSON to specify mapping between custom raw fields to specific fields in Axonius.
    JSON structure

```
{"raw_data_key_1": "Custom Field 1", "raw_data_key_2": "Custom Field 2"}
```

Implementation example:

```
{"raw_data_key_1": "Custom Field 1", "raw_data_key_2": "Custom Field 2"}
```

In this example, the raw field `cat1` will be mapped as `Payroll Profile` in Axonius, and similarly, the other specified fields will follow the given mapping.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the Paycom REST API.

## Supported From Version

Supported from Axonius version 6.1