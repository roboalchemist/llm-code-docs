# Source: https://docs.axonius.com/docs/symantec-cloud-swg.md

# Symantec Cloud Secure Web Gateway (WSS Agent)

<Callout icon="❗️" theme="error">
  Deprecated

  This adapter has been deprecated.
</Callout>

Symantec WSS is a cloud-delivered secure web gateway that protects against malware and enforces policies to access the web.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **User Name** and **Password** *(required)* - The credentials for a user account that has  permission to fetch assets. To learn how to generate credentials, see [About Cloud SWG API Authentication](https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/cloud-swg/help/cloudswg-api-reference/api-keys.html).

2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

3. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

4. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![SymatecCloudSWG](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SymatecCloudSWG.png)

## APIs

Axonius uses the [Cloud Secure Web Gateway (Cloud SWG) Closed Network Tunnel REST API](https://techdocs.broadcom.com/us/en/symantec-security-software/web-and-network-security/cloud-swg/help/cloudswg-api-reference/api-reference-wssa.html).

## Supported From Version

Supported from Axonius version 5.0