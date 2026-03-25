# Source: https://docs.axonius.com/docs/entrust-certificate-hub.md

# Entrust Certificate Hub

Entrust Certificate Hub is a centralized platform for managing digital certificates across various environments, automating certificate lifecycle management, and providing visibility into security compliance.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Certificates

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Entrust Certificate Hub server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Token** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  The CertHub API uses bearer token based authentication. You create your token using the CertHub UI API Tokens page.
</Callout>

9. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

10. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

11. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

12. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Entrust Certificate Hub](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Entrust%20Certificate%20Hub.png)

## APIs

Axonius uses the CertHub API.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1.33.0