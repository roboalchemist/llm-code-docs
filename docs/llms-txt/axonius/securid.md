# Source: https://docs.axonius.com/docs/securid.md

# RSA SecurID

RSA SecurID provides identity and access management capabilities for on-premise deployments – in authentication, access management, and identity governance.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the RSA SecurID server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Port** *(required, default: 5555)* - The port used for the connection.

3. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.
   To obtain an API Key, login to the <Anchor label="Cloud Administration Console" target="_blank" href="https://access.securid.com/AdminInterface/login">Cloud Administration Console</Anchor> with Super Admin credentials. Then select **My Account** `>` **Company Settings** `>` **Authentication API Keys**.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="RSASEcureID" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RSASEcureID.png" />

## APIs

Axonius uses the [SecurID Authentication API](https://community.rsa.com/t5/securid-cloud-authentication/securid-authentication-api-developer-s-guide/ta-p/568534).
The API domain is local on the client.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 80**
* **TCP port 443**

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| v1      | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.7