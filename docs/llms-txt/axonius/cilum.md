# Source: https://docs.axonius.com/docs/cilum.md

# Cilium

Cilium is an open source and eBPF-based networking, security, and observability tool that helps secure network connectivity between application services.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Containers

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Cilium server.

2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

3. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

4. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Cilium](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Cilium.png)

## APIs

Axonius uses the [Cilium API](https://docs.cilium.io/en/stable/api/#get--endpoint).

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| v1.16   | Yes       | --    |

## Supported From Version

Supported from Axonius version 6.1.32.1