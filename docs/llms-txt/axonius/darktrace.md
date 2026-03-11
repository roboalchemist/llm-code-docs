# Source: https://docs.axonius.com/docs/darktrace.md

# Darktrace

Darktrace Immune System protects workforce and data from sophisticated attackers, by detecting, investigating and responding to cyber-threats.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Darktrace server.
2. **Public API Key** *(required)* - A public API Key associated with a user account that has the [Required Permissions](/docs/darktrace#required-permissions) to fetch assets.
3. **Private API Key** *(required)* - A private API Key associated with a user account that has the [Required Permissions](/docs/darktrace#required-permissions) to fetch assets.
4. **Signature Offset in hours** *(optional)* - Increase or decrease the number of hours to offset the timestamp of the Axonius client.
   * If the client timestamp is less than the server timestamp, increase the number of hours to synchronize the values. For example, if the server timestamp is 16:00 and the client timestamp is 14:00, enter `2` to synchronize the timestamp values.
   * If the client timestamp is more than the server timestamp, decrease the number of hours to synchronize the values. For example, if the server timestamp is 14:00 and the client timestamp is 16:00, enter `-2` to synchronize the timestamp values.
5. **Verify SSL** - Select to verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
6. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.
7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image align="center" alt="Darktrace_31-3-22" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Darktrace_31-3-22.png" />

***

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch model breaches for devices** - Select whether to fetch an additional layer of data, the list of model breaches that run on each device.
   * When enabled, all connections for this adapter also fetch model breaches for each device.
   * When disabled, all connections for this adapter do not fetch model breaches for each device.
2. **Fetch only devices that have a MAC Address and Host Name** - Select to only fetch devices with a MAC address and hostname. If cleared, all connections for this adapter will fetch devices even if they don't have a MAC address or hostname.
3. **Don't fetch devices without hostname** - Select to exclude fetching devices without a hostname. If cleared, all connections for this adapter will fetch devices even if they don't have a hostname.
4. **Device types to fetch** - Select the device types to fetch from the drop-down.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

***

## APIs

Axonius uses the Darktrace API.

***

## Required Permissions

The value supplied in [Public API Key](#parameters) and [Private API Key](#parameters) must be associated with credentials that have API Access permissions.

### Creating an Account with API Access Permissions

1. Log in to the Darktrace Web app by using an Admin account.
2. From the left menu, select **Admin → Permissions Admin**.
3. Click **Account Create** to create an account for API integration.
4. Activate the newly created account by clicking the **Flags** (`</>`) icon on the right. A green icon confirms that the API access is enabled.
5. Acquire the public and private tokens required for the adapter setup, as detailed in the next section.

### Acquiring the API Token Pair (Public and Private Token)

1. Log in to Darktrace.
2. From the left menu, select **Admin → System Config**.
3. From the **Settings** dialog in the left, select **API Token**. The public token is displayed on the right side. To view the private token, click **Remove**.