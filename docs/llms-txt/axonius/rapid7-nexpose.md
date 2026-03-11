# Source: https://docs.axonius.com/docs/rapid7-nexpose.md

# Rapid7 Nexpose and InsightVM

Rapid7 Nexpose is an on-premise vulnerability management solution, providing discovery, detection, verification, risk classification, impact analysis, reporting and mitigation.
Rapid7 InsightVM is a cloud-based vulnerability management solution that combines Rapid7’s Insight platform along with Nexpose core capabilities.

<Callout icon="📘" theme="info">
  Notes

  * This adapter supports Rapid7 InsightVM API Version 3. If you are using  Rapid7 InsightVM API v4 use the [Rapid7 InsightVM](/docs/rapid7-insightvm) adapter.
  * This adapter works with Rapid7 Managed Threat Complete. There is an associated IP allow list.
</Callout>

## Asset Types Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Vulnerabilities.svg) Aggregated Security Findings | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Software.svg) Software | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg) SaaS Applications

## Before You Begin

### APIs

Axonius uses Rapid7 InsightVM API Version 3.

### Required Permissions

The username used to connect the adapter must have Read access to devices.

To fetch users, the Global Administrator permission is required.

### Creating User and Password Credentials in the Rapid7 Nexpose Admin Panel

**To create a read-only username and password credentials for Axonius:**

1. Connect to the Rapid7 Nexpose admin panel as an admin, and navigate to the administration panel

   <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(93).png" />

2. In the Users panel, click **Create** to create a new account for Axonius.

   <Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(94).png" />

3. From the **General** menu option, fill in the user details.
   If you have enabled Two Factor Authentication, generate a Two Factor Authentication token, to be used in the Rapid7 Nexpose adapter configuration in Axonius.

   <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(779).png" />

<Callout icon="📘" theme="info">
  Note

  To enable Two Factor Authentication:

  1. As a Global Administrator, navigate to the **Administration** tab.
  2. Click the Administer link in the Global and Console Settings section.
  3. Select Enable two factor authentication.
</Callout>

4. From the Roles dropdown, select **User**.

   <Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(96).png" />

5. From the Site Access option, select **Allow this user to access all sites**.

   <Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(97).png" />

6. From the Asset Group Access option, select **Allow this user to access all asset groups**.

   <Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(98).png" />

7. Click **Save** and login at least once to the Admin panel. The user is created.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host name** - The hostname or IP address of the Rapid7 Nexpose/InsightVM server.

2. **Port** - Use port 3780.

