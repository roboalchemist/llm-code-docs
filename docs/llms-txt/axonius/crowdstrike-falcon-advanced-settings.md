# Source: https://docs.axonius.com/docs/crowdstrike-falcon-advanced-settings.md

# Crowdstrike Advanced Settings

## Accessing Advanced Configuration

1. Navigate to **Adapters** and search for `CrowdStrike Falcon` then click the adapter tile
2. In the left menu, select **Advanced Configuration** under **Advanced Settings**

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

## Advanced Settings

1. **Amount of requests per second** *(default: 5, min: 1, max: 5)* - Set the amount of requests per second. If you are uncertain of the amount, it is best to leave as is.
2. **Get uninstall token for device** - Select this option to fetch the uninstall token for a specific device using the following API:
   `https://assets.falcon.crowdstrike.com/support/api/swagger.html#/sensor-update-policies/revealUninstallToken`
3. **Get Detections Information for devices** - Select this option to fetch detections information about the device, including the total counts of the detections.

<Callout icon="📘" theme="info">
  Note

  If **Get Detections Information for devices** is enabled in your environment, note that as of September 2025, the following API endpoints used by the adapter were deprecated and replaced:

  * `detects/entities/summaries/GET/v1` - deprecated, replaced by: `alerts/aggregates/alerts/v2`

  * `detects/queries/detects/v1` - deprecated, replaced by: `alerts/queries/alerts/v2`
</Callout>

4. **Get Configuration Assessments for device** - Select this option to fetch configuration assessments for the device. To access the Configuration Assessment API, your API client must be assigned the Falcon Configuration Assessment:read scope.
5. **Enrich Configuration Assessments with Rule Name** - Select this option to enrich configuration assessments with the rule name.
6. **Policy types to fetch** - Select which policy type you want to fetch. Prevention, Sensor Update and Firewall policies are available for selections.

<Accordion title="Avoid Duplicate Devices" icon="fa-info-circle">
  * **Enable logic to avoid duplicate devices** - Enable this option to access the following settings:

  ### Cloud based device options

  * **Avoid device duplications based on local IP address and account ID** - Select this option to avoid returning duplicate machines when using the scroll API. If a duplicate hostname, serial number, or IP address is detected, the most recent device is fetched.
  * **Avoid device duplications based on hostname** - Select this option to avoid returning duplicate machines based on a hostname when using the scroll API. If a duplicate hostname is detected, only the most recent device is fetched.
  * **Avoid device duplications based on external IP**  - Select this option to avoid returning duplicate machines based on the device's external IP.

  ### Non-cloud based device options

  * **Avoid device duplications based on hostname** - Select this option to only fetch the latest information for a hostname of a device.
</Accordion>

