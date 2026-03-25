# Source: https://docs.axonius.com/docs/entrust.md

# Entrust

Entrust provides identity, payment, and data security solutions.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Certificates

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Entrust server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Certificate File** *(required)* - Upload the certificate file containing the public key for the keypair being used to authenticate.

3. **Certificate Key File** *(required)* - Upload the certificate key file for the certificate being used to authenticate.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Entrust](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Entrust.png)

## APIs

Axonius uses the [Entrust API](https://api.managed.entrust.com/doc/#operation/caList).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

Read permissions are required in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.0