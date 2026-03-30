# Source: https://docs.axonius.com/docs/citrix-daas.md

# Citrix DaaS

Citrix DaaS (device as a service) is a cloud-based solution that allows companies to securely deliver DaaS and VDI apps and desktops to any device, over any network.

## Asset Types Fetched

* Devices, Application Settings, Users, Groups

## Before You Begin

**Ports**

* **TCP port 80**
* **TCP port 443**

### APIs

Axonius uses the following APIs:

* [Citrix DaaS REST APIs](https://developer.cloud.com/citrixworkspace/citrix-daas/citrix-daas-rest-apis/docs/citrix-daas-apis)
* [Citrix Cloud API](https://developer.cloud.com/citrix-cloud/citrix-cloud-api-overview/docs/get-started-with-citrix-cloud-apis)

### Permissions

Refer to [Citrix DaaS documentation](https://docs.citrix.com/en-us/citrix-daas) for information about the Profiles and Permissions required to fetch assets.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - Enter the endpoint of your Citrix Cloud region that Axonius can communicate with via the [Required Ports](#required-ports).

| Citrix Cloud Region | Endpoint                                                 |
| ------------------- | -------------------------------------------------------- |
| US                  | [https://api-us.cloud.com](https://api-us.cloud.com)     |
| EU                  | [https://api-eu.cloud.com](https://api-eu.cloud.com)     |
| AP-S                | [https://api-ap-s.cloud.com](https://api-ap-s.cloud.com) |
| JP                  | [https://api.citrixcloud.jp](https://api.citrixcloud.jp) |

2. **Customer ID** - The customer ID (CCID) for a user account that has the permissions to fetch assets.

3. **Client ID** and **Client Secret** - The credentials for a user account that has the permissions to fetch assets.

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Citrix_DaaS.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
5. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

**Fetch Settings** *(only available for customers who have Axonius SaaS Applications)* - Select this option to fetch Application Settings. This will also make the adapter fetch Users and Groups data.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| v1      | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.7