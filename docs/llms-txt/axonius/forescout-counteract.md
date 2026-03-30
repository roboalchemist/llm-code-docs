# Source: https://docs.axonius.com/docs/forescout-counteract.md

# ForeScout CounterACT

ForeScout CounterACT platform provides insight into network-connected devices.

<Callout icon="📘" theme="info">
  Note

  You need a license for the ForeScout eyeExtend Connect Module for Web API from the vendor in order to use this adapter.

  To allow Axonius to use the ForeScout eyeExtend Connect Module for Web API, you need to install and configure that module, especially user credentials and valid IP addresses. For details, see  '[How to Install' and 'Configure the Module' sections in the ForeScout eyeExtend Connect Module for Web API Plugin Configuration Guide](https://docs.forescout.com/bundle/web-api-1-5-4-h/page/c-about-eyeextend-connect-module-web-api.html).
</Callout>

## Assets Types Fetched

* Devices
* Software
* SaaS Applications

## Before You Begin

### Authentication Methods

The adapter supports the following authentication method to establish a connection:

* User credentials - This method requires a Username and Password associated with an account that has the required permissions to access the ForeScout CounterACT XML or REST APIs.
* API key - In environments where the ForeScout Web API is utilized, an API key (also referred to as a Client ID) is required to authenticate requests.

### Required Permissions

The user account that is supplied in [User Name](#connection-parameters) must have permissions to use the API. For more information, see the ForeScout <Anchor label="Web API Plugin Configuration Guide" target="_blank" href="https://docs.forescout.com/bundle/web-api-1-5-4-h/page/t-configure-web-api-plugin.html">Web API Plugin Configuration Guide</Anchor>.

### APIs

Axonius uses the following APIs to retrieve asset data:

* [Forescout eyeExtend Connect Module: Web API](https://docs.forescout.com/bundle/web-api-1-5-4-h/page/t-configure-web-api-plugin.html)
* [Forescout Admin API](https://docs.forescout.com/bundle/admin-api/page/index.html#/Segments/getSegments)

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **ForeScout CounterACT Domain** - The URL for the ForeScout CounterACT domain.
2. **User Name** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

<Image align="center" alt="ForeScout CounterAct adapter - Add Connection" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/ForeScout_CounterACT_Add_Connection.png" className="border" />

### Optional Parameters

<Callout icon="📘" theme="info">
  Note

  The following **Admin API** configuration settings are necessary if you want to <Anchor label="fetch device segments from the Admin API" target="_blank" href="/docs/forescout-counteract#advanced-settings">fetch device segments from the Admin API</Anchor>.
</Callout>

1. **Admin API User Name** - Enter the ForeScout Admin API user name.
2. **Admin API Password** - Enter the ForeScout Admin API password.
3. **Admin API Client ID** - Enter the ForeScout Admin API Client ID.
4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
5. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Do not fetch devices with no MAC address and no hostname** - Select whether to exclude fetching devices without MAC address and without hostname.
2. **Do not fetch devices with no IP** - Select whether to exclude fetching devices without an IP address.
3. **Ignore irrelevant device manufacturers** - Select this option to ignore the device manufacturer field.
4. **Number of parallel requests** *(required, default: 10)* - Set the number of parallel requests this adapter connection will send in parallel to the ForeScout CounterACT server at any given point.
5. **Re-authenticate after every X requests** *(required, default: 100)* - Set the number of requests to allow before attempting to re-authenticate to get a new session token.
6. **List of fields to be used for device "Last Seen"** *(optional)* -  Enter a list of field names to be used for determining the device's 'Last Seen' value. Items positioned earlier in the list take precedence over others. For example, if you enter `online_va` and then `online`:
   * The adapter first searches for `online_va` in the device fields.
   * If the field name is found, the 'Last Seen' value is the timestamp for `online_va`.
   * If the field name is not found, the adapter searches for `online` in the device fields.
   * If the field name is found, the 'Last Seen' value is the timestamp for `online`.
   * If none of the field names are found, or if the list is empty (the default state), the 'Last Seen' value is the maximum timestamp from all the device fields (previously existing logic).
7. **Use Azure Instance ID for Cloud ID** - Select to set the device's Cloud ID field with the value of the Azure Instance ID field.
8. **Fetch device segments from Admin API** - Select this option to fetch device segments using ForeScout Admin API. Make sure to fill in the ForeScout Admin API User Name, Password, and Client ID parameters in order to use this setting.
9. **Mapping of script results to aggregated fields** - Click the + symbol to open the **Script Result Field** and the **Aggregated Field**.
   * **Script Result Field** - Enter the script result field name. The script result field name can be found in the advanced view for devices. For example: `script_result.1a2b3c4d5e`
   * **Aggregated Field** - Enter the device field name as it appears in the Axonius query. For example, if you want the script result to be parsed to the device serial, insert `device_serial` in the text box.
10. **Preferred fields for device Host Name parsing** - Select the preferred fields to be used to parse the device hostname. The adapter checks each preferred field in turn and assigns the device hostname to the first non-empty value it finds.

<br />