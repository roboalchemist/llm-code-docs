# Source: https://docs.axonius.com/docs/paloaltonetworks-iot.md

# Palo Alto Networks IoT Security (Zingbox)

Palo Alto Networks IoT Security prevents threats, block vulnerabilities, and automatically enforce policies for IoT, IoMT, and OT devices.

**Related Enforcement Actions:**

* [Palo Alto Networks IoT Security - Tag assets](/docs/zingbox-tag-asset)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Aggregated Security Findings, SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Palo Alto Networks IoT Security server that Axonius can communicate with via the [Required Ports](#required-ports), for example `https://\<my_customer>.iot.paloaltonetworks.com`

2. **Customer ID** *(required)* - The customer ID specifies the API call for a specific tenant.

3. **Key ID** *(required)* - The identifier for the Access Key.

4. **Access API Key** *(required)* - Password Type

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="zingbox_param" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-M9MI8OV2.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch vulnerabilities** - Select this to fetch vulnerabilities.
2. **Fetch devices details** - Select this to send a flag to the API to get the full details of the fetched devices.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Palo Alto IoT Security API Reference](https://docs.paloaltonetworks.com/iot/iot-security-api-reference/iot-security-api/get-device-inventory.html)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 4.5