# Source: https://docs.axonius.com/docs/island.md

# Island

Island is an enterprise browser, built on Chromium, with numerous built-in capabilities for protecting against user-, data-, and network-based threats.

### Use Cases the Adapter Solves (optional)

* **Detecting Unmanaged Assets**: Identify devices running the Island browser that are not currently accounted for in your inventory.
* **Analyzing Access and Usage**: Gain visibility into user activity and installed extensions to ensure compliance with corporate security policies.
* **Verifying Security Coverage**: Confirm that the Island enterprise browser is correctly deployed across the organization's user base.

### Asset Types Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg) SaaS Applications

<br />

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**
Verify

### APIs

Axonius uses the Island API Version 1.

### Permissions

The following permissions are required:
Verify

#### Supported From Version

Supported from Axonius version 4.6

### Setting Up Island to Work with Axonius

Verify

<br />

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for **Island**, and click on the adapter tile.\
Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Island server. (default: `https://management.island.io`)
2. **Token** - An API Key associated with a user account that has permissions to fetch assets.
3. **Connection Label** - A label to help you distinguish between multiple connections for the same adapter. See [Connection label](/docs/adding-a-new-adapter-connection#setting-adapter-connection-parameters).

<Image align="center" alt="Island connection screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Island.png" width="500" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.
5. **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network and not from the primary Axonius instance, which may be an Axonius-hosted (SaaS) instance or Customer-hosted (on-premises / private cloud). To use this option, you need to set up an Axonius Gateway.

<br />

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note:

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />

1. **Fetch timeline events** - Select this option to fetch timeline events.
2. **Fetch users** - By default this adapter fetches users. Clear this option to not fetch users.
3. **Fetch installed extensions** - Select this option to enrich devices with installed extensions.

<br />

### Related Enforcement Actions

Verify