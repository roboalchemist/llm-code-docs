# Source: https://docs.axonius.com/docs/alibaba-cloud.md

# Alibaba Cloud

Alibaba Cloud provides cloud computing services and cloud Infrastructure as a service.

The Alibaba Cloud adapter enables Axonius to fetch and catalog cloud infrastructure assets, including compute instances and user identities, ensuring comprehensive visibility into your Alibaba Cloud environment.

## Asset Types Fetched

* Devices
* Users

## Before You Begin

### Required Ports

* TCP port 443

### Authentication Methods

* Alibaba Access Key ID
* Alibaba Access Key Secret

### Required Permissions

The **Access Key ID** and **Access Key Secret** used for the connection must be associated with a user that has read permissions to the resources that you want to fetch.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Region ID** - Specify a region ID based on the geographic location of your business operation. For the complete list of region IDs, see <Anchor label="Alibaba Cloud Help Center - Regions and Zones" target="_blank" href="https://www.alibabacloud.com/help/doc-detail/40654.htm">Alibaba Cloud Help Center - Regions and Zones</Anchor>.

   <Callout icon="📘" theme="info">
     Note

     You can enter multiple region IDs separated by commas.
   </Callout>
2. **Alibaba Access Key ID** and **Alibaba Access Key Secret** - Specify your account access key ID and secret, which you can get by doing as follows:
   1. Log on to the Alibaba Cloud console.
   2. At the upper-right corner, hover the cursor over the username, and select **Access Keys** from the shortcut menu that appears.
   3. In the security prompt box, click **Continue** to manage the Access Key. The Access Key ID and Access Key Secret are displayed.

<Image align="center" alt="Alibab Cloud - Add Connection" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Alibaba_Cloud_Add_.png" className="border" />

### Optional Parameters

1. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

* **Fetch Users** - Select this option to fetch users. Note that the region must be in the supported regions of a CloudSSO directory (listed <Anchor label="here" target="_blank" href="https://www.alibabacloud.com/help/en/cloudsso/product-overview/sso-region-description">here</Anchor>) and CloudSSO must be activated for the Alibaba account in that region.