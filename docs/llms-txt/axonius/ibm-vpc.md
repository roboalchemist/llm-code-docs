# Source: https://docs.axonius.com/docs/ibm-vpc.md

# IBM VPC

IBM Cloud Virtual Private Cloud (VPC) is a secure software-defined network (SDN) on which customers can build isolated private clouds.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the IBM Virtual Private Cloud server.

2. **Token Host Name or IP Address** *(required, default: `https://iam.cloud.ibm.com`)* -  Address that the adapter uses for acquiring the token. A default value is supplied. If necessary a different address can be entered.

3. **API Key** *(required)* - An API Key associated with a user account that has permissions in order to fetch assets. Learn more about [the API Key](https://cloud.ibm.com/apidocs/vpc/latest#api-authentication).

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![IBMVirtualPrivateCloud](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IBMVirtualPrivateCloud.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

The adapter only fetches VPCs by default. Use the following settings to select which additional assets to fetch (for instance instance, load balancers). The IBM IAM must be enabled accordingly for each additional asset. Click the plus icon to add another setting.

1. **VPC Fetching Configuration**  - Configure whether to add the following to VPC fetches:
   * **List all address prefixes**

   * **List all routing tables**.
2. **Additional Fetching Configuration**   - Configure whether to add the following to  fetches:
   * Instances
   * Network ACLs
   * Images
   * Subnets
   * Snapshots
   * Columnes
   * Load Balaners
   * Security Groups
   * Floating IPs

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [IBM Virtual Private Cloud API](https://cloud.ibm.com/apidocs/vpc/latest)

## Supported From Version

Supported from Axonius version4.8