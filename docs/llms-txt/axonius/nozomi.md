# Source: https://docs.axonius.com/docs/nozomi.md

# Nozomi Vantage

Nozomi Vantage is a SaaS platform for global network monitoring and protection.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Vulnerabilities
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Nozomi Vantage server.

2. **API Key Name** and **API Key Token** *(required)* - The credentials associated with a user account that has permissions to fetch assets. For information about how to create the API key name and token, see [API keys in Vantage](https://technicaldocs.nozominetworks.com/products/vantage/topics/c_vantage_api-keys.html).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Nozomi Vantage](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Nozomi%20Vantage.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

### Endpoints Config

Enable each of the following options to enrich assets data with data from the required endpoint(s):

1. **Enrich Assets Endpoint with Vulnerabilities Endpoint**
2. **Enrich Assets Endpoint with Software Endpoint**
3. **Enrich Assets Endpoint with Sites Endpoint**

### Global Endpoints Config

1. **Pagination Page Size** *(default: 500)* - Enter a number to set the pagination size, meaning, how much information per request will be fetched from all endpoints.
2. **Worker Threads in Parallel** *(default: 1)* - Enter the number of workers that will send requests in parallel. The maximum value is 20. Note that entering a high value may affect performance, which depends on the resources available across your servers at the time of fetch. Consider scheduling the adapter before altering this value.

### Parser Config

1. **Choose field to populate Device Last Seen** *(default: last\_activity\_time)* - Select which field to populate Axonius's Device Last Seen field with. The default is `last_activity_time`, and you can also select `time`.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Nozomi Networks Vantage API V1](https://vantage.nozominetworks.io/api-docs/index.html).

## Supported From Version

Supported from Axonius version 6.1