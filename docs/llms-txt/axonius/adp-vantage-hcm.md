# Source: https://docs.axonius.com/docs/adp-vantage-hcm.md

# ADP Vantage HCM

ADP Vantage HCM is an all-in-one HR platform that includes payroll, benefits, and talent management administration.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the ADP Vantage server.

2. **Client ID** and **Client Secret** *(required)* - The Client ID and Secret you received from ADP that has the [Required Permissions](#required-permissions) to fetch assets. Contact your ADP representative to receive the Client ID and Client Secret.

3. **Certificate File** *(required)* - The  X.509 certificate, Base64 ASCII encoded PEM file issued by ADP. For more detailed information, see [Generating a Certificate Signing Request](https://developers.adp.com/articles/general/generate-a-certificate-signing-request).

4. **Private Key File** *(required)* - The .KEY file created as part of the CSR process. For more detailed information, see [Generating a Certificate Signing Request](https://developers.adp.com/articles/general/generate-a-certificate-signing-request).

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

9. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image align="center" alt="ADP Vantage" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ADP%20Vantage.png" />

## APIs

Axonius uses the [Workers API](https://developers.adp.com/articles/api/hcm-offrg-vantg/hcm-offrg-vantg-hr-workers-v2-workers/apiexplorer).

<Callout icon="📘" theme="info">
  Note

  The actual endpoint used is `/​hr/​v2/​worker-demographics`. It is equivalent to `/​hr/​v2/​workers`, but doesn’t include sensitive personal information such as Social Security numbers.
</Callout>

## Required Permissions

The value supplied in [Client ID](#parameters) must have Read access to the `/​hr/​v2/​worker-demographics` endpoint.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version       | Supported | Notes |
| ------------- | --------- | ----- |
| API Version 2 | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.7