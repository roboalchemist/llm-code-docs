# Source: https://docs.axonius.com/docs/microsoft-defender-atp.md

# Microsoft Defender for Endpoint (Microsoft Defender ATP)

Microsoft Defender for Endpoint (Microsoft Defender ATP) helps enterprise networks prevent, detect, investigate, and respond to advanced threats.

## Asset Types Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Alerts_Findings.svg) Aggregated Security Findings | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Software.svg) Software | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg) SaaS Applications | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Alerts_Incidents.svg) Alerts/Incidents

## Before You Begin

### Authentication Methods

* Client Credentials **OR** Managed Identity (Tenant ID)

### Required Permissions

**General Permissions**

* AdvancedQuery.Read.All
* Machine.Read.All
* Vulnerability.Read.All
* Software.Read.All
* User.Read.All

**Permissions to fetch AV information**

* AdvancedQuery.Read.All
* Application permissions

**Permissions to fetch recommendations**

* SecurityRecommendation.Read.All

**Permissions to fetch Alerts/Incidents**

* Alert.Read.All

### Configuring the Axonius App in the Microsoft Azure Portal

1. Log in to the Azure Portal with an administrator account.

2. Select **Azure Active Directory**. If you have more than one directory, verify that you are logged in to the correct directory. If you are not, select the top-right account logo and then select **Switch Directory** and select the directory you want Axonius to access.

3. Select **App registrations `>` New registration**. Fill in the details and click **Register**.

   ![NewAppDetails](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(367\).png)

4. After you have created the app, you should see its Application ID and Directory ID. Write down these values in a safe place, These values are known as Client ID and Tenant ID.

   ![ApplicationAndDirectoryID](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(368\).png)

5. In the left menu, select **Certificates & Secrets `>` New Client Secret**. Click **Add** and copy the secret.

   ![CopySecret](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(369\).png)

6. In the left menu, select **API Permissions `>` Add a permission**. Then select **APIs my organization uses** and select the WindowsDefenderATP API.

7. Add the permissions *Machine.Read.All, Vulnerability.Read.All, Software.Read.All, User.Read.All*.

8. To fetch AV information, you also need to add *AdvancedQuery.Read.All* and *AdvancedQuery.Read* permissions. Application permissions are required.

9. To fetch recommendations you also need to add *SecurityRecommendation.Read.All*.

10. To fetch Alerts you need to add  *Alert.Read.All* permissions.

11. Select **Grant admin consent for Default Directory** to apply these permissions.

    ![GrantDaminConsent](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(370\).png)

<Callout icon="📘" theme="info">
  Note

  The Defender ATP software inventory only lists and makes available via the API, software that has an official Common Platform Enumeration (CPE). The adapter cannot fetch from ATP software that is not listed in the Software Inventory, as it is not made available via the API.
  For more information, see the [ Microsoft Defender for Endpoint and ATP documentation](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/tvm-software-inventory?view=o365-worldwide).
</Callout>

## Connecting the Adapter in Axonius

### Required Parameters

1. **Authentication Method** - Select between Client Credentials and Managed Identity.
2. **Source Host Name** - Select the domain field configuration. If you access the Azure US government environment, select `api-gcc.securitycenter.microsoft.us`.

**Authenticating with Client Credentials**

1. **Client ID** - The Application ID of the Axonius application
2. **Client Secret** - A user created key for the Axonius application.

   ![ATPAddConnection\_clientcredentials](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/atp_clientcredentials.png)

**Authenticating with Managed Identity**

1. **Tenant ID** - The Azure Tenant ID, which is the directory tenant you want to request permission from. The value can be in GUID or a friendly name format. If you don't know which tenant the user belongs to and you want to let them sign in with any tenant, use `common`.

   ![ATPAddConnection\_managed identity](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/atp_managedidentity.png)

### Optional Parameters

1. **Verify SSL** - Select to verify the SSL certificate offered by Microsoft Defender for Endpoint. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - A proxy to use when connecting to  Microsoft Defender for Endpoint.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

<Callout icon="🚧" theme="warn">
  Attention

  Configuring **Advanced Settings** lengthens the time fetches take. Fetching Security Findings or SaaS Applications might take an hour or more. All other Advanced Settings might take much longer. This is due to the Defender for Endpoint configuration.
</Callout>

1. **Fetch users** - Toggle on to fetch information for users associated with fetched devices assets from Microsoft Defender for Endpoint.
   * **Fetch only interactive users** - Select whether to fetch only users that match the description of interactive in the [MDE documentation](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-devicelogonevents-table).
   * **Username regex search** - Enter one or more regex strings that can be used to identify users apart from other accounts.
