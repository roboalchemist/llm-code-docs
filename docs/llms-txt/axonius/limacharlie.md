# Source: https://docs.axonius.com/docs/limacharlie.md

# LimaCharlie

LimaCharlie provides endpoint-driven information security tools to run an MSSP or SOC,  as well as APIs that allow users to build and monetize their own products.

**Related Enforcement Actions:**

* [LimaCharlie - Isolate/Unisolate Assets](/docs/isolate-and-unisolate-in-limacharlie)
* [LimaCharlie - Tag Sensors](/docs/limacharlie-tag-sensors)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Organization ID** *(required)* - Your LimaCharlie Organization ID.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate offered by `https://api.limacharlie.io/`. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-amp-ca-settings)\*\*

4. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to `https://api.limacharlie.io/`

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to `[https://api.limacharlie.io/` via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to `[https://api.limacharlie.io/` via the value supplied in **HTTPS Proxy**.

7. For details on the common adapter connection parameters and buttons, see `Adding a New Adapter Connection`

<Image align="center" alt="image.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1400).png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  From Version 4.6, Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Ignore devices that have not been seen in the last X hours** *(optional, default: 0)* - Enter 1 or more hours to ignore devices that have not been seen by the source. A value of 0 means to fetch all connected devices.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [LimaCharlie.io REST API](https://doc.limacharlie.io/docs/api/container/static/swagger/v1/swagger.json).