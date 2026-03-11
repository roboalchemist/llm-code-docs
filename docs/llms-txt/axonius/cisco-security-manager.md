# Source: https://docs.axonius.com/docs/cisco-security-manager.md

# Cisco Security Manager

Cisco Security Manager provides policy enforcement and rapid troubleshooting of security events, offering summarized reports across the security deployment.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Cisco Security Manager server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1486\).png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Async chunks in parallel** *(required, default: 50)* - Specify the number of parallel requests all connections for this adapter will send to the Cisco Security Center server in parallel at any given point.

<Callout icon="📘" theme="info">
  NOTE

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Cisco Security Manager API Version 2.4](https://www.cisco.com/c/dam/en/us/td/docs/security/security_management/cisco_security_manager/security_manager/417/API/CSM-API-Spec-v24.pdf).

* The API is licensed. A specific CSM API license must be applied via the **CSM Tools** `>` **Security Manager Administration** `>` **Licensing** page. For details, see the [Cisco Security Manager 4.17 API Sepcification (Version 2.4) - section 1.11](https://www.cisco.com/c/dam/en/us/td/docs/security/security_management/cisco_security_manager/security_manager/417/API/CSM-API-Spec-v24.pdf).
* There are a few prerequisites to use and work with the API. For details, see the [Cisco Security Manager 4.17 API Sepcification (Version 2.4) - section 1.12](https://www.cisco.com/c/dam/en/us/td/docs/security/security_management/cisco_security_manager/security_manager/417/API/CSM-API-Spec-v24.pdf).
* It is required to enable the API service from the global administration settings. For details, see the [Cisco Security Manager 4.17 API Sepcification (Version 2.4) - section 1.13](https://www.cisco.com/c/dam/en/us/td/docs/security/security_management/cisco_security_manager/security_manager/417/API/CSM-API-Spec-v24.pdf).

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version                     | Supported | Notes |
| --------------------------- | --------- | ----- |
| Cisco Security Manager 4.17 | Yes       |       |