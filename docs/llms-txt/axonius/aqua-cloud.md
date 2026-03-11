# Source: https://docs.axonius.com/docs/aqua-cloud.md

# Aqua Security (SaaS)

Aqua Security provides container and cloud native cybersecurity for teams using Docker, Kubernetes, serverless, and other cloud native technologies.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Aqua Security server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** and **API Secret** *(required)* - An API Key associated with a user account that has Permission to fetch assets.

3. **API Roles** *(optional)* - The Aqua role(s) that are associated with the token. Use commas to specify more than one.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Aqua Security (SaaS)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Aqua%20Security%20\(SaaS\).png)

## APIs

Axonius uses the [Aqua Platform SaaS Authentication API](https://docs.aquasec.com/saas/api-reference/getting-started-with-aqua-platform-apis/api-authentication/#authentication-endpoint).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Supported From Version

Supported from Axonius version 6.1