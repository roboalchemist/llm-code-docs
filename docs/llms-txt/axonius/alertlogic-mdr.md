# Source: https://docs.axonius.com/docs/alertlogic-mdr.md

# Alert Logic MDR

Alert Logic delivers managed detection and response (MDR) with comprehensive coverage for public clouds, SaaS, on-premises, and hybrid environments.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Aggregated Security Findings, SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.cloudinsight.alertlogic.com`)* - The Alert Logic server.
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.  You can also use Access Key and Secret Key authentication. To do this, enter the  Access Key into the User name field and the Secret Key into the password field.
3. **Is Parent Account** *(required, default: false)* - Select to designate the account as a Parent account in which the devices of each child account belonging to the Parent account are fetched. When cleared (default), the account is considered a Child account in which only the devices of the particular account are fetched.
4. **Verify SSL** *(required, default: false)* - Select to verify the SSL certificate offered by the value supplied in **Alert Logic Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-amp-ca-settings).
5. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Alert Logic Domain**.
   * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **Alert Logic Domain**.
   * If not supplied, Axonius will connect directly to the value supplied in **Alert Logic Domain**.
6. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Alert Logic Domain** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
7. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the value supplied in **Alert Logic Domain** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
8. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="AlertLogicMDR\(1\)" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AlertLogicMDR(1).png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  From version 4.6, Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

* **Fetch Exposures** *(required, default: false)* - Select whether to fetch exposures data (vulnerabilities) for each device.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Alert Logic Cloud Insight API](https://console.account.alertlogic.com/users/api/index.html#/).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 8080/443**

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| V1      | Yes       |       |

## Supported From Version

Supported from Axonius version 4.5