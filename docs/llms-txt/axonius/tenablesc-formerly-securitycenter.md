# Source: https://docs.axonius.com/docs/tenablesc-formerly-securitycenter.md

# Tenable.sc (SecurityCenter)

Tenable.sc (formerly SecurityCenter) consolidates and evaluates vulnerability data, prioritizing security risks.
Note that the Source field shown in the Axonius Installed Software table for Tenable shows either *Direct* or *Agent Scanning*.

* *Direct* - the information about this source is updated to the Axonius fetch time from Tenable.
* *Agent Scanning* - the information is updated only according to the information fetched by the Tenable Agent, and up to date according to the time that the Tenable agent ran.

## Asset Types Fetched

* Devices, Aggregated Security Findings, Software, SaaS Applications, Alerts/Incidents

## Before You Begin

### Authentication Methods

Connect the adapter with either of the following parameter pairs:

* **User Name** and **Password**
* **Access Key** and **Secret Key**
* **Session Token** and **Session Cookie**

<Callout icon="📘" theme="info">
  Note

  The preferred credentials to use for authentication are **Access Key** and **Secret Key**.
</Callout>

### Required Permissions

The Tenable.sc account used to connect the adapter must have the Security Manager role, with access to all the required repositories.
For details about Tenable SC user roles, see [User Roles](https://docs.tenable.com/tenablesc/Content/UserRoles.htm).

## Connecting the Adapter in Axonius

### Required Parameters

1. **Tenable.sc domain** - The URL of the Tenable.sc management server. (e.g., `https://tenable-sc.company.com`).
2. **User Name** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

OR

2. **Access Key** and **Secret Key** - The API key-secret pair associated to a user account that has the [Required Permissions](#required-permissions) to fetch assets.

OR

2. **Session Token** and **Session Cookie** - A session cookie associated with the supplied username.

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/tenableSCconnection.png)

### Optional Parameters

1. **API Optional Prefix** - Optional API prefix.
2. **API Key for Kong authentication** - The API key for authentication using the Kong API Gateway.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
5. **HTTPS Proxy User Name** - The user name to use when connecting to the URL of the Tenable.sc management server via the value supplied in **HTTPS Proxy**.
6. **HTTPS Proxy Password** - The password to use when connecting to the URL of the Tenable.sc management server via the value supplied in **HTTPS Proxy**.
7. **Enable Client Side Certificate** - Check this option to enable Axonius to send requests using the certificates uploaded to allow Mutual TLS configuration for this adapter.
   * Click **Upload File** next to **Client Private Key File** to upload a client private key file in PEM format.
   * Click **Upload File** next to **Client Certificate File** to upload a public key file in PEM format.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Plugin parser** *(default: true)* - Toggle on this option to enable the plugin parser so the adapter will parse information from plugins.

2. **Do not fetch devices with no MAC address and no hostname** - Select whether to exclude fetching devices without a MAC address or hostname.

3. **Do not fetch devices with no MAC address and no hostname and no os type** - Select whether to exclude fetching devices without either a MAC address, hostname, or operating system (OS) types.

4. **Fetch vulnerabilities** - Select to fetch devices' unmitigated vulnerability data from Tenable.sc.

<Callout icon="📘" theme="info">
  Note

  If you want to also fetch mitigated vulnerabilities appearing in the **Mitigated** table of Tenable.sc, select **Fetch vulnerabilities** and **Fetch mitigated vulnerabilities**.

  When a vulnerability is fetched from the Mitigated table it is marked *Mitigated - Not Vulnerable*. When a vulnerability is fetched from the cumulative table and was vulnerable before, it is marked *Previously Mitigated (Currently Vulnerable)*.
</Callout>

5. **Fetch accepted risk vulnerabilities** - Select to fetch vulnerabilities with accepted risk.

6. **Fetch vulnerabilities last seen in the last X days** - Enter a number of days to only fetch vulnerabilities from that number of days back.

7. **Fetch SCAP scans** - Select whether to fetch data from SCAP scans.

8. **Do not fetch devices with unauthenticated scans only** - Choose whether to fetch devices with unauthenticated scans only from Tenable.sc.

9. **Fetch info level vulnerabilities only for listed plugin IDs** *(optional)* - Specify a comma-separated list of Tenable.sc plugin IDs.

10. **Repository name exclude list** *(optional)* - Specify a comma-separated list of Tenable.sc repositories. Repositories are databases within Tenable.sc that contain vulnerability data. For more details, see [Tenable.sc - Repositories](https://docs.tenable.com/tenablesc/Content/Repositories.htm).

11. **Repository name include list** *(optional)* - Enter names of one or more comma-separated repositories from which to fetch data. If you use this field, data will only be fetched from these repositories.

12. **Repository name exclude list - use 'contains' logic instead of exact match** - Select whether to consider the values supplied in **Repository name exclude list** as exact repository names.

13. **Fetch scan results** - Select whether to fetch scan results for each repository.

14. **Fetch scan details** - Select whether to fetch a new request (scan details) for each repository.

15. **Don’t populate OS from a not reliable source** - Select whether to populate the OS fields only if the data from Tenable is considered reliable (from a Tenable agent or an authenticated scan).

16. **Async chunks in parallel** *(required, default: 50)* - Specify the number of parallel requests all connections for this adapter will send to the Tenable.sc server at any given point.

17. **Devices in memory chunk size** *(required, default: 5000)* - Specify the maximum number of devices that the adapter will keep in memory at the same time.

18. **Fetch additional device data in the background** - Select to fetch some device data in the background, such as fetching installed software per device and asset groups.

19. **Run background fetch every X hours** *(optional, default: 24)* - Enter the number of hours to wait before running a background fetch. If left empty, a background fetch will start after every regular fetch.

20. **Parse interface name from vulnerability text** - Select whether to parse device interface name from the vulnerability text.

21. **Fetch installed software from Tenable plugins** - Select installed software plugins from the drop-down list that you want to fetch information about. The data is extracted from the output of the selected vulnerability scan plugins with no additional API calls.

22. **Installed Software** - Toggle on this option to enable fetching **all** installed software from Tenable.sc. The data (installed software per device) is extracted from a dedicated Tenable.sc software inventory API endpoint.
    <Accordion title="Installed Software Settings" icon="fa-info-circle">
      1. **Fetch top N installed software** - If you select this option, specify any value. This will specify the number of the top installed software fetched from `http://Tenable.sc`.

      * When the value of Fetch top installed software is empty or 0, then all installed software is fetched.

      2. **Fetch hostname from Plugin ID 55472** - Select whether all connections for this adapter will parse the device hostname from the Plugin data (text) of Plugin ID 55472.
         * When the plugin text does not have information about the hostname, then the regular hostname is used.
         * If this field is cleared, then the regular hostname is used.

      3. **Fetch Windows services from Plugin ID 44401** - Select whether all connections for this adapter will fetch data from the Windows services plugin 44401 for each device.

      4. **Parse SSL certificate from Plugin ID 10863** - Select to parse SSL certificate information from plugin ID number 10863.

      5. **Create Certificate assets from SSL certificates parsed from Plugin ID 10863** - Select to create separate Certificate assets from SSL certificate data discovered by Tenable Plugin 10863. Certificates become queryable as a distinct asset type in Axonius, separate from the devices where they were discovered.

      6. **Parse CPEs from Plugin ID 45590** - Select to parse CPEs from plugin ID number 45590.

      7. **Fetch vulnerabilities with severity equal or above this level** *(required, default: Info)* - Select the minimum level of severity to fetch vulnerabilities.

      8. **Fetch all plugin IDs over 1M** - Select whether to fetch all plugin IDs equal or greater than 1,000,000 (no matter their severity or info level).

      9. **Fetch tags from assets** - Select whether to fetch asset tags for devices.

      10. **Parse Windows Store Application from Plugin ID 85736** - Select this option to fetch the Plugin ID 85736 and parse the results as a list of strings containing the Windows Store Applications installed on the device.

      11. **Ignore devices that only have this plugin** *(optional)* - Enter one or more plugins for the adapter to not fetch devices that only have plugins with these IDs.

      12. **Fetch First Discovery Date and Last Observed Date from Plugin-19506** - Select this option to use Plugin-19506 to fetch the first discovery date and the last observed data for devices.

      13. **Fetch alerts** - Select this option to fetch Tenable.sc alerts as a new asset in the Alerts/Incidents category.

      14. **Fetch and parse OS Identification from Plugin-11936 output only** - Select this option to only parse the OS Identification field from the output of Plugin-11936.
    </Accordion>

23. **Enable fetching of asset groups** - Toggle on this option to fetch Tenable asset groups.

    <Accordion title="Asset Groups Settings" icon="fa-info-circle">
      1. **Fetch from devices without UUID** - Select this option to fetch asset groups from devices without UUID. This setting is only relevant when Enable fetching of asset groups is enabled. When this selection is cleared, then all tenable asset group information is fetched.

      2. **Fetch OS serial information** - Select this option to fetch OS Serial information from plugins 131568, 35351, 24270.

      3. **Parse DNS as hostname** *(default: false)* - Select this option so that the source for the hostname will be the DNS. Note that this setting will only take effect if *Parse hostname from Plugin ID 55472* is not enabled.

      4. **Fetch devices from mobile repositories** - Select this option to fetch devices from mobile repositories.

      5. **Enable real-time asset updates (Supported events: New alerts)** - Select this option to update assets in real time with New Alerts events.

      6. **Use CVE dates for device last seen calculation** - Select this option to use CVE dates for the device last seen calculation.

      7. **Parse plugin 16193 - Antivirus Software Check** - Select this option to fetch plugin 16193 if it is present for the device.

      8. **Parse plugin 54615 - Device Type** - Select this to fetch and parse *Device Type* and *Confidence Level* from plugin 54615.

      <Callout icon="📘" theme="info">
        Note

        Even if **Fetch vulnerabilities** is disabled, the adapter will still fetch and parse plugins if their fetch configurations are enabled.
      </Callout>

      9. **Page size** *(default: 2000)* - Set the default page size the adapter will use when making requests.

      10. **Insert both CVE and Plugin as Security Findings** - Select this option to parse each CVE ID and plugin ID in the vulnerability as Security Finding.

      11. **Add open port only from non-mitigated vulnerability** - Select this option to limit the adding of open ports based on the mitigated state.

      12. **Fetch Secure Boot Status** - Select this option to fetch and parse secure boot status from plugins 34096, 34097, 34098.

      13. **Parse WMI Encryptable Volume Enumeration from Plugin 51187** - Select this to fetch Plugin 51187 which fetches Bitlocker data. This capability lessens the requirement to set up MBAM within an environment just to fetch Bitlocker data.

      14. **Fetch Accept Risk Rules** and **Fetch Recast Risk Rules** - Enable these settings to fetch data from these endpoints.

      15. **Parse software name from Plugin ID 63155** - Select to fetch the software name for the CVE associated with Plugin 63155.

      16. **Wait for the last scan to complete before fetching data** - Select to have the adapter fetch data only after its last scan is complete.

      17. **Parse plugins as compliance findings** - Select to parse plugins from number 1\_000\_000 and up as Compliance findings.

      18. **Exclude devices with hostname starting with** *(optional)* - Use this option to exclude devices whose hostnames start with a defined string. Enter the string or a comma-separated list of strings which the hostnames to exclude will start with.
    </Accordion>

24. **Enable granular heavy fields selection** - Enable this to select specific heavy fields to ingest. When enabled, unselected fields are not populated, reducing database size and improving performance. When disabled, the global heavy fields setting are used.
    * **Heavy Fields to Ingest** - Select fields from the list. Each adapter connection can have different heavy field configurations.

<Callout icon="📘" theme="info">
  Note

  For details about general advanced settings under the **Adapter Configuration** tab, see [**Adapter Advanced Settings**](/docs/advanced-settings).
</Callout>

### Related Enforcement Actions

* [Tenable.sc (SecurityCenter) - Add IP Addresses to Assets](/docs/add-ips-to-tenablesc-asset)
* [Tenable.sc (SecurityCenter) - Launch Scan](/docs/tenable-sc-launch-scan)
  <br />

<br />