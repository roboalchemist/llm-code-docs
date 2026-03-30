# Source: https://docs.axonius.com/docs/adp.md

# ADP

ADP  (Workforce) is a provider of human resources management software and services.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the ADP server.

2. **Client ID** and **Client Secret** *(required)* - The Client ID and Secret you received from ADP. Please note that you need to contact your ADP representative to receive the Client ID and Client Secret.

3. **Certificate File** *(required)* - The ADP issued certificate file (.CRT file). For more detailed information, see [Generating a Certificate Signing Request](https://developers.adp.com/articles/general/generate-a-certificate-signing-request).

4. **Key File** *(required)* - The .KEY file created as part of the CSR process. For more detailed information, see [Generating a Certificate Signing Request](https://developers.adp.com/articles/general/generate-a-certificate-signing-request).

5. **Verify SSL** *(required, default: False)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional, default: empty)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the server using the **HTTPS Proxy**.

9. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](https://docs.axonius.com/docs/adding-a-new-adapter-connection#/).

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1633).png" />

## APIs

Axonius uses the [ADP API Version 2](https://developers.adp.com/).