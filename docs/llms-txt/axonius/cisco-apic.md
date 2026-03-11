# Source: https://docs.axonius.com/docs/cisco-apic.md

# Cisco Application Policy Infrastructure Controller (APIC)

Cisco Application Policy Infrastructure Controller (APIC) is the main architectural component of Cisco ACI. It is the unified point of automation and management for the Cisco ACI fabric, policy enforcement, and health monitoring and optimizes performance and agility.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Cisco APIC server.

2. **Authentication Domain**  *(optional)* - An alternative domain to be used for authentication. If empty, the DefaultAuth domain will be used. If you are authenticating with a Cisco APIC local user account, configure the Authentication Domain with the value “apic#fallback”, or the domain that is configured in the Cisco APIC web interface for local user accounts. If the connection fails with that setting, make sure that 'Fallback Domain Availability' is set to “Always Available” on the Cisco APIC web interface.

   ![CiscoAPICAuth](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CiscoAPICAuth.png)

3. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![CiscoAPICNew2](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CiscoAPICNew2.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch sensors** - Select this option to fetch data about sensors for each device

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Operating Cisco Application Centric Infrastructure API](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/aci/apic/sw/1-x/Operating_ACI/guide/b_Cisco_Operating_ACI/b_Cisco_Operating_ACI_appendix_011.html)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Required Permissions

APIC role-based access control is required for the value supplied in [User Name](#parameters): read-only, or read-write

## Supported From Version

Supported from Axonius version 4.5