3. **User name** and **Password** The credentials for a user account that has the [Required Permissions](#required-permissions) to view site asset data.

### Optional Parameters

1. **Verify SSL**  - Select whether to verify the SSL certificate offered by the value supplied in **Host name**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - A proxy to use when connecting to the value supplied in **Host name**.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host name** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the value supplied in **Host name** via the value supplied in **HTTPS Proxy**.

5. **Token (for 2FA only)**
   * If supplied, Axonius will use two factor authentication when communicating with the Rapid7 Nexpose/InsightVM server. If you have enabled Two Factor Authentication, specify the Two Factor Authentication token.
   * If not supplied, Axonius will not use two factor authentication when communicating with the Rapid7 Nexpose/InsightVM server.

6. **Wait time between retries** - Specify the wait time between retries when receiving errors.

7. **Fetch tags**  - Select whether to fetch device tags from Rapid7 Nexpose/InsightVM.

8. **Fetch installed software** - Select whether to fetch installed software from Rapid7 Nexpose/InsightVM.

9. **Fetch open ports**  - Select whether to fetch open ports from Rapid7 Nexpose/InsightVM.

10. **Fetch policies**  - Select whether to fetch the policies associated with devices from Rapid7 Nexpose/InsightVM.

11. **Fetch vulnerabilities** - Select whether to fetch devices' vulnerabilities from Rapid7 Nexpose/InsightVM..

12. **Fetch vulnerabilities solutions**  - Select whether to fetch vulnerability solution names associated with devices from Rapid7 Nexpose/InsightVM.

13. **Fetch policies rules**  - Select whether to fetch the policy rules associated with devices from Rapid7 Nexpose/InsightVM.

14. **Site name exclude list** - Enter a comma-separated list of site names to be excluded from data fetch. If not supplied, Axonius will fetch devices from all site names.

15. **Number of simultaneous devices** - Set the number of simultaneous devices received from Rapid7 Nexpose/InsightVM server to gain better control on the performance of all connections of for this adapter. If not supplied, Axonius will set the number as 50.

16. **Do not fetch devices with no MAC address and no hostname**  - Select whether to exclude fetching devices without MAC address and without hostname.
    * If enabled, Axonius will only fetch devices having MAC address or hostname.
    * If disabled, Axonius will fetch devices even if those do not have MAC address and no hostname.

17. **Do not fetch vulnerabilities with status invulnerable** - Select this option to not fetch vulnerabilities whose status is ‘invulnerable’.

18. **Tag keys include list** - Enter a-comma separated list of specific tags to be fetched.

19. **Consider Tag keys include list as deny list** - Select this option to treat the values supplied for **Tag keys include list** as an **exclude list**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image border={false} src="https://files.readme.io/11e9efbb785261f7fa331243706f4b68eb52a6da17eaa20e07db189a5ea8adb4-image.png" />

<br />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Parse user accounts for devices** *(required, default: true)* - Select whether to fetch users information for fetched devices.
   * If enabled, all connections for this adapter will fetch also user information that is associated with the fetched devices. For example, **Last Used User** field.
   * If disabled, all connections for this adapter will not fetch any user information that is associated with the fetched devices.

2. **Fetch users** - Select this option to fetch data for Rapid7 InsightVM users.

3. **Use IP address as part of the Axonius ID** - Select this option to add the IP address to the device.id value.

4. **Calculate Last Seen from Agent and Scan data** - Select this option to populate the **Last Seen** field with the the greater of the two dates from the**Last Scan** and **Last Agent Import** fields.

5. **Fetch asset group data for devices** - Select this parameter to fetch asset group data from Rapid7 for device enrichment.

6. **Fetch devices excluded from scans** - Select this option to fetch assets excluded from scans. Assets include IP addresses and ranges of addresses.

7. **Don’t split source vulnerabilities into CVEs** -  Select this option to present each source vulnerability as a vulnerability of its own, represented as a single row on the vulnerability page instead of being broken down into each CVE in the vulnerability.

8. **Filter fetched devices** - Toggle on this option to filter the devices that are fetched using  InsightVM assets search filter syntax. Enter in the field an InsightVM assets search filter. Write an expression using [InsightVM search filter syntax](https://docs.rapid7.com/insightvm/performing-filtered-asset-searches/).

9. **Do not parse users as last used users** - Select this option to parse users as Users instead of Last Used Users (the default). Note that you must enable the **Fetch users** advanced configuration for this to apply.

10. **Parse Proof and Key Rich Text Fields for vulnerabilities** - Select this option to parse the Proof and Key rich text fields so that they appear in the Vulnerabilities table.

11. **Do not parse Host Name for IP values** - Select this option to avoid populating the Host Name and Secondary Hostname fields in case its value is a valid IP.

12. **Do not parse agent version from services** - Enable this to have the adapter keep only the agent version from the installed software.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Related Enforcement Actions:

[Rapid7 - Add IP Addresses to Site](/docs/add-ips-to-rapid7-insightvm-site)
[Rapid7 - Remove IP Addresses from Asset](/docs/remove-ips-from-asset)
[Rapid7 - Add or Remove Tag to/from Assets](/docs/tag-rapid7-nexpose-insightvm-assets)

## Troubleshooting

Make sure you perform monthly maintenance and tuning on your On-Premise Rapid7 Postgresql database as explained by Rapid7. This ensures optimzed Axonius fetch performance.

* [Rapid7 Configuring maximum performance in an enterprise environment](https://docs.rapid7.com/nexpose/configuring-maximum-performance-in-an-enterprise-environment/)
* [Rapid7 Planning for Capacity Requirements](https://docs.rapid7.com/nexpose/planning-for-capacity-requirements/).