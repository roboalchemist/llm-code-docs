# Source: https://docs.axonius.com/docs/spektra.md

# SPEKTRA

NTT SPEKTRA (Sentient Platform for Network Transformation) is a managed network services platform.

## Asset Types Fetched

* Devices

## Before You Begin

**Authentication Method**

* Subscription Key / API Key

### APIs

Axonius uses the [SPEKTRA Edge API](https://docs.edgelq.com/apis/).

#### Supported From Version

Supported from Axonius version 6.1

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the SPEKTRA server.
2. **Subscription Key** - A subscription key associated with a user account that has permissions to fetch assets.
3. **API Key** - An API Key associated with a user account that has permissions to fetch assets.

![SPEKTRA](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SPEKTRA.png)

### Optional Parameters

1. **Spektra Region** - Specify one or more comma-separated region names to configure the adapter for specific customer regions.

2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

3. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

4. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

**Parser Config**

**Additional Network Device Families** - Axonius classifies the following device  models as Network devices by default: *Network gear*, *Controller*, *IP switch*, *Access point*. Enter additional Network Device Model families to customize which device model families should be classified as network infrastructure devices. Any device which matches this will be classed as a network infrastructure device.