# Source: https://docs.axonius.com/docs/ibm-bigfix.md

# BigFix

BigFix provides remote control, patch management, software distribution, operating system deployment, network access protection and hardware and software inventory functionality.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Aggregated Security Findings
* Software
* SaaS Applications

## Parameters

1. **BigFix Domain** *(optional)* - The hostname or IP address of the BigFix server that Axonius can communicate with via the [Required Ports](#required-ports).

<Callout icon="📘" theme="info">
  Note

  When **BigFix SOAP Domain** is not configured, **BigFix Domain** is required.
</Callout>

2. **BigFix SOAP Domain (to use instead of REST)** *(optional)* - The domain for the SOAP WebReports server. For information on how to correctly configure the SOAP WSDL, see [APIs](#apis).

<Callout icon="📘" theme="info">
  Note

  * When **BigFix Domain** is not configured, **BigFix SOAP Domain** is required.

  * When both domains are configured, **BigFix SOAP Domain** is used.
</Callout>

3. **Port** *(optional)* - Enter the port.

4. **User Name** and **Password** *(required)* - The credentials for a user account that has the  Required Permissions to fetch assets.

5. **Advanced Settings** *(optional)* - Use to run a query by Relevance expression instead of the regular flow.
   **To run by a Relevance expression in Advanced Settings**

   1. Create a JSON file containing the parameters **relevance** (string), **fields** (list of fields) and **mode**.  mode must have the constant value custom\_relevance.

   For example:

   ```JSON
    {
     "mode": "custom_relevance",
    "relevance": "ids of bes computers",
     "fields": ["id"]
    }
   ```

   b.     Upload the JSON file by clicking **Choose file**.

6. **Verify SSL** - Select whether to verify the SSL certificate offered by the value supplied in **BigFix Domain**. For more details, see [SSL Trust & CA Settings](/docs/global-settings#ssl-trust-amp-ca-settings).

7. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **BigFix Domain**.

8. **Max Requests Per Second** - Maximum number of API requests per second. Set this value if you experience rate limiting (401/429 errors).

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![BigFix](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BigFix.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Exclude IPv6 addresses** - Select this option to fetch only IPv4 addresses and exclude IPv6 addresses.
2. **Fetch CVEs** - Fetch CVE vulnerability information for computers.
3. **BigFix fields include list** *(optional)* - Specify a comma-separated list of fields to fetch from BigFix in addition to a basic set of data fetched for each device (such as IP, MAC address, OS information, serial number). The supplied field format should be as defined by BigFix. Otherwise, only basic data is fetched for each device.

<Callout icon="📘" theme="info">
  Note

  Fields should not contain double quotes.
</Callout>

4. **BigFix fields exclude list** - Specify a comma-separated list of BigFix property names to exclude from dynamic parsing, you can use regex phrases to identify multiple fields with a defined name structure
5. Fetch CPU details\*\* *(optional)* - Select whether to include CPU details in the fetch.
6. **Fetch installed applications** - Select this option to enrich devices with data for installed applications.
7. **Fetch installed and missing patches** - Select this option to enrich devices with installed and missing patches information.
8. **Only fetch devices that have been changed in the last X days** - Enter a number of days to filter the devices that are fetched based on the devices that were changed.
9. **BigFix fields to parse as tags** - Enter an  optional list of comma-separated field names to   additionally   parse  as adapter tags.
10. **Fetch analyses** - Select this option to fetch BigFix analyses results.
11. **Parse fields dynamically** *(default: true)* - By default Axonius parses fields dynamically. Clear this option to disable dynamic parsing of the adapter.
12. **Analysis and Site names** - Click the arrow and plus sign and enter Analysis name and Site names to filter the analysis results. When you use 'Fetch analyses' you have to enter at least one Analysis and Site name. Click the plus sign to add more.
13. **Enable Custom Parsing** - Enable this option to define how to parse specific fields from the raw data fetched. You can choose to parse the data into an already existing field, or create a new one. This adapter supports  **Device Custom Parsing**. See [Adapter Custom Parsing](https://docs.axonius.com/axonius-help-docs/docs/adapter-custom-parsing)  for more information.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Before connecting to the BigFix REST API, certain actions must be completed. For more information, see [Prerequisites](https://developer.bigfix.com/rest-api/prerequisites.html).

When connecting to the BigFix SOAP Domain, the SOAP WSDL needs to be correctly configured on the WebReports server. In order for the connection to work, the WSDL file needs to be in the correct location on the server. For more information, see [Configuring SOAP](https://developer.bigfix.com/other/soap-api/soap_configuration.html).

## Required Ports

Axonius must be able to communicate with the value supplied in [BigFix Domain](#parameters) via the following ports:

* 52311 (default port)

## Required Permissions

Create a new operator account and configure the following permissions:

* Assign "GSSC 3rd Line" role to the new operator
* Set "Can Submit Queries" and "Custom Content" permissions both to "Yes"
* Set "Unmanaged Assets" to "Show All"
* Set "Can use WebUI" and "Can use REST API" both to "Yes"

Configure the BigFix adapter in Axonius to use the new operator.

User format should be UPN format: [User@Domain.com](mailto:User@Domain.com)

For details, see [BigFix Server Requirements](https://help.hcl-software.com/bigfix/11.0/inventory/index.html).