7. **Fetch devices last logged in users** - Select this option to fetch the last 10 users who logged in for each device.
8. **Fetch devices network history** - Select this option to fetch the history  of IP and MAC addresses for devices.
9. **Fetch users** - Select this option to fetch users and their associated security roles. For more information, see [CrowdStrike Required Permissions](/docs/crowdstrike-falcon#required-permissions).
10. **Devices per page** *(required, default: 100)* - Specify the number of results per page received for a given request to gain better control of the performance of all connections of this adapter. The value specified can be from 100 to 5000. A higher value makes fewer API calls, which helps prevent API rate limit.
11. **Fetch Zero Trust Assessment Data** - Select this option to enriche devices with additional data from the zero trust assessment endpoint.
12. **Get drive encryption data** - Select this option to get the encryption status of the device's drives.
13. **Get FileVantage data** - Select this option to fetch FileVantage data.
14. **Get USB control policy data** - Select this option to enrich each device with the USB control policy to which the device belongs.
15. **Fetch installed patches from the following report** - Enter the name of the Installed Patches report to fetch. Leave empty not to fetch installed patches.
16. **List of tags to parse as fields** - Enter a comma-separated list of tags to parse as fields.
17. **Fetch devices in hidden status** - Select this option to fetch devices in hidden status.
18. **Use hostname as device manufacturer serial number for mobile devices** - Select this option to use the hostname as the device manufacturer serial number for mobile devices.
19. **Fetch incidents** - Enable this option to fetch CrowdStrike incidents.
20. **Create applications from vulnerabilities** - Select this option to create SaaS Application assets from the software related to each vulnerability.
21. **Fetch application settings** *( for accounts with Axonius SaaS Applications)* - By default Axonius fetches application settings. Clear this option to not fetch application settings.

<Accordion title="Vulnerability Fetch Settings" icon="fa-info-circle">
  * **Enable vulnerability fetch** - Enable this option to fetch vulnerabilities found on the devices and configure relevant settings.

  <Callout icon="📘" theme="info">
    **Note**

    To use this setting,  the value supplied for the **Username / Client ID** connection parameter must have Read access permissions to the Vulnerabilities API scope `vulnerabilities:read`.
  </Callout>

  * **Device types to enrich with vulnerability data** - Select whether to enrich vulnerability data from devices or external devices (or both).
  * **Include data facets in results** - From the drop-down select data facets to use in results.
  * **Parse vulnerability descriptions** - Select this option to parse vulnerability descriptions.

  ### Filter vulnerabilities settings

  * **Enable advanced vulnerabilities filtering** - Enable this option to enable advanced vulnerabilities filtering and configure relevant filters.
    * **Filter mechanism** - Select the filter mechanism from the drop-down, either FQL filter or pre-defined filter options.

    * **FQL filter**
      Enter a valid Falcon Query Language (FQL) filter string as specified here: [Falcon Query Language](https://falcon.crowdstrike.com/login/?next=%2Fdocumentation%2F45%2Ffalcon-query-language-fql).

  #### Pre-defined filter options

  You can configure the following pre-defined filter options.

  * **Filter by status** - Enable this option to filter by status. Select either Include or Exclude to set statuses that will either be included or excluded in the fetch.
    * **List** - From the drop-down select status types to either exclude or include.
  * **Filter by timestamps**
    Use the settings available to filter the vulnerabilities set depending on when they were last seen, closed, created or updated. A 0 value in any of the fields (default) will prevent fetching any vulnerabilities.

  #### Suppression filter settings

  * **Filter by suppression info** - Enable this option to filter by suppression info.
    * **Filter by is\_supressed** - Enable this option to determine (in combination with the true/false drop-down) whether to fetched suppressed vulnerabilities.

  #### CVE filter settings

  **Filter by CVE info** - Enable this option to filter by CVE info.

  * **ExPRT filtering** -  Enable this option to implement ExPRT filtering. Select either Include or Exclude to set levels of severity that will either be included or excluded in the fetch.
    * **List** - From the drop-down select levels of severity to either exclude or include.

  * **Exploit filtering** - Enable this option to implement filtering by exploit types. Select either Include or Exclude to set types of exploits that will either be included or excluded in the fetch.
    * **List** - From the drop-down select types of exploits to either exclude or include.

  * **Severity filtering** - Enable this option to implement filtering by severity. Select either Include or Exclude to set levels of severity that will either be included or excluded in the fetch.
    * **List** - From the drop-down select levels of severity to either exclude or include.
</Accordion>

22. **Fetch external devices of type DNS Domain. Requires EASM license** - Select this option to fetch external DNS domain devices. This setting requires an EASM license.
23. **Fetch external devices of type IP. Requires EASM license** - Select this option to fetch external IP devices. This setting requires an EASM license.
24. **Enrich devices with online state** - Select this option to enrich devices with their online state (for example: 'online', 'offline', or 'unknown').
25. **Parse POD devices as containers** - Select this option to parse POD devices as containers.
26. **Skip parsing containers** - Select this option to skip the parsing of containers.
27. **Fetch MITRE ATT\&CK data** - Select to fetch MITRE ATT\&CK techniques information.
28. **Fetch Alerts and Severities** - Select to fetch CrowdStrike alerts and risk severities.
29. **Fetch Alerts as Incidents** - Select to fetch CrowdStrike alerts as Incidents.
30. **Deny List of Product Type Description** - Enter a list of Product Type Descriptions you **don't** want the adapter to fetch.
31. **Deny List of Deployment Types** - Enter a list of Deployment Types you **don't** want the adapter to fetch.

<Accordion title="CSPM Account / Tenants Settings" icon="fa-info-circle">
  * **Enable CSPM Account / Tenant fetching** - Enable this option to fetch CSPM accounts and tenants found on the devices and configure relevant settings.
  * **Account / Tenant Types** - Select the account types you want to fetch - AWS, Azure, or GCP accounts. You can select more than one option.
  * **Member CID Options** *(optional)* - Add strings to add the member CID to. This helps adjust the authentication process during Accounts fetch.
</Accordion>

32. **Platform Include list** - Specify a comma-separated list of platforms in CrowdStrike, in order to only fetch devices associated with the platforms listed, otherwise devices associated with any platform are fetched.
33. **Device Type Include List** - Specify a comma-separated list of product\_type\_desc parameters in CrowdStrike to fetch.
34. **Machine Domain Include list** - Specify a comma-separated list of Microsoft Active Directory domains. The connection for this adapter will only collect devices from the domains provided in this list.
35. **OS Version exclude list** - Add a comma separated list of OS Versions. Devices with these Operating Systems will not be fetched.
36. **OS Version include list** - Add a comma separated list of OS Versions. Devices without these Operating Systems will not be fetched.
37. **Group Name Include list** - Specify a list of groups of systems in CrowdStrike. The connection for this adapter will only collect devices associated with the groups provided in this list.
38. **Group name exclude list** - Specify a list of group names. If a device has this group associated with it, Axonius will exclude it.
39. **Exclude hosts that have 'EC2' in their name and haven't been seen in the last X days** - Remove EC2 hosts with EC2 in their name that have a last seen date lower than the specified number of days.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>