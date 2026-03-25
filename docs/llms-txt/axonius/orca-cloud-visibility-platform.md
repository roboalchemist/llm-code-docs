# Source: https://docs.axonius.com/docs/orca-cloud-visibility-platform.md

# Orca Cloud Visibility Platform

Orca Cloud Visibility Platform delivers visibility to cloud security posture, including prioritized alerts on vulnerabilities, compromises, misconfigurations, and more.

<Callout icon="📘" theme="info">
  Note

  The Axonius adapter was updated to support the latest Orca API as of October 2025. As the Legacy Orca API is being deprecated, all users of the Orca Adapter are advised to upgrade to Axonius version 7.0.11 to ensure continued functionality.
</Callout>

### Asset Types Fetched

* Devices, Users, Aggregated Security Findings ,Software, Roles, Groups, SaaS Applications, Tickets, Compute Services, Application Services, Networks, Load Balancers, Databases, Containers, Object Storage, Network Services, File Systems, Accounts/Tenants, Serverless Functions, Disks, Compute Images, Secrets, Certificates, Network/Firewall Rules, Alerts/Incidents

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key/API Token

### APIs

* `POST https://DOMAIN/api/serving-layer/query` - for fetching all assets
* `POST https://DOMAIN/api/query/logs` - for fetching logs

### Permissions

Consult with your vendor for permissions for reading the objects.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Orca Domain** - The hostname of the Orca Cloud Visibility Platform server. Make sure you enter the correct hostname for your region. For example, in the US the domain should be *app.us.orcasecurity.io*.
2. **API Key** - The API Key generated in the Orca Cloud Visibility Platform.

<Callout icon="📘" theme="info">
  Note

  The API Key was deprecated in Orca. An API Key is supported only if it was previously generated.
</Callout>

3. **API Token** - The API Key generated in the Orca Cloud Visibility Platform for Axonius usage.

<Callout icon="📘" theme="info">
  Note

  * You must supply either the **API Key** or  **API Token**.

  * It is highly recommended to use the **API Token**.
</Callout>

<Image alt="orca_prms" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/orca_prms.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

### Custom asset fetch rules

Enable **Custom asset fetch rules** to fetch Orca data as the specified asset type, instead of as devices. Under each setting, add the required Orca asset types.

* For example, under  **Orca types to fetch as Group assets**, enter Orca types to fetch as Groups and not as devices.

### Alerts Fetch Mode

From the drop-down select **Simple Alerts Fetch \[DEPRECATED]** (default) or **Advanced Alerts Fetch**.

#### Simple Alerts Fetch \[DEPRECATED]

Select or clear the following options:

* **Show all status alerts** *(default: true)*
* **Show informational alerts** *(default: true)*
* **Show resolved alerts** *(default: negative)*.

#### Advanced Alerts Fetch

Set the following:

* **Fetch only selected alert categories** - From the drop-down select one or more alert categories to fetch. Only these categories will be fetched. If none are selected, then all alert categories are fetched.
* **Fetch only alerts that are linked to assets of the selected categories** - From the drop-down select one or more alerts that are related to specific inventory items to fetch.
* **Fetch only selected alert severities** - From the drop-down select one or more alert severities to fetch. Only these severities will be fetched. If none are selected, then all alert severities are fetched.
* **Fetch only selected alert status** - From the drop-down select one or more alert statuses. Only these statuses will be fetched. If none are selected, then all alert statuses are fetched.
* **Fetch only alerts with Orca Score greater than or equal to** *(optional)* - Select whether to fetch alerts with an Orca Score greater than or equal to a specified number.
* **Fetch only alerts with Max CVSS score greater than or equal to** *(optional)* - Select whether to fetch alerts with a Max CVSS score greater than or equal to a specified number.

### Additional Settings

1. **Orca tags to parse as fields** - Enter a list of Orca tag keys to parse as separated fields. Adding items one at a time will create a comma-separated list.
2. **Extra entities to fetch** - Select from the dropdown assets to fetch in addition to Devices.
3. **Fetch alerts starting from the last X hours** - Enter the number of hours back from which to begin to fetch alerts.  Alerts will be fetched from that number of hours back, or greater.
4. **Fetch logs starting from the last x hours** - Enter the number of hours back from which to begin to fetch logs.  Logs will be fetched from that number of hours back, or greater.
5. **Fetch Container Tags** *(required, default: true)* - Select whether to fetch container tags to the GUI..
6. **Parse all Orca tags as fields** - Select this option to parse all Orca tags as fields.
7. **Fetch assets with current states. If nothing is selected, all asset states are fetched** *(optional)* - Enter which current states to fetch assets. If nothing is selected, all asset states are fetched.
8. **List of asset tags to fetch** - Enter a space separated list of the asset tags   to fetch in the following format: `<TAG_NAME> = <TAG_VALUE>`. Both TAG\_NAME and TAG\_VALUE are case sensitive.
9. **Enable Vulnerabilities fetch** - Enable this option to fetch vulnerability data. When this is enabled, you can also enable **Fetch Vulnerable Packages**.
10. **Use CVSS Max Score as Risk Totals source** - Select this option so that the source for the vulnerability risk level will be from CVSS Max Score.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>