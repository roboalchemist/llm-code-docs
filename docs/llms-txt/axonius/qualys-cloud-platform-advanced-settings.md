# Source: https://docs.axonius.com/docs/qualys-cloud-platform-advanced-settings.md

# Qualys Cloud Platform Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Use Qualys API** *(required, default: true)* - Select whether to use the Qualys API to fetch data.
2. **Asset CVE on Host Detection** *(DEPRECATED)* - Not currently being used and will be deprecated. Previously it added CVE information to host detections, but Qualys now does this by default.
3. **Use Global IT Asset Inventory API** - Select whether to use Global IT Asset Inventory API.
   * If enabled, all connections for this adapter will use the Global IT Asset Inventory API to fetch data.

<Callout icon="📘" theme="info">
  Note

  For Qualys API, you can enable only **Fetch vulnerabilities data**; however, to ensure maximum coverage, it is recommended to also enable **Enrich vulnerabilities from detection**.
</Callout>

* If disabled, all connections for this adapter will not use the Global IT Asset Inventory API to fetch data.

4. **Fetch vulnerabilities data** *(required, default: true)* - Select to fetch vulnerabilities from the Qualys Cloud Platform. For more information, see [Fetching Vulnerabilities](/docs/qualys-cloud-platform-advanced-settings#fetching-vulnerabilities).
5. **Ignore fixed vulnerabilities** - Select this option to ignore vulnerabilities where the Status field is set to "Fixed".
6. **Fetch authentication report**  - Select whether to fetch authentication report information from Qualys Cloud Platform. The authentication report includes the authentication status for the scanned hosts: Passed, Failed, Passed with insufficient privileges, or Not Attempted.
   * If enabled, all connections for this adapter will also fetch authentication report information from Qualys Cloud Platform.
   * If disabled, all connections for this adapter will not fetch authentication report information from Qualys Cloud Platform.
7. **Fetch tickets**  - Select whether to fetch tickets associated with devices from information Qualys Cloud Platform.
   * If enabled, all connections for this adapter will also fetch tickets information for tickets associated with devices from Qualys Cloud Platform.
   * If disabled, all connections for this adapter will not fetch tickets associated with devices from Qualys Cloud Platform.
8. **Use DNS name as hostname even if NetBIOS name exists**  - Select whether to use DNS name or NetBIOS name as the device hostname if both exists.
   * If enabled, all connections for this adapter use the DNS name as the device hostname even if NetBIOS name also exists.
   * If disabled, all connections for this adapter use the NetBIOS name as the device hostname, when exists.
9. **Do not force FQDN as Host Name for Mac OS devices** - Enable to make the device's netbiosName field the default Host Name.
10. **Fetch unscanned IP addresses** - Select whether to fetch yet-to-be-scanned hosts. Such devices' data will contain only an IP address (also as ID).
    * If enabled, all connections for this adapter will also fetch unscanned IP addresses from Qualys Cloud Platform.
    * If disabled, all connections for this adapter will not fetch unscanned IP addresses from Qualys Cloud Platform.
11. **Fetch Asset Groups** - Select whether to fetch Asset Groups.
    * If enabled, all connections for this adapter will also fetch Asset Groups.
    * If disabled, all connections for this adapter will not fetch Asset Groups.
12. **Do not fetch devices with no MAC address and hostname**  - Select whether to exclude fetching devices without MAC addresses and hostnames.
    * If enabled, all connections for this adapter will only fetch devices that have MAC addresses or hostnames.
    * If disabled, all connections for this adapter will fetch devices even if they do not have MAC addresses and hostnames.
13. **Fetch PCI and Patchable Flags** - Select whether to add PCI and Patchable flags to fetched vulnerabilities. When you fetch the Patchable flag you can create queries based on patch availability.
    * If enabled, all connections for this adapter will add a PCI Flag and a Patchable flag to fetched vulnerabilities.
    * If disabled, all connections for this adapter will not add a PCI Flag  and a Patchable flag to fetched vulnerabilities.

<Callout icon="📘" theme="info">
  Note

  To use this functionality,  the value supplied in [User Name](/docs/qualys-cloud-platform#connecting-the-adapter-in-axonius) must have one of the following roles: Manager, Unit Manager, Scanner, Reader.
</Callout>

12. **Fetch scanner appliances** - Select whether to fetch scanner appliances as devices.
    * If enabled, all connections for this adapter will fetch scanner appliances as devices.
    * If disabled, all connections for this adapter will not fetch scanner appliances data.
13. **Fetch Web Applications** - Select this option to fetch Web Applications. This setting requires permission to read from the “Web Application Scanning API”.
14. **Fetch policy compliance** - Select whether to fetch policy compliance associated with devices.
    * If enabled, all connections for this adapter will also fetch policy compliance associated with each device.

<Callout icon="📘" theme="info">
  Note

  Policy compliance is only fetched  if **Fetch policy posture information** is enabled.
</Callout>

* If disabled, all connections for this adapter will not fetch policy compliance associated with each device.

14. **Fetch policy posture information** - Select whether to fetch the posture information of every policy compliance.
    * If enabled, all connections for this adapter will also fetch policy posture information associated with policy compliance.
    * If disabled, all connections for this adapter will not fetch policy posture information.
15. **Add STIG rules to policy posture** - Select this option to fetch STIG rule IDs rule IDs associated with policy compliance  and add that information to the fetched posture information.

<Callout icon="📘" theme="info">
  Note

  STIG rules are fetched only if **Fetch policy posture information** is enabled.
</Callout>

19. **Fetch QID CVE IDs** - Select whether to fetch additional CVEs for each QID in the vulnerability list from the next URL API.
    * If enabled, all connections for this adapter will fetch additional CVEs.
    * If disabled, all connections for this adapter will not fetch additional CVEs.

20. **Fetch users**  - Select whether to fetch user account data from Qualys.
    * If enabled, all connections for this adapter will fetch user account data from Qualys.
    * If disabled, all connections for this adapter will not fetch user account data from Qualys.

21. **Use ‘lastCheckedIn’ field as ‘last\_seen’** -  Define how to compute the 'last\_seen' attribute in Qualys, depending on the API used to integrate with Axonius.
    * If you are using the [Qualys API](https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf):
      * If selected, the last\_seen attribute is calculated from **lastCheckedIn**. If the **lastCheckedIn** value isn't present, the last\_seen attribute is calculated from **lastVulnScan**.
      * If cleared, the last\_seen attribute is calculated from the most recent date fetched from any of the following fields: **lastVulnScan**, **lastCheckedIn**, **lastComplianceScan**, **lastSystemBoot**, or **modified**.
    * If you are using the [Global IT Asset Inventory API](https://www.qualys.com/docs/qualys-global-ai-api-user-guide.pdf):
      * If selected, the last\_seen attribute is calculated from **lastCheckedIn**. If the **lastCheckedIn** value isn't present, the last\_seen attribute is calculated from **lastVulnScan**.
      * If cleared, the last\_seen attribute is calculated from the most recent date fetched from any of the following fields: **createdDate**, **lastCheckedIn**,  **sensorLastUpdatedDate**, **lastModifiedDate**,  **lastUpdated**, **lastActivity**,  **lastInventory**, **lastVMScan**, **lastComplianceScan**, **lastFullScan**.

22. **Filter assets only on adapter side** - Select this option to have the adapter request all assets without using the **Ignore devices that have not been seen by the source in the last X hours** adapter configuration (see "General Configuration for Incremental Fetch" under [Configuring Incremental Fetch](/docs/qualys-cloud-platform#configuring-incremental-fetch-optional)) as a time delta filter, so it will filter them only on the adapter's side.

23. **Do not fetch devices without Last Seen** -  Define whether to fetch devices without the last\_seen attribute.
    * If enabled, all connections for this adapter will not fetch devices without the last\_seen attribute.
    * If disabled, all connections for this adapter will fetch devices without the last\_seen attribute.

24. **Do not fetch devices without Host Name** - Select this option to not fetch devices without a Host Name.

25. **Fetch policy posture actual settings** - Select this option to fetch policy posture actual settings.

26. **Do not populate hostname when tracking method is IP** -  Set whether to populate the device hostname field when the tracking method is IP.
    * If enabled, all connections for this adapter will not populate the device hostname field when the tracking method is IP.
    * If disabled, all connections for this adapter will populate the device hostname field.

27. **Parse Software from VM detections** - Select whether to parse installed software using the Vulnerability Management detection. When you select this option the system will parse the software from the next detections QID’s: 45453, 90235, 90295, 91228, 372899, 105310, 45141.  To implement this feature. you must also select **Enable fetching VM Detections**.

28. **Enrich vulnerabilities from detections** -  Select whether to enrich the vulnerabilities  information using results from the VM detection information for all connections for this adapter. This means it will add data from the VM detection to vulnerabilities by QID.  To implement this feature, you must also select **Fetch vulnerabilities data** and **Enable fetching VM Detections**.

29. **Parse "BIOS Serial" as "Device Manufacturer Serial"** - Select this option to parse BIOS serial numbers as device manufacturer serial numbers.

30. **Fetch VM scans** *(optional)* - Select whether to fetch VM scan information from the **/api/2.0/fo/scan/** endpoint of the connected devices. For more details, see [Qualys API User Guide (PDF), page 26](https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf).

<Callout icon="📘" theme="info">
  Note

  The Global IT Asset Inventory API is supported. When using the Global IT Asset Inventory API, the following advanced settings also fetch devices:

  * Enable fetching VM Detections

  * Fetch policy compliance

  * Fetch policy posture information

  * Fetch policy posture actual settings

  * Add STIG rules to policy posture

  * Fetch affect exploitable config from VM detection

  * Fetch affect running service from VM detection

  * Fetch affect running kernel from VM detection
</Callout>

38. **Fetch compliance scans** - Select to fetch compliance scans.

39. **Ignore devices by tracking methods** - Do not fetch devices that have one or more of the tracking methods selected from the dropdown.

40. **Do not include Public IPs in Network Interfaces** - When selected, Public IP addresses won't be included in Network Interface devices.

41. **Fetch parents' tags** - Select to fetch parent tags.

42. **Exclude packages from software (Inventory API)** - Select to exclude packages from software. This option is only relevant for the Inventory API since the data doesn't appear in the Qualys API.

43. **Fetch devices by** - Use this drop-down to fetch relevant devices with the recommended  'Last Seen Threshold'.  Either select 'Last modified' or 'Last scanned for vulnerabilities'. From version 4.8.4 the default value the first time you connect this adapter is 'Last modified'. Consult Axonius support to find the best setting for your system.

44. **Incremental fetch from last successful** - Use this setting to only fetch changes in Qualys. This needs to be configured together with an additional Qualys connection. See [Configuring Incremental Fetch](/docs/qualys-cloud-platform#configuring-incremental-fetch-optional) for more details.

45. **Fetch Hosts** *(default: true)* - Select this option to fetch additional host information for each device.

46. **VM Concurrency Limit**  - Enter a value for the system to use as the  concurrency limit (the maximum number of requests to send in one go) to access the Qualys API.

47. **Fetch vulnerabilities last seen in X days** - Enter a number of days to only fetch vulnerabilities from that number of days back.

48. **Insert QIDs without CVEs**- Select this option to fetch Qualys Vulnerabilities that only have a QID and do not have a CVE. Note that in order to see each CVE on a separate row and to present Qualys Vulnerabilities that only have QIDs you need to make sure the System Setting under Data>Cache and Performance> **Don’t split source vulnerabilities into CVEs** is not enabled.

49. **Insert both CVE and QID as Security Findings** - Select this option to fetch and parse both CVE and QID-based Security Findings. The adapter will add one Security Findings for each QID and one Security Findings for each available CVE ID.

50. **Parse System Serial from detection** - Select this option to set the Device Manufacturer Serial source to be from Qualys detections (QID: 45208).

51. **Ignore terminated EC2 instances** - Select this option to not fetch terminated EC3 instances.

52. **Ignore installed software** - Select this option to drop all installed software information from found devices.

53. **Parse domain from hostname** *(default: true)* - Select this option to parse the domain from the hostname when there is no precise domain value brought by the API.

54. **Parse only admins as last logged users** - Select this option to include only admins as possible values for the Last Logged Users field.

55. **Classify CVEs from low to critical** - Enable this option to map Qualys vulnerabilities to Axonius vulnerabilities, as follows:

* Minimal -> Info
* Medium -> Low
* Serious -> Medium
* Critical -> High
* Urgent -> Critical

<Callout icon="📘" theme="info">
  Note

  This feature is available from version 6.1.32 and later. When you enable this setting, it is recommended that you update existing queries with Qualys adapter CVE severities so that they match the newly mapped values. Otherwise, the existing queries will not be valid and will give incorrect results.
</Callout>

56. **Devices tags deny list** - Enter Qualys tags to skip device ingestion.

<Accordion title="Tickets Advanced Settings" icon="fa-info-circle">
  Enable **Edit tickets advanced settings** to edit the following settings:

  1. **Fetch Tickets as Assets** - Select this option to fetch tickets as separate assets instead of adding them to devices.
  2. **Ticket States** - Enter a list of possible ticket states.
  3. **Vulnerability Severities** - Specify the number of vulnerability severities to fetch. Only vulnerabilities with these severity numbers will be included in the ticket.
  4. **Potential Vulnerability Severities** - Specify the number of potential vulnerability severities to fetch. Only potential vulnerabilities with these severity numbers will be included in the ticket.
  5. **Modified Since X days** - Specify the number of days back to fetch modified vulnerabilities. Only vulnerabilities modified in the last X days will be included in the ticket.
</Accordion>

<Accordion title="VM Detections Settings" icon="fa-info-circle">
  **Enable fetching VM Detections** to fetch additional vulnerability management information for AWS, Azure and GCP cloud appliances.

  <Callout icon="💡" theme="warn">
    Warning

    You must enable **both** 'Enable fetching VM Detections' and 'Enrich vulnerabilities from detections' to populate the `Qualys Vulnerability: Status`, `Qualys Vulnerability: Last Fixed` and
    `Qualys Vulnerability: Status fields` on the adapter.
  </Callout>

  When you enable VM detection fetch, you can edit the following settings:

  1. **Show Information Gathering** - Select this option to show detection records with information gathered along with confirmed vulnerabilities and potential vulnerabilities.

  <Callout icon="💡" theme="warn">
    Warning

    This increases the time to fetch detection, as the API response becomes slower.
  </Callout>

  2. **Mandatory vulnerabilities QID** - Enter a list of vulnerabilities QID the adapter should try to fetch as mandatory.
  3. **Detections Statuses** - Enter a list of detection statuses to fetch.
  4. **Detections Allowed Types** - Enter a detection type to fetch. You can enter either Confirmed or Potential. If you don't enter anything, the adapter will consider all detection types as allowed and fetch them without filtering.
  5. **Fetch Disabled Detections** - Select to fetch disabled detections.
  6. **Fetch Ignored Detections** - Select to fetch ignored detections.

  #### Running Kernel Settings

  1. **Fetch running kernel** - Enable this to fetch running kernels.
  2. **Running kernel filter** - Select whether to filter kernel-related vulnerabilities, and how to filter them.

  #### Running service settings

  1. **Fetch running service** - Enable this to fetch running services.
  2. **Running service filter** - Select whether to filter service-related vulnerabilities, and how to filter them.

  #### Affect exploitable config settings

  1. **Fetch affect exploitable config** - Enable this to fetch exploitable configuration context.
  2. **Affect exploitable filter** - Select whether to filter config-related vulnerabilities, and how to filter them.
  3. **Filter superseded QIDs** - Select this to exclude outdated or superseded vulnerability IDs from fetch.
  4. **Fetch only fixed VM detections from last X days** - Set the time period in days from which to fetch fixed VM detections.
  5. **Fetch Qualys Detection Scores** - Select this to fetch the Qualys Quality Detection Scores.
</Accordion>

<Accordion title="Knowledge Base Advanced Settings" icon="fa-info-circle">
  Enable **Edit Knowledge Base Advanced Settings** to edit the following settings:

  1. **Skip Information Gathering Vulnerabilities** *(default: true)* - When checked, this checkbox ignores vulnerabilities with the type “Information Gathering.”
  2. **Vulnerabilities Details** - Select the level of vulnerability details. "Basic" includes basic elements plus CVSS Base and Temporal scores. "All" includes all vulnerability details, including the basic details.
  3. **Enrich Vulnerabilities with Qualys TruRisk** - Select this option to enrich Vulnerabilities with Qualys TruRisk score. This will add a field titled Qualys TruRisk Score to the Vulnerabilities page.
</Accordion>

<Accordion title="Reports Advanced Settings" icon="fa-info-circle">
  Enable **Edit Reports Advanced Settings** to edit the following settings:

  1. **Fetch All Authentication Reports** - Select this option to fetch all reports using the Authentication Report report type.
  2. **Fetch Compliance Reports** - Select this option to fetch all reports using the Compliance Report report type.
  3. **Number of retries when fetching devices with Module Unsupported Error. Impacts fetch time** *(default: 0)* - Set a number of retries the adapter should perform when fetching devices with a Module Unsupported Error. Note that the more retries you perform, the longer the fetch time will be.
</Accordion>

<Accordion title="Certificates Advanced Settings" icon="fa-info-circle">
  Enable **Edit Certificates advanced settings** to edit the following settings:

  1. **Fetch certificates as Certificate asset** - Select this option to fetch and parse certificates as generic assets. Note that if this and **Fetch certificates as devices** are both selected, certificates will be fetched as both Devices and Certificates generic assets, with the same data.
  2. **List CertView Certificates API Version** - Enter a CertView Certificates API version to use. The default is v1.
  3. **Certificate Details** - Set the level of certificate attributes you want to list. The default value is basic, meaning, only commonly used attributes are fetched. You can also fetch these additional attributes: Serial number, Auth Key Identifier, Subject Key Identifier, Key Usage, Base64 certificate and Enhanced Key Usage.
</Accordion>

<Accordion title="Posture Info Advanced Settings" icon="fa-info-circle">
  Enable **Edit Posture Info Advanced Settings** to edit the following settings:

  1. **Exclude inactive controls** - Select this option to include inactive controls data in the posture info fetch.

  2. **Use latest API version** - Select this option to use the latest API version when fetching Posture information. When this is enabled, the Rationale and Remediation fields are added to the Qualys Posture Info complex field. Note that this might increase fetch time.

  3. **Do not ingest posture info heavy fields** - Select this option to **not** fetch Policy Title, Control References, and Rationale from the **Qualys: Qualys Postures Info** endpoint.

  4. **Fetch specific policy compliances by ID** - Enter a specific policy ID to limit the fetch of policy compliance and posture to those related to the specified policy ID.

  5. **Fetch Agent Platform latest version** - Select to fetch the latest version of the agent platform.

  6. **Store and enrich CVE ID with QDS data** *(default: disabled)* - Select to send the enriched CVEs information to the database. Note that for this to work, you must also select **Enable fetching VM Detections** and **Fetch Vulnerabilities**.

  7. **Filter fetched Police Postures by Compliance Status** - Select compliance statuses of police postures to fetch. The options are Failed, Error, and Passed.

  8. **Parse local users from last used users** - Enable this to automatically create local user accounts based on the list of users who last logged into a device. Local user entries will be generated for users found in the device’s **Last Used Users** field. This makes it easier to capture and track local accounts that may otherwise be missed, helping you maintain a more complete and accurate user inventory.

  9. **Add Connected from IP as Network Interfaces: IPs** - Enable this to use the IP address that the device is connected from the Network Interface IP address.
</Accordion>

### Fetching Vulnerabilities

You can fetch vulnerabilities via the [Qualys API](https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf), which automatically fetches vulnerabilities by default.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>