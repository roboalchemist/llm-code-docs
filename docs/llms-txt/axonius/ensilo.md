# Source: https://docs.axonius.com/docs/ensilo.md

# FortiEDR (enSilo)

FortiEDR (formerly enSilo) automates and orchestrates detection, prevention, and response against malware and ransomware.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Ensilo Domain** *(required)* - The enSilo domain URL (e.g. https\://your\_bomgar\_domain.com).
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![FortiEDR.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FortiEDR\(2\).png)

## APIs

Axonius uses the [Fortinet Endpoint Protection and Response Platform RESTful API](https://fortinetweb.s3.amazonaws.com/docs.fortinet.com/v2/attachments/df7ab511-7435-11ea-9384-00505692583a/API_Guide_V4.1.pdf).

## Required Permissions

The value supplied in [User Name](#parameters) must have “Rest API” permissions to fetch assets.
Refer to Authorization in [Fortinet Endpoint Protection and Response Platform RESTful API](https://fortinetweb.s3.amazonaws.com/docs.fortinet.com/v2/attachments/df7ab511-7435-11ea-9384-00505692583a/API_Guide_V4.1.pdf) for full details of how to create user authorization.