# Source: https://docs.axonius.com/docs/proofpoint-meta.md

# Proofpoint ZTNA (Meta)

Proofpoint ZTNA (Meta) provides zero-trust secure remote access to enterprise applications.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Proofpoint Meta API Endpoint** *(required, default: `https://api.metanetworks.com` )* - The  default value of the endpoint should not be changed, this is the gateway to Proofpoint's Meta API.
2. **Client ID** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.
3. **Client secret** *(required)* - An API Key associated with a user account that has permissions to fetch assets.
4. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Proofpoint Meta API Endpoint**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).
   * When enabled, the SSL certificate offered by the value supplied in **Proofpoint Meta API Endpoint** is verified against the CA database inside of Axonius. When the SSL certificate can not be validated against the CA database inside  Axonius, the connection fails with an error.
   * When disabled, the SSL certificate offered by the value supplied in **Proofpoint Meta API Endpoint** is not verified against the CA database inside Axonius.
5. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Proofpoint Meta API Endpoint**.
   * When supplied, Axonius uses the proxy when connecting to the value supplied in **Proofpoint Meta API Endpoint**.
   * When not supplied, Axonius connects directly to the value supplied in **Proofpoint Meta API Endpoint**.
6. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Proofpoint Meta API Endpoint** via the value supplied in **HTTPS Proxy**.
   * When supplied, Axonius authenticates with this value when connecting to the value supplied in **HTTPS Proxy**.
   * When not supplied, Axonius does not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
7. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the value supplied in **Proofpoint Meta API Endpoint** via the value supplied in **HTTPS Proxy**.
   * When supplied, Axonius authenticates with this value when connecting to the value supplied in **HTTPS Proxy**.
   * When not supplied, Axonius does not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![ProofpointZTNAN.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ProofpointZTNAN.png)

## APIs

Axonius uses the Meta Networks - APIs.

## Required Ports

Axonius must be able to communicate with the value supplied in [Proofpoint Meta API Endpoint](#parameters) via the following ports:

* **HTTP/S (80/443)**

## Required Permissions

The value supplied in [Client ID](#parameters) must have

* users:read  permission
* network\_elements:read permission
* metaconnects:read permission
* devices:read permission

## Supported From Version

Supported from Axonius version 4.4