2. **Fetch applications** - Select whether to fetch installed applications from Microsoft Defender for Endpoint.
3. **Fetch vulnerabilities** - Select whether to fetch devices' vulnerabilities from Microsoft Defender for Endpoint.
4. Fetch Secure Assessments configuration (Advanced Hunting Query) - Select whether to fetch data from the `DeviceTvmSecureConfigurationAssessment` table (Advanced Hunting Query).
5. **Fetch vulnerability changes** - Select whether to fetch vulnerability changes from Microsoft Defender for Endpoint.
6. **Fetch recommendations** - Select whether to fetch security recommendations from  Microsoft Defender for Endpoint.
7. **Fetch only applicable and non-compliant recommendations** - Select whether to fetch only recommendations that are applicable and non-compliant. You must also enable **Fetch recommendations** for this setting to take effect. If **Fetch only applicable and non-compliant recommendations** is disabled and **Fetch recommendations** is enabled, all recommendations are fetched.
8. **Fetch missing KBs** - Select whether to fetch missing KBs (security updates). You can choose to fetch them from either of the following sources:  **Extract from Vulnerabilities API** or **Fetch from Get Missing KBs API \[Background]**.
9. **Fetch alerts** - Select whether to fetch API DeviceAlertEvents.
10. **Fetch device AV info** - Select this option to fetch additional information about the Anti-Virus status for each device.
11. **Fetch only onboarded devices** - Select whether to only fetch devices that were onboarded.
12. **Fetch only devices with hostname** - Select this option to only fetch devices with hostname values (the field `computerDnsName` in Defender for Endpoint).
13. **Fetch sensors as Devices from Defender Identity** - Select this option to fetch Sensors as Devices. Note that you must have the `SecurityIdentitiesSensors.Read.All` permission to fetch Sensor information. This permission can be found under Microsoft Graph permissions.
14. **Ignore offline interfaces** - Select whether interfaces that have the operational status 'Down' will not be added to devices.
15. **Ignore inactive devices** - Select this option to ignore devices that have an inactive status.
16. **Fetch Devices by tag** - Toggle on this option to enter a comma separated list of tags by which to fetch devices. Only devices with the tags in the list will be fetched.
17. **Filter last logged users by domain** - Toggle on this option to filter the last logged users by domain.
    * **Allowed domains list** - Enter a comma separated list of domains from which to fetch the last logged users. This option is only available when  **Filter last logged users by domain** is enabled.
18. **Fetch discovered devices information**   - Select this option to fetch information on devices discovered by installed agents.
19. **Fetch exploited vulnerabilities**  - Select this option to fetch the fields related to vulnerability exploitation from Defender for Endpoints Plan 1 & 2.
20. **Avoid duplicate hostnames** - Select this option to consider only the latest hostname field data received by Microsoft Defender for Endpoint to avoid duplicating hostnames.
21. **Fetch Vulnerabilities seen in the last X days** *(default: 0=All)* - Define how many days back you want to fetch vulnerabilities. If you do not provide a number, the adapter fetches all vulnerabilities.
22. **Ignore loopback IPs** - Select this option to ignore IP addresses of SoftwareLoopback type.
23. **Fetch vulnerabilities as Security Findings** -  When enabled, if a vulnerability is related to multiple file paths, then multiple vulnerabilities will be parsed as Security Findings - a vulnerability for each file path.
24. **Fetch vulnerabilities remediation information** - Select to fetch remediation details for vulnerabilities. Note that this might increase fetch time.
25. **Aggregate vulns having the same cve id, software version/vendor and last seen into one record** - Select to aggregate vulnerabilities with the same CVE ID, Software Version, Software Vendor and Last Seen values into one record. This can help reduce data size.
26. **Fetch Listening Port Processes (Last Hour) | Advanced Hunting Query** - Select to fetch information about processes listening on network ports from the last hour using Advanced Hunting queries.
27. **Fetch Processes (Last Hour) | Advanced Hunting Query** - Select to fetch process execution data from the last hour using Advanced Hunting queries.
28. **Fetch Recent Executables (Last 7 Days) | Advanced Hunting Query** - Select to fetch information about executable files run in the last 7 days using Advanced Hunting queries.
29. **Fetch Suspicious DLLs (Last 1 Day) | Advanced Hunting Query** - Select to fetch information about potentially suspicious DLL files loaded in the last day using Advanced Hunting queries.
30. **Fetch Recent Kernel Events (Last 1 Day) | Advanced Hunting Query** - Select to fetch information about kernel-level events from the last day using Advanced Hunting queries.
31. **Fetch Recent Scheduled Tasks (Last 7 Days) | Advanced Hunting Query** - Select to fetch information about scheduled tasks created or modified in the last 7 days using Advanced Hunting queries.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Related Enforcement Actions

* [Microsoft Defender - Enrich Devices with MDE Client Analyzer Results](/docs/defender-atp-enrichment)
* [Offboard Assets - Microsoft Defender ATP](/docs/defender-atp-offboard)
* [Microsoft Defender ATP - Add or Remove Tag to/from Assets](/docs/defender-atp-tag-assets)
* [Microsoft Defender ATP - Isolate/Unisolate Assets](/docs/isolateunisolate-in-microsoft-defender-atp)