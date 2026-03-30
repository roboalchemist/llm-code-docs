# Source: https://docs.axonius.com/docs/teleport.md

# Teleport

Teleport is an open-source tool that provides access to servers and cloud applications using SSH, Kubernetes and HTTPS.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the \[ADAPTER NAME] server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **User Name** and **Password** *(required)* - The credentials for a user account that has  permission to fetch assets.

3. **Certificate File** *(optional)* - Upload the certificate file containing the public key for the keypair being used to authenticate.

4. **Key File** *(optional)* - Upload the key file for the certificate being used to authenticate.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-K32YVC2I.png" />

## APIs

Axonius uses the <Anchor label="Teleport API" target="_blank" href="https://goteleport.com/docs/zero-trust-access/api/">Teleport API</Anchor>.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1