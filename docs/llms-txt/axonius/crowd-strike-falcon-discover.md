# Source: https://docs.axonius.com/docs/crowd-strike-falcon-discover.md

# CrowdStrike Falcon Discover

CrowdStrike Falcon Discover is a network security monitoring tool that provides real-time visibility into devices, users, and applications.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Software
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required, default api.crowdstrike.com)* - The hostname or IP address of the CrowdStrike Falcon Discover server.

2. **Client ID** and **Client Secret** *(required)* - The **Client ID** and **Client Secret**. Refer [creating credentials](/docs/crowdstrike-falcon#creating-credentials-latest-api) for information about how to create the Client ID and Client Secret.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. **Enhanced Device Search Settings** - These settings help to ensure the greatest number of devices will be returned. For example, if many devices in a specific location have "LAPTOP-" as a prefix, you can add "LAPTOP-" to the list of prefixes to search for.
   * **Add support for host naming conventions** - Toggle on to enable the adapter to search for devices based on host names when there are naming conventions in place.
   * **Host Name Prefix** - Enter a comma-separated list of host name prefixes to search for.

<Callout icon="📘" theme="info">
  Note

  * This could potentially bring back more devices.

  * This feature does not support regex.
</Callout>

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="CrowdStrikeDiscover" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CrowdStrikeDiscover.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch applications** - Select this option to fetch applications (installed software) on each device.
2. **Only fetch applications used in the last X days (leave 0 for all)** - Enter a value higher than zero and select **Fetch applications** in order to only fetch applications used in the selected amount of days. Leave 0 (default) to fetch all applications, regardless of the last used timestamp.
3. **Filter installed software** - Toggle on this setting to filter the installed software.
   * **Require software name** - Only populate installed software if the software has a name.
   * **Use file name if no software name** - If the software does not have a name, use the file name.
   * **Filter by software name** - Toggle on to filter by software name. Select either Include or Exclude to set software names that will either be included or excluded in the fetch.
     * **List** - Enter a comma-separated list of software names to either exclude or include.
4. **Fetch IoT devices** - Select this option to fetch the IoT devices from the `discover/queries/iot-hosts/v1` endpoint.
5. **Fetch only latest software versions** - Enable this option to choose only the device with the latest last-seen timestamp.
6. **Fetch only software with Update Time and Last Used On present** - Enable this option to fetch only software with existing values for the following attributes: `last_updated_timestamp: "string"`, `last_used_timestamp: "string"`.
7. **Fetch users** - Toggle on this option to fetch users.

### Advanced device filtering

* **Filter devices** - Toggle on this option to filter devices and configure relevant settings.

* **Filter by data providers** - Toggle on to filter by data providers. Select either Include or Exclude to set data providers that will either be included or excluded in the fetch.
  * **List** - In the field, enter data providers to either exclude or include.

* **Filter by discoverer count** - Toggle on to filter devices by their discoverer count field. Select **Greater than** if devices need more discoverers in order to be fetched or **Less than** if devices need less discoverers in order to be fetched. Otherwise select **Equal to** or **Not Equal**.
  * **Amount** - Set the amount of discoverers required by a device.
  * **Filter by confidence level** - From the dropdown, select the confidence level.

### Separate historical IP addresses

* **Separate historical IP addresses** - Toggle on to configure a pattern to apply to an interface alias in order to identify a historical IP address and record it separately from current IP addresses. Historical IP addresses will not be taken into account for device correlation but will remain queriable, if desired.
  * **Interface alias regex pattern** - In the field, enter a regex pattern to apply to an interface alias in order to identify a historical IP address.

8. **Avoid device duplications based on hostname** - Select this option to filter devices with the same hostname and keep only the one with the most recent Last Seen date.
9. **Parse browser extensions separately from installed software with more information** - Select this option to separate the parsing of browser extensions from other installed software into a new table called "Browser Extensions".
10. **Fetch Only Devices within Specific Networks** - Enter names of networks, the adapter will only fetch devices within these networks.
11. **Ingest devices only if type is "managed"** - Select this option to fetch only managed devices.
12. **Ingest devices only if Product Type exists** - Select this option to only ingest devices if the Product Type field exists on the device.
13. **Ingest devices only if hostname exists** - Select this option to only ingest devices if the hostname field exists on the device.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses:

* [CrowdStrike Falcon Authentication API](https://falcon.crowdstrike.com/login/?next=%2Fdocumentation%2F46%2Fcrowdstrike-oauth2-based-apis)

* [CrowdStrike Falcon Get Devices API](https://falcon.crowdstrike.com/login/?next=%2Fdocumentation%2F197%2Ffalcon-discover-apis)

* [CrowdStrike Falcon Discover Applications](https://falcon.crowdstrike.com/login/?next=%2Fdocumentation%2F197%2Ffalcon-discover-apis#get-a-list-of-applications-that-meet-criteria-you-define) (for the Advanced setting, 'Fetch applications')

## Required Permissions

The value supplied in [Client ID](#parameters) must the following permission in order to fetch assets.

| Scope  | Permission |
| ------ | ---------- |
| Assets | Read       |

## Supported From Version

Supported from Axonius version 4.8