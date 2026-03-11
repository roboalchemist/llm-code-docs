# Source: https://docs.axonius.com/docs/dell-techdirect.md

# Dell TechDirect

Dell TechDirect is a centralized portal for managing the deployment and configuration of Dell EMC products.

The Dell TechDirect adapter enables Axonius to fetch and catalog warranty and service entitlement information for Dell hardware assets, ensuring accurate lifecycle management and support coverage visibility.

## Asset Types Fetched

* Devices

## Before You Begin

### Authentication Methods

The adapter uses a **Client ID** and **Client Secret** for authentication with the hostname or IP address.

### Required Permissions

The **Client ID** and **Client Secret** must be authorized for the **Warranty API** within the <Anchor label="Dell TechDirect portal" target="_blank" href="https://tdm.dell.com/portal">Dell TechDirect portal</Anchor>.

### APIs

Axonius uses the <Anchor label="TechDirect API" target="_blank" href="https://www.dell.com/support/contents/en-us/article/product-support/self-support-knowledgebase/technologies-and-tools/techdirect/self-dispatch-and-apis">TechDirect API</Anchor> to retrieve asset data.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** *(default: `apigtwpc2.us.dell.com`)* - Enter the hostname or IP address of the Dell TechDirect server.

2. **Client ID** and **Client Secret** - Enter the credentials for a user account that has permission to fetch assets.

3. **Service Tags** - Enter a single or multiple service tags separated by commas.

<Image alt="Dell TechDirect.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DEll%20TechDirect.png" />

### Optional Parameters

1. **Service Tags File** - Upload a file with service tags. Each new row in the file is a tag. The adapter uses these tags in the file and in the **Service Tags** field.

2. **Service Tag CSV Column Header** - Enter a column header for the Service Tag CSV file. When you enter a column header the adapter tries to load service tags from the column with this header in the CSV file that is uploaded in the **Service Tags** file field. If you do not enter a value in this field, the adapter assumes the file only consists of tags separated by line (the file does not have to be a CSV file).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Parse Entitlement With Latest End Date** - Select this option to configure the adapter to parse the entitlement with the latest end date. If this option is disabled, the adapter parses all the entitlements found.