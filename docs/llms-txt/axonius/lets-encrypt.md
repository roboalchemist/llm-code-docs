# Source: https://docs.axonius.com/docs/lets-encrypt.md

# Let's Encrypt

Let's Encrypt is a non-profit certificate authority run by Internet Security Research Group that provides X.509 certificates for Transport Layer Security encryption at no charge.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Certificates

## Parameters

1. **LetsEncrypt Account Private Key File** *(required)* - Click **Upload File** to upload the  private key certificate, used for authentication.

2. **Private Key Password** *(optional)* - Enter the password for the **LetsEncrypt Account Private Key File**, if it is password protected.

3. **Certificate Authority Directory** *(required, default: `https://acme-v02.api.letsencrypt.org`)* - The domain of your source of Certificates.

4. **User Contact Details** *(required)* - Enter your user account details (e.g. mailto:[aaa@bbb.com](mailto:aaa@bbb.com)) for your account-key.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Lets Encrypt.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Lets%20Encrypt.png)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1.62