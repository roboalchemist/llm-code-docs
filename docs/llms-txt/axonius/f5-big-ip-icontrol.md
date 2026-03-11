# Source: https://docs.axonius.com/docs/f5-big-ip-icontrol.md

# F5 BIG-IP iControl

F5 BIG-IP iControl is a Web services-enabled open API providing granular control over the configuration and management of F5's application delivery platform, BIG-IP.

F5 BIG-IP iControl provides information on virtual servers and their assigned pools.

A pool is a logical set of devices, such as web servers, that you group together to receive and process traffic. Instead of sending client traffic to the destination IP address specified in the client request, F5 BIG-IP sends the request to any of the nodes that are members of that pool.

A pool consists of pool members. A pool member is a logical object that represents a physical node on the network. Once you have assigned a pool to a virtual server, F5 BIG-IP directs traffic coming into the virtual server to a member of that pool. An individual pool member can belong to one or multiple pools, depending on how you want to manage your network traffic.

For more details on pools, see [Ask F5 - About Pools](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/ltm-basics-11-6-0/4.html).

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Domains & URLs, Compute Services, Load Balancers, Certificates, Network/Firewall Rules, Application Resources

## Parameters

1. **F5 BIG-IP Domain** - Your F5 BIG-IP domain.
2. **User Name** and **Password** - Provide the user name and password for a read-only user.
3. **Login Provider** - Use "tmos".
4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="F5 BIG-IP iControl" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/F5%20BIG-IP%20iControl.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch devices configuration** - Select whether to fetch [Device configuration information](https://clouddocs.f5.com/api/icontrol-rest/APIRef_tm_cm_device.html) as devices.
2. **Fetch virtual servers policies** - Select to fetch policy information for each virtual server. When this is enabled, F5 Firewall Security Rules are fetched and parsed as Network/Firewall Rules.
3. **Enrich policies with ASM context elements** - Select this option to enrich the policies objects with the following ASM context elements:  Cookies, Methods, File Types, Violations, Evasions, HTTP Protocols, Web Services Securities, Signatures.
4. **Fetch NAT rules** - Select this option to fetch the NAT rules from F5 iControl REST and associate them with the Virtual Servers.
5. **Fetch GTM (Global Traffic Management) assets** - Select this option to fetch GTM WideIPs, GTM Pools, and GTM Servers.
6. **API version to use (e.g. 13.1.1)** - Enter the F5 API version to use. If not specified, the latest API version is used. For backwards compatibility it may be useful to set an older API version.
7. **Fetch SSL certificates and profiles** -Select this option to fetch SSL Client Profiles as Application Resources and SSL Certificates as Certificates.
8. **Merge Load Balancer HA Pairs** - Select this option to fetch HA Virtual Servers as Load Balancer assets.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Authentication with the F5 REST API](https://clouddocs.f5.com/api/icontrol-soap/Authentication_with_the_F5_REST_API.html).

* Read more about the virtual server at [APIRef\_tm\_ltm\_virtual](https://clouddocs.f5.com/api/icontrol-rest/APIRef_tm_ltm_virtual.html).
* Read more about the load balancing pool configuration at [APIRef\_tm\_ltm\_pool](https://clouddocs.f5.com/api/icontrol-rest/APIRef_tm_ltm_pool.html).

## Required Permissions

The value supplied in [User Name](#parameters) must match the reader role called `Auditor`.