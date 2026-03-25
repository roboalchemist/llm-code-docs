# Source: https://docs.axonius.com/docs/ibm-bigfix-inventory.md

# BigFix Inventory

BigFix Inventory gathers information about installed software and hardware in your IT infrastructure.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Aggregated Security Findings, Software, SaaS Applications

## Parameters

1. **BigFix Inventory Domain** *(required)* - The hostname of the   BigFix Inventory server.
2. **User Name** and **Password** *(optional)* - The credentials for a user account that has the permissions to fetch assets.
3. **API Token (For MFA Cases)** *(optional)* - The API token to authenticate. Should be used for MFA cases.
4. **Verify SSL** - Select whether to verify the SSL certificate offered by the value supplied in **BigFix Inventory Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
5. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **BigFix Inventory Domain**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="BigFix%20Inventory" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BigFix%20Inventory.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch CPU details** *(optional)* - Select whether to include CPU details in the fetch.

2. **Fetch installed software** *(optional, default: true)* - Select whether to fetch installed software data for fetched devices.

3. **Software page size** *(default: 10000)* - Set the default software page size the adapter will use when making requests.

4. **Device page size** *(default: 100000)* - Set the number of devices to fetch in each request.

5. **Fetch software CVE data** *(optional)* - Select whether to fetch CVE details in addition to the basic software data.

6. **Fetch only devices seen within the last X days** *(optional)* - Use this option to filter the devices that are fetched. Only devices with a last seen value within the last X days, where X is the input, will be fetched.

7. **List of custom properties to fetch** *(optional)* - Enter a comma-separated list of custom computer property numbers to fetch and parse. For example, if a custom computer property is `computer_property_1`, you need to enter 1 into the field. In order to use this option you need to enter the 'Custom JSON Properties definition'.

8. **Custom properties JSON definition** *(optional)* - You can enter a JSON object to define the mapping between the custom computer properties and their definition. This input is used to parse the custom computer properties with the desired title. The structure of the JSON file should be as follows:

```json
{
  "computer_property_1": {
    "type": [
      "string",
      "array",
      "null"
    ],
    "items": "string",
    "title": "Custom field ABC",
    "mappings": {
      "type": "array",
      "association": true,
      "description": "Mappings into datasource properties",
      "item": [
        {
          "datasource_site_remote_id": 1234,
          "datasource_analysis_remote_id": 5,
          "datasource_property_remote_id": 6,
          "datasource_id": 7
        }
      ]
    }
  },

```

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Ports

For details, see <Anchor label="Port requirements" target="_blank" href="https://help.hcl-software.com/bigfix/10.0/inventory/Inventory/planinconf/r_port_requirements.html">Port requirements</Anchor>.