# Source: https://docs.axonius.com/docs/proofpointtap.md

# Proofpoint TAP

Proofpoint Targeted Attack Protection (TAP) is an email-based security solution for ransomware prevention and other email-based threats.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Proofpoint TAP server, generally tap-api-v2.proofpoint.com.

2. **Principal Name** and **Secret** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL**  - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="Proofpoint_TAP" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Proofpoint_TAP.png" />

## APIs

Axonius uses the [Proofpoint People API](https://help.proofpoint.com/Threat_Insight_Dashboard/API_Documentation/People_API).

## Required Permissions

The value supplied in [Principal Name](#parameters) must have service credentials to authenticate to the API.

## Supported From Version

Supported from Axonius version 4.5