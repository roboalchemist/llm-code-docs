# Source: https://docs.axonius.com/docs/intruder-io.md

# Intruder.io

Intruder is an online vulnerability scanner that enables the identification of misconfigurations, missing patches, encryption weaknesses, application bugs, and more.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
  , Aggregated Security Findings
  , SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Intruder.io server.

2. **Access Token** *(required)* - An Access Token associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Intruder.io" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Intruder.io.png" />

## APIs

Axonius uses the [ Intruder.io Pagination API](https://developers.intruder.io/docs/pagination)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Required Permissions

The value supplied in [Access Token](#parameters) must be associated with credentials that have Read Only  permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 4.8