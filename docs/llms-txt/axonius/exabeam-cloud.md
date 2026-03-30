# Source: https://docs.axonius.com/docs/exabeam-cloud.md

# Exabeam Cloud

Exabeam Cloud is a cloud-based Security Information and Event Management (SIEM) solution.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Exabeam Cloud server.

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets. For information on how to generate an API Key, see [Authentication](https://developers.exabeam.com/exabeam/docs/api-keys#generate-an-api-key).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image border={false} src="https://files.readme.io/25f9305fe65a530666e8a34e00c02a73e646d8635685db53149fd0f1c164920f-image.png" />

<br />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Only fetch devices seen in the last X number of day(s)** *(default: 30)* - Enter a number of days. This setting enables you to fetch only devices and corresponding information if they were seen by Exabeam Cloud in the number of days set.
2. **Time window batch size** *(optional)* - Enter an integer number defining the size of the time window batch.
3. **Time window batch unit** - *(optional)* - Select the time unit to apply to the number you entered in the previous field: Hours, Minutes, or Seconds.
   * **Example:** If the value of **Time window batch size** is 5 and the value of **Time window batch unit** is Minutes - the time window of the batch will be 5 minutes.
4. **Maximum devices per API call** - *(optional, default: 3000)* - Define the maximum number of devices allowed per API call.
5. **Fields to fetch** *(default: host, product, vendor)* - From the dropdown, select the fields to fetch from the API. The adapter will fetch the host, product, and vendor by default.
6. **Advanced hostname source mapping (JSON)** *(optional)* - Configure a field to use as the device hostname source. Use the following format:
   ```json
   {
       "target_field": "product_name",
       "conditions": [
           {
               "target_value": "Azure SQL",
               "hostname_field": "db_name"
           },
           {
               "target_value": "Example 2",
               "hostname_field": "case2fieldName"
           }
       ]
   }
   ```

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Exabeam API](https://developers.exabeam.com/exabeam/reference).

## Required Permissions

The value supplied in [User Name](#parameters) must have Read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.1