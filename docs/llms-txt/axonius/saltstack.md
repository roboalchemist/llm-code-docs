# Source: https://docs.axonius.com/docs/saltstack.md

# SaltStack Open Source

SaltStack Open Source is open-source software for event-driven security, cloud and configuration management.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **SaltStack Open Source Domain** *(required)* - The domain for the SaltStack Open Source server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** *(required)* - The credentials for a user account that has  permission to fetch assets.

3. **Eauth** - The eauth backend configured for the user.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![SaltStack Open Source.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SaltStack%20Open%20Source.png)

## APIs

Axonius uses the [REST API for Salt](https://docs.saltproject.io/en/latest/ref/netapi/all/salt.netapi.rest_cherrypy.html).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 4.6