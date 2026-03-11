# Source: https://docs.axonius.com/docs/cybereason-deep-detect-respond.md

# Cybereason Deep Detect & Respond

Cybereason Deep Detect & Respond (EDR) defends against advanced attacks by collecting and analyzing behavioral data to identify suspicious activities.

**Related Enforcement Actions**

* [Cybereason Deep Detect & Respond - Add Tag to Assets](/docs/tag-in-cybereason-deep-detect-respond)
* [Cybereason Deep Detect & Respond - Isolate/Unisolate Assets](/docs/isolate-unisolate-in-cybereason-deep-detect-respond)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Cybereason Domain** *(required)* - The hostname of the Cybereason server.

2. **User Name** and **Password** *(required)* - The user name and password for an account that has read access to the API.

3. **Verify SSL** - Select to verify the SSL certificate offered by the value supplied in **Cybereason Domain**. For more details, see [SSL Trust & CA Settings](/docs/global-settings#ssl-trust-amp-ca-settings).

4. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Cybereason Domain**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Cybereason](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Cybereason.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Custom tags Include list** *(optional)* - Specify a comma-separated list of Cybereason tags.
   * If supplied, all connections for this adapter will only fetch devices tagged with any of the comma-separated list of Cybereason tags you have specified.
   * If not supplied, all connections for this adapter will fetch any device.
2. **Fetch processes** - Select this option to fetch processes.
3. **Avoid hostname duplications** - When selected, if two or more devices have the same hostname, only the device with the latest last\_seen value is fetched.
4. **Ignore stale agents** - Select to ignore agents with a 'Stale' status.
5. **Use CSV API** *(default: false)* - By default the system uses the Sensor Query API. Select this option to use the CSV API to fetch devices.
6. **Fetch devices with location tag** *(optional)* - Enter a list of location tags to make the adapter fetch only devices with the matching tag(s).

<Callout icon="📘" theme="info">
  Note

  Only change the default setting after guidance from Axonius Support.
</Callout>

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Permissions

The value supplied in [User Name](#parameters) must have the following permissions in order to fetch assets:

* system admin
* sensor admin L1