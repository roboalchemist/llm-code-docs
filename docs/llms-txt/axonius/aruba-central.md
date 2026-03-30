# Source: https://docs.axonius.com/docs/aruba-central.md

# HPE Aruba Networking Central

HPE Aruba Networking Central is a unified cloud-based network operations, assurance and security platform that simplifies the deployment, management, and optimization of wireless, wired and WAN environments.

<Callout icon="📘" theme="info">
  Note

  Due to changes that were made to the vendor’s API, it’s paramount that you change the value in [Advanced Settings → Adapter Configuration](/docs/advanced-settings#wait-for-a-connection-to-the-source-for-up-to-x-seconds)→ 'Wait for a connection to the sources for up to X seconds' to *3000*.
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Region** *(required)* - Select the region corresponding to the domain name. The value must match the **My Zone** value, which can be viewed under the User Settings in HPE Aruba Networking Central. The selected regions map to the following domain URLs:

| Region      | Domain Name                                          |
| ----------- | ---------------------------------------------------- |
| US-1        | `https://app1-apigw.central.arubanetworks.com`       |
| US-2        | `https://apigw-prod2.central.arubanetworks.com`      |
| US-WEST-4   | `https://apigw-uswest4.central.arubanetworks.com`    |
| EU-1        | `https://eu-apigw.central.arubanetworks.com`         |
| EU-3        | `https://apigw-eucentral3.central.arubanetworks.com` |
| Canada-1    | `[https://apigw-ca.central.arubanetworks.com`        |
| China-1     | `https://apigw.central.arubanetworks.com.cn`         |
| APAC-1      | `https://api-ap.central.arubanetworks.com`           |
| APAC-EAST1  | `https://apigw-apaceast.central.arubanetworks.com`   |
| APAC-SOUTH1 | `https://apigw-apacsouth.central.arubanetworks.com`  |

2. **Custom Region** *(optional)* - If you want to select a region not listed in the **Region** dropdown list:
   1. From the **Region** dropdown list, select **CUSTOM**.
   2. From the **Custom Region** parameter, specify the domain name.
3. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.
4. **Customer ID** *(required)* - The Customer ID value is obtained from the User Settings in HPE Aruba Networking Central.
5. **Client ID** and **Client Secret** *(required)* - The Client ID and Client Secret is obtained from the application created. For more details, see [Creating Application & Token](https://developer.arubanetworks.com/hpe-aruba-networking-central/docs/api-gateway-creating-application-token).

<Callout icon="📘" theme="info">
  Note

  If you are working with a version of HPE Aruba Networking Central that is greater than 2.5.5, the credentials used in the adapter must be a local account or outside of the SAML domain, since SAML users cannot generate tokens via the API. Refer to [HPE Networking Support Portal](https://networkingsupport.hpe.com/) for further information.
</Callout>

6. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

7. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

8. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

9. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="ArubaCentral" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ArubaCentral.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Devices type to fetch** *(required, default: Access Point, Switch)* - Select multiple types of devices to fetch, including wired and wireless clients.
2. **Fetch clients (Wired/Wireless) as network devices** - Select this option to fetch clients as network devices.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [HPE Aruba Networking Central API](https://developer.arubanetworks.com/hpe-aruba-networking-central/docs/api-reference-guide).