# Source: https://docs.axonius.com/docs/infoblox.md

# Infoblox DDI

Infoblox DDI consolidates DNS, DHCP, IP address management, and other core network services into a single platform, managed from a common console.

<Callout icon="🚧">
  For on-prem Infoblox NIOS use this adapter
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Domains & URLs, Networks

## Parameters

1. **Infoblox Domain** *(required)* - The hostname or IP address of the Infoblox DDI server.
2. **API version** *(required, default: 2.5)* - Select the API version from the dropdown.

<Callout icon="📘" theme="info">
  Note

  Additional discovery device objects are fetched, depending on the API version selected. For example, fetching chassis serial number information requires configuring at least API version 2.10.5 and selecting that version from the **API version** dropdown.
</Callout>

3. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate offered by the value supplied in **Infoblox Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Infoblox Domain**.

6. **API Gateway Connection** *(optional)* - Enable this to use API gateway parameters for authentication. After enabling this option, under **API Gateway Type**, choose **Layer7** and fill in the parameters that are displayed (in addition to **Infoblox Domain**). Read about [Layer7 API Gateway Parameters](/docs/adding-a-new-adapter-connection#layer7-api-gateway-parameters).

<Callout icon="📘" theme="info">
  Note

  When you use an API gateway connection, the other authentication parameters are not required. However, to add the connection successfully, you need to enter placeholder values in these fields.
</Callout>

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Infoblox DDI" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-BN9OIU5M.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **CIDR exclude list** *(optional)* - Specify a comma-separated list CIDR blocks to exclude (for example: 192.168.20.0/24,192.168.30.0/24).

2. **CIDR include list** *(optional)* - Specify a comma-separated list of CIDR blocks to include (for example: 192.168.20.0/24,192.168.30.0/24).

3. **Fetch using Infoblox database download** - Select this option to reduce fetch time by downloading a backup of the database instead of making API requests. Note that admin permissions are required for this option. This option only applies to the DHCP Lease and DNS Host Record asset types, the other asset types are still fetched via API requests.

4. **Filter results by the Discovered Data field** - Specify whether to collect devices from Infoblox if their Discovered Data field has data.

5. **Results per page** *(required, default: 1000)* - Set the number of results per page received for a given query to the Infoblox wAPI, to gain better control on the performance of all connections for this adapter.

6. **Time in seconds to sleep between each request** *(optional)* - Specify sleeping time in seconds between each API request Axonius sends to Infoblox.

7. **Fetch lease information** *(required, default: true)* - Select whether to fetch information from the 'lease' API endpoint. The 'lease' API endpoint is slower than 'ipv4address' API endpoint, but fetches much more information like 'Fingerprint' and discovery information.

8. **Fetch networks as assets** - Select whether to fetch Infoblox networks as assets.

9. **Fetch DHCP ranges** - Select whether to fetch DHCP address ranges.

10. **Fetch used addresses information** - Select whether to fetch information from the 'ipv4address’ API endpoint. The 'ipv4address’ API endpoint is faster than the 'lease' API endpoint.

11. **Fetch A records** - Select whether to fetch A records from Infoblox.

12. **Fetch shared A records** - Select whether to fetch shared A records from Infoblox.

13. **Fetch CNAME records** - Select whether to fetch DNS CNAME records.

14. **Fetch HOST records** - Select whether to fetch data from WAPI/record:host

15. **Fetch fixed addresses** - Select whether to fetch data from WAPI/fixedaddress

16. **Fetch discovery device objects** *(optional)* - Select to fetch discovery device objects.  Additional discovery device objects are fetched, depending on the API version selected.

17. **Fetch DNS Members** - Select to fetch data from WAPI/member:dns.

18. **Fetch IPAM statistics** - Select to fetch data from WAPI/ipam:statistics.

19. **Do not parse Last Seen of A Records** - Select to not parse Last Seen of A Records.

20. **Ignore A records discovered by NetMRI** - Select to ignore A records discovered by NetMRI. If cleared, the adapter connection will fetch all A records if the **Fetch A records** is enabled.

21. **Use start time as last seen** - Select to set the device **Last Seen** field value based on the fetched device's DHCP start time. If cleared, the adapter connections will use the fetched device's DHCP end time.

<Callout icon="📘" theme="info">
  Note

  If **Use start time as last seen** is selected, you must also select **Fetch lease information**.
</Callout>

22. **Include lease states** *(optional)* - By default, the following lease states of devices are not fetched: ‘ABANDONED', ‘BACKUP', 'EXPIRED', 'FREE', 'RELEASED'. If you want to include one or more of these lease states in the fetch, select the relevant lease states from the dropdown.
23. **Skip records without Hostname and MAC Address** - By default the system skips records without Hostname and MAC Address, clear this option to not skip records without both a Hostname and a MAC Address.
24. **Merge device records by MAC address** - Select to merge records that have the same MAC address. A new device asset will be created, containing the data from each Infoblox asset. This setting can also help with correlation by minimizing the number of records correlated together.
25. **Ignore all devices without last seen value** - Select to ignore all devices without last seen value.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses [Infoblox APIs](https://www.infoblox.com/developer-portal/developer-portal-api-documentation/).

## Required Permissions

The value supplied in [Username](#parameters) must have at least Read-only permissions to access the devices.
**To create a user with Read-only permissions**

1. Login to Infoblox as an administrator and select  **Administration** `>` **Roles**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(76\).png)
2. Click the **Plus sign** on the right part of the page to add a new role.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(77\).png)
3. Give this role an indicative name, and click **Next**. In the **Extensible Attributes** page, click **Next** again, then click **Save & Add Permissions**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(78\).png)
    
4. In the **Permissions** page, click the **Plus sign** to add permissions to the newly-created role.
   Axonius needs read-only permissions to the items displayed in the image. Select them and click **Save & Close**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(79\).png)
5. Navigate to "Groups" and click the **Plus sign** to create a new group.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(80\).png)
6. Specify an indicative name for this group, and click **Next**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(81\).png)
7. Select the **API** option to enable API access for this group, and click the **Plus sign** to add a role to it.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(82\).png)
8. Navigate to **Custom Roles** and click the newly created role.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(83\).png)
9. Verify that the role is currently displayed in the Roles list. Verify that **"API"** is selected, and click **Save & Close**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(84\).png) 
10. Click the newly created group, and then click the **Plus sign** to create a new user. Fill in the details and click **Save & Close**.
    ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(85\).png)