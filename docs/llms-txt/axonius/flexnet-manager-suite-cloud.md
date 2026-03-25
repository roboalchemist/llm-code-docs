# Source: https://docs.axonius.com/docs/flexnet-manager-suite-cloud.md

# FlexNet Manager Suite Cloud

FlexNet Manager Suite Cloud from Flexera is a SaaS offering for software license compliance and license optimization.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Software
* Licenses
* SaaS data

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname of the FlexNet Manager Suite Cloud server's API. For North America, use *api.flexera.com*. For EU, use *api.flexera.eu*.

<Callout icon="📘" theme="info">
  Note

  The  **Authentication URL** (login.flexera.com) and **Host Name** must be added to an  "Allow list" for firewall rules.
</Callout>

2. **Refresh Token** *(required)* - Access token obtained from Flexera IAM associated with an admin user.

3. **Organization ID** *(required)* - Organization ID provided by Flexera, that defines the organization.

4. **Verify SSL** - Select to verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **Use EU Domain for Authentication Token** *(optional)* - Select to authenticate to the EU domain required to access the API. When cleared, Axonius authenticates to the US domain.

9. **API Gateway Connection *(optional)*** - Enable this to use API gateway parameters for authentication. After enabling this option, under API Gateway Type, choose Layer7 and fill in the parameters that are displayed (in addition to **Host Name or IP Address**). Read about [Layer7 API Gateway Parameters](/docs/adding-a-new-adapter-connection#layer7-api-gateway-parameters).

<Callout icon="📘" theme="info">
  Note

  When you use an API gateway connection, the other authentication parameters are not required. However, to add the connection successfully, you need to enter placeholder values in these fields.
</Callout>

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![flexnet](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-DCRG5LGK.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Device type include list** *(optional)* - Enter a comma-separated list of device types to include in the fetch. If not specified, this adapter will fetch all device types.

2. **Inventory status exclude list** *(optional)* - Enter a comma-separated list of inventory status types to exclude from the fetch. If not specified, this adapter will fetch all types of inventory status.

3. **Pagination page limit** *(required, default: 200)* - Enter the maximum number of results fetched per page.

4. **Fetch software** *(optional, default: true)* - Select to fetch Information about software assets.

5. **Enrich Flexera device Software with ServiceNow data** *(optional, default: false)* - Select this option to enrich devices fetched by FlexNet with software data fetched from the [ServiceNow](/docs/servicenow) adapter. From the **Value** dropdown, select the ServiceNow connection ID to use. Note that to successfully enable this, you must configure a ServiceNow adapter connection and enable the following ServiceNow advanced configuration: *Fetch "cmdb\_software\_product\_model" table for Various Software enrichment*.

6. **Fetch licenses (only SM)**  *(only for accounts with Axonius SaaS Applications)* - Select this option to fetch licenses.

7. **Fetch Software Technopedia** - Select this option to fetch Software Technopedia fields.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [IT Asset Management Data API](https://fnms-data-api-docs.s3.amazonaws.com/index.html).

## Permissions

The following permissions are required:

* fnms:device:create||common:org:own: Allows creating file containing active devices with installed software
* fnms:file:show||common:org:own: Allows getting pre-signed URL to download a file
* fnms:asset:index||common:org:own: Allows listing assets
* fnms:license:index||common:org:own: Allows listing license attributes and entitlements
* fnms:inventory:index||common:org:own: Allows listing inventories
* fnms:operator:index||common:org:own: Allows listing accounts