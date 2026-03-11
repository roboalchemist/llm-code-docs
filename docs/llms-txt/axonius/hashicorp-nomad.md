# Source: https://docs.axonius.com/docs/hashicorp-nomad.md

# HashiCorp Nomad

HashiCorp Nomad deploys new and legacy applications across multiple datacenters, regions, and clouds.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the HashiCorp Nomad server.

2. **Nomad Token** *(required)* - A Token that can be used to fetch assets. When ACLs are enabled, a Nomad token is provided to API requests using the X-Nomad-Token header or with the bearer scheme in the authorization header. When using authentication, clients should communicate via TLS.

3. **User Name** and **Password** *(required)* - The credentials for a user account that has  permission to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![HashiCorpNomad](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HashiCorpNomad.png)

## APIs

Axonius uses the [Nomad API](https://developer.hashicorp.com/nomad/api-docs).

## Supported From Version

Supported from Axonius version 6.0