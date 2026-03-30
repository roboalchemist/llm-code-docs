# Source: https://docs.axonius.com/docs/sentinelone.md

# SentinelOne

SentinelOne is an endpoint protection solution including prevention, detection, and response.

### Asset Types Fetched

* Devices, Aggregated Security Findings, Users, Software, Roles, Groups, Application Settings, SaaS Applications, Alerts/Incidents

## Before You Begin

### Required API Endpoints and Permissions

#### APIs

Axonius uses the following APIs according to the asset type fetched:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Asset Type
      </th>

      <th>
        API Endpoints
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Devices
      </td>

      <td>
        * web/api/v1.6/agents
        * web/api/v1.6/agents/count
        * web/api/v2.0/agents
        * web/api/v2.1/agents
        * web/api/v2.1/device-control 'Device Controls'
        * web/api/v2.1/device-control/events 'Events'
        * web/api/v2.1/firewall-control 'Firewall Controls'
        * web/api/v2.1/xdr/assets/overview 'Last Reboot Date'
        * [https://xdr.us1.sentinelone.net/api/query](https://xdr.us1.sentinelone.net/api/query) ‘SDL Events’
      </td>
    </tr>

    <tr>
      <td>
        Users
      </td>

      <td>
        * web/api/v2.1/users
      </td>
    </tr>

    <tr>
      <td>
        Aggregated Security Findings
      </td>

      <td>
        * web/api/v2.1/application-management/risks
      </td>
    </tr>

    <tr>
      <td>
        Software
      </td>

      <td>
        * web/api/v1.6/agents/`{device_id}`/applications
        * web/api/v2.1/application-management/inventory
        * web/api/v2.1/application-management/inventory/endpoints
      </td>
    </tr>

    <tr>
      <td>
        Roles
      </td>

      <td>
        * web/api/v2.1/rbac/roles
        * web/api/v2.1/rbac/role/`{role_id}`
      </td>
    </tr>

    <tr>
      <td>
        Groups
      </td>

      <td>
        * web/api/v2.1/groups
      </td>
    </tr>

    <tr>
      <td>
        SaaS Applications + Events (Deep Visibility Events used to enrich Devices)
      </td>

      <td>
        * web/api/v2.1/dv/init-query
        * web/api/v2.1/dv/query-status
        * web/api/v2.1/dv/events
      </td>
    </tr>

    <tr>
      <td>
        Alerts/Incidents
      </td>

      <td>
        * web/api/v2.1/threats
      </td>
    </tr>

    <tr>
      <td>
        Application Settings
      </td>

      <td>
        * /web/api/v2.1/system/configuration
        * /web/api/v2.1/settings/smtp
        * /web/api/v2.1/settings/syslog
        * /web/api/v2.1/settings/sso
        * `/web/api/v2.1/sites/{site_id}/policy`
      </td>
    </tr>
  </tbody>
</Table>

#### Permissions

* To connect this adapter, you can use the default Read-Only Viewer role that provides read-only access to the system.
* When connecting with **Singularity Data Lake (SDL) API Key** (see [Optional Parameters](/docs/sentinelone#optional-parameters)), Log Read Access permission level is required.
* To fetch Application Settings, you must have Site Viewer access to the management server.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters - All Asset Types

1. **SentinelOne Domain** - The hostname or IP Address of the SentinelOne management server. This field format is `[instance].sentinelone.net`.

### Required Parameters - Application Settings

**Option 1 (Recommended):**

1. **API token** - An API token that has access to the Application Settings endpoints listed in [Required API Endpoints and Permissions](https://docs.axonius.com/docs/sentinelone#required-api-endpoints-and-permissions).

**Option 2 - When using API token is impossible or insufficient:**

When you don't have an API token, or when the token cannot access certain settings, the fetch will fail and you will be prompted to provide the following parameters:

1. **User Name** and **Password** - The credentials for an account that has site viewer access to the management server. For information on how to create users in SentinelOne, see [Create a Single User](https://euce1-100.sentinelone.net/docs/en/creating-a-single-user.html#creating-a-single-user).
2. **2FA Secret Key** - The secret generated in SentinelOne for setting up 2-factor authentication.
   <Accordion title="Setting uo 2-factor authentication in SentinelOne" icon="fa-info-circle">
     1. Log in to SentinelOne.
     2. After entering the user name and password, the 2FA page displays a QR Code and a token. Copy the token.
     3. On the adapter’ **Add Connection** section in Axonius, click the **Generate Secret Key** icon from the **2FA Secret** field.<br />
        ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-1CWEX57L.png)
     4. The Set 2FA Secret Key screen opens. Enter the copied token into the 2FA Secret Key field and click **Next**.<br />
        ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-98C3U38F.png)
     5. Click the Copy icon to copy the 6-digit code displayed.<br />
        ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-HD8QO8UL.png)
     6. On the **SentinelOne Two-Factor Authentication** screen, paste the code in the appropriate field and click **Continue**.<br />
        ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-NXVDOPZB.png)
     7. Back in Axonius, click **Complete** in the Set 2FA Secret Field dialog.
     8. Click **Save**.
   </Accordion>

<Image align="center" width="auto" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-8HAK6PNI.png" height="auto" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **Singularity Data Lake (SDL) API Key** - To enable SDL queries in the Advanced Settings, enter the API Key from the Singularity Data Lake. Note: this requires Log Read Access permission.
4. **Enable Client Side Certificate** - Select to enable Axonius to send requests using the certificates uploaded to allow Mutual TLS configuration for this adapter. If you enable Mutual TLS on your SentinelOne environment, this parameter is required.

   1. Click **Upload File** next to **Client Private Key File** to upload a client private key file in PEM format.
   2. Click **Upload File** next to **Client** **Certificate File** to upload a public key file in PEM format.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note:

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch applications** - Select to fetch SentinelOne applications.

<Callout icon="💡" theme="warn">
  Note

  To fetch SentinelOne applications, you must configure **Application Scanning** in your SentinelOne environment. This is relevant for every Axonius version starting from 6.1.13.
</Callout>

2. **Fetch application CVEs** - Select whether to fetch CVE security vulnerability information for software.

<Callout icon="🚧" theme="warn">
  Note

  SentinelOne can also fetch non-CVE threats and parse them into the Security Findings table. To enable this capability, contact Axonius support.
</Callout>

2. **Ignore vulnerabilities from ubuntu packages** - Select to ignore vulnerabilities of software detected as an ubuntu package.
3. **Fetch decommissioned devices** - Select whether to fetch devices that are decommissioned.

<Callout icon="💡" theme="warn">
  Note

  To fetch decommissioned devices, you must have the Endpoints View Credentials permission.
</Callout>

5. **Fetch threats for infected devices** - Select this option to fetch threats of a device when the infected value on the SentinelOne server is set to True. When you enable this setting, the adapter also fetches MITRE ATT\&CK techniques from threat indicators to the device.
6. **Fetch threats only for selected incident statuses** - Select which threat incident statuses should be fetched: Unresolved, In Progress, or Resolved. (You can select more than one)
7. **Fetch device control events** - Select this option to fetch the device control events for each device.
8. **Fetch Application settings** - Select this option to fetch application settings for users.
9. **Fetch last installed software version only** - Select this option to fetch only the version with the most recent installed date for each software.
10. **Deep Visibility query** - Enter a SentinelOne Deep Visibility query name to fetch the query events and parse them inside the devices as “Deep Visibility Events“.
11. **Remove old tags** - Select this option to remove old tags that are no longer being fetched from SentinelOne.
12. **Background fetch tasks** - Select tasks from the drop-down that will be fetched in the background.
13. **Background fetch interval (Hours)** *(default: 72 (3 days))* - Set the interval in hours for background fetch.
14. **Background fetch data maximum age** **(Days)** *(default: 7 days)* - Select this option to limit the maximum age of data retrieved during background fetches.
15. **Enable fetch from Skylight query** - Toggle on to enable fetch from the Skylight query.

<Callout icon="💡" theme="warn">
  Note

  When **Enable fetch from Skylight query** is enabled, enter the SDL query to fetch events. This requires you to configure the **Singularity Data Lake (SDL) API Key** parameter and have the Log Read Access permission.
</Callout>

15. **Ignore public IPs from externalIp field** - Select this option to ignore public IPs from the externalIp field.
16. **Fetch uninstalled devices from V1** - Select this option to fetch uninstalled devices from V1.
17. **Parse Device Model without Manufacturer info** - Select this option to parse the device model field without the manufacturer information in the model name.
18. **Enable real-time asset updates (Supported events: Recently activated devices)** - Enable this option to fetch devices that have been recently activated and to trigger the respective event. All workflows configured with this event are then triggered.
19. **Fetch users** - Uncheck this to disable user fetch.
20. **Fetch Last Reboot Date** - Enable to fetch and display the Last Reboot Date for SentinelOne devices. The adapter will collect this information from an additional endpoint.
21. **Deduplicate devices by computer name and keeping greater agent version** - Select this option to avoid fetching the same device with several agent versions by keeping the device with the latest agent version. The adapter will use the device’s "computer name" as the key to index data. Note that this process might increase disk usage and fetch time.
22. **Fetch firewall rules** - Enable to fetch firewall rules for Devices. The results are written into the **Firewall Rules** table on the Device's Profile page.
23. **Fetch pending third-party application patches** - Select to fetch OS Available Security Patches detected in third-party applications that are installed on devices.
24. **Fetch ransomware detections** - Select to fetch ransomware detections, the results will be parsed into the device's Ransomware Detection field.
25. **Enrich devices with Deep Visibility events** - Add Deep Visibility events you want to enrich Device data with. You can select more than one option from the menu.
    * **Last Interactive User Logons: timeframe (days)** *(default: 10)* - Set the number of days to look back for to enrich devices with interactive user logons.

<Callout icon="📘" theme="info">
  Note:

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Related Enforcement Actions

[SentinelOne - Add or Remove Tag to/from Assets](/docs/tag-in-sentinelone)

[SentinelOne - Initiate Scan](/docs/initiate-sentinelone-scan)

[SentinelOne - Remove Asset](/docs/sentinelone-remove-asset)

[SentinelOne - Execute Remote Script Orchestration](/docs/sentinelone-execute-remote-script)

[SentinelOne - Isolate/Unisolate a Device](/docs/sentinelone-isolate-unisolate-assets)

[SentinelOne - Change Asset Site](/docs/sentinelone-change-site)

[SentinelOne - Change Asset Group](/docs/sentinelone-change-group)

[SentinelOne - Send Broadcast Message](/docs/sentinelone-send-broadcast-msg)

[SentinelOne - Enable Or Disable Agent](/docs/sentinelone-enable-disable-agent)