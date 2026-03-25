# Source: https://docs.axonius.com/docs/tripwrie-enterprise.md

# Tripwire Enterprise

Tripwire Enterprise is a security configuration management (SCM) suite that provides fully integrated solutions for policy, file integrity, and remediation management. This adapter connects to the Tripwire Enterprise management server to import information about devices that are managed by that solution.

## Types of Assets Fetched

* Devices
* Software
* SaaS Applications
* Databases

## Parameters

1. **Tripwire Domain** *(required)* - The hostname or IP address of the Tripwire Enterprise server.

2. **User Name** and **Password** *(required)* - The username and password for an account that has read access to the API.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![tripwire.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/tripwire.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection,  refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Apps element names** - Enter a comma-separated string of element names. For each element name the adapter fetches the device apps using the endpoint "versions/latest?elementName=`{element_name}`".
2. **Node types to fetch** - Select one or more node types to fetch from.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the Tripwire API.

## Required Permissions

The value supplied in [**User Name** and **Password**](#parameters) must have Read-only permissions to fetch assets.

Use the Swagger to test whether the user-password pair you created has the right permissions assigned. The URL for you to test is: `YOUR TRIPWIRE SERVER.domain.com/api`