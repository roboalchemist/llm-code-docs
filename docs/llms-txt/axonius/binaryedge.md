# Source: https://docs.axonius.com/docs/binaryedge.md

# BinaryEdge

BinaryEdge scans the public internet to create real-time threat intelligence streams and reporting.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **API Token** *(required)* - An API Token associated with a user account that has permissions to fetch assets. The API Token is provided by BinaryEdge.
2. **Search Query** - The string used to query the BinaryEdge data. Refer to [search](https://docs.binaryedge.io/api-v2.html#v2querysearch).
3. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the **BinaryEdge Domain**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).
   * When enabled, the SSL certificate offered by the **BinaryEdge Domain** is verified against the CA database inside of Axonius. When the SSL certificate cannot be validated against the CA database inside Axonius, the connection fails with an error.
   * When disabled, the SSL certificate offered by the **BinaryEdge Domain** is not verified against the CA database inside Axonius.
4. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the **BinaryEdge Domain**.
   * When supplied, Axonius uses the proxy when connecting to the **BinaryEdge Domain**.
   * When not supplied, Axonius connects directly to the  **BinaryEdge Domain**.
5. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the **BinaryEdge Domain** via the value supplied in **HTTPS Proxy**.
   * When supplied, Axonius authenticates with this value when connecting to the value supplied in **HTTPS Proxy**.
   * When not supplied, Axonius does not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
6. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the **BinaryEdge Domain** via the value supplied in **HTTPS Proxy**.
   * When supplied, Axonius authenticates with this value when connecting to the value supplied in **HTTPS Proxy**.
   * When not supplied, Axonius does not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="BinaryEdgeN.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BinaryEdgeN.png" />

## APIs

Axonius uses the [BinaryEdge API V2](https://docs.binaryedge.io/api-v2.html).

## Required Ports

Axonius must be able to communicate with the value supplied in [API Token](#parameters) via the following ports:

* **TCP port 443**

## Required Permissions

The value supplied in [API Token](#parameters) must be associated with credentials that have READ permissions to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version           | Supported | Notes |
| ----------------- | --------- | ----- |
| BinaryEdge API V2 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.4