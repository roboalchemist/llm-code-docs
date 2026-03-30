# Source: https://docs.axonius.com/docs/cisco-secure-workload.md

# Cisco Secure Workload (Formerly Tetration)

Cisco Secure Workload (formerly Tetration) is a microsegmentation platform that offers zero trust-based workload protection for multi cloud data centers.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Cisco Secure Workload server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key and Secret** *(required)* - An API Key and Secret associated with a user account that has permissions to fetch assets. For details, see [Generate API Key and Secret](https://www.cisco.com/c/en/us/td/docs/security/workload_security/secure_workload/user-guide/3_7/cisco-secure-workload-user-guide/openapi.html#task_911065).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![CiscoSecureWorkload\_Adapter](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CiscoSecureWorkload_Adapter.png)

## APIs

Axonius uses the [Cisco Secure Workload REST API Version 1.0](https://www.cisco.com/c/en/us/td/docs/security/workload_security/secure_workload/user-guide/3_7/cisco-secure-workload-user-guide/openapi.html).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**