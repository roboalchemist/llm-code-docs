# Source: https://docs.axonius.com/docs/netshot.md

# Netshot

Netshot is a network automation and configuration management tool that provides network device backup, compliance checks, and configuration changes.

The Netshot adapter enables Axonius to fetch and catalog network devices, providing visibility into their inventory details and configuration compliance.

## Asset Types Fetched

* Devices, Groups

## Before You Begin

### Required Ports

* TCP port 80/443

### Authentication Methods

* API Key

### Permissions

The value supplied in [API Key](#required-parameters) must be associated with credentials that have Read Only permissions in order to fetch assets.

### APIs

Axonius uses the <Anchor label="Netshot REST API" target="_blank" href="https://github.com/netfishers-onl/Netshot/wiki/Using-the-REST-API">Netshot REST API</Anchor> to retrieve asset data.

### Supported From Version

Supported from Axonius version 6.1.33.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** - Enter the hostname or IP address of the Netshot server.

2. **API Key** - Enter the API key associated with a user account that has permissions to fetch assets. For more information on how to generate the API key, see [Authentication](https://github.com/netfishers-onl/Netshot/wiki/Using-the-REST-API#authentication).

![Netshot.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Netshot.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

5. **API Gateway Connection** - Enable this to use API gateway parameters for authentication. After enabling this option, under **API Gateway Type**, choose Layer7 and fill in the parameters that are displayed (in addition to **Host Name or IP Address**). Read about [Layer7 API Gateway Parameters](/docs/adding-a-new-adapter-connection#layer7-api-gateway-parameters).

   <Callout icon="📘" theme="info">
     Note

     When you use an API gateway connection, the other authentication parameters are not required. However, to add the connection successfully, you need to enter placeholder values in these fields.
   </Callout>

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Enrich Devices List Endpoint with Device Details Endpoint** – Select this option to enrich each device from the Devices List endpoint with data from the Netshot Device Details endpoint.
2. **Enrich Device Details Endpoint with Device Compliance Endpoint** – Select this option to correlate and enrich the device inventory with compliance status data.
3. **Fetch Compliance Findings from Device Compliance Endpoint** – Select this option to retrieve granular compliance findings (specific rule passes/failures) associated with the devices.
4. **Fetch Groups from Device Groups Endpoint** - Select this option to fetch device groups from the Device Groups endpoint and thus create Group assets.