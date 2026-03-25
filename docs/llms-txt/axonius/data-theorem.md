# Source: https://docs.axonius.com/docs/data-theorem.md

# Data Theorem

Data Theorem is an application security platform focusing on API Security, Web Security, Mobile Security, and Cloud Security.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Data Theorem server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. For information about the API Key, see [Authentication](https://docs.securetheorem.com/api_security_results/overview.html#/).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Data Theorem](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Data%20Theorem.png)

## APIs

Axonius uses the [Data Theorem API Security Results API](https://docs.securetheorem.com/api_security_results/overview.html).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1.32.1