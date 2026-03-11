# Source: https://docs.axonius.com/docs/defender-gcc.md

# Microsoft Defender for Endpoint for GCC

Microsoft Defender for Endpoint for GCC helps enterprise government networks prevent, detect, investigate, and respond to advanced threats.

<br />

### Asset Types Fetched

* Devices, Aggregated Security Findings, Users, Software, SaaS Applications, Alerts/Incidents

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Tenant ID
* Client ID/Client Secret

### Permissions

The AdvancedQuery.Read.All permissions are required for basic Microsoft Defender for Endpoint configuration.

## Configuring the application in the Microsoft Azure portal

1. Log in to the Azure Portal with an administrator account.

2. Select **Azure Active Directory**. If you have more than one directory, verify that you are logged in to the correct directory. If you are not, select the top-right account logo and then select **Switch Directory** and select the directory you want Axonius to access.

3. Select **App registrations `>` New registration**. Fill in the details and click **Register**.

   <Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1023)(367).png" />

4. After you have created the app, you should see its Application ID and Directory ID. Write down these values in a safe place, These values are known as Client ID and Tenant ID.

   <Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1023)(368).png" />

5. In the left menu, select **Certificates & Secrets `>` New Client Secret**. Click **Add** and copy the secret.

   <Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1023)(369).png" />

6. In the left menu, select **API Permissions `>` Add a permission**. Then select **APIs my organization uses** and select the WindowsDefenderATP API.

7. Add the permissions *Machine.Read.All, Vulnerability.Read.All, Software.Read.All, User.Read.All*.

8. To fetch AV information, you also need to add *AdvancedQuery.Read.All* and *AdvancedQuery.Read* permissions. Application permissions are required.

9. To fetch recommendations you also need to add *SecurityRecommendation.Read.All*.

10. To fetch Alerts you need to add  *Alert.Read.All* permissions.

11. Select **Grant admin consent for Default Directory** to apply these permissions.
    ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(370\).png)

<br />

<Callout icon="📘" theme="info">
  **Note**

  The Defender ATP software inventory only lists and makes available via the API, software that has an official Common Platform Enumeration (CPE). The adapter cannot fetch from ATP software that is not listed in the Software Inventory, as it is not made available via the API.
  For more information, see the [ Microsoft Defender for Endpoint and ATP documentation](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/tvm-software-inventory?view=o365-worldwide).
</Callout>

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Source Host Name** *(default: api-gcc.securitycenter.microsoft.us)* - Select the domain field configuration. If you access the GCC High & DOD, select **api-gov.securitycenter.microsoft.us**
2. **Tenant ID**  - The Azure Tenant ID.
3. **Client ID** - The Application ID of the Axonius application
4. **Client Secret** - A user created key for the Axonius application.

<Image alt="Microsoft Defender for Endpoint for GCC Connection Screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/MicrosoftDefenderforEndpointforGCC.png" />

### Optional Parameters

1. **Custom Scope** - Add a custom scope to be used when requesting data from the Microsoft API. See these examples for the format the scope should be in: `https://securitycenter.onmicrosoft.com/windowsatpservice`, `https://api-gcc.securitycenter.microsoft.us`, `https://api-gov.securitycenter.microsoft.us`.
2. **Verify SSL** - Select to verify the SSL certificate offered by Microsoft Defender for Endpoint. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
3. **HTTPS Proxy**  - A proxy to use when connecting to  Microsoft Defender for Endpoint.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  **Note**

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

<Callout icon="📘" theme="info">
  **Note**

  Defender for Endpoint configuration can extend fetch time for advanced settings.
</Callout>

1. **Fetch users**  - Select whether to fetch information for users associated with fetched devices assets from  Microsoft Defender for Endpoint.
2. **Fetch applications** - Select whether to fetch installed applications from  Microsoft Defender for Endpoint.
3. **Fetch vulnerabilities** - Select whether to fetch devices' vulnerabilities from Microsoft Defender for Endpoint.
4. **Fetch alerts** - Select whether to fetch API DeviceAlertEvents.
5. **Fetch device AV info** - Select this option to etch additional information about the Anti-Virus status for each device.
6. **Fetch only onboarded devices** - Select whether to only fetch devices that were onboarded.
7. **Ignore offline interfaces**  - Select whether interfaces that have the operational status 'Down' will not be added to devices.
8. **Ignore inactive devices** *(optional)* - Select whether to ignore devices that have an inactive status.
9. **Filter last logged users by domain** - Toggle on this option to filter the last logged users by domain.
   * **Allowed domains list** - Enter a comma separated list of domains from which to fetch the last logged users. This option is only available when  **Filter last logged users by domain** is enabled.
10. **Fetch discovered devices information**  - Select this option to fetch information on devices discovered by installed agents.

<Callout icon="📘" theme="info">
  **Note**